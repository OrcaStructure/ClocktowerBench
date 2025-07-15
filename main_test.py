# test_game.py
import pytest
import main as game

# A dummy dict that returns "type_<role>" for any role
class DummyRoleMap(dict):
    def get(self, key, default=None):
        return f"type_{key}"

@pytest.fixture(autouse=True)
def patch_utils(monkeypatch):
    # monkey-patch utils.role_map and utils.role_mapper before each test
    monkeypatch.setattr(game.utils, 'role_map', DummyRoleMap())
    monkeypatch.setattr(game.utils, 'role_mapper', lambda role: f"alignment_{role}")

def test_initial_game_state_structure():
    state = game.initalise_game()

    # top-level keys
    assert set(state.keys()) == {"players", "player_count", "script_name", "script", "day", "time"}

    # defaults
    assert state["player_count"] == game.PLAYER_NUMBER
    assert state["script_name"] == "Trouble Brewing"
    assert state["script"] == game.utils.load_text_file("trouble_brewing_edited.txt")
    assert state["day"] == 1
    assert state["time"] == "night"

def test_player_count_and_names():
    state = game.initalise_game()
    players = state["players"]

    # exactly eight players named player0…player7
    assert len(players) == 8
    expected_names = {f"player{i+1}" for i in range(8)}
    assert set(players.keys()) == expected_names

def test_each_player_initial_values():
    state = game.initalise_game()
    players = state["players"]

    for name, pdata in players.items():
        # role comes straight from the closure
        role = pdata["role"]
        assert isinstance(role, str) and role != ""

        # our dummy mapper hooks were used
        assert pdata["role_type"] == f"type_{role}"
        assert pdata["alignment"] == f"alignment_{role}"

        # all these should be set to their stated defaults
        assert pdata["alive"] is True
        assert pdata["has_votes"] is True
        assert pdata["voted"] is False

        # memories and context start empty
        assert pdata["short_term_memory"] == ""
        assert pdata["long_term_memory"] == ""
        assert pdata["context"] == ""