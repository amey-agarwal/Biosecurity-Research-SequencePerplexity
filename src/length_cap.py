def percentile_length_cap(lengths: list[int], percentile: float = 90) -> int:
    sorted_lengths = sorted(lengths)
    idx = min(int(len(sorted_lengths) * percentile / 100), len(sorted_lengths) - 1)
    return sorted_lengths[idx]


def apply_length_cap(rows: list[dict], cap_bp: int) -> list[dict]:
    counts_before = {}
    counts_truncated = {}
    for row in rows:
        source = row["source"]
        counts_before[source] = counts_before.get(source, 0) + 1
        row["scored_length"] = row["length"]
        if row["length"] > cap_bp:
            counts_truncated[source] = counts_truncated.get(source, 0) + 1
            row["sequence"] = row["sequence"][:cap_bp]
            row["scored_length"] = cap_bp

    for source, total in counts_before.items():
        truncated = counts_truncated.get(source, 0)
        print(f"{source}: {truncated}/{total} sequences truncated to {cap_bp}bp")

    return rows
