from Classes.button import Buttons

COLORS = [
    (0, 0, 0),
    (195, 102, 255),
    (92, 255, 255),
    (255, 114, 78),
    (156, 255, 57),
    (255, 90, 71),
    (255, 75, 184),
]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GAME_OVER_COLOR = (255, 125, 0)
PRESS_ESC_COLOR = (255, 215, 0)

SIZE_SCREEN = (400, 500)

LIMIT = 100000
COUNTER = 0

FPS = 25

FONT_NAME = 'Calibri'
SIZE_SCORE = 25
SIZE_OVER_ESC = 65

RIGHT = 1
LEFT = -1

PLAY_PATH = 'images\Play_Button.png'
PLAY_WIDTH = 300
PLAY_HEIGHT = 200
X_PLAY = 50
Y_PLAY = 300
PLAY_BUTTON = Buttons(X_PLAY, Y_PLAY, PLAY_WIDTH, PLAY_HEIGHT)

