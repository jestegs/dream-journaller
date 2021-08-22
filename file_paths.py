"""
Contains the file paths for the project and handles
directory/file operations.
"""

import os

# declare path literals

PROGRAM_DIR = os.getcwd()

DATABASE = os.path.join(PROGRAM_DIR, "dream_journals.db")

NEW_PARA = "NEW_PARAGRAPH"
