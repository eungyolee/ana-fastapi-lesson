def find_digits_sum(n: int) -> int:
	hap = 0
	for digit in str(n):
		hap += int(digit)
	
	return hap