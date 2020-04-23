import string
def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

# Total number of words in the file, by adding up the frequencies in the histogram
def total_words(hist):
    return sum(hist.values())

# Number of different words in the dictionary (number of items in the dictionary)
def different_words(hist):
    return len(hist)

hist = process_file('emma.txt')   # Create word histogram
words = different_words(hist)     # Number of different words
total = total_words(hist)         # Total number of workds

print(hist)
print("Different words in file =", words)
print("Total words in file =", total)

