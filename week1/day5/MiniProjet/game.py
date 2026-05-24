import random

ITEMS = ["rock", "paper", "scissors"]

# Qui bat qui : clé bat valeur
BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

class Game:

    def get_user_item(self):
        while True:
            user_item = input("Your move — rock / paper / scissors: ").strip().lower()
            if user_item in ITEMS:
                return user_item 
            print(f"  ✗ '{user_item}' is not valid. Please type rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(ITEMS)

    def get_game_result(self, user_item, computer_item):
        """
        Compare user_item and computer_item.
        Returns 'win', 'draw', or 'loss'.
        """
        if user_item == computer_item:
            return "draw"
        elif BEATS[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        1. Determine & print the result.
        2. Return the result string: 'win' | 'draw' | 'loss'.
        """
        # Get user item 
        user_item = self.get_user_item()

        # Get Computer item
        computer_item = self.get_computer_item()

        # Determine result
        result = self.get_game_result(user_item, computer_item)

        # Print outcome
        messages = {
            "win":  f"You selected {user_item}. The computer selected {computer_item}. You win! 🎉",
            "draw": f"You selected {user_item}. The computer selected {computer_item}. It's a draw! 🤝",
            "loss": f"You selected {user_item}. The computer selected {computer_item}. You lose! 💀",
        }
        print(messages[result])

        return result
        
        