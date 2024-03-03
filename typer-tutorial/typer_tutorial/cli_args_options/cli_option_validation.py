import typer
from typing_extensions import Annotated

def name_callback(value: str) -> str:
    if value != "Camila":
        raise typer.BadParameter("Sorry, we only greet Camila")
    return value

def main(
    name: Annotated[str, typer.Option(callback=name_callback)] = "Camila",
) -> None:
    print(f"Hiya {name}")

if __name__ == "__main__":
    typer.run(main)