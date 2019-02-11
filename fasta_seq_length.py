#!/Users/alanyocca/anaconda3/bin/python
#02-04-19
#Alan E. Yocca

import re

filename="/Users/alanyocca/Documents/pbcoding_group/local/sequence.fasta"

fh = open(filename, "r")
print("I opened the file, yay")

#define sequence
sequence=""
for line in fh:
  line = line.strip("\n")
  if re.match(r"^>",line):
    #header
    #print("Found match!")
    #print(line)
    pass
  else:
    sequence+=str(line)

print("This file contains: " + str(len(sequence)) + " characters")
print("This file contains: " + str(len(re.findall("[gG]",sequence))) + " Gs")
print("This file contains: " + str(len(re.findall("[cC]",sequence))) + " Cs")

gc_total = len(re.findall("[gG]",sequence)) + len(re.findall("[cC]",sequence))
gc_dec = gc_total / len(sequence)
gc_per = gc_dec * 100


print("This file contains: " + str(gc_per) + " GC %")

#print("This file contains: " + sum(str(len(re.findall("[gG]",sequence))) + str(len(re.findall("[gG]",sequence))))/str(len(sequence)) + " Gs")


fh.close()
