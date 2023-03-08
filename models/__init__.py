""" Implements the base model for all classe in this project"""
from models.engine.file_storage import FileStorage

FILE_PATH = "file.json"

storage = FileStorage(FILE_PATH)
storage.reload()

