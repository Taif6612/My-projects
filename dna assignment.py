def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna) 


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)
    
    
def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0'abc123'.isalnum
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid.

    >>>is_valid_sequence('ATCGGCB')
    False
    >>>is_valid_sequence('ATCGGC')
    True

    '''
    
    for char in dna:
        if not (char in 'ATCG'):
            return False

    return True

def insert_sequence(dna1,dna2,index):
    ''' (str,str,int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('CCAT','GG',3)
    'CCAGGT'

    '''

    dna3=dna1[:index]+dna2+dna1[index:]

    return dna3

def get_complement(nucleotide):
    ''' (str) -> str
    Return the nucleotide's complement.

    >>>get_complement('T')
    A
    >>>get_complement('G')
    C

    '''

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'
    return ''


def get_complementary_sequence(sequence):
    ''' (str) -> str
    Return the DNA sequence that is comlementary to the given DNA sequence

    >>>get_complementary_sequence(AT)
    TA
    >>>get_complementary_sequence(TG)
    AC

    '''
    result_sequence = ""

    for nucleotide in sequence:
        result_sequence = result_sequence + get_complement(nucleotide)

    return result_sequence
    





























    
