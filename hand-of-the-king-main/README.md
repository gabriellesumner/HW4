# A Game of Thrones: Hand of the King

Play a two-player Python variant of [A Game of Thrones: Hand of the King](https://boardgamegeek.com/boardgame/205610/game-thrones-hand-king) with optional integration of artificial intelligence (AI).

***NOTE: This repository was created for learning purposes in CSC 3510 (Introduction to Artificial Intelligence) at Florida Southern College.***

## Requirements

The code provided here was developed in Python 3.9.5 on Windows 10 using VS Code and a Git Bash terminal. Setup and usage may vary slightly for other operating systems or software tools. The standard Python libraries should be sufficient for running the code. The only additional library (graphics.py) is provided in the repo.

In addition, the instructions that follow assume you have properly installed git on your machine. Click [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you need help doing that.

## Setup

The best way to use this code is to [clone the repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) to your local machine. To do so in VS Code, open a terminal and navigate to the parent directory of your choice using the `cd` command, e.g.:

    $ cd ~/Documents/csc3510

Then, use `git clone` to create a new subdirectory called wordle with the code from this repository:

    $ git clone https://github.com/meicholtz/hand-of-the-king

Go into the directory and make sure the appropriate files are there by using the `ls` command:

    $ cd hand-of-the-king
    $ ls

## Usage

Use the following commands to play the game:

- To play HOTK with two human players,

        $ python hand_of_the_king.py

- To play HOTK using an AI player (as player1, for example),

        $ python hand_of_the_king.py --player1 ai_player

    where ai_player is the name of any file that contains the function `get_computer_move(board, cards, banners)`.

- You can play human vs human, AI vs human, or AI vs AI.
