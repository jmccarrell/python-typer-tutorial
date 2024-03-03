import typer

from typing_extensions import Annotated

def main(name: Annotated[str, typer.Argument(envvar="SUPER_NAME")] = "Blech"):
    print(f"hiya Mr. {name}")

if __name__ == "__main__":
    typer.run(main)

# (typer-tutorial-py3.9) ❯ SUPER_NAME=Glurg !py
# SUPER_NAME=Glurg python env_var_cli_arg.py
# hiya Mr. Glurg
