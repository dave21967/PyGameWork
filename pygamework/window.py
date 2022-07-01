import pygame
from pygamework.input import Input

class Scene:
    def __init__(self, tree, *args):
        self.tree = tree
        self.args = args

    def on_scene_exit(self):
        pass

    def on_scene_entry(self):
        pass

    def on_key_pressed(self, key):
        pass

    def on_key_released(self, key):
        pass

    def on_key_typed(self, key, text):
        pass

    def on_mouse_button_down(self, button):
        pass

    def on_mouse_button_up(self, button):
        pass

    def on_mouse_moved(self, pos):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pass


class SceneTree:
    def __init__(self):
        self.scenes = {}
        self.run = True

    def set_scene(self, name, scene):
        self.scenes[name] = scene
    
    def get_scene(self, name):
        return self.scenes[name]

    def set_main_scene(self, name):
        if 'main' in self.scenes:
            self.scenes['main'].on_scene_exit()
        self.scenes['main'] = self.scenes[name]
        self.scenes['main'].on_scene_entry()
    
    def quit(self):
        self.run = False

class GameWindow:
    def __init__(self, width, height, title):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.tree = SceneTree()
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):
        while self.tree.run:
            dt = self.clock.tick(self.FPS)/1000
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    self.tree.quit()
                if evt.type == pygame.MOUSEBUTTONUP:
                    self.tree.get_scene("main").on_mouse_button_up(pygame.mouse.get_pressed())
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    self.tree.get_scene("main").on_mouse_button_down(pygame.mouse.get_pressed())
                if evt.type == pygame.KEYDOWN:
                    self.tree.get_scene("main").on_key_pressed(evt.key)
                    self.tree.get_scene("main").on_key_typed(evt.key, evt.unicode)
                if evt.type == pygame.KEYUP:
                    self.tree.get_scene("main").on_key_released(evt.key)
                if evt.type == pygame.MOUSEMOTION:
                    self.tree.get_scene("main").on_mouse_moved(Input.mouse_pos())
            
            self.tree.get_scene("main").update(dt)

            self.screen.fill((0,0,0))
            self.tree.get_scene("main").draw(self.screen)
            pygame.display.flip()
        
        pygame.quit()