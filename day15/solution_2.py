from collections import deque

WALL = "#"
ELF = "E"
GOBLIN = "G"
CAVERN = "."

maze = list()

ELF_DAMAGE = 3
ELF_DIES = False

def print_maze():
    for line in maze:
        print("".join(line))
    print()

class Enemy:
    def __init__(self, enemytype, x, y):
        self.type = enemytype
        self.x = x
        self.y = y
        self.hp = 200
        self.dmg = ELF_DAMAGE if self.type == ELF else 3
        self.enemytype = ELF if self.type == GOBLIN else GOBLIN

    def get_coordinates(self):
        return self.x, self.y
    
    def get_info(self):
        return self.x, self.y, self.enemytype

    def __lt__(self, other):
        return (self.x < other.x) or (self.x == other.x and self.y < other.y)


class Battle:
    def __init__(self, filename="input.txt"):
        """

        :type filename: string
        :rtype: object
        """
        self.enemies = list()
        self.round = 0
        global maze
        maze = list()
        with open(filename, "r") as fin:
            for ind_x, line in enumerate(fin):
                line = list(line.strip())
                for ind_y, char in enumerate(line):
                    if char in [GOBLIN, ELF]:
                        enemy = Enemy(char, ind_x, ind_y)
                        self.enemies.append(enemy)
                maze.append(line)

    def has_enemies(self):
        unique = set()
        for line in maze:
            for el in line:
                unique.add(el)
        return GOBLIN in unique and ELF in unique

    def has_enemy_in_range(self, target):
        x, y, c = target.get_info()
        return any((
            maze[x-1][y]==c,
            maze[x+1][y]==c,
            maze[x][y-1]==c,
            maze[x][y+1]==c
            ))

    def make_move(self, enemy):
        if self.has_enemy_in_range(enemy):
            return

        stack = deque([[enemy]])
        visited = set()
        paths = {}
        while len(stack) > 0:
            path = stack.popleft()
            current_enemy = path[-1]
            if self.has_enemy_in_range(current_enemy):
                target = self.get_enemy_to_attack(current_enemy)
                if target.get_info() in paths:
                    continue
                paths[target.get_info()] = path
            elif current_enemy.get_coordinates() not in visited:
                x, y = current_enemy.get_coordinates()
                possible_routes = list()
                for _x, _y in [(x-1, y),(x, y-1), (x, y+1), (x+1, y)]:
                    if maze[_x][_y] == CAVERN:
                        possible_routes.append(Enemy(enemy.type, _x, _y))
                for possible_route in possible_routes:
                    new_path = list(path)
                    new_path.append(possible_route)
                    stack.append(new_path)
                visited.add(current_enemy.get_coordinates())
        if len(paths) == 0:
            return enemy
        path = paths[sorted(paths.keys(), key=lambda x: (len(paths[x]), paths[x][-1].x, paths[x][-1].y))[0]]
        x, y = path[0].get_coordinates()
        maze[x][y] = CAVERN
        x, y = path[1].get_coordinates()
        maze[x][y] = enemy.type
        enemy.x, enemy.y = x, y
        return enemy

    def get_enemy_to_attack(self, enemy):
        x, y, c = enemy.get_info()
        possible_coordinates = [(x-1, y), (x, y-1), (x, y+1),(x+1, y)]
        possible_enemies = list()
        for en in self.enemies:
            if (en.x, en.y) in possible_coordinates and en.type == c and en.hp > 0:
                possible_enemies.append(en)
        possible_enemies.sort(key=lambda x: (x.hp, x.x, x.y))
        return possible_enemies[0]
    
    def attack(self, enemy, target):
        global ELF_DIES
        target.hp -= enemy.dmg
        if target.hp <= 0:
            x, y = target.x, target.y
            maze[x][y] = CAVERN
            if target.type == ELF:
                ELF_DIES = True

    def print_list(self, l):
        for enemy in l:
            print(enemy.x,enemy.y, enemy.type, enemy.hp)

    def print_enemies(self):
        for enemy in self.enemies:
            print(enemy.x,enemy.y, enemy.type, enemy.hp)

    def simulate(self):
        while self.has_enemies():
            self.round += 1
            self.enemies.sort()
            for enemy in self.enemies:
                if enemy.hp <= 0:
                    continue
                if not self.has_enemies():
                    self.round -= 1
                    break
                if not self.has_enemy_in_range(enemy):
                    enemy = self.make_move(enemy)
                if not self.has_enemy_in_range(enemy):
                    continue
                nearest_enemy = self.get_enemy_to_attack(enemy)
                self.attack(enemy, nearest_enemy)

    def get_result(self):
        hp_sum = sum([enemy.hp for enemy in self.enemies if enemy.hp>0])
        return hp_sum * self.round


def main():
    global ELF_DIES, ELF_DAMAGE
    battle = Battle("input.txt")
    battle.simulate()
    while ELF_DIES:
        ELF_DAMAGE += 1
        ELF_DIES = False
        battle = Battle("input.txt")
        battle.simulate()
        print(battle.get_result())

if __name__ == "__main__":
    main()
