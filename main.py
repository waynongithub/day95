from turtle import Screen, register_shape
from bullet import Bullet
from bomb import Bomb
from player import Player
from ufo import UFO
from score import Score
from line import Line
import time
import random


nc = "\033[0;97m"
red = "\033[0;91m"
green = "\033[0;92m"
blue = "\033[0;96m"
yellow = "\033[0;93m"
lilac = "\033[0;95m"


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0) # speeds up setting up the board
screen.listen()

# register shapes
# register_shape('images/alien.gif')
# register_shape('images/explode.gif')
# player.shape('images/rocket.gif')
# bullet = Bullet(0)
def end_game():
    screen.bgcolor('coral')


# bullet = Bullet()
# player = Player()
score = Score(level=1, ufos_destroyed=0)
players = []
ufos = []
bombs = []

line = Line()
baseline = -200
ufo_size = 26
shooting_chance = 10

limit_left = -380
limit_right = 380
bottom_row = 180
do_switch = False
do_drop = False
ufo_hit = False


def place_ufos():
    # for y in (270, 240, 210, 180):
    global ufos
    ufos = []
    for y in (240, 210, 180):
        for x in range(-250, 270, 80):
            # print(f"ufo {x}, {y}")
            ufos.append(UFO((x, y)))
# screen.tracer(3)


for i in range(0, score.lives_left):
    players.append(Player())

player = players.pop(-1)
player.goto(0, baseline)

def clear_players(players):
    for player in players:
        player.clear()

def draw_players(players):
    for i, rocket in enumerate(players):
        rocket.ycor = -270
        rocket.xcor = -380 + (i * 50)
        rocket.goto(rocket.xcor, rocket.ycor)


active_bullet = False
shot_fired = False


def shoot():
    global shot_fired
    shot_fired = True


def ufo_drop_bomb(idx, ufo):
    can_shoot = True
    if ufo.ycor < 350:
        if idx < 7:
            if ufos[idx + 7].ycor < 400 or ufos[idx + 14].ycor < 400:
                can_shoot = False
        elif idx < 14:
            if ufos[idx + 7].ycor < 400:
                can_shoot = False
        if can_shoot:
            rd = random.choice(range(0, 500))
            if rd == 17:
                bombs.append(Bomb(ufo.xcor, ufo.ycor))


place_ufos()
draw_players(players)


def kees():
    screen.onkey(key="z", fun=end_game)
    screen.onkey(key="Left", fun=player.move_left)
    screen.onkey(key="Right", fun=player.move_right)
    screen.onkey(key="space", fun=shoot)

kees()

print(f"lives left={score.lives_left}")
while score.lives_left > 0:
    screen.update()

    if shot_fired:
        shot_fired = False
        if not active_bullet:
            bullet = Bullet(player.xcor())
            active_bullet = True

    if active_bullet:
        bullet.move()
        if bullet.ycor() > 300:
            # https://stackoverflow.com/questions/43972351/how-to-fully-delete-a-turtle
            bullet.reset()
            active_bullet = False

    if active_bullet:
        print("there is an active bullet")
        if bullet.ycor() > 160:
            for ufo in ufos:
                if ((ufo.ycor - ufo_size) <= bullet.ycor() <= (ufo.ycor + ufo_size)) and (
                        ufo.xcor - ufo_size <= bullet.xcor() <= ufo.xcor + ufo_size) and bullet.y_move > 0:
                    print(f"{lilac}kaboooom{nc}")
                    ufo_hit = True

                    ufo.got_hit()
                    bullet.reset()
                    active_bullet = False
                    score.ufo_destroyed()
                    if score.ufo_destroyed_in_current_level == 21:
                        score.next_level()
                        place_ufos()
    time.sleep(0.017)

    leftmost = 0
    rightmost = 0
    bottom = 300

    for idx, ufo in enumerate(ufos):
        ufo_drop_bomb(idx, ufo)
        if ufo_hit:
            ufo.step = ufo.step + 0.1
        ufo.move(do_switch, do_drop)
        if ufo.ycor < 400:
            if ufo.xcor < leftmost:
                leftmost = ufo.xcor
            if ufo.xcor > rightmost:
                rightmost = ufo.xcor
            if ufo.ycor < bottom:
                bottom = ufo.ycor

    ufo_hit = False
    if leftmost < limit_left or rightmost > limit_right:
        do_switch = True
    else:
        do_switch = False

    if bottom_row < bottom:
        do_drop = True
    else:
        do_drop = False

    for bomb in bombs:
        bomb.move()
        if bomb.ycor() < baseline - 32:
            bombs.remove(bomb)
            bomb.reset()
        # elif bomb.ycor() <= baseline and (player.xcor() - 10 <= bomb.xcor() <= player.xcor() + 10):
        elif bomb.ycor() <= baseline and (player.xcor() - 20 <= bomb.xcor() <= player.xcor() + 20):
            score.player_dead()
            bomb.goto(200, -290)
            bomb.reset()
            print(f"{yellow}I'M DEAAAAAAD !!!!!! {nc}")
            if len(players) > 0:
                players[-1].goto(-300,500)
                players[-1].clear()
                players.pop(-1)

        else:
            if active_bullet:
                if (bomb.ycor() - 10) <= bullet.ycor() <= (bomb.ycor() + 10) and (bomb.xcor() - 10 <= bullet.xcor() <= bomb.xcor() + 10):
                    bombs.remove(bomb)
                    bomb.reset()
                    bullet.reset()


    if score.lives_left == 0:
        score.game_over()

screen.exitonclick()
print(f"after the while loop")

# TODO pressing space fires new bullet
# TODO bullet disappears when it hits a ufo or when it leaves the board
# TODO can only fire when previous bullet has disappeared
# TODO load enemies
# TODO enemies move left and right
# TODO if lower line of enemies is destroyed, the block moves lower
# TODO enemies move down with every swing
# TODO hit enemies
# TODO with every hit, enemies move faster
# TODO enemies drop bombs: when? how many?
# TODO Only the ones that have no lower neighbour drop bombs
# TODO Bombs should not hit ufos => faster ufo => faster dropspeed
# TODO bombs kill player
# TODO boss ufo
# TODO shelters: partially destroyed with every hit
# TODO keep score
# TODO levels