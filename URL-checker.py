'''
https://www.codingdrills.com/practice/valid-url-checker 

 

Question: Valid URL Checker 

Write a function that checks whether a given string is a valid URL or not.
 The function should return T if the input string is a valid URL and F otherwise. 

Hint:
A valid URL starts with "http://" or "https://" 
A valid URL must contain a domain name followed by a domain extension (e.g., .com, .org, .net, etc.) 
Consider only basic URLs with HTTP/HTTPS protocols.
 You do not need to consider other protocols like FTP, telnet, etc. 
 You do not need to check for the existence of the URL on the internet, just the format. 
'''
import re
string=str(input())
test=re.search(r'^(http://|https://).+\.(com|net|org)$', string)
if test:
    print('T')
else:
    print('F')