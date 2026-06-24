NB_CORNERS = 8
NB_EDGES = 12




class Cube:
    def __init__(self):
        self.corner_perm = list(range(NB_CORNERS))
        self.corner_ori = [0] * NB_CORNERS

        self.edge_perm = list(range(NB_EDGES))
        self.edge_ori = [0] * NB_EDGES
    
    def is_solved(self):
        return (self.corner_perm == list(range(NB_CORNERS)) and
                self.corner_ori == [0] * NB_CORNERS and
                self.edge_perm == list(range(NB_EDGES)) and
                self.edge_ori == [0] * NB_EDGES)
    
    def copy(self):
        new_cube = Cube()
        new_cube.corner_perm = self.corner_perm[:]
        new_cube.corner_ori = self.corner_ori[:]
        new_cube.edge_perm = self.edge_perm[:]
        new_cube.edge_ori = self.edge_ori[:]
        return new_cube
    
    def __eq__(self, other):
        return (self.corner_perm == other.corner_perm and
                self.corner_ori == other.corner_ori and
                self.edge_perm == other.edge_perm and
                self.edge_ori == other.edge_ori)
    
    def __repr__(self):
        return (f"Cube(corner_perm={self.corner_perm}, corner_ori={self.corner_ori}, "
                f"edge_perm={self.edge_perm}, edge_ori={self.edge_ori})")