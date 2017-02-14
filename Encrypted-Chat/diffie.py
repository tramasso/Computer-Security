 from random import randint
 q = pow(2,101)-69
 a = pow(2,80)-65
 xa = randint(0,q)
 xb = randint(0,q)
 ya = pow(a,xa,q)
 yb = pow(a,xb,q)
 k1 = pow(yb,xa,q)
 k2 = pow(ya,xb,q)

