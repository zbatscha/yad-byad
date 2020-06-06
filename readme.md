# Yad B'Yad

http://yadbyad.herokuapp.com/

## Inspiration
This web app was created as an interactive art piece for the ‘Words as Objects’ (VIS 321) course in Visual Arts taught by Professor Scanlan at Princeton University.

The popular web game geoguessr and the Jewish Torah pointer (yad) served as inspirations. The torah scroll, unlike the hardcopy classics, is a linear text, and the yad (beyond other purposes) serves to spotlight a single word at a time.

## How It Works

Much like geoguessr does with greographical location, yadbyad is a trivia game that places the user at a random word within a random novel (among a library of the top 100 classics sourced from Project Gutenberg). Moving word by word through the text, either forward or backward, it's up to the user to guess the world they've been thrown into, with as few moves as possible!

Think you know the classics? Give it a shot at http://yadbyad.herokuapp.com/.

# Install

    $ git clone https://github.com/zbatscha/yad-byad.git
    $ cd yad-byad
    $ python -m venv venvYad
    $ . venvYad/bin/activate
    (venvYad) $ pip install -r requirements.txt 
    (venvYad) $ python run.py port

For example, if port is set to 5000, go to http://localhost:5000.
