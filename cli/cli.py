from pathlib import Path
import os
import sys
import time

import yaml


def find_presets() -> dict[int, str]:
    with Path("../cli/config.yaml").open("r") as file:
        presets = {}

        config = yaml.safe_load(file)

        for i, favourite in enumerate(config["favourites"]):
            presets[i + 1] = favourite

        presets[0] = "status"

    return presets


def read_target(presets: dict[int, str]) -> str:
    preset = input()
    return preset if not preset.isdigit() else presets[int(preset)]


def trigger_desk(targete: str) -> None:
    if target != "status":
        print(f"\nSwitching to {target} position")

        os.system(f"idasen-controller --forward --move-to {target}")

    else:
        os.system(f"idasen-controller --forward")


if __name__ == "__main__":
    print("\nControl your Idasen Desk!")
    print("\nWait a few seconds to let the desk connect.")
    time.sleep(6)

    presets = find_presets()

    try:
        while True:
            print("\nWhat now?")
            for preset in presets:
                print(f"- ({preset}) {presets[preset]}")

            target = read_target(presets)
            trigger_desk(target)

    except KeyboardInterrupt:
        sys.exit(0)
