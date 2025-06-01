import sys
import os
import shutil
import time
from pathlib import Path
from datetime import datetime
# Yummy imports :3

newSaveMonitoring = False # Control variable for new game tracking.

#  Define parent directory then expand from it. 
RepoParentDirectory = Path(os.environ['USERPROFILE']) / "AppData" / "LocalLow" / "semiwork" / "Repo"
RepoSaveDirectory = RepoParentDirectory / "saves"
RepoBackupFolder = RepoParentDirectory / "Repo_Backups"

# To be created and filled out later.
def monitorNewSaves():
    newSaveMonitoring = True
    while newSaveMonitoring:
        before = getFolderContents(RepoSaveDirectory)
        print("Scanning for new games, please begin playing REPO! You won't be able to interact with\nthis program for 60 seconds, but it's doing it's magic.")
        time.sleep(60)
        after = getFolderContents(RepoSaveDirectory)
        newFolder = after - before
        if newFolder:
            pass # TODO: Finish this function that tracks new saves and copy pastes them into the backup folder.
        else: continue

def getFolderContents(directory: Path) -> set: # Read specified folder and saves it's contents into a set.
    return {item.name for item in directory.iterdir() if item.is_dir()}

def monitorDefinedSave():
    pass # TODO: Define a save to backup, paste it into backup folder.

def flushSaveBackups():
    pass # TODO: Delete the backup folder.

def helpMenu():
    pass # TODO: Write extra information about what each thing does // how to input the right data.

# Checks for the backup folder, creating one if necessary. The folder can be safely deleted whenever.
def checkForBackupFolder(): 
    if not RepoBackupFolder.exists():
        try:
            RepoBackupFolder.mkdir()
            print(f"Repo save backup folder created. Location: {RepoBackupFolder}")
        except Exception as e:
            print(f"Backup folder creation failed, cause: {e}")
    else:
        print(f"Backup folder present, it can be found here at: {RepoBackupFolder}")

def startMenu(): # Display options and allow user selection. 

    print("Welcome to the R.E.P.O Save Helper, the only tool you'll need to backup your")
    print("saves to prevent accidental OR bullsh*t deaths from ruining your fun!")
    print("\nHere are the things I can do:")
    print("1. Back up a new game. (I check for new file creations and make backups accordingly!)\n2. Back up a specific game. (You provide me with the path to the folder!)")
    print("3. Flush save backups. (I delete all the backups I have created, your real save data won't be touched!)\n4. Help!!! (I can tell you more about each thing.)\n5. Quit it! (Exits the program.)")
    
    selection = input("Pick a number, any number. (Make sure you pick a number!): ").strip()

    if selection == "1":
        monitorNewSaves()
    if selection == "2":
        monitorDefinedSave()
    if selection == "3":
        flushSaveBackups()
    if selection == "4":
        helpMenu()
    if selection == "5":
        try: 
            sys.exit(0)
        except BaseException:
            os._exit(0)
    else:
        print("I said pick a number!") # Attitude

checkForBackupFolder() # Check for folder on startup, this is the first thing called.

startMenu() # Once checked, display start options.