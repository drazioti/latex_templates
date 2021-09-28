def karatsuba(x,y,B):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2
        a =  x // B**(m2)
        b =  x % B**(m2)
        c =  y // B**(m2)
        d =  y % B**(m2)

        z0 = karatsuba(b,d,B)
        z1 = karatsuba((a+b),(c+d),B)
        z2 = karatsuba(a,c,B)
        return ( z2 * B**(2*m2) ) + ( (z1 - z2 - z0) * B**(m2) ) + z0