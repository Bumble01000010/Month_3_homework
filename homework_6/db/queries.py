
#--------------------------------------------User--------------------------------------
#____________________________________________Create____________________________________
CREATE_USERS_TABLE= '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    ) 
'''

#____________________________________________Read______________________________________

GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'

#____________________________________________Update____________________________________

INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'
UPDATE_USER_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ?'

#____________________________________________Delete____________________________________

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'

#--------------------------------------------Questions---------------------------------
#____________________________________________Read______________________________________

GET_ALL_QUESTIONS = 'SELECT * from questions'
GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'

#____________________________________________Update_____________________________________

INSERT_QUESTION = 'INSERT INTO questions (question_text, correct) VALUES (?, ?)'

#--------------------------------------------Results------------------------------------
#____________________________________________Update____________________________________

INSERT_RESULT = 'INSERT INTO results (user_id, question_id, is_crrect) VALUES (?, ?, ?)'
#____________________________________________Read_______________________________________

GET_SCORE_BY_USER_ID = 'SELECT COUNT(*) as total, SUM(is_correct) as correct FROM results WHERE user_id = ?'