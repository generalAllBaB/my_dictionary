import asyncio
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData, CallbackQuery
from aiogram.types import InlineKeyboardButton
import random
from gtts import gTTS
from aiogram.types import FSInputFile
from nltk import ngrams
from collections import Counter
from db_user import *


#-----------------------------------------------------------------------------------------------------------------------
def add_message_id_all_messages(id):
    with open(f'user/all_message_id.txt', "r") as get_all_messages:
        get_text = get_all_messages.read() + "\n" + str(id)
        with open(f'user/all_message_id.txt', "w") as add_text:
            add_text.write(get_text)
        with open(f'user/all_message_id.txt', 'r') as delete_emptiness:
            lines = delete_emptiness.readlines()
            lines = [line for line in lines if line.strip()]
        with open(f'user/all_message_id.txt', 'w') as lines_delete_emptiness:
            lines_delete_emptiness.writelines(lines)
async def delete_message(user_id, bot):
    with open(f'user/all_message_id.txt', 'r') as file:
        for line in (file.readlines()):
            try:
                await bot.delete_message(user_id, message_id=int(line))
            except:
                pass
    with open(f'user/all_message_id.txt', 'w') as add_zero_id:
        add_zero_id.write("")
#-----------------------------------------------------------------------------------------------------------------------
async def train_callback_0(query: CallbackQuery):
    update_train_0()
    # -----------------------------------------------------------------------------------------------------------
    if get_max_words(query.from_user.id) == "Все слова":
        # -------------------------------------------------------------------------------------------------------
        if get_words(query.from_user.id) == "Все слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM words ORDER BY RANDOM() LIMIT {get_number_of_words()}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) >= int(get_froms(query.from_user.id)) and int(row_id) <= int(
                        get_before(query.from_user.id)):
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
        # -------------------------------------------------------------------------------------------------------
        elif get_words(query.from_user.id) == "Невыученные слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM words ORDER BY RANDOM() LIMIT {get_number_of_words()}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) >= int(get_froms(query.from_user.id)) and int(row_id) <= 99:
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
        # -------------------------------------------------------------------------------------------------------
        elif get_words(query.from_user.id) == "Выученные слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM words ORDER BY RANDOM() LIMIT {get_number_of_words()}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) == 100:
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
    # -----------------------------------------------------------------------------------------------------------
    else:
        row_count = get_max_words(query.from_user.id)
        # -------------------------------------------------------------------------------------------------------
        if get_words(query.from_user.id) == "Все слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM words ORDER BY RANDOM() LIMIT {row_count}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) >= int(get_froms(query.from_user.id)) and int(row_id) <= int(get_before(query.from_user.id)):
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
        # -------------------------------------------------------------------------------------------------------
        elif get_words(query.from_user.id) == "Невыученные слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM words ORDER BY RANDOM() LIMIT {row_count}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) >= int(get_froms(query.from_user.id)) and int(row_id) <= 99:
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
        # -------------------------------------------------------------------------------------------------------
        elif get_words(query.from_user.id) == "Выученные слова":
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM ORDER BY RANDOM() LIMIT {row_count}")
            random_rows = cursor.fetchall()
            column_name = 'train'
            for row in random_rows:
                row_id = row[0]
                if int(row_id) == 100:
                    cursor.execute(f"UPDATE words SET {column_name} = 1 WHERE ID = ?", (row_id,))
            conn.commit()
            conn.close()
#-----------------------------------------------------------------------------------------------------------------------
class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: str
#-----------------------------------------------------------------------------------------------------------------------
async def start(message: types.Message, bot):
    if not gef_user(message.from_user.id):
        add_user(message.from_user.id)

        for x in ["all_message_id.txt", "add_000.txt", "add_001.txt", "add_002.txt", "add_003.txt", "add_004.txt"]:
            with open(f'user/{x}', "w", encoding='utf-8') as f:
                f.write("")

    add_mode(message.from_user.id, "0")

    add_activity(message.from_user.id)

    await delete_message(message.from_user.id, bot)

    add_message_id_all_messages(str((await bot.send_message(message.from_user.id, "menu:", reply_markup=await button_000())).message_id))

    try:
        await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
    except:
        pass
