import csv
from collections import Counter

with open('Height-Weight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

data = Counter(new_data)
mode_data_range = {
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,
    "150-160":0,
    "160-170":0,
}
for weight,occurence in data.items():
    if 100<float(weight)<110:
        mode_data_range["100-110"]+=occurence
    elif 110<float(weight)<120:
        mode_data_range["110-120"]+=occurence
    elif 120<float(weight)<130:
        mode_data_range["120-130"]+=occurence
    elif 130<float(weight)<140:
        mode_data_range["130-140"]+=occurence
    elif 140<float(weight)<150:
        mode_data_range["140-150"]+=occurence
    elif 150<float(weight)<160:
        mode_data_range["150-160"]+=occurence
    elif 160<float(weight)<170:
        mode_data_range["160-170"]+=occurence

mode_range, mode_occurence = 0,0

for range,occurence in mode_data_range.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence = [int(range.split('-')[0]),int(range.split('-')[1])],occurence

mode = float((mode_range[0]+mode_range[1])/2)
print('the mode is:',mode)