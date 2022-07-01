import os
import json
import pickle

class FileMode:
    READ = "r"
    WRITE = "w"
    APPEND = "a"
    WRITE_BINARY = "wb"
    READ_BINARY = "rb"

class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    @staticmethod
    def file_exists(filepath):
        return os.path.exists(filepath)
    
    def store_text(self, txt):
        with open(self.file_name, self.mode) as file:
            file.write(txt)
    
    def get_text(self):
        with open(self.file_name, self.mode) as file:
            return file.read()
    
    def store_json(self, jdata):
        with open(self.file_name, self.mode) as file:
            json.dump(jdata, file, indent=4)
    
    def get_json(self):
        with open(self.file_name, self.mode) as file:
            return json.load(file)
    
    def store_object(self, o):
        with open(self.file_name, self.mode) as file:
            pickle.dump(o, file)
    
    def get_object(self):
        with open(self.file_name, self.mode) as file:
            return pickle.load(file)