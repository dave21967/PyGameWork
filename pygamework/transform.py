import pygame

class Transform:
    @staticmethod
    def flip_x(img):
        return pygame.transform.flip(img, True, False)
    
    @staticmethod
    def flip_y(img):
        return pygame.transform.flip(img, False, True)
    
    @staticmethod
    def rotate(img, angle):
        return pygame.transform.rotate(img, angle)