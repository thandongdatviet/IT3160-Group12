'''Constant values used for setting screen, drawing roads and GUI for the application'''
MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT = 1440, 890
'''Maximum height and width for display screen'''

MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT = 936, 850
'''Minimum height and width for display screen'''

UI_TOP, UI_LEFT, UI_WIDTH, UI_HEIGHT = 0, 980, 460, 890
'''Coordinates for setting map's GUI'''

INFINITY = 999999
'''Default value for f, g, h between 2 point when searching route'''

COLOR = {
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0)
}
'''Dictionary for colors using in the application '''

ROAD_WIDTH = 3
'''Road's width to show on the map'''

POINT_RADIUS = 3
'''Circle point's radius'''