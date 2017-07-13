# gradle-cache2mavenrepo
Simple python code for making Maven Repository Folder by Gradle Cache Folder

Made this code for Maven Repo of offline standalone build-environment and not using Nexus Repo.

Gradle cache folder is located "C:\Users\{{username}}\.gradle\caches\modules-2\files-2.1\" and this code utilizes that folder.
There are three problems with making Maven Repository Folder by Gradle Cache Folder.

1. Gradle cache has Dot-delimiter named folder(ex. com.fasterxml.jackson.core), bun not in Maven repo (ex.  com\fasterxml\jackson\core)
2. Gradle cache has folders with random name(ex. junit\4.12\2973d150c0dc1fefe998f834810d68f278ea58ec\junit-4.12.jar), but not in Maven repo (ex. junit\4.12\junit-4.12.jar)
3. Jar, pom are separated by folders with random name in Gradle cache, but in Maven repo, they are in one folder


* This code is for Windows. In other OSs, should change directory seperator ('\\') in code. 

* With Python 3.6.1, Gradle 4.0.1 
