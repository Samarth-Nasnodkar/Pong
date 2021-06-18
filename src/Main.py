import pygame
from libs.vectors import Vector2
from random import randint


class Game:
    def __init__(self):
        # Initialisations
        pygame.init()
        pygame.display.set_caption("Pong")
        # Loading Sprites
        self.ball = pygame.image.load("../sprites/Ball.png")
        self.paddle = pygame.image.load("../sprites/Paddle.png")
        # Resizing sprites
        self.ball = pygame.transform.scale(self.ball, (15, 15))
        self.paddle = pygame.transform.scale(self.paddle, (7, 80))
        # Declaring constants
        self.width = 720
        self.height = 720
        self.ballVelocity = Vector2(randint(-10, 10), randint(-10, 10))
        self.playerPosition = Vector2(self.width - 7, int(self.height / 2))
        self.aiPosition = Vector2(0, int(self.height / 2))
        self.playerVelocity = Vector2(0, int(self.height / 40))
        self.ballPosition = Vector2(int(self.width / 2), int(self.height / 2))
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.ball, self.ballPosition.toTuple)
        self.screen.blit(self.paddle, self.playerPosition.toTuple)
        self.screen.blit(self.paddle, self.aiPosition.toTuple)
        pygame.display.update()
        # Declaring variables
        self.isRunning = True
        # End of Declarations
        self.eventLoop()

    def moveAI(self):
        if self.ballVelocity.x >= 0:
            return

        if self.ballPosition.x >= self.height * 0.75:
            return

        pitchLength = int(self.ballVelocity.y * self.ballPosition.x / self.ballVelocity.x)
        finalCoord = self.aiPosition.y
        if self.ballVelocity.y >= 0:
            finalCoord = self.ballPosition.y + pitchLength
        else:
            finalCoord = self.ballPosition.y - pitchLength

        if finalCoord < 0:
            finalCoord = -1 * finalCoord
        elif finalCoord > self.height:
            while finalCoord > self.height:
                finalCoord = finalCoord - self.height

        if self.aiPosition.y < finalCoord < self.aiPosition.y + 80:
            return

        if self.aiPosition.y + 40 < finalCoord:
            self.aiPosition += self.playerVelocity * 2
        elif self.aiPosition.y > finalCoord:
            self.aiPosition -= self.playerVelocity * 2

        if self.aiPosition.y <= 0:
            self.aiPosition.y = 0
        elif self.aiPosition.y + 80 >= self.height:
            self.aiPosition.y = self.height - 80

    def drawCrease(self):
        rects = 20
        W, H = 4, int((self.height / rects) - 10)
        startW, startH = int(self.width / 2) - int(W/2), 0
        rectColor = (255, 255, 255)
        for i in range(rects):
            pygame.draw.rect(self.screen, rectColor, (startW, startH, W, H))
            startH += H + 10

    def eventLoop(self):
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.isRunning = False
            key = pygame.key.get_pressed()
            if key[pygame.K_w] or key[pygame.K_UP]:
                self.playerPosition -= self.playerVelocity
                if self.playerPosition.y <= 0:
                    self.playerPosition.y = 0
            elif key[pygame.K_s] or key[pygame.K_DOWN]:
                self.playerPosition += self.playerVelocity
                if self.playerPosition.y + 80 >= self.height:
                    self.playerPosition.y = self.height - 80

            self.ballPosition += self.ballVelocity
            if self.ballPosition.x + 15 >= self.width:
                self.ballPosition.x = self.width - 15
                self.ballVelocity.x *= -1
            # if self.ballPosition.x <= 0:
            #     self.ballPosition.x = 0
            #     self.ballVelocity.x *= -1
            if self.ballPosition.y + 15 >= self.height:
                self.ballPosition.y = self.height - 15
                self.ballVelocity.y *= -1
            if self.ballPosition.y <= 0:
                self.ballPosition.y = 0
                self.ballVelocity.y *= -1
            if self.width - 7 <= self.ballPosition.x + 7.5 <= self.width and self.playerPosition.y <= self.ballPosition.y + 7.5 <= self.playerPosition.y + 80:
                self.ballVelocity.x *= -1
            if self.ballPosition.x <= 7 and self.aiPosition.y <= self.ballPosition.y + 7.5 <= self.aiPosition.y + 80:
                self.ballPosition.x = 7
                self.ballVelocity.x *= -1
            self.screen.fill((0, 0, 0))
            self.drawCrease()
            self.screen.blit(self.ball, self.ballPosition.toTuple)
            self.screen.blit(self.paddle, self.playerPosition.toTuple)
            self.moveAI()
            self.screen.blit(self.paddle, self.aiPosition.toTuple)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    session = Game()
