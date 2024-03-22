## Hidden in Plain Sight

#### Challenge Difficulty: Easy
#### Topic: stego
#### Author: d151nt3gr4t0r


The challenge provides us with an image. 

We can attempt to find the flag hidden in the challenge's metadata, but it's not there. The next best thing is to check whethere there's a hidden file embedded in the image. To do that, we can use steghide.

`steghide extract -sf challenge.jpg`
When it prompts for a password just skip it over by pressing enter.

Success! We now have a new file which contains the flag!

Flag: csc{st3g_15_4bs0lut3ly_4m4z1n9!!}