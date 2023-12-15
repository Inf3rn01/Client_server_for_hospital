import sqlite3
import os
from settings import DB_PATH
class DBManager:

    def __init__(self, db_path:str) -> None:
        self.db_path = db_path

    def check_base(self, db_path) -> True:
        return os.path.exists(self.db_path)

    def connect_to_db():



    def create_base():


    def execute():





db_manager = DBManager(DB_PATH)