print (True and False) #false
print (True and True and False) #false
print (False and False and True) #false
print(True and True and True) #true
print(True and False and False and True) #false
print(False and True and False and True) #false
print(True and True and True and True) # true
print(False and False and False and False and True) #false
print(False and False and False and False and False) #false
print(True and False and True and False)  #false



print(True or False) #true
print(True or True) #true
print (False or False) #false
print(True or False or True) #true
print(False or False or True) #true
print(False or False or False) #false
print(False or False or False or False or True) #true
print(False or True or False or True) #true
print(True and True and True and True) #true
print(True and True and True and True and True and False) #true



print(True and False or True) #true
print(False or True and False) #false
print(False and True or True) #true
print(False and True or False or False) #false
print(True and False and True or False) #false
print(False or False and False) #false
print(True and True or True and True) #true
print(True and False or True and False or False and True) #false
print(True or False or False or False or False) #true
print(False or True and True or True and True) #true



print(37>34 or 34<13) #true
print(34<31 and 31<33) #false
print(88<31 and 77>99) #false
print(33>44 or 31<30) #false
print(1>3 or 5<1) #false
print(9<3 or 4<3) #false
print(35>66 or 54<88) #true
print(99<100 and 11<111) #true
print(190<200 and 99<199) #true
print(11<10 and 9<9) #false