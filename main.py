from hashlib import new
from posixpath import split
import sys


#read all the lines from the file and close it
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

f.close()

#create a new list to store lines that are food items. lines with only number were my own calorie counts
new_list = []


#only append lines that end with a number and have more than one part
for line in data:
    if (len(line.split()) > 1 and any(ch.isdigit() for ch in line.split()[-1])):
        new_list.append(line.replace('\n', ''))

#calculate the total calories for all food items listed
calorie_total = 0
for d in new_list:
    calorie_total += int(d.split()[-1])

#print the each food item as written in the file and the total calories
print('Food items: ')
for item in new_list:
    print(item)

print(f'\nCalorie total: {calorie_total}')