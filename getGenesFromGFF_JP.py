# created by Jeremy Pardo on 2/25/2019
import datetime
import argparse
import re
from collections import defaultdict
def gffParser(gff,delim):
    gffDict = defaultdict()
    with open(gff,'r') as gffFile:
        for line in gffFile:
            line = line.strip()
            if line.startswith("#"):
                pass
            else:
                parsedLine = line.split(delim)
                if parsedLine[2] == "gene":
                    chr = parsedLine[0]
                    start = parsedLine[3]
                    end = parsedLine[4]
                    range = [chr,start,end]
                    geneIDLine = re.sub(";.*$","",parsedLine[8])
                    geneID = re.sub("^ID=gene:","",geneIDLine)
                    gffDict.setdefault(geneID,range)
    return(gffDict)







def main():
    start = datetime.datetime.now()
    print("Started program at: {0}".format(start))
    # Command line interface
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gff", help="Path to gff file")
    parser.add_argument("-d", "--delim", help="file seperator",default="\t")
    parser.add_argument("-i", "--interval", help="genomic interval", default="\t")
    args = parser.parse_args()
    gff = args.gff
    delim = args.delim
    interval = args.interval
    print(interval.split(","))
    print(gffParser(gff,delim))
if __name__ == "__main__":
    main()