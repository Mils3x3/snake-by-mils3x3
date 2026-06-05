import time


def save_snake_positions(snake):
    return [(segment.xcor(), segment.ycor()) for segment in snake.body]


def restore_snake_positions(snake, saved_positions, saved_heading):
    for segment, position in zip(snake.body, saved_positions):
        segment.goto(position)

    snake.body[-1].setheading(saved_heading)


def wait_for_safe_direction(my_screen, snake, snake_control, crash_message, safe_headings):
    selected_heading = None

    def remove_all_controls():
        my_screen.onkeypress(None, "Up")
        my_screen.onkeypress(None, "Down")
        my_screen.onkeypress(None, "Left")
        my_screen.onkeypress(None, "Right")

        my_screen.onkeyrelease(None, "Up")
        my_screen.onkeyrelease(None, "Down")
        my_screen.onkeyrelease(None, "Left")
        my_screen.onkeyrelease(None, "Right")

        my_screen.onkeypress(None, "w")
        my_screen.onkeypress(None, "s")
        my_screen.onkeypress(None, "a")
        my_screen.onkeypress(None, "d")

        my_screen.onkeyrelease(None, "w")
        my_screen.onkeyrelease(None, "s")
        my_screen.onkeyrelease(None, "a")
        my_screen.onkeyrelease(None, "d")

        my_screen.onkeypress(None, "W")
        my_screen.onkeypress(None, "S")
        my_screen.onkeypress(None, "A")
        my_screen.onkeypress(None, "D")

        my_screen.onkeyrelease(None, "W")
        my_screen.onkeyrelease(None, "S")
        my_screen.onkeyrelease(None, "A")
        my_screen.onkeyrelease(None, "D")

    def choose_heading(new_heading):
        nonlocal selected_heading

        if selected_heading is not None:
            return

        if new_heading in safe_headings:
            selected_heading = new_heading
            snake.body[-1].setheading(new_heading)
            crash_message.clear_message()

    remove_all_controls()
    snake_control.clear_control_state()

    my_screen.onkeypress(lambda: choose_heading(90), "Up")
    my_screen.onkeypress(lambda: choose_heading(270), "Down")
    my_screen.onkeypress(lambda: choose_heading(180), "Left")
    my_screen.onkeypress(lambda: choose_heading(0), "Right")

    my_screen.onkeypress(lambda: choose_heading(90), "w")
    my_screen.onkeypress(lambda: choose_heading(270), "s")
    my_screen.onkeypress(lambda: choose_heading(180), "a")
    my_screen.onkeypress(lambda: choose_heading(0), "d")

    my_screen.onkeypress(lambda: choose_heading(90), "W")
    my_screen.onkeypress(lambda: choose_heading(270), "S")
    my_screen.onkeypress(lambda: choose_heading(180), "A")
    my_screen.onkeypress(lambda: choose_heading(0), "D")

    my_screen.listen()

    while selected_heading is None:
        my_screen.update()
        time.sleep(0.01)

    remove_all_controls()

    my_screen.onkeypress(snake_control.go_up, "Up")
    my_screen.onkeypress(snake_control.go_down, "Down")
    my_screen.onkeypress(snake_control.go_left, "Left")
    my_screen.onkeypress(snake_control.go_right, "Right")

    my_screen.onkeypress(snake_control.go_up, "w")
    my_screen.onkeypress(snake_control.go_down, "s")
    my_screen.onkeypress(snake_control.go_left, "a")
    my_screen.onkeypress(snake_control.go_right, "d")

    my_screen.onkeypress(snake_control.go_up, "W")
    my_screen.onkeypress(snake_control.go_down, "S")
    my_screen.onkeypress(snake_control.go_left, "A")
    my_screen.onkeypress(snake_control.go_right, "D")

    snake_control.clear_control_state()
    snake_control.can_turn = False


def get_next_position(snake, heading, setup):
    head_x = round(snake.body[-1].xcor())
    head_y = round(snake.body[-1].ycor())

    if heading == 0:
        head_x += setup.MOVE_DISTANCE
    elif heading == 90:
        head_y += setup.MOVE_DISTANCE
    elif heading == 180:
        head_x -= setup.MOVE_DISTANCE
    elif heading == 270:
        head_y -= setup.MOVE_DISTANCE

    return head_x, head_y


def is_inside_border(position, setup):
    x, y = position

    return (
        x <= setup.WIDTH / 2 - setup.MOVE_DISTANCE and
        x >= ((setup.WIDTH / 2) * -1) + setup.MOVE_DISTANCE and
        y <= setup.HEIGHT / 2 - setup.MOVE_DISTANCE and
        y >= ((setup.HEIGHT / 2) * -1) + setup.MOVE_DISTANCE
    )


def get_body_positions_that_stay(snake):
    body_positions = []

    for segment in snake.body[1:-1]:
        body_positions.append((round(segment.xcor()), round(segment.ycor())))

    return body_positions


def get_safe_headings(snake, setup):
    safe_headings = []
    possible_headings = [90, 270, 180, 0]
    body_positions = get_body_positions_that_stay(snake)

    for heading in possible_headings:
        next_position = get_next_position(snake, heading, setup)

        if not is_inside_border(next_position, setup):
            continue

        if next_position in body_positions:
            continue

        safe_headings.append(heading)

    return safe_headings