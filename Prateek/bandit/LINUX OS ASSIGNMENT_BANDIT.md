### LINUX OS ASSIGNMENT

BANDIT

level 0 : ssh bandit0@bandit.labs.overthewire.org -p 2220

level 0-1 : commands used are ls and cat

&#x20; ls  find files and cat  read files

level 1-2 : commands used are  ls and cat ./-

\-> -  is treated as stdin, so ./- forces it as filename

level 2-3 :  command : cat -- "--spaces in this filename--"

&#x20;-> quotes is used to handle spaces in file names

level 3-4 : commands :  ls -a , cat ...Hiding-From-You

&#x20;-> -a shows hidden files starting with .

Level 4-5 : commands : ls , file ./\* , cat ./-file07

\->  file identifies readable file among binaries

level 5-6 : commands : find . -type f -size 1033c ! -executable , cat ./maybehere07/.file2

Alternative one line commant : find . -type f -size 1033c ! -executable -exec cat {} \\;

\-> to find files efficiently nstead of manual search

level 6-7 : commands : find / -user bandit7 -group bandit6 -size 33c 2>/dev/null , cat /var/lib/dpkg/info/bandit7.password

\-> Searches entire system with filters and 2>/dev/null removes permission denied errors

level 7-8 : command : grep "millionth" data.txt

\-> grep finds lines with keyword efficiently

level 8-9 : command : sort data.txt | uniq -u

\->  sort groups duplicates and uniq -u shows unique lines

level 9-10 : command : strings data.txt | grep "="

\-> strings extracts readable text from binary

level 10-11 : command : base64 -d data.txt

\-> decode Base64 data to original readable text



