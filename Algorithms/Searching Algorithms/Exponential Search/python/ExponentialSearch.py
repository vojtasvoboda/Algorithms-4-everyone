class ExponentialSearch:
    def search(self, haystack, needle):
        if haystack[0] == needle:
            return 0

        pos = 1
        while pos < len(haystack) and haystack[pos] < needle:
                pos *= 2

        return self.binarySearch(haystack, needle, pos // 2, pos)

    def binarySearch(self, haystack, needle, lower_bound, higher_bound):
        while lower_bound <= higher_bound:
            middle = lower_bound + (higher_bound - lower_bound) // 2
            if haystack[middle] == needle:
                return middle
            elif haystack[middle] < needle:
                lower_bound = middle + 1
            elif haystack[middle] > needle:
                higher_bound = middle - 1

        return -1

bs = ExponentialSearch()
haystack = [1, 2, 3, 4, 56, 78, 99]

print(bs.search(haystack, 56))
