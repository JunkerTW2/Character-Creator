# Limited by what I know in python currently, but I will expand on this in the future to include more features and options for character creation and management.
while True: # Loop to ensure valid menu selection.
    selection = input("Select an option: ")
    if selection == "1":
        print("Creating a new character")
        name = input("Enter character name: ")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        while True: # Loop to ensure valid class selection.
            character_class = input("Select character class: ")
            if character_class in ["1", "2", "3"]:
                break
            else:
                print("Invalid class selection. Please choose a valid option.")
        # Inheritance and class-specific attributes can be implemented here in the future as I learn more about Python.
        if character_class == "1":
            print(f"{name} the Warrior has been created!")
        elif character_class == "2":
            print(f"{name} the Mage has been created!")
        elif character_class == "3":
            print(f"{name} the Rogue has been created!")
        else:
            print("Invalid class selection.")
        while True: # Loop to ensure valid menu selection.
            print(f"{name}'s Character Profile")
            print("1. Strengths")
            print("2. Weaknesses")
            print("3. Motivations")
            print("4. Goals")
            print("5. Personality Traits")
            print("6. Backstory")
            selection = input("Select an option: ")
            if selection in ["1", "2", "3", "4", "5", "6"]:
                break
            else:
                print("Invalid profile selection. Please choose a valid option.")
            # Note to self: Refresher on inheritance logic.
            # Placeholder for character profile management functionality, allowing the user to choose different aspects of their character's profile to create.
            if selection == "1":
                print(f"{name}'s Strengths: ")
                # Placeholder for choosing a character's strengths based on a tag system.
            if selection == "2":
                print(f"{name}'s Weaknesses: ")
                # Placeholder for choosing a character's weaknesses based on a tag system.
            if selection == "3":
                print(f"{name}'s Motivations: ")
                # Placeholder for choosing a character's motivations based on a tag system.
            if selection == "4":
                print(f"{name}'s Goals: ")
                # Placeholder for choosing a character's goals based on a tag system.
            if selection == "5":
                print(f"{name}'s Personality Traits: ")
                # Placeholder for choosing a character's personality traits based on a tag system.
            if selection == "6":
                print(f"{name}'s Backstory: ")
                # Placeholder for choosing a character's backstory based on a tag system.
    elif selection == "2":
        print("Loading existing character...")
        # Placeholder for loading character functionality
    elif selection == "3":
        print("Exiting the character creation system. Goodbye!")
        # Exit the program. Maybe even break to a new menu in the future.
        break
    else:
        print("Invalid selection. Please choose a valid option.")
    
