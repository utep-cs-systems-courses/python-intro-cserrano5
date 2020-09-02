# Imported Libraries
import sys
import re
import string

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Word dictionary
dictionary = {}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output file>")
        exit()

    # will open input file and write in it
    with open(input_file_name, 'r') as inputFile:
        for line in inputFile:
            line = line.strip()     # this will remove the leading spaces and newline character
            line = line.lower()     # this will convert characters in line to lowercase, avoid case mismatch
            line = re.sub("-", " ", line)

            line = re.sub(r"[,.;@#?!&$]+\ *", " ", line)   # removes punctuation marks from the line
            line = line.translate(line.maketrans("", "", string.punctuation))

            words = re.split('[ \t]', line)
            for word in words:
                if word == "":
                    break
                if word in dictionary:
                    dictionary[word] = dictionary[word] + 1
                else:
                    dictionary[word] = 1
    with open(output_file_name, "w")as outputFile:
        for word in sorted(dictionary):
            outputFile.write(word + " " + str(dictionary[word]) + "\n")
    outputFile.close()