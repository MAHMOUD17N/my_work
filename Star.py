import pygame
import math
import random

WIDTH, HEIGHT = 1000, 800  
FPS = 60
BLACK = (12, 8, 20)       
YELLOW = (255, 230, 50)   
ORANGE = (255, 100, 30)   

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmos Star - Final Outline Simulation")
clock = pygame.time.Clock()

def calculate_star_points(cx, cy, spikes, outer_radius, inner_radius):
    points = []
    angle = -math.pi / 2  
    for i in range(spikes * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        x = cx + math.cos(angle) * r
        y = cy + math.sin(angle) * r
        points.append((x, y))
        angle += math.pi / spikes
    points.append(points[0])
    return points

class BackgroundStar:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.size = random.uniform(0.5, 1.5)  
        self.speed = random.uniform(0.2, 0.6)  
        self.alpha = random.randint(100, 255)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.uniform(0, WIDTH)

    def draw(self, surface):
        s_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(s_surface, (255, 255, 255, self.alpha), (self.size, self.size), self.size)
        surface.blit(s_surface, (self.x - self.size, self.y - self.size))

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1.0, 3.5) 
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.radius = random.uniform(2.0, 4.5) 
        self.alpha = 255
        self.fade_speed = random.uniform(1.5, 3.0) 
        self.color = random.choice([YELLOW, ORANGE, (255, 60, 0)])

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.alpha -= self.fade_speed
        if self.radius > 0.1:
            self.radius -= 0.02

    def draw(self, surface):
        if self.alpha > 0 and self.radius > 0:
            p_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            color_with_alpha = (self.color[0], self.color[1], self.color[2], int(self.alpha))
            pygame.draw.circle(p_surface, color_with_alpha, (self.radius, self.radius), self.radius)
            surface.blit(p_surface, (self.x - self.radius, self.y - self.radius))

cx, cy = WIDTH // 2, HEIGHT // 2
star_vertices = calculate_star_points(cx, cy, 5, 220, 95)
total_segments = len(star_vertices) - 1

bg_stars = [BackgroundStar() for _ in range(150)]

state = "ERASING"  
progress = 1.0     
speed = 0.0035     
particles = []

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for bg_star in bg_stars:
        bg_star.update()
        bg_star.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def get_pos_on_star(p_val):
        if p_val <= 0.0:
            return star_vertices[0][0], star_vertices[0][1]
        if p_val >= 1.0:
            return star_vertices[-1][0], star_vertices[-1][1]
        
        pos = p_val * total_segments
        idx = int(pos)
        rem = pos - idx
        
        x1, y1 = star_vertices[idx]
        x2, y2 = star_vertices[idx + 1]
        
        rx = x1 + (x2 - x1) * rem
        ry = y1 + (y2 - y1) * rem
        return rx, ry

    if state == "ERASING":
        progress -= speed
        if progress <= 0.0:
            progress = 0.0
            state = "FORWARD_DRAW"

        current_max_idx = int(progress * total_segments)
        current_points = star_vertices[:current_max_idx + 1]
        erase_x, erase_y = get_pos_on_star(progress)
        current_points.append((erase_x, erase_y))

        if len(current_points) >= 2:
            pygame.draw.lines(screen, ORANGE, False, current_points, 8)
            pygame.draw.lines(screen, YELLOW, False, current_points, 4)

        if progress > 0.0:
            for _ in range(6):
                particles.append(Particle(erase_x, erase_y))

    elif state == "FORWARD_DRAW":
        progress += speed
        if progress >= 1.0:
            progress = 1.0
            state = "FINISHED"

        current_max_idx = int(progress * total_segments)
        current_points = star_vertices[:current_max_idx + 1]
        draw_x, draw_y = get_pos_on_star(progress)
        current_points.append((draw_x, draw_y))

        if len(current_points) >= 2:
            pygame.draw.lines(screen, ORANGE, False, current_points, 8)
            pygame.draw.lines(screen, YELLOW, False, current_points, 4)

        if progress < 1.0:
            for _ in range(3):
                particles.append(Particle(draw_x, draw_y))

    elif state == "FINISHED":
        pygame.draw.lines(screen, ORANGE, False, star_vertices, 8)
        pygame.draw.lines(screen, YELLOW, False, star_vertices, 4)

    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.alpha <= 0:
            particles.remove(p)

    pygame.display.flip()

pygame.quit()


# star with python
