from colorama import init, Fore, Style

init(autoreset=True)

BOLD = Style.BRIGHT
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
RESET = Style.RESET_ALL


def info(msg):
    print(f"{BOLD}{G}{msg}{RESET}")


def info_inline(msg):
    # Print message in-place on the same terminal line, clearing the line first
    # Uses carriage return + ANSI escape to clear the line then prints without newline
    print(f"\r\033[K{BOLD}{G}{msg}{RESET}", end="", flush=True)


def warn(msg):
    print(f"{BOLD}{Y}{msg}{RESET}")


def error(msg):
    print(f"{BOLD}{R}{msg}{RESET}")


def stopped():
    print(f"{BOLD}{R}Script Stopped By User{RESET}")
