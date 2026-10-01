# Q. Count the number of characters in a string.

text = " HELLO "
print("The number of characters in the string is:", len(text))

# Q. Reverse a string.

reverse = text[::-1]
print("Reversed string:", reverse)

# Q. Check whether a string is palindrome.

if text == text[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")

# Q. Count the number of vowels in a string.

vowel_count = 0
for i in text:
    if i in 'aeiouAEIOU':
        vowel_count += 1
print("The number of vowels in the string is:", vowel_count)

# Q. Count the number of consonants in a string.

consonants_count = 0
for i in text:
    if i not in 'aeiouAEIOU':
        consonants_count += 1
print("The number of consonants in the string is:", consonants_count)

# Q. Count the number of words in a sentence.

sentence = "This is a sample sentence like a sentence"
words = sentence.split(" ")
print("The number of words in the sentence is:", len(words))

# Q. Convert a string to lowercase.
lower = text.lower()
print("Lowercase String:", lower)

# Q. Remove leading and trailing whitespace from a string.
new_text = text.strip()
print("New string :", new_text)

# Q. replace word with new word

new_word = text.replace("HELLO", "HI")
print("new word:", new_word)

# Q. Count the number of occurrences of a character in a string.

counts = new_text.count("H")
print("The number of repeated character in the string is:", counts)

# Q. Find the first occurrence of a character in a string.

char = new_text.find("H")
print("The first occurrence of the character in the string is:", char)

for i in range(len(new_text)):
    if new_text[i] == "L":
        print("The first occurrence of the character in the string is:", i)
        break
    else: 
        print("character not found")

# Q. Check whether a string contains a Python or not.

string = "I'm learning Python Programming."

if "Python" in string:
    print("Yes, 'Python' is present in the string.")
else:
    print("No, 'Python' is not present in the string.")

# Q. Extract the first name from a full name.

full_name = "Keshav Shinde"

first_name = full_name.split()[0]
print("First name:", first_name)

# Q. Extract the domain from an email address.

email ="keshavshinde9881@gmail.com"
domain = email.split('@')[1]
print("Domain name:", domain)

# Q. Count the frequency of each word in a sentence.
frequency = {}

for i in words:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[1] = 1

# Q. Find the longest word in a sentence.

largest_word = words[0]
for i in words:
    if len(i) > len(largest_word):
        largest_word = i
print("largest word in sentence is:", largest_word)

# Q. Find the shortest word in a sentence.

shortest_word = words[0]
for i in words:
    if len(i) < len(shortest_word):
        shortest_word = i
print("shortest word in the sentence is:", shortest_word)

# Q. Generate a username from a full name.

username = full_name.split()[0].lower() + full_name.split()[1].lower()
print("Username:", username)
