import pygame


# TODO fix knife movement


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
    def __init__(self, knifesprite: pygame.sprite, player1, kx: int = None, ky: int = None):
        self.sprite = knifesprite
        self.player = player1
        self.x = kx or 512
        self.y = ky or 450
        self.difficulty = 0.1

    def move(self):
        self.x -= self.difficulty
        self.difficulty *= 1.00000001


class Player:
    def __init__(self, sprite: pygame.sprite, crouched: pygame.sprite, background: pygame.sprite,
                 x: int = None, y: int = None) -> None:
        self.crouched = crouched
        self.iscrouched = False
        self.sprite = sprite
        self.x = x or 224
        self.y = y or 0
        self.background = background

    def draw(self, screen, background, knife1):
        background.update()
        background.render(screen)
        if self.iscrouched:
            screen.blit(self.crouched, (self.x, self.y))
        else:
            screen.blit(self.sprite, (self.x, self.y))
        screen.blit(knife1.sprite, (knife1.x, knife1.y))
        pygame.display.flip()

    def move(self, screen, direction, background, knife1):
        match direction:
            case "left":
                self.x -= 0.4
                self.draw(screen, background, knife1)
            case "right":
                self.x += 0.2
                self.draw(screen, background, knife1)

        if self.x.__round__(2) == (knife1.x.__round__(2) - 64):
            endgame()

        self.x = max(0, min(self.x, 448))

    def jump(self, screen, background, knife1):
        temp = 0.2
        for i in range(2000):
            self.y -= temp
            knife1.move()
            self.draw(screen, background, knife1)
            temp -= 0.0002

    def crouch(self, screen, background):
        self.iscrouched = True
        Background.update(self.background)
        Background.render(self.background, screen)
        screen.blit(self.crouched, (self.x, self.y))
        pygame.display.flip()


def game(screen, player1, background, move, jump, direction, crouch, knife_sprite, knife1):
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
            player1.draw(screen, background, knife1)

        if player1.y < 448:
            player1.y += 1

        if jump:
            player1.jump(screen, background, knife1)
        elif move:
            player1.move(screen, direction, background, knife1)
        elif crouch:
            player1.crouch(screen, background)

        if knife1.x < 0:
            knife1 = Knife(knife_sprite, player1)
        knife1.move()

        if player1.x.__round__(2) == (knife1.x.__round__(2) - 64):
            endgame()


def endgame():
    print("YOU LOSE")
    main()


def main():
    move, jump, crouch = False, False, False
    enemies = []
    direction = "left"
    pygame.init()

    # Load the character's sprite
    character_sprite = pygame.image.load("character.png")
    crouched = pygame.image.load("crouched.png")

    # Load the enemy sprites
    knife_sprite = pygame.image.load("knife.png")

    # Load the logo into the window
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    # Set the title of the window
    pygame.display.set_caption("Jumpymongus")

    # Window dimensions
    screen = pygame.display.set_mode((512, 512))

    background = Background()
    player1 = Player(character_sprite, crouched, background)
    knife1 = Knife(knife_sprite, player1)
    print("setup")
    game(screen, player1, background, move, jump, direction, crouch, knife_sprite, knife1)


if __name__ == "__main__":
    main()
