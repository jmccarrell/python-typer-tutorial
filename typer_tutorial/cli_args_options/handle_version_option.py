# demos precedence of --version over --name given is_eager

import importlib.metadata
from typing import Union
import typer
from typing_extensions import Annotated

def report_version(report: bool) -> None:
    if report:
        package_name: str = "typer-tutorial"
        v = importlib.metadata.version(package_name)
        print(f"{package_name}: {v}")
        raise typer.Exit()

def name_callback(name: str) -> str:
    if name != "Camila":
        raise typer.BadParameter("We only greet Camila")
    return name

def main(
    name: Annotated[str, typer.Option(callback=name_callback)] = "Camila",
    version: Annotated[
        Union[bool, None], 
        typer.Option(callback=report_version, is_eager=True)
    ] = None
):
    print(f"Hiya {name}")

if __name__ == "__main__":
    typer.run(main)