#-----------------------------------------------------------------------------------------------------------------------
async def message_text(message: types.Message, bot):
    if message.text == "/clear_random":
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM words ORDER BY RANDOM() LIMIT {get_number_of_words()}")
        random_rows = cursor.fetchall()
        column_name = 'lvl'
        for row in random_rows:
            row_id = row[4]
            if int(row_id) != 0:
                cursor.execute(f"UPDATE words SET {column_name} = {int(row_id) - 1} WHERE ID = ?", (row[0],))
        conn.commit()
        conn.close()
        get_id_message = str((await bot.send_message(message.from_user.id, "у 100 слов уравень уменьшился на 1")).message_id)

        await asyncio.sleep(5)

        try:
            await bot.delete_message(message.from_user.id, message_id=int(get_id_message))
        except:
            pass

    add_activity(message.from_user.id)
    mode = get_mode(message.from_user.id)
    add_mode(message.from_user.id, "0")
    if mode == 1 or mode == 2 or mode == 3:
        await delete_message(message.from_user.id, bot)
        if mode == 1:
            with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        elif mode == 2:
            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        else:
            with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        await delete_message(message, bot)
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        try:
            await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
        except:
            pass
        if len(word) >= 1 and len(translation) >= 1:
            add_message_id_all_messages(str((await bot.send_message(message.from_user.id, f"Добавить слово\n\nСлово: {word}\nТранскрипция*: {transcription}\nПеревод: {translation}\n\n* - необязательно добавлять", reply_markup=await button_004())).message_id))
        else:
            add_message_id_all_messages(str((await bot.send_message(message.from_user.id, f"Добавить слово\n\nСлово: {word}\nТранскрипция*: {transcription}\nПеревод: {translation}\n\n* - необязательно добавлять", reply_markup=await button_003())).message_id))

    elif mode == 4 or mode == 5 or mode == 6:
        await delete_message(message.from_user.id, bot)
        if mode == 4:
            with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        elif mode == 5:
            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        else:
            with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
                f.write(message.text)
        await delete_message(message, bot)
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        with open(f'user/add_004.txt', "r", encoding='utf-8') as f:
            lvl = f.read()
        try:
            await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
        except:
            pass

        add_message_id_all_messages(str((await bot.send_message(message.from_user.id, f"Редактировать\n\nСлово: {word}\nТранскрипция: {transcription}\nПеревод: {translation}\nВыучено(%): {lvl}", reply_markup=await button_009())).message_id))

    elif mode == 7:
        await delete_message(message.from_user.id, bot)
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        text1 = "train" + word
        text2 = "train" + message.text

        n = 3
        ngrams_text1 = Counter(ngrams(text1, n))
        ngrams_text2 = Counter(ngrams(text2, n))

        intersection = sum((ngrams_text1 & ngrams_text2).values())

        union = sum((ngrams_text1 | ngrams_text2).values())

        jaccard_sim = intersection / union

        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            IDd = f.read()

        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT lvl FROM words WHERE ID = {IDd}")
        result = cursor.fetchone()[0]
        conn.close()

        if jaccard_sim > 0.8:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()

            if str(result) != "100":
                result = int(result) + 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()

            get_id_message = str((await bot.send_message(message.from_user.id, f"Правильно✅\n\n{word}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.delete_message(message.from_user.id, message_id=int(get_id_message))
            except:
                pass
        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()
            if str(result) != "0":
                result = int(result) - 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()

            get_id_message = str((await bot.send_message(message.from_user.id, f"Неправильно❌\n\n{word}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)
            try:
                await bot.delete_message(message.from_user.id, message_id=int(get_id_message))
            except:
                pass
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
        row_count = cursor.fetchone()[0]
        conn.close()
        try:
            await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
        except:
            pass

        if str(row_count) == "0":
            get_id_message = str((await bot.send_message(message.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.edit_message_text(chat_id=message.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
            except:
                pass

        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
            random_row = cursor.fetchone()
            conn.commit()
            conn.close()

            audio = gTTS(text=random_row[3], lang="ru")
            audio.save(f'user/train_002.mp3')
            audio = FSInputFile(path=f'user/train_002.mp3', filename="audio")
            add_message_id_all_messages(str((await bot.send_audio(message.from_user.id, audio=audio)).message_id))

            with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[0]))

            with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[1]))

            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[2]))

            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[3]))

            button = InlineKeyboardBuilder()
            button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

            add_mode(message.from_user.id, "7")
            add_message_id_all_messages(str((await bot.send_message(message.from_user.id, f"Тренировка - {row_count}\n\nПеревод: {random_row[3]}\n\nОтправьте слово", reply_markup=button.as_markup())).message_id))

    elif mode == 8:
        await delete_message(message.from_user.id, bot)
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            word = f.read()
        text1 = "train" + word
        text2 = "train" + message.text

        n = 3
        ngrams_text1 = Counter(ngrams(text1, n))
        ngrams_text2 = Counter(ngrams(text2, n))

        intersection = sum((ngrams_text1 & ngrams_text2).values())

        union = sum((ngrams_text1 | ngrams_text2).values())

        jaccard_sim = intersection / union

        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            IDd = f.read()

        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT lvl FROM words WHERE ID = {IDd}")
        result = cursor.fetchone()[0]
        conn.close()

        if jaccard_sim > 0.8:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()

            if str(result) != "100":
                result = int(result) + 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()

            get_id_message = str((await bot.send_message(message.from_user.id, f"Правильно✅\n\n{word}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.delete_message(message.from_user.id, message_id=int(get_id_message))
            except:
                pass
        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()
            if str(result) != "0":
                result = int(result) - 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()

            get_id_message = str((await bot.send_message(message.from_user.id, f"Неправильно\n\n{word}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)
            try:
                await bot.delete_message(message.from_user.id, message_id=int(get_id_message))
            except:
                pass
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
        row_count = cursor.fetchone()[0]
        conn.close()
        try:
            await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
        except:
            pass

        if str(row_count) == "0":
            get_id_message = str((await bot.send_message(message.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.edit_message_text(chat_id=message.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
            except:
                pass

        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
            random_row = cursor.fetchone()
            conn.commit()
            conn.close()

            audio = gTTS(text=random_row[1], lang="ru")
            audio.save(f'user/train_003.mp3')
            audio = FSInputFile(path=f'user/train_003.mp3', filename="audio")
            add_message_id_all_messages(str((await bot.send_audio(message.from_user.id, audio=audio)).message_id))

            with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[0]))

            with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[1]))

            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[2]))

            with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
                f.write(str(random_row[3]))

            button = InlineKeyboardBuilder()
            button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

            add_mode(message.from_user.id, "8")
            add_message_id_all_messages(str((await bot.send_message(message.from_user.id, f"Тренировка - {row_count}\n\nСлово: {random_row[1]}\n\nОтправьте перевод", reply_markup=button.as_markup())).message_id))
    else:
        try:
            await bot.delete_message(message.from_user.id, message_id=int(message.message_id))
        except:
            pass
#-----------------------------------------------------------------------------------------------------------------------
async def dictionary(query: CallbackQuery, callback_data: MyCallback, bot):
    if get_number_of_words() == 0:

        await bot.answer_callback_query(callback_query_id=query.id, text='Словарь пуст❌', show_alert=True)

        get_id_message = str((await bot.send_message(query.from_user.id, "Словарь пуст❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)

        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass
    else:
        for x in ["add_000.txt", "add_001.txt", "add_002.txt", "add_003.txt", "add_004.txt"]:
            with open(f'user/{x}', "w", encoding='utf-8') as f:
                f.write("")

        x_1 = get_sorting_words(query.from_user.id)
        x_2 = get_sorting_words(query.from_user.id)

        if x_1 == "A-Z" or x_1 == "Z-A":
            x_1 = "word"
        elif x_1 == "А-Я" or x_1 == "Я-А":
            x_1 = "translation"
        elif x_1 == "0-100" or x_1 == "100-0":
            x_1 = "lvl"

        if x_2 == "A-Z" or x_2 == "А-Я" or x_2 == "0-100":
            x_2 = "ASC"
        elif x_2 == "Z-A" or x_2 == "Я-А" or x_2 == "100-0":
            x_2 = "DESC"

        rows = get_list_words_dictionary(x_1, x_2)

        button = InlineKeyboardBuilder()
        if get_number_of_words() <= 90:
            for x_3 in rows:
                if x_1 == "word":
                    button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                elif x_1 == "translation":
                    button.row(InlineKeyboardButton(text=str(x_3[3]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                elif x_1 == "lvl":
                    button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
            button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))
        else:
            count = 0
            for x_3 in rows:
                if count <= 88:
                    if x_1 == "word":
                        button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                    elif x_1 == "translation":
                        button.row(InlineKeyboardButton(text=str(x_3[3]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                    elif x_1 == "lvl":
                        button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                else:
                    break
                count += 1
            button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))
            button.button(text="➡️", callback_data=MyCallback(foo="dictionary_002", bar="2"))
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Словарь\n\nСортировка: {get_sorting_words(query.from_user.id)}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def dictionary_000(query: CallbackQuery, callback_data: MyCallback, bot):
    x_1 = get_sorting_words(query.from_user.id)
    x_2 = get_sorting_words(query.from_user.id)

    if x_1 == "A-Z" or x_1 == "Z-A":
        x_1 = "word"
    elif x_1 == "А-Я" or x_1 == "Я-А":
        x_1 = "translation"
    elif x_1 == "0-100" or x_1 == "100-0":
        x_1 = "lvl"

    if x_2 == "A-Z" or x_2 == "А-Я" or x_2 == "0-100":
        x_2 = "ASC"
    elif x_2 == "Z-A" or x_2 == "Я-А" or x_2 == "100-0":
        x_2 = "DESC"

    rows = get_list_words_dictionary(x_1, x_2)

    for x_3 in rows:
        if str(x_3[0]) == callback_data.bar:
            with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
                f.write(str(x_3[0]))
            with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
                f.write(str(x_3[1]))
            with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
                try:
                    f.write(str(x_3[2]))
                except:
                    f.write("0")
            with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
                f.write(str(x_3[3]))
            with open(f'user/add_004.txt', "w", encoding='utf-8') as f:
                f.write(str(x_3[4]))
            add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Редактировать\n\nСлово: {x_3[1]}\nТранскрипция: {str(x_3[2])}\nПеревод: {x_3[3]}\nВыучено(%): {x_3[4]}", reply_markup=await button_009())).message_id))
            break
#-----------------------------------------------------------------------------------------------------------------------
async def dictionary_001(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "1":
        button = InlineKeyboardBuilder()
        button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="4"))
        add_mode(query.from_user.id, "4")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте слово, которое вы хотите отредактировать", reply_markup=button.as_markup())).message_id))
    elif callback_data.bar == "2":
        button = InlineKeyboardBuilder()
        button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="4"))
        add_mode(query.from_user.id, "5")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте транскрипцию, которую вы хотите отредактировать", reply_markup=button.as_markup())).message_id))

    elif callback_data.bar == "3":
        button = InlineKeyboardBuilder()
        button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="4"))
        add_mode(query.from_user.id, "6")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте перевод, который вы хотите отредактировать", reply_markup=button.as_markup())).message_id))

    elif callback_data.bar == "4":
        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            idd = f.read()
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        lvl = "0"
        edit_words(word, transcription, translation, lvl, idd)

        await bot.answer_callback_query(callback_query_id=query.id, text='Слово отредактированно✅', show_alert=True)
        get_id_message = str((await bot.send_message(query.from_user.id, "Слово отредактированно✅\n\nmenu:", reply_markup=await button_000())).message_id)
        add_message_id_all_messages(get_id_message)
        await asyncio.sleep(2)
        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass

    elif callback_data.bar == "5":

        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            idd = f.read()

        delete_word(idd)

        await bot.answer_callback_query(callback_query_id=query.id, text='Слово удалено✅', show_alert=True)
        get_id_message = str((await bot.send_message(query.from_user.id, "Слово удалено✅\n\nmenu:", reply_markup=await button_000())).message_id)
        add_message_id_all_messages(get_id_message)
        await asyncio.sleep(2)
        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:",
                                        reply_markup=await button_000())
        except:
            pass
#-----------------------------------------------------------------------------------------------------------------------
async def dictionary_002(query: CallbackQuery, callback_data: MyCallback, bot):
    x_1 = get_sorting_words(query.from_user.id)
    x_2 = get_sorting_words(query.from_user.id)

    if x_1 == "A-Z" or x_1 == "Z-A":
        x_1 = "word"
    elif x_1 == "А-Я" or x_1 == "Я-А":
        x_1 = "translation"
    elif x_1 == "0-100" or x_1 == "100-0":
        x_1 = "lvl"

    if x_2 == "A-Z" or x_2 == "А-Я" or x_2 == "0-100":
        x_2 = "ASC"
    elif x_2 == "Z-A" or x_2 == "Я-А" or x_2 == "100-0":
        x_2 = "DESC"

    rows = get_list_words_dictionary(x_1, x_2)

    button = InlineKeyboardBuilder()
    count = 0
    count_1 = (int(callback_data.bar) - 1) * 88 + 1
    count_2 = count_1 + 88
    for x_3 in rows:
        if count >= count_1:
            if count <= count_2:
                if x_1 == "word":
                    button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                elif x_1 == "translation":
                    button.row(InlineKeyboardButton(text=str(x_3[3]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                elif x_1 == "lvl":
                    button.row(InlineKeyboardButton(text=str(x_3[1]), callback_data=MyCallback(foo="dictionary_000", bar=str(x_3[0])).pack()))
                else:
                    break
        count += 1
    if callback_data.bar == "2":
        button.row(InlineKeyboardButton(text="⬅️", callback_data=MyCallback(foo="dictionary", bar="0").pack()))
        button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="1"))
        if count_2 < get_number_of_words():
            button.button(text="➡️", callback_data=MyCallback(foo="dictionary_002", bar="3"))
    else:
        button.row(InlineKeyboardButton(text="⬅️", callback_data=MyCallback(foo="dictionary_002", bar=str(
            int(callback_data.bar) - 1)).pack()))
        button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="1"))
        if count_2 < get_number_of_words():
            button.button(text="➡️", callback_data=MyCallback(foo="dictionary_002", bar=str(int(callback_data.bar) + 1)))
    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Словарь\n\nСортировка: {get_number_of_words()}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def add(query: CallbackQuery, callback_data: MyCallback, bot):
    for x in ["add_000.txt", "add_001.txt", "add_002.txt", "add_003.txt", "add_004.txt"]:
        with open(f'user/{x}', "w", encoding='utf-8') as f:
            f.write("")

    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Добавить слово\n\nСлово:\nТранскрипция*:\nПеревод:\n\n* - необязательно добавлять", reply_markup=await button_003())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def add_000(query: CallbackQuery, callback_data: MyCallback, bot):
    button = InlineKeyboardBuilder()
    button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="3"))
    add_mode(query.from_user.id, "1")

    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте слово, которое вы хотите добавить", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def add_001(query: CallbackQuery, callback_data: MyCallback, bot):
    button = InlineKeyboardBuilder()
    button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="3"))
    add_mode(query.from_user.id, "2")

    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте транскрипцию, которую вы хотите добавить", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def add_002(query: CallbackQuery, callback_data: MyCallback, bot):
    button = InlineKeyboardBuilder()
    button.button(text="Назад", callback_data=MyCallback(foo="exit", bar="3"))
    add_mode(query.from_user.id, "3")

    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Отправьте перевод, который вы хотите добавить", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def add_003(query: CallbackQuery, callback_data: MyCallback, bot):
    with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
        word = f.read()
    with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
        transcription = f.read()
    with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
        translation = f.read()

    add_word(word, transcription, translation)

    await bot.answer_callback_query(callback_query_id=query.id, text='Слово добавленно в словарь✅', show_alert=True)
    get_id_message = str((await bot.send_message(query.from_user.id, "Слово добавлено✅\n\nmenu:", reply_markup=await button_000())).message_id)

    add_message_id_all_messages(get_id_message)

    await asyncio.sleep(2)

    try:
        await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
    except:
        pass
