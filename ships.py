#Чуть не додел до конца
#Делал по аналогии с разбором задачи в вебинаре
#С наступившим новым годом!







class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Ship:
    def __init__(self, lenght, dot, direct):
        self.length = lenght
        self.dot = dot
        self.direct = direct
        self.health = length

    def dot(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.dot.x
            cur_y = self.dot.y
            if self.direct == 0:
                cur_x += i
            elif self.direct == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots
    def damage(self, shot):
        return shot in self.dot

class Board:
    def __init__(self,  size = 6):
        self.size = size
        self.count = 0
        self.busy = []
        self.ships = []

        self.field = [ ["O"]*size for _ in range(size) ]
    def __str__(self):
        pole = ''
        pole += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            pole += f"\n{i + 1} | " + " | ".join(row) + " |"
        return pole

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, flag=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if flag:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "*"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()
        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.health -= 1
                self.field[d.x][d.y] = "X"
                if ship.health == 0:
                    self.count += 1
                    self.contour(ship, flag = True)
                    pritn("Корабль потоплен")
                else:
                    pritn("Ранен")
                    return True
        self.field[d.x][d.y] = "."
        print("Промах")
        return False


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)
class AI(Player):
    def ask(self):
        dot = Dot(randint(0,5), randint(0, 5))
        print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return dot


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите число")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

