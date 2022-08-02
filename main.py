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
    global destination
    destination = (random.choice(destinations))
    print ('Your destination is generating...')
    final_destination = input('I have selected ' + destination + ' as your destination. Does this sound good? Enter y/n: ')
    if final_destination == 'y':
        print ('Great! Let\'s continue!')
    else:
        print ('That is okay. Let\'s try something else.')
        random_destination()

def random_restaurant():
    global restaurant
    if (destination == 'Manitou Springs'):
        restaurant = (random.choice(restaurants_Manitou_Springs))
        return restaurant
    elif (destination == 'Breckenridge'):
        restaurant = (random.choice(restaurants_Breckenridge))
        return restaurant
    else:
        restaurant = (random.choice(restaurants_Denver))
        return restaurant

def final_restaurant():
    print ('Get ready for some good food!')
    chosen_restaurant = input('I have selected ' + (restaurant) + ' as your restaurant. Does this sound good? Enter y/n: ')
    if chosen_restaurant == 'y':
        print ('Great! Let\'s continue!')
    else:
        print ('That is okay. Let\'s try something else.')
        random_restaurant()
        final_restaurant()


def random_transportation():
    print ('Generating Mode of Transportation...')
    final_transportation = input('I have selected ' + (random.choice(transportation)) + ' as your mode of transportation. Does this sound good? Enter y/n: ')
    if final_transportation == 'y':
        print ('Great! Let\'s continue!')
    else:
        print ('That is okay. Let\'s try something else.')
        random_transportation()

def random_entertainment():
    global entertainment
    if destination == 'Manitou Springs':
        entertainment = (random.choice(entertainment_Manitou_Springs))
        return entertainment
    elif destination == 'Breckenridge':
        entertainment = (random.choice(entertainment_Breckenridge))
        return entertainment
    else:
        entertainment = (random.choice(entertainment_Denver))
        return entertainment

def final_entertainment():
    print('Generating your entertainment for today...')
    chosen_entertainment = input ('I have selected ' + entertainment + ' as your activity for today. Does this sound fun? Enter y/n: ')
    if chosen_entertainment == 'y':
        print ('Great! Let\'s continue!')
    else:
        print ('That is okay. Let\'s try something else.')
        random_entertainment()
        final_entertainment()


def day_trip_generator():
    random_destination()
    random_restaurant()
    final_restaurant()
    random_transportation()
    random_entertainment()
    final_entertainment()
day_trip_generator()

