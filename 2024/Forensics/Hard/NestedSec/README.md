# NestedSec: Unveiling the Shadows

## Category
[Forensic|Stego]

## Estimated difficulty
[Hard]

## Description
The challenge is multilayered which is what raises the difficulty. There are 4 stages in total. All the stages are nested. The challenge itself is a combination of steganography and forensics. 

## Scenario
You are a skilled cybersecurity analyst working for a top-secret intelligence agency. Recently, you intercepted a communication indicating a potential security threat from an unknown hacker group. As you dig deeper, you discover that they've hidden a crucial piece of information within a series of encrypted files. Your mission is to unravel the layers of encryption and uncover the hidden message.
We have vague info that the attackers locked something with one of the commands used in the attack.

## Write-up
- The players will be given a folder with 2 files inside, "filetype.zip" and "hidden.wav".
- The players will have to open the "hidden.wav" with a tool like sonic-visualizer and add a spectrogram layer to reveal a QR code. Once scanned, the QR code will reveal the message "Hello There, good job, here's the password: 5teg0_F0r_L1fe".
- The password then will be used to upzip the "filetype.zip" file. Inside there is the file "filetype.exe".
- The file "filetype.exe" is a txt file masqueraded as an exe file. Once the players remane the file, they will find a base64 code inside.
- The players will need to decode the base64 and recognize that it is in reality a .pcap file (wireshark file format).
- Once the players reconstruct the base64 code back to .pcap file they will need to open it in wireshark and find 2 things. 
- The first is the "attack1.zip" file which can be retrieved from the HTTP traffic and wireshark can automatically reconstruct the packages. Note that the "attack1.zip" is password protected.
- The second is that they will need to use some special filters to determine the kind of the activity and what command the attacker used. More information can be found here: https://www.infosecmatter.com/detecting-network-attacks-with-wireshark/ (The filter the players need to use is "arp.dst.hw_mac==00:00:00:00:00:00" which shows that the attacker performed an ARP scan with the command "arp-scan -l", which is the password).
- After the players unzip the "attack1.zip" file, they will find the "nviso1.pdf" file which hides the "flag.txt" file. They can extract it with a linux tool like "pdfextract".

Hints:
1) An interesting fact is that there are many layers to sound.
2) Not everything is what it seems at first. Names have power. Maybe change things a little bit ;)
3) Everything is just data and can take many different forms, from 1 and 0 to txt, exe, jpg, wav etc. You can manipulate data as you will.
4) Could somebody have used the command used by the attacker as a way to lock something? No, that would be dumb, who would do something like this?
5) Everything seems innocent at first glance but some things are hidden.

## Flag
CSC{Achievement_Unlocked_:)}

## Creator
Konstantinos Pantazis

## Creator bio
Konstantinos is currenlty a SOC analyst at NVISO with experience in both blue and red sides of cybersecurity. His prior positions were as a consultant and he has also expirience in IAM, QA testing, Penetration Testing, Red Teaming and SOC. He also holds a bachelor's degree in IT engineering.

You can find him here:
https://github.com/kostas-pa
https://gr.linkedin.com/in/kopantazis

