## Title: Reversible is Crackable
## Details:
* difficulty: Easy
* category: Reverse 
* author: Sarmed
* flags: Flag {Reverse Engineered}

## Description:
Reverse engineering a file can always lead to great exploits. Logic is breakable. 

## Hint:
The secret lies in the conditions.

## Intended Learning and outcome:

With the given challenge, I was able to understand how to make your own algorithm to encrypt, compare, and decrypt secrets. And how weak logic can be exploited. 

## Solution: 

There are 2 files in this challenge, one is a python file, and the other is an executable. When we download and run both, they are showing and asking for the same thing which is password for an admin user. We open the python file to review the script and see a custom encryption and decryption algorithm that is converting the user's password input into an encrypted value and then comparing it to a certain string. The string looks like the encrypted password of the admin, we are shown a key as well. We can call the decrypt function on that string and print the value using **print(decrypt(key, "\x1dNRL[\x06qD[RD"))**, we find the password which is **Hello world**. We run the script again, enter the password and see Success message, we run the executable file again too, enter the password, and see the flag.

........




