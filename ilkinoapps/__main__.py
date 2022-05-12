from ilkinoapps.ilkino_service import *
from ilkinoapps.ilkino_gui import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-gift")
    args = parser.parse_args()
    gifts = args.gift.split(",")

    service = IlkinoService(gifts)
    service.setup()
    gui = IlkinoGui(service)
    gui.run()
