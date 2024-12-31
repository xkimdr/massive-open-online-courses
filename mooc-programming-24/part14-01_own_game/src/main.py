import math
import pygame
from random import randint


class GameObject:
    def __init__(
        self,
        window_size: tuple[int, int],
        surface: pygame.Surface,
        spawn_randomly: bool = True,
    ) -> None:
        self._surface = surface
        self._size_x = self._surface.get_width()
        self._size_y = self._surface.get_height()
        self._boundary_x = window_size[0] - self._size_x
        self._boundary_y = window_size[1] - self._size_y

        if spawn_randomly:
            self._pos_x = randint(0, self._boundary_x)
            self._pos_y = randint(0, self._boundary_y)
        else:
            self._pos_x = self._boundary_x // 2
            self._pos_y = self._boundary_y // 2

    def move(self, dx: int, dy: int) -> None:
        self._pos_x = max(0, min(self._pos_x + dx, self._boundary_x))
        self._pos_y = max(0, min(self._pos_y + dy, self._boundary_y))

    def is_colliding_with(self, other: "GameObject") -> bool:
        return (
            self._pos_x < other._pos_x + other._size_x
            and self._pos_x + self._size_x > other._pos_x
            and self._pos_y < other._pos_y + other._size_y
            and self._pos_y + self._size_y > other._pos_y
        )

    def pos(self) -> tuple[int, int]:
        return (self._pos_x, self._pos_y)

    def surface(self) -> pygame.Surface:
        return self._surface


class Player(GameObject):
    def __init__(self, window_size: tuple[int, int]) -> None:
        surface = pygame.image.load("robot.png")
        super().__init__(window_size, surface, False)

        self._speed = 5
        self._score = 0
        self._health = 100

    def update(self, keys: pygame.key.ScancodeWrapper) -> None:
        if keys[pygame.K_LEFT]:
            self.move(-self._speed, 0)
        if keys[pygame.K_RIGHT]:
            self.move(self._speed, 0)
        if keys[pygame.K_UP]:
            self.move(0, -self._speed)
        if keys[pygame.K_DOWN]:
            self.move(0, self._speed)

    def take_damage(self, amount: int) -> None:
        self._health = max(0, self._health - amount)

    def add_score(self, amount: int) -> None:
        self._score += amount

    def score(self) -> int:
        return self._score

    def health(self) -> int:
        return self._health


class Enemy(GameObject):
    def __init__(self, window_size: tuple[int, int]) -> None:
        surface = pygame.image.load("monster.png")
        super().__init__(window_size, surface)

        self.speed = 3

    def update(self, player_pos: tuple[int, int]) -> None:
        delta_x = player_pos[0] - self._pos_x
        delta_y = player_pos[1] - self._pos_y

        angle = math.atan2(delta_y, delta_x)

        dx = int(self.speed * math.cos(angle))
        dy = int(self.speed * math.sin(angle))

        self.move(dx, dy)


class Coin(GameObject):
    def __init__(self, window_size: tuple[int, int]) -> None:
        surface = pygame.image.load("coin.png")
        super().__init__(window_size, surface)


class Game:
    def __init__(self) -> None:
        pygame.init()

        self._size_x = 800
        self._size_y = 600
        self._window = pygame.display.set_mode((self._size_x, self._size_y))

        self._caption = "Coin Rush"
        pygame.display.set_caption(self._caption)

        self._font = pygame.font.SysFont("Arial", 24)
        self._clock = pygame.time.Clock()

        self._colors = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
        }

        self._help()
        self._reload()
        self._run()

    def _message(self, message: str, color: str, center: tuple[int, int]) -> None:
        surface = self._font.render(message, True, self._colors[color])
        rect = surface.get_rect(center=center)
        self._window.blit(surface, rect)

    def _help(self) -> None:
        self._window.fill(self._colors["white"])

        lines = [
            "Use the arrow keys to move the robot.",
            "Collect all the coins to win the game.",
            "Avoid the monster to stay safe!",
        ]

        y_offset = 150
        for line in lines:
            self._message(line, "black", (self._size_x // 2, y_offset))
            y_offset += 40

        line = "Press Enter to start the game."
        self._message(line, "blue", (self._size_x // 2, y_offset + 40))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                break

    def _reload(self) -> None:
        size = (self._size_x, self._size_y)
        self._player = Player(size)
        self._enemy = Enemy(size)
        self._coins = [Coin(size) for _ in range(20)]

        self._game_over = False
        self._game_won = False

    def _update(self, keys: pygame.key.ScancodeWrapper) -> None:
        self._player.update(keys)
        self._enemy.update(self._player.pos())

        if self._player.is_colliding_with(self._enemy):
            self._player.take_damage(10)

        self._coins = [
            coin
            for coin in self._coins
            if not self._player.is_colliding_with(coin) or self._player.add_score(10)
        ]

        if len(self._coins) == 0:
            self._game_won = True

    def _draw(self) -> None:
        self._window.fill(self._colors["white"])

        self._window.blit(self._player.surface(), self._player.pos())
        self._window.blit(self._enemy.surface(), self._enemy.pos())

        for coin in self._coins:
            self._window.blit(coin.surface(), coin.pos())

        line = f"Score: {self._player.score()}"
        self._message(line, "black", (80, 40))

        line = f"Health: {self._player.health()}"
        self._message(line, "blue", (self._size_x - 100, 40))

    def _watch(self, keys: pygame.key.ScancodeWrapper) -> None:
        center = (self._size_x // 2, self._size_y // 2)

        if self._player.health() == 0:
            self._game_over = True
            line = "Game Over! Press Q to quit or R to restart."
            self._message(line, "red", center)

        if self._game_won:
            line = "You Win! Press Q to quit or R to restart."
            self._message(line, "green", center)

        if self._game_over or self._game_won:
            if keys[pygame.K_q]:
                exit()
            if keys[pygame.K_r]:
                self._reload()

    def _run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()

            if not self._game_over and not self._game_won:
                self._update(keys)

            self._draw()
            self._watch(keys)

            pygame.display.flip()
            self._clock.tick(60)


if __name__ == "__main__":
    Game()
