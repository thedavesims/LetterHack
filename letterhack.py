print "LetterHack - Letterpress Word Solver"

#The list of letters that appear on your letterpress screen
letter_string = "TDGZGUWPZDVTGBOSGXNREAINN"
#Convert letters to lowercase and split it into a list
letters = list(letter_string.lower())
#list to hold our words loaded from our text file
words=[]

found_words=[]
#load words from dictionary file
with open("enable.txt") as f:
	for line in f.readlines():
		words.append(line.strip()) #strip whitespace and append to list

for word in words: #for each word in the list
	word_as_list = list(word)
	for letter in letters:
		if letter in word_as_list:
			word_as_list.remove(letter)
	if len(word_as_list) == 0:
		found_words.append(word)


found_words.sort(key=len)

print "Top 5 Words by length: "
for word in found_words[-5:]:
	print word

