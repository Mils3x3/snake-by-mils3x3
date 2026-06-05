class SnakeControl:
    def __init__(self, snake_body_parameter):
        self.snake_body = snake_body_parameter
        self.can_turn = True
        self.queued_heading = None

    def clear_control_state(self):
        self.can_turn = True
        self.queued_heading = None

    def turn(self, new_heading, opposite_heading):
        current_heading = self.snake_body[-1].heading()

        if self.can_turn:
            if current_heading != opposite_heading:
                self.snake_body[-1].setheading(new_heading)
                self.can_turn = False
        else:
            self.queued_heading = new_heading

    def reset_turn(self):
        self.can_turn = True

        if self.queued_heading is not None:
            current_heading = self.snake_body[-1].heading()

            if abs(current_heading - self.queued_heading) != 180:
                self.snake_body[-1].setheading(self.queued_heading)
                self.can_turn = False

            self.queued_heading = None

    def go_up(self):
        self.turn(90, 270)

    def go_down(self):
        self.turn(270, 90)

    def go_left(self):
        self.turn(180, 0)

    def go_right(self):
        self.turn(0, 180)