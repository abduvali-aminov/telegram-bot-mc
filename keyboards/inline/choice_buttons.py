from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_APPLES, URL_PEAR
from keyboards.inline.callback_datas import buy_callback

# Вариант 1, как в прошлом уроке
# choice = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear")),
#         InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple")
#     ],
#     [
#         InlineKeyboardButton(text="Отмена", callback_data="next")
#     ]
# ])


# Вариант 2 - с помощью row_width и insert.
choiceOnTime = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesOnTime")
choiceOnTime.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noOnTime")
choiceOnTime.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceOnTime.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceWithin24 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesWithin24")
choiceWithin24.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noWithin24")
choiceWithin24.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceWithin24.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceWithin5 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesWithin5")
choiceWithin5.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noWithin5")
choiceWithin5.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceWithin5.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceReason1 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesReason1")
choiceReason1.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noReason1")
choiceReason1.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceReason1.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceReason2 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesReason2")
choiceReason2.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noReason2")
choiceReason2.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceReason2.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceReason3 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesReason3")
choiceReason3.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noReason3")
choiceReason3.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceReason3.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceAccepted1 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesAccepted1")
choiceAccepted1.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noAccepted1")
choiceAccepted1.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceAccepted1.insert(cancel_button)


# Вариант 2 - с помощью row_width и insert.
choiceAccepted3 = InlineKeyboardMarkup(row_width=2)

yes_button = InlineKeyboardButton(text="Yes", callback_data="yesAccepted3")
choiceAccepted3.insert(yes_button)

no_button = InlineKeyboardButton(text="No", callback_data="noAccepted3")
choiceAccepted3.insert(no_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choiceAccepted3.insert(cancel_button)


