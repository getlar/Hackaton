import pandas as pd
from collections import Counter

excel_file_path = 'questionnaire.xlsx'


df = pd.read_excel(excel_file_path, sheet_name='QUESTIONNAIRE', header=None)

# load it into a string and split it by the comma

listofbeers = list(df.iloc[0, 0].split(','))

# lowercase all the beers

listofbeers = [beer.lower() for beer in listofbeers]

# remove whitespaces from the beginning and end of the beers

listofbeers = [beer.strip() for beer in listofbeers]

#print(listofbeers)

# count number of mentions of each beer and print it
# if it is already mentioned, don't print it again

beer_name_counts = Counter(listofbeers)

# Print out beer names and their counts
for beer_name, count in beer_name_counts.items():
    print(f"{beer_name}: {count} times")

# print how many beer names are there in the counter

print(len(beer_name_counts))

# print the most mentioned beer

print(beer_name_counts.most_common(1))

listofsmth = list(df.iloc[1, 0].split(','))

# lowercase all the strings

listofsmth = [smth.lower() for smth in listofsmth]

# remove whitespaces from the beginning and end of the strings

listofsmth = [smth.strip() for smth in listofsmth]

#print(listofsmth)

# further split strings in the list by ";"

new_list = []

for item in listofsmth:
    splitted = item.split(';')
    for i,splits in enumerate(splitted):
        new_list.append(splitted[i])

cum = []

for new_item in new_list:
    new_item = new_item.strip()
    splitted = new_item.split(' ')
    #print(splitted)
    try:
        num = int(splitted[0])
        cum.append(num)
    except ValueError:
        pass

#print(sum(cum))

beer_map = {}

for beer_name, count in beer_name_counts.items():
    for smth in listofsmth:
        if beer_name in smth:
            if beer_name in beer_map:
                beer_map[beer_name].append(smth)
            else:
                beer_map[beer_name] = [smth]

#print(beer_map["soproni"])

# seperate the strings in beer_map["soproni"] by the ";" 

new_list = []

for item in beer_map["arany ászok"]:
    splitted = item.split(';')
    for i,splits in enumerate(splitted):
        if "arany ászok" in splits:
            new_list.append(splitted[i])

#print(new_list)

cum = []

for item in new_list:
    item = item.strip()
    splitted = item.split(' ')
    num = int(splitted[0])
    cum.append(num)

print(sum(cum))


        