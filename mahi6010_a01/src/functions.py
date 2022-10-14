"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-05-14"
-------------------------------------------------------
"""


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


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    lis = list(name)
    valid = True
    if lis[0].isalpha() or lis[0] == "_":
        valid = True
        for i in lis:
            if i.isalpha() or i.isnumeric() or i == "_":
                valid = True
            else:
                valid = False
    else:
        valid = False

    return valid


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


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        result - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # iterating by row of A
    for i in range(len(a)):

        # iterating by column by B
        for j in range(len(b[0])):

            # iterating by rows of B
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    estring = []

    for letter in string:
        letter_upper = letter.upper()
        for char_upper in letter_upper:
            if char_upper in ALPHABET:
                for i in range(len(ALPHABET)):
                    char = ALPHABET[i]
                    if char_upper == char:
                        shift_amt = i + n
                        if shift_amt > len(ALPHABET):
                            extra = shift_amt - len(ALPHABET)
                            if extra > 0:
                                shift_amt = extra - 1
                            else:
                                shift_amt = extra
                        elif shift_amt == len(ALPHABET):
                            shift_amt = 0
                        shift_char = ALPHABET[shift_amt]
                        estring.append(shift_char)
                        break
            else:
                estring.append(letter_upper)
    return estring
