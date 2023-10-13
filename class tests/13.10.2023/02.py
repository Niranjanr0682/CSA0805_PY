# Create a Python word-guessing game where the program has a predefined list of
# 5 words. The player is prompted to input a keyword, and the program searches
# the list for a match. Starting with 10 points, each incorrect guess deducts 2
# points. If the player guesses the keyword correctly, the program displays
# congratulations and the final points. When points hit 0, a "try again" message is shown.

words = ["hello", "world", "python", "programming", "game"]
keyword = input("Enter a keyword: ").lower()
points = 10
while points:
    if keyword in words:
        print("Congratulations! You guessed the keyword correctly.")
        print("Your final points are:", points)
        break
    else:
        points -= 2
        if points <= 0:
            print("You have run out of points. Try again!")
        else:
            print("Incorrect guess. You have", points, "points left.")
            print("Try again:")
            keyword = (input("Enter a keyword: ").lower())
