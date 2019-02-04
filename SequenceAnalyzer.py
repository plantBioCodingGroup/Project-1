# reads in a fasta file and skips header lines
import datetime
def fileReader(file_Path):
    print("Started reading file at: {0}".format(datetime.datetime.now()))
    filePath = file_Path
    seq_list = list()
    with open(filePath, 'r') as infile:
        for line in infile:
            if line.startswith(">"):
                pass
            else:
                seq_list.append(line)
        print("Finished reading file at: {0}".format(datetime.datetime.now()))
    return (seq_list)

# Counts the number of each base and saves them to a dictionary
def seqCounter(file):
    import collections
    seq_list = fileReader(file)
    seq_map = collections.Counter()
    for i in range(len(seq_list)):
        for j in seq_list[i]:
            seq_map[j.upper()] += 1
    print("Finished counting nucleotides at: {0}".format(datetime.datetime.now()))
    return (seq_map)

# calculates and prints GC, AT percentage
def getStats(seq_map):
    total = seq_map['A'] + seq_map['T'] + seq_map['G'] + seq_map['C']
    AT_percent = ((seq_map['A'] + seq_map['T']) / total) * 100
    GC_percent = ((seq_map['G'] + seq_map['C']) / total) * 100
    print("The number of A bases is: {0}".format(seq_map['A']))
    print("The number of T bases is: {0}".format(seq_map['T']))
    print("The number of C bases is: {0}".format(seq_map['C']))
    print("The number of A bases is: {0}".format(seq_map['G']))
    print(" The AT percentage is: {0}".format(AT_percent))
    print(" The GC percentage is: {0}".format(GC_percent))


def main():
    getStats(seqCounter("/Users/Jeremy/Documents/MSU/VanBuren_Lab/Grass_Drought/Eragrostis_tef/Tef_V3_5-8-18.fasta"))


if __name__ == "__main__":

    start = datetime.datetime.now()
    main()
    print("Process finished in: {0}".format((datetime.datetime.now()) - start))
