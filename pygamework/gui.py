import pygame

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.half_screen_w = int(pygame.display.get_surface().get_size()[0]/2)
        self.half_screen_h = int(pygame.display.get_surface().get_size()[1]/2)
        self.screen_w = pygame.display.get_surface().get_size()[0]
        self.screen_h = pygame.display.get_surface().get_size()[1]

    def apply(self, target):
        return target.rect.move(self.rect.topleft)

    def update(self, target):
        left = -target.rect.x+self.half_screen_w
        top = -target.rect.y+self.half_screen_h

        self.rect = pygame.Rect(left, top, self.screen_w, self.screen_h)

class BoundCamera(Camera):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def update(self, target):
        left = -target.rect.x+self.half_screen_w
        top = -target.rect.y+self.half_screen_h

        left = min(0, left)
        top = min(0,top)
        left = max(-(self.width - self.screen_w), left)
        top = max(-(self.height - self.screen_h), top)
        self.rect = pygame.Rect(left, top, self.screen_w, self.screen_h)

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, pos, size, value, color=(0,255,0)):
        self.value = value
        self.max_value = value
        self.size = size
        self.color = color
        self.bg_color = (255,0,0)
        self.pos = pos
    
    def draw(self, screen):
        if self.value < 0:
            self.value = 0
        pygame.draw.rect(screen, (255,255,255), (self.pos.x-1, self.pos.y-1, ((self.size.x+2)*self.max_value)/100, self.size.y+2), 1)
        pygame.draw.rect(screen, self.bg_color, (self.pos.x, self.pos.y, (self.size.x*self.max_value)/100, self.size.y))
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, (self.size.x*self.value)/100, self.size.y))

class Label(pygame.sprite.Sprite):
    def __init__(self, pos, text, font_size=20, text_color=(255,255,255)):
        self.font = pygame.font.SysFont("Aryal", font_size)
        self.text = text
        self.color = text_color
        self.image = self.font.render(self.text, True, self.color)
        self.pos = pos
    
    def set_font(self, font):
        self.font = font

    def set_text(self, txt):
        self.text = txt

    def draw(self, screen):
        self.image = self.font.render(self.text, True, self.color)
        screen.blit(self.image, (self.pos.x, self.pos.y))


class Button(pygame.sprite.Sprite):
    def __init__(self, text, pos, font_size=20, color=(0,0,0), text_color=(255,255,255)):
        self.font = pygame.font.SysFont("Aryal", font_size)
        self.text = text
        self.color = color
        self.hover_color = (127,127,127)
        self.text_color = text_color
        self.txt_image = self.font.render(self.text, True, self.text_color)
        self.rect = self.txt_image.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y
        self.mouse_hover = False
    
    def set_text(self, txt):
        self.text = txt
    
    def set_font(self, font):
        self.font = font
    
    def on_mouse_inside(self):
        mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],5,5)
        self.mouse_hover = self.rect.colliderect(mouse_rect)
    
    def update(self):
        self.on_mouse_inside()
    
    def on_click(self, call_back):
        call_back()

    def draw(self, screen):
        self.txt_image = self.font.render(self.text, True, self.text_color)
        self.rect = self.txt_image.get_rect(center=self.rect.center)
        btn_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width+20, self.rect.height)
        if self.mouse_hover:
            pygame.draw.rect(screen, self.hover_color, btn_rect, 2, 10)
        else:
            pygame.draw.rect(screen, self.color, btn_rect, 2, 10)
        screen.blit(self.txt_image, self.rect)

class InputField(pygame.sprite.Sprite):
    def __init__(self, pos, size, font_size=20, text_color=(255,255,255)):
        super().__init__()
        self.text = ""
        self.size = size
        self.color = text_color
        self.bg_color = (255,255,255)
        self.font = pygame.font.SysFont("Aryal", font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.active = False

    def set_font(self, font):
        self.font = font

    def select(self):
        self.active = self.rect.collidepoint(pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

    def update(self, txt):
        if self.active:
            self.text += txt
    
    def delete(self):
        if self.active:
            self.text = self.text[:-1]

    def draw(self, screen):
        self.rect.width = max(self.size.x, self.image.get_width()+10)
        self.image = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.bg_color, self.rect, 2)
        screen.blit(self.image, self.rect)