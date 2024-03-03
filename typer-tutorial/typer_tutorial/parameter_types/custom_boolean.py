# show accept/reject instead of accept/no-accept for a boolean
from typing import Union

import typer
from typing_extensions import Annotated

def main(accept: Annotated[Union[bool, None], typer.Option("--accept/--reject", "-a/-r")] = None):
    print(f"accept: {accept}")

if __name__ == "__main__":
    typer.run(main)
