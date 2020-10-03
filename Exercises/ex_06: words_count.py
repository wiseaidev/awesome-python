"""
File: words_count.py
compute the numbre of words and the average word length in a given sentence .
"""
if __name__ == "__main__":
	try:
		sentence = input("Enter your sentence: ").strip()
		words_list = sentence.split(' ')
		count0 = len(words_list)
		count1 = sentence.count(' ') + 1
		assert count1 == count0
		print(f"there are {count0} words in this sentence.")
		words_len = [len(word) for word in words_list]
		word_avg = sum(words_len)/count0
		print(f"the average word length is {word_avg:.2f} letters.")
	except Exception as e:
		print(e)