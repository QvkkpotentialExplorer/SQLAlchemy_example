from data import db_session
db_session.global_init('./db/predprof.db')
from data.db_session import db_sess
from data.users import Users

#Обращение к таблице
#db_sess.query(Таблица) - так ты обращаешься к таблице
#db_sess.query(Таблица).filter(Таблица.столбец и условие) - так ты выставляешь фильтр
#db_sess.query(Таблица).filter(Таблица.столбец и условие).all() - так ты достаешь все строки колонки,которые удовлетворяют условию
#db_sess.query(Таблица).filter(Таблица.столбец и условие).first() - так ты достаешь первую строку колонки,которая удовлетворяет условию

#Запись в БД
# 1. users = Users( перечисляешь колнки таблицы и их значения) - создаешь экземпляр строки,привязанную к таблице, в БД
# 2. db_sess.add(users) - добавляешь это в сессию
# 3. db_sess.commit() - комитишь изменения в БД

#Удаление из БД
# 1. user = db_sess.query(Users).filter(Users.id == 1).first() - находим нужную строку
# 2. db_sess.delete(user)
# 3. db_sess.commit()


print(db_sess)
