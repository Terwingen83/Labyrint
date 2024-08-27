from src.models.position import Position
from src.utils.pathfinding import pathfinding
from src.models.entity import Entity, Wall, Diamond
import random
from copy import copy

PART_SIZE = 3

def fill_map(map, start_pos, end_pos):
    parts = [
        ###

        ###
        [Position(0, 0), Position(1, 0), Position(2, 0), Position(0, 2), Position(1, 2), Position(2, 2)],

        # #
        # #
        # #
        [Position(0, 0), Position(0, 1), Position(0, 2), Position(2, 0), Position(2, 1), Position(2, 2)],

        # #

        # #
        [Position(0, 0), Position(0, 2), Position(2, 0), Position(2, 2)],

        # #
        #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1)],

        # #
          #
        # #
        [Position(0, 0), Position(0, 2), Position(2, 0), Position(2, 2), Position(2, 1)],

        ###

        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0)],

        # #

        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 2)],

        ###
        #
        ###
        [Position(0, 0),  Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0), Position(0, 1), Position(1, 2)],

        ###
          #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 2), Position(2, 1)],

        # #
        # #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(2, 1), Position(1, 2)],

        ###
        # #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 0), Position(2, 1)],

        ###
          #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0), Position(1, 2)],

        ###
        #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 0)],

        # #
          #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(2, 1), Position(1, 2)],

        # #
        #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 2)]
    ]

    # TODO: Items zum einsammeln hinzufügen
    list_pathfinding_positions = []
    for x in range(1, map.maxsize.x - 1, PART_SIZE ):
        for y in range(1, map.maxsize.y - 1, PART_SIZE ):
            room_pos = Position(x, y)
            list_pathfinding_positions.append(room_pos)

    random.shuffle(list_pathfinding_positions)
    list_pathfinding_positions2 = copy(list_pathfinding_positions)

    for room_pos in list_pathfinding_positions2:
        random.shuffle(parts)

        for wall_part in parts:
            for wall_pos in wall_part:
                position = wall_pos + room_pos
                map.add_entity(Wall(position))

            map.map_output()
            print()

            found_path = True
            for saved_room_position in list_pathfinding_positions:
                found_path = found_path and bool(pathfinding(map, start_pos, saved_room_position + Position(1, 1)))

            found_path_end = pathfinding(map, start_pos, end_pos)
            if found_path == False or found_path_end is None:
                for wall_position in wall_part:
                    position = wall_position + room_pos
                    wall = map.occupation(position)

                    if wall is not None:
                        map.remove_entity(wall)
            else:
                break

