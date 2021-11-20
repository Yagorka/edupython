import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.dumps(res)
    return wrapper

# @to_json
# def get_data():
#     return 1
#
#
# print(type(get_data()))  # вернёт '{"data": 42}'
# print(get_data())
# print(get_data.__name__)