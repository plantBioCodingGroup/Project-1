#!/bin/python
#Alan E. Yocca
#02-17-19
#fasta_cds_to_pep.py

#convert cds file to peptide file
#specify own codon usage table

import re

fasta_filename="/Users/alanyocca/Documents/pbcoding_group/local/D_melanogaster.cds.Chr4.fa"
usage_table_filename="/Users/alanyocca/Documents/pbcoding_group/local/Codon_AA_table.txt"
output_filename="/Users/alanyocca/Documents/pbcoding_group/local/D_melanogaster.pep.Chr4.fa"

ut_fh = open(usage_table_filename, "r")
codon_to_pep={}
for line in ut_fh:
  line = line.strip("\n")
  if re.match(r"^Amino",line):
    #header
    pass
  else:
  	#example line from table:
    #A	GCU,GCC,GCA,GCG
    aa_to_cds_list = line.split('\t')
    cds_list = aa_to_cds_list[1].split(',')
    for codon in cds_list:
    	codon_to_pep[codon] = aa_to_cds_list[0]

ut_fh.close()

out_fh = open(output_filename, "w")
cds_fh = open(fasta_filename, "r")
print("I opened the file, yay")

#define sequence
sequence=""
header=""
first=1
for line in cds_fh:
	line = line.strip("\n")
	if re.match(r"^>",line):
		#fasta header, print out
		#if not first header, convert, and print out previous sequence
		if first != 1:
			#convert sequence to pep using dictionary
			#courtesy of SO
			cds_seq_split = [sequence[i: i + 3] for i in range(0, len(sequence), 3)]
			for codon in cds_seq_split:
				#write out all conversions
				if not codon in codon_to_pep:
					#print("codon not def %s", codon)
					#stop codon or start codon?
					if codon == "ATG":
						out_fh.write( "M" )
					else:
						out_fh.write( "*" )
					break
				out_fh.write( codon_to_pep[codon] )
		else:
			first=0
			out_fh.write( line + '\n' )
	else:
		sequence+=str(line)

out_fh.close()
cds_fh.close()













