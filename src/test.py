import sys
import os
import pygame
import time
from pygame.locals import *
from pygame.draw import rect
from pygame.font import Font
from pygame.display import set_mode, set_caption, flip
from pygame.event import get
from const import *
from display import Display
from initialize import *
from map import Map


class Main:
    """Class used for run the application using `pygame`"""
    def __init__(self):
        pygame.init()
        self.screen = set_mode(
            (MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT))
        set_caption('Map Truc Bach')
        self.path = None
        """Found path will be saved here"""
        self.map = Map()
        self.display = Display()

        self.show_defined_roads, self.show_open_close_list = False, False
        self.open_list, self.closed_list = [], []

    def mainloop(self):
        """The loop of the app"""
        screen = self.screen
        map = self.map
        display = self.display
        start_point, end_point, is_click = None, None, False
        start_time, end_time, route_length, ratio = 0.0, 0.0, 0.0, 1.12
        # Start the loop
        while True:
            display.show_background(screen, map.img)

            if self.show_defined_roads:
                display.draw_points(screen, list(map.map_points.values()))
                display.draw_roads(screen, map.roads)

            if self.show_open_close_list:
                display.draw_points(screen, self.open_list, COLOR["BLUE"], 5)
                display.draw_points(screen, self.closed_list, COLOR["RED"], 5)

            display.draw_found_path(screen, self.path)
            display.show_ui(screen, start_point, end_point,
                            1000 * (end_time - start_time), route_length,
                            is_click)
            display.show_locations(screen, start_point, end_point)
            button_rect = rect(screen, 'blue', (UI_LEFT + 150, 250, 150, 50))
            text = Font(None, 36).render("Find path", True, COLOR["WHITE"])
            screen.blit(text, text.get_rect(center=button_rect.center))
            flip()
            for event in get():
                if event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    is_click = False
                    if UI_LEFT > x > 16 and y > 32:
                        self.path = []
                        self.closed_list = []
                        self.open_list = []
                        tmp_point, is_mid_point, nearest_road = self.choose_point_from_mouse_click((x, y))
                        if is_mid_point: self.map.add_mid_point(tmp_point, nearest_road)
                        if event.button == 1:  # Left mouse button
                            if tmp_point != end_point:
                                start_point = tmp_point
                        elif event.button == 3:  # Right mouse button
                            if tmp_point != start_point:
                                end_point = tmp_point
                    if button_rect.collidepoint((x, y)):
                        is_click = True
                        if start_point and end_point:
                            start_time = time.time()
                            self.path, self.open_list, self.closed_list = map.find_path(
                                start_point, end_point)
                            end_time = time.time()
                            route_length = ratio * sum(
                                [road.length
                                 for road in self.path]) if self.path else 0.0

                elif event.type == KEYDOWN:
                    if event.key == K_s:
                        # Toggle window size
                        display.maximized = not display.maximized
                        if display.maximized:
                            self.screen = set_mode((MAXIMIZED_WINDOW_WIDTH,
                                                    MAXIMIZED_WINDOW_HEIGHT))
                        else:
                            self.screen = set_mode((MINIMIZED_WINDOW_WIDTH,
                                                    MINIMIZED_WINDOW_HEIGHT))

                    elif event.key == K_t:
                        # Toggle see defined roads
                        self.show_defined_roads = not self.show_defined_roads

                    elif event.key == K_r:
                        self.show_open_close_list = not self.show_open_close_list

                    elif event.key == K_q:
                        # Quit the app
                        pygame.quit()
                        sys.exit()

                elif event.type == QUIT:
                    # Quit the app
                    pygame.quit()
                    sys.exit()

    def choose_point_from_mouse_click(self, click_pos: tuple[int, int]):
        """
        Based on a mouse click, choose a point on the screen that its position is exists in the map data.

        :param start_point: A tuple with the (x, y) coordinates of the starting point.

        :return: A tuple with the (x, y) coordinates of the chosen point.
        """
        # nearest_road_from, nearest_road_to, min_dist = None, None, 999
        # for road in self.map.roads:
        #     if road._is_look(start_point):
        #         tmp_dist = road._calc_dist(start_point)
        #         if tmp_dist < min_dist:
        #             nearest_road_from = road.from_point
        #             nearest_road_to = road.to_point
        #             min_dist = tmp_dist
        # if nearest_road_to and nearest_road_from:
        #     dist_from, dist_to = nearest_road_from._calc_dist(
        #         start_point), nearest_road_to._calc_dist(start_point)
        #     if dist_from < dist_to:
        #         start_point = (nearest_road_from.x, nearest_road_from.y)
        #     else:
        #         start_point = (nearest_road_to.x, nearest_road_to.y)
        # return start_point
        nearest_point, nearest_road, min_dist_point, min_dist_road = None, None, INFINITY, INFINITY
        for key in self.map.map_points:
            point = self.map.map_points[key]
            if point._calc_dist(click_pos) < min_dist_point:
                nearest_point = point
                min_dist_point = point._calc_dist(click_pos)
                if min_dist_point <= 10:
                    return nearest_point.pos, False, None
                
        for road in self.map.roads:
            if road._calc_dist(click_pos) < min_dist_road and road._is_look(click_pos):
                nearest_road = road
                min_dist_road = road._calc_dist(click_pos)
        
        if min_dist_point < min_dist_road:
            return nearest_point.pos, False, None
        else:
            return nearest_road._perpendicular_pos(click_pos), True, nearest_road
            


main = Main()
main.mainloop()
