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

# Checks for the backup folder, creating one if necessary. The folder can be safely deleted whenever.
def checkForBackupFolder(omission): 
    if not RepoBackupFolder.exists():
        try:
            RepoBackupFolder.mkdir()
            if omission is not True:
                print(f"Repo save backup folder created. Location: {RepoBackupFolder}")
        except Exception as e:
            print(f"Backup folder creation failed, cause: {e}")
    else:
        print(f"Backup folder present, it can be found here at: {RepoBackupFolder}")

def promptBackupUpdate():
    backupUpdateConfirmation = input("Do you want to update your backup? (Y/N) ").strip
    if backupUpdateConfirmation == "Y":
        updateConfirmed = True
    if backupUpdateConfirmation == "N":
        updateConfirmed = False
    else: 
        print("It's a Y or N question dude") # TODO: Figure out why it keeps printing this regardless of input.
        promptBackupUpdate()                 # Will figure out tomorrow, I am tired.
    return updateConfirmed

def awaitBackupUpdate(saveFolder, destination):
    if promptBackupUpdate():
        pass

# To be created and filled out later.
def monitorNewSaves():
    newSaveMonitoring = True
    print("Checking for new saves, please begin playing R.E.P.O!")
    while newSaveMonitoring:
        before = getFolderContents(RepoSaveDirectory)
        time.sleep(10)
        after = getFolderContents(RepoSaveDirectory)
        newFolder = after - before
        if newFolder:
            print("New game detected!")
            newFolder = next(iter(newFolder))
            newSave = RepoSaveDirectory / newFolder
            dest = RepoBackupFolder / newFolder
            if not dest.exists():
                print("Creating backup of new game...")
                shutil.copytree(newSave, dest)
                print(f"Save successfully backed up! It can be found here: {dest}")
            else:
                print(f"Backup already exists at {dest}, skipping copy.")
                continue
        else: 
            print("No new save detected yet, continuing to monitor...")
            continue

def getFolderContents(directory: Path) -> set: # Read specified folder and saves it's contents into a set.
    return {item.name for item in directory.iterdir() if item.is_dir()}

def monitorDefinedSave():
    pass # TODO: Define a save to backup, paste it into backup folder.

def flushSaveBackups():
    flushConfirmation = input("Are you certain you want to flush your backups? (Y/N)\nThis will wipe every backup present in your folder.").strip
    if flushConfirmation == "Y":
        if RepoBackupFolder.exists():
            try: shutil.rmtree(RepoBackupFolder)
            except FileNotFoundError as e: print(e)
            checkForBackupFolder(True)
        else: print("There is no backup folder present.")
    if flushConfirmation == "N":
        print("\nReturning to the start menu...")
        startMenu()

    pass # TODO: Delete the backup folder.

def helpMenu():
    pass # TODO: Write extra information about what each thing does // how to input the right data.

def startMenu(omission): # Display options and allow user selection. 

    # Omission boolean to reduce clutter and ensure the initial message is only printed
    # once instead of any time something other than the numbers 1 through 5 are sent.
    if omission is not True:
        print("Welcome to the R.E.P.O Save Helper, the only tool you'll need to backup your")
        print("saves to prevent accidental OR bullsh*t deaths from ruining your fun!")
        print("\nHere are the things I can do:")
        print("1. Back up a new game. (I check for new file creations and make backups accordingly!)\n2. Back up a specific game. (You provide me with the path to the folder!)")
        print("3. Flush save backups. (I delete all the backups I have created, your real save data won't be touched!)\n4. Help!!! (I can tell you more about each thing.)\n5. Quit it! (Exits the program.)")
        selection = input("Pick a number, any number. (Make sure you pick a number!): ").strip()

    if omission is True:
        print("\nI said pick a number!") # Attitude
        selection = input().strip()

    if selection == "1":
        monitorNewSaves()
    if selection == "2":
        # monitorDefinedSave()
        promptBackupUpdate()
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
        startMenu(True)

checkForBackupFolder(False) # Check for folder on startup, this is the first thing called.

startMenu(False) # Once checked, display start options.