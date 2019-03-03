# Example library for yapf custom style defaults

[YAPF](https://github.com/google/yapf) is a great project with a noble goal: to provide a functional, flexible, and configurable Python code formatter. I've enjoyed using yapf and have customized my style.yapf to the point where it consistently does what I want.

## Problem

Now that I've succeeded, I'd like to share this configuration with friends, colleagues, and the world! Unfortunately, as of yapf version 0.26.0, any default styles require a pull request to the actual yapf codebase. Default styles are hard-coded in "yapflib/style.py" with 4 options: pep8, Google, Chromium, and Facebook. Since "Sam Roeca" is probably not large enough to deserve a place in this codebase, the YAPF designers have forced me to do one of 3 things:

1. Accept that I will need to share a fairly specific, non-versioned configuration file that is bound to change with my preferences over time.
2. Refactor the yapf codebase to accept plugins. Given its current design, this would take some time.
3. Become a wizard and dig into the dark magic of imports, namespaces, and mutations.

For both fun and practical reasons, I've chosen the wizard approach.

This codebase takes advantage of Python's darker truths to insert my own custom style (named "sam_roeca") into a version-able, distributable Python package. On one hand, the code is pretty short. On the other hand, it may not survive a major, or even minor, version update from the yapf maintainers. My code relies on "private" values to make its magic. This leaves me undeterred; I welcome a day when the yapf maintainers revisit code in yapflib/style.py. When that day comes, they may even expose a plugin interface to make this dark magic unnecessary.

## Installation

This isn't currently hosted on pypi. If you want it, clone this repo and from this directory, run:

```bash
poetry install
```

The install command creates a binary in your path called "sam-yapf". It's an alternative to yapf's default binary that adds the "sam_roeca" style as an available default. Everything else remains intact.

To test out my lovely formatter, run the following commands:

```bash
poetry run sam-yapf --help
poetry run sam-yapf test.py
```

The first prints a help message while the second formats the test script.

## How it works

Everything is done in 1 of 2 files: sam_yapf.py and pyproject.toml.

### sam_yapf.py

Python only executes modules once: on import. I import the modules I care about and then mutate the module's mutable value to my own end.

Note: as mentioned in the introduction, I'm relying on some private (eg, "_...") variables. This is normally frowned upon. If there are any non-pull-request alternatives to my approach, please create an issue with your suggested path forward.

### pyproject.toml

If you're not using [poetry](https://github.com/sdispater/poetry), you should be.

This file is basically setup.py. In fact, under the hood, poetry translates it into setup.py. Basically, poetry's author realized that Rust's [cargo](https://github.com/rust-lang/cargo) is the cat's meow and finally managed to implement a sane dependency manager / build tool for Python. My hat is off to Sébastien Eustace for finally making me love building Python libraries.

This line basically creates the executable script:

```toml
[tool.poetry.scripts]
sam-yapf = "sam_yapf:MAIN_SCRIPT"
```

## Written by

Samuel Roeca *samuel.roeca@gmail.com*
