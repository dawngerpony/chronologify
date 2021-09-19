# chronologify

A web application to create playlists of artists' tracks in chronological order.

## Technologies

- Python
- [Poetry][poetry] for dependency management and packaging

Soon:

- The [Flask][flask] web framework

## Getting started

### Installing prerequisites

1. Install PyCharm.
1. Install [Homebrew][homebrew].
1. [Install Poetry][poetry-install] via the recommended method.
1. At this point you might want to close and reopen your terminal.
1. Test the installation by running `poetry --version`. You should see something like this:

        Poetry version 1.1.6


### Setting up your project

Now that your prerequisites are configured, you can set up the project.

1. Clone this repository.
1. Open it in PyCharm.
1. Install Poetry dependencies:

        poetry install

1. Print the location of your Poetry virtual environment:

        poetry env info -p

1. Configure PyCharm to use the above virtualenv.
1. Close and reopen your terminal.

### How to run the tests

```shell
poetry run pytest
```

[flask]: https://flask.palletsprojects.com/en/2.0.x/#
[homebrew]: https://brew.sh
[poetry]: https://python-poetry.org
[poetry-install]: https://python-poetry.org/docs/#installation
