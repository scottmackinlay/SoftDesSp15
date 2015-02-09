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

def proteinTime(dna, threshold):
    """
    takes a set of dna and turns that shit into a string of proteins
    """
    



print findAllOrfsEVER('ATGONETAGAT')