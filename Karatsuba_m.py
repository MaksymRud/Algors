

def karatsuba_rec(x, y):

    if(x // 10 == 0 or y // 10 == 0):
        return x*y
    
    digits_x = count_digit(x)

    a = x // pow(10, digits_x//2)
    b = x % pow(10, digits_x//2)
    
    digits_y = count_digit(y)

    c = y // pow(10, digits_y//2)
    d = y % pow(10, digits_y//2)

    if(digits_y % 2 != 0 or digits_x % 2 != 0):
        return (pow(10, digits_x//2) * a + b)*(pow(10, digits_y//2) * c + d)
    else:
        return pow(10, digits_x)*karatsuba_rec(a, c) + pow(10, digits_x//2)*(karatsuba_rec(a + b, c + d) - karatsuba_rec(a, c) - karatsuba_rec(b, d)) + karatsuba_rec(b, d)
    
print(karatsuba_rec(355, 3453))