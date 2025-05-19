Got it\! Changing the `tsp_filepath` to a relative path makes your project more portable.

Here's how to update the `README` with a relative file path, assuming `berlin52.tsp` is located in a `data` folder one level up from where your script is running, or in the same directory.

-----

# Traveling Salesperson Problem (TSP) Solver using Genetic Algorithm

-----

This project tackles the classic **Traveling Salesperson Problem (TSP)** using a **Genetic Algorithm**. Imagine a salesperson who needs to visit a list of cities and return home, but they want to do it in the shortest way possible. That's the TSP, and our genetic algorithm is designed to find a super-efficient route\!

-----

## Features

  * **Smart Distance Calculator:** We figure out the exact straight-line distance between any two cities using their coordinates.
  * **Genetic Algorithm Powerhouse:** This is the core of our solution, mimicking natural selection to find the best paths:
      * **Starting Strong:** We kick things off with a bunch of random routes to form our initial "population."
      * **Route Reviewer (Fitness Function):** Each route is scored based on its total distance—shorter is better\!
      * **Picking the Best (Tournament Selection):** We hold mini-competitions to select the fittest routes as "parents" for the next generation.
      * **Mixing It Up (Order Crossover):** We combine parts of two good parent routes to create new, potentially even better "offspring" routes.
      * **Keeping It Fresh (Swap Mutation):** Every now and then, we randomly swap two cities in a route to introduce new possibilities and avoid getting stuck.
      * **Saving the Best (Elitism):** The absolute best routes from one generation automatically get a spot in the next, ensuring we never lose our progress.
  * **Easy Data Loading:** Our tool can read standard TSP data files (`.tsp` format) to grab city coordinates effortlessly.

-----

## Getting Started

### Prerequisites

To get this project up and running, you'll need **Python 3.x** and a few handy libraries:

  * `numpy` (for numerical operations)
  * `pandas` (for displaying data nicely)
  * `math` (Python's built-in math functions)
  * **`tsp_io`** (a custom module we use to read TSP files – make sure this file is with your main script\!).

You can install `numpy` and `pandas` like this:

```bash
pip install numpy pandas
```

***Important:** The `tsp_io.py` file, which contains the `read_tsp_coords` function, needs to be in the same folder as your main script.*

### Installation

1.  **Get the code:** You can either clone the repository (if it's on GitHub) or simply download all the project files into a folder.
    ```bash
    git clone <repository_url> # Replace with your repository URL
    cd <project_directory>
    ```
2.  **Verify `tsp_io.py`:** Double-check that `tsp_io.py` is right there in the same directory as your main Python file.

### How to Run

1.  **Prepare your TSP data:** You'll need a `.tsp` file (like `berlin52.tsp`, which is a classic example) that contains your city coordinates.

    **Place your `.tsp` file:**

      * If `berlin52.tsp` is in the **same directory** as your Python script, use:
        ```python
        tsp_filepath = 'berlin52.tsp'
        ```
      * If `berlin52.tsp` is in a folder named `data` **next to your script** (e.g., `your_project/data/berlin52.tsp`), use:
        ```python
        tsp_filepath = 'data/berlin52.tsp'
        ```
      * If `berlin52.tsp` is in a folder named `tsp_files` **inside your script's directory**, use:
        ```python
        tsp_filepath = 'tsp_files/berlin52.tsp'
        ```

    **Update the `tsp_filepath` variable in the `if __name__ == "__main__":` section of your script accordingly.** For this README, let's assume it's in a `data` folder:

    ```python
    tsp_filepath = 'data/berlin52.tsp'
    ```

    **Remember to change this path to match the relative location of your `.tsp` file\!**

2.  **Execute the script:** Open your terminal or command prompt, navigate to your project directory, and run:

    ```bash
    python your_script_name.py # Replace 'your_script_name.py' with the actual name of your Python file
    ```

You'll see output showing the cities loaded, a peek at the calculated distances, and finally, the best tour and its total distance that our genetic algorithm discovered\!

-----

## Fine-Tuning the Algorithm

Want to tweak how the genetic algorithm works? You can adjust these parameters in the `if __name__ == "__main__":` block:

  * **`POPULATION_SIZE`**: How many different routes are considered in each generation.
  * **`NUM_GENERATIONS`**: How many times the algorithm iterates to evolve better solutions.
  * **`TOURNAMENT_SIZE`**: The number of routes competing when selecting parents.
  * **`CROSSOVER_RATE`**: The chance that two parent routes will combine to make a new one.
  * **`MUTATION_RATE`**: The probability that a small, random change will occur in a route.
  * **`ELITE_SIZE`**: The number of top-performing routes that automatically carry over to the next generation.

<!-- end list -->

```python
    POPULATION_SIZE = 100
    NUM_GENERATIONS = 1100
    TOURNAMENT_SIZE = 4
    CROSSOVER_RATE = 0.85
    MUTATION_RATE = 0.33
    ELITE_SIZE = 2
```

Playing around with these values can have a big impact on how quickly and effectively the algorithm finds a great solution\!

-----
