# Can the Bio model give low likelihood scores of sequence relevance to the training composition?

If a gene sequence has low sequence relevance to the training composition but high functionality, then it can be engineered (and potentially harmful), or it is an underrepresented or newly found gene that the model isn't trained on. 


Biosecurity risk; AI safety 

Making a graph with low and high functional scores on the y-axis and probability on the x-axis.
Square means well-studied, triangle means understudied.
Red colour: engineered; green colour: natural. 

Red square: well-studied engineered 
Red triangle: understudied engineered (MAIN FOCUS)
Green square: well-studied natural (SHOULD BE WELL PLACED); 
Green triangle: understudied natural (alternate hypothesis)

API request that works 
Check the Predict options - https://api.biolm.ai/#f300f7c8-cbb7-44f9-92ce-36c72bbba5f9
POST Evo 2 1B Base -> Predict

Questions that I should get answers to 
1. What inputs is the model trained on? 
2. Simple architecture and working of the model
3. How does sequence log probability inferencing work? 

International Gene Synthesis consortium helps to check if a particular gene is of concern. This is the baseline. If it works well for every engineered gene, then it is a good baseline and can be used for checking engineered genes, doesn't work well, then it can be argued against. 

Every single choice gets logged
How do you know this? (e.g. Claude told you, learnt from project experience)
> Model ? 
===> top-level model, less compute and API access, (Project Exp)
===> control setup to use other models, HyenaDNA or Nucleotide Transformer, on free Colab

> Coverage
==> confused with representation (how well that sequence is studied in database)
==> how well a base has been read is coverage

Progress flow

1. I need to fetch data
write src/fasta_ncbi.py : use Entrez and efetch function for server-side filtering of coding regions

2. need to parse the fetched data - assimilating into file with rows
src/parse_ncbi.py : SeqIO.parse cause different fasta files different comment lines, manual GC content value findng, OPTIONALLY removing sequences with N's more than 1%. 

3. how much data should i fetch?
Several taxa, 50 sequences for each taxa.
src/representation.py : number of sequence of the taxa being imported

4. What model am I using ? 
Nucleotide Transformer fr free tier 
Evo2 if everything works fine (paid tier API)

what is the relevance of this data to the model ?

# Problems and Solutions
1. I don't want to get IP blocked making random calls to NCBI; 
> Use Entrez and Biopython

2. Different files different comments different code to manage it;
> SeqIo.parse does my job of fasta parsing robustly

3. There might be N's in sequence, these are redundant but still part of sequence;
> threshold as < 0.01 for #of N in sequence length

4. The taxa I get; one might be in large number as compared to other; need to keep a fixed low threshold for the species
> 50 for each taxa

5. The model API calls may get inflated and up the costs, need to run a mock method of the project and check
> crop the sequences to a fixed length [BIGGEST CAVEAT]; masked parts of the sequence that the model is asked to predict? ; NT used for start,later use Evo2

6. jaxlib dependency error - pip install for nucleotide_transformer pulled a corresponding jaxlib dependency that was incompatible with the Colab framework. 
> !pip install -U "jax[cuda12]" and restart the session

7. HF_TOKEN warning - recommendatoin to use token in ntoebook run
> COLAB secrets

8. Nucleotde transformer tokenises in non-overlapping 6-mers
> Had to run model to check the logits obtained (2, 32, 4017); managed by understanding the logits

9. SSL error
> pip install --upgrade certifi && export SSL_CERT_FILE=$(python3 -m certifi)

10. Fasta file reading errors
> parse_ncbi.py parsing the fasta file

11. Addgene paid and access tough

12. NCBI synthetic construct is natural gene with (transposon?) insertions - wrong category of comparison

13. iGEM has category for each constructed sequence - experience 'Works' and is Coding sequence

14. Sequence may seem correct but should end in a stop codon, be a multiple of 3 and not have any stop codons in the sequence before the last codon.
