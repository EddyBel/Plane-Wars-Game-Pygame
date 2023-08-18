<h1 align="center">Plane Wars (Game Pygame)</h1>

![Preview](https://img.shields.io/github/last-commit/EddyBel/Plane-Wars-Game-Pygame?color=%23AED6F1&style=for-the-badge)
![Preview](https://img.shields.io/github/license/EddyBel/Plane-Wars-Game-Pygame?color=%23EAECEE&style=for-the-badge)
![Preview](https://img.shields.io/github/languages/top/EddyBel/Plane-Wars-Game-Pygame?color=%23F9E79F&style=for-the-badge)
![Preview](https://img.shields.io/github/languages/count/EddyBel/Plane-Wars-Game-Pygame?color=%23ABEBC6&style=for-the-badge)
![Preview](https://img.shields.io/github/languages/code-size/EddyBel/Plane-Wars-Game-Pygame?color=%23F1948A&style=for-the-badge)

<p align="center" >
    <img src="./assets/docs/Preview_1.png" />
    <img src="./assets/docs/Preview_2.png" />
    <img src="./assets/docs/Preview_3.png" />
</p>

This pygame is based on a spaceship that has to dodge and destroy asteroids. The player has a life bar and a destroyed asteroid counter, pilot your ship and see how long you can survive in this challenging outer space!

## Why did I build this game?

This game was built as a practice project to learn Python and the Pygame library. It seemed like a fun way to deepen my knowledge of these technologies while creating something fun and challenging. Although the game is simple, I hope it serves as a good example of how to implement some of the basic features of Pygame, such as the main screen, event handling, and collision.

## Features

- [x] The game is written in Python and uses the Pygame library for the graphical interface and event handling.
- [x] The player can move through the arrow keys and shoot with the space bar.
- [x] The asteroids move towards the ship and regenerate as they leave the screen.
- [x] If the ship collides with an asteroid, the player's life bar decreases. If the life bar reaches zero, the game is over.
- [x] The counter of destroyed asteroids is increased each time the player destroys an asteroid with a shot.

# Future features

While the game is already fun and challenging, there are some additional features that I would like to add in the future:

- [ ] **Start menu**: A home screen that allows the player to start the game, view high scores or access settings.
- [ ] **Best Scores**: A table of the best scores obtained by the players.
- [ ] **Collision system improvement**: Currently, the ship simply disappears when it collides with an asteroid. I would like to improve this with visual effects and a smoother transition to the finished game screen.
- [ ] **Destruction effects**: When destroying the ship or asteroids, I would like to add visual effects to make the game even more exciting.
- [ ] **Different difficulties and game modes**: I would like to add different game modes, such as an easier difficulty or an endless mode, so that players can choose how they want to play.
- [ ] **New levels**: It would be fun to add new levels with additional obstacles and challenges as the player progresses through the game.

# Steps to run the project

First we must clone the repository on the computer and move it to the project folder.

```sh
git clone https://github.com/EddyBel/Plane-Wars-Game-Pygame.git
cd Plane-Wars-Game-Pygame
```

For the following it is necessary to have python virtualenv installed, if you don't have it you can install it with the following command.

```sh
pip install virtualenv
```

Then you can create the virtual environment where the script will run and we will have our dependencies, the virtual environment can have the name you like for example we will use **"env "** as the name of the environment.

```sh
python -m venv env
```

Now we can activate and enter our virtual environment, for each operating system is different, but always starts entering the folder with the name of the virtual environment created and would be as follows.

> ### Windows
>
> ```sh
> ./env/Script/activate
> ```

> ### Linux
>
> ```sh
> source ./env/bin/activate
> ```

Once inside our virtual environment we can install all the necessary dependencies stored in the requeriments.txt file.

```sh
pip install -r .\requeriments.txt
```

The only thing left to do is to run the game, the main file of the game is named **main.py**, and we can run it as follows.

```sh
python _init_.py
```

# Technologies used

- Python
- Pygame
