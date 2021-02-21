from trello import TrelloClient

from settings import settings

client = TrelloClient(
    api_key=settings.api_key,
    api_secret=settings.api_secret,
)


def delete_board_archived_items():
    english_board_id = "yTsv60N4"
    english_board = client.get_board(english_board_id)

    print(english_board.name)
    closed_cards = english_board.closed_cards()
    for closed_card in closed_cards:
        print(closed_card.name)
        closed_card.delete()
    # lists = english_board.list_lists()
    # for board_list in lists:
    #     print(board_list.name)
