from rubik.cube import Cube, NB_CORNERS, NB_EDGES

TWIST_COUNT = 3 ** (NB_CORNERS - 1)
FLIP_COUNT = 2 ** (NB_EDGES - 1)

def get_twist(cube: Cube) -> int:
    twist = 0
    for i in range(NB_CORNERS - 1):
        twist = twist * 3 + cube.corner_ori[i]
    return twist

def get_flip(cube: Cube) -> int:
    flip = 0
    for i in range(NB_EDGES - 1):
        flip = flip * 2 + cube.edge_ori[i]
    return flip