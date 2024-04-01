# Forecasting Access

## Category
Web

## Estimated difficulty
Hard

## Description
The player needs to identify the adminpanel, bypass the localhost restriction utilizing the "X-Forwarded-Host" header and then reverse the session token, bruteforce the secret key, and finally sign their own administrator key. Once done, they can access the admin panel and retrieve the flag.

## Scenario
When you don't like the weather, change it. Locate the admin panel, hack into it and retrieve your flag.

## Write-up
Looking for robots.txt, we can identify a disallow entry on adminpanel. 
Attempting to access the admin panel, we get an error "Remote Users are not allowed to access this interface!". 
Utilizing the "X-Forwarded-Host" header and setting it to "127.0.0.1" bypasses this check and we get a different error, "Access Denied".
The application obviously performs checks based on the session cookie to identify if an admin is logged in. However, changing the session token gets us nowhere.
The session token is in a JSON format. 
var visitor_cookie = {"info": {"rng":"876546278357619", "username": "visitor", "role":"visitor"}, "signature":""}

It's noticable that there is a signature to sign the cookie and verify it has not been changed. Pasting the signature we have from the latest session token in hash-identifier, we can see it's a SHA1 hash. The value it hashes, are the contents of "info" {"rng":"876546278357619", "username": "visitor", "role":"visitor"} as a string. However, the hash of this value is not the same with the signature, indicating there's HMAC-SHA1 used instead. The secret key can be bruteforced with kali's rockyou list. Writing a simple python script to bruteforce the token, can identify the secret to the value "secret123". Using this value as a key, we can sign arbitrary tokens and change our identity and role. 
Forge one token with the values "admin" in both username and role. if you navigate to the front page, you'll notice that the token has been accepted by the application and the name "Admin" instead of "Visitor" is displayed in the Welcome message.

You can then send that token to the admin panel, chaining it to the first bypass we identified, and retrieve the flag.


## PoC script
The script can be found in private/exploit.py

## Flag
csc{c0ngr4t5_y0u_kn0ck3d_m3_ou7}

## Creator
Konstantinos Papanagnou

## Creator bio
Konstantinos Papanagnou is a Senior Penetration Tester at NVISO Security. He is also the Lead Technical Director of Cyber Security Challenge Greece.
