# Program created by Jeremy Pardo on 02-14-2019
import datetime
import argparse
import re
import pandas as pd
from itertools import groupby

# function to convert DNA sequence to RNA sequence
def makeRNA(seq):
    newSeq = re.sub("T","U",seq.upper())
    return newSeq
# inverts a dictionary makes keys values and values keys
def invertDict(dict):
    newdict = {}
    for k in dict:
        for codon in dict[k].split(","):
            newdict.setdefault(codon,k)
    return(newdict)
# reads in a codon table and converts it to a dictionary
def getCodonDict (codonTable,delim):
    codonTable = pd.read_csv(codonTable,delim)
    AAdict = {}
    for i in codonTable.index:
        AAdict.setdefault(codonTable.iloc[i,0],codonTable.iloc[i,1])
    codonDict = invertDict(AAdict)
    return codonDict


# Parses FASTA file using a generator expression
# credit to https://www.biostars.org/p/710/
def fastaReader(fasta):
    """
        Fasta iterator modified from Brent Pedersen
        Correct Way To Parse A Fasta File In Python
        given a fasta file. yield tuples of header, sequence
    """
    with open(fasta,'r') as fastaFile:
        faiter = (x[1] for x in groupby(fastaFile, lambda line: line[0] == ">"))
        for header in faiter:
            # get header
            headerStr = header.__next__().strip()

            # join all sequence lines to one.
            seq = "".join(s.strip() for s in faiter.__next__())

            yield (headerStr, seq)

# loop through FASTA translate sequence and write to new file
def fastaTranslator(fasta,codonTable,delim,output):

    fiter = fastaReader(fasta)
    with open(output,'w') as outputFile:
        #loop through fasta generator and get header and sequence
        for faSeq in fiter:
            headerStr, seq = faSeq
            seq = makeRNA(seq)
        #Test if length of sequence is a multiple of 3 otherwise raise an error and exit.
            if len(seq) % 3 != 0:
                print("Error: length of CDS sequence is not a multiple of 3.")
                exit()
            AAseq = ""
        # loop through sequence and translate
            for i in range(0, len(seq), 3):
                codon = seq[i:i + 3]
                AA = getCodonDict(codonTable, delim)[codon]
                AAseq = AAseq + AA
            outputFile.write(headerStr+'\n'+AAseq+'\n')






def main():
    start = datetime.datetime.now()
    print("Started program at: {0}".format(start))
    # Command line interface
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--fasta",help="Path to FASTA file")
    parser.add_argument("-c","--codon2AA",help="Path to codon table")
    parser.add_argument("-d","--delim",default="\t",help="File delimter for codon table")
    parser.add_argument("-o","--output",default="./translatedFasta.fa",help="path to output file")
    args = parser.parse_args()
    fasta = args.fasta
    codon = args.codon2AA
    delim = args.delim
    output = args.output
    fastaTranslator(fasta,codon,delim,output)
    print("Finished in {0}".format(datetime.datetime.now()-start))


if __name__ == "__main__":
    main()

