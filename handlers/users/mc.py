import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choiceOnTime, choiceReason1, choiceWithin5, choiceWithin24, choiceAccepted1, choiceReason2, choiceAccepted3, choiceReason3
from loader import dp, bot


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="CW Deadline. CW Submission.  \n"
                              "On time?",
                         reply_markup=choiceOnTime)


@dp.callback_query_handler(text="yesOnTime")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: Yes \n\nResult: Full Mark")
    await call.answer("Full Mark", show_alert=True)


@dp.callback_query_handler(text="noOnTime")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Within 24 hours?",
                              reply_markup=choiceWithin24)


@dp.callback_query_handler(text="yesWithin24")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Late Submission!")
    await call.message.answer(f"Is there a valid reason?",
                              reply_markup=choiceReason3)


@dp.callback_query_handler(text="noWithin24")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Submitted within 5 days",
                              reply_markup=choiceWithin5)


@dp.callback_query_handler(text="yesWithin5")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Is there a valid reason?",
                              reply_markup=choiceReason1)


@dp.callback_query_handler(text="noWithin5")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Is there a valid reason?",
                              reply_markup=choiceReason2)


@dp.callback_query_handler(text="yesReason1")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("MC (late submission option)")
    await call.message.answer(f"Accepted?",
                              reply_markup=choiceAccepted1)


@dp.callback_query_handler(text="noReason1")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: No\n Submitted within 5 days: Yes\n"
                              "Is there a valid reason: No \n\nResult: Mark=0")
    await call.answer("Mark=0", show_alert=True)


@dp.callback_query_handler(text="yesAccepted1")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: No\nSubmitted within 5 days: Yes\n"
                              "Is there a valid reason: Yes\nAccepted: Yes \n\nResult: Full Mark")
    await call.answer("Full Mark", show_alert=True)


@dp.callback_query_handler(text="noAccepted1")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: No\nSubmitted within 5 days: Yes\n"
                              "Is there a valid reason: Yes\nAccepted: No  \n\nResult: Mark=0")
    await call.answer("Mark=0", show_alert=True)


@dp.callback_query_handler(text="yesReason2")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("MC (non-submission/deferral before specified deadline)")
    await call.message.answer("Accepted")
    await call.message.answer("On Time: No \nWithin 24 hours: No\nSubmitted within 5 days: No\n"
                              "Is there a valid reason: Yes \n\nResult: Deferral reassessment")
    await call.answer("Deferral reassessment", show_alert=True)


@dp.callback_query_handler(text="noReason2")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: No\nSubmitted within 5 days: No\n"
                              "Is there a valid reason: No \n\nResult: Mark=0")
    await call.answer("Mark=0", show_alert=True)


@dp.callback_query_handler(text="yesReason3")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("MC")
    await call.message.answer(f"Accepted?",
                              reply_markup=choiceAccepted3)


@dp.callback_query_handler(text="noReason3")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: Yes\n"
                              "Is there a valid reason: No \n\nResult: Minus 10 marks from overall mark but not below"
                              " 40")
    await call.answer("Minus 10 marks from overall mark but not below 40", show_alert=True)


@dp.callback_query_handler(text="yesAccepted3")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: Yes\n"
                              "Is there a valid reason: Yes \nAccepted: Yes \n\nResult: Full Mark")
    await call.answer("Full Mark", show_alert=True)


@dp.callback_query_handler(text="noAccepted3")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("On Time: No \nWithin 24 hours: Yes\n"
                              "Is there a valid reason: Yes \nAccepted: No \n\nResult: Minus 10 marks from overall mark"
                              " but not below 40")
    await call.answer("Minus 10 marks from overall mark but not below 40", show_alert=True)


@dp.callback_query_handler(text="cancel")
async def cancel_process(call: CallbackQuery):
    await call.answer("The process is stopped", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
