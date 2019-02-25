# Exercises with the Drosophila melanogaster Chromosome 4
02-13-19:

## Translate cds file to a pep file
A cds file contains the nucleotide sequence. This nucleotide sequence is one that is translated to amino acids
Therefore, it already has introns and UTRs removed
- In this directory, you should find the cds file for Chromosome 4

- In the programming language of your choice:
  - Read in this cds file
  - Convert each codon to an amino acid
  - Write the converted sequence out to a new file

02-25-19:

## List genes in given interval from GFF file
<i>Drosophila melanogaster</i> General Feature Format (GFF) file:
- Drosophila_melanogaster.BDGP6.95.chromosome.4.gff3
Info on GFF file:
- https://useast.ensembl.org/info/website/upload/gff.html
- In the programming language of your choice:
  - Read in GFF file
  - Specify genomic range on the cmd line:
    - eg. `$ my_program.py --chromosome 4 --start 1 --stop 1000`
  - Report all genes in the specified range


