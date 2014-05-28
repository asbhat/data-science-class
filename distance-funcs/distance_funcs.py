def distance(u, v):
	"""
	Returns Euclidean distance between two vectors
	"""

	import math

	# sumList = []
	# for i in xrange(len(u)):
	# 	sumList.append((u[i] - v[i]) ** 2)

	# return math.sqrt(sum(sumList))

	return math.sqrt(sum([(ui - vi) ** 2 for ui, vi in zip(u, v)]))


def dot(u, v):
	"""
	Returns dot product between two vectors
	"""

	#Method 1
	# sumList = []
	# for i in xrange(len(u)):
	# 	sumList.append(u[i] * v[i])

	#Method 2
	# total = 0
	# for ui, vi in zip(u, v):
	# 	total += ui * vi

	#Method 3
	return sum([ui * vi for ui, vi in zip(u, v)])

	# Only works on numpy arrays
	# return sum(u * v)


if __name__ == '__main__':
	u = [1, 3.4, 5.6, -2]
	v = [5, 7, 5, 3]

	print dot(u, v)
	print
	print distance(u, v)