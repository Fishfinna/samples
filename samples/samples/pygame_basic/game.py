# Shanti Stein-Gagnon
# A01229344, Set B
import pygame
import pygame.locals
import random


class Rabbit(pygame.sprite.Sprite):
    """This is the main player Class"""

    def __init__(self):
        super().__init__()
        image = pygame.image.load("rabbit.png")
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        # Starting position = top of the screen
        self.rect.x = 250
        self.rect.y = 250

    def update(self, fox):

        if self.rect.x < fox.rect.x and self.rect.x - 15 > 0:
            self.rect.x = self.rect.x - 10

        elif self.rect.x > fox.rect.x and self.rect.x + 55 < 500:
            self.rect.x = self.rect.x + 10

        if self.rect.y < fox.rect.y and self.rect.y - 15 > 0:
            self.rect.y = self.rect.y - 10

        elif self.rect.y > fox.rect.y and self.rect.y + 55 < 500:
            self.rect.y = self.rect.y + 10


class Fox(pygame.sprite.Sprite):
    """This is the main player Class"""

    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("fox.png")
        self.grow_factor = 1
        self.image = pygame.transform.scale(self.original_image, (100, 95))
        self.rect = self.image.get_rect()

        # start in the center of the screen
        self.rect.x = 100
        self.rect.y = 100


def main():
    """Main function to play the fox kill game"""
    pygame.init()

    # Screen is 500x500 pixels
    window = pygame.display.set_mode((500, 500))
    window.set_colorkey((255, 255, 255))
    clock = pygame.time.Clock()

    # New fox
    fox = Fox()

    # create the meat
    rabbits = pygame.sprite.Group()
    rabbit = Rabbit()
    rabbits.add(rabbit)

    running = True
    while running:

        # Paint the screen white
        window.fill((100, 130, 25))

        # Create a new Clock object
        clock.tick(30)

        rabbit.update(fox)

        if pygame.sprite.spritecollide(fox, rabbits, dokill=False):
            rabbit.rect.x = random.choice(range(20, 450))
            rabbit.rect.y = random.choice(range(20, 450))

        # Event loop - quit if closed or 'escape' is pressed
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            elif event.type == pygame.locals.KEYDOWN:
                if event.key in (pygame.locals.K_ESCAPE, pygame.locals.K_q):
                    running = False

        # Get the keys outside of the event loop (!)
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT]:
            # Move the player right by 20 pixels
            # We have to make sure it does not go "off" the screen
            fox.rect.x = min(fox.rect.x + 20, 410)
        elif keys[pygame.locals.K_LEFT]:
            # Move the player left by 20 pixels
            fox.rect.x = max(fox.rect.x - 20, 0)

        elif keys[pygame.locals.K_UP]:
            fox.rect.y = max(fox.rect.y - 20, 0)

        elif keys[pygame.locals.K_DOWN]:
            fox.rect.y = min(fox.rect.y + 20, 410)

        # Update the player image
        window.blit(fox.image, fox.rect)
        window.blit(rabbit.image, rabbit.rect)

        # Update the screen
        pygame.display.update()


if __name__ == "__main__":
    main()
