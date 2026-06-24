from rubik import moves

VALID_FACES = "UDLRFB"

class InvalidMoveError(Exception):
    """Exception levée lorsqu'une séquence de mouvements invalide est rencontrée."""
    exit_code = 1

def _token_to_move(token: str):
    """Convertit un token de mouvement en fonction de mouvement correspondante."""
    if not token:
        raise InvalidMoveError("Token vide.")
    face = token[0].upper()
    if face not in VALID_FACES:
        raise InvalidMoveError(f"Face invalide : {face}")
    modifier = token[1:]
    func_name = face.lower()

    if modifier == "":
        pass
    elif modifier == "'":
        func_name += "_prime"
    elif modifier == "2":
        func_name += "2"
    else:
        raise InvalidMoveError(f"Modificateur invalide : {modifier}")
    
    move_func = getattr(moves, func_name, None)
    if move_func is None:
        raise InvalidMoveError(f"Fonction de mouvement non trouvée pour : {func_name}")
    return move_func


def parse_sequence(sequence: str) -> list:
    tokens = sequence.split()
    if not tokens:
        raise InvalidMoveError("La séquence est vide.")
    return [_token_to_move(token) for token in tokens]