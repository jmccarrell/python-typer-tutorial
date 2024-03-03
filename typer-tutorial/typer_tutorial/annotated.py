import random
import typer
from typing_extensions import Annotated

def get_name() -> str:
    return random.choice(["Kenny", "Eli", "Jet"])

def main(name: Annotated[str, typer.Argument(help="name of the user to greet", default_factory=get_name)]):
    """
    Say hi to NAME very gently.
    """
    print(f"hiya {name}")

if __name__ == "__main__":
    typer.run(main)