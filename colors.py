# ANSI escape codes for Atari 800XL-like colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY = "\033[90m"

RESET = '\033[0m'
# Background colors
BG_BLACK = '\033[40m'
BG_BLUE = '\033[44m'

def colorize(text, color, background=BG_BLACK):
    return f"{background}{color}{text}{RESET}"
