# shows writing multiline help text that typer/rich will format appropriately on output.
import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    Manage users CLI application.

    Lorem ipsum dolor sit amet. Non similique rerum sed amet quidem non culpa voluptas in voluptatem obcaecati rem libero magnam eum eius velit. Non quia nesciunt At libero minima qui earum eius. Et sint dolores et repellat saepe est veniam quidem in culpa ipsum!

    Et tempora minima sed voluptas nobis est deleniti sint non delectus quisquam ut officia consequatur? Non laboriosam provident ad omnis tempora ut quam illo et quibusdam quod et ratione illo sed laborum beatae! Cum totam dolor aut neque facilis sit obcaecati cupiditate vel nemo accusamus et sequi galisum aut sunt illo aut illum optio. In provident unde ea similique natus et inventore dolor?

    Ut obcaecati delectus a doloremque corrupti ea illum reiciendis ex voluptate officiis. Et quidem suscipit id voluptatibus placeat non velit totam eum minus dolores id iste repudiandae?
    """


@app.command()
def create(user_name: str):
    """
    Create user USER_NAME
    """
    print(f"created {user_name}")


if __name__ == "__main__":
    app()
