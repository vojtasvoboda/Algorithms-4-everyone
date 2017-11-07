class JumpSearch:
    def search(self, haystack, needle):
        length = len(haystack)
        previous = 0
        increment = int(length**(1/2))
        step = increment
        while haystack[min(step, length) - 1] < needle:
            previous = step
            step += increment
            if previous >= length:
                return -1

        while haystack[previous] < needle:
            previous += 1
            if previous == min(step, length):
                return -1

        if haystack[previous] == needle:
            return previous

        return -1

js = JumpSearch()
haystack = [1, 2, 5, 8, 66, 456]
print(js.search(haystack, 456))
