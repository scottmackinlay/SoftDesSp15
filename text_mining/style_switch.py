
import string
import random
import math
from most_common import common_words

def word_list_it(filename):
    '''
    returns a list of a specified file's words in the original order
    '''
    fin=file(filename)
    word_list=[]
    for line in fin:
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            word_list.append(word)
    return word_list

def sort_hist(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort()
    t.reverse()
    return t

def hist_it(filename):
    '''
    takes a file and returns a hist of its words in order of most common (in form of list)
    '''
    word_list=word_list_it(filename)

    hist={}
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return sort_hist(hist)

def what_comes_next(target,filename):
    '''
    takes a target word and gives one of the top 5 percent of words that follow it in a given file
    '''

    following={}
    word_list=word_list_it(filename)
    for i in range(len(word_list)-1):
        if word_list[i]==target:
            following[word_list[i+1]]=following.get(word_list[i+1],0)+1
    if len(following)==0:
        return ''
    elif len(following)>=6:
        return sort_hist(following)[random.randint(0,5)][1]
    elif len(following)<6: 
        return sort_hist(following)[random.randint(0,len(following)-1)][1]
    
def vocab_switch(file_one,file_two,common_words):
    '''
    takes file one and correctly inserts file two's words in at key locations
    '''

    word_list=word_list_it(file_one)
    changers=words_to_change(hist_it(file_one),common_words)
    for i in range(3,len(word_list)):
        if word_list[i] in changers:
            change_to=what_comes_next(word_list[i-1],file_two)
            if change_to not in common_words and change_to!='':
                word_list[i]=change_to.upper()
    return word_list

def words_to_change(word_pairs,common_words):
    '''
    takes a hist of a body of text and determines which words need changing by 
    determining which words are the most common text that arent common in the
    english language
    '''
    return [i[1] for i in word_pairs if i[1] not in common_words]
    
def list_to_text(listy):
    '''
    takes a list and saves it to a text file
    '''
    text=''
    for i in listy:
        text=text+i+' '
    text_file = open("results.txt", "w")
    text_file.write(text)
    text_file.close()

if __name__ == '__main__':
    # print what_comes_next("wish",'test.txt')
    list_to_text(vocab_switch('call_maybe.txt','twenty_under.txt',common_words))