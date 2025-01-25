
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


def open_or_senior(data):
      return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]