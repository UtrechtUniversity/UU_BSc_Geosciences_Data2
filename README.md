# Data and Statistics course for the BSc in Geosciences at UU

## Running instructions without Spyder

To make sure the dependencies are in place, use a virtual environment. First install the dependencies (needed only once or after changing them):

```
poetry install
```
Then enter the venv using:

```
poetry shell
```

After this you can run the script, either directly in a Python REPL or in an IDE, e.g. by starting VS Code from inside the venv:

```
code .
```

To publish the script, run:

```
quarto render $FILENAME
```