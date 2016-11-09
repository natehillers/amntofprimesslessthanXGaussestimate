## Primeslessthan(x)
## Actual # of primes less than (10) = 4, Primeslessthan(100) = 25, Primeslessthan(1,000,000,000) = 50,487,537 etc.
## Gauss estimate of Primeslessthan(x) ~= (1/log(x)) 
## ~= Integral(from 2 > x) of (1/ln(t)) dt

import math
from scipy import integrate

higherlimitinput = input("What do you want the upper limit to be? ")

def Guassestimate(x):
	higherlimitinteger = int(higherlimitinput)
	oneover = lambda x: 1/(math.log(x))
	ans, err = integrate.quad(oneover, 2, higherlimitinteger)
	return round(ans)

print(Guassestimate(higherlimitinput))