"Demo exit status using Typer"
import typer

existing_usernames = ["hearty", "fool"]

def maybe_create_user(name: str):
    if name in existing_usernames:
        print(f"User {name} exists")
        raise typer.Exit(code=1)
    print(f"Created user: {name}")


def main(username: str):
    maybe_create_user(username)

if __name__ == "__main__":
    typer.run(main)
