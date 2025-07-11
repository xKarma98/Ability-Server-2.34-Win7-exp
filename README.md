# Ability-Server-2.34-Win7-exp
I am unware if anyone has tried to exploit this beyond windows XP, so I'm assuming this will be a extention to this OS.

From googling around I have noticed the vulnerability in the STOR ftp command which is used for: Uploading files.
Second I noticed this is authenticated.
Thirdly, I grabbed a copy of this binary on exploit-db popped it into IDA and noticed how the buffers had no sanitization.

With the aid of another blog I figured out how to fuzz this command because I have never done so before.
We will place that code in the fuzz-test.py
