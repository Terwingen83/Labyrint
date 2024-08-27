from src.models.position import Position


def pathfinding(map, start_pos, end_pos):
    north = Position(0, -1)
    south = Position(0, +1)
    west = Position(-1, 0)
    east = Position(+1, 0)
    directions = [north, east, south, west]

    known_fields = {}

    path = []
    player_pos = start_pos

    if start_pos == end_pos:
        return start_pos

    while True:
        if player_pos in path:
            path = path[:path.index(player_pos) + 1]
        else:
            path.append(player_pos)

        if player_pos == end_pos:
            break

        if player_pos in known_fields:
            known_fields[player_pos] += 1
        else:
            known_fields[player_pos] = 1

        shortest_distance = 99999999999

        # Für alle Nachbarfelder
        for dir in directions:
            new_pos = player_pos + dir

            # Wenn das Nachbarfeld belegt ist, ignorieren wir es. Zur Wegfindung interessieren uns nur leere Felder
            # die Start Position ist immer belegt, unsere Spielfigur steht ja immer noch dort - trotzdem können wir da lang gehen
            if not map.occupation(new_pos) or new_pos == start_pos:
                # Entfernung vom Nachbarfeld zum Ziel + wenn wir schon mal drauf waren, dann sollten wir besser versuchen
                # woanders lang zu laufen, weshalb wir etwas 'Entfernung' hinzu addieren
                distance = (end_pos - new_pos).length() + known_fields.get(new_pos, 0)

                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_distance_pos = new_pos
        if known_fields[start_pos] > 5: # in case we can't reach the target
            return None

        player_pos = shortest_distance_pos

    return path[1]