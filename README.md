# Snake Game
-------------------------------------------------------------------------------------------------------------------------------------------------
A classic Snake game implemented in Python using the Pygame library. Control the snake to eat food, grow longer, and try to achieve the highest score possible. Avoid colliding with walls or the snake itself to keep the game going.

# Features
-------------------------------------------------------------------------------------------------------------------------------------------------
Smooth snake movement with arrow keys.
Dynamic food spawning.
Collision detection for both walls and the snake's body.
Score tracking displayed on the screen.

# Requirements
-------------------------------------------------------------------------------------------------------------------------------------------------
To run the game, ensure you have Python and Pygame installed on your system.

bash
pip install pygame
How to Play
Run the game script:

bash
python snake_game.py
Use the arrow keys to control the snake's direction:
Up Arrow to move up.
Down Arrow to move down.
Left Arrow to move left.
Right Arrow to move right.
The goal is to eat the red food blocks, which increases the snake's length and your score.
The game ends when:
The snake collides with the screen boundaries.
The snake collides with itself.

# Code Explanation
-------------------------------------------------------------------------------------------------------------------------------------------------
# Game Setup
Screen Dimensions: The game runs in an 800x600 pixel window.
Cell Size: The grid size is set to 20x20 pixels for snake and food positions.
Colors: Defined RGB values for black (background), green (snake), and red (food).

# Main Components
-------------------------------------------------------------------------------------------------------------------------------------------------
# Snake Initialization:
The snake starts as a list of segments represented by coordinates.
The initial direction of movement is set to "RIGHT".
Food Initialization:

Food is randomly placed within the game boundaries, snapping to the grid defined by CELL_SIZE.
Score Tracking:

The score is updated each time the snake eats food.
The score is displayed on the screen using the Pygame font system.

# Game Loop
-------------------------------------------------------------------------------------------------------------------------------------------------
The game runs in a continuous loop until the player quits or the snake collides with a wall or itself. Key steps include:

# Event Handling:
-------------------------------------------------------------------------------------------------------------------------------------------------
Detect key presses to change the snake's direction (while ensuring it doesn't reverse).
Snake Movement:

The snake's head moves in the current direction.
The new head position is calculated and added to the snake's body.

# Collision Detection:

With Food: If the snake's head collides with the food, the snake grows by one segment, and the score is incremented.
With Boundaries: If the snake's head crosses the game window boundaries, the game ends.
With Itself: If the snake's head collides with any part of its body, the game ends.

# Rendering:
The screen is cleared and redrawn with the updated snake, food, and score.
Frame Rate Control:

The frame rate is set to 10 frames per second to manage game speed.

# Functions
draw_snake(snake_body): Draws the snake on the screen.
draw_food(food_pos): Draws the food on the screen.
display_score(score): Displays the current score in the top-left corner.
Game Over
When the game ends, a message is displayed in the terminal with the final score, and the game window closes.

# Example Gameplay
-------------------------------------------------------------------------------------------------------------------------------------------------
Starting State:
A green snake begins at the top-left of the screen.
A red food block is randomly placed on the grid.
During Play:
The snake moves in the chosen direction, eating food to grow.
Game Over:
The game ends when the snake hits a wall or itself, with the score displayed in the terminal.
