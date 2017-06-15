import glob 
import csv 
import re

def normalizing_time_stamp(original_file):
	print original_file
	file_open = open(original_file,'r')
	file_read = csv.reader(file_open)
	output_file_open = open('/home/vamsi/Documents/Flutura_hackathon/Test/Gearbox/Gearbox_Modified/'+re.sub('.csv','',original_file.split('/')[-1])+'_normalized.csv','w')
	file_writer = csv.writer(output_file_open)
	for each_row in file_read:
		try:
			file_writer.writerow([each_row[1].split(' ')[0].split('-')[-1],':'.join(each_row[1].split(' ')[1].split(':')[:-1]),each_row[2]])
		except:
			file_writer.writerow(['day']+['time']+[each_row[2]])

if __name__ == '__main__':
	path = '/home/vamsi/Documents/Flutura_hackathon/Test/Gearbox/*'
	files = glob.glob(path)
	for file in files:
		normalizing_time_stamp(file)
	


