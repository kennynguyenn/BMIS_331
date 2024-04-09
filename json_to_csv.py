import json
import csv
#Change the path below to your results file
with open('/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/results/search.json', 'r') as json_file:
    data_list = json.load(json_file)

fieldnames = set().union(*(d.keys() for d in data_list))

csv_file_path = 'Work_SPK1.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)

print(f'CSV file "{csv_file_path}" created successfully.')
