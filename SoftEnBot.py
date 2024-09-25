import pandas as pd
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data_manipulation.generate_graph import generate_graph

bot = Bot(token='')
dp = Dispatcher(bot)

data_dict = {}

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyboard_markup.add(KeyboardButton('/restart'))
keyboard_markup.add(KeyboardButton('/EnterData'))
keyboard_markup.add(KeyboardButton('/statistics'))
keyboard_markup.add(KeyboardButton('/graph'))




def calculate_stats_from_excel(excel_file):
    df = pd.read_excel(excel_file)
    stats_message = ""

    for column in df.select_dtypes(include=['number']).columns:
        max_val = df[column].max()
        min_val = df[column].min()
        avg_val = df[column].mean()

        stats_message += (
            f"Column: {column}\n"
            f"Max: {max_val}\n"
            f"Min: {min_val}\n"
            f"Avg: {avg_val}\n\n"
        )

    return stats_message



@dp.message_handler(commands=['graph'])
async def graph(message: types.Message):
    generate_graph()
    time.sleep(2)
    with open('data.png', 'rb') as file:
        await message.bot.send_photo(chat_id=message.chat.id, photo=file, caption="Here is your data")





@dp.message_handler(commands=['statistics'])
async def statistics(message: types.Message):
    excel_file_path = 'result.xlsx'
    await bot.send_message(message.from_user.id,str(calculate_stats_from_excel(excel_file_path)))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Welcome to our bot! Enter /start command to start bot, and command "
                           "/statistics to see averages or send /EnterData command  to enter data into Excel file, "
                           "/restart to re-enter data, use /graph to visualize entered data", reply_markup=keyboard_markup)


@dp.message_handler(commands=['restart'])
async def restart_process(message: types.Message):
    user_id = message.from_user.id
    if user_id in data_dict:
        if (datetime.now().strftime("%Y-%m-%d") == data_dict[user_id]['Date'][:10]):
            await bot.send_message(user_id, "You have already entered data today.")
            return
        data_dict.pop(user_id)
        await bot.send_message(user_id, "Data entry process restarted. You can start again by typing /EnterData.")
    else:
        await bot.send_message(user_id, "No data entry process is currently active.")


@dp.message_handler()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if user_id in data_dict:
       if (datetime.now().strftime("%Y-%m-%d") == data_dict[user_id]['Date'][:10]):
            await bot.send_message(message.from_user.id, "You have already entered data today.")
            return

    if user_id not in data_dict:
        data_dict[user_id] = {'User': message.from_user.username,
                              'Weight': '', 'Price per liter': '', 'Liters': '',
                              'Miles driven': '', 'Date': ''}
        await bot.send_message(message.from_user.id, "Enter net weight:")
    elif 'Weight' in data_dict[user_id] and data_dict[user_id]['Weight'] == '':
        data_dict[user_id]['Weight'] = message.text
        await bot.send_message(message.from_user.id, "Enter price per liter:")
    elif 'Price per liter' in data_dict[user_id] and data_dict[user_id]['Price per liter'] == '':
        data_dict[user_id]['Price per liter'] = message.text
        await bot.send_message(message.from_user.id, "Enter how many liters:")
    elif 'Liters' in data_dict[user_id] and data_dict[user_id]['Liters'] == '':
        data_dict[user_id]['Liters'] = message.text
        await bot.send_message(message.from_user.id, "Enter how many miles driven:")
    elif 'Miles driven' in data_dict[user_id] and data_dict[user_id]['Miles driven'] == '':
        data_dict[user_id]['Miles driven'] = message.text
        data_dict[user_id]['Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame(data_dict.values())
        df.to_excel('result.xlsx', index=False)
        await bot.send_message(message.from_user.id, "Your data has been saved.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   