from environs import Env
from aiogram import Bot, Dispatcher


bot_token = "5500745825:AAGB6wu0MYTXv8YuPQc18WStQmdOmzp997U"

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


thread_exb = {'Молитвенные нужды': 7, 'Наставление на день': 64, 'Объявления': None,
                  'Дни рождения': 9, 'Кабинеты': 324, 'Записи собраний': 3,
                  'Волонтёры': 59, 'Жизнь церкви': 61, 'Расписание служений': 57}
