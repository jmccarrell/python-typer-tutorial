# method 2 to parse custom types is to call down through click
# Cf:
# https://typer.tiangolo.com/tutorial/parameter-types/custom-types/#click-custom-type
# https://click.palletsprojects.com/en/8.1.x/parameters/#implementing-custom-types

import click
import typer
from typing_extensions import Annotated


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"<CustomClass: value={self.value}>"


class CustomClassParser(click.ParamType):
    name = "CustomClass"

    def convert(self, value, param, ctx):
        return CustomClass(value * 3)


def main(
    custom_arg: Annotated[CustomClass, typer.Argument(click_type=CustomClassParser())],
    custom_opt: Annotated[CustomClass, typer.Option(click_type=CustomClassParser())] = "KTM",
):
    print(f"custom arg: {custom_arg}")
    print(f"--custom-opt: {custom_opt}")


if __name__ == "__main__":
    typer.run(main)
