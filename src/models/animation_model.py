# Модуль содержит математические и физические модели фейерверков.

import random
import math
import pygame

class Particle:
    # Класс, описывающий отдельную искру (частицу) фейерверка.

    def __init__(self, x: float, y: float, color: tuple, gravity: float):
        # Инициализация физических параметров частицы.
        self.x = x
        self.y = y
        self.color = color
        self.gravity = gravity
        
        # Перевод полярных координат в декартовы для взрыва во все стороны
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        self.lifetime = random.randint(40, 70)  # Ограниченное время жизни
        self.alpha = 255  # Прозрачность

    def update(self):
        # Обновление координат частицы под действием скоростей и гравитации.
        self.x += self.vx
        self.vy += self.gravity  # Эффект гравитации падения вниз
        self.y += self.vy
        self.lifetime -= 1
        
        # Плавное угасание альфа-канала (прозрачности)
        if self.lifetime > 0:
            self.alpha = max(0, int((self.lifetime / 70) * 255))

class FireworkRocket:
    # Класс ракеты, которая летит вверх перед взрывом.

    def __init__(self, start_x: float, target_y: float):
        # Инициализация стартовой позиции и цели взрыва.
        self.x = start_x
        self.y = 600  # Снизу экрана
        self.target_y = target_y
        self.vy = random.uniform(-12, -8)  # Скорость полета вверх
        self.exploded = False
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

    def update(self):
        # Движение ракеты вверх.
        self.y += self.vy
        if self.vy < 0:
            self.vy += 0.05  # Небольшое замедление при подлете к пику
        if self.y <= self.target_y or self.vy >= 0:
            self.exploded = True

class FireworkManager:
    # Класс управления всеми ракетами и частицами на экране.

    def __init__(self):
        # Создание контейнеров для объектов.
        self.rockets = []
        self.particles = []
        self.gravity = 0.15  # Значение гравитации по умолчанию

    def launch_rocket(self):
        # Случайная генерация параметров нового фейерверка.
        start_x = random.randint(100, 700)
        target_y = random.randint(100, 350)
        self.rockets.append(FireworkRocket(start_x, target_y))

    def update(self):
        # Сквозное обновление состояний всех объектов.
        # Автоматический запуск новых фейерверков с некоторой вероятностью
        if random.random() < 0.03 and len(self.rockets) < 5:
            self.launch_rocket()

        # Обновление ракет
        for rocket in self.rockets[:]:
            rocket.update()
            if rocket.exploded:
                # Спавн частиц при взрыве
                num_particles = random.randint(60, 100)
                for _ in range(num_particles):
                    self.particles.append(Particle(rocket.x, rocket.y, rocket.color, self.gravity))
                self.rockets.remove(rocket)

        # Обновление частиц
        for particle in self.particles[:]:
            particle.update()
            if particle.lifetime <= 0 or particle.alpha <= 0:
                self.particles.remove(particle)