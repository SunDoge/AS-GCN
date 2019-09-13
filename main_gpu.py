import torch
import time
import argparse
from typing import List


def occupy_gpus(devices: List[int]):
    # float takes 4 bytes, we use 1000 instead of 1024 to make it less
    in_features = 10 * 1000 / 4

    x = torch.rand()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
