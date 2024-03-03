# shows the cli command differing from the default: uses the function name
import typer

app = typer.Typer()

# pass the desired name either as name keyword arg
@app.command(name="create")
def cli_create(user_name: str):
    """
    Create USER_NAME
    """
    print(f"created {user_name}")

# or as the first arg
@app.command("delete")
def cli_delete(user_name: str):
    """
    Delete USER_NAME
    """
    print(f"deleted {user_name}")

if __name__ == "__main__":
    app()
