# [Explore]

## Category
Web

## Estimated difficulty
Easy

## Description
The hints to the flag are hidden in Header values only visible through OPTIONS request. 

## Scenario
You think you explore like a pro? Give it a shot and find the flag. 

## Write-up
Opening the IP on a browser will give us a blank webpage with the text "My father told me to explore all my options before I make a choice". 
Let's try to use OPTIONS to see what we can do in this page.
`curl -X OPTIONS localhost`

This returns 2 posibilities. HEAD and GET. We already ran GET and nothing came up. Let's give HEAD a shot.
`curl -I localhost`
```
HTTP/1.1 200 OK
X-Powered-By: Express
FLAG: flag is hidden under /flag endpoint...
Date: Mon, 09 Oct 2023 15:19:18 GMT
Connection: keep-alive
Keep-Alive: timeout=5
```

So there is another endpoint that has the flag. Let's GET that one.
`curl localhost/flag`

This returns "Not Quite there". 
Let's try OPTIONS again.
`curl localhost/flag -X OPTIONS`

We get 4 options, GET,POST,HEAD,OPTIONS. It's weird this returns options. This must be custom coded. Let's view the headers as well.
```
*   Trying 127.0.0.1:80...
* Connected to localhost (127.0.0.1) port 80 (#0)
> OPTIONS /flag HTTP/1.1
> Host: localhost
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< X-Powered-By: Express
< FLAG: csc{0pt10n5_4r3_1mp0r74nt}
< Content-Type: text/html; charset=utf-8
< Content-Length: 21
< ETag: W/"15-u2UBAkhipd++OLgh+LlfM20nPM4"
< Date: Mon, 09 Oct 2023 15:21:35 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
< 
* Connection #0 to host localhost left intact
GET,POST,HEAD,OPTIONS   
```

## PoC script
curl -X OPTIONS -v localhost/flag

## Flag
csc{0pt10n5_4r3_1mp0r74nt}

## Creator
Konstantinos Papanagnou

## Creator bio
Konstantinos is a Senior Penetration Tester at NVISO. His main interest lies in Red Teaming. You can find more about him on linkedin https://www.linkedin.com/in/konstantinos-papanagnou-7989ba195/ 
