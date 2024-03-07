import typer

def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hello to NAME, optionally with --lastname.
    If --formal is used, speak formally.
    """
    print(f"hello {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)