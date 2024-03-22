## Lost and Found

#### Challenge Difficulty: Medium
#### Topic: filesystem, magic bytes
#### Author: d151nt3gr4t0r


The challenge provides us with a filesystem. 

We need to mount the filesystem and navigate into the lost+found directory. Within that directory, there's an interesting file, called .flag.

Retrieving that file back to our local filesystem will be useful. Let's use the file command on this file to identify what this file is. It looks like it's data, which is not normal. Let's strings this file. 

To an experienced eye this looks like an image, but it is not identified for some reason. When this happens it's good to verify if the "Magic Bytes" are modified. The magic bytes are the first bytes to a file which are used to identify its filetype. We can tell this is a png, so we need to replace the first bytes to the typical PNG magic bytes. We can find the right bytes with an online search. 

After we replace with the correct bytes using hexeditor, we can run "file" again and now it identifies a png image as the filetype. Opening the image reveals the flag.

Flag: csc{f1l3_5y5t3m5_4r3_c00l!}