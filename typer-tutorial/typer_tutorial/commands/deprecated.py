# show marking a command as deprecated
# eg:
# delete           Delete USER_NAME                        (deprecated)

import typer

app = typer.Typer()


@app.command()
def create(user_name: str):
    """
    Create USER_NAME
    """
    print(f"created {user_name}")


@app.command(deprecated=True)
def delete(user_name: str):
    """
    Delete USER_NAME
    """
    print(f"deleted {user_name}")


if __name__ == "__main__":
    app()
