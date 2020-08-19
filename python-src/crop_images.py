import pygame, sys 
from PIL import Image 

pygame.init()

def displayImage( screen, px, topleft):
     screen.blit(px, px.get_rect())
     if topleft:
         pygame.draw.rect( screen, (128,128,128), pygame.Rect(topleft[0], topleft[1], pygame.mouse.get_pos()[0] - topleft[0], pygame.mouse.get_pos()[1] - topleft[1]))
     pygame.display.flip()  

def setup(path):
     px = pygame.image.load(path)
     screen = pygame.display.set_mode( px.get_rect()[2:] )
     screen.blit(px, px.get_rect())
     pygame.display.flip()
     return screen, px

def mainLoop(screen, px):
     topleft = None
     bottomright = None
     n=0
     while n!=1:
         for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONUP:
                 if not topleft:
                     topleft = event.pos
                 else:
                     bottomright = event.pos
                     n=1
         displayImage(screen, px, topleft)
     return ( topleft + bottomright )

if __name__ == "__main__":
     input_loc="C:\pic1.PNG"
     output_loc="C:\pic2.PNG"
     screen, px = setup(input_loc)
     left, upper, right, lower = mainLoop(screen, px)
     im = Image.open(input_loc)
     im = im.crop(( left, upper, right, lower))
     pygame.display.quit()
     im.save(output_loc)