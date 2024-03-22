## Insecure

#### Challenge Difficulty: Easy
#### Topic: RSA 
#### Author: d151nt3gr4t0r

The challenge supplies us with the n and e values of the rsa key. 

```
e = 65537
n = 1034776851837418228051242693253376923

c = 1006234941664191676977296641660749407
```

We can use factordb.com to factorize the public key and retrieve the 2 factors it was created with, p and q. With these factors, we can calculate the phi and inverse it to decrypt the encrypted message.

p = 1086027579223696553
q = 952809000096560291

phi = 1034776851837418226012406113933120080
d = 568411228254986589811047501435713

The python script below does exactly that. 

```python
from Crypto.Util.number import inverse

# Challenge values
e = 65537
n = 1034776851837418228051242693253376923
c = 1006234941664191676977296641660749407

# from factordb.com
p = 1086027579223696553
q = 952809000096560291

# Calculations start here
phi = (p-1) * (q-1)

d = inverse(e,phi)

decrypted_m = pow(c,d,n)
print(decrypted_m)
```

wrap the decrypted value (45678974185296321458796325) into the csc{} flag structure and submit the flag! 