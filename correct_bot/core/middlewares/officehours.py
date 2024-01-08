from datetime import datetime
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message, TelegramObject


def office_hours() -> bool:
    return datetime.now().weekday() in (1, 2, 3, 4, 5) and datetime.now().hour in ([i for i in (range(8, 19))])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            # handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            # event: Message,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        if not office_hours():
            return await handler(event, data)
        # await event.answer("Время работы бота:\r\nПн-пт с 8 до 18. Приходите в рабочие часы.")
