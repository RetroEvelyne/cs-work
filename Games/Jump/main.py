import pygame


# TODO: THINGS TO TELL MADDIE
# probs need a class for the character and the obstacles

def draw_character(x, y, screen, charactersprite):
    screen.fill((0, 0, 0))
    screen.blit(charactersprite, (x, y))
    pygame.display.flip()
    return


def move_character(x, y, screen, charactersprite, direction):
    if direction == "left":
        x -= 0.4
        draw_character(x, y, screen, charactersprite)
    elif direction == "right":
        x += 0.2
        draw_character(x, y, screen, charactersprite)
    if x < 0:
        return 0
    if x > 448:
        return 448
    return x


def jump_character(x, y, screen, charactersprite):
    temp = 0.2
    for i in range(4000):
        y -= temp
        draw_character(x, y, screen, charactersprite)
        temp -= 0.0001
        # print(x, y)


def duckcharacter():
    pass


def game(x, y, screen, character_sprite, move, jump, direction):
    running = True

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            jump = True
                        case pygame.K_LEFT:
                            direction = "left"
                            move = True
                        case pygame.K_RIGHT:
                            direction = "right"
                            move = True
                        case pygame.K_DOWN:
                            duck = True
                            # TODO

                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_UP:
                            jump = False
                        case pygame.K_LEFT:
                            move = False
                        case pygame.K_RIGHT:
                            move = False
                        case pygame.K_DOWN:
                            duck = False
        draw_character(x, y, screen, character_sprite)
        if jump:
            jump_character(x, y, screen, character_sprite)
        if move:
            x = move_character(x, y, screen, character_sprite, direction)
        if y < 448:
            y += 1
        # print(x, y)


def main():
    x, y = 224, 0
    move, jump = False, False
    direction = "left"
    pygame.init()
    logo = pygame.image.load("logo.png")
    charactersprite = pygame.image.load("character.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Jumpymongus")

    screen = pygame.display.set_mode((512, 512))

    game(x, y, screen, charactersprite, move, jump, direction)


if __name__ == "__main__":
    main()
