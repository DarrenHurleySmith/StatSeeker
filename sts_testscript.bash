#!/bin/bash

FILE=$1
SIZE=$2

echo "Processing $FILE"
cd sts-2.1.2/
printf "0\n../$FILE\n1\n0\n10\n1\n" | ./assess $SIZE
#cp experiments/AlgorithmTesting/finalAnalysisReport.txt ../../results/"sp80022cd NIST.txt"
cd ..

