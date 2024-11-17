def power(a, b):
    return a**b

def divide(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        res = "Can't Divide By Zero"
    finally:
        return res