#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	count = 0
	for i in text:
		if i.isalnum():
			count += 1
	return count

def get_word_length_histogram(text):
	mots = text.split()
	count = []
	lettres = 0

	for mot in mots:

		lettres = 0
		for i in mot:
			if i.isalnum():
				lettres += 1

		if lettres in range(len(count)):
			count[lettres] = count[lettres] + 1
		else:
			while lettres > len(count):
				count.append(0)
			count.append(1)

	return count

def format_histogram(histogram):
	ROW_CHAR = "*"
	for i in range(1, len(histogram)):
		if i < 10:
			print('', i, (ROW_CHAR * histogram[i]))
		else:
			print(i, (ROW_CHAR * histogram[i]))

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	ROW_CHAR = ' '
	BLOCK_CHAR = "l"
	LINE_CHAR = "¯"
	sommet = max(histogram)

	for i in range(max(histogram)):  # from 0 to len-1

		liste = [BLOCK_CHAR if i >= sommet else ' ' for i in histogram]

		print("".join(liste))
		sommet -= 1

	print('', LINE_CHAR * (len(histogram) - 1))

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
