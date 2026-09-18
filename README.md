# Bookbot

BookBot is my first Boot.dev project!

This is a command tool I built in Python that takes a book file (.txt) and counts all the words inside it. It also looks through the whole book letter by letter to count how many times each letter shows up, then sorts them from the most common to the rarest so you get a neat breakdown of the text.

## Project Info
* **Unit:** Unit 03 — Build a Bookbot
* **Platform:** Built for my Boot.dev lessons

## How to Set It Up

Make sure you have Python 3 installed on your computer.

   Clone my repository to your machine:
   ```bash
   git clone <your-github-repository-url>
   ```
   Open up your terminal and jump into the project folder:
   ```bash
   cd Bookbot
   ```

## How to Run It

To check out the stats for a book, just run `main.py` in your terminal and type the path to the book file right next to it:

```bash
python3 main.py books/frankenstein.txt
```

### Running the Tests
If you want to run the automated tests and make sure all the math functions are working perfectly, you can run `pytest`:

```bash
pytest test_stats.py
```

## What the Output Looks Like

When you run the tool on a book, it prints out a nice, formatted dashboard in your terminal:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 85000 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
i: 24613
============= END ===============
```

## Credits
I made this as part of my Year 9 Computing Technology assignment using the concepts from the Boot.dev "Learn Python for Beginners", "Learn Linux" and "Build a Bookbot" courses.
