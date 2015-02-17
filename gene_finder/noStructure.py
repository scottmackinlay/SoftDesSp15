# -*- coding: utf-8 -*-
"""
Created spring semester in soft des
@author: Scottttty

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
dna=load_seq("./data/X73525.fa")


def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

def reversereverse(dna):
    """
    Reverses the input string and translates it to its opposite side of the dna

    >>> reversereverse('ATGCATGC')
    'GCATGCAT'
    >>> reversereverse('AC')
    'GT'

    """
    nucDict= {'A':'T','T':'A','G':'C','C':'G'}
    Comp=[] # compliment
    for i in dna:
        Comp.append(nucDict[i])
    Comp.reverse()
    return ''.join(Comp)



def usedUp(dna):
    """
    passes true if the dna passed has no things to find on that frame
    >>> usedUp('ATGTAG')
    False
    >>> usedUp('ATGAAATTT')
    True
    """
    for i in range(0,len(dna),3):
        if dna[i:i+3]=='ATG':
            for p in range(i,len(dna),3):
                if dna[p:p+3]=='TAG' or dna[p:p+3]=='TGA' or dna[p:p+3]=='TAA':
                    return False
    return True

def findFirstORF(dna):
    """ passes out the first in-frame ORF that it comes across in a string of dna
        also passes out the rest of the dna strand after the found ORF


        >>> findFirstORF('ATGPOOPOOTAGPOOPOO')
        ['ATGPOOPOO', 'TAGPOOPOO']
        >>> findFirstORF('ATGPOOoTAG')
        >>> findFirstORF('ATGATGTAG')
        ['ATGATG', 'TAG']

    """
    # print 
    # print 'I was passed',dna
    for i in range(0,len(dna),3):
        if dna[i:i+3]=='ATG':       #i is the point where ATG is found
            # print 'Atg found at', i
            for p in range(i,len(dna),3):   # p is where we find a stop codon
                if dna[p:p+3]=='TAG' or dna[p:p+3]=='TGA' or dna[p:p+3]=='TAA':
                    # print 'stop found at',p
                    # print'Ill pass out', [dna[i:p],dna[p:len(dna)]]
                    return [dna[i:p],dna[p:len(dna)]]


def findAllOrfsOneFrame(dna):
    """
    finds all the ORFS in one frame of the dna string
    >>> findAllOrfsOneFrame('ATGONETAGATGTWOTAGATGTRETAG')
    ['ATGONE', 'ATGTWO', 'ATGTRE']
    >>> findAllOrfsOneFrame('ATGONETAGPOOOATGTAG')
    ['ATGONE']
    >>> findAllOrfsOneFrame('ATGCCCTTTGGG')
    []
    """
    final=[]
    while usedUp(dna)==False:
        [ORF,dna]=findFirstORF(dna)
        final.append(ORF)
    return final


def findAllOrfsEVER(dna):
    """
    Finds all ORFs on all three reading frames

    >>> findAllOrfsEVER('ATGONETAGATGTWOTAGooATGTHIRDFRAMTAG')
    ['ATGONE', 'ATGTWO', 'ATGTHIRDFRAM']
    >>> findAllOrfsEVER('ATGTAGOATGTAGOATGTAG')
    ['ATG', 'ATG', 'ATG']
    """
    final=[]
    for frame in range(0,3):
        if usedUp(dna)==False:
            final.extend(findAllOrfsOneFrame(dna))
        dna=dna[1:len(dna)]
    return final

def bothStrands(dna):
    """
    Finds all ORFS on given dna in both directions
    (original and reversed/complementary)

    >>> bothStrands('ATGCTATAGCAT')
    ['ATGCTA', 'ATGCTA']

    >>> bothStrands('ATGTTTTAGATGTTTTAG')
    ['ATGTTT', 'ATGTTT']

    >>> bothStrands('ATGTAGATGATTATT')
    ['ATG']

    >>> bothStrands('ATGCATGTAGCCTAG')
    ['ATGCATGTAGCC', 'ATG']

    """
    final=[]
    final.extend(findAllOrfsEVER(dna))
    dna=reversereverse(dna)
    final.extend(findAllOrfsEVER(dna))
    return final

def dnaToProteinOnce(dna):
    """
    This takes a single string and turns it into a string of protein chunks
    >>> dnaToProteinOnce('ATGCCC')
    'MP'

    This one doesnt need as many doc tests as the others because the inputs to this 
    function are so well tested
    """
    protein=[]
    for i in range(0,len(dna),3):
        protein.append(aa_table[dna[i:i+3]])
    return ''.join(protein)


def dnaToProtein(dna,threshold):
    """
    Takes a string of dna and returns every possible list of protein chunks that
    the dna could have coded for (includes reverse compliment and all reading 
    frames therein)

    Oh and it will pass only the proteins coded by ORFs that excede the threshold.

    >>> dnaToProtein('ATGACTTAGTATGCCCTAGCCTACCCCAT',1)
    ['MT', 'MP', 'MG']
    >>> dnaToProtein('ATGACTTAGTATGCCCTAGCCTACCCCAT',7)  #THIS IS TOO DAMN SENSITIVE
    []
    """

    ORFList=bothStrands(dna)
    proteinList=[]
    for ORF in ORFList:
        if len(ORF)>threshold:
            proteinList.append(dnaToProteinOnce(ORF))
    return proteinList

def longestORFNoncoding(dna,numTrials):
    """
    Takes a length of dna and over a specified number of trials, it finds how long 
    the longest ORF would be (just because of randomness) The threshold is this.
    """
    Longest=0
    for i in range(numTrials):
        randProteins=bothStrands(shuffle_string(dna))   #finds all ORFs in a random (but long) string of dna
        randProteins.sort(key=len)  
        if len(randProteins[-1])>Longest:
            Longest=len(randProteins[-1])      
    return Longest


proteinList= dnaToProtein(dna,longestORFNoncoding(dna,15))
for i in proteinList:
    print i


if __name__ == "__main__":
    import doctest
    doctest.testmod()                             

