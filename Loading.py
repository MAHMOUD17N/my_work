import pygame
import sys
import math

def main():
    pygame.init()
    screen_width, screen_height = 800, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Loading Animation - Real Collision")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font_large = pygame.font.SysFont("Arial", 80, bold=True)

    letters = ["L", "o", "a", "d", "ı", "n", "g"]
    x_positions = [180, 240, 290, 340, 395, 435, 485]
    base_y = 250 

    pos_L_x = x_positions[0] + 25
    pos_I_x = x_positions[4] + 12

    touch_y = 172 
    jump_height = 120  

    dot_x = pos_L_x
    dot_y = touch_y
    
    progress = 0.0      
    direction = 1       
    letter_scales = [1.0] * len(letters)

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        progress += 0.025 * direction 
        
        if progress >= 1.0:
            progress = 1.0
            direction = -1        
            letter_scales[4] = 0.55  

        elif progress <= 0.0:
            progress = 0.0
            direction = 1         
            letter_scales[0] = 0.55  

        dot_x = pos_L_x + (pos_I_x - pos_L_x) * progress
        
        dot_y = touch_y - (math.sin(progress * math.pi) * jump_height)

        for i in range(len(letter_scales)):
            if letter_scales[i] < 1.0:
                letter_scales[i] += 0.04  
                if letter_scales[i] > 1.0:
                    letter_scales[i] = 1.0

        for i, char in enumerate(letters):
            char_surface = font_large.render(char, True, BLACK)
            orig_w, orig_h = char_surface.get_size()
            
            scale_y = letter_scales[i]
            scale_x = 1.0 + (1.0 - scale_y) * 0.4  
            
            new_w = int(orig_w * scale_x)
            new_h = int(orig_h * scale_y)
            
            scaled_surface = pygame.transform.smoothscale(char_surface, (new_w, new_h))
            
            render_x = x_positions[i] - (new_w - orig_w) // 2
            render_y = base_y - new_h
            
            screen.blit(scaled_surface, (render_x, render_y))

        pygame.draw.circle(screen, BLACK, (int(dot_x), int(dot_y)), 8)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



#  loading



