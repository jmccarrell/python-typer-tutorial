from typer.testing import CliRunner

from typer_tutorial.test_app.simple_test_app import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ("Stanley", "--city", "Georgetown"))
    assert result.exit_code == 0
    print(f"testing: {result.stdout}")
    assert "Stanley" in result.stdout
    assert "ride to Georgetown" in result.stdout
