"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roshni Mahindru
ID:      210756010
Email:   mahi6010@mylaurier.ca
__updated__ = "2022-08-03"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​​‌​‌‌‌‌:
            None
        -------------------------------------------------------
        """

        b_len = 27
        d = 1
        # Checks if input is already sorted
        if Sorts.is_sorted_alpha(strings) is False:
            for h in range(len(min(strings, key=len))):
                buckets = [list() for _ in range(b_len)]
                for i in strings:
                    e = len(min(strings, key=len)) - d
                    tmp = int((ord(i[e].lower()) - 96))
                    buckets[tmp].append(i)
                a = 0
                for b in range(b_len):
                    buck = buckets[b]
                    for i in buck:
                        strings[a] = i
                        a += 1
                d += 1
        return
        """
        ['w', 'yjjh', 'z', 't', 'xqt', 'dglk', 'ksr']
        [a,b,c,]
        
        [
        apple,
        banana,
        cactuses
        ]
        """
        """
        if strings != []:
            max_char = len(strings[0])
            for value in strings:
                if len(value) >= max_char:
                    max_char = len(value)  # set to 4
                    bucket = []  # Creates the buckets for each letter of the alphabet
                    for _ in range(26):
                        bucket.append([])
                    # Iterates over each character index
                    for char_index in range(max_char - 1, -1, -1):
                        for value in strings:
                            temp = value.lower()
                            # Appends current string to correct bucket
                            if len(value) >= char_index + 1:
                                bucket[
                                    ord(temp[char_index]) % 97
                                ].append(value)
                        index = 0  # Replacing the strings in the input, in sorted order
                        for b in bucket:
                            while len(b) > 0:
                                strings[index] = b.pop(0)
                                index += 1
                                """
    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort on integers.
        Use: Sorts.radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of base 10 integers (list)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​​‌​‌‌‌‌:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
