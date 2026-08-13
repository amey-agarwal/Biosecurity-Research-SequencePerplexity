from src.fetch_ncbi import fetch_ncbi_cds
from src.parse_ncbi import parse_ncbi_fasta
from src.shuffle import shuffle_sequence

path = fetch_ncbi_cds("Escherichia coli", email="ameyagarwal10@gmail.com", retmax=5)
rows = parse_ncbi_fasta(path, "Escherichia coli")

natural_seq = rows[0]["sequence"]
shuffled_seq = shuffle_sequence(natural_seq)
print(natural_seq)
print(shuffled_seq)
