from pathlib import Path
from typing_extensions import Annotated

import typer

# these options all come from Click:
#  https://click.palletsprojects.com/en/8.1.x/parameters/
# Cf: click.Path
def main(
    config: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    text = config.read_text()
    print(f"config: {text}")


if __name__ == "__main__":
    typer.run(main)
