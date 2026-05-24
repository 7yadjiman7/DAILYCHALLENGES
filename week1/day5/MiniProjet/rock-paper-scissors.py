from DAILYCHALLENGES.week1.day5.MiniProjet.game import Game


def get_user_menu_choice():
    """
    Display the main menu, validate input, and return the user's choice.
    Possible returns: 'p' (play), 's' (scores), 'q' (quit).
    No looping inside this function.
    """
    print("\n╔══════════════════════════╗")
    print("║   ROCK · PAPER · SCISSORS ║")
    print("╠══════════════════════════╣")
    print("║  [p] Play a new game      ║")
    print("║  [s] Show scores          ║")
    print("║  [q] Quit                 ║")
    print("╚══════════════════════════╝")

    choice = input("Your choice: ").strip().lower()

    if choice not in ("p", "s", "q"):
        print(f"  ✗ '{choice}' is not a valid option. Please choose p, s, or q.")
        return None     # caller decides what to do with invalid input

    return choice


def print_results(results):
    """
    Print a friendly summary of all games played.
    results: dict like {'win': 2, 'loss': 4, 'draw': 3}
    """
    total = sum(results.values())
    print("\n╔══════════════════════════╗")
    print("║        GAME SUMMARY       ║")
    print("╠══════════════════════════╣")
    print(f"║  Games played : {total:<10}║")
    print(f"║  Wins         : {results['win']:<10}║")
    print(f"║  Losses       : {results['loss']:<10}║")
    print(f"║  Draws        : {results['draw']:<10}║")
    print("╚══════════════════════════╝")
    print("Thanks for playing! See you next time 👋\n")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice is None:
            # Invalid input — just show the menu again
            continue

        elif choice == "p":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "s":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()