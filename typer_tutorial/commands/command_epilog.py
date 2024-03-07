# shows appending a message to help of a command
# and shows use of colorized markup; requires rich module installed

import typer

app = typer.Typer(rich_markup_mode="rich")

@app.command(epilog="Made with [red]love[/red] :heart:")
def create(user_name: str):
    """
    Create USER_NAME.
    """
    print(f"created {user_name}")

if __name__ == "__main__":
    app()
