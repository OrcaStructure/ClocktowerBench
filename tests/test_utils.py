import pytest
import utils

def test_role_mapper_townsfolk_and_outsider():
    # Townsfolk and Outsider roles should both map to "good"
    assert utils.role_mapper("washerwoman") == "good"
    assert utils.role_mapper("librarian") == "good"

def test_role_mapper_minion():
    # Minion roles should map to "evil"
    assert utils.role_mapper("poisoner") == "evil"

def test_role_counts_valid():
    # Known good configurations
    assert utils.role_counts(5) == [3, 0, 1, 1]
    assert utils.role_counts(8) == [5, 1, 1, 1]

def test_role_counts_invalid():
    # Out-of-range player numbers should error
    with pytest.raises(ValueError):
        utils.role_counts(4)

def test_load_text_file_not_found():
    # Nonexistent filenames raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        utils.load_text_file("this_file_does_not_exist.txt")

def test_system_prompt_generator_branches(monkeypatch):
    # Stub out the script append so we don't hit the filesystem
    monkeypatch.setattr(utils, "load_text_file", lambda fn: "<<<SCRIPT>>>")

    # Good‐alignment branch (requires exact "Good")
    good = utils.system_prompt_generator("Good", "TestRole", 4, 2)
    assert "You are playing in a game of Blood on the Clocktower." in good
    assert "Your role is TestRole." in good
    assert good.endswith("<<<SCRIPT>>>")

    # Anything else falls to the evil branch
    evil = utils.system_prompt_generator("evil", "TestRole", 3, 1)
    assert "You are playing in a game of Blood on the Clocktower." in evil
    assert "Your role is TestRole." in evil
    assert "evil team" in evil
    assert evil.endswith("<<<SCRIPT>>>")

def test_make_player_structure(monkeypatch):
    # Avoid a huge prompt; stub that out
    monkeypatch.setattr(
        utils, "system_prompt_generator", 
        lambda alignment, role, pc, wp: f"[PROMPT:{alignment}/{role}/{pc}/{wp}]"
    )

    pl = utils.make_player("washerwoman", 1, 5)
    # Core fields
    assert pl["role"] == "washerwoman"
    assert pl["role_type"] == utils.role_map["washerwoman"]
    assert pl["alignment"] == "good"
    assert pl["which_player"] == 1
    assert pl["system_prompt"] == "[PROMPT:good/washerwoman/5/1]"
    # Memory slots start empty
    assert pl["short_term_memory"] == ""
    assert pl["long_term_memory"] == ""
    assert pl["context"] == ""
    # Voting flags default correctly
    assert pl["has_votes"] is True
    assert pl["voted"] is False
