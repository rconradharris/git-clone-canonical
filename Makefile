check-locations:
	sort locations.txt | uniq | diff locations.txt  - || echo "error: not alphabetized or line not unique" && echo OK

resort-locations:
	sort locations.txt > .locations.resorted && mv .locations.resorted locations.txt
