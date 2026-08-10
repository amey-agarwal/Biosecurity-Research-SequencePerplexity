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

> Sequences ? 
===> Websites can be NCBI and Addgene (Common websites used)
===> NCBI nuccore database pinged using Biopython Entrez (standard, rate-compliant - NCBI doesn't allow raw scrapers and will get you IP Blocked) (trusting Claude to not get IP blocked)

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
