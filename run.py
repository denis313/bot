import asyncio
import logging
from config import bot, dp, thread_exb
import handlers
from bd import get_data_by_timme
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler


logger = logging.getLogger(__name__)


async def message():
    thread_exb = {'Молитвенные нужды': 128, 'Наставление на день': 12, 'Объявления': 3,
                  'Дни рождения': 5, 'Кабинеты': None, 'Записи собраний': 126,
                  'Волонтёры': 124, 'Жизнь церкви': 122, 'Расписание служений': 120}
    for data in get_data_by_timme(dispatch_time=(str(datetime.now().date()))):
        subject, dispatch_time, text_message = data
        await bot.send_message(chat_id=-1001851089340, text=text_message, message_thread_id=thread_exb[subject])


async def message_2():
    # subject, dispatch_time, text_message = get_data_by_timme(dispatch_time=(str(datetime.now().date())))
    thread_exb = {'Молитвенные нужды': 128, 'Наставление на день': 12, 'Объявления': 3,
                  'Дни рождения': 5, 'Кабинеты': None, 'Записи собраний': 126,
                  'Волонтёры': 124, 'Жизнь церкви': 122, 'Расписание служений': 120}
    for data in get_data_by_timme(dispatch_time=('2023-10-12')):
        subject, dispatch_time, text_message = data
        await bot.send_message(chat_id=-1001851089340, text=text_message, message_thread_id=thread_exb[subject])


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    scheduler.add_job(message, trigger='cron',
                      hour=0o7,
                      minute=0o0,
                      misfire_grace_time=30*60)
    # scheduler.add_job(message_2, trigger='interval',
    #                   minutes=2)
    # start
    scheduler.start()

    # Подключение хендлеров
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    # shedule
if __name__ == '__main__':
    print('work')
    print(f'{datetime.now().date()} {datetime.now().hour}:{datetime.now().minute}')
    asyncio.run(main())
