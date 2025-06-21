'''
The shutil module in is used for file and directory operations — especially copying, moving, deleting, and archiving.
'''
import shutil

# Copy a file
shutil.copy("example.txt", "backup.txt")

# Move a file
shutil.move("backup.txt", "folder/backup.txt")

# Delete a folder
shutil.rmtree("folder")

# Get disk usage
usage = shutil.disk_usage("/")
print(f"Free: {usage.free // (1024**3)} GB")
