import time
import random

#### Crypto stuff not important
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size :])).decode("utf-8")

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class PathGroup:
    tiles = []
    current_cordinates = None
    path_history = []

    def __repr__(self):
        return "[X] {} -- {} \n".format(self.tiles, self.path_history)


grid = [
    [
        "SPHINX",
        "urn",
        "vulture",
        "arch",
        "snake",
        "urn",
        "bug",
        "plant",
        "arch",
        "staff",
        "SPHINX",
    ],
    [
        "plant",
        "foot",
        "bug",
        "plant",
        "vulture",
        "foot",
        "staff",
        "vulture",
        "plant",
        "foot",
        "bug",
    ],
    [
        "arch",
        "staff",
        "urn",
        "Shrine",
        "Shrine",
        "Shrine",
        "plant",
        "bug",
        "staff",
        "urn",
        "arch",
    ],
    [
        "snake",
        "vulture",
        "foot",
        "Shrine",
        "Shrine",
        "Shrine",
        "urn",
        "snake",
        "vulture",
        "foot",
        "vulture",
    ],
    [
        "staff",
        "urn",
        "bug",
        "Shrine",
        "Shrine",
        "Shrine",
        "foot",
        "staff",
        "bug",
        "snake",
        "staff",
    ],
    [
        "snake",
        "plant",
        "bug",
        "urn",
        "foot",
        "vulture",
        "bug",
        "urn",
        "arch",
        "foot",
        "urn",
    ],
    [
        "SPHINX",
        "arch",
        "staff",
        "plant",
        "snake",
        "staff",
        "bug",
        "plant",
        "vulture",
        "snake",
        "SPHINX",
    ],
]


def print_grid_with_path_group(grid, pg):
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if (i, j) in pg.path_history:
                if (i, j) == pg.path_history[-1]:
                    print(
                        bcolors.FAIL + str("YOU").ljust(8, " ") + bcolors.ENDC, end=""
                    )
                else:
                    print(str("STEP").ljust(8, " "), end="")
            else:
                print(str(y).ljust(8, " "), end="")
        print()


def try_get_tile(tile_tuple):
    try:
        return grid[tile_tuple[0]][tile_tuple[1]], (tile_tuple[0], tile_tuple[1])
    except Exception as e:
        return None


def print_current_map():
    for x in grid:
        for y in x:
            print(str(y).ljust(8, " "), end="")
        print()


starting_tile = (3, 10)
starting_path = PathGroup()
starting_path.tiles = ["vulture"]
starting_path.current_cordinates = starting_tile
starting_path.path_history = [starting_tile]


def move(path, tile):
    sub_path = PathGroup()
    sub_path.tiles.append(tile)
    sub_path.current_cordinates = tile
    sub_path.path_history = path.path_history.copy()
    sub_path.path_history.append(tile)
    return sub_path


cur_tile = starting_tile


def menu(path):
    cur_tile = path.current_cordinates
    print(cur_tile)
    next_tile = None
    while next_tile == None:
        print(
            bcolors.OKGREEN
            + "\t ------------- The puzzle room layout -------------"
            + bcolors.ENDC
        )
        print_grid_with_path_group(grid, path)
        choice = input("Which direction will you journey next? : ").upper()
        match choice:
            case "N":
                next_tile = (cur_tile[0] -1, cur_tile[1])
            case "S":
                next_tile = (cur_tile[0] +1, cur_tile[1])
            case "E":
                next_tile = (cur_tile[0], cur_tile[1] +1)
            case "W":
                next_tile = (cur_tile[0], cur_tile[1] -1)
            case "NE":
                next_tile = (cur_tile[0] -1, cur_tile[1] +1)
            case "NW":
                next_tile = (cur_tile[0] -1, cur_tile[1] -1)
            case "SE":
                next_tile = (cur_tile[0] +1, cur_tile[1] +1)
            case "SW":
                next_tile = (cur_tile[0] +1, cur_tile[1] -1)
            case _:
                print("That doesn't seem to be a valid direction")
	
    new_path = move(path, next_tile)
    return new_path

def check_path(path):
    print(path)
    for tile in path.path_history:
        if tile[1] > 10 or tile[1] < 0:
            exit(-1)
        if tile[0] > 6 or tile[0] < 0:
            exit(-1)

    if path.current_cordinates == (3, 9):
        exit(-1)

    if try_get_tile(path.current_cordinates)[0] == "SPHINX":
        exit(-1)

    if len(set(path.path_history)) != len(path.path_history):
        exit(-1)

    for tile in path.path_history[:-1]:
        if try_get_tile(path.current_cordinates)[0] == try_get_tile(tile)[0]:
            exit(-1)

    if try_get_tile(path.current_cordinates)[0] != "Shrine" and len(
        set([x[1] for x in path.path_history])
    ) != len([x[1] for x in path.path_history]):
        exit(-1)

    print(try_get_tile(path.current_cordinates)[0])
    if try_get_tile(path.current_cordinates)[0] == "Shrine":
        key = "".join([try_get_tile(x)[0] for x in path.path_history])
        print(key)
        enc_flag = b"FFxxg1OK5sykNlpDI+YF2cqF/tDem3LuWEZRR1bKmfVwzHsOkm+0O4wDxaM8MGFxUsiR7QOv/p904UiSBgyVkhD126VNlNqc8zNjSxgoOgs="
        obj = AESCipher(key)
        dec_flag = obj.decrypt(enc_flag)
        if "pctf" in dec_flag:
            print(bcolors.OKCYAN + dec_flag + bcolors.ENDC)
            exit(0)
        else:
            print('a')
            exit(-1)
cur_path = starting_path
while True:
    n_path = menu(cur_path)
    check_path(n_path)
    cur_path = n_path
