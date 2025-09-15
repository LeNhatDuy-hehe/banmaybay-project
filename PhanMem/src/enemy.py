import pygame
from utils import load_image
from settings import ENEMY_SIZE, cao, rong  # lấy luôn chiều cao, rộng màn hình
import random

class Dich(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        # Load ảnh địch
        enemy = load_image("image/enemy/enemy1.png")
        self.image = pygame.transform.scale(enemy, ENEMY_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

        # Thêm vận tốc ngang để bay chéo
        self.dx = random.choice([-2, -1, 1, 2])

    def update(self):
        # Bay xuống
        self.rect.y += self.speed
        # Bay chéo ngang
        self.rect.x += self.dx

        # Nếu chạm biên trái/phải thì đổi hướng, zigzag
        if self.rect.left <= 0 or self.rect.right >= rong:
            self.dx = -self.dx
        # Nếu địch đi ra khỏi màn hình thì xuất hiện lại ở trên, random vị trí x
        if self.rect.top > cao:
            self.rect.y = -20
            self.rect.x = random.randint(20, rong - 20)

            # Reset hướng chéo mới cho đa dạng
            self.dx = random.choice([-2, -1, 1, 2])
