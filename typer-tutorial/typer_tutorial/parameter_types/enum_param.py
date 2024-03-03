from enum import Enum
from typing_extensions import Annotated

import typer


class BikeBrands(str, Enum):
    ktm = "KTM"
    husky = "Husky"
    bmw = "BMW"


def main(bike: Annotated[BikeBrands, typer.Option(case_sensitive=False)] = BikeBrands.ktm):
    print(f"{bike} is the best motorcycle brand ever in the history of the world!")


if __name__ == "__main__":
    typer.run(main)
