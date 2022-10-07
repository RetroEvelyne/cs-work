import pygame


class Background:
    def __init__(self):
        self.bgimage = pygame.image.load("background.png")
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 0.075

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.height:
            self.bgX1 = self.rectBGimg.height
        if self.bgX2 <= -self.rectBGimg.height:
            self.bgX2 = self.rectBGimg.height

    def render(self, screen):
        screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        screen.blit(self.bgimage, (self.bgX2, self.bgY2))


class Bird:
    pass


class Knife:
    pass


class Player:
    def __init__(self, sprite: pygame.sprite, crouched: pygame.sprite, background: pygame.sprite,
                x: int = None, y: int = None) -> None:
        self.crouched = crouched
        self.sprite = sprite
        self.x = x or 224
        self.y = y or 0
        self.background = background

    def draw(self, screen):
        Background.update(self.background)
        Background.render(self.background, screen)
        screen.blit(self.sprite, (self.x, self.y))
        pygame.display.flip()

    def move(self, screen, direction):
        match direction:
            case "left":
                self.x -= 0.4
                self.draw(screen)
            case "right":
                self.x += 0.2
                self.draw(screen)

        self.x = max(0, min(self.x, 448))

    def jump(self, screen):
        temp = 0.2
        for i in range(4000):
            self.y -= temp
            self.draw(screen)
            temp -= 0.0001

    def crouch(self, screen):
        Background.update(self.background)
        Background.render(self.background, screen)
        screen.blit(self.crouched, (self.x, self.y))
        pygame.display.flip()


def game(screen, player1, background, move, jump, direction, crouch):
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
                            crouch = True
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
                            crouch = False
        background.update()
        background.render(screen)
        if not crouch:
            player1.draw(screen)

        if player1.y < 448:
            player1.y += 1

        if jump:
            player1.jump(screen)
        elif move:
            player1.move(screen, direction)
        elif crouch:
            player1.crouch(screen)


def main():
    move, jump, crouch = False, False, False
    direction = "left"
    pygame.init()

    # Load the character's sprite
    character_sprite = pygame.image.load("character.png")
    crouched = pygame.image.load("crouched.png")

    # Load the logo into the window
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    # Set the title of the window
    pygame.display.set_caption("Jumpymongus")

    # Window dimensions
    screen = pygame.display.set_mode((512, 512))

    background = Background()
    player1 = Player(character_sprite, crouched, background)
    print("setup")
    game(screen, player1, background, move, jump, direction, crouch)


if __name__ == "__main__":
    main()
