from collections import namedtuple

LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
STRAIGHT = "-"
STRAIGHT_VERTICAL = "|"
SLASH = "/"
BACKSLASH = "\\"
INTERSECTION = "+"

STATES = {
    LEFT : STRAIGHT,
    STRAIGHT : RIGHT,
    RIGHT : LEFT
}

CartDirections = namedtuple('CartDirections',['dx','dy','road', 'left','right','backslash', 'slash'])

DIRECTIONS = {
    RIGHT : CartDirections(0, 1, STRAIGHT, UP, DOWN, DOWN, UP),
    LEFT : CartDirections(0, -1, STRAIGHT, DOWN, UP, UP, DOWN),
    UP : CartDirections(-1, 0, STRAIGHT_VERTICAL, LEFT, RIGHT, LEFT, RIGHT),
    DOWN : CartDirections(1, 0, STRAIGHT_VERTICAL, RIGHT, LEFT, RIGHT, LEFT)
}

class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.state = LEFT
        self.direction = direction

    def move(self, maze):
        self.x += DIRECTIONS[self.direction].dx
        self.y += DIRECTIONS[self.direction].dy

        state = maze[self.x][self.y]

        if (state == INTERSECTION):
            if self.state == LEFT:
                self.direction = DIRECTIONS[self.direction].left
            elif self.state == RIGHT:
                self.direction = DIRECTIONS[self.direction].right

            self.state = STATES[self.state]
        elif (state == SLASH):
            self.direction = DIRECTIONS[self.direction].slash
        elif (state == BACKSLASH):
            self.direction = DIRECTIONS[self.direction].backslash

    def __lt__(self, other):
        return (self.x < other.x) or (self.x == other.x and self.y < other.y)

    def get_coords(self):
        return (self.y, self.x)

def main():
    maze = list()
    carts = list()
    coords = set()
    with open("input.txt", "r") as fin:
        for ind_x, line in enumerate(fin):
            road = list(line)
            for ind_y, char in enumerate(road):
                if char in DIRECTIONS.keys():
                    cart = Cart(ind_x, ind_y, char)
                    carts.append(cart)
                    coords.add(cart.get_coords())
                    road[ind_y] = DIRECTIONS[char].road
            maze.append(road)
    
    while True:
        carts.sort()
        for cart in carts:
            coords.remove(cart.get_coords())
            cart.move(maze)
            current_coordinates = cart.get_coords()
            if (current_coordinates in coords):
                print('Collision at ', current_coordinates)
                return
            else:
                coords.add(current_coordinates)

if __name__ == "__main__":
    main()