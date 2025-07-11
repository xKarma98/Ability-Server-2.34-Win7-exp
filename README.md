# Ability-Server-2.34-Win7-exp
I am unware if anyone has tried to exploit this beyond windows XP, so I'm assuming this will be a extention to this OS.

From googling around I have noticed the vulnerability in the STOR ftp command which is used for: Uploading files.
Second I noticed this is authenticated.
Thirdly, I grabbed a copy of this binary on exploit-db popped it into IDA and noticed how the buffers had no sanitization.

With the aid of another blog I figured out how to fuzz this command because I have never done so before.
We will place that code in the fuzz1.py

With 1000 chars it crashed now we need the pattern offset, optimially I just used mona to save some time `!mona po 67423167`
<img width="530" height="219" alt="dM" src="https://github.com/user-attachments/assets/db2fbc0c-aab4-439c-bf83-b8fbd750537f" />


After we collect the offset, we need to do a EIP overwrite to ensure we have the control.
<img width="317" height="300" alt="44124" src="https://github.com/user-attachments/assets/9bb091a5-d8bf-4bc8-a49f-e418ff0f0ad4" />

We have done so. But now we need to eliminate the bad chars, otherwise we will have some serious issues.
