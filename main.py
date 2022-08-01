destinations = ['Denver', 'Aspen', 'Boulder', 'Breckenridge', 'Vail', 'Canon City']
restaurants = ['Buckhorn Exchange', 'Bingo Burger', 'Illegal Petes', 'Casa Bonita', 'Beau Jos', 'Biker Jims', 'Iron Chateau']
transportation = ['Train', 'Car', 'Bicycle', 'RTD Rail', 'Uber']
entertainment = ['History Colorado Center', 'Ute Indian Museum', 'Sunrise Ballon Ride', 'Cheyenne Mountain Zoo', 'Red Rock Canyon Concert', '3-Hour Brewery Tour']

import random

def random_destination():
    print ('Your destination is generating...')
    print(random.choice(destinations))

def random_restaurant():
    print ('Get ready for some good food!')
    print (random.choice(restaurants))

def random_transportation():
    print ('Generating Mode of Transportation...')
    print (random.choice(transportation))

def random_entertainment():
    print('Generating your entertainment for today...')
    print (random.choice(entertainment))

def day_trip_generator():
    random_destination()
    random_restaurant()
    random_transportation()
    random_entertainment()
day_trip_generator()
