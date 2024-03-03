import typer
from typing_extensions import Annotated

def main(
    name: Annotated[str, typer.Argument(envvar="GREET_NAME", help="Name to extend greetings to")] = "Dianne",
    formal: Annotated[bool, typer.Option(help="formally greet")] = False,
):
    """
    Say hi to NAME.
    If --formal is used, speak more formally.
    """
    greeting: str = "Good day {name}" if formal else "Hiya {name}"
    print(greeting.format(name=name))

if __name__ == "__main__":
    typer.run(main)