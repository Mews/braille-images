
# Braille Image Generator

![Logo](https://i.ibb.co/1rR3qGw/braille-images.png)

#### A python app that converts images to text using braille characters, such as
```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠶⠾⠿⠿⠿⠿⠿⠿⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠾⠿⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠿⠧⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠷⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠤⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠾⠿⠿⠿⠿⠿⠿⠿⠿⠀⠰⠶⠶⠶⠦⠀⠀
⠀⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠸⠿⠿⠿⠿⠧⠀
⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠸⠿⠿⠿⠿⠿⠆
⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠏⠀⠾⠿⠿⠿⠿⠿⠇
⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠼⠿⠿⠿⠿⠿⠿⠿
⠿⠿⠿⠿⠿⠿⠿⠟⠁⠠⠤⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⠿⠿⠿⠿⠿⠿⠿⠿
⠿⠿⠿⠿⠿⠿⠿⠀⠰⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇
⠸⠿⠿⠿⠿⠿⠿⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠁
⠀⠻⠿⠿⠿⠿⠿⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠋⠀
⠀⠀⠙⠻⠿⠿⠟⠀⠿⠿⠿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠷⠤⠤⠤⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⠸⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠻⠿⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

# Features

- A fully featured GUI to visualize the output and make changes live
    - ![GUI](https://i.ibb.co/ysPDnZG/Screenshot-2024-05-05-185401.png)
- A command line interface available via `py -m braille-images`
## Usage

> Before using the app, you must install its dependencies by running `pip install -r requirements.txt`

To open the GUI simply open the `run.cmd` file, or alternatively run `py main.py`

To use the command line interface run `py braille-images -h` for info on how to use it

If you have any issues using the app feel free to contact me through [my discord!](https://discord.com/users/467268976523739157)