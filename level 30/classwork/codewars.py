def basic_op(operator, value1, value2):
       return eval(str(value1) + operator + str(value2))


def litres(time):
    return int(time * 0.5)



def century(year):
    if year % 100==0:
        return year//100
    else:
        return year// 100 + 1