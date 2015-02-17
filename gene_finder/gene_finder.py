# -*- coding: utf-8 -*-
"""
Created spring semester in soft des
@author: Scottttty

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###

#1
def get_complement(nucleotide):

    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    nucDict= {'A':'T','T':'A','G':'C','C':'G'}
    return nucDict[nucleotide]

    # TODO: implement this
    
#2
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    nucDict= {'A':'T','T':'A','G':'C','C':'G'}

    revComp=[]
    for i in range(len(dna)):
        revComp.append(nucDict[dna[len(dna)-i-1]])
        
    #dna = dna[::-1]
    return ''.join(revComp)
    

#3
def rest_of_ORF(dna):

    """
    Takes a sting of dna and spits out the ORF

    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """

    for i in range(0,len(dna),3):
        if dna[i:i+3]=='TAG' or dna[i:i+3]=='TGA' or dna[i:i+3]=='TAA':
            return dna[0:i]
    
    return dna


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    final=[]
#    while dna.find != -1:
    for x in range(10):
        final.append(rest_of_ORF(dna[dna.find('ATG'):len(dna)]))
        dna=dna[len(rest_of_ORF(dna)):len(dna)]
        if dna.find('ATG')!=-1:
            dna=dna[dna.find('ATG'):len(dna)]
        else:
            return final
    return final
                    
    
#5
# def find_all_ORFs(dna):
#     """ Finds all non-nested open reading frames in the given DNA sequence in all 3
#         possible frames and returns them as a list.  By non-nested we mean that if an
#         ORF occurs entirely within another ORF and they are both in the same frame,
#         it should not be included in the returned list of ORFs.
        
#         dna: a DNA sequence
#         returns: a list of non-nested ORFs

#     >>> find_all_ORFs("ATGCATGAATGTAG")
#     ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
#     """
#     # TODO: implement this
#     pass
#     final=[]
# #    while dna.find != -1:
#     for x in range(10):
#         final.append(rest_of_ORF(dna[dna.find('ATG'):len(dna)]))
#         dna=dna[len(rest_of_ORF(dna)):len(dna)]
#         if dna.find('ATG')!=-1:
#             dna=dna[dna.find('ATG'):len(dna)]
#         else:
#             return final
#     return final

#6
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    final=[]
    final.append(find_all_ORFs(dna))
    dna=get_reverse_complement(dna)
    if dna.find('ATG')!=-1:
        final.append(find_all_ORFs(dna[dna.find('ATG'):len(dna)]))
    return final



'''
DONT DO THE ONES BELOW THIS LINE
'''


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    #sorted(listName, key=len)
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
        
    # TODO: implement this
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()