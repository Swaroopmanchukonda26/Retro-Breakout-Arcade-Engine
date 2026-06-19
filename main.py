import turtle
import time

# --- CONSTANTS & CONFIGURATION ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 40
BALL_INITIAL_SPEED = 3

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#4cc9f0")
        self.shapesize(stretch_wid=1, stretch_len=6)  # Create a horizontal paddle
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        new_x = self.xcor() - PADDLE_SPEED
        if new_x > -330:  # Stay inside screen boundaries
            self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + PADDLE_SPEED
        if new_x < 330:
            self.setx(new_x)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#f72585")
        self.penup()
        self.goto(0, -100)
        self.x_move = BALL_INITIAL_SPEED
        self.y_move = BALL_INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # Reverse vertical trajectory direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse horizontal trajectory direction

    def reset_position(self):
        self.goto(0, -100)
        self.bounce_y()

class Brick(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2.5)  # Brick dimensions
        self.penup()
        self.goto(x, y)

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-350, 260)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 14, "bold"))

    def increment(self):
        self.score += 10
        self.update_score()
        
    def game_over(self, won=False):
        self.goto(0, 0)
        msg = "🏆 YOU WIN! 🏆" if won else "💥 GAME OVER 💥"
        self.write(msg, align="center", font=("Courier", 24, "bold"))

# --- MAIN ENGINE LOOP GAMEPLAY ---
def run_game():
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("#111116")
    screen.title("Retro Python Breakout Engine")
    screen.tracer(0)  # Turns off automatic screen refreshing for smooth rendering

    # Instantiate Actors
    paddle = Paddle()
    ball = Ball()
    scoreboard = Scoreboard()

    # Build the Grid Matrix Matrix Array of Bricks
    colors = ["#7209b7", "#3f37c9", "#4361ee", "#4cc9f0"]
    bricks = []
    for row_idx, y_pos in enumerate(range(200, 100, -25)):
        row_color = colors[row_idx % len(colors)]
        for x_pos in range(-360, 390, 60):
            brick = Brick(x_pos, y_pos, row_color)
            bricks.append(brick)

    # Event Key Listeners Bindings
    screen.listen()
    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "Right")

    game_is_on = True
    while game_is_on:
        time.sleep(0.01)  # Limits frame iterations speed
        screen.update()    # Manually updates the display canvas
        ball.move()

        # 1. Detect Outer Wall Collisions
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
        if ball.ycor() > 280:
            ball.bounce_y()

        # 2. Detect Bottom Out / Life Loss
        if ball.ycor() < -280:
            ball.reset_position()
            # Optional: Deduct life score points here

        # 3. Detect Paddle Intersection Collisions
        if ball.ycor() == -240 and ball.y_move < 0:
            if paddle.xcor() - 65 < ball.xcor() < paddle.xcor() + 65:
                ball.bounce_y()

        # 4. Detect Brick Matrix Collisions
        for brick in bricks:
            if ball.distance(brick) < 28:
                brick.goto(2000, 2000)  # Teleport brick off-screen safely
                bricks.remove(brick)
                ball.bounce_y()
                scoreboard.increment()
                break  # Break loop to process one hit per frame update

        # 5. Check Win Condition
        if not bricks:
            screen.update()
            scoreboard.game_over(won=True)
            game_is_on = False

    screen.mainloop()

if __name__ == "__main__":
    run_game()
