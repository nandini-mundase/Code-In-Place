from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_back():
    turn_left()
    turn_left()

def main():
    move()
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    put_beeper()
    turn_back()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_back()

if __name__=="__main__":
    main()


