Turtle Crosser Game
This Python-based game, built with the Turtle graphics library, challenges players to guide a turtle character safely across lanes of moving cars. The game leverages object-oriented design to modularize key functionalities for enhanced readability and maintainability.

Key Functionality and Class Structure

Player Control: The Player class encapsulates all logic related to the player’s movement. The player can move the turtle character using the Up and Down arrow keys.
Car Management: The CarManager class handles car creation and movement. Cars are generated randomly across the screen, with their speed increasing as the player advances to higher levels.
Scoreboard: The Scoreboard class tracks the player’s current level and displays a game-over message if the turtle collides with a car. Level increments each time the player reaches the finish line, adding a progressive difficulty element.

The main game loop continuously:
  Updates the screen,
  Generates new cars and moves them across the screen,
  Checks for collisions between the turtle and cars,
  Monitors if the player reaches the finish line, triggering a level increase.

This modular approach, with each non-library class addressing specific functionality, enhances the game's scalability and code maintainability.
