# one of two ways to provide your own type in an Typer app.
# in this case, our class parses its string input, and returns an instance of the class.

# cf: https://typer.tiangolo.com/tutorial/parameter-types/custom-types/#type-parser
import typer
from typing_extensions import Annotated


class CustomClass:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"<CustomClass: value:{self.value}>"


def parse_custom_class(value: str):
    return CustomClass(value * 2)


def main(
    custom_arg: Annotated[CustomClass, typer.Argument(parser=parse_custom_class)],
    custom_opt: Annotated[CustomClass, typer.Option(parser=parse_custom_class)] = "KTM",
):
    print(f"custom arg: {custom_arg}")
    print(f"--custom-opt: {custom_opt}")

if __name__ == "__main__":
    typer.run(main)
