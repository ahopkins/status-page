import sys
from os import environ

from lib.calculate import run_calculations
from lib.data import fetch_data
from lib.sync import run_sync


def run():
    # environ["GITHUB_WORKSPACE"] = "/home/packetfabric/Skunk/Status/prototype/skunk/docs"
    # environ["GITHUB_PAT"] = "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"
    # environ["GITHUB_REPOSITORY"] = "ahopkins/status-page"
    for k, v in environ.items():
        print(k, v)
    sys.exit()
    data = fetch_data()
    run_sync(data)
    run_calculations(data)


if __name__ == "__main__":
    run()
