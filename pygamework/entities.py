import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
    
    def get_sprite(self, x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet, (0,0), (x,y,w,h))
        return sprite

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, pos, *groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y
    
    def update(self, dt):
        pass

    def draw(self,screen):
        screen.blit(self.image, self.rect)

class AnimatedSprite(Sprite):
    def __init__(self,sheet, pos, *groups):
        super().__init__(sheet, pos, groups)
        self.frame = 0
        self.anim_index = 0
        self.animations = {}

    def load_animations(self):
        pass
    
    def play(self, anim_name, fps=10):
        self.frame += 1
        
        if self.frame%fps == 0:
            if self.anim_index == (len(self.animations[anim_name])-1):
                self.anim_index = 0
            else:
                self.anim_index += 1

        self.image = self.animations[anim_name][self.anim_index]

class TmxTile(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)