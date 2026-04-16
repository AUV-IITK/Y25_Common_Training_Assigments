Bandit Wargame Solutions (Level 0–10)
Level 0 → 1
Command: ssh bandit0@bandit.labs.overthewire.org -p 2220 cat readme

Explanation: Used the cat command to read the file and obtain the password for the next level.

Level 1 → 2
Command: ls cat ./-

Explanation: The file name is -, which is a special character. Using ./ ensures it is treated as a file in the current directory.

Level 2 → 3
Command: ls cat "spaces in this filename"

Explanation: The file name contains spaces, so quotes are used to handle it correctly.

Level 3 → 4
Command: ls -a cat .hidden

Explanation: Used ls -a to list hidden files. The password was inside .hidden.

Level 4 → 5
Command: ls file ./* cat ./-file07

Explanation: Used the file command to identify readable files. Then used cat to open the correct file.

Level 5 → 6
Command: find . -type f -size 1033c cat ./file

Explanation: Used find to locate a file of exact size (1033 bytes), then read it.

Level 6 → 7
Command: find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null cat /path/to/file

Explanation: Searched system-wide for a file with specific user, group, and size. Ignored permission errors.

Level 7 → 8
Command: ls cat data.txt | grep millionth

Explanation: Used grep to find the line containing the word "millionth".

Level 8 → 9
Command: sort data.txt | uniq -u

Explanation: Sorted the file and used uniq -u to find the unique line.

Level 9 → 10
Command: strings data.txt | grep =

Explanation: Used strings to extract readable text and grep to find the password containing '='.

Level 10 → 11
Command: base64 -d data.txt

Explanation: Decoded the Base64 encoded content to get the password.

Notes
All commands were executed on the Bandit server using SSH.
Each level required understanding of basic Linux commands.
Brute force was not used; logical command usage was applied.
<img width="784" height="292" alt="image" src="https://github.com/user-attachments/assets/96d62a89-351b-446e-8e58-e852b5084a3c" />
<img width="1130" height="289" alt="image" src="https://github.com/user-attachments/assets/f4f9af02-37dc-439e-b20c-cf9e858b4f1e" />
<img width="1256" height="335" alt="image" src="https://github.com/user-attachments/assets/3100536f-11aa-4ccd-94d7-4da350a74ca7" />



