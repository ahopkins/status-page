from os import environ

from lib.monitor import get_monitors, run_monitors


def run():
    monitors = get_monitors()
    run_monitors(monitors)


if __name__ == "__main__":
    run()
