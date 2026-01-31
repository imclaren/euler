#!/usr/bin/python3

# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters.
# The use of 'and' when writing out numbers is in compliance with
# British usage.

def letter_count(words): 
    return sum([len(w) for w in words.split()])

def num2word(n):
    l_one = ['', 'one ','two ','three ','four ', 'five ',
        'six ','seven ','eight ','nine ']
    l_ten = ['ten ','eleven ','twelve ','thirteen ', 'fourteen ',
        'fifteen ','sixteen ','seventeen ','eighteen ','nineteen ']
    l_twenty = ['','','twenty ','thirty ','forty ',
        'fifty ','sixty ','seventy ','eighty ','ninety ']
    l_thousand = ['','thousand ','million ', 'billion ', 'trillion ',
        'quadrillion ', 'quintillion ', 'sextillion ', 'septillion ',
        'octillion ', 'nonillion ', 'decillion ', 'undecillion ',
        'duodecillion ', 'tredecillion ', 'quattuordecillion ',
        'sexdecillion ', 'septendecillion ', 'octodecillion ',
        'novemdecillion ', 'vigintillion ']
    l = []
    a = str(n).split()[0]
    while len(a) >= 3:
        l.append(int(a[len(a)-3:]))
        a = a[:-3]
    if a: l.append(int(a))
    words = ''
    for i, x in enumerate(l):
        if x:
            tens = x%10
            hundreds = (x%100)//10
            thousands = (x%1000)//100
            if not hundreds: words = l_one[tens]+l_thousand[i]+words
            elif hundreds == 1: words = l_ten[tens]+l_thousand[i]+words
            elif hundreds > 1: words = l_twenty[hundreds]+l_one[tens]+l_thousand[i]+words
            if thousands:
                if x%100: h = 'hundred and '
                else: h = 'hundred '
                words = l_one[thousands]+h+words
    return words

result = sum([letter_count(num2word(i+1)) for i in range(0,1000)])
print(result)
