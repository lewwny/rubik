
from rubik.cube import Cube


def _apply_corner_cycle(cube: Cube, cycle: list[int], ori_deltas: list[int]) -> None:
    """Applique un cycle de 4 positions de coins, avec deltas d'orientation.

    cycle[i] -> cycle[i+1] (et cycle[-1] -> cycle[0])
    ori_deltas[i] est ajouté à l'orientation du coin qui arrive en cycle[i+1].
    """
    old_perm = cube.corner_perm[:]
    old_ori = cube.corner_ori[:]

    for i in range(4):
        src = cycle[i]
        dst = cycle[(i + 1) % 4]
        cube.corner_perm[dst] = old_perm[src]
        cube.corner_ori[dst] = (old_ori[src] + ori_deltas[i]) % 3


def _apply_edge_cycle(cube: Cube, cycle: list[int], ori_deltas: list[int]) -> None:
    """Applique un cycle de 4 positions d'arêtes, avec deltas d'orientation (0 ou 1)."""
    old_perm = cube.edge_perm[:]
    old_ori = cube.edge_ori[:]

    for i in range(4):
        src = cycle[i]
        dst = cycle[(i + 1) % 4]
        cube.edge_perm[dst] = old_perm[src]
        cube.edge_ori[dst] = (old_ori[src] + ori_deltas[i]) % 2


def r(cube: Cube) -> None:
    """Mouvement R (face droite, sens horaire), appliqué en place."""
    corner_cycle = [4, 0, 3, 7]
    corner_ori_deltas = [1, 2, 1, 2]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [8, 0, 11, 4]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def r_prime(cube: Cube) -> None:
    """Mouvement R' (inverse de R) : on applique R trois fois."""
    r(cube)
    r(cube)
    r(cube)


def r2(cube: Cube) -> None:
    """Mouvement R2 (demi-tour) : on applique R deux fois."""
    r(cube)
    r(cube)


def u(cube: Cube) -> None:
    """Mouvement U (face haut, sens horaire)."""
    corner_cycle = [0, 1, 2, 3]
    corner_ori_deltas = [0, 0, 0, 0]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [0, 1, 2, 3]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def u_prime(cube: Cube) -> None:
    """Mouvement U' (inverse de U)."""
    u(cube)
    u(cube)
    u(cube)


def u2(cube: Cube) -> None:
    """Mouvement U2 (demi-tour)."""
    u(cube)
    u(cube)


def l(cube: Cube) -> None:
    """Mouvement L (face gauche, sens horaire)."""
    corner_cycle = [2, 1, 5, 6]
    corner_ori_deltas = [0, 0, 0, 0]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [2, 9, 6, 10]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def l_prime(cube: Cube) -> None:
    l(cube)
    l(cube)
    l(cube)


def l2(cube: Cube) -> None:
    l(cube)
    l(cube)


def f(cube: Cube) -> None:
    """Mouvement F (face avant, sens horaire)."""
    corner_cycle = [1, 0, 4, 5]
    corner_ori_deltas = [0, 0, 0, 0]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [1, 8, 5, 9]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def f_prime(cube: Cube) -> None:
    f(cube)
    f(cube)
    f(cube)


def f2(cube: Cube) -> None:
    f(cube)
    f(cube)


def d(cube: Cube) -> None:
    """Mouvement D (face bas, sens horaire)."""
    corner_cycle = [5, 4, 7, 6]
    corner_ori_deltas = [0, 0, 0, 0]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [5, 4, 11, 6]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def d_prime(cube: Cube) -> None:
    d(cube)
    d(cube)
    d(cube)


def d2(cube: Cube) -> None:
    d(cube)
    d(cube)


def b(cube: Cube) -> None:
    """Mouvement B (face arrière, sens horaire)."""
    corner_cycle = [3, 2, 6, 7]
    corner_ori_deltas = [0, 0, 0, 0]
    _apply_corner_cycle(cube, corner_cycle, corner_ori_deltas)
    edge_cycle = [3, 10, 7, 11]
    edge_ori_deltas = [0, 0, 0, 0]
    _apply_edge_cycle(cube, edge_cycle, edge_ori_deltas)


def b_prime(cube: Cube) -> None:
    b(cube)
    b(cube)
    b(cube)


def b2(cube: Cube) -> None:
    b(cube)
    b(cube)