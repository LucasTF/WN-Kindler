from click.testing import CliRunner
from wnk.commands.list_novels import list_novels

def test_list_novels():
  runner = CliRunner()
  result = runner.invoke(list_novels, ['-s', '0'])
  assert result.exit_code == 0