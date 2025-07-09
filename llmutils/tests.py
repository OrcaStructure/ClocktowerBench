import pytest
from unittest.mock import patch, MagicMock
import asyncio


# Import your functions
# from your_file import assemble_context, invoke_llm, batch_llm_calls

from api_funcs import assemble_context, invoke_llm, batch_llm_calls


def test_assemble_context():
    stm = "short term"
    ltm = "long term"
    instructions = "do something"

    context = assemble_context(stm, ltm, instructions)

    assert "short term" in context
    assert "long term" in context
    assert "do something" in context


@patch("your_file.send_llm_request")
def test_invoke_llm(mock_send_llm_request):
    player = {
        "system_prompt": "system",
        "short_term_memory": "STM",
        "long_term_memory": "LTM"
    }
    instructions = "next move"
    tools = ["tool"]

    mock_send_llm_request.return_value = ("tool_name", {"key": "value"})

    result = invoke_llm(player, instructions, tools)

    mock_send_llm_request.assert_called_once()
    assert result == ("tool_name", {"key": "value"})


@pytest.mark.asyncio
@patch("your_file.invoke_llm_wrapper")
async def test_batch_llm_calls(mock_invoke_llm_wrapper):
    mock_invoke_llm_wrapper.side_effect = lambda *a, **kw: "fake_result"

    players = [
        {"system_prompt": "", "short_term_memory": "", "long_term_memory": ""},
        {"system_prompt": "", "short_term_memory": "", "long_term_memory": ""}
    ]
    instructions_list = ["ins1", "ins2"]
    tools = ["tool"]

    results = await batch_llm_calls(players, instructions_list, tools)

    assert results == ["fake_result", "fake_result"]
    assert mock_invoke_llm_wrapper.call_count == 2
