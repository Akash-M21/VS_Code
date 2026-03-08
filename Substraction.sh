#!/bin/bash

# Script to subtract numbers interactively up to 20 iterations

echo "Enter initial number:"
read initial
result=$initial

for i in {1..20}; do
    echo "Enter number to subtract (or 'q' to quit):"
    read num
    if [ "$num" = "q" ]; then
        break
    fi
    if ! [[ "$num" =~ ^-?[0-9]+$ ]]; then
        echo "Invalid number, try again."
        continue
    fi
    result=$((result - num))
done

echo "Final result: $result"