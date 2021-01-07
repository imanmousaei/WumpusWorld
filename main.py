import numpy as np

from Agent import Agent
from Node import Node, nodes, n, config_nodes
from consts import *

q_table = np.zeros((n*n, ACTION_COUNT))

config_nodes()

all_batches_scores = []

agent = Agent()

exploration_rate = EXPLORATION_RATE
for batch in range(NUM_BATCHES):
    current_batch_score = 0
    for step in range(MAX_STEPS_PER_BATCH):
        agent_current_state = agent.state()

        exploration_rate_threshold = np.random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[agent_current_state][:])
        else:
            action = np.random.randint(ACTION_COUNT)

        reward, ended = agent.move(action)
        agent_new_state = agent.state()

        current_batch_score += reward

        q_table[agent_current_state, action] = q_table[agent_current_state, action] * (
                    1 - LEARNING_RATE) + LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(q_table[agent_new_state][:]))

        if ended:
            break

    exploration_rate = MIN_EXPLORATION_RATE + (MAX_EXPLORATION_RATE - MIN_EXPLORATION_RATE) * np.exp(
        -EXPLORATION_DECAY_RATE * batch)

    all_batches_scores.append(current_batch_score)

print(all_batches_scores)
