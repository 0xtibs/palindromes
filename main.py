import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = ", len(pali_list), "\nThey have been saved into Palindrome file!")
textfile = open("palindromes.txt", 'w')
for elements in pali_list:
    textfile.write(elements + '\n')
textfile.close()