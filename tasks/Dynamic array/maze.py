class Maze:
    def __init__(self, chikei):
        self.mapping = chikei

    # 指定箇所が壁かどうかの判定
    def is_wall(self, x: int, y: int) -> bool:
        if self.mapping[x - 1][y - 1] == "#":
            return True
        else:
            return False


# 迷路の設定
s = ["..#.", "#.##", "...."]

# 判定箇所の指定
r = 1
c = 2

my_maze = Maze(s)
if my_maze.is_wall(r, c):
    print("YES")
else:
    print("NO")
