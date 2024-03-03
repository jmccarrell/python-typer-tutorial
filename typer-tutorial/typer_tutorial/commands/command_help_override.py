# shows passing help as an arg to the command function
# not generally preferred, but possible
import typer

app = typer.Typer(help="Super duper user manager CLI")


@app.command(help="Create a new user with USER_NAME")
def create(user_name: str):
    """
    Eg, some internal utility function that actually creates the user
    """
    print(f"Created user {user_name}")


@app.command(help="delete the USER_NAME")
def delete(user_name: str):
    """
    Likewise, function doc for some internal purpose, not to be displayed to the user.
    """
    print(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
