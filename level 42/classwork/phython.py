def is_isogram(string):
     return len(string) == len(set(string.lower()))


def find_short(s):
      return min(len(x) for x in s.split())