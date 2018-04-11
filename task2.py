"""
===================   TASK 2   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def gcd(a,b):
    a_apsolutno = abs(a)
    b_apsolutno = abs(b)

    z=abs(a_apsolutno - b_apsolutno)

    if z==0:
        return a_apsolutno
    else:

        return gcd(z,min(a_apsolutno,b_apsolutno))

print(gcd(-12,8))