# adventure_game.py
# Task 1: Set up the project
# Purpose: This script is a text-based adventure game created for Simplilearn Project 2.
# It uses functions and conditionals to navigate a quest for hidden treasure.
# Actions: Folder created, adventure_game.py initialized.

import sys

# --- Optimization: Helper Function for Input Validation ---
def prompt_choice(prompt: str, choices: tuple[str, ...]) -> str:
    """Prompt the user until they enter one of the allowed choices (Normalized to lower)."""
    choices_lower = tuple(c.lower() for c in choices)
    while True:
        resp = input(prompt).strip().lower()
        if resp in choices_lower:
            return resp
        print(f"Please enter one of: {', '.join(choices)}")

# Task 2: Create a function to start the game
# Actions: Define start_game(), display intro, ask for name, and provide initial path choice.
def start_game():
    """Displays the game introduction and gathers player information."""
    print("\n--- ⚔️  WELCOME TO THE ANCIENT LAND QUEST ⚔️  ---")
    print("Your mission is to find the legendary treasure hidden in this land.")
    
    # Actions: Ask the player for their name and store it in a variable
    player_name = input("What is your name, brave explorer? ").strip()
    if not player_name:
        player_name = "Explorer"
    
    print(f"\nGreetings, {player_name}. Your journey begins at a fork in the road.")
    
    # Actions: Provide the player with an initial choice (explore a forest or enter a cave)
    choice = prompt_choice("Do you want to explore the 'forest' or enter the 'cave'? ", ("forest", "cave"))
    
    success_points = 0
    if choice == "forest":
        if forest_path():
            success_points += 1
    else:
        if cave_path():
            success_points += 1

    # Task 4 Expansion: Moving toward the treasure via the Ruins
    if ruins_search():
        success_points += 1

    # Final logic to determine Winning or Losing outcome
    # Winning: Finding the treasure (requires map fragment or solving the lock)
    has_map = success_points >= 2
    if final_chamber(has_map):
        print("\nWINNING: Congratulations! You found the hidden treasure—gold and a glowing gem!")
    else:
        print("\nLOSING: You made a poor decision or failed a challenge. The adventure ends.")
    
    play_again()

# Task 3: Create the forest path
# Actions: Define forest_path(), provide river/tree choices, use if-else for outcomes.
def forest_path() -> bool:
    """Describes the forest scenario and handles player choices."""
    print("\nYou walk into a dense forest. The light grows dim and the path splits.")
    # Actions: Provide choices (follow a river or climb a tree)
    # Using your version 1 story logic (river=music, tree=smoke/guard)
    choice = prompt_choice("Do you 'follow river' (toward music) or 'climb tree' (toward smoke)? ", ("follow river", "climb tree"))
    
    if "river" in choice:
        print("You follow the music and find travelers who give you a clue: 'Seek the sun stone.'")
        return True
    else:
        print("You climb a tree and see a guard. Do you try to 'sneak' or 'wake' the guard?")
        sub = prompt_choice("> ", ("sneak", "wake"))
        if sub == "sneak":
            print("You sneak past and find footprints leading to the ruins.")
            return True
        else:
            print("The guard wakes angrily and casts you out of the forest.")
            return False

# Task 4: Create the cave path
# Actions: Define cave_path(), provide torch/dark choices, use conditionals for outcomes.
def cave_path() -> bool:
    """Describes the cave scenario and uses conditionals to determine the outcome."""
    print("\nA cave yawns before you. It's cold and the floor is slick.")
    # Actions: Provide choices (light a torch or proceed in the dark)
    choice = prompt_choice("Do you 'light torch' or 'proceed in dark'? ", ("light torch", "proceed in dark"))
    
    if choice == "light torch":
        print("Inside, the cave forks. Take the 'glow' path or the 'silent' path?")
        branch = prompt_choice("> ", ("glow", "silent"))
        if branch == "glow":
            print("The glowing path leads to a riddle: I speak without a mouth and hear without ears.")
            answer = input("What am I? ").strip().lower()
            if "echo" in answer:
                print("Correct! You found a map fragment.")
                return True
            print("Wrong! A trapdoor opens and you fall into a pit.")
            return False
        else:
            print("The silent path reveals a stone with a carved sun. You found a landmark!")
            return True
    else:
        print("LOSING: You trip in the dark and get hopelessly lost.")
        return False

# Intermediate logic: Strategic decision at the Ruins
def ruins_search() -> bool:
    print("\nYou arrive at the ruined temple. Columns lean and vines choke the stones.")
    choice = prompt_choice("Do you search 'inside' the temple or around the 'grounds'? ", ("inside", "grounds"))
    if choice == "grounds":
        print("You find a loose flagstone that reveals a narrow tunnel. You advance safely.")
        return True
    else:
        print("Inside the temple, alarm bells ring! Do you 'hide' or 'run'?")
        evade = prompt_choice("> ", ("hide", "run"))
        if evade == "hide":
            print("You avoid the trap and move forward.")
            return True
        return False

# Final Challenge: Navigating the final quest goal
def final_chamber(has_map: bool) -> bool:
    print("\nYou reach a heavy stone door engraved with a sun.")
    if not has_map:
        print("Without a map, you struggle. Try to 'solve' the pattern or 'force' the door?")
        attempt = prompt_choice("> ", ("solve", "force"))
        if attempt == "force": return False
    
    code = input("Enter the three-letter lockcode (Hint: 'sun'): ").strip().lower()
    return code == "sun"

# Task 5: Run the adventure game
# Actions: Call start_game(), run in loop, provide restart option.
def play_again():
    """Provides an option to restart the game after completion."""
    # Restarting: Choosing to replay the game after an unsuccessful attempt
    again = prompt_choice("\nRESTARTING: Would you like to play again? (yes/no): ", ("yes", "no"))
    if again == "yes":
        start_game()
    else:
        print("Thanks for playing, Farewell adventurer!")
        sys.exit()

if __name__ == "__main__":
    # Task 1 Action: Simple print statement to confirm that the setup is working
    print("--- SYSTEM CHECK: Environment Setup Confirmed. Initializing Quest... ---\n")
    # Action: Call start_game() to begin the adventure
    start_game()