from stage.one.s4_for_loop import route, data
from tests.utils import check_attributes, post


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    req_data = {
        'field_1': '0',
        'field_2': '10',
        'field_3': '2'
    }
    await post(test_cli, route['url'], data=req_data)
