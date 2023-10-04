from direction import Direction, Down, Left, Right, Up
from position import Position


class Snake:
    def __init__(self) -> None:
        self._position_list: list[Position] = [Position(x=3, y=8), Position(x=2, y=8)]
        self.direction: Direction = Right()
        self.prev_direction: Direction = Right()
        pass

    def move(self) -> None:
        self._position_list.insert(0, self.next_position)
        self._position_list.pop()
        self.prev_direction = self.direction

    # prev_directionの方向に進む
    def move_according_to_inertia(self) -> None:
        self._position_list.insert(0, self.head + self.prev_direction.delta)
        self._position_list.pop()

    def up(self) -> None:
        self.direction = Up()

    def down(self) -> None:
        self.direction = Down()

    def left(self) -> None:
        self.direction = Left()

    def right(self) -> None:
        self.direction = Right()

    def grow(self) -> None:
        self._position_list.insert(0, self.next_position)

    @property
    def position_list(self) -> list[Position]:
        return self._position_list

    @property
    def head(self) -> Position:
        return self._position_list[0]

    @property
    def body(self) -> list[Position]:
        return self._position_list[1:]

    @property
    def next_position(self) -> Position:
        return self.head + self.direction.delta
