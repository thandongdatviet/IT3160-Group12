from math import cos, sin, radians, atan2, degrees
import pygame
from pygame import Surface, Rect
from pygame.draw import rect, circle, line, polygon
from pygame.image import load
from pygame.transform import scale
from const import *
from point import Point
from road import Road, TwoWayRoad


class Display:
    '''Class for display image, icons, ... in the application '''
    def __init__(self) -> None:
        self.maximized = True
        self.ratio = MINIMIZED_WINDOW_HEIGHT / MAXIMIZED_WINDOW_HEIGHT
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.big_start_icon = scale(load("assets/start.png"), (64, 64))
        self.big_end_icon = scale(load("assets/destination.png"), (64, 64))
        self.small_start_icon = scale(load("assets/start.png"), (32, 32))
        self.small_end_icon = scale(load("assets/destination.png"), (32, 32))

    def show_background(self, surface: Surface, img: Surface):
        """Show the map's image on the screen.

        Parameters:
            :param surface (pygame.Surface): The surface to display the image on.
            :param img (pygame.Surface): The image to display.
        """
        if self.maximized:
            surface.blit(img, (0, 0))
        else:
            surface.blit(
                scale(img, (MINIMIZED_WINDOW_WIDTH, MINIMIZED_WINDOW_HEIGHT)),
                (0, 0))

    def show_ui(self, surface: Surface, start_point: Point, end_point: Point,
                time: float, route_length: float, is_click: bool):
        """
        Display GUI on the screen.

        Parameters:
            surface (pygame.Surface): The surface to display the UI.
            start_point (Point): Start point's position to show in the GUI.
            end_point (Point): End point's position to show in the GUI.
            time (float): Find route's time (ms).
            route_length (float): The length of found route between 2 point (meters).
            is_click (bool): A boolean to check if the GUI's 'Find route' button is clicked.
        """
        rect(surface, COLOR["WHITE"], Rect(UI_LEFT, UI_TOP, UI_WIDTH,
                                           UI_HEIGHT))

        UI_CENTER_x = UI_LEFT + UI_WIDTH // 2
        UI_CENTER_y = UI_TOP + UI_HEIGHT // 2
        start_icon_rect = self.big_start_icon.get_rect()
        start_icon_rect.x, start_icon_rect.y = UI_CENTER_x - 200, UI_CENTER_y - 400

        end_icon_rect = self.big_end_icon.get_rect()
        end_icon_rect.x, end_icon_rect.y = UI_CENTER_x - 200, UI_CENTER_y - 300

        time_text = ""
        if is_click and start_point and end_point:
            time_text = "Search time: {:.2f} ms".format(time)
        search_time = self.font.render(time_text, True, 'black', 'white')
        search_time_rect = search_time.get_rect()
        search_time_rect.x, search_time_rect.y = UI_CENTER_x - 200, UI_CENTER_y - 100

        length_text, length_text_font = "", 'black'
        if is_click and start_point and end_point:
            length_text = "Length: {:.2f} m".format(
                route_length) if route_length else "PATH NOT FOUND"
        if not route_length:
            length_text_font = 'red'
        length_text = self.font.render(length_text, True, length_text_font)
        route_length_rect = length_text.get_rect()
        route_length_rect.x, route_length_rect.y = UI_CENTER_x - 200, UI_CENTER_y

        surface.blit(self.big_start_icon, start_icon_rect)
        surface.blit(self.big_end_icon, end_icon_rect)
        surface.blit(search_time, search_time_rect)
        surface.blit(length_text, route_length_rect)

        if start_point:
            start_location = self.font.render(str(start_point), True, 'black')
            start_location_rect = start_location.get_rect()
            start_location_rect.x, start_location_rect.y = UI_CENTER_x - 120, UI_CENTER_y - 380
            surface.blit(start_location, start_location_rect)
        if end_point:
            end_location = self.font.render(str(end_point), True, 'red')
            end_location_rect = end_location.get_rect()
            end_location_rect.x, end_location_rect.y = UI_CENTER_x - 120, UI_CENTER_y - 280
            surface.blit(end_location, end_location_rect)

    def show_locations(self, surface: Surface, start_point: Point,
                       end_point: Point):
        """Display start point's icon and end point's icon on the GUI.

        Parameters:
            :param surface (pygame.Surface): The surface to display.
            :param start_point (Point): The start point's location.
            :param end_point (Point): The end point's location.
        """
        if start_point:
            surface.blit(self.small_start_icon,
                         (start_point[0] - 16, start_point[1] - 32))
        if end_point:
            surface.blit(self.small_end_icon,
                         (end_point[0] - 16, end_point[1] - 32))

    def draw_points(self,
                    surface: Surface,
                    points: list[Point],
                    color=COLOR["BLACK"],
                    radius=POINT_RADIUS):
        """Draw points into the map.

        Parameters:
            :param surface (pygame.Surface): The surface we want to draw points.
            :param points (list[Point]): List of points.
        """
        if self.maximized:
            for point in points:
                center = point.pos
                circle(surface, color, center, radius)
        else:
            for point in points:
                center = (point.x * self.ratio, point.y * self.ratio)
                circle(surface, color, center, radius)

    def draw_roads(self,
                   surface: Surface,
                   roads: list[Road],
                   color=COLOR["BLACK"]):
        """Draw roads into the map.

        Parameters:
            :param surface (pygame.Surface): The surface onto which the roads are to be drawn.
            :param roads (list[Road]): A list of Road objects to be drawn.
            :param color (Tuple[int, int, int]) (optional): The color of the roads. Default is black.
        """
        width = ROAD_WIDTH
        if self.maximized:
            for road in roads:
                if isinstance(road, TwoWayRoad):
                    start_pos, end_pos = road.from_pos, road.to_pos
                    line(surface, color, start_pos, end_pos, width)
                else:
                    start_pos, end_pos = road.from_pos, road.to_pos
                    self.draw_arrow(surface, start_pos, end_pos, color)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = (self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                line(surface, color, start_pos, end_pos, width)

    def draw_arrow(self,
                   surface: Surface,
                   start_pos: tuple,
                   end_pos: tuple,
                   color=COLOR["BLACK"]):
        """Draw an arrow on a surface from `start_pos` to `end_pos`.

        Parameters:
            :param surface (pygame.Surface): The surface onto which the arrow is to be drawn.
            :param start_pos (Tuple[int, int]): A tuple containing the (x,y) coordinates of the arrow's start position.
            :param end_pos (Tuple[int, int]): A tuple containing the (x,y) coordinates of the arrow's end position.
            :param color (Tuple[int, int, int]) (optional): The color of the arrow. Default is black.
        """
        width = ROAD_WIDTH
        x1, y1 = start_pos
        x2, y2 = end_pos

        angle = atan2(y2 - y1, x2 - x1)
        angle = degrees(angle)

        line(surface, color, start_pos, end_pos, width)

        arrow_width, arrow_len = 10, 15
        arrow_points = [(0, 0), (-arrow_len, -arrow_width / 2),
                        (-arrow_len, arrow_width / 2)]

        rotated_arrow_points = []
        for point in arrow_points:
            rotated_x = point[0] * cos(radians(angle)) - point[1] * sin(
                radians(angle))
            rotated_y = point[0] * sin(radians(angle)) + point[1] * cos(
                radians(angle))
            rotated_arrow_points.append((x2 + rotated_x, y2 + rotated_y))
        polygon(surface, color, rotated_arrow_points)

    def draw_found_path(self, surface: Surface, roads: list[Road]):
        """Draw the found route on a surface.

        Parameters:
            :param surface (pygame.Surface): The surface onto which the route is to be drawn.
            :param roads (list[Road]): A list of Road objects defining the route to be drawn.
        """
        if roads is None: return
        color, width = COLOR["RED"], ROAD_WIDTH

        if self.maximized:
            self.draw_roads(surface, roads, color)
        else:
            for road in roads:
                x1, y1 = road.from_pos
                x2, y2 = road.to_pos
                start_pos = (self.ratio * x1, self.ratio * y1)
                end_pos = (self.ratio * x2, self.ratio * y2)
                line(surface, color, start_pos, end_pos, width)