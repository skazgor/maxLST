#!/bin/bash

# List of random graph files
files=("random_graph_1.txt" "random_graph_2.txt" "random_graph_3.txt" "random_graph_4.txt" "random_graph_5.txt" "random_graph_6.txt" "random_graph_7.txt" "random_graph_8.txt" "random_graph_9.txt" "random_graph_10.txt")

# Path to your C++ program
# program="./2_appx"
program="./exact_exponential"

# Iterate over each file
for file in "${files[@]}"
do
    echo "Running $program with input file: $file"
    time $program < $file
    echo "---------------------------------------------"
done
