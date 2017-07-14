import os
from os.path import join, dirname, join, isdir, abspath
from shutil import copytree, move, rmtree

# directroy separator. Windows: \\ , Linux: /
separator = os.sep

def searchFiles(path):
	# fileList(String List): paths including filename 
	fileList = []
	for path,pathname,filenames in os.walk(path):
		for f in filenames:
			fileList.append( join (path, f) )
	
	return fileList

# file location example) 
# Python Code- C:\temp\g2repo.py, 
# Target Gradle Cache Folder- C:\temp\files-2.1
# Maven Repo- C:\temp\files-2.1_repo
gradle_cache = join( dirname( os.path.realpath(__file__) ), "files-2.1") # Set your own Gradle Cache Folder path

# Maven Repo path
path = gradle_cache + "_repo"
copytree(gradle_cache, path)

files = searchFiles(path)

for f in files:
	# Ignore folders with random name and Make folders by spliting foldername with dot-delimiter 
	temp = dirname( dirname(abspath(f)) )[len(path)+1:].split(separator)
	target = path + separator + temp[0].replace('.',separator) + separator + separator.join(temp[1:])
	print("File: " + f)
	print("Copy Target: " + target)
	if not os.path.exists(target):
		os.makedirs(target)
	# Move jar, pom and etc
	move(f, join(target, os.path.basename(f) ) )
	# Delete folders with random name, jar, pom and etc
	print("Folder Delete: " + dirname(abspath(f)))
	rmtree( dirname(abspath(f)) )
# Delete dot-delimiter folders
for d in [ join( path, f ) for f in os.listdir(path) if ( (isdir( join(path, f))) & (f.find(".") > -1) )]:
	print("Folder Delete: " + d)
	rmtree( d )
