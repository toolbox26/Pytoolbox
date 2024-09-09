# file_tools.py

class FileTools:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def append_to_file(file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

    @staticmethod
    def count_lines(file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
