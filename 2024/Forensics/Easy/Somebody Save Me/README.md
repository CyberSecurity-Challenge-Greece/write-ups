## Somebody Save Me

#### Challenge Difficulty: Easy
#### Topic: Filesystem
#### Author: d151nt3gr4t0r

The challenge provides us with a file that has no extension called sys. After running 'file' on this file, we retrieve the following output. 

`sys: Linux rev 1.0 ext4 filesystem data, UUID=d63d05f2-7e05-4e45-91ff-4495ce82b197 (extents) (64bit) (large files) (huge files)`

We can tell it's a filesystem. We can mount it, but there is nothing but a test file in the filesystem. This means that the flag has probably been deleted. 
If we're lucky and it was not been overwritten, we will be able to retrieve the file contents, even if the file is gone. This is because when we delete a file, the only thing being deleted in the background is the file descriptor and not the file contents. The file contents remain on disk until they are overwritten by another file. This is to save both energy and increase the disk's lifespan (Especially for HDD disks).

1st intended solution:
Let's open the filesystem using Autopsy. Autopsy can read the file system and look for file contents even if there is no file descriptor in place. It looks for starting sequences of files and ending sequences like EOF to identify where the file contents end. As it scans the file system, you will see some txt files popping up, such as passwords.txt, confidential.txt. In one of these files there is a base64 string which if when you decrypt, contains the final flag.

2nd intended solution: 
Using strings on the filesystem can yield all the previous file contents that existed. We can manually go through the output and make sense out of the text. Somewhere in the text, there is a base64 sequence, which you can decode to retrieve the flag.

Final flag: csc{1_w45_l05t_4nd_y0u_f0und_m3!}