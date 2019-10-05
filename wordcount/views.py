from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#Increase count
			worddictionary[word] += 1
		else:
			#add word to dictionary
			worddictionary[word] = 1

	sorted(worddictionary.items())

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary.items()})
