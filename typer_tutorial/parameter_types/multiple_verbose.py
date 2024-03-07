# show how to count up the number of --verbose on the command line
import typer
from typing_extensions import Annotated


def main(verbose: Annotated[int, typer.Option("--verbose", "-v", count=True)] = 0):
    print(f"verbosity is level: {verbose}")


if __name__ == "__main__":
    typer.run(main)
