import pygame

class Entity:
    screen = None

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pass

    def update(self):
        pass

class Player (Entity):
    x = 0
    y = 0
    color = None
    velocidade = 7

    def __init__(self, screen, x, y, color):
        super().__init__(screen)
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            [self.x, self.y, 30, 100]
        )
class Ball (Entity):
    x = 0
    y = 0
    velocidade = 2
    primeira_vez = 1
    raio = 10
    factor_x = 1
    factor_y = 1
    width = None

    def __init__(self, screen,  x, y):
        super().__init__(screen)
        self.x = x
        self.y = y
        self.raio = 10
        self.velocidade = 4
        self.factor_x = 1
        self.factor_y = 1
        self.width, self.height = screen.get_size()

    def update(self, player_1, player_2):
        self.x += self.velocidade * self.factor_x
        self.y += self.velocidade * self.factor_y

        # Colisão com o topo/fundo do ecrã
        if self.y - self.raio <= 0 or self.y + self.raio >= self.height:
            self.factor_y *= -1

        # Collision com Jogador 1
        if (player_1.x < self.x < player_1.x + 30 and
                player_1.y < self.y < player_1.y + 100):
            self.factor_x = 1  # Bounce right

        # Collision com Jogador 2
        if (player_2.x < self.x < player_2.x + 30 and
                player_2.y < self.y < player_2.y + 100):
            self.factor_x = -1  # Bounce left

        # Bola fora do limite do ecrã
        if self.x < 0 or self.x > self.width:
            self.reset()

    def draw(self):
        pygame.draw.circle(
            self.screen,
            (34, 34, 34),
            [self.x, self.y],
            self.raio
        )

    def reset(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.factor_x *= -1  # Muda direcção
        self.factor_y *= -1