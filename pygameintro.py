from tkinter import EventType
import pygame
x= pygame.init() #this line will initialise al pygame modules
# print(x) 
# you get output: (5, 0) which means that 5modules gets initialized and 0 modules are unintialized.

# We want to creat a pygame window:
gameWindow= pygame.display.set_mode((1200,500))
# set_mode() takes a tuple containing width and height. (width,height)
# that window will come and then disappears.
# We fix it by creating a game loop.


# giving title to window:
pygame.display.set_caption("MyGame")

# when we make a game, generally we have three types of simple events that is: start game, end game(when user close the game) and game over

exit_game=False #I made this variable bcoz when this variable gets true then exit from the program otherwise don't exit from the program.
game_over=False # this variable get true when his game gets over.

# creating Game loop:
while(not exit_game):
      for event in pygame.event.get():
            # In pygame.event.get() contains all events of pygame which we do from mouse or keyboard.
            #print(event) #you get all events

            # pygame.event
            # Manage the incoming events from various input devices and the windowing platform
            # See all pygame event in pygame documentation.
            if event.type==pygame.QUIT: #here we are checking that if event type is equal to QUIT event , then exit_game becomes true.
                  exit_game=True
            if event.type==pygame.KEYUP: # this if checks whtether key is pressed or not, if yes then it checks which key is pressed.
                  #checking for the  key press and similarly you can give keydown not keyright or keyleft.
                  # this is the syntax, and you have to remember it.
                  if event.key== pygame.K_RIGHT: #After checking for down key, now we are checking for the press for right key press.
                        print("You have pressed right key")
            ticks= pygame.time.get_ticks()
            if ticks>10000:
                  print(ticks)


# If you do not write pygame.quit() ,quit() your window not responds due to infinite while loop.



pygame.quit() #Here pygame quit first
quit() # hten program gets quit.

