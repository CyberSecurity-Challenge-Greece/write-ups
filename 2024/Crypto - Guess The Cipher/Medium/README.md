## My X is so weird

#### Challenge Difficulty: Medium
#### Topic: XOR
#### Author: d151nt3gr4t0r

The challenge provides 2 message files which do not contain any relevant information. Attempting to XOR the two files together reveals the flag.

A simple python script that decrypts the message:
```python
with open('output', 'rb') as handle:
    flag = handle.read()
flag = bytearray(flag)
with open('key','rb') as handle:
    key = handle.read()
key = bytearray(key)
print(len(flag))
print(len(key))
for i in range(len(flag)):
    flag[i] = key[i] ^ flag[i]

with open('test', 'wb') as handle:
    handle.write(flag)

```

Flag: csc{x0r_wh3n_y0u_d0nt_kn0w_wh4t_3l53_t0_d0}