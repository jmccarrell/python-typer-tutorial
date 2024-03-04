# show importing subcommands from other files in this package
import typer

import items
import users
import lands

app = typer.Typer()
app.add_typer(items.app, name="items")
app.add_typer(users.app, name="users")
app.add_typer(lands.app, name="lands")

if __name__ == "__main__":
    app()
