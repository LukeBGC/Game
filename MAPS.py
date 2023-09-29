# This program creates the map for each of the levels

# MAP 1
def map_1():
    spawn = (8,1)
    e_locations = [(10,6), (4,9)]
    interactable_locations = [(5,4), (9,10)]
    open_spaces = [(8,2),
                    (8,3),
                    (6,4), (7,4), (8,4), (9,4), (10, 4),
                    (5,5), (8,5), (10,5),
                    (5,6), (8,6), (9,6),
                    (5,7), (8,7),
                    (5,8), (8,8),
                    (5,9), (8,9),
                    (4,10), (6,10), (7,10), (8,10),
                    (4,11), (5,11), (6,11)]
    return spawn, e_locations, interactable_locations, open_spaces
