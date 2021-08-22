"""
Manage database operations.
"""

import sqlite3
from file_paths import DATABASE, NEW_PARA

connect = sqlite3.connect(DATABASE)
cursor = connect.cursor()


# cursor.fetchall() - get the action from a cursor execution


def tag_str_to_list(tags):
    tags_list = tags.split(", ")
    tags_list.sort()
    return tags_list


def tag_list_to_str(tag_list):
    return ", ".join(tag_list)


def get_largest_id():
    with connect:
        cursor.execute("SELECT MAX(CAST(Id AS INT)) FROM dreams")

    fetch = cursor.fetchone()[0]

    if fetch is None:
        return 0
    else:
        return int(fetch)


def insert_from_gui(journal, dream_id, title, date, tags, body, overwrite=False):
    if not dream_id.isdigit():
        print("Save aborted. Dream Id must be a number.")
        return -2

    if not title or not body:
        print("Save aborted. Please write some content!")
        return -3

    if journal == "":
        print("Save aborted. Please choose a journal!")
        return -4

    with connect:
        cursor.execute("SELECT Id FROM dreams WHERE Id=:dream_id", {"dream_id": dream_id})
        is_duplicate = cursor.fetchone()
        if not overwrite and is_duplicate:
            print("Duplicate dream id \"" + str(dream_id) + "\" not written to database.")
            return -1
        elif overwrite and is_duplicate:
            print("Duplicate dream \"" + str(dream_id) + "\" overwritten.")
            cursor.execute("DELETE FROM dreams WHERE Id=:dream_id", {"dream_id": dream_id})

        body = body.replace('\n', NEW_PARA)
        body = body.replace('\t', '')

        cursor.execute(
            "INSERT INTO dreams VALUES (?, ?, ?, ?, ?, ?)",
            (journal, dream_id, title, date, tags, body)
        )

    connect.commit()
    return 0


def get_from_gui(dream_id):
    with connect:
        cursor.execute(
            "SELECT Id, Title, Date, Tags, Body FROM dreams WHERE Id=:dream_id",
            {'dream_id': dream_id}
        )

    dream = []
    for item in cursor.fetchone():
        dream.append(item)
    dream[4] = dream[4].replace(NEW_PARA, '\n\t')
    dream[4] = '\t' + dream[4]

    return dream


def get_journal_by_text(journal_name):
    with connect:
        cursor.execute(
            "SELECT Id, Title, Date, Tags, Body FROM dreams WHERE Journal=:journal_name ORDER BY Id",
            {'journal_name': journal_name}
        )

    return cursor.fetchall()


def get_all_dreams():
    with connect:
        cursor.execute(
            "SELECT Id, Title, Date, Tags, Body FROM dreams ORDER BY Id"
        )

    return cursor.fetchall()


def delete_entry(dream_id):
    with connect:
        cursor.execute("DELETE FROM dreams WHERE Id=:dream_id", {"dream_id": dream_id})

    print("Deleted dream with id '" + dream_id + "'")

    connect.commit()


def delete_journal(journal_name):
    with connect:
        cursor.execute("DELETE FROM dreams WHERE Journal=:journal_name", {"journal_name": journal_name})
        cursor.execute("DELETE FROM journal_names WHERE JName=:journal_name", {"journal_name": journal_name})

    print("Deleted journal '" + journal_name + "'")

    connect.commit()


def create_dreams_table():
    with connect:
        cursor.execute(
            """CREATE TABLE dreams (
            Journal text,
            Id integer,
            Title text,
            Date text,
            Tags text,
            Body text
            )"""
        )

    connect.commit()


def erase_dreams_table():
    with connect:
        cursor.execute("DROP TABLE dreams")

    create_dreams_table()

    connect.commit()


def create_tags_list():
    with connect:
        cursor.execute(
            """CREATE TABLE tags (
            Tag text
            )"""
        )

    connect.commit()


def erase_tags_list():
    with connect:
        cursor.execute("DROP TABLE tags")
    create_tags_list()
    connect.commit()


def get_tags():
    with connect:
        cursor.execute("SELECT * FROM tags ORDER BY Tag")
    tags = []
    for item in cursor.fetchall():
        tags.append(item[0])
    return tags


def add_tag(tag):
    if tag == "":
        print("Can't create blank tag")
        return

    with connect:
        for ptag in get_tags():
            if tag == ptag:
                print("Tag " + str(tag) + " already exists!")
                return

        cursor.execute("INSERT INTO tags VALUES (?)", (tag,))

    connect.commit()


def delete_tag(tag):
    with connect:
        cursor.execute("DELETE FROM tags WHERE Tag=:tag", {"tag": tag})

    connect.commit()


def create_journ_name_table():
    with connect:
        cursor.execute(
            """CREATE TABLE journal_names (
            JName text
            )"""
        )

    connect.commit()


def erase_journ_name_table():
    with connect:
        cursor.execute("DROP TABLE journal_names")
    create_journ_name_table()
    connect.commit()


def add_journal(journal_name):
    if journal_name == "":
        print("Can't create blank journal name")
        return

    for journal in get_journal_names():
        if journal == journal_name:
            print("Journal " + journal_name + " already exists!")
            return -1

    with connect:
        cursor.execute("INSERT INTO journal_names VALUES (?)", (journal_name,))

    connect.commit()


def get_journal_names():
    with connect:
        cursor.execute("SELECT * FROM journal_names ORDER BY JName")

    journals = []
    for item in cursor.fetchall():
        journals.append(item[0])
    return journals


def ERASE_ALL_TABLES():
    erase_tags_list()
    erase_dreams_table()
    erase_journ_name_table()


if __name__ == "__main__":
    #ERASE_ALL_TABLES()
    pass
