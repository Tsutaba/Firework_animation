# Главный класс приложения, управляющий жизненным циклом программы.

import pygame
from src.models.animation_model import FireworkManager
from src.renderers/renderer import Renderer
from src.widgets/controls import HUD

class App:
    # Управляющий класс архитектуры приложения.

    def __init__(self):
        # Конфигурация окна и внутренних компонентов.
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_display_mode((self.width, self.height))
        pygame.display.set_caption("Лабораторная 2: Сложная анимация фейерверков")
        
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        # Компоненты ООП структуры
        self.manager = FireworkManager()
        self.renderer = Renderer(self.screen)
        self.hud = HUD(self.screen)

    def handle_events(self):
        # Обработка событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    # Запуск ракеты пользователем в координату клика
                    mx, my = event.pos
                    from src.models.animation_model import FireworkRocket
                    rocket = FireworkRocket(mx, my)
                    self.manager.rockets.append(rocket)
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Увеличение гравитации (частицы падают быстрее)
                    self.manager.gravity = min(1.0, self.manager.gravity + 0.05)
                elif event.key == pygame.K_DOWN:
                    # Уменьшение гравитации (эффект невесомости)
                    self.manager.gravity = max(0.0, self.manager.gravity - 0.05)

    def run(self):
        # Основной игровой цикл.
        while self.is_running:
            self.handle_events()
            self.manager.update()
            self.renderer.render(self.manager)
            self.hud.draw_controls(self.manager.gravity)
            
            pygame.display.flip()
            self.clock.tick(60)  # Фиксация 60 FPS

        pygame.quit()