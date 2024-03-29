# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
# from data import config
#
# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

import logging

from aiogram import Bot, Dispatcher, types

import config

import logging

from aiogram import Bot, Dispatcher, types

import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )