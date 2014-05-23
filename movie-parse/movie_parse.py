fileToOpen = 'movies.txt.small'

labels = ['product/productId', 'review/text', 'review/helpfulness', \
		 'review/score']

def parse_file(fileToOpen, labels):
	openFile = open(fileToOpen, 'r')
	outputData = []
	outputRow = [0 for x in range(5)]
	for ln in openFile:
		splitln = ln.split()
		if len(splitln) > 1:
			for i in range(len(labels)):
				if splitln[0].startswith(labels[i]):
					outputRow[i] = ' '.join(splitln[1:])
					break
				
		else:
			helpList = outputRow[2].split('/')
			if int(helpList[1]) == 0:
				helpPct = 0
			else:
				helpPct = float(helpList[0])/float(helpList[1])
			outputRow[2] = helpPct
			outputRow.insert(3,helpList[1])
			outputData.append(outputRow)
			outputRow = [0 for x in range(5)]

	return outputData

if __name__ == '__main__':
	outputData = parse_file(fileToOpen, labels)
	outputFile = open('parsedmoviefile.txt', 'w')
	
	outputFile.write('ASIN\tText\tHelpfulness\tHCount\tScore\n')

	for ln in outputData:
		outputFile.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(ln[0],ln[1],ln[2],ln[3],ln[4]))
	outputFile.close()
