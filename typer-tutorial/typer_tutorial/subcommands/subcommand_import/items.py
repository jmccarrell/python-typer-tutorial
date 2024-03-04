import typer

app = typer.Typer()


@app.command("create")
def item_create(item: str):
    print(f"Create item {item}")


@app.command("delete")
def item_delete(item: str):
    print(f"Delete item {item}")


@app.command("sell")
def item_sell(item: str):
    print(f"Sell item {item}")


if __name__ == "__main__":
    app()
