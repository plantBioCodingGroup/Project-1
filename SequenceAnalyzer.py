

def fileReader(file_Path):
    filePath = file_Path
    file = open(filePath, 'r')
    seq_list = list()
    for line in file:
        if line.startswith(">"):
            pass
        else:
            seq_list.append(line)

    file.close()
    return(seq_list)
def seqCounter(file):
    seq_list = fileReader(file)
    seq_map = {"A":0,"T":0,"G":0,"C":0}
    for i in range(len(seq_list)):
        for j in seq_list[i]:
            if j.upper() == "A":
                seq_map['A'] = seq_map['A'] + 1
            elif j.upper() == "T":
                seq_map['T'] = seq_map['T'] + 1
            elif j.upper() == "C":
                seq_map['C'] = seq_map['C'] + 1
            elif j.upper() == "G":
                seq_map['G'] = seq_map['G'] + 1



    return(seq_map)
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
    import datetime
    start = datetime.datetime.now()
    main()
    print("It took: {0}".format((datetime.datetime.now())-start))
