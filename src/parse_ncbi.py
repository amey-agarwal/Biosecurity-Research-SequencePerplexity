from Bio import SeqIO


def parse_ncbi_fasta(path: str, taxon: str, n_threshold: float | None = None) -> list[dict]:
    rows = []
    total = 0
    for record in SeqIO.parse(path, "fasta"):
        total += 1
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
            "source": "ncbi_natural",
            "taxon": taxon,
            "length": length,
            "gc_content": gc,
        })

    if n_threshold is not None:
        print(f"{taxon}: {total} -> {len(rows)} sequences after N-content filter (threshold={n_threshold})")

    return rows
