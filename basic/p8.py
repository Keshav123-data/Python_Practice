# Q.8 Reverse a string without using [::-1].
text = "hello"
reversed_text = ""  
for char in text: # Iterate through each character in the string
    reversed_text = char + reversed_text   # added the new character to the before of the reversed string
print(reversed_text)