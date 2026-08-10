from Bio import Entrez


def fetch_taxon_record_count(taxon: str, email: str) -> int:
    Entrez.email = email
    query = f"{taxon}[Organism] AND biomol_genomic[PROP]"
    search = Entrez.esearch(db="nuccore", term=query, retmax=0)
    result = Entrez.read(search)
    search.close()
    return int(result["Count"])
