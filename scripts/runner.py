from lib.calculate import run_calculations
from lib.data import fetch_data
from lib.sync import run_sync


def run():
    data = fetch_data()
    run_sync(data)
    run_calculations(data)


if __name__ == "__main__":
    run()
