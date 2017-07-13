import os
from os.path import join, dirname, join, isdir, abspath
from shutil import copyfile, rmtree


def searchFiles(path):
	# files(String List): paths including filename  
	dirs = [ join( path, f ) for f in os.listdir(path) if isdir( join(path, f)) ]
	files= [ join( path, f ) for f in os.listdir(path) if os.path.isfile( join(path, f)) ]
	# Extends files from all directory 
	for d in dirs:
		file.extend ( searchFiles ( d ) )
	
	return files
# file location example) Python- C:\temp\g2repo.py, Target Gradle Cache Folder- C:\temp\repo (will be Maven Repo)
path = join( dirname( os.path.realpath(__file__) ), "repo") 
files = searchFiles(path)

for f in files:
	# Ignore folders with random name
	# Make folders by spliting dot-delimiter foldername	
	temp = dirname( dirname(abspath(f)) )[len(path)+1:].split('\\')
	target = path + '\\' + temp[0].replace('.','\\') + '\\' + '\\'.join(temp[1:])
	print("File: " + f)
	print("Copy Target: " + target)
	if not os.path.exists(target):
		os.makedirs(target)
	# Copy jar, pom and etc
	copyfile(f, join(target, os.path.basename(f) ) )
	# Delete folders with random name, jar, pom and etc
	print("Folder Delete: " + dirname(abspath(f)))
	rmtree( dirname(abspath(f)) )
	# Delete dot-delimiter folders
for d in [ join( path, f ) for f in os.listdir(path) if ( (isdir( join(path, f))) & (f.find(".") > -1) )]:
	print("Folder Delete: " + d)
	rmtree( d )
