#!/usr/bin/python
#
# Re-ID solution for Commander Lambda
#

import sys

#-----------
# From Sieve of Eratosthanes solution posted at:
# http://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/10733621#10733621

from itertools import count
                                         # ideone.com/aVndFM
def postponed_sieve():                   # postponed sieve, by Will Ness      
    yield 2; yield 3; yield 5; yield 7;  # original code David Eppstein, 
    sieve = {}                           #   Alex Martelli, ActiveState Recipe 2002
    ps = postponed_sieve()               # a separate base Primes Supply:
    p = next(ps) and next(ps)            # (3) a Prime to add to dict
    q = p*p                              # (9) its sQuare 
    for c in count(9,2):                 # the Candidate
        if c in sieve:               # c's a multiple of some base prime
            s = sieve.pop(c)         #     i.e. a composite ; or
        elif c < q:  
             yield c                 # a prime
             continue              
        else:   # (c==q):            # or the next base prime's square:
            s=count(q+2*p,2*p)       #    (9+6, by 6 : 15,21,27,33,...)
            p=next(ps)               #    (5)
            q=p*p                    #    (25)
        for m in s:                  # the next multiple 
            if m not in sieve:       # no duplicates
                break
        sieve[m] = s                 # original test entry: ideone.com/WFv4f
#-------------


def answer(n):
    primes_str = ''
    id_str = ''

    # Get primes until we have a complete new ID string
    for prime in postponed_sieve():
        #print 'DEBUG:', i, ': prime =', prime
        primes_str += str(prime)
        if len(primes_str) >= (n + 5):
            id_str = primes_str[n:n + 5]
            #print '     DEBUG: id_string =', id_string
            break

    return id_str


def main():
    # Parse command args
    args = sys.argv[1:] 
    if not args:
        print 'Usage: <scriptname> n'
        sys.exit(1)
    id_index = int(args[0])
    print answer(id_index)

if __name__ == '__main__':
    main()