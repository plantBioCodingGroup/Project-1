#!/bin/bash

GC=` tail -n +2 sequence.fasta | grep -n -o 'G\|C' | wc -l`
Total=` tail -n +2 sequence.fasta | grep -n -o 'G\|C\|A\|T' | wc -l`

echo "$GC Gs and Cs"
echo "$Total total bases"
echo "GC Content = $(echo "scale=3;$GC/$Total" | bc -l)"
