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

	parser = argparse.ArgumentParser(description="This program filters an isolate file for filenames in a list")
	#parser.add_argument('-i', nargs='?', type=str, help="folder with all files", required=True)
	#parser.add_argument('-d', nargs='?', type=str, help="Tokens to search at the table ( ; separates between token)", required=True)
	parser.add_argument('-t', nargs='?', type=str, help="table to check for tokens", required=True)
	parser.add_argument('-l', nargs='?', type=str, help="list to use for filtering", required=True)
	parser.add_argument('-f', nargs='?', type=str, help="filename column", required=True)
	parser.add_argument('-o', nargs='?', type=str, help='output file directory', required=True)


	args = parser.parse_args()

	typesFiltered = filterFiles(args)

	isDone = writeFile(typesFiltered, args)

	if isDone:
		print 'Done'
	else:
		print 'Error while writing file'


def filterFiles(args):
	print 'Running'

	objectOfTypes = {}
	headerLine = True;

	filesToCheck = []
	toWritw = []

	with open(args.l, 'r') as listToUse:
		lines = listToUse.readlines();
		for i in lines:
			filesToCheck.append(i.strip('\n').strip())

	with open(args.t) as fileContent:
		fileList = fileContent.readlines()
		for i in fileList:
			if headerLine:
				headerLine = False;
				continue
			else:
				line = i.split('\t')
				fileToCheck = line[int(args.f)].strip()
				if fileToCheck in filesToCheck:
					toWrite.append(line)

			
	return toWrite


def writeFile(objectToWrite, args):
	
	with open(os.path.join(args.o, 'isolatesFiltered.txt'), 'w') as toWrite:
		for i in objectToWrite:
			toWrite.write(j + '\n')

	return True




if __name__ == "__main__":
    main()