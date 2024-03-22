# [CHALLENGE_TITLE]
CrackTheSeed

## Category
Crypto

## Estimated difficulty
Easy

## Description
The player needs to crack the mt_rand seed which is 32 bits and for which source code is available. The player has to compile the cracking program and use it correctly. This is a white box challenge.

## Scenario
We are looking for a hacker who can hack randomness in itself! Go on and hack the planet!

## Write-up
First break down the "hacktheworld" string to 2 parts 7 characters and 6, as described in the code.
```
mt_srand($seed1);
$finalString .= randomString(7);

mt_srand($seed2);
$finalString .= randomString(6);
```
So you have "hackthe" for seed1 and "world" for seed2

Then identify the ord number that corresponds to each character. You can use python for that:

```
string1 = "hackthe"
string2 = "world"
for char in string1:
	print(ord(char), end=" ")
print()
for char in string2:
	print(ord(char), end=" ")
```

Compile https://github.com/openwall/php_mt_seed and run it like so:
./mt_crack expected_ord expected_ord min_seed_value max_seed_value [repeat sequence as many times as needed (7 for the first string, 6 for the second)]

string 1: ./mt_crack 104 104 97 122  97 97 97 122  99 99 97 122  107 107 97 122  116 116 97 122  104 104 97 122  101 101 97 122
string 2: ./mt_crack 112 112 97 122  108 108 97 122  97 97 97 122  110 110 97 122  101 101 97 122  116 116 97 122

More instructions can be found on the github page on how to use the tool. Find the seeds with the tool and provide them to the website.

## PoC script
?seed1=3145518921&seed2=1909564737

## Flag
csc{0nly_32_b1ts???}

## Creator
Bram Van Gaal

## Creator bio
This challenge was based on a vulnerability I found in the wild where mt_rand was used for password reset URLs. You can find more about this vulnerability at https://bramdoessecurity.com/travianz-hacked/
