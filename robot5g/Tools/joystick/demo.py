import pygame

pygame.init()

white = (240, 240, 240)
background = (43, 43, 43)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CONTROL')

pygame.display.update()
gameExit = False

lead_x = 400
lead_y = 300

joysticks = list()
clock = pygame.time.Clock();

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Dectected joystick '", joysticks[-1].get_name(), "'")

joystick = joysticks[0]

while not gameExit:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 3:
            lead_y -= 10
        if event.button == 1 or event.button == 5:
            lead_x += 10
        if event.button == 0:
            lead_y += 10
        if event.button == 2 or event.button == 4:
            lead_x -= 10
        if event.button == 7:
            gameExit = True

    LeftAxisX = joystick.get_axis(0)
    LeftAxisY = joystick.get_axis(1)
    trigger = joystick.get_axis(2)
    RightAxisY = joystick.get_axis(3)
    RightAxisX = joystick.get_axis(4)
    if (RightAxisY < -0.5) or (LeftAxisY < -0.5) or (trigger < -0.5):
        lead_y -= 10
    if (RightAxisX > 0.5) or (LeftAxisX > 0.5):
        lead_x += 10
    if (RightAxisY > 0.5) or (LeftAxisY > 0.5) or (trigger > 0.5):
        lead_y += 10
    if (RightAxisX < -0.5) or (LeftAxisX < -0.5):
        lead_x -= 10
    hat = joystick.get_hat(0)
    dx, dy = hat
    lead_x += -10 * dx
    lead_y += -10 * dy

    gameDisplay.fill(background)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, 60, 60])

    pygame.display.update()
pygame.quit()

quit()
