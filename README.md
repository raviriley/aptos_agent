# Aptos Agent

## Initial Setup

### Python & Poetry

We're currently using Python 3.10.
We use [Poetry](https://python-poetry.org/docs/) for Python dependency management.
Ensure you have Python 3.10.\* installed and set up, along with Poetry.
Click [here](https://python-poetry.org/docs/#installation) for Poetry installation instructions.

### Getting Started

The first thing you should do after cloning this repo is install the Poetry dependencies by running `poetry install`.
Once you have the dependencies installed, you can now spawn a virtualenv shell by running `poetry shell`.
Whenever working on the project you should always use the `poetry shell`.

## Running the code

If running any of these commands **outside** of the Poetry shell, prepend `poetry run `. For example, dev would be `poetry run dev`.

| Command                    | Description                                  |
| -------------------------- | -------------------------------------------- |
| `dev` / `d`                | Runs the agent                               |
| `format` / `f`             | Automatically formats code and sorts imports |
| `lint` / `l`               | Lints code and checks for any issues         |
| `test` / `t`               | Runs the tests                               |
| `format-lint` / `fl`       | Runs `format` then `lint`                    |
| `format-lint-test` / `flt` | Runs `format`, `lint`, and `test`            |
