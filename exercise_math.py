def math():
    a = 57
    b = 7

    result = [
        a + b,
        a - b,
        a * b,
        (a + b) / 2,
        int(a / b),
        a % b,
        a / b
    ]    

    for x in result:
        print(x) 
    
    return result