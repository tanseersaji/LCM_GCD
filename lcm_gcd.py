def gcd(a,b):
    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0:
        return None
    elif a == 0 and not b == 0:
        return b
    elif not a == 0 and b == 0:
        return a
    
    if a > b:
        return gcd((a%b),b)
    else:
        return gcd(a, (b%a))

def lcm(a,b):
    return int(abs(a*b)/gcd(a,b))
    

if __name__ == "__main__":

    print(gcd(gcd(18,24),45))