#-----------------------------------------------------------------------------------------------------------------------
async def train(query: CallbackQuery, callback_data: MyCallback, bot):
    if get_number_of_words() == 0:
        await bot.answer_callback_query(callback_query_id=query.id, text='В словаре нет слов❌', show_alert=True)
        get_id_message = str((await bot.send_message(query.from_user.id, "Словарь пустой❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)
        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass
    else:
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Тренировка\n\nmenu:", reply_markup=await button_001())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def train_000(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        await train_callback_0(query)

    else:
        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            IDd = f.read()

        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT lvl FROM words WHERE ID = {IDd}")
        result = cursor.fetchone()[0]
        conn.close()

        if translation.count(callback_data.bar) >= 1:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()

            if str(result) != "100":
                result = int(result) + 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()
            translation = translation.replace("train", "")

            await bot.answer_callback_query(callback_query_id=query.id, text=f'Правильно✅\n\n{translation}', show_alert=True)

            get_id_message = str((await bot.send_message(query.from_user.id, f"Правильно✅\n\n{translation}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.delete_message(query.from_user.id, message_id=int(get_id_message))
            except:
                pass

        elif translation.count(callback_data.bar) == 0:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()
            if str(result) != "0":
                result = int(result) - 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()
            translation = translation.replace("train", "")

            await bot.answer_callback_query(callback_query_id=query.id, text=f'Неправильно❌\n\n{translation}', show_alert=True)

            get_id_message = str((await bot.send_message(query.from_user.id, f"Неправильно❌\n\n{translation}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)
            try:
                await bot.delete_message(query.from_user.id, message_id=int(get_id_message))
            except:
                pass

    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
    row_count = cursor.fetchone()[0]
    conn.close()

    if str(row_count) == "0":
        await bot.answer_callback_query(callback_query_id=query.id, text='Слов не найдено❌', show_alert=True)

        get_id_message = str((await bot.send_message(query.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)

        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass

    else:
        list = []
        if int(row_count) <= 5:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
            random_row = cursor.fetchone()
            bar = str(random_row[0])
            word = str(random_row[1])
            transcription = str(random_row[2])
            good = random_row[3]
            list.append(random_row[3])
            conn.commit()
            conn.close()

            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dictionary ORDER BY RANDOM() LIMIT 4")
            random_rows = cursor.fetchall()
            for row in random_rows:
                list.append(row[3])
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 5")
            random_rows = cursor.fetchall()
            bar = str(random_rows[0][0])
            word = str(random_rows[0][1])
            transcription = str(random_rows[0][2])
            good = random_rows[0][3]
            for row in random_rows:
                list.append(row[3])
            conn.commit()
            conn.close()

        audio = gTTS(text=word, lang="en")
        audio.save(f'user/train_000.mp3')
        audio = FSInputFile(path=f'user/train_000.mp3', filename="audio")
        add_message_id_all_messages(str((await bot.send_audio(query.from_user.id, audio=audio)).message_id))

        random.shuffle(list)

        with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
            f.write(str(bar))

        with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
            f.write("train" + str(good))

        button = InlineKeyboardBuilder()
        for x in list:
            button.row(InlineKeyboardButton(text=x, callback_data=MyCallback(foo="train_000", bar="train" + x[:20]).pack()))
        button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Тренировка - {row_count}\n\nСлово: {word}\nТранскрипция: {transcription}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def train_001(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        await train_callback_0(query)

    else:
        with open(f'user/add_000.txt', "r", encoding='utf-8') as f:
            IDd = f.read()

        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT lvl FROM words WHERE ID = {IDd}")
        result = cursor.fetchone()[0]
        conn.close()

        if translation.count(callback_data.bar) >= 1:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()

            if str(result) != "100":
                result = int(result) + 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()
            translation = translation.replace("train", "")

            await bot.answer_callback_query(callback_query_id=query.id, text=f'Правильно✅\n\n{translation}', show_alert=True)

            get_id_message = str((await bot.send_message(query.from_user.id, f"Правильно✅\n\n{translation}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)

            try:
                await bot.delete_message(query.from_user.id, message_id=int(get_id_message))
            except:
                pass

        elif translation.count(callback_data.bar) == 0:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute(f"UPDATE words SET train = 0 WHERE ID = {IDd}")
            conn.commit()
            conn.close()
            if str(result) != "0":
                result = int(result) - 1
                conn = sqlite3.connect("db_user.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE words SET lvl = {result} WHERE ID = {IDd}")
                conn.commit()
                conn.close()
            translation = translation.replace("train", "")

            await bot.answer_callback_query(callback_query_id=query.id, text=f'Неправильно❌\n\n{translation}', show_alert=True)

            get_id_message = str(
                (await bot.send_message(query.from_user.id, f"Неправильно❌\n\n{translation}")).message_id)
            add_message_id_all_messages(get_id_message)

            await asyncio.sleep(2)
            try:
                await bot.delete_message(query.from_user.id, message_id=int(get_id_message))
            except:
                pass

    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
    row_count = cursor.fetchone()[0]
    conn.close()

    if str(row_count) == "0":

        await bot.answer_callback_query(callback_query_id=query.id, text='Слов не найдено❌', show_alert=True)

        get_id_message = str((await bot.send_message(query.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)

        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass

    else:
        list = []
        if int(row_count) <= 5:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
            random_row = cursor.fetchone()
            bar = str(random_row[0])
            word = str(random_row[3])
            good = random_row[1]
            list.append(random_row[1])
            conn.commit()
            conn.close()

            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dictionary ORDER BY RANDOM() LIMIT 4")
            random_rows = cursor.fetchall()
            for row in random_rows:
                list.append(row[1])
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect("db_user.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 5")
            random_rows = cursor.fetchall()
            bar = str(random_rows[0][0])
            word = str(random_rows[0][3])
            good = random_rows[0][1]
            for row in random_rows:
                list.append(row[1])
            conn.commit()
            conn.close()

        audio = gTTS(text=word, lang="ru")
        audio.save(f'user/train_001.mp3')
        audio = FSInputFile(path=f'user/train_001.mp3', filename="audio")
        add_message_id_all_messages(str((await bot.send_audio(query.from_user.id, audio=audio)).message_id))

        random.shuffle(list)

        with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
            f.write(str(bar))

        with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
            f.write("train" + str(good))

        button = InlineKeyboardBuilder()
        for x in list:
            button.row(InlineKeyboardButton(text=x[:20], callback_data=MyCallback(foo="train_001", bar="train" + x[:20]).pack()))
        button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Тренировка - {row_count}\n\nПеревод: {word}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def train_002(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        await train_callback_0(query)

    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
    row_count = cursor.fetchone()[0]
    conn.close()

    if str(row_count) == "0":

        await bot.answer_callback_query(callback_query_id=query.id, text='Слов не найдено❌', show_alert=True)

        get_id_message = str((await bot.send_message(query.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)

        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass

    else:
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
        random_row = cursor.fetchone()
        conn.commit()
        conn.close()

        audio = gTTS(text=random_row[3], lang="ru")
        audio.save(f'user/train_002.mp3')
        audio = FSInputFile(path=f'user/train_002.mp3', filename="audio")
        add_message_id_all_messages(str((await bot.send_audio(query.from_user.id, audio=audio)).message_id))

        with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[0]))

        with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[1]))

        with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[2]))

        with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[3]))

        button = InlineKeyboardBuilder()
        button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

        add_mode(query.from_user.id, "7")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Тренировка - {row_count}\n\nПеревод: {random_row[3]}\n\nОтправьте слово", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def train_003(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        await train_callback_0(query)
    # ---------------------------------------------------------------------------------------------------------------
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words WHERE train = 1")
    row_count = cursor.fetchone()[0]
    conn.close()

    if str(row_count) == "0":
        await bot.answer_callback_query(callback_query_id=query.id, text='Слов не найдено❌', show_alert=True)

        get_id_message = str((await bot.send_message(query.from_user.id, "Слов не найдено❌\n\nmenu:", reply_markup=await button_000())).message_id)

        add_message_id_all_messages(get_id_message)

        await asyncio.sleep(2)

        try:
            await bot.edit_message_text(chat_id=query.from_user.id, message_id=int(get_id_message), text="menu:", reply_markup=await button_000())
        except:
            pass

    else:
        conn = sqlite3.connect("db_user.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM words WHERE train = 1 ORDER BY RANDOM() LIMIT 1")
        random_row = cursor.fetchone()
        conn.commit()
        conn.close()

        audio = gTTS(text=random_row[1], lang="en")
        audio.save(f'user/train_003.mp3')
        audio = FSInputFile(path=f'user/train_003.mp3', filename="audio")
        add_message_id_all_messages(str((await bot.send_audio(query.from_user.id, audio=audio)).message_id))

        with open(f'user/add_000.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[0]))

        with open(f'user/add_001.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[1]))

        with open(f'user/add_002.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[2]))

        with open(f'user/add_003.txt', "w", encoding='utf-8') as f:
            f.write(str(random_row[3]))

        button = InlineKeyboardBuilder()
        button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="5").pack()))

        add_mode(query.from_user.id, "8")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Тренировка - {row_count}\n\nСлово: {random_row[1]}\n\nОтправьте перевод", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting(query: CallbackQuery, callback_data: MyCallback, bot):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words")
    row_count = cursor.fetchone()[0]
    conn.close()
    add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Настройки\n\nМаксимальное количество слов в тренировке: {get_max_words(query.from_user.id)}\n\
Слова: {get_words(query.from_user.id)}\n\
Выучено (%): от {get_froms(query.from_user.id)}  до {get_before(query.from_user.id)}\n\
Сортировка слов: {get_sorting_words(query.from_user.id)}\n\n\
Количество найденных слов: {row_count}", reply_markup=await button_005())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting_000(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Настройки\n\nМаксимальное количество слов в тренировке: {get_max_words(query.from_user.id)}", reply_markup=await button_008())).message_id))
    else:
        add_max_words(query.from_user.id, max_words=str(callback_data.bar))
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Настройки\n\nМаксимальное количество слов в тренировке: {get_max_words(query.from_user.id)}", reply_markup=await button_008())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting_001(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Слова: {get_words(query.from_user.id)}", reply_markup=await button_007())).message_id))
    else:
        add_words(query.from_user.id, words=callback_data.bar)
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Слова: {get_words(query.from_user.id)}", reply_markup=await button_007())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting_002(query: CallbackQuery, callback_data: MyCallback, bot):
    count = 0
    button = InlineKeyboardBuilder()
    while count <= 50:
        button.row(InlineKeyboardButton(text=str(count), callback_data=MyCallback(foo="setting_002", bar=str(count)).pack()))
        button.button(text=str(count + 1), callback_data=MyCallback(foo="setting_002", bar=str(count + 1)))
        count += 2
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="2").pack()))
    button.button(text="➡️", callback_data=MyCallback(foo="setting_002", bar="112"))
    button_2 = InlineKeyboardBuilder()
    while count <= 99:
        button_2.row(InlineKeyboardButton(text=str(count), callback_data=MyCallback(foo="setting_002", bar=str(count)).pack()))
        button_2.button(text=str(count + 1), callback_data=MyCallback(foo="setting_002", bar=str(count + 1)))
        count += 2
    button_2.row(InlineKeyboardButton(text="100", callback_data=MyCallback(foo="setting_002", bar="100").pack()))
    button_2.row(InlineKeyboardButton(text="⬅️", callback_data=MyCallback(foo="setting_002", bar="111").pack()))
    button_2.button(text="Назад", callback_data=MyCallback(foo="exit", bar="2"))
    if callback_data.bar == "111":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): от {get_froms(query.from_user.id)}", reply_markup=button.as_markup())).message_id))
    elif callback_data.bar == "112":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): от {get_froms(query.from_user.id)}", reply_markup=button_2.as_markup())).message_id))
    else:
        add_froms(query.from_user.id, froms=callback_data.bar)
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): от {get_froms(query.from_user.id)}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting_003(query: CallbackQuery, callback_data: MyCallback, bot):
    count = 0
    button = InlineKeyboardBuilder()
    while count <= 50:
        button.row(InlineKeyboardButton(text=str(count), callback_data=MyCallback(foo="setting_003", bar=str(count)).pack()))
        button.button(text=str(count + 1), callback_data=MyCallback(foo="setting_003", bar=str(count + 1)))
        count += 2
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="2").pack()))
    button.button(text="➡️", callback_data=MyCallback(foo="setting_003", bar="112"))
    button_2 = InlineKeyboardBuilder()
    while count <= 99:
        button_2.row(InlineKeyboardButton(text=str(count), callback_data=MyCallback(foo="setting_003", bar=str(count)).pack()))
        button_2.button(text=str(count + 1), callback_data=MyCallback(foo="setting_003", bar=str(count + 1)))
        count += 2
    button_2.row(InlineKeyboardButton(text="100", callback_data=MyCallback(foo="setting_003", bar="100").pack()))
    button_2.row(InlineKeyboardButton(text="⬅️", callback_data=MyCallback(foo="setting_003", bar="111").pack()))
    button_2.button(text="Назад", callback_data=MyCallback(foo="exit", bar="2"))
    if callback_data.bar == "111":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): до {get_before(query.from_user.id)}", reply_markup=button.as_markup())).message_id))
    elif callback_data.bar == "112":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): до {get_before(query.from_user.id)}", reply_markup=button_2.as_markup())).message_id))
    else:
        add_before(query.from_user.id, before=callback_data.bar)
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Выучено (%): до {get_before(query.from_user.id)}", reply_markup=button.as_markup())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def setting_004(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "0":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Сортировка слов: {get_sorting_words(query.from_user.id)}", reply_markup=await button_006())).message_id))
    else:
        if callback_data.bar == "1":
            add_sorting_words(query.from_user.id, sorting_words="A-Z")
        elif callback_data.bar == "2":
            add_sorting_words(query.from_user.id, sorting_words="Z-A")
        elif callback_data.bar == "3":
            add_sorting_words(query.from_user.id, sorting_words="А-Я")
        elif callback_data.bar == "4":
            add_sorting_words(query.from_user.id, sorting_words="Я-А")
        elif callback_data.bar == "5":
            add_sorting_words(query.from_user.id, sorting_words="0-100")
        elif callback_data.bar == "6":
            add_sorting_words(query.from_user.id, sorting_words="100-0")
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Сортировка слов: {get_sorting_words(query.from_user.id)}", reply_markup=await button_006())).message_id))
#-----------------------------------------------------------------------------------------------------------------------
async def exit(query: CallbackQuery, callback_data: MyCallback, bot):
    if callback_data.bar == "1":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "menu:", reply_markup=await button_000())).message_id))

    elif callback_data.bar == "2":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Настройки\n\nМаксимальное количество слов в тренировке: {get_max_words(query.from_user.id)}\n\
