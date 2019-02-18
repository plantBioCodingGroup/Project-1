# Program created by Jeremy Pardo on 02-14-2019
import datetime
import argparse
import re
import pandas as pd
from itertools import groupby

def makeRNA(seq):
    newSeq = re.sub("T","U",seq.upper())
    return newSeq
def invertDict(dict):
    newdict = {}
    for k in dict:
        for codon in dict[k].split(","):
            newdict.setdefault(codon,k)
    return(newdict)

def getCodonDict (codonTable,delim):
    codonTable = pd.read_csv(codonTable,delim)
    AAdict = {}
    for i in codonTable.index:
        AAdict.setdefault(codonTable.iloc[i,0],codonTable.iloc[i,1])
    codonDict = invertDict(AAdict)
    return codonDict



def fastaReader(fasta,codonTable,delim):
    with open(fasta,'r') as fastaFile:
        faiter = (x[1] for x in groupby(fastaFile, lambda line: line[0] == ">"))
        for header in faiter:
            # get header
            headerStr = header.__next__().strip()

            # join all sequence lines to one.
            seq = "".join(s.strip() for s in faiter.__next__())

            yield (headerStr, seq)

def fastaTranslator(fasta,codonTable,delim,output):
    fiter = fastaReader(fasta, codonTable, delim)
    with open(output,'w') as outputFile:
        for faSeq in fiter:
            headerStr, seq = faSeq
            seq = makeRNA(seq)
            if len(seq) % 3 != 0:
                print("Error: length of CDS sequence is not a multiple of 3.")
                exit()
            AAseq = ""
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

    #if len(seq) % 3 != 0:
     #   print("Error: length of CDS sequence is not a multiple of 3.")
      #  exit()
#    for i in range(0, len(seq), 3):
#        codon = seq[i:i + 3]
#       AA = getCodonDict(codonTable, delim)[codon]
#       AAseq = AAseq + AA
#print(AAseq)

#AAseq = str()
 #       for line in fastaFile:
  #          if line.startswith(">"):
   #             seq = ""
    #            seqID = line.split()
     #           print(seqID[0])
      #      else:
       #         while not line.startswith(">"):
        #           line = line.strip("\n")
         #           seq = seq+makeRNA(line)
#
 #       yield seq