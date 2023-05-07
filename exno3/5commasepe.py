# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

inp = input("ENTER COMMA SEPARATED WORDS: ")
words = [word for word in inp.split(",")]
unique_words = list(set(words))
sorted_words = sorted(unique_words)
output_str = ",".join(sorted_words)
print("WORDS IN SORTED LIST: " + output_str)


















# repo created by kerston2104