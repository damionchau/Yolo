Before running the following game, you will need to import and initiate the following:

import math
import pgzrun
import pygame
import pgzero
import sys
import random
from pgzero.builtins import Actor
from random import randint

Game Description
Dragon Egg Hunt is a 2-player game where the players are heroes tasked with collecting dragon eggs from three different dragon lairs of varying difficulties. The players move around the game world with the arrow keys and WASD keys on their respective keyboards. The dragon in each lair will be sleeping, and players must avoid waking them up. The players must collect all the eggs in each lair to complete the game. The game ends if a player wakes up a dragon or loses all their lives.

Installation
Clone the repository: git clone https://github.com/yourusername/dragon-egg-hunt.git
Install the required dependencies: pip install -r requirements.txt
Usage
Navigate to the project directory: cd dragon-egg-hunt
Run the game: python main.py
Use the arrow keys to move the first player and the WASD keys to move the second player.

The randomness of the dragons sleep schedule will increase as you collect more eggs.

README File for COCO Image Dataset Splitting Script
This is a Python script that splits the Microsoft Common Objects in Context (COCO) dataset into training and validation subsets for use with the YOLOv5 object detection algorithm.

Prerequisites
COCO dataset downloaded and extracted to local machine
Python 3.x installed
YOLOv5 installed
Existing directories for storing training and validation subsets
Usage
Open the script file in a text editor and edit the following paths to match your local file system:
coco_images : directory where downloaded images are stored
coco_labels : directory where corresponding annotation files are stored
ee104TrainImagePath : directory where the training images subset will be stored
ee104TrainLabelPath : directory where the training annotation files subset will be stored
ee104ValImagePath : directory where the validation images subset will be stored
ee104ValLabelPath : directory where the validation annotation files subset will be stored
Set the train_ratio and val_ratio variables to your desired proportions for splitting the dataset into training and validation subsets.

Save the changes to the script file.

Run the script in a Python environment to generate the training and validation subsets.

