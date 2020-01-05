"""
sources:
https://en.wikipedia.org/wiki/Euler%27s_totient_function#Computing_Euler's_totient_function
"""

def getPhi(nr):
    phi = nr
    i = 2
    while i**2 <= nr:
        if nr%i == 0:
            while nr%i == 0:
                nr = nr//i
            phi *= 1-(1/i)
        i += 1
    if nr > 1: # Input nr is a prime number
        phi *= 1 - (1 / nr)
    return int(phi)


max = (0,0)
for i in range(2, 1_000_000+1):
    x=i/getPhi(i)
    if x > max[0]:
        max = (x, i)
print('answer:', max[1])


