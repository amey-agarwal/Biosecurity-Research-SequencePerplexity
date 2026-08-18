import io
import re
from Bio import SeqIO


def _is_low_quality_cds(description: str) -> bool:
    if "[pseudo=true]" in description:
        return True
    location = re.search(r"\[location=([^\]]*)\]", description)
    if location and ("<" in location.group(1) or ">" in location.group(1)):
        return True
    return False


def parse_ncbi_fasta(path: str, taxon: str, n_threshold: float | None = None, source: str = "ncbi_natural") -> list[dict]:
    with open(path) as f:
        lines = f.readlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(">"))
    cleaned = "".join(line for line in lines[start:] if line.strip())
    handle = io.StringIO(cleaned)

    rows = []
    total = 0
    skipped_quality = 0
    for record in SeqIO.parse(handle, "fasta"):
        total += 1
        if _is_low_quality_cds(record.description):
            skipped_quality += 1
            continue

        seq = str(record.seq).upper()
        length = len(seq)
        if length == 0:
            continue

        n_count = seq.count("N")
        if n_threshold is not None and n_count / length > n_threshold:
            continue

        non_n_length = length - n_count
        if non_n_length == 0:
            continue
        gc = sum(1 for base in seq if base in "GC") / non_n_length * 100

        rows.append({
            "sequence": seq,
            "source": source,
            "taxon": taxon,
            "length": length,
            "gc_content": gc,
        })

    print(f"{taxon}: {total} -> {total - skipped_quality} after pseudogene/partial-CDS filter ({skipped_quality} skipped)")
    if n_threshold is not None:
        print(f"{taxon}: {total - skipped_quality} -> {len(rows)} sequences after N-content filter (threshold={n_threshold})")

    return rows
