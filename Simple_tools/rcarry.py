import random
import time

hero_names = [
    'alch',
    'am',
    'arc',
    'blood',
    'bounty?',
    'bristle',
    'brood?',
    'ck',
    'clinkz?',
    'dk?',
    'doom',
    'drow',
    'druid',
    'ember',
    'gyro',
    'jug',
    'legion',
    'life',
    'luna',
    'lycan',
    'medusa',
    'meppo?',
    'mirana',
    'mk',
    'morph',
    'naga',
    'np',
    'pa',
    'pl',
    'razor?',
    'riki',
    'sf?',
    'shaker?',
    'silencer?',
    'slark',
    'sniper',
    'spectre',
    'squirel?',
    'sven',
    'ta?',
    'terror',
    'trol',
    'ursa',
    'veng',
    'void',
    'weaver',
    'wk']



a = ""
while a != "n":
    x = random.randrange(0, len(hero_names))
    print(hero_names[x])
    time.sleep(1)
    #a = input("")
    #print(sorted(hero_names))
