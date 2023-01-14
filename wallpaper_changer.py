import ctypes
import os

IMG_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "infectedWallpaper.jpg",
    )
)

ctypes.windll.user32.SystemParametersInfoW(20, 0, IMG_PATH, 0)
