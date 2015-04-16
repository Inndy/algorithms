import random, sys

def generate_map(w, h, fill_percentage = 27):
    def rand_point():
        return 0 if random.randint(0, 99) > fill_percentage else 1
    return [ bytearray(rand_point() for _ in range(w)) for _ in range(h) ]

class Map2D(object):
    BLANK = 0
    BLOCK = 1
    STEPS = 2
    def __init__(self, map = None, size = (0, 0)):
        """
        Initialize from a existed map or create a clean map from size

        map     2-D list
        size    tuple(width, height)
        """
        if map:
            self.map = map
        elif size:
            w, h = size
            self.map = [ bytearray(0 for _ in range(w)) for _ in range(h) ]

    def render_map(self, blank = ' ', block = 'X', steps = '.'):
        M = [ blank, block, steps ]
        return '\n'.join( ''.join(M[c] for c in r) for r in self.map )

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    def __getitem__(self, key):
        return self.map[key]

def DFS(m, f, start, end):
    """
    DFS-path-searching algorithm

    m       Map2D object
    f       2D-list flag map
    start   tuple(x, y)
    end     tuple(x, y)
    """
    x, y = start
    if start == end:
        m[y][x] = 2
        return [end]
    if not (0 <= x < m.width and 0 <= y < m.height) or m[y][x] != 0 or f[y][x]:
        return None
    f[y][x] = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r = DFS(m, f, (x + dx, y + dy), end)
        if r:
            m[y][x] = 2
            return [start] + r
    return None

sys.setrecursionlimit(10000)
WIDTH = 15
HEIGHT = 15
m = Map2D(generate_map(WIDTH, HEIGHT))
f = Map2D(size = (WIDTH, HEIGHT))
route = DFS(m, f, (0, 0), (WIDTH - 1, HEIGHT - 1))
print(m.render_map())
print(route)
