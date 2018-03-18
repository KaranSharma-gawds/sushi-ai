import time
from coordinates import Coordinates
import controller
import recipes

def clear_tables():
    for plate in Coordinates.empty_plates:
        controller.mouse_click(plate)
    time.sleep(1)
    

def startGame():
    #play click
    controller.mouse_click(Coordinates.play_pos)
    #continue click
    controller.mouse_click(Coordinates.continue_pos)
    #second continue click
    controller.mouse_click(Coordinates.continue_pos)
    #skip click
    controller.mouse_click(Coordinates.skip_pos)
    #today's goal click
    controller.mouse_click(Coordinates.continue_pos)


# if __name__ == "__main__":
#     startGame()
