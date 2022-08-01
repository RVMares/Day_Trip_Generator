destinations = ['Manitou Springs', 'Breckenridge', 'Denver']
restaurants_Manitou_Springs = ['Iron Chateau', 'Border Burger Bar', 'Manitou Brewing Company', 'Mo\'s Diner & Lounge', 'The Mason Jar', 'Pizzeria Rustica']
entertainment_Manitou_Springs = ['Santa\'s Workshop', 'River Running', 'Colorado Wolf and Wildlife Center', 'Garden of the Gods', 'The Incline', 'Western Museum of Mining and Industry', 'Miramont Castle']
restaurants_Breckenridge = ['Hearthstone', 'Piante Pizzeria', 'Twist', 'Relish', 'Aurum Food and Wine', 'Mountain Flying Fish']
entertainment_Breckenridge = ['Breckenridge Ski Resort', 'Rafting', 'Shopping on Main Street', 'Country Boy Mine', 'Visit Isak the Breckenridge Troll', 'Edwin Carter Museum and Park', 'Breckenridge Theater presenting "\The Play That Goes Wrong\"']
restaurants_Denver = ['The Poke House', 'Apple Blossom', 'Chez Maggy', 'A5 Steakhouse', 'Toro Latin Kitchen', 'Cantina Loca', 'Glo Noodle House', 'Jax Fish House']
entertainment_Denver = ['16th Street Mall', 'Larimer Square', 'Meow Wolf Denver', 'Colorado Railroad Museum', 'Elitch Gardens Theme and Water Park', 'Denver Zoo', 'Denver Museum of Nature and Science', 'Jurassic World: The Exhibition']
transportation = ['Train', 'Rental Car', 'Bicycle', 'RTD Rail', 'Uber', 'Taxi', 'Rental Scooter']

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
