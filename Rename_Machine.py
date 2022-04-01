import os
import shutil
import zipfile

def rename_Machine():

	videoPath = input('Drop the Video Directory: ')
	if(videoPath[0] == videoPath[-1] == "\""):
		videoPath = videoPath[1:-1]

	# videoPath = "manual_path"

	fname = {}
	i = 0
	for file in os.listdir(videoPath):
		fname[i], fext = os.path.splitext(file)
		if (fext == '.mkv' or fext == '.mp4' or fext == '.MP4'):
			i+=1

	#Getting Script's Current Directory
	current = os.getcwd()
	subPath = input('Drop the Subtitle Zip File: ')
	if(subPath[0] == subPath[-1] == "\""):
		subPath = subPath[1:-1]
	print(current)

	# Creating a Folder Named "Files" in the Script's Current Directory.
	if (os.path.exists(current+'\\Files') == False):
		os.makedirs(current+'\\Files')
	
	with zipfile.ZipFile(subPath, 'r') as LocalObj:
		# Extract all the contents of zip file in different directory
		shutil.rmtree('Files', ignore_errors=True)
		LocalObj.extractall('Files')
		LocalObj.close()
	i = 0
	for file in os.listdir('Files'):
		nFile = fname[i]+'.srt'
		os.rename(os.path.join('Files', file), os.path.join('Files', nFile))
		shutil.move('Files/'+nFile, videoPath+'/'+nFile)
		i+=1

	# After All rename and moving Deleting the Folder Named "Files" from the Script's Current Directory.
	if os.path.exists(current+'\\Files'):
		shutil.rmtree(current+'\\Files', ignore_errors=True)
		
	again = ' '
	while (again == ' '):
		again = input("\n\nRename Again (Y/N): ")
		if((again == 'y') or (again == 'Y')):
			print("\n-------------------------------------------\n\n")
			rename_Machine()
		elif((again == 'n') or (again == 'N')):
			print("\nThanks for using!\n\n")
		else:
			print("Invalid Command! Please type either Y or N")
			again = ' '

if __name__ == '__main__':
	rename_Machine()