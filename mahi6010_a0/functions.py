"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Roshni Mahindru
ID:210756010
Email:mahi6010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from curses.ascii import isupper
from pickle import FALSE


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    j = 1
    while i < len(values):
        j = i + 1
        while j < len(values):
            if values[j] == values[i]:
                values.pop(j)
                j -= 1
            j += 1
        i += 1
    return


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    temp = []
    for x in range(0, len(s)):
        if s[x] in vowels:
            temp.append('')
        else:
            temp.append(s[x])
    out = ""
    for ele in temp:
        out += ele
    return(out)


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = fv.readline()
    main = []
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    while line != '':
        mini = list(line)
        for i in mini:
            if i != '\n':
                main.append(i)
        line = fv.readline()
    for i in main:
        if i.isdigit():
            d += 1
        elif i.isalpha():
            if i.islower():
                l += 1
            else:
                u += 1
        elif i == ' ':
            w += 1
        else:
            r += 1
    return u, l, d, w, r


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        if year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
    return leap_year


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    left = 0
    right = len(s) - 1
    palindrome = True
    while left != (len(s)):
        if s[left] != s[right]:
            palindrome = False
        left += 1
        right -= 1
    return palindrome


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    for x in range(0, len(a) - 1):
        diff = a[x] - a[x + 1]
        if diff < 0:
            diff = diff * -1
        if diff > md:
            md = diff
    return md


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for x in a[0]:
        list = []
        list.append(x)
        b.append(list)
    for y in range(1, len(a)):
        for z in range(0, len(a[0])):
            b[z].append(a[y][z])
    return(b)


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    num = 0
    for b in range(len(a)):
        for c in a[b]:
            if c < small:
                small = c
            if c > large:
                large = c
            total += c
            num += 1
    average = total / num
    return small, large, total, average


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    x = 0
    if word[0] in "aeiouAEIOU":
        pl += word
        pl += "way"
    else:
        for i in word:
            if i in "aeiouyAEIOUY":
                break
            else:
                x += 1
        pl += word[x:]
        pl += word[0:x]
        pl += "ay"
    pl = pl.lower()
    for i in range(0, len(word)):
        if word[i].isupper():
            pl[i].upper()
    return pl
