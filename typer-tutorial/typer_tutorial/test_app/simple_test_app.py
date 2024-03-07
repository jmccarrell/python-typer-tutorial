from typing import Optional

import typer

app = typer.Typer()


@app.command()
def main(name: str, city: Optional[str] = None):
    print(f"Hiya {name}")
    if city:
        print(f"Lets ride to {city}")


if __name__ == "__main__":
    app()
