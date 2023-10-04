"""
Delete all non-essential organic data from test user
"""

from pinterest.organic.boards import Board
from integration_tests.config import DEFAULT_BOARD_ID

def test_delete_organic_data():
    """
    Delete organic boards from default client
    """
    all_boards, _ = Board.get_all()
    for board in all_boards:
        if board.id == DEFAULT_BOARD_ID:
            continue
        Board.delete(board_id=board.id)

    assert len(Board.get_all()[0]) == 1