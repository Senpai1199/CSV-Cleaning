import csv
import re
output = ['', '', '', '']
	
with open('messy_data.csv', 'r') as csv_file:
	with open('clean_data.csv', 'w', newline='') as csv_write:
		csv_reader = csv.reader(csv_file)
		csv_writer = csv.writer(csv_write)

		for row in csv_reader:
			for column in row:
				p1 = re.match(r'[a-zA-Z]+\s?[a-zA-z]+\s?[a-zA-Z]+', column)
				p2 = re.match(r'[f]?2017(A|B)[0-9]{1}PS[0-9]{4}', column)
				p3 = re.match(r'(M|F)', column) # r'[MF]{1}'
				if(p1):
					output[0] = column
				elif(p2):
					output[1] = column
				elif(p3):
					output[3] = column
				else:
					output[2] = column
			csv_writer.writerow(output)
			output = ['', '', '', '']






				
