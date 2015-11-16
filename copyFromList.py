import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys
from datetime import datetime
import random


def main():

	parser = argparse.ArgumentParser(description="This program copies files from one directory to other based on a filtering list of files")
	#parser.add_argument('-i', nargs='?', type=str, help="folder with all files", required=True)
	#parser.add_argument('-d', nargs='?', type=str, help="Tokens to search at the table ( ; separates between token)", required=True)
	parser.add_argument('-l', nargs='?', type=str, help="list", required=True)
	parser.add_argument('-q', nargs='?', type=str, help="query folder", required=True)
	parser.add_argument('-r', nargs='?', type=str, help="results folder", required=True)


	args = parser.parse_args()

	isDone = copyFiles(args)


	if isDone:
		print 'Done'
	else:
		print 'Error while writing file'

def copyFiles(args):

	onlyfiles = [ f for f in listdir(args.q) if isfile(join(args.q,f)) ]

	with open(args.l, 'r') as listToUse:
		lines = listToUse.readlines();
		for i in lines:
			fileToCheck = i.strip('\n')
			if i in onlyfiles:
				shutil.copyfile(join(args.q,i), args.r)



	return True

if __name__ == "__main__":
    main()