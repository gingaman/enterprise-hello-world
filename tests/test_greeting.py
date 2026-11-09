"""HelloWorld™ test suite.

Current coverage: 14%. Remaining coverage scheduled for follow-up
(see JIRA HW-1, opened 2024, unassigned).
"""

from helloworld.plugins import DefaultGreeter


def test_greeting_is_a_greeting() -> None:
    assert DefaultGreeter().produce("en-GB") == "Hello, World!"
