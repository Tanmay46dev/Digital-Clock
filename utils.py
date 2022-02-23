from datetime import datetime
import pygame
pygame.font.init()

def get_font(size: int, name=None) -> pygame.font.Font:
    return pygame.font.SysFont(name, size)

def get_current_time(twelve_hour=False) -> str:
    hour = datetime.now().strftime("%H")

    if twelve_hour:
        hour = datetime.now().strftime("%I")

    return f"{hour} : {datetime.now().strftime('%M')} : {datetime.now().strftime('%S')}"

def get_current_date() -> str:
    return datetime.today().strftime("%B %d, %Y")
