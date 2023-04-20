from dino_runner.utils.constants import BIRD, Y_POS_BIRD
from dino_runner.components.obstacles.obtstacle import Obstacle


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = Y_POS_BIRD
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], (self.rect.x, self.rect.y))
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0
