# show the basics of type conversion in parameters
import typer

def main(name: str, age: int = 20, height_meters: float = 1.89, female: bool = True):
    print(f"NAME: {name} type: {type(name)}")
    print(f"--age: {age} type: {type(age)}")
    print(f"--height_meters: {height_meters} type: {type(height_meters)}")
    print(f"--female: {female}  type: {type(female)}")

if __name__ == "__main__":
    typer.run(main)