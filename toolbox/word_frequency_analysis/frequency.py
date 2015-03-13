""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	fin=file(file_name)
	word_list=[]
	for line in fin:
	    for word in line.split():
	        word = word.strip(string.punctuation + string.whitespace)
	        word = word.lower()
	        word_list.append(word)
	return word_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	listy=hist_it(word_list)
	return listy[1:n]

def hist_it(word_list):
    '''
    takes a word list and returns a hist of its words in order of most common (in form of list)
    '''
    hist={}
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return sort_hist(hist)

def sort_hist(hist):
    '''
    takes a hist and spits out and orderd list of the elements of the hist
    '''
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort()
    t.reverse()
    return t

if __name__ == '__main__':
	top_words=get_top_n_words(get_word_list("pg32325.txt"),20)
	print top_words