# Author- Marlee Hunter
# Purpose- Uses the graphics window to create a game to try and guess where the Champion(a hidden dot) is.
# User can click screen 14 times to try and guess. The distance from the champion is calculated each time
# along with the guess count. If the Champion is found, a message that the user won will show up, else a message
# that the user lost will show up


from graphics import *
import random

def distance(pt1, pt2):
    '''
    Purpose: calculate the distance between 2 graphics Points
    Pre-conditions: two Point objects
    Post-conditions: returns distance using distance formula
    '''
    return ((pt1.getX() - pt2.getX())**2 + (pt1.getY() - pt2.getY())** 2) ** 0.5

def drawPoint(pt, color, win):
    '''
    Purpose: draw a Circle of radius 6 at location given by pt with the color specified on the GraphWin win
    Pre-conditions: pt is a Point object which acts as center of circle, color is string, win is GraphWin object used to draw on 
    Post-conditions: a colored Circle of radius 6 is drawn on win, center at location given by pt
    '''
    c = Circle(pt, 6)
    c.setFill(color)
    c.draw(win)


def main():
    
    # Create a graphics window
    win = GraphWin("March Madness - Find the Champion", 800, 600)

    # Choose a random location for the Champion
    champion_x = random.randint(20, 780)
    champion_y = random.randint(20, 580)
    champion = Point(champion_x, champion_y)

    # Display instructions to the user
    instructions = Text(Point(400, 50), "Click on the window to find the Champion!")
    instructions.draw(win)
    
    # Get user's guess
    guess_point = win.getMouse()

    # Draw user's guess
    drawPoint(guess_point, "orange", win)    
    
    # Initialize counter for guesses
    guesses = 1
    
    # Display number of guesses
    guesses_label = Text(Point(700, 50), f"Guesses: {guesses}")
    guesses_label.draw(win)
    
    # Initialize the distance
    dist = distance(guess_point, champion)
    
    # Create a Text object for distance label
    distance_label = Text(Point(700, 100), f"Distance: {int(dist)}")
    distance_label.draw(win) 

    # Start the game loop
    while dist >= 10 and guesses < 15:
        
        # Get user's guess
        guess_point = win.getMouse()

        # Draw user's guess
        drawPoint(guess_point, "orange", win)

        # Increment guesses counter
        guesses += 1

        # Display number of guesses
        guesses_label.setText(f"Guesses: {guesses}")

        # Calculate distance between user's guess and Champion
        dist = distance(guess_point, champion)

        # Update distance text
        distance_label.setText(f"Distance: {int(dist)}")

    # Check if distance is less than or equal to 10
    if dist <= 10:
        
        # User found the Champion
        champion_text = Text(Point(400, 300), "You found the Champion!")
        champion_text.setSize(20)
        champion_text.setTextColor("green")
        champion_text.draw(win) 

    else:
        # Display message
        lost_text = Text(Point(400, 300), "Sorry, you didn't find the Champion!")
        lost_text.setSize(20)
        lost_text.setTextColor("red")
        lost_text.draw(win)

    # Draw the Champion (revealed)
    drawPoint(champion, "blue", win)

    # Wait for another click to close the window
    instructions.setText("Click anywhere to close the window.")
    win.getMouse()
    win.close()

main()

