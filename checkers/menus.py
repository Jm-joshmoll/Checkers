import pygame
import sys
from checkers.button import Button
from checkers.constants import white, black

# TODO: comment code

class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.title_font = pygame.font.Font(None, 72)
        self.menu_buttons = [
            Button("Player vs. Player", (self.width // 2 - 100, self.height // 2 - 100)),
            Button("Play Against AI", (self.width // 2 - 100, self.height // 2 - 50)),
            Button("AI vs. AI", (self.width // 2 - 100, self.height // 2)),
            Button("Settings", (self.width // 2 - 100, self.height // 2 + 50)),
            Button("Quit", (self.width // 2 - 100, self.height // 2 + 100))
        ]
        self.current_screen = "menu"

    def handle_events(self, mouse_pos, mouse_buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.current_screen == "menu":
            for button in self.menu_buttons:
                if button.is_clicked(mouse_pos) and mouse_buttons[0]:
                    if button.text == "Settings":
                        self.current_screen = "settings"
                        return self.current_screen
                    elif button.text == "Quit":
                        print("Exiting...")
                        pygame.quit()
                        sys.exit()
                    elif button.text == "Player vs. Player":
                        print("Starting game against player...")
                        return "pvp"
                    elif button.text == "Play Against AI":
                        print("Starting game against AI...")
                        return "pva"
                    elif button.text == "AI vs. AI":
                        print("Starting game AI vs. AI...")
                        return "ava"

        return None

    def draw(self, surface):
        surface.fill(black)
        title_surface = self.title_font.render("Checkers Game", True, white)
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 4))
        surface.blit(title_surface, title_rect)

        for button in self.menu_buttons:
            button.draw(surface)

class SettingsMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.title_font = pygame.font.Font(None, 72)
        self.settings_buttons = [
            Button("Sound: On", (self.width // 2 - 100, self.height // 2 - 100)),
            Button("Music: On", (self.width // 2 - 100, self.height // 2 - 50)),
            Button("Back to Menu", (self.width // 2 - 100, self.height // 2 + 100))
        ]
        self.current_screen = "settings"

    def handle_events(self, mouse_pos, mouse_buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for button in self.settings_buttons:
            if button.is_clicked(mouse_pos) and mouse_buttons[0]:
                if button.text == "Sound: On":
                    button.text = "Sound: Off"
                elif button.text == "Music: On":
                    button.text = "Music: Off"
                elif button.text == "Sound: Off":
                    button.text = "Sound: On"
                elif button.text == "Music: Off":
                    button.text = "Music: On"
                elif button.text == "Back to Menu":
                    self.current_screen = "menu"
                    # Switch back to main menu
                    return self.current_screen

        return None

    def draw(self, surface):
        surface.fill((0, 0, 0))
        title_surface = self.title_font.render("Settings", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 4))
        surface.blit(title_surface, title_rect)

        for button in self.settings_buttons:
            button.draw(surface)
