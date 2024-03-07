# shows how to add --verbose at the top level that applies to all commands
import typer

state = {"verbose": False}
app = typer.Typer()


@app.command()
def create(user_name: str):
    if state["verbose"]:
        print(f"about to create {user_name}")
    print(f"creating {user_name}")


@app.command()
def delete(user_name: str):
    if state["verbose"]:
        print(f"will delete {user_name}")
    print(f"deleted {user_name}")


@app.callback()
def main(verbose: bool = False):
    """
    Manage users CLI
    """
    if verbose:
        state["verbose"] = True


if __name__ == "__main__":
    app()
