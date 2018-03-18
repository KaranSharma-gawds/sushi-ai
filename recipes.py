from coordinates import Coordinates
import controller
import time
mouse_click = controller.mouse_click
'''
Recipes:

    onigiri:
        2 rice, 1 nori

    caliroll:
        1 rice, 1 nori, 1 roe

    gunkan:
        1 rice, 1 nori, 2 roe
'''

class MakeFood:
    def fold_mat(self):
        mouse_click(Coordinates.mat)
    
    def caliroll(self):
        print('making caliroll')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        mouse_click(Coordinates.food.roe)
        time.sleep(0.1)
        self.fold_mat()
    
    def onigiri(self):
        print('making onigiri')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        time.sleep(0.1)
        self.fold_mat()
    
    def gunkan(self):
        print('making gunkan')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        mouse_click(Coordinates.food.roe)
        mouse_click(Coordinates.food.roe)
        time.sleep(0.1)
        self.fold_mat()

class BuyFood:
    def rice():
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.rice_pos)
        mouse_click(Coordinates.phone.rice.rice)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def sake():
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.sake_pos)
        mouse_click(Coordinates.phone.sake.sake)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def shrimp():
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.toppings_pos)
        mouse_click(Coordinates.phone.toppings.topping11)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def unagi():
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.toppings_pos)
        mouse_click(Coordinates.phone.toppings.topping12)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def nori():    # nori
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.toppings_pos)
        mouse_click(Coordinates.phone.toppings.topping21)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def fish_egg():     # fish egg
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.toppings_pos)
        mouse_click(Coordinates.phone.toppings.topping22)
        mouse_click(Coordinates.phone.delivery.normal)
    
    def salmon():     # salmon
        mouse_click(Coordinates.phone_pos)
        mouse_click(Coordinates.phone.toppings_pos)
        mouse_click(Coordinates.phone.toppings.topping31)
        mouse_click(Coordinates.phone.delivery.normal)
    