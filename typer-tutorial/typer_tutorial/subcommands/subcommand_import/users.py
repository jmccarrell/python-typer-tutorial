import typer

app = typer.Typer()


@app.command("create")
def user_create(user: str):
    print(f"Create user {user}")


@app.command("delete")
def user_delete(user: str):
    print(f"Delete user {user}")


if __name__ == "__main__":
    app()
