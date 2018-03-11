import os
import re
import shutil

search_dir = 'D:\Downloads\TV\GOT\GOT.s07'
dest_dir = 'D:\Downloads\TV\GOT\GOT.s07'
show = ''
ext = ['mkv','mp4']
DEBUG = False

if os.path.isdir(dest_dir) and search_dir is not dest_dir:
#	shutil.rmtree(dest_dir)
	os.mkdir(dest_dir)

required_dirs = [direc for direc in os.listdir(search_dir) if re.match(show, direc, flags=re.IGNORECASE)]
files_to_move = [
	[search_dir + '\\' + direc + '\\', d] 
		for direc in required_dirs 
			for d in os.listdir(search_dir + '\\' + direc) 
				if os.path.splitext(d)[1][1:] in ext]

counter = 0
print len(files_to_move)
for d, fname in files_to_move:
	if not DEBUG:
		shutil.move(d + fname, dest_dir)
		shutil.rmtree(d)
	else:
		print d+fname, dest_dir
	counter += 1
	finished = counter * 100 / len(files_to_move)
	print '#' * finished, '_' * (100-finished), '{0}% finished'.format(finished)




