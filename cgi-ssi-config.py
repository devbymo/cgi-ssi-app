#!C:\Users\meem2\AppData\Local\Programs\Python\Python38-32
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
my_str = form.getvalue('mail')

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#user_name = "Hello!!!, he said ---and went."

# To take input from the user
#my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)




