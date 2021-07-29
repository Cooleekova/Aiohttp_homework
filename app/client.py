import asyncio
import requests


async def create_user():
    response = requests.post(
        'http://127.0.0.1:8088/users',
        json={'username': 'vanya', 'email': 'vanya@vanya.ru', 'password': 'Ivan123', }
    )
    print(response.text)


async def get_user():
    response = requests.get('http://127.0.0.1:8088/users/1')
    # data = response.text()
    print(response.text)


async def get_ad():
    response = requests.get('http://127.0.0.1:8088/ads/1')
    # data = response.text()
    print(response.text)


async def create_ad():
    response = requests.post(
        'http://127.0.0.1:8088/ads',
        json={'title': 'vanya', 'description': 'vanya', 'creator_id': '1', }
    )
    print(response.text)


async def delete_ad():
    response = requests.delete('http://127.0.0.1:8088/ads/1')
    print(response.text)

# async def get_my_user(**kwargs):
#     async with aiohttp.client.ClientSession() as client:
#         async with client.get(f'http://127.0.0.1:8088/users/3', **kwargs) as response:
#             print(response.text())
#             return await response.text()
#
#
# async def post_my_user(json):
#     async with aiohttp.client.ClientSession() as client:
#         async with client.post('http://127.0.0.1:8088/users', json=json) as r:
#             data = r.json()
#             return await data

asyncio.run(get_user())

