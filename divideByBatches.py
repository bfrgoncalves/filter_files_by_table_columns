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

	parser = argparse.ArgumentParser(description="This program copies files from one directory to other in btaches based on a filtering list of files")
	#parser.add_argument('-i', nargs='?', type=str, help="folder with all files", required=True)
	#parser.add_argument('-d', nargs='?', type=str, help="Tokens to search at the table ( ; separates between token)", required=True)
	parser.add_argument('-l', nargs='?', type=str, help="list", required=True)
	parser.add_argument('-q', nargs='?', type=str, help="query folder", required=True)
	parser.add_argument('-m', nargs='?', type=str, help="max per batch", required=True)
	parser.add_argument('-r', nargs='?', type=str, help="results folder", required=True)


	args = parser.parse_args()

	isDone = copyFiles(args)


	if isDone:
		print 'Done'
	else:
		print 'Error while writing file'

def copyFiles(args):

	onlyfiles = [ f for f in listdir(args.q) if isfile(join(args.q,f)) ]
	#print onlyfiles
	countFolders = 1
	countNumberFiles = 0

	newFolder = 'batch_' + str(countFolders)

	with open(args.l, 'r') as listToUse:
		lines = listToUse.readlines();
		for i in lines:
			fileToCheck = i.strip('\n').strip()
			if fileToCheck in onlyfiles:
				if countNumberFiles == int(args.m):
					countNumberFiles = 0
					countFolders += 1
					newFolder = 'batch_' + str(countFolders)

				countNumberFiles += 1
				filename, extension = os.path.splitext(fileToCheck);
				filename = filename.replace('.','_')
				filenameToUse = filename + extension
				shutil.copyfile(join(args.q,fileToCheck), join(args.r, newFolder, filenameToUse))



	return True



if __name__ == "__main__":
    main()