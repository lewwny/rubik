from rubik.cube import Cube, NB_CORNERS, NB_EDGES


def test_cube_starts_solved():
    cube = Cube()
    assert cube.is_solved()


def test_solved_cube_has_identity_permutations():
    cube = Cube()
    assert cube.corner_perm == list(range(NB_CORNERS))
    assert cube.edge_perm == list(range(NB_EDGES))
    assert cube.corner_ori == [0] * NB_CORNERS
    assert cube.edge_ori == [0] * NB_EDGES


def test_copy_is_independent():
    cube = Cube()
    clone = cube.copy()
    clone.corner_perm[0] = 3
    assert cube.corner_perm[0] == 0  # l'original n'est pas affecté
    assert clone.corner_perm[0] == 3


def test_equality():
    cube_a = Cube()
    cube_b = Cube()
    assert cube_a == cube_b

    cube_b.corner_ori[0] = 1
    assert cube_a != cube_b


def test_modified_cube_is_not_solved():
    cube = Cube()
    cube.edge_ori[3] = 1
    assert not cube.is_solved()