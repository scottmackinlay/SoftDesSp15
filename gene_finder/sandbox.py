def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    final=[]
    end = False

    for frame in range(3):
        startSearch=frame
        print 'frame',frame
        while ~end:
            for i in range(startSearch,len(dna),3):
                if dna[i:i+3]=='ATG':
                    print 'found ATG at', i
                    for p in range(i,len(dna),3):

                        if dna[p:p+3]=='TAG' or dna[p:p+3]=='TGA' or dna[p:p+3]=='TAA':
                            print dna[i:p]
                            print 'found STOP at', p
                            final.append(dna[i:p])
                            startSearch=p
                            break
                        else:
                            end=True 
                    break
            end = True
    return final