Слова: {get_words(query.from_user.id)}\n\
Выучено (%): от {get_froms(query.from_user.id)}  до {get_before(query.from_user.id)}\n\
Сортировка слов: {get_sorting_words(query.from_user.id)}\n\n\
Количество найденных слов: {get_number_of_words()}", reply_markup=await button_005())).message_id))

    elif callback_data.bar == "3":
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        if len(word) >= 1 and len(translation) >= 1:
            add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Добавить слово\n\nСлово: {word}\nТранскрипция*: {transcription}\nПеревод: {translation}\n\n* - необязательно добавлять", reply_markup=await button_004())).message_id))
        else:
            add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Добавить слово\n\nСлово: {word}\nТранскрипция*: {transcription}\nПеревод: {translation}\n\n* - необязательно добавлять", reply_markup=await button_003())).message_id))

    elif callback_data.bar == "4":
        with open(f'user/add_001.txt', "r", encoding='utf-8') as f:
            word = f.read()
        with open(f'user/add_002.txt', "r", encoding='utf-8') as f:
            transcription = f.read()
        with open(f'user/add_003.txt', "r", encoding='utf-8') as f:
            translation = f.read()
        with open(f'user/add_004.txt', "r", encoding='utf-8') as f:
            lvl = f.read()
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, f"Редактировать\n\nСлово: {word}\nТранскрипция: {transcription}\nПеревод: {translation}\nВыучено(%): {lvl}", reply_markup=await button_002())).message_id))

    elif callback_data.bar == "5":
        add_message_id_all_messages(str((await bot.send_message(query.from_user.id, "Тренировка\n\nmenu:", reply_markup=await button_001())).message_id))
