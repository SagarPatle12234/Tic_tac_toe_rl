# Q-Learning Tic-Tac-Toe 🎮🤖

An exploration into the fundamentals of Reinforcement Learning. This repository contains a Tic-Tac-Toe agent trained from scratch using **pure Q-Learning** and vanilla Python. 

No deep neural networks, no PyTorch, and no TensorFlow—just the Bellman Equation, an environment state-space, and a 30,000-episode training loop to prove that mathematical intuition scales.

## 🧠 The "Why"
In an era of massive Large Language Models and automated MLOps pipelines, it is easy to lose sight of the raw math that powers artificial intelligence. I built this project to go back to the basics. By understanding exactly how a simple Q-table updates to force a win (or a draw) in a deterministic game, the jump to Deep Q-Networks (DQNs) and complex algorithmic systems becomes much more intuitive.

## ⚙️ How It Works (Under the Hood)

The agent learns via a classic reinforcement learning loop:
1. **State ($s$):** The current layout of the 3x3 board.
2. **Action ($a$):** Placing an 'X' or an 'O' in an empty cell.
3. **Reward ($R$):** The agent receives `+1` for a win, `-1` for a loss, and `0` for a draw or a standard move.
4. **Learning:** After every move, the agent updates its "knowledge" (the Q-table) using the **Bellman Equation**:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

*Where:*
* $\alpha$ is the learning rate.
* $\gamma$ is the discount factor (valuing immediate rewards vs. future traps).
* $\max_{a'} Q(s', a')$ represents the maximum expected future reward for the next state.

Early in the 30,000 training episodes, the agent explores randomly. By the end, it exploits its Q-table to become practically unbeatable.

## 🚀 Features
* **Zero Dependencies:** Written entirely in standard Python (`random`, `time`, `os`).
* **Instant Training:** Trains both an X and O agent for 30,000 episodes on startup in a matter of seconds.
* **Interactive CLI:** A clean command-line interface to interact with the environment.
* **Simulation Mode:** Watch the trained AI play against itself to observe optimal play.
* **Human vs. AI:** Play against the agent (as 'O') and try to beat it. 

## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/q-learning-tictactoe.git](https://github.com/yourusername/q-learning-tictactoe.git)
   cd q-learning-tictactoe

2.**Run the script:**
    python tic_tac_toe.py

3.**=== Q-Learning Tic-Tac-Toe ===**
1. Watch AI vs AI Simulation
2. Play vs AI (You play as O)
3. Exit

 🛠️ Code Structure
TicTacToe Class: Manages the environment, board state, available moves, and win/draw conditions.

train_agents(): Handles the episodic training loop, reward distribution, and Q-value updates.

CLI Loop: Manages user inputs, rendering the board, and clearing the terminal for a clean UI.

🤝 Let's Connect
I'm a Data Scientist / AI Engineer student passionate about both the high-level applications and the low-level mathematics of Machine Learning.

Connect with me on LinkedIn

Read my post detailing the logic behind this project [here](https://www.linkedin.com/posts/sagar-patle-304ab1300_machinelearning-reinforcementlearning-python-activity-7446568767213568000-kLwR?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAE0Me3QB8KyuxgoaZ9tUGsTiT4judQ2LNYI).
