from Bio import Entrez

from src.fetch_ncbi import build_ncbi_query


def fetch_taxon_record_count(taxon: str, email: str) -> int:
    Entrez.email = email
    query = build_ncbi_query(taxon)
    search = Entrez.esearch(db="nuccore", term=query, retmax=0)
    result = Entrez.read(search)
    search.close()
    return int(result["Count"])
