import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys
from datetime import datetime


def main():

	parser = argparse.ArgumentParser(description="This program filters files from a directory by searching for filenames in a list")
	parser.add_argument('-i', nargs='?', type=str, help="folder with all files", required=True)
	parser.add_argument('-d', nargs='?', type=str, help="Tokens to search at the table ( ; separates between token)", required=True)
	parser.add_argument('-o', nargs='?', type=str, help='Destination folder', required=True)
	parser.add_argument('-t', nargs='?', type=str, help="table to check for tokens", required=True)


	args = parser.parse_args()

	filterFiles(args)

def filterFiles(args):
	print 'Running'

	with open(args.t) as fileContent:
		fileList = fileContent.readlines()

		for i in fileList:
			fileToCheck = os.path.join(args.i, i)
			print fileToCheck
			print os.path.isfile(fileToCheck)
			if os.path.isfile(fileToCheck):
				print 'AQUI'
				shutil.copyfile(fileToCheck, args.o)

	print 'Done'



if __name__ == "__main__":
    main()