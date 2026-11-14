# 📰 Fake News Headline Generator

A simple Python command-line project that generates random, humorous, fictional breaking-news headlines. It combines randomly selected subjects, actions, and places or situations to create a different headline each time.

> **Disclaimer:** This project is for learning and entertainment. The generated headlines are fictional and should not be treated as real news or factual claims.

## ✨ Features

-   Generates random headlines using predefined lists.
-   Combines a subject, an action, and a place or situation.
-   Uses a simple interactive command-line interface.
-   Lets users generate multiple headlines in one session.
-   Validates responses and handles invalid input.
-   Uses Python's built-in `random` module; no third-party packages are
    needed.

## 🛠️ Built With

-   **Python 3**
-   **`random` module** --- randomly selects headline elements.

## 📁 Project Structure

``` text
Fake-News-Headline-Generator/
│
├── main.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer. No external dependencies are required.

### Run the Project

1.  Clone the repository:

    ``` bash
    git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
    ```

2.  Move into the project directory:

    ``` bash
    cd Fake-News-Headline-Generator
    ```

3.  Run the program:

    ``` bash
    python main.py
    ```

    On some systems, use:

    ``` bash
    python3 main.py
    ```

## 💻 Example

The exact output changes because the program selects each headline element randomly.

``` text
Breaking News: Hania Aamir launches at Wagah Border

Do you want another headline? (yes/no): yes

Breaking News: A Group of Monkeys dances with inside Parliament

Do you want another headline? (yes/no): no

Thanks for using Fake News Headline Generator.
```

## ⚙️ How It Works

1.  The program imports Python's `random` module.
2.  It stores possible headline subjects, actions, and places or situations in three lists.
3.  The main loop uses `random.choice()` to select one item from each list.
4.  An f-string combines the selected items into a headline.
5.  The program asks whether the user wants another headline.
6.  If the response is `yes`, another headline is generated. If it is `no`, the program displays a closing message and exits.
7.  Any other response triggers an invalid-input message and the program asks again.

## 📚 Python Concepts Practiced

-   Importing a built-in module
-   Lists and string values
-   Random selection with `random.choice()`
-   `while` loops and nested loops
-   Conditional statements (`if`, `elif`, and `else`)
-   User input with `input()`
-   String formatting with f-strings
-   Input cleanup using `strip()` and `lower()`
-   Program termination with `exit()`

## 🎯 Project Purpose

This project is a beginner-level Python exercise for practicing basic programming concepts and building an interactive terminal application. It demonstrates how simple data collections, random selection, loops, and conditional logic can work together.

## 🔮 Possible Future Improvements

These are ideas for future versions and are **not currently implemented**:

-   Add more headline categories and selectable themes.
-   Let users choose how many headlines to generate.
-   Add an option to save generated headlines to a text file.
-   Improve headline grammar by adjusting combinations.
-   Add a graphical user interface.
-   Allow users to add their own subjects, actions, and places.

## 👤 Author

**Inam Ur Rehman**

-   GitHub:
    [@YOUR-GITHUB-USERNAME](https://github.com/fatalerror-404-app)


