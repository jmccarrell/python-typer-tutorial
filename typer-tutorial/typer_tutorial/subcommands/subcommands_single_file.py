import typer

app = typer.Typer()
item_app = typer.Typer()
app.add_typer(item_app, name="item")
user_app = typer.Typer()
app.add_typer(user_app, name="user")


@item_app.command("create")
def item_create(item: str):
    print(f"Create item {item}")


@item_app.command("delete")
def item_delete(item: str):
    print(f"Delete item {item}")


@item_app.command("sell")
def item_sell(item: str):
    print(f"Sell item {item}")


@user_app.command("create")
def user_create(user: str):
    print(f"Create user {user}")


@user_app.command("delete")
def user_delete(user: str):
    print(f"Delete user {user}")


if __name__ == "__main__":
    app()
