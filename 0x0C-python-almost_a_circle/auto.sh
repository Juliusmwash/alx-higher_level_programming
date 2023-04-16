#!/bin/bash
strings=("0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20")

fixed_string=("-main.py")

for s in "${strings[@]}"; do
	joined_string="$s$fixed_string"
	printf "\n\n======================  %s\n" "$joined_string"
	./$joined_string
done
