Read Me
Backing up ArcGIS Online Files
Chris Matechi
Created 11/19/21
Updated (to clarify points for interview) on 6/7/22

##########################
Description
##########################
The biggest drawback to ArcGIS Online (AGOL) is that there is no bulk backup feature. Users are expected to convert each feature service into a shapefile and then download it,then go back and delete the shapefile from the ArcGIS Online Account.
This is time consuming and error prone. Manually deleting the file copies is especially risky.

An easier way is to use a Python Script to Automate this process.

##########################
Requirements
##########################
Before using this script, YOU MUST INSTALL the arcgis and datetime packages in your Python directory. You can install the packages with Anaconda or a similar service but if you are already running ArcMap or ArcGIS Pro it is ieasier to use
the IDE that installs with them.

If youn are a non Florida State University (FSU) user, you will need to open the file and replace your AGOL organizational URL on line 8 OR THE SCRIPT WILL NOT WORK.
(e.g. switch Org = "https://cosspp.maps.arcgis.com" to Org = "https://YOUR_ORGS_NAME.maps.arcgis.com"

The URL is the same URL you use when loggng into AGOL.

If you want to backup more than 99 itmes, you will need to update the maximum number of items backed up on (max_items) on line 13.

##########################
Credentials
##########################
The script will prompt you to enter your ArcGIS Online username and Password.

I did not hardcode these parametes in becasue (1) I wanted this script to be used by others, (2) credentials may change overtime and then somebody who knows how to code would have to update them, and (3) storing passwords in code is not secure at all.

##########################
Instructions 
##########################

1. Open the file called Backup_ArcGIS_Online.ipynb. The easiest way to open it is to right click on the file and then select
"Open with IDLE (ArcGIS Pro)".

2. Run the script by clicking "Run" and then "Run Module". It may take a minute for the script to conenct to the ArcGIS server.
Be patient. It may not look like it's doing anything. Eventually it will prompt you to 
enter your username. On the slow internet at the FSUCML this can take up to a minute. 

[Those who are more familiar with Python and modules can run this script in their prefferred environment and pickup at step 3.]

3. Enter your ArcGIS Username when prompted. Press ENTER.

4. Enter your ArcGIS Password when prompted. Press ENTER

5. Enter the filepath when prompted. Optional - create a new folder to hold the backup files
and use this as your filepath. It is easier to keep them organized if each backup session
is stored in it's own folder.

A typical path will look like:
 K:\RSCH-CML-ABSI\ABSI Tech Files\Data\ArcGIS Online Backups\MonthYY
Do not enter quotes or a slash at the end. 

7. The program will print a list of items that will be backed up. Review the list.

8. If the list looks correct, type "Y" when prompted to continue the program. Otherwise, press any other key to quit.

9. Be patient. This will still take way less time than a manual backup.

10. You should see outputs indicating when a feature service is being downloaded and when
it is complete.

11. Views will not download because the data are stored in the parent layer so downloading views would be redundant.

12. Layers that ABSI does not own (e.g. fdacs layers) cannot be backed up so you will see 
an error. Ignore these.

13. Investigate any errors for ABSI owned layers.

14. Close the program.

ABSI staff should back up AGOL files at least once per month.

