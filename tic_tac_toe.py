import random
import time
import os

class TicTacToe:
    def __init__(self):
        # 0 = Empty, 1 = X, -1 = O
        self.board = [0] * 9 

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == 0]

    def make_move(self, position, player):
        self.board[position] = player

    def check_winner(self):
        win_cond = [(0,1,2), (3,4,5), (6,7,8), # Rows
                    (0,3,6), (1,4,7), (2,5,8), # Cols
                    (0,4,8), (2,4,6)]          # Diagonals
        
        for a, b, c in win_cond:
            if self.board[a] != 0 and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a] 
                
        if 0 not in self.board:
            return 'Draw'
        return None

    def get_state(self):
        return str(self.board)

    def render(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        b = [symbols[x] for x in self.board]
        print(f"\n {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} \n")

class QAgent:
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.q_table = {}
        self.epsilon = epsilon  
        self.alpha = alpha      
        self.gamma = gamma      

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, available_moves, training=True):
        if training and random.uniform(0, 1) < self.epsilon:
            return random.choice(available_moves)

        q_values = [self.get_q(state, a) for a in available_moves]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(available_moves, q_values) if q == max_q]
        return random.choice(best_actions)

    def update(self, state, action, reward, next_state, next_available_moves):
        current_q = self.get_q(state, action)
        max_next_q = max([self.get_q(next_state, a) for a in next_available_moves]) if next_available_moves else 0.0
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[(state, action)] = new_q

def train_agents(episodes=30000):
    env = TicTacToe()
    agent_x = QAgent() 
    agent_o = QAgent() 
    
    print(f"Training Agents... Running {episodes} rapid self-play games.")
    print("Please wait a few seconds...")
    
    for _ in range(episodes):
        env.__init__()
        agents = {1: agent_x, -1: agent_o}
        turn = 1
        last_state = {1: None, -1: None}
        last_action = {1: None, -1: None}
        
        while True:
            current_agent = agents[turn]
            state = env.get_state()
            available = env.available_moves()
            
            action = current_agent.choose_action(state, available, training=True)
            env.make_move(action, turn)
            winner = env.check_winner()
            
            if last_state[turn] is not None:
                current_agent.update(last_state[turn], last_action[turn], 0, state, available)
                
            if winner is not None:
                if winner == 'Draw':
                    r_x, r_o = 0.5, 0.5
                else:
                    r_x = 1 if winner == 1 else -1
                    r_o = 1 if winner == -1 else -1
                    
                current_agent.update(state, action, r_x if turn == 1 else r_o, None, [])
                
                other = -turn
                if last_state[other] is not None:
                    agents[other].update(last_state[other], last_action[other], r_o if other == -1 else r_x, None, [])
                break
                
            last_state[turn] = state
            last_action[turn] = action
            turn = -turn
            
    print("Training complete!\n")
    return agent_x, agent_o

def clear_screen():
    # Clears the terminal for animation effect
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_ai_vs_ai(agent_x, agent_o):
    env = TicTacToe()
    agents = {1: agent_x, -1: agent_o}
    turn = 1 
    
    while True:
        clear_screen()
        print("=== AI vs AI Simulation ===")
        print(f"Agent {'X' if turn == 1 else 'O'} is thinking...")
        env.render()
        time.sleep(0.8) # Pause so you can actually see the move
        
        state = env.get_state()
        available = env.available_moves()
        
        # training=False ensures they play their absolute best moves
        action = agents[turn].choose_action(state, available, training=False)
        env.make_move(action, turn)
        
        winner = env.check_winner()
        if winner is not None:
            clear_screen()
            print("=== AI vs AI Simulation ===")
            env.render()
            if winner == 'Draw':
                print("Result: Perfect Game - It's a Draw!")
            else:
                print(f"Result: Agent {'X' if winner == 1 else 'O'} Wins!")
            input("\nPress Enter to return to menu...")
            break
            
        turn = -turn

def play_human(agent):
    env = TicTacToe()
    turn = 1 
    
    while True:
        clear_screen()
        print("=== You vs AI ===")
        print("You are O. The Agent is X.")
        print("Positions are 0-8 (Top-Left to Bottom-Right)")
        env.render()
        
        if turn == 1:
            print("Agent's Turn...")
            time.sleep(0.5)
            action = agent.choose_action(env.get_state(), env.available_moves(), training=False)
            env.make_move(action, 1)
        else:
            valid = False
            while not valid:
                try:
                    action = int(input("Enter your move (0-8): "))
                    if action in env.available_moves():
                        valid = True
                    else:
                        print("Invalid move. Cell is taken or out of bounds.")
                except ValueError:
                    print("Please enter a valid number.")
            env.make_move(action, -1)
            
        winner = env.check_winner()
        if winner is not None:
            clear_screen()
            print("=== Final Board ===")
            env.render()
            if winner == 'Draw':
                print("Game Over: It's a Draw!")
            elif winner == 1:
                print("Game Over: Agent (X) Wins!")
            else:
                print("Game Over: You (O) Win! (Wait, how did you do that?!)")
            input("\nPress Enter to return to menu...")
            break
            
        turn = -turn

if __name__ == "__main__":
    # Train both agents on startup
    agent_x, agent_o = train_agents(episodes=30000)
    
    while True:
        clear_screen()
        print("=== Q-Learning Tic-Tac-Toe ===")
        print("1. Watch AI vs AI Simulation")
        print("2. Play vs AI (You play as O)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            simulate_ai_vs_ai(agent_x, agent_o)
        elif choice == '2':
            play_human(agent_x)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Press Enter to try again.")
            input()