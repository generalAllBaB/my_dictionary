import sqlite3
import datetime

#-----------------------------------------------------------------------------------------------------------------------
def gef_user(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    result = cursor.execute(f"SELECT * FROM `user` WHERE `user_id` = {user_id}").fetchall()
    conn.close()
    return bool(len(result))

def add_user(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO 'user' ('user_id') VALUES ({user_id})")
    conn.commit()
    conn.close()

def add_activity(user_id):
    current_date = datetime.datetime.now()
    current_date = str(current_date.day) + str(current_date.month) + str(current_date.year)
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `activity` = {current_date} WHERE `user_id` = {user_id}")
    conn.commit()
    conn.close()

def add_mode(user_id, mode):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `mode` = {mode} WHERE `user_id` = {user_id}")
    conn.commit()
    conn.close()

def get_mode(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `mode` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def get_sorting_words(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `sorting_words` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def add_max_words(user_id, max_words):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET max_words = ? WHERE user_id = ?", (max_words, user_id))
    conn.commit()
    conn.close()

def get_max_words(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `max_words` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def add_words(user_id, words):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `words` = ? WHERE `user_id` = ?", (words, user_id))
    conn.commit()
    conn.close()

def get_words(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `words` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def add_froms(user_id, froms):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `froms` = {froms} WHERE `user_id` = {user_id}")
    conn.commit()
    conn.close()

def get_froms(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `froms` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def add_before(user_id, before):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `before` = {before} WHERE `user_id` = {user_id}")
    conn.commit()
    conn.close()

def get_before(user_id):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT `before` FROM `user` WHERE `user_id` = {user_id}")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def add_sorting_words(user_id, sorting_words):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `user` SET `sorting_words` = ? WHERE `user_id` = ?", (sorting_words, user_id))
    conn.commit()
    conn.close()
#-----------------------------------------------------------------------------------------------------------------------
def get_number_of_words():
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM words")
    result_words = cursor.fetchone()
    conn.close()
    return result_words[0]

def get_list_words_dictionary(x_1, x_2):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    querys = f"SELECT * FROM words ORDER BY {x_1} {x_2}"
    cursor.execute(querys)
    rows = cursor.fetchall()
    conn.close()
    return rows

def edit_words(word, transcription, translation, lvl, idd):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    query = "UPDATE words SET word = ?, transcription = ?, translation = ?, lvl = ? WHERE id = ?"
    cursor.execute(query, (word, transcription, translation, lvl, idd))
    conn.commit()
    conn.close()

def delete_word(idd):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE ID = ?", (idd,))
    conn.commit()
    conn.close()

def add_word(word, transcription, translation):
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    insert_query = '''
                    INSERT INTO words (word, transcription, translation, lvl)
                    VALUES (?, ?, ?, ?)
                    '''
    cursor.execute(insert_query, (word, transcription, translation, "0"))
    conn.commit()
    cursor.close()
    conn.close()

def update_train_0():
    conn = sqlite3.connect("db_user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE words SET train = 0")
    conn.commit()
    conn.close()