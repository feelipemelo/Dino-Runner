import pygame

#CLOUD
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, X_POS_BG, Y_POS_BG, GAME_SPEED, DEFAULT_TYPE, CLOUD, X_POS_CLOUD, Y_POS_CLOUD, GAME_OVER, SOL
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.dinosaur import Dinosaur 
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
#Shield
from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = GAME_SPEED

        self.x_pos_bg = X_POS_BG
        self.y_pos_bg = Y_POS_BG
        self.x_pos_cloud = X_POS_CLOUD
        self.y_pos_cloud = Y_POS_CLOUD

        self.sound = False
        

        self.death_count = 0
        self.score = 0
        self.player = Dinosaur()

        self.obstacle_manager = ObstacleManager()

        self.power_up_manager = PowerUpManager()

    #score
    def execute(self):
        self.running = True
        self.music()
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()
           

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        #Shield
        self.power_up_manager.reset_power_ups()
        

        self.game_speed = GAME_SPEED
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()      

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False 
                
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        #Shield
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def music(self):
        self.sound = True
        self.mix = pygame.mixer.get_init()
        if self.mix and self.sound:
            pygame.mixer.music.load('dino_runner/assets/Fundo.mp3')
            pygame.mixer.music.play(-1)
        
   
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        #CLOUD
        self.draw_cloud()
        self.draw_sol(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        #Shield
        self.draw_power_upper_time()
        self.power_up_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    #CLOUD
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud + 40))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000
        self.x_pos_cloud -= self.game_speed

    def draw_sol(self, screen):
        self.screen.blit(SOL, (30, 50))

    #Shield
    def draw_power_upper_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000) #, 2)
            print(time_to_show)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen, 
                    font_size = 18,
                    pos_x_center = 300,
                    pos_y_center = 80
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE 


    def draw_score(self):
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            font_size = 25,
            pos_x_center=1000,
            pos_y_center=50
        )

    #score
    def handle_events_on_menu(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run() 
    #score            
    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component("Press any key to start", self.screen)
        else:
            draw_message_component("Press any key to restart", self.screen, pos_y_center=half_screen_height + 140)
            draw_message_component(
                f"Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )          
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 70, half_screen_height - 40))
            self.screen.blit(GAME_OVER, (half_screen_width - 180, half_screen_height - 280))
        
        pygame.display.update()  # .flip()

        self.handle_events_on_menu()

        if self.death_count >= 1:
            draw_message_component(
                f"Last Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )


    
