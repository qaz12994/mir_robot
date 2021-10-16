import pygame

pygame.init()
pygame.joystick.init()

last = pygame.joystick.get_count() - 1
joystick = pygame.joystick.Joystick(last)
joystick.init()
print(joystick.get_name())
clock = pygame.time.Clock()
while True:
    pygame.event.get()
    clock.tick(20)
    for i in range(9):
        v = joystick.get_button(i)
        if v:
            print(i, joystick.get_button(i))
