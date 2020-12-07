# gradle-cache2maven-repo
Simple python code for making Maven Repository Folder via Gradle Cache Folder

Gradle cache folder is located "C:\Users\\{{username}}\\.gradle\caches\modules-2\files-2.1\" in defalut setting. (in Linux: ~/.gradle/*)

*g2repo.py* utilizes that folder and also solves three problems with coverting Gradle Cache Folder to Maven Repository Folder.

1. Gradle cache has folder named dot-delimiter (ex. com.fasterxml.jackson.core), but Maven repo does not (ex. com\fasterxml\jackson\core)
2. Gradle cache has folders with random name (ex. junit\4.12\2973d150c0dc1fefe998f834810d68f278ea58ec\junit-4.12.jar), but Maven repo does not(ex. junit\4.12\junit-4.12.jar)
3. Jar, pom are separated by folders with random name in Gradle cache, but they are in one folder in Maven repo.


* with Python 3.6.1, Gradle 4.0.1 
> \# Before executing, set your gradle cache folder path in code.

> python g2repo.py
