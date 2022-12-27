
# Malicious_Packages

##

![alt text](https://github.com/oz105/phishing_links/blob/main/img/img.png)

### FOLDER

1. In "Codes" we have: 

      1. "building_tgz_meta_data.py" - This file runs and collects all the "malware" packages from "github advisory", then it searches in 8 different mirrors to find 
         said packages. if it finds new packages, it downloads them to a folder that was pre determined as well as gather data about the package.
         code outputs: csv file for new packages metadata, json file for new packages metadata, downloded packages in pre determined folder,
         json file for all "github advisory's" malware packages in a pre determined range. 
            
            to run this file you need a couple of things:
            1) to install 5 packages "requests", "beautifulsoup4", "csv", "urllib3", "wget".
               use:
                  1. "pip install requests"
                  2. "pip install beautifulsoup4"
                  3. "pip install csv"
                  4. "pip install urllib3"
                  5. "pip install wget"

            2) to change 4 parameters:
                  1. (X_start) - (int) the first page to be searched in "github advisory" for malware packages
                  2. (X_finish) - (int) the last page to be searched in "github advisory" for malware packages
                  3. (folder_url) - (str) the complete path to the folder you wish the new found packages will be downloaded to
                  4. (already_found_meta_data) - (dict) all the found and downloaded packages' metadata - can be copied from the file "already_found_meta_data" located                      in - "Tgz_files/already_found_meta_data.txt"
            
            after the run, the new data collected needs to be added to these files on github:
            1) from the file "malicious_meta_data_table.csv" located in the code's folder to "Npm - MetaData.csv" (location - "Tgz_files/Npm - MetaData.csv")
            2) from the file "all_tgz_malicious_github_advisory.json" located in the code's folder to "already_found_meta_data.txt" 
               (location - "Tgz_files/already_found_meta_data.txt")
            3) from the folder you chose to be the receptor for all new packages - you need to upload the packages to the folder "NPM" 
               (location - "Tgz_files/NPM/")

      2. "explore_evil_packages_files.py" -  This file should be running on Google Colab to explore the Malicious Packages on cloud and not on the privte                                                                computer.
      
