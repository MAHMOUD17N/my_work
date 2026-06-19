import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cute Lamp Interaction")

BG_DARK = (30, 35, 45)     
BG_LIGHT = (200, 190, 150)   
LAMP_COLOR = (120, 120, 130)
LIGHT_YELLOW = (255, 240, 150) 
CORD_COLOR = (180, 180, 180)

is_lit = False
cord_start_y = 380  
cord_current_y = 380
cord_max_pull = 440 
is_dragging = False

running = True
while running:
    screen.fill(BG_LIGHT if is_lit else BG_DARK)
    
    if is_lit:
        light_poly = [(200, 350), (400, 350), (550, 700), (50, 700)]
        light_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(light_surface, (255, 255, 150, 40), light_poly)
        screen.blit(light_surface, (0,0))

    pygame.draw.rect(screen, LAMP_COLOR, (290, 350, 20, 200)) 
    pygame.draw.ellipse(screen, LAMP_COLOR, (250, 530, 100, 30)) 

    lamp_poly = [(220, 180), (380, 180), (410, 350), (190, 350)]
    pygame.draw.polygon(screen, (150, 155, 170) if is_lit else LAMP_COLOR, lamp_poly)

    if is_lit:
        pygame.draw.circle(screen, (40, 40, 40), (270, 240), 6)
        pygame.draw.circle(screen, (40, 40, 40), (330, 240), 6)
        pygame.draw.arc(screen, (200, 50, 50), (285, 250, 30, 30), 3.14, 0, 15)
    else:
        pygame.draw.arc(screen, (40, 40, 40), (255, 235, 25, 20), 0, 3.14, 3)
        pygame.draw.arc(screen, (40, 40, 40), (320, 235, 25, 20), 0, 3.14, 3)
        pygame.draw.arc(screen, (40, 40, 40), (290, 260, 20, 10), 3.14, 0, 3)

    pygame.draw.line(screen, CORD_COLOR, (230, 350), (230, cord_current_y), 3)
    pygame.draw.circle(screen, (200, 200, 200), (230, cord_current_y), 8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (mouse_x - 230)**2 + (mouse_y - cord_current_y)**2 <= 15**2:
                is_dragging = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if is_dragging:
                if cord_current_y > cord_start_y + 30:
                    is_lit = not is_lit
                is_dragging = False
                cord_current_y = cord_start_y 

        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                mouse_y = event.pos[1]
                if mouse_y < cord_start_y:
                    cord_current_y = cord_start_y
                elif mouse_y > cord_max_pull:
                    cord_current_y = cord_max_pull
                else:
                    cord_current_y = mouse_y

    pygame.display.flip()

pygame.quit()
sys.exit()


# cute lamp
