#number of vowels in a string
input_string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)

