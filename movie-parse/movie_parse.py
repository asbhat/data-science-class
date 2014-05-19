fileToOpen = 'movies.txt.small'

labels = ['product/productId', 'review/text', 'review/helpfulness', \
		 'review/score']

def parse_file(fileToOpen, labels):
	openFile = open(fileToOpen, 'r')
	outputData = []
	outputRow = [0 for x in range(4)]
	for ln in openFile:
		splitln = ln.split()
		if len(splitln) > 1:
			for i in range(len(labels)):
				if splitln[0].startswith(labels[i]):
					outputRow[i] = ' '.join(splitln[1:])
					break
				
		else:
			outputData.append(outputRow)
			outputRow = [0 for x in range(4)]

	return outputData

if __name__ == '__main__':
	outputData = parse_file(fileToOpen, labels)
	outputFile = open('parsedmoviefile.txt', 'w')
	for la in labels:
		outputFile.write(la + '\t')
	outputFile.write('\n')

	for ln in outputData:
		for elem in ln:
			outputFile.write(elem + '\t')
		outputFile.write('\n')
	outputFile.close()
