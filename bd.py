import sqlite3


def insert_data(subject: str, dispatch_time:  str, text_message: str):
    try:
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO main.records(subject, dispatch_time, text_message) VALUES(?,?,?)",
                        (subject, dispatch_time, text_message))
    except Exception as e:
        print(e)


def get_data_by_timme(dispatch_time: str) -> list:
    try:
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            user_data = cur.execute("SELECT subject, dispatch_time, text_message FROM records "
                                    "WHERE dispatch_time = ?", (dispatch_time,)).fetchall()
        return user_data
    except Exception as e:
        print(e)


def all_data():
    try:
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM records ").fetchall()
        return data
    except Exception as e:
        print(e)


def del_data(id_data: int):
    try:
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM records WHERE id_data = ?", (id_data,))
    except Exception as e:
        print(e)