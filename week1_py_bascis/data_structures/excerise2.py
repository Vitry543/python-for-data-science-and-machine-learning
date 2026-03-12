# word frequency counter
sentence=input("Enter a sentence: ")

# split the sentence into words
words=sentence.split()

# create a dictionary to store word frequencies
word_freq={}

# # count the frequency of each word
# for word in words:
#     if word in word_freq:
#         word_freq[word]+=1
#     else:
#         word_freq[word]=1

# # print the word frequencies
# for word,freq in word_freq.items():
#     print(word,freq)

# count the frequency of each word in a case-insensitive manner
for word in words:
    word=word.lower()
    if word in word_freq:# here in if condition it will check if the word is already in the dictionary
        word_freq[word]+=1
    else:
        word_freq[word]=1

# print the word frequencies
for word,freq in word_freq.items():
    print(word,freq)

print(word_freq)
