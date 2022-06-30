import pygame
from pygame.math import Vector2

class Input:
    MOUSE_LEFT = 0
    MOUSE_MIDDLE = 1
    MOUSE_RIGHT = 2

    @staticmethod
    def mouse_pos():
        return Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    
    @staticmethod
    def mouse_pressed(btn):
        return pygame.mouse.get_pressed() == btn
    
    @staticmethod
    def mouse_rect():
        mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        return pygame.Rect(mouse_pos.x, mouse_pos.y, 5,5)