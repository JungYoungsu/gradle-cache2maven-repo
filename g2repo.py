import os
from os.path import join, dirname, join, isdir, abspath
from shutil import copytree, copyfile, rmtree

# directroy separator. Windows: \\ , Linux: /
separator = os.sep

def searchFiles(path):
	# files(String List): paths including filename  
	dirs = [ join( path, f ) for f in os.listdir(path) if isdir( join(path, f)) ]
	files= [ join( path, f ) for f in os.listdir(path) if os.path.isfile( join(path, f)) ]
	# Extends files from all child directory 
	for d in dirs:
		files.extend ( searchFiles ( d ) )
	
	return files
	

# file location example) 
# Python Code- C:\temp\g2repo.py, 
# Target Gradle Cache Folder- C:\temp\cache
# Maven Repo- C:\temp\cache_repo
gradle_cache = join( dirname( os.path.realpath(__file__) ), "cache") # Set your own Gradle Cache Folder path

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
	# Copy jar, pom and etc
	copyfile(f, join(target, os.path.basename(f) ) )
	# Delete folders with random name, jar, pom and etc
	print("Folder Delete: " + dirname(abspath(f)))
	rmtree( dirname(abspath(f)) )
# Delete dot-delimiter folders
for d in [ join( path, f ) for f in os.listdir(path) if ( (isdir( join(path, f))) & (f.find(".") > -1) )]:
	print("Folder Delete: " + d)
	rmtree( d )
