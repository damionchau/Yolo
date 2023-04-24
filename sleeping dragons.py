import math
import pgzrun
import pygame
import pgzero
import sys
import random
from pgzero.builtins import Actor
from random import randint


WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (200, 300)
ATTACK_DISTANCE = 200
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 9                                               #Set lives for both players
eggs_collected = 0                                      #initial amount of eggs in posession
game_over = False
game_complete = False
reset_required = False

x = random.randint(1, 7)       #sent random variables to increase randomness and make it unpredictable 
y = random.randint(1, 5)
z = random.randint(1, 3)
easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 100)),   #image actore for sleeping dragon
    "eggs": Actor("one-egg", pos=(480, 100)),           #one egg 
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": x,                                      #set to x, a random number from 1-7
    "sleep_counter": 0,
    "wake_counter": 0
 }
medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 300)),
    "eggs": Actor("two-eggs", pos=(480, 300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": y,                                      #set to y, a random number from 1-5
    "sleep_counter": 0,
    "wake_counter": 0
 }
hard_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 500)),
    "eggs": Actor("three-eggs", pos=(480, 500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 4,
    "sleep_counter": z,                                      #set to z, a random number from 1-3
    "wake_counter": 0
 }
lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor("hero", pos=HERO_START)
hero2 = Actor("hero2", pos=HERO_START)
def draw():
    global lairs, eggs_collected, lives, game_complete
    screen.clear()
    screen.blit("dungeon", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER!", fontsize=60, center=CENTER, color=FONT_COLOR)        #losing screen
    elif game_complete:
        screen.draw.text("YOU WON!", fontsize=60, center=CENTER, color=FONT_COLOR)          #game completion win screen
    else:
        hero.draw()
        hero2.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)
def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"] is False:
            lair["eggs"].draw()
def draw_counters(eggs_collected, lives):
    screen.blit("egg-count", (0, HEIGHT - 30))                  #setting font size colors positions
    screen.draw.text(str(eggs_collected),                       #egg collected number
                     fontsize=40,
                     pos=(30, HEIGHT - 30),
                     color=FONT_COLOR)
    screen.blit("life-count", (60, HEIGHT - 30))
    screen.draw.text(str(lives),
                     fontsize=40,
                     pos=(90, HEIGHT - 30),
                     color=FONT_COLOR)
    screen.draw.text(str(lives),
                     fontsize=40,
                     pos=(90, HEIGHT - 30),
                     color=FONT_COLOR)
 
def update():
    if keyboard.right:                              #set movement keys for player 1
        hero.x += MOVE_DISTANCE
        if hero.x > WIDTH:
            hero.x = WIDTH
    elif keyboard.left:
        hero.x -= MOVE_DISTANCE
        if hero.x < 0:
            hero.x = 0
    elif keyboard.down:
            hero.y += MOVE_DISTANCE
            if hero.y > HEIGHT:
                hero.y = HEIGHT
    elif keyboard.up:
        hero.y -= MOVE_DISTANCE
        if hero.y < 0:
            hero.y = 0

    check_for_collisions()

    if keyboard.d:                              #set movement keys for player 2
        hero2.x += MOVE_DISTANCE
        if hero.x > WIDTH:
            hero.x = WIDTH
    elif keyboard.a:
        hero2.x -= MOVE_DISTANCE
        if hero2.x < 0:
            hero.x = 0
    elif keyboard.s:
            hero2.y += MOVE_DISTANCE
            if hero.y > HEIGHT:
                hero2.y = HEIGHT
    elif keyboard.w:
        hero2.y -= MOVE_DISTANCE
        if hero2.y < 0:
            hero2.y = 0

           
    check_for_collisions()
    
def update_lairs():                                             #definition for global lairs and variables 
    global lairs, hero, hero2, lives
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)
clock.schedule_interval(update_lairs, 1)

def update_sleeping_dragon(lair):                                      #define sleeping dragon counter
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"].image = "dragon-awake"
        lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1
def update_waking_dragon(lair):
    if lair["wake_counter"] >= DRAGON_WAKE_TIME:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1
def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0    
        else:
            lair["egg_hide_counter"] += 1
            # This function updates the state of an egg in a lair. If the egg is hidden, it checks
# whether it has been hidden for enough time (as defined by the EGG_HIDE_TIME constant).
# If the egg has been hidden for long enough, the egg is unhidden and the egg_hide_counter
# is reset to 0. If the egg has not been hidden for long enough, the egg_hide_counter is
# incremented by 1.
                
def check_for_collisions():
    global lairs, eggs_collected, lives, reset_required, game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collision(lair)
            
def check_for_dragon_collision(lair):
    x_distance = hero.x - lair["dragon"].x
    y_distance = hero.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()
        
        # This function checks for collisions between the heroes and dragons and eggs.
    # It updates the global variables eggs_collected, lives, reset_required, and game_complete.
    
    x_distance = hero2.x - lair["dragon"].x
    y_distance = hero2.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()
        # If the dragon in the lair is awake and a reset is not already required,
       # check for a collision between the hero and the dragon.
def handle_dragon_collision():
    global reset_required
    reset_required = True
    animate(hero, pos=HERO_START, on_finished=subtract_life)
    animate(hero2, pos=HERO_START, on_finished=subtract_life)
def check_for_egg_collision(lair):
    global eggs_collected, game_complete
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        
        # This function checks for a collision between a hero and a dragon in a given lair.
# If the distance between the hero and the dragon is less than ATTACK_DISTANCE, it
# calls the handle_dragon_collision function.
    if hero2.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True
            
            # This function checks for a collision between a hero and an egg in a given lair.
# If a collision is detected, the egg is hidden and the egg count is added to the
# eggs_collected global variable. If the eggs_collected reaches the EGG_TARGET, the
# game_complete global variable is set to True.

def subtract_life():
    global lives, reset_required, game_over
    lives -= 1
    if lives == 0:
        game_over = True
    reset_required = False   

pgzrun.go()