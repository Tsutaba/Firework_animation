# Модуль отрисовки простых текстовых контроллеров и HUD.

import pygame

class HUD:
    # Класс отображения текстовой информации и подсказок.

    def __init__(self, screen: pygame.Surface):
        # Инициализация шрифтов.
        pygame.font.init()
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 16)

    def draw_controls(self, gravity_value: float):
        # Вывод текста управления на экран.
        text_gravity = self.font.render(f"Гравитация (Стрелки Вверх/Вниз): {gravity_value:.2f}", True, (200, 200, 200))
        text_click = self.font.render("Клик мыши — запустить фейерверк в точку", True, (150, 150, 150))
        
        self.screen.blit(text_gravity, (20, 20))
        self.screen.blit(text_click, (20, 45))