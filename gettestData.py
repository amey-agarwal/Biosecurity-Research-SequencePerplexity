from src.fetch_ncbi import fetch_ncbi_cds, build_synthetic_construct_query
from src.parse_ncbi import parse_ncbi_fasta
from src.shuffle import shuffle_sequence

def fetchNCBISeq():
    path = fetch_ncbi_cds("Escherichia coli", email="ameyagarwal10@gmail.com", retmax=30)
    rows = parse_ncbi_fasta(path, "Escherichia coli")

    natural_seq = rows[0]["sequence"]
    shuffled_seq = shuffle_sequence(natural_seq)
    print(natural_seq)
    print(shuffled_seq)

def fetchSyntheticNCBISeq():
    path = fetch_ncbi_cds("synthetic construct", email="ameyagarwal10@gmail.com",
                       retmax=30, query=build_synthetic_construct_query())
    rows = parse_ncbi_fasta(path, "synthetic construct", source="engineered")

    natural_seq = rows[0]["sequence"]
    shuffled_seq = shuffle_sequence(natural_seq)
    print(natural_seq)
    print(shuffled_seq)

# fetchNCBISeq()
# fetchSyntheticNCBISeq()

def interrogateTestData_print_id():
    rows = parse_ncbi_fasta("data/raw/ncbi/Escherichia_coli.fasta", "Escherichia coli")
    clean_ids = {r["id"] for r in rows}
    print(len(clean_ids), "clean out of however many were in the file")
    for i in clean_ids:
        print(i)

# interrogateTestData_print_id()

def verifyTestData(fasta_filepath): #sequence correct?
    seqs = {}
    cur = None
    with open(fasta_filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                cur = line[1:]
                seqs[cur] = ''
            else:
                seqs[cur] += line.upper()

    for desc, seq in seqs.items():
        n = len(seq)
        mult3 = n % 3 == 0
        start_ok = seq.startswith('ATG')
        stop_codon = seq[-3:]
        stop_ok = stop_codon in ('TAA','TAG','TGA')
        codons = [seq[i:i+3] for i in range(0, n-2, 3)]
        internal_stops = sum(1 for c in codons[:-1] if c in ('TAA','TAG','TGA'))
        print(f'{desc[:45]:45s} len={n:5d} mult3={str(mult3):5s} start_ATG={str(start_ok):5s} stop={stop_codon}({str(stop_ok):5s}) internal_stops={internal_stops}')

# fetchNCBISeq()
# fetchSyntheticNCBISeq()

# interrogateTestData_print_id()

verifyTestData('data/raw/ncbi/Escherichia_coli.fasta')
