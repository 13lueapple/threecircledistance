import pygame, sys, random, math


pygame.init()
WIDTH, HEIGHT = 1200, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


Font_size = 30
Font = pygame.font.SysFont("malgungothic", Font_size)

Font_size1 = 45
Font1 = pygame.font.SysFont("malgungothic", Font_size1)

class Circle:
    number = 0
    def __init__(self, color, name, font, font_size) -> None:
        self.posX = random.choice(range(200, WIDTH, 100))
        self.posY = random.choice(range(200, HEIGHT, 100))
        self.color = color
        self.font_size = font_size
        self.font = font
        self.name = name
        Circle.number += 1
        self.number = Circle.number

    def get_pos(self):
        return self.posX, self.posY

    def get_color(self):
        return self.color

    def get_radius(self):
        m_posX, m_posY = pygame.mouse.get_pos()
        return round(math.sqrt(math.pow(m_posX - self.posX, 2) + math.pow(m_posY - self.posY, 2)))
    
    def render_text(self):
        self.cnt = f"원 {self.name}의 좌표 : {self.get_pos()}, 반지름(거리) : {self.get_radius()}"
        return self.font.render(self.cnt, False, self.color)
    
    def blit_text(self, win):
        win.blit(self.render_text(), (0, HEIGHT - (self.font_size)*self.number - 30))

    def get_name(self):
        return self.name
    

class intersection:
    def __init__(self, cA: Circle, cB: Circle, cC: Circle) -> None:
        self.x1, self.y1 = cA.posX, cA.posY
        self.x2, self.y2 = cB.posX, cB.posY
        self.x3, self.y3 = cC.posX, cC.posY
        

    def calculate(self, cA, cB, cC):
        self.r1, self.r2, self.r3 = cA.get_radius(), cB.get_radius(), cC.get_radius()
        self.A = 2*(self.x2 - self.x1)
        self.B = 2*(self.y2 - self.y1)
        self.C = math.pow(self.x1, 2) - math.pow(self.x2, 2) + math.pow(self.y1, 2) - math.pow(self.y2, 2) + math.pow(self.r2, 2) - math.pow(self.r1, 2)
        self.D = 2*(self.x3 - self.x2)
        self.E = 2*(self.y3 - self.y2)
        self.F = math.pow(self.x2, 2) - math.pow(self.x3, 2) + math.pow(self.y2, 2) - math.pow(self.y3, 2) + math.pow(self.r3, 2) - math.pow(self.r2, 2)

        self.x = (self.C*self.E - self.B*self.F)/(self.B*self.D - self.A*self.E)
        self.y= (self.D*self.C - self.F*self.A)/(self.E*self.A - self.B*self.D)
        return format(self.x, ".5f"), format(self.y, ".5f")
    
        
    

circle1 = Circle(RED, 'R', Font, Font_size)
circle2 = Circle(GREEN, 'G', Font, Font_size)
circle3 = Circle(BLUE, 'B', Font, Font_size)

calculator = intersection(circle1, circle2, circle3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    window.fill(BLACK)
    
    pygame.draw.circle(window, circle1.get_color(), circle1.get_pos(), circle1.get_radius(), 5)
    pygame.draw.circle(window, circle2.get_color(), circle2.get_pos(), circle2.get_radius(), 5)
    pygame.draw.circle(window, circle3.get_color(), circle3.get_pos(), circle3.get_radius(), 5)
    pygame.draw.circle(window, circle1.get_color(), circle1.get_pos(), 5)
    pygame.draw.circle(window, circle2.get_color(), circle2.get_pos(), 5)
    pygame.draw.circle(window, circle3.get_color(), circle3.get_pos(), 5)

    circle1.blit_text(window)
    circle2.blit_text(window)
    circle3.blit_text(window)

    finalCoord = list(map(float, calculator.calculate(circle1, circle2, circle3)))
    pygame.draw.circle(window, WHITE, finalCoord, 10)
    window.blit(Font1.render(str(f"원의 교점:{calculator.calculate(circle1, circle2, circle3)}"), False, WHITE), (30,300-Font_size1))
    window.blit(Font1.render(str(f"마우스 위치:{pygame.mouse.get_pos()}"), False, WHITE), (30,300))
    

    pygame.display.update()