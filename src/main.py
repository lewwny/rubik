from rubik.cube import Cube
from rubik.moves import r, r_prime, r2, u, u_prime, u2, l, l_prime, l2
from rubik.parser import parse_sequence, InvalidMoveError

def main():
    try:
        sequence = parse_sequence(input("Entrez une séquence de mouvements (ex: R U R' U'): "))
        cube = Cube()
        for move_fn in sequence:
            move_fn(cube)
        if cube.is_solved():
            print("Le cube est résolu après l'application de la séquence.")
        else:
            print("Le cube n'est pas résolu après l'application de la séquence.")
    except InvalidMoveError as e:
        print(f"Erreur : {e}")
        return
    except (KeyboardInterrupt, EOFError):
        print("\nInterruption par l'utilisateur.")
        return

if __name__ == "__main__":
    main()
