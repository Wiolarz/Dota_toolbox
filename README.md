# dota
 a list of short programs that could be useful for a dota 2 player


Project is split into folders with each focused on separate task.
# Folders:

## tournament
Latest project centered around providing a data regarding possibility of e-sports team attending "The International"
directly via DPC points system.

dota_major - once provided with DPC standings and attendance of the last major in a season 
can generate every possible scenario and then display in how many scenarios each team got a direct invite

playoffs - works in similar way to the dota_major, but it operates on the bracket system.
It requires at least group stage to be over, so that a user can enter team placements in each group.
Program also allows for the user to enter scores of the already concluded matches in the bracket
to pinpoint predictions based on the latest results.


## old_calculator
one of my first attempts to create a useful program.

It's aim was to find the most efficient item build for a hero.

Finally I only managed to account for the most basic dota attributes.

Dota 2 item database is really old, if were to return to this code everything would have to be scrapped,

I'm keeping it only for a reference how I wrote code many years ago.

Update folder was an attempt to write that code again some time later, but it isn't worth it to use it anymore.
Basically updates occur too often to rely on manual changes each time.
Proper calculator will require scraping data tools.


## Simple_tools
very old and random code:

dotaplus - simple equation to count conversion of dota plus shard to number of ban slots

guid - a stub centered around providing in game notifications for different time related mechanics

hero_picker - stub centered around providing help with hero recommendations during draft phase

rhero - basic code that displays every two seconds a name of a randomly selected  a nem of dota 2 hero, 
it could be used instead of the in game tool, in order to avoid picking a hero in the first phase


rcarry - rhero.py copy with a smaller range of characters including only "carry" heroes


