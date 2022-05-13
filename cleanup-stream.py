##############################
##   Stream cleanup Script  ##
###################################################################
## Python Script developed by SimmyDizzle (LiveSimmy)            ##
## I use this script in conjunction with my streamdeck and a     ##
## series of other tools, however this will work for everyone    ##
## with minor changes to the file paths. This just cleans up     ##
## and moves remaining files around to the appropriate directorys##
###################################################################
## Socials:                                                      ##
## https://facebook.com/livesimmy                                ##
## https://twitter.com/livesimmy                                 ##
## https://tiktok.com/@livesimmy                                 ##
###################################################################
import shutil, os, time, os.path
from datetime import datetime

dt = datetime.now()

HomePath = 'C:/Videos'

# Check if path exists
if os.path.exists(HomePath):
	# Our buffer was saved but was not used?
	file_path = HomePath +'/Buffer Replay .mp4'

	# If our Replay Buffer still exists, move it to the saved buffers.
	if os.path.exists(file_path):
		new_name = HomePath + '/Saved Buffers/Buffer Replay - ' + dt.strftime('%A %d-%m-%Y, %H.%M.%S') + '.mp4'
		shutil.copy( HomePath + '/Buffer Replay .mp4', new_name)
		time.sleep(2)
		os.remove( HomePath + '/Buffer Replay .mp4')

	# Move the current videos to the next path
	videos = [f for f in os.listdir(HomePath) if '.mp4' in f.lower()]
	for video in videos:
		new_path = HomePath + '/Past Streams/' + video
		current_path = HomePath + '/' + video
		shutil.move(current_path, new_path)

# Path didn't exist, we exit the script.
else:
	exit

# EOF
