import pandas as pd
import numpy as np
import codecs
import json
import collections

def raw_data_to_word_count(rawData, key, successKey, \
	successFlag=True, removeWords=[]):

	"""Transforms list of dictionaries to count of words"""

	titles = [row[key].split() for row in rawData if \
	row[successKey]==successFlag]

	words = [e[i].lower().strip('.,;:[]{}()-?') for e in titles for \
	i in xrange(len(e))]

	titlesCounter = collections.Counter(words)

	for k in list(titlesCounter.keys()):
		if k in removeWords:
			del titlesCounter[k]


	return titlesCounter


def word_count_to_top_list(titlesCounter, n=15):

	"""Returns top n words and their counts"""

	topTitleWords = sorted([[k, titlesCounter[k]] for k in \
		titlesCounter], key=lambda x:x[1], reverse=True)[:n]


	return topTitleWords



if __name__ == '__main__':

	text = \
	codecs.open('pizza_request_dataset.json', 'r', 'utf-8').read()
	rawData = json.loads(text)

	successFlag = raw_input('Successful? [True]/False')
	if successFlag == '' or successFlag == 'True': 
		successFlag = True
	elif successFlag == 'False':
		successFlag = False

	removeWords = ['request','a','and','to','for','in','my','i','of',\
	'the','some','on','with','have','me','is','']

	titlesCounter = raw_data_to_word_count(rawData, 'request_title', \
		'requester_received_pizza', successFlag, removeWords)

	topTitleWords = word_count_to_top_list(titlesCounter)