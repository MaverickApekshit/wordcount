from django.http import HttpResponse
from django.shortcuts import render
import operator #For sorting function to sor the words by count


def home(request):
	'''Render the home page'''
	return render(request, 'home.html')

def count(request):
	'''Render the result page with count of words'''

	#Get the words from text input
	fulltext = request.GET['fulltext']

	#Get the words
	wordlist = fulltext.split()

	#Dictionary to store each word
	worddictionary = {}

	#Count the number of occurences of each word
	for word in wordlist:
		if word in worddictionary:
			#Increase count
			worddictionary[word] += 1
		else:
			#Add word to dictionary
			worddictionary[word] = 1

	#Sort the list of words according to number of occrences
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
