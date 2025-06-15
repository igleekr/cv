#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 10 06:54:35 2025

@author: kingsleylee
"""

# Version 1

n = 20
number_range = set(range(2, n+1))
primes_list = []


prime = number_range.pop()
primes_list.append(prime)

multiples = set(range(prime*2, n+1, prime))
# range(start, stop, step)

number_range.difference_update(multiples)
# removes the numbers that are the same in both sets


# Version 2

# upper bound
n = 1000

# number range to be checked
number_range = set(range(2, n+1))

# empty list to append discovered primes to
primes_list = []

# while loop
while number_range:
    prime = number_range.pop()
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    
# print our list of primes
print(primes_list)

# number of primes found
prime_count = len(primes_list)

# largest prime
largest_prime = max(primes_list)

# summary
print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}.")



# Version 3


def primes_finder(n):
    # number range to be checked
    number_range = set(range(2, n+1))

    # empty list to append discovered primes to
    primes_list = []

    # while loop
    while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
        
    # print our list of primes
    # print(primes_list)

    # number of primes found
    prime_count = len(primes_list)

    # largest prime
    largest_prime = max(primes_list)

    # summary
    print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}.")





primes_list = primes_finder(100)

print(primes_list)



primes_list = primes_finder(1000)
print(primes_list)


primes_list = primes_finder(10000000)


'''

An interesting note on the use of the pop() method with sets in Python...

In the prior tutorial we were coding up a fun & interesting example of identifying prime numbers 
with the emphasis on showing off some of the functionality that can be used with sets in Python.

In the real world - we would need to make a consideration around the pop() method when used on 
a set as in some cases it can be a bit inconsistent.

The pop() method will usually extract the lowest element of a set. Sets however are, by 
definition, unordered. The items are stored internally with some order, but this internal 
order is determined by the hash code of the key (which is what allows retrieval to be so fast). 

This hashing method means that we can't 100% rely on it successfully getting the lowest 
value. In very rare cases, the hash provides a value that is not the lowest.

It's nothing to worry about here, like I say we were just coding up something fun 
to pull together some of what we have learned so far - but it's a useful thing to note 
when using sets in Python in the future!


The simplest solution to force the minimum value to be used is to replace the line...

prime = number_range.pop()

...with the lines...

prime = min(sorted(number_range))
number_range.remove(prime)


Where we firstly force the identification of the lowest number in the number_range into 
our prime variable, and following that we remove it.

However, because we have to sort the list for each iteration of the loop in order to get 
the minimum value, it's slightly slower than what we saw with pop()!

'''

























































