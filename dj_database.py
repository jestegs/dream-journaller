"""
Manage database operations.
"""

import sqlite3
from file_paths import DATABASE, NEW_PARA

connect = sqlite3.connect(DATABASE)
cursor = connect.cursor()


# cursor.fetchall() - get the action from a cursor execution


def tag_str_to_list(tags):
    """
    Turns the stored string of tags into a list.

    :param tags: The string of tags, separated by ", "
    :return: A list containing all tags in parameter "tags"
    """
    tags_list = tags.split(", ")
    tags_list.sort()
    return tags_list


def tag_list_to_str(tag_list):
    """
    Join the list of tags to a string for database storage.

    :param tag_list: A list of an entry's tags.
    :return: A string of tags, separated by ", "
    """
    return ", ".join(tag_list)


def get_largest_id():
    """
    Return the largest dream number in the table "dreams".

    :return: The largest dream number/id in "dreams".
    """
    with connect:
        cursor.execute("SELECT MAX(CAST(Id AS INT)) FROM dreams")

    fetch = cursor.fetchone()[0]

    if fetch is None:
        return 0
    else:
        return int(fetch)


def insert_from_gui(journal, dream_id, title, date, tags, body, overwrite=False):
    """
    Insert an entry into the database.
    Removes tabs and replaces newline characters for internal storage.

    :param journal: The name of the journal the entry will be entered under.
    :param dream_id: The number of the entry.
    :param title: The title of the journal entry.
    :param date: The date of the entry.
    :param tags: The tags associated with the entry.
    :param body: The actual entry itself.
    :param overwrite: Whether or not the entry will overwrite an equivalent dream id.
    :return: Error code to report back to the calling method.
        0: Successful entry into database.
        -1: Dream id is a duplicate and isn't allowed to overwrite.
        -2: Dream id is not a number
        -3: The entry title or body is empty.
        -4: No journal is chosen.
    """
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
    """
    Return a list containing all content of an entry from a database.
    Format: (id, title, date, tags, body).
    Adds a tab character to the start of each paragraph and replaces the NEW_PARA constant with a newline character.

    :param dream_id: The id of the entry to retrieve.
    :return: A list containing the content in the entry.
    """
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
    """
    Retrieve an entire journal.

    :param journal_name: The name of the journal to return.
    :return: All the entries within param journal_name
    """
    with connect:
        cursor.execute(
            "SELECT Id, Title, Date, Tags, Body FROM dreams WHERE Journal=:journal_name ORDER BY Id",
            {'journal_name': journal_name}
        )

    return cursor.fetchall()


def get_all_dreams():
    """
    Retrieve all dreams in the database ordered by id.

    :return: Every entry in the database.
    """
    with connect:
        cursor.execute(
            "SELECT Id, Title, Date, Tags, Body FROM dreams ORDER BY Id"
        )

    return cursor.fetchall()


def delete_entry(dream_id):
    """
    Delete an entry from the database.

    :param dream_id: The number/id of the entry to be deleted.
    """
    with connect:
        cursor.execute("DELETE FROM dreams WHERE Id=:dream_id", {"dream_id": dream_id})

    print("Deleted dream with id '" + dream_id + "'")

    connect.commit()


def delete_journal(journal_name):
    """
    Delete an entire journal.

    :param journal_name: The name of the journal to be deleted.
    """
    with connect:
        cursor.execute("DELETE FROM dreams WHERE Journal=:journal_name", {"journal_name": journal_name})
        cursor.execute("DELETE FROM journal_names WHERE JName=:journal_name", {"journal_name": journal_name})

    print("Deleted journal '" + journal_name + "'")

    connect.commit()


def create_dreams_table():
    with connect:
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='dreams'")
        if cursor.fetchone()[0] == 1:
            print("Table dreams already exists. Continuing...")
        else:
            print("Table dreams does not exist. Creating...")

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

            print("Table dreams created.")

    connect.commit()


def erase_dreams_table():
    with connect:
        cursor.execute("DROP TABLE dreams")

    create_dreams_table()

    connect.commit()


def create_tags_list():
    with connect:
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tags'")
        if cursor.fetchone()[0] == 1:
            print("Table tags already exists. Continuing...")
        else:
            print("Table tags does not exist. Creating...")
            cursor.execute(
                """CREATE TABLE tags (
                Tag text
                )"""
            )
            print("Table tags created.")

    connect.commit()


def erase_tags_list():
    with connect:
        cursor.execute("DROP TABLE tags")
    create_tags_list()
    connect.commit()


def get_tags():
    """
    Retrieve all the tags from the tags database.

    :return: A list of every tag added to the database.
    """
    with connect:
        cursor.execute("SELECT * FROM tags ORDER BY Tag")
    tags = []
    for item in cursor.fetchall():
        tags.append(item[0])
    return tags


def add_tag(tag):
    """
    Add a tag to the tags database.

    :param tag: Tag to add.
    """
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
    """
    Delete a tag from the tags database.

    :param tag: Tag to be deleted.
    """
    with connect:
        cursor.execute("DELETE FROM tags WHERE Tag=:tag", {"tag": tag})

    connect.commit()


def create_journ_name_table():
    with connect:
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='journal_names'")
        if cursor.fetchone()[0] == 1:
            print("Table journal_names already exists. Continuing...")
        else:
            print("Table journal_names does not exist. Creating...")
            cursor.execute(
                """CREATE TABLE journal_names (
                JName text
                )"""
            )
            print("Table journal_names created.")

    connect.commit()


def erase_journ_name_table():
    with connect:
        cursor.execute("DROP TABLE journal_names")
    create_journ_name_table()
    connect.commit()


def add_journal(journal_name):
    """
    Add a journal to the journal database.

    :param journal_name: Name of the new journal.
    :return: Error codes
        None: journal_name is blank
        -1: journal_name already exists
    """
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
    """
    Get all existing journal names.

    :return: A list of all existing journal names.
    """
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
