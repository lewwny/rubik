from rubik.cube import Cube
from rubik.moves import (
    r, r_prime, r2,
    u, u_prime, u2,
    l, l_prime, l2,
    f, f_prime, f2,
    d, d_prime, d2,
    b, b_prime, b2,
)


def test_r_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        r(cube)
    assert cube.is_solved()


def test_r_then_r_prime_is_identity():
    cube = Cube()
    r(cube)
    r_prime(cube)
    assert cube.is_solved()


def test_r2_twice_is_identity():
    cube = Cube()
    r2(cube)
    r2(cube)
    assert cube.is_solved()


def test_r_moves_expected_corners():
    cube = Cube()
    r(cube)
    # la pièce qui était en 4 (DFR) doit maintenant être en 0 (URF)
    assert cube.corner_perm[0] == 4
    assert cube.corner_perm[3] == 0
    assert cube.corner_perm[7] == 3
    assert cube.corner_perm[4] == 7


def test_r_does_not_touch_other_corners():
    cube = Cube()
    r(cube)
    for pos in [1, 2, 5, 6]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_r_moves_expected_edges():
    cube = Cube()
    r(cube)
    assert cube.edge_perm[0] == 8
    assert cube.edge_perm[11] == 0
    assert cube.edge_perm[4] == 11
    assert cube.edge_perm[8] == 4


def test_r_does_not_change_edge_orientation():
    cube = Cube()
    r(cube)
    for pos in [0, 4, 8, 11]:
        assert cube.edge_ori[pos] == 0


def test_r_does_not_touch_other_edges():
    cube = Cube()
    r(cube)
    for pos in [1, 2, 3, 5, 6, 7, 9, 10]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0


def test_u_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        u(cube)
    assert cube.is_solved()


def test_u_then_u_prime_is_identity():
    cube = Cube()
    u(cube)
    u_prime(cube)
    assert cube.is_solved()


def test_u2_twice_is_identity():
    cube = Cube()
    u2(cube)
    u2(cube)
    assert cube.is_solved()


def test_u_moves_expected_corners():
    cube = Cube()
    u(cube)
    assert cube.corner_perm[0] == 3
    assert cube.corner_perm[1] == 0
    assert cube.corner_perm[2] == 1
    assert cube.corner_perm[3] == 2


def test_u_does_not_touch_other_corners():
    cube = Cube()
    u(cube)
    for pos in [4, 5, 6, 7]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_u_moves_expected_edges():
    cube = Cube()
    u(cube)
    assert cube.edge_perm[0] == 3
    assert cube.edge_perm[1] == 0
    assert cube.edge_perm[2] == 1
    assert cube.edge_perm[3] == 2


def test_u_does_not_touch_other_edges():
    cube = Cube()
    u(cube)
    for pos in [4, 5, 6, 7, 8, 9, 10, 11]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0


def test_l_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        l(cube)
    assert cube.is_solved()


def test_l_then_l_prime_is_identity():
    cube = Cube()
    l(cube)
    l_prime(cube)
    assert cube.is_solved()


def test_l2_twice_is_identity():
    cube = Cube()
    l2(cube)
    l2(cube)
    assert cube.is_solved()


def test_l_moves_expected_corners():
    cube = Cube()
    l(cube)
    assert cube.corner_perm[2] == 6
    assert cube.corner_perm[1] == 2
    assert cube.corner_perm[5] == 1
    assert cube.corner_perm[6] == 5


def test_l_does_not_touch_other_corners():
    cube = Cube()
    l(cube)
    for pos in [0, 3, 4, 7]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_l_moves_expected_edges():
    cube = Cube()
    l(cube)
    assert cube.edge_perm[2] == 10
    assert cube.edge_perm[9] == 2
    assert cube.edge_perm[6] == 9
    assert cube.edge_perm[10] == 6


def test_l_does_not_touch_other_edges():
    cube = Cube()
    l(cube)
    for pos in [0, 1, 3, 4, 5, 7, 8, 11]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0


def test_f_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        f(cube)
    assert cube.is_solved()


def test_f_then_f_prime_is_identity():
    cube = Cube()
    f(cube)
    f_prime(cube)
    assert cube.is_solved()


def test_f2_twice_is_identity():
    cube = Cube()
    f2(cube)
    f2(cube)
    assert cube.is_solved()


def test_f_moves_expected_corners():
    cube = Cube()
    f(cube)
    assert cube.corner_perm[1] == 5
    assert cube.corner_perm[0] == 1
    assert cube.corner_perm[4] == 0
    assert cube.corner_perm[5] == 4


def test_f_does_not_touch_other_corners():
    cube = Cube()
    f(cube)
    for pos in [2, 3, 6, 7]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_f_moves_expected_edges():
    cube = Cube()
    f(cube)
    assert cube.edge_perm[1] == 9
    assert cube.edge_perm[8] == 1
    assert cube.edge_perm[5] == 8
    assert cube.edge_perm[9] == 5


def test_f_does_not_touch_other_edges():
    cube = Cube()
    f(cube)
    for pos in [0, 2, 3, 4, 6, 7, 10, 11]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0


def test_d_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        d(cube)
    assert cube.is_solved()


def test_d_then_d_prime_is_identity():
    cube = Cube()
    d(cube)
    d_prime(cube)
    assert cube.is_solved()


def test_d2_twice_is_identity():
    cube = Cube()
    d2(cube)
    d2(cube)
    assert cube.is_solved()


def test_d_moves_expected_corners():
    cube = Cube()
    d(cube)
    assert cube.corner_perm[5] == 6
    assert cube.corner_perm[4] == 5
    assert cube.corner_perm[7] == 4
    assert cube.corner_perm[6] == 7


def test_d_does_not_touch_other_corners():
    cube = Cube()
    d(cube)
    for pos in [0, 1, 2, 3]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_d_moves_expected_edges():
    cube = Cube()
    d(cube)
    assert cube.edge_perm[5] == 6
    assert cube.edge_perm[4] == 5
    assert cube.edge_perm[11] == 4
    assert cube.edge_perm[6] == 11


def test_d_does_not_touch_other_edges():
    cube = Cube()
    d(cube)
    for pos in [0, 1, 2, 3, 7, 8, 9, 10]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0


def test_b_four_times_returns_to_solved():
    cube = Cube()
    for _ in range(4):
        b(cube)
    assert cube.is_solved()


def test_b_then_b_prime_is_identity():
    cube = Cube()
    b(cube)
    b_prime(cube)
    assert cube.is_solved()


def test_b2_twice_is_identity():
    cube = Cube()
    b2(cube)
    b2(cube)
    assert cube.is_solved()


def test_b_moves_expected_corners():
    cube = Cube()
    b(cube)
    assert cube.corner_perm[3] == 7
    assert cube.corner_perm[2] == 3
    assert cube.corner_perm[6] == 2
    assert cube.corner_perm[7] == 6


def test_b_does_not_touch_other_corners():
    cube = Cube()
    b(cube)
    for pos in [0, 1, 4, 5]:
        assert cube.corner_perm[pos] == pos
        assert cube.corner_ori[pos] == 0


def test_b_moves_expected_edges():
    cube = Cube()
    b(cube)
    assert cube.edge_perm[3] == 11
    assert cube.edge_perm[10] == 3
    assert cube.edge_perm[7] == 10
    assert cube.edge_perm[11] == 7


def test_b_does_not_touch_other_edges():
    cube = Cube()
    b(cube)
    for pos in [0, 1, 2, 4, 5, 6, 8, 9]:
        assert cube.edge_perm[pos] == pos
        assert cube.edge_ori[pos] == 0