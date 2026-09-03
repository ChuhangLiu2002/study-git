def two_sum(numbers, target):
	"""返回数组中和为 target 的两个数字的下标。"""
	seen = {}

	for index, number in enumerate(numbers):
		complement = target - number
		if complement in seen:
			return [seen[complement], index]
		seen[number] = index

	return []


if __name__ == "__main__":
	numbers = [2, 7, 11, 15]
	target = 9
	print(two_sum(numbers, target))  # [0, 1]
