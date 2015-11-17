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

	parser = argparse.ArgumentParser(description="This program filters files from a directory by searching for filenames in a list")
	#parser.add_argument('-i', nargs='?', type=str, help="folder with all files", required=True)
	#parser.add_argument('-d', nargs='?', type=str, help="Tokens to search at the table ( ; separates between token)", required=True)
	parser.add_argument('-t', nargs='?', type=str, help="table to check for tokens", required=True)
	parser.add_argument('-i', nargs='?', type=str, help="column index to check", required=True)
	parser.add_argument('-f', nargs='?', type=str, help="filename column", required=True)
	parser.add_argument('-min', nargs='?', type=str, help='min percentage of a population to be sampled for a given group', required=True)
	parser.add_argument('-max', nargs='?', type=str, help='max number of samples for a given group', required=True)
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

	with open(args.t) as fileContent:
		fileList = fileContent.readlines()
		for i in fileList:
			if headerLine:
				headerLine = False;
				continue
			else:
				line = i.split('\t')
				typeToCheck = line[int(args.i)].strip()
				if typeToCheck not in objectOfTypes:
					objectOfTypes[typeToCheck] = []
					objectOfTypes[typeToCheck].append(line[int(args.f)])
				else:
					objectOfTypes[typeToCheck].append(line[int(args.f)])

		print objectOfTypes['']
		numberOfGroups = objectOfTypes.keys()
		maxNumberOfSamples = int(args.max)

		totalSampled = 0
		for i in objectOfTypes:
			maxNumber = len(objectOfTypes[i])
			minValue = int(float(args.min) * maxNumber)

			if maxNumber > maxNumberOfSamples:
				maxNumber = maxNumberOfSamples

			if minValue > maxNumber:
				minValue = maxNumber

			#print minValue
			#print maxNumber

			picked = random.sample(objectOfTypes[i], random.randint(minValue,maxNumber))

			totalSampled += len(picked)

			objectOfTypes[i] = picked

		print 'Total sample length: ' + str(totalSampled)
			

	return objectOfTypes

def writeFile(objectToWrite, args):
	
	with open(os.path.join(args.o, 'groupFilterResults.txt'), 'w') as toWrite:
		for i in objectToWrite:
			for j in objectToWrite[i]:
				toWrite.write(j + '\n')

	return True




if __name__ == "__main__":
    main()