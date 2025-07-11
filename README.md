# Ability-Server-2.34-Win7-exp
I am unware if anyone has tried to exploit this beyond windows XP, so I'm assuming this will be a extention to this OS.

# Disclaimer: I am not a professional, just some unemployed idiot
This is to the best of my knowledge.

From googling around I have noticed the vulnerability in the STOR ftp command which is used for: Uploading files.
Second I noticed this is authenticated.
Thirdly, I grabbed a copy of this binary on exploit-db popped it into IDA and noticed how the buffers had no sanitization.

With the aid of another blog I figured out how to fuzz this command because I have never done so before.
We will place that code in the fuzz1.py

With 1000 chars it crashed now we need the pattern offset, optimially I just used mona to save some time `!mona po 67423167`

<img width="530" height="219" alt="dM" src="https://github.com/user-attachments/assets/db2fbc0c-aab4-439c-bf83-b8fbd750537f" />


After we collect the offset, we need to do a EIP overwrite to ensure we have the control.
What you can do if you want this manually is take your current offset and add B or C to it, B will appear as `424242424` C will be `4343434343`

<img width="317" height="300" alt="44124" src="https://github.com/user-attachments/assets/9bb091a5-d8bf-4bc8-a49f-e418ff0f0ad4" />

We have done so. But now we need to eliminate the bad chars, otherwise we will have some serious issues.
When you search go to your ESP in the cpu registers and scroll down to the 4 b's of the EIP overwrite and search from 00 to FF.
I have discovered the following characters being bad: `0x0 0xA 0xD`

# Getting our gadget.
1. The first step I took was running `!mona find -s "\xFF\xE4"` this is the opcode for jmp esp -> jmp extended stack pointer.
2. Running into some issues I didn't go back to check, but we will choose ntdll.dll for this exploit. Prior I had issues with GDI32.dll, USER32.dll.
3. In mona click search for a sequence of commands: `jmp esp` Once that has been done you will find a address in the module ntdll.dll of `0x77f1E871` opcode: `xff xe4`

# Lastly, we need to write a payload.
This will remove the bad chars in the exploit for it to make work.
Also, when writing I noticed the 16 0x90's aka a NO op in assembly which literally does nothing, I have inserted 32 instead of 16 of them and that's when my payload initially began to work.


### Purpose of this NOP sled?
##### Source: https://en.wikipedia.org/wiki/NOP_slide
(no-operation) instructions meant to "slide" the CPU's instruction execution flow to its final, desired destination whenever the program branches to a memory address anywhere on the slide. 


msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LPORT=4444 -b '\x00\x0a\x0d' -f python -e x86/alpha_mixed


# End results.
<img width="589" height="295" alt="asdM" src="https://github.com/user-attachments/assets/5fac1b66-fc98-4bae-af77-bfb6534b4b80" />

<img width="518" height="228" alt="asM" src="https://github.com/user-attachments/assets/b06cfa37-4945-45dd-a3cc-9acf4bc9217e" />


# Sources:
https://blog.naver.com/sjhmc9695/221495713802 # Credit for initial skeleton payload.

https://iwayinfocenter.informationbuilders.com/TLs/TL_soa_ism_ftp/source/ftpserver_config41.htm

https://wmsmartt.wordpress.com/2011/11/25/ability-ftp-2-34-stack-based-buffer-overflow/
