check-locations:
	sort locations.txt | uniq | diff locations.txt  - || echo "error: not alphabetized or line not unique" && echo OK