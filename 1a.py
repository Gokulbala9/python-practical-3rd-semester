tup = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 20)]
print("Original list of tuples:", tup)
sums = list(map(sum, tup))
print("Sum of elements in each tuple:", sums)
average = sum(sums) / len(sums)
print("Average of tuple sums:", average)
