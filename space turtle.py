import turtle
import random
import time

# Set up the game window
wn = turtle.Screen()
wn.title("Space Invaders")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# Create the player's spaceship
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=2)
player.penup()
player.goto(0, -250)

player_speed = 15

# Create player's bullets
bullets = []

def fire_bullet():
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
    bullet.penup()
    bullet.goto(player.xcor(), player.ycor() + 10)
    bullet.dy = 5

    bullets.append(bullet)

# Keyboard bindings
wn.listen()
wn.onkeypress(fire_bullet, "space")

# Create alien invaders
enemies = []

for _ in range(5):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-350, 350)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemy.dx = 1
    enemy.dy = 30

    enemies.append(enemy)

enemy_speed = 2

# Define functions for player movement
def move_left():
    x = player.xcor()
    if x > -380:
        x -= player_speed
    player.setx(x)

def move_right():
    x = player.xcor()
    if x < 380:
        x += player_speed
    player.setx(x)

# Keyboard bindings
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Initialize score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.hideturtle()

# Function to check for collisions
def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 15:
        return True
    return False

# Main game loop
while True:
    wn.update()

    # Move the player's bullets
    for bullet in bullets:
        y = bullet.ycor()
        y += bullet.dy
        bullet.sety(y)

        # Check if the bullet has gone out of the screen
        if y > 275:
            bullet.hideturtle()
            bullets.remove(bullet)

    # Move the alien invaders
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy.dx
        enemy.setx(x)

        # Move the enemies down and change direction when they reach the screen's edge
        if x > 380 or x < -380:
            for e in enemies:
                y = e.ycor()
                y -= enemy.dy
                e.sety(y)
                e.dx *= -1

        # Check for collisions between bullets and aliens
        for bullet in bullets:
            if is_collision(bullet, enemy):
                bullet.hideturtle()
                bullets.remove(bullet)
                enemy.hideturtle()
                enemies.remove(enemy)
                score += 10
                score_display.clear()
                score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check for game over conditions
    for enemy in enemies:
        if enemy.ycor() < -240:
            for e in enemies:
                e.hideturtle()
            game_over_display.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
            time.sleep(2)
            wn.bye()
