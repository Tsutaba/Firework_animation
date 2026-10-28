#c Модуль отвечает за отрисовку графических объектов на экране.

import pygame
from src.models.animation_model import FireworkManager

class Renderer:
    # Отрисовщик анимации системы фейерверков.

    def __init__(self, screen: pygame.Surface):
        # Связывание рендерера с окном pygame.
        self.screen = screen

    def render(self, manager: FireworkManager):
        # Отрисовка фона, летящих ракет и прозрачных частиц.
        # Очистка экрана черным цветом (ночное небо)
        self.screen.fill((10, 10, 20))

        # Отрисовка ракет (небольшие светящиеся точки)
        for rocket in manager.rockets:
            pygame.draw.circle(self.screen, rocket.color, (int(rocket.x), int(rocket.y)), 4)

        # Отрисовка частиц с поддержкой альфа-канала прозрачности
        for p in manager.particles:
            # Создаем временную поверхность для отрисовки прозрачного круга
            size = 6
            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            
            # Извлекаем RGB и добавляем текущую прозрачность частицы
            rgba_color = (p.color[0], p.color[1], p.color[2], p.alpha)
            
            pygame.draw.circle(surf, rgba_color, (size, size), size)
            self.screen.blit(surf, (int(p.x) - size, int(p.y) - size))