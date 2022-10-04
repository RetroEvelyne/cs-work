import pygame


def drawcharacter(x, y, screen, charactersprite):
    screen.fill((0, 0, 0))
    screen.blit(charactersprite, (x, y))
    pygame.display.flip()
    return


def move(x, y, screen, charactersprite, direction):
    if direction == "left":
        x += 1
        drawcharacter(x, y, screen, charactersprite)
    elif direction == "right":
        x -= 1
        drawcharacter(x, y, screen, charactersprite)


def jump(x, y, screen, charactersprite):
    temp = 0.2
    for i in range(4000):
        y -= temp
        drawcharacter(x, y, screen, charactersprite)
        temp -= 0.0001


def main():
    x, y = 224, 0
    pygame.init()
    logo = pygame.image.load("logo.png")
    charactersprite = pygame.image.load("character.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Jumpymongus")

    screen = pygame.display.set_mode((512, 512))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jump(x, y, screen, charactersprite)
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    move = True
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    move = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
        drawcharacter(x, y, screen, charactersprite)
        if y < 448:
            y += 1


if __name__ == "__main__":
    main()
