"""Extract and classify every citation in the supplied IM bibliography.

This is a transparent topic map, not a claim that every paywalled paper was read
in full. Classification is based on the citation title and publication type.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "pdfs" / "IM-RESEARCH-BIBLIOGRAPHY.pdf"
OUTPUT = ROOT / "research_catalog.csv"

CATEGORIES = [
    ("ADHD and attention", ("adhd", "attention", "attentional", "impuls")),
    ("Autism and social timing", ("autis", "social timing", "interpersonal synchron")),
    ("Stroke, gait and rehabilitation", ("stroke", "gait", "walking", "hemipares", "parkinson", "rehabilitation", "motor recovery")),
    ("Language, reading and auditory processing", ("reading", "dyslex", "language", "speech", "phonolog", "auditory processing")),
    ("Motor timing and coordination", ("motor", "rhythm", "timing", "coordination", "synchron", "metronome", "movement")),
    ("Working memory and executive function", ("working memory", "executive", "cognitive control", "intelligence", "memory")),
    ("Time perception and neuroscience", ("time perception", "temporal", "brain", "neural", "cortex", "cerebell", "fMRI")),
]


def normalize(value: str) -> str:
    value = value.replace("\r", " ").replace("\u00a0", " ").replace("\u00ad", "")
    value = value.replace("‐", "-").replace("–", "-")
    return re.sub(r"\s+", " ", value).strip()


def entries(section: str, maximum: int) -> list[tuple[int, str]]:
    chunks = re.split(r"(?m)^\s*(?=\d+\.\s)", section)
    found: list[tuple[int, str]] = []
    for chunk in chunks:
        item = normalize(chunk)
        match = re.match(r"^(\d+)\.\s*(.+)$", item)
        if not match:
            continue
        number = int(match.group(1))
        if number <= maximum:
            found.append((number, match.group(2)))
    # Page numbers occasionally appear as false list items; retain one citation per expected number.
    unique = {number: citation for number, citation in found}
    return sorted(unique.items())


def category(citation: str) -> str:
    lower = citation.lower()
    scored = [(sum(term in lower for term in terms), label) for label, terms in CATEGORIES]
    score, label = max(scored)
    return label if score else "General cognition, learning and measurement"


def evidence_type(citation: str) -> str:
    lower = citation.lower()
    if "meta-analysis" in lower or "review" in lower:
        return "Review or synthesis"
    if "randomized" in lower or "randomised" in lower:
        return "Randomized study"
    if "case" in lower or "a 9-year-old" in lower or "an adolescent" in lower:
        return "Case report or case study"
    if "white paper" in lower or "conference" in lower or "unpublished" in lower:
        return "Grey literature"
    if "manual" in lower or "technical" in lower:
        return "Test or technical reference"
    return "Journal article or book reference"


def implication(topic: str) -> str:
    return {
        "ADHD and attention": "Use short tasks, simple cues, optional challenge, and avoid attention-treatment claims.",
        "Autism and social timing": "Offer predictable sensory controls and strengths-based rhythm practice; do not target core traits.",
        "Stroke, gait and rehabilitation": "Allow clinician-selected movements; gait and balance activities require supervision.",
        "Language, reading and auditory processing": "Do not infer reading or language gains from improved tapping timing.",
        "Motor timing and coordination": "Provide immediate early/late feedback and direct within-person timing measures.",
        "Working memory and executive function": "Keep cognitive load adjustable and separate task performance from transfer claims.",
        "Time perception and neuroscience": "Use timing theory to guide measurement, not as proof of clinical effectiveness.",
        "General cognition, learning and measurement": "Treat as contextual evidence unless a direct intervention effect is established.",
    }[topic]


def main() -> None:
    raw = "\n".join(page.extract_text() or "" for page in PdfReader(SOURCE).pages)
    direct_raw, supporting_raw = raw.split("SUPPORTING RESEARCH REFERENCES", 1)
    rows = []
    for section, items in (("IM-specific", entries(direct_raw, 21)), ("Supporting", entries(supporting_raw, 179))):
        for number, citation in items:
            topic = category(citation)
            rows.append({
                "section": section,
                "number": number,
                "citation": citation,
                "topic": topic,
                "evidence_type_inferred_from_citation": evidence_type(citation),
                "product_implication": implication(topic),
                "review_status": "Citation/title classified; consult full text before clinical claims",
            })
    if len(rows) != 200:
        raise RuntimeError(f"Expected 200 references, extracted {len(rows)}")
    with OUTPUT.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} references to {OUTPUT}")


if __name__ == "__main__":
    main()
