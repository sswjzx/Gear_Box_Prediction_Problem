import csv 
import glob 
import re
import pandas as pd
from datetime import datetime


def normalizing_time_stamp(original_file,index):
	print original_file
	file_open = open(original_file,'r')
	file_read = csv.reader(file_open)
	output_file_open = open('/home/vamsi/Documents/Flutura_hackathon/Test/Gearbox/Gearbox_Normalized/'+re.sub('.csv','',original_file.split('/')[-1])+'_final.csv','w')
	file_writer = csv.writer(output_file_open)
	time_hash = {}
	for each_row in file_read:
		try:
			if time_hash.get(each_row[0]+' '+each_row[1]):
				time_hash[each_row[0]+' '+each_row[1]] += [each_row[2]]
			else:
				time_hash[each_row[0]+' '+each_row[1]] = [each_row[2]]
			# file_writer.writerow([each_row[1].split(' ')[0].split('-')[-1],':'.join(each_row[1].split(' ')[1].split(':')[:-1]),each_row[2]])
		except:
			print each_row
	value_column_name  = '_'.join(original_file.split('/')[-1].split('_')[1:-1])
	file_writer.writerow(['day_time']+['value_'+value_column_name])
	for each_key in time_hash:
		try:
			list_type = map(float,time_hash[each_key]) 
			file_writer.writerow([each_key,sum(list_type)/len(list_type)])
		except:
			print time_hash[each_key]
	left_out_indexes = set(index) - set(time_hash.keys())
	for each_index in left_out_indexes:
		file_writer.writerow([each_index,float('Nan')])

if __name__ == '__main__':
	index = []
	s = pd.date_range("00:00", "23:59", freq="1min").time
	l = s.tolist()
	l = [i.strftime('%H:%M') for i in l]
	for i in range(1,32):
		if i <= 9:
			l_n = ['0'+str(i)+' '+j for j in l]
			index.extend(l_n)
		else:
			l_n = [str(i)+' '+j for j in l]
			index.extend(l_n)

	path = '/home/vamsi/Documents/Flutura_hackathon/Test/Gearbox/Gearbox_Modified/*'
	files = glob.glob(path)
	for file in files:
		normalizing_time_stamp(file,index)
