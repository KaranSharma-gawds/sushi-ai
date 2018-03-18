from . import coordinates
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
    def fold_mat():
        mouse_click(Coordinates.mat)
    
    def caliroll():
        print('making caliroll')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        mouse_click(Coordinates.food.roe)
        time.sleep(0.1)
        fold_mat()
    
    def onigiri():
        print('making onigiri')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        time.sleep(0.1)
        fold_mat()
    
    def gunkan():
        print('making gunkan')
        mouse_click(Coordinates.food.rice)
        mouse_click(Coordinates.food.nori)
        mouse_click(Coordinates.food.roe)
        time.sleep(0.1)
        fold_mat()
