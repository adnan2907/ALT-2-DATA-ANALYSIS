import csv
import pandas as pd

#startng v1.0
#arl = airport runway lengths
arl = pd.read_csv('Airport Runway lengths 2.0.csv')

pd.set_option('display.max_rows', arl.shape[0]+1)

with open('Airport Runway lengths 2.0.csv','r') as my_data:
    airport_runway_length = csv.reader(my_data)

#removing letter special charater 'Â' in Country list(column)
    special_chars = 'Â'
    for letter in arl['Country']:
        letter = special_chars.replace('Â', '')
        
print(arl['Country'])

#starting v2.0
#finding the length of the longest and shortest runway

with open('Airport Runway lengths 2.0.csv','r') as runway_length:
    print("The longest runway is: ", max(arl['Runway']))
    print("the shortest runway is: ", min(arl['Runway']))

exit()