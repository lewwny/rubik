from rubik.cube import Cube
from rubik.coords import get_twist, get_flip, TWIST_COUNT, FLIP_COUNT


def test_solved_cube_has_twist_zero():
    cube = Cube()
    assert get_twist(cube) == 0


def test_solved_cube_has_flip_zero():
    cube = Cube()
    assert get_flip(cube) == 0


def test_twist_matches_hand_calculated_example():
    # reprend exactement l'exemple fait à la main :
    # corner_ori = [1, 0, 2, 1, 0, 2, 1, 2] -> twist attendu = 925
    cube = Cube()
    cube.corner_ori = [1, 0, 2, 1, 0, 2, 1, 2]
    assert get_twist(cube) == 925


def test_flip_matches_hand_calculated_example():
    # reprend exactement l'exemple fait à la main :
    # edge_ori = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1] -> flip attendu = 844
    cube = Cube()
    cube.edge_ori = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    assert get_flip(cube) == 844


def test_twist_ignores_last_corner_orientation():
    # la 8e valeur (position 7) ne doit jamais influencer le résultat,
    # puisqu'elle est censée être déductible des 7 premières
    cube_a = Cube()
    cube_a.corner_ori = [1, 0, 2, 1, 0, 2, 1, 2]

    cube_b = Cube()
    cube_b.corner_ori = [1, 0, 2, 1, 0, 2, 1, 0]  # dernière valeur différente

    assert get_twist(cube_a) == get_twist(cube_b)


def test_flip_ignores_last_edge_orientation():
    cube_a = Cube()
    cube_a.edge_ori = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]

    cube_b = Cube()
    cube_b.edge_ori = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]  # dernière valeur différente

    assert get_flip(cube_a) == get_flip(cube_b)


def test_twist_stays_within_valid_range():
    cube = Cube()
    cube.corner_ori = [2, 2, 2, 2, 2, 2, 2, 2]  # le maximum possible sur 7 chiffres
    twist = get_twist(cube)
    assert 0 <= twist < TWIST_COUNT


def test_flip_stays_within_valid_range():
    cube = Cube()
    cube.edge_ori = [1] * 12  # le maximum possible sur 11 chiffres pertinents
    flip = get_flip(cube)
    assert 0 <= flip < FLIP_COUNT


def test_twist_changes_when_orientation_changes():
    cube = Cube()
    base_twist = get_twist(cube)

    cube.corner_ori[0] = 1
    assert get_twist(cube) != base_twist


def test_flip_changes_when_orientation_changes():
    cube = Cube()
    base_flip = get_flip(cube)

    cube.edge_ori[0] = 1
    assert get_flip(cube) != base_flip