def friend(x):
     return [x for x in x if len(x) == 4]

def maskify(cc):
      return "#"*(len(cc)-4) + cc[-4:]