import pytest

from rubik.cube import Cube
from rubik.parser import parse_sequence, InvalidMoveError
from rubik import moves


def test_parse_simple_move():
    result = parse_sequence("R")
    assert result == [moves.r]


def test_parse_prime_move():
    result = parse_sequence("R'")
    assert result == [moves.r_prime]


def test_parse_double_move():
    result = parse_sequence("R2")
    assert result == [moves.r2]


def test_parse_multiple_tokens():
    result = parse_sequence("R U R'")
    assert result == [moves.r, moves.u, moves.r_prime]


def test_parse_tolerates_extra_spaces():
    result = parse_sequence("  R   U2  ")
    assert result == [moves.r, moves.u2]


def test_parse_empty_sequence_raises():
    with pytest.raises(InvalidMoveError):
        parse_sequence("")


def test_parse_invalid_face_raises():
    with pytest.raises(InvalidMoveError):
        parse_sequence("X")


def test_parse_invalid_modifier_raises():
    with pytest.raises(InvalidMoveError):
        parse_sequence("R3")


def test_parse_forbidden_slice_move_raises():
    # M, E, S sont interdits par le sujet
    with pytest.raises(InvalidMoveError):
        parse_sequence("M")


def test_parsed_sequence_applies_correctly_to_cube():
    cube = Cube()
    sequence = parse_sequence("R R R R")
    for move_fn in sequence:
        move_fn(cube)
    assert cube.is_solved()