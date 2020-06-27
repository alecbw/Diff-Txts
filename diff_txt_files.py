import sys
import os
import argparse
import logging
import csv
import difflib

logger = logging.getLogger()
logger.setLevel(logging.INFO)


argparser = argparse.ArgumentParser()
argparser.add_argument('-file1', nargs='?', default="all", help="The name of your file")
argparser.add_argument('-file2', nargs='?', default="all", help="The name of your file")
# argparser.add_argument('-output', nargs='?', default="csv", help="What output type you want (txt or csv). Default behavior is csv")

args = argparser.parse_args()

text1 = open(args.file1).readlines()
text2 = open(args.file2).readlines()


output_list = []
for n, line in enumerate(difflib.unified_diff(text1, text2)):
	output_list.append(line)

print(f"There are {len(output_list)} diff'd lines")

with open(f"Diffed Result.txt", "w") as f:
	f.write("\n".join(output_list))



# TODO WIP
def convert_pdf_cid_characters(line):
	split_line = line.split(" ")
	for n, word in enumerate(split_line):
		if "(cid" in word:
			print(word)
			word = word.lower().split('(')[1]
			word = word.split(')')[0]
			ascii_num = word.split(':')[-1]
			ascii_num = int(ascii_num)
			split_line[n] = chr(ascii_num)  # 66 = 'B' in ascii
	
	return " ".join(split_line)