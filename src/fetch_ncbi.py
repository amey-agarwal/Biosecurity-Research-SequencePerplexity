import os
from Bio import Entrez


def build_ncbi_query(taxon: str) -> str:
    return f"{taxon}[Organism] AND biomol_genomic[PROP] AND srcdb_refseq[PROP] AND cds[FKEY]"


def build_synthetic_construct_query() -> str:
    return '"synthetic construct"[Organism] AND biomol_genomic[PROP] AND cds[FKEY]'


def fetch_ncbi_cds(taxon: str, email: str, retmax: int = 50, out_dir: str = "data/raw/ncbi", query: str | None = None) -> str:
    Entrez.email = email
    if query is None:
        query = build_ncbi_query(taxon)

    search = Entrez.esearch(db="nuccore", term=query, retmax=retmax)
    ids = Entrez.read(search)["IdList"]
    search.close()

    if not ids:
        raise ValueError(f"No NCBI records found for taxon: {taxon}")

    fetch = Entrez.efetch(db="nuccore", id=ids, rettype="fasta_cds_na", retmode="text")
    raw_fasta = fetch.read()
    fetch.close()

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{taxon.replace(' ', '_')}.fasta")
    with open(out_path, "w") as f:
        f.write(raw_fasta)

    return out_path
