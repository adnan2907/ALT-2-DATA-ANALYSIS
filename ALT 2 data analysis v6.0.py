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
    print("The longest runway is: ", max(arl['Runway']), "ft")
    print("the shortest runway is: ", min(arl['Runway']), "ft")


#starting v3.0
#finding most common runway length and number of times repeating
#all lengths of runway is measured in ft (feet)
    
runway_length = pd.read_csv('Airport Runway lengths 2.0.csv')

#runway in a list:
runway_list = runway_length['Runway'].tolist()
print(runway_list)

common_runway_length = arl['Runway'].value_counts().idxmax()
print("The most common runway length is: ", common_runway_length, "ft")

runway_repeating = arl['Runway'].value_counts().max()
print("This runway repeats: ", runway_repeating, "times")

#starting v4.0
#finding the most common countries and number of times repeating
list_of_airports = pd.read_csv('Airport Runway lengths 2.0.csv')

airport_list = list_of_airports['Airport'].tolist()

most_common_airport = arl['Airport'].value_counts().idxmax()
print("The most common airport is: ", most_common_airport)

airport_repeating = arl['Airport'].value_counts().max()
print("This airport repeats: ", airport_repeating, "times")

#starting v5.0
#find how much times each runway in repeating
#getting different ranges

arl = pd.read_csv('Airport Runway lengths 2.0.csv')

runway_length_list = arl['Runway'].tolist()

#putting the ranges = to 0 
runway_0_to_3000 = 0
runway_3000_to_6000 = 0
runway_6000_to_9000 = 0
runway_9000_to_12000 = 0
runway_12000_to_15000 = 0
runway_15000_to_18000 = 0

#counting the runway lengths occurances 
for item in runway_length_list:
    if item < 3000:
        runway_0_to_3000 +=1
        
    elif item > 3000 and item < 6000:
        runway_3000_to_6000 +=1
        
    elif item > 6000 and item < 9000:
        runway_6000_to_9000 +=1
        
    elif item > 9000 and item < 12000:
        runway_9000_to_12000 +=1
        
    elif item > 12000 and item < 15000:
        runway_12000_to_15000 +=1
        
    elif item > 15000 and item < 18000:
        runway_15000_to_18000 +=1
        
print("There are",  runway_0_to_3000, "repeating between 0-3000")
print("There are", runway_3000_to_6000, "runways between 3000-6000")
print("There are", runway_6000_to_9000, "runways between 6000-9000")
print("There are", runway_9000_to_12000, "runways between 9000-12000")
print("There are", runway_12000_to_15000, "runways between 12000-15000")
print("There are", runway_15000_to_18000, "runways between 15000-18000")

#starting v6.0
#graph for lengths against times repeating 

import pygal

#List of runways from above
runway_0_to_3000 = 20
runway_3000_to_6000 = 120
runway_6000_to_9000 = 358
runway_9000_to_12000 = 435
runway_12000_to_15000 = 124
runway_15000_to_18000 = 4

#adding to graph
runway_chart = pygal.Bar()
runway_chart.x_title = "Repeating Runway lengths"
runway_chart.y_title = "Runway Lengths in ft "
runway_chart.add('0-3000', runway_0_to_3000)
runway_chart.add('3000-6000', runway_3000_to_6000)
runway_chart.add('6000-9000', runway_6000_to_9000)
runway_chart.add('9000-12000', runway_9000_to_12000)
runway_chart.add('12000-15000', runway_12000_to_15000)
runway_chart.add('15000-18000', runway_15000_to_18000)

#updating to graph
runway_chart.render_to_file('Repeating lengths.svg')

exit()