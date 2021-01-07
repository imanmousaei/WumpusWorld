"""
.: empty node
P: pit -> death
W: wumpus -> death
G: gold
"""

table = [
    ['.', '.', 'P', '.'],
    ['.', '.', '.', 'P'],
    ['P', 'W', '.', '.'],
    ['.', '.', 'P', 'G']
]

n = len(table)


ACTION_COUNT = 4  # R U L D

# scores:
WIN_REWARD = +1000
DIE_REWARD = -1000
SHOT_REWARD = -10
ELSE_REWARD = -1


NUM_BATCHES = 10000
MAX_STEPS_PER_BATCH = 100

# for seeing how good we are:
EACH_PART_SIZE = 100
PART_NUM = int(NUM_BATCHES/EACH_PART_SIZE)

# Q-Learning constants :

LEARNING_RATE = 0.8
DISCOUNT_RATE = 0.9

EXPLORATION_RATE = 1.0
MAX_EXPLORATION_RATE = 1.0
MIN_EXPLORATION_RATE = 0.1
EXPLORATION_DECAY_RATE = 0.001

