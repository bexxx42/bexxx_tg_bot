import types

from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS


class IsUser(BoundFilter):
    async def check(self, message: Message):
        print(message.from_user.id not in ADMINS)
        return message.from_user.id not in ADMINS