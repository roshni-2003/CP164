"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author: Roshni Mahindru
ID:     210756010
Email:  mahi6010@mylaurier.ca
__updated__ = "2022-04-14"
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
        Returns‌‌​‌​​‌‌:
            None
        -------------------------------------------------------
        """
        if len(strings) <= 0:
            return None
        else:

            b_len = 27
            d = 1
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
        Returns‌‌​‌​​‌‌:
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
