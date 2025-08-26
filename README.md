# Python Linear Algebra Toolkit

A Python project demonstrating fundamental linear algebra concepts, including solving systems of linear equations and applying 2D transformations like rotation and scaling. This project is structured to follow data science best practices, with a clear separation between source code and exploratory analysis in a Jupyter Notebook.

## Features

- **System of Equations Solver**: Compares exact solutions (`np.linalg.solve`) with least-squares approximations (`np.linalg.lstsq`).
- **2D Geometric Transformations**: Applies rotation, scaling, and composite transformations to a set of 2D points.
- **Clear Visualizations**: Uses Matplotlib to generate plots that clearly illustrate the effects of each transformation.
- **Modular Code**: Logic is separated into a `src` directory, making the code reusable and easy to understand.
- **Reproducible Environment**: A `requirements.txt` file is provided to ensure the project can be run on any machine.

## A Note on Professional Practices

Beyond the core linear algebra concepts, this project also serves as an learning exercise in professional software development and data science practices. Key practices include:

-   **Unit Testing**: The `tests/` directory contains unit tests for the core logic. This was implemented to ensure code correctness and as a self-directed learning exercise to showcase best practices in creating maintainable and reliable software.
-   **Modular and Reusable Code**: All core logic is refactored into the `src/` directory.
-   **Configuration Management**: Parameters are externalized into a `config.yaml` file.

## Installation

To get started with this project, clone the repository and set up a virtual environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/linear-algebra-toolkit.git
    cd linear-algebra-toolkit
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

All the analysis and visualizations are contained within the Jupyter Notebook.

1.  **Start Jupyter Lab or Jupyter Notebook:**
    ```bash
    jupyter lab
    # or
    jupyter notebook
    ```

2.  **Open the notebook:**
    Navigate to `notebooks/01-matrix-algebra-2D-transformations.ipynb` and run the cells to see the output.

## Project Structure

The project follows a streamlined structure to ensure clarity and reproducibility:

```
├── README.md               # The top-level README for developers using this project.
├── config.yaml             # Configuration file for parameters.
├── notebooks/              # Jupyter notebooks for analysis and exploration.
│   └── 01-matrix-algebra-2D-transformations.ipynb
├── requirements.txt        # The requirements file for reproducing the analysis environment.
├── src/                    # Source code for use in this project.
│   ├── __init__.py         # Makes src a Python module.
│   ├── linear_system.py    # Functions for solving linear systems.
│   ├── transformations.py  # Functions for applying geometric transformations.
│   └── visualization.py    # Functions for plotting.
└── tests/                  # Directory for unit tests.
    └── test_transformations.py
```
