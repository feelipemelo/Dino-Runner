import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MP3_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
X_POS_BG = 0 
Y_POS_BG = 380
GAME_SPEED = 20

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340

Y_POS_BIRD = 220

X_POS_CLOUD = 0
Y_POS_CLOUD = 40

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino.png"))

DINO_RUN_2 = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run_3.png")),
]

DINO_JUMP = pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Jump.png"))

DINO_DUCK = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Duck_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Duck_4.png")),
]

DINO_RUN_2_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run_Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run_2_Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Run_3_Shield.png")),
]

DINO_JUMP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Jump_Shield.png"))

DINO_DUCK_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Duck_2_Shield.png")), 
    pygame.image.load(os.path.join(IMG_DIR, "Dino_2/Dino_Duck_4_Shield.png")),
]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/SmallCactus11.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/SmallCactus22.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/SmallCactus33.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/LargeCactus11.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/LargeCactus22.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Cactus_Copia/LargeCactus33.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_4.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud_Copia.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track - Copia.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

SOL = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sol.png'))


JUMP_VEL = 8.5

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
