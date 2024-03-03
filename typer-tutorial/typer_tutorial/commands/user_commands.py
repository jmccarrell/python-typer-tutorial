import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def create(user_name: str):
    print(f"creating user {user_name}")


@app.command()
def delete(
    user_name: str,
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete the user?")
    ],
):
    if not force:
        print("deletion cancelled")
        return
    print(f"deleted user: {user_name}")


@app.command()
def delete_all(
    user_name: str,
    force: Annotated[bool, typer.Option(prompt="delete all users?")],
):
    if not force:
        print("delete all cancelled")
        return
    print("all users deleted")


@app.command()
def initialize():
    print("initialize the user DB")


if __name__ == "__main__":
    app()