#-----------------------------------------------------------------------------------------------------------------------

#button
#-----------------------------------------------------------------------------------------------------------------------
async def button_000():
    button = InlineKeyboardBuilder()
    button.button(text="📖 Словарь", callback_data=MyCallback(foo="dictionary", bar="0"))
    button.button(text="📝 Добавить", callback_data=MyCallback(foo="add", bar="0"))
    button.row(InlineKeyboardButton(text="👨🏼‍🎓 Тренировка", callback_data=MyCallback(foo="train", bar="0").pack()))
    button.row(InlineKeyboardButton(text="🛠 Настройка", callback_data=MyCallback(foo="setting", bar="0").pack()))

    return button.as_markup()

async def button_001():
    button = InlineKeyboardBuilder()
    button.button(text="Поиск перевода", callback_data=MyCallback(foo="train_000", bar="0"))
    button.row(InlineKeyboardButton(text="Поиск слова", callback_data=MyCallback(foo="train_001", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Написание слова по переводу", callback_data=MyCallback(foo="train_002", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Написание перевода по слову", callback_data=MyCallback(foo="train_003", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))

    return button.as_markup()

async def button_002():
    button = InlineKeyboardBuilder()
    button.button(text="Слово", callback_data=MyCallback(foo="dictionary_001", bar="1"))
    button.row(InlineKeyboardButton(text="Транскрипция", callback_data=MyCallback(foo="dictionary_001", bar="2").pack()))
    button.row(InlineKeyboardButton(text="Перевод", callback_data=MyCallback(foo="dictionary_001", bar="3").pack()))
    button.row(InlineKeyboardButton(text="Сохранить", callback_data=MyCallback(foo="dictionary_001", bar="4").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="dictionary", bar="0").pack()))

    return button.as_markup()

async def button_003():
    button = InlineKeyboardBuilder()
    button.button(text="Слово", callback_data=MyCallback(foo="add_000", bar="0"))
    button.row(InlineKeyboardButton(text="Транскрипция", callback_data=MyCallback(foo="add_001", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Перевод", callback_data=MyCallback(foo="add_002", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))

    return button.as_markup()

async def button_004():
    button = InlineKeyboardBuilder()
    button.button(text="Слово", callback_data=MyCallback(foo="add_000", bar="0"))
    button.row(InlineKeyboardButton(text="Транскрипция", callback_data=MyCallback(foo="add_001", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Перевод", callback_data=MyCallback(foo="add_002", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Сохранить", callback_data=MyCallback(foo="add_003", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))

    return button.as_markup()

async def button_005():
    button = InlineKeyboardBuilder()
    button.button(text="Максимальное количество слов в тренировке", callback_data=MyCallback(foo="setting_000", bar="0"))
    button.row(InlineKeyboardButton(text="Слова", callback_data=MyCallback(foo="setting_001", bar="0").pack()))
    button.row(InlineKeyboardButton(text="От", callback_data=MyCallback(foo="setting_002", bar="111").pack()))
    button.button(text="До", callback_data=MyCallback(foo="setting_003", bar="111"))
    button.row(InlineKeyboardButton(text="Сортировка слов", callback_data=MyCallback(foo="setting_004", bar="0").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="1").pack()))

    return button.as_markup()

async def button_006():
    button = InlineKeyboardBuilder()
    button.button(text="Словам (A-Z)", callback_data=MyCallback(foo="setting_004", bar="1"))
    button.row(InlineKeyboardButton(text="Словам (Z-A)", callback_data=MyCallback(foo="setting_004", bar="2").pack()))
    button.row(InlineKeyboardButton(text="Переводу (А-Я)", callback_data=MyCallback(foo="setting_004", bar="3").pack()))
    button.row(InlineKeyboardButton(text="Переводу (Я-А)", callback_data=MyCallback(foo="setting_004", bar="4").pack()))
    button.row(InlineKeyboardButton(text="Уровню (0-100)", callback_data=MyCallback(foo="setting_004", bar="5").pack()))
    button.row(InlineKeyboardButton(text="Уровню (100-0)", callback_data=MyCallback(foo="setting_004", bar="6").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="2").pack()))

    return button.as_markup()

async def button_007():
    button = InlineKeyboardBuilder()
    button.button(text="Все слова", callback_data=MyCallback(foo="setting_001", bar="Все слова"))
    button.row(InlineKeyboardButton(text="Невыученные слова", callback_data=MyCallback(foo="setting_001", bar="Невыученные слова").pack()))
    button.row(InlineKeyboardButton(text="Выученные слова", callback_data=MyCallback(foo="setting_001", bar="Выученные слова").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="2").pack()))

    return button.as_markup()

async def button_008():
    button = InlineKeyboardBuilder()
    button.button(text="Все слова", callback_data=MyCallback(foo="setting_000", bar="Все слова"))
    button.row(InlineKeyboardButton(text="5", callback_data=MyCallback(foo="setting_000", bar="5").pack()))
    button.row(InlineKeyboardButton(text="10", callback_data=MyCallback(foo="setting_000", bar="10").pack()))
    button.row(InlineKeyboardButton(text="15", callback_data=MyCallback(foo="setting_000", bar="15").pack()))
    button.row(InlineKeyboardButton(text="20", callback_data=MyCallback(foo="setting_000", bar="20").pack()))
    button.row(InlineKeyboardButton(text="25", callback_data=MyCallback(foo="setting_000", bar="25").pack()))
    button.row(InlineKeyboardButton(text="30", callback_data=MyCallback(foo="setting_000", bar="30").pack()))
    button.row(InlineKeyboardButton(text="50", callback_data=MyCallback(foo="setting_000", bar="50").pack()))
    button.row(InlineKeyboardButton(text="100", callback_data=MyCallback(foo="setting_000", bar="100").pack()))
    button.row(InlineKeyboardButton(text="150", callback_data=MyCallback(foo="setting_000", bar="150").pack()))
    button.row(InlineKeyboardButton(text="200", callback_data=MyCallback(foo="setting_000", bar="200").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="exit", bar="2").pack()))

    return button.as_markup()

async def button_009():
    button = InlineKeyboardBuilder()
    button.button(text="Слово", callback_data=MyCallback(foo="dictionary_001", bar="1"))
    button.row(InlineKeyboardButton(text="Транскрипция", callback_data=MyCallback(foo="dictionary_001", bar="2").pack()))
    button.row(InlineKeyboardButton(text="Перевод", callback_data=MyCallback(foo="dictionary_001", bar="3").pack()))
    button.row(InlineKeyboardButton(text="Сохранить", callback_data=MyCallback(foo="dictionary_001", bar="4").pack()))
    button.row(InlineKeyboardButton(text="Удалить", callback_data=MyCallback(foo="dictionary_001", bar="5").pack()))
    button.row(InlineKeyboardButton(text="Назад", callback_data=MyCallback(foo="dictionary", bar="0").pack()))

    return button.as_markup()