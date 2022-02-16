from hashlib import new
from posixpath import split
import sys

def main():
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


    #calculate the amount of protein
    protein = 0
    for line in new_list:
        for word in line.replace('\n', '').split():
            if word[-1].isalpha() and word[-1] == 'p' and word[-2].isdigit():
                protein+= int(word[:-1])

    #calculate the total calories for all food items listed
    calorie_total = 0
    for d in new_list:
        calorie_total += int(d.split()[-1])

    #print the each food item as written in the file and the total protein and calories
    print('Food items: ')
    for item in new_list:
        print(item)

    print(f'\nTotal protein: {protein}g')
    print(f'Calorie total: {calorie_total}')

    #check if the calorie total is written to the file and if not, write it
    calories_present = False
    try:
        calories_present = (calorie_total is not int(data[-1]))
    except:
        pass

    if (not calories_present):
        print('writing calories')
        with open (sys.argv[1], 'a') as f:
            f.write(f'\n{calorie_total}')
            f.close()

if __name__ == '__main__':
    main()