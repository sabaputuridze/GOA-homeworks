def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def swap_name(name):
    first_name, last_name = name.split()
    return f"{last_name} {first_name}"

