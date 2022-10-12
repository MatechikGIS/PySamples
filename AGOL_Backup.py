#Created by: Chris Matechik
#Created on: October 1, 2020
#

#This script backs up your ArcGIS Online (AGOL) files by first creating copies in your AGOL account, then downloading those copies to a folder of your choice, then deleting the copies.
#Currently, AGOL has no bulk backup function, so this script can save a tremendous amount of time.


#Import the arcgis and datetime packages.
import arcgis
from arcgis.gis import GIS
import datetime as dt
#use a prompt to gather the ArcGIS Online (AGOL) username
username = input("Please enter your AGOL username:")
# I have hardcoded my organizations ArcGIS Online URL. Change this to your organization's URL before running the script. Alternatively, you could insert a prompt here (e.g. Org = input("Enter your organizations URL:")
Org = "https://cosspp.maps.arcgis.com"
#establish connectionn with the AGOL server by creating the gis object with the credentials (username and organization) entered above.
gis = GIS (Org,username)

#Establishes what is getting backed up by querying all of the user's feature services.  I have set the maximum number of files to 99 because ABSI has never ahd over 50 feature services, but you can adjust this number for your needs.
backups = gis.content.search(query="type:Feature Service, owner:{}".format(username), max_items=99, sort_field='modifed', sort_order='desc')
#Prompts user to enter file path in which backup files will be stored.
destination = input("Please enter the filepath. Do Not include quotes around the path. (e.g. K:\RSCH-CML-ABSI\ABSI Tech Files\Data\ArcGIS Online Backups\MonthYY): \n")

#Prints a list of files that will be backed up for the user to see.
print(str(len(backups)) + " Backing up the following items to " + destination +":")
print(*backups, sep = "\n")

#Verify that the user wants to continue based on the list provided above by asking them to type "Y" to continue.
response = input("Do you wish to proceed? Enter Y to continue. Press any other key to quit. \n")

#Start If Else Statement that backs up the files if the user enters "Y" or "y" and terminates if they enter anything else.
if response == "Y" or response == "y":
    #create function to download the backup files
    def download_files(backup_list, backup_location):
        for backup in backup_list:
            try:
                #Excludes views (copies of feature services) from downloading.
                if 'View Service' in backup.typeKeywords:
                    print(backup.title + " is view, not downloading")
                #Downloads all other feature services.
                else:
                    print("Downloading " + backup.title)
                    version = dt.datetime.now().strftime("%d_%b_%Y")
                    result = backup.export(backup.title + "_" + version, "File Geodatabase")
                    result.download(backup_location)
                    result.delete()
                    print("Successfully downloaded " + backup.title)
            #Prints message if there is an error.
            except:
                print("Error while downloading " + backup.title)
        #Tell user that the function is complete and remind them to share this time saving tool with others.
        print("######The function has completed. Please tell your office mates about this script and save them sime time!###########")

    #Call the function created above.
    download_files(backups, destination)

#Quits the program if the user enters anything other than "Y" or "y".
else:
    quit ()
