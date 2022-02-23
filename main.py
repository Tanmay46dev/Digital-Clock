import pygame
from utils import *

pygame.init()

def main():
    # Window attributes
    WIDTH, HEIGHT = 700, 400
    # Creating a window
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Digital clock!")

    # pygame.Surface object with the current date grabbed from utils.py's get_current_date function
    current_date_surface = get_font(40).render(get_current_date(), True, "white")

    # Keeps track of whether or not the clock format is 12 hour
    twelve_hour_clock = False

    # Keeps track of the current clock format
    current_clock_format = "24"

    instruction_surface = get_font(27).render("Press 'SPACE' to toggle between twenty-four and twelve hour clock format!", True, "white")

    # Main loop
    running = True
    while running:
        WIN.fill("#212121")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    twelve_hour_clock = not twelve_hour_clock

        # Drawing

        current_time_surface = get_font(WIDTH-(WIDTH-100)).render(get_current_time(twelve_hour_clock), True, "white")
        WIN.blit(current_time_surface, current_time_surface.get_rect(center=(WIDTH/2, 100)))
        WIN.blit(current_date_surface, current_date_surface.get_rect(center=(WIDTH/2, 180)))
        
        WIN.blit(instruction_surface, instruction_surface.get_rect(center=(WIDTH/2, HEIGHT-100)))


        # Draw the current clock format
        if twelve_hour_clock:
            current_clock_format = "12"
        else:
            current_clock_format = "24"
        
        current_clock_format_surface = get_font(30).render(f"Current clock format: {current_clock_format} hour", True, "white")
        WIN.blit(current_clock_format_surface, current_clock_format_surface.get_rect(center=(WIDTH/2, HEIGHT-50)))

        # Updating the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
