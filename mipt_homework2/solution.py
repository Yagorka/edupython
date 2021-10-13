import tempfile
import os


class File:

    def __init__(self, filename):
        if not os.path.exists(filename):
            self.f = open(filename, 'w')
            self.f.close()
        self.filename = filename

    def write(self, string):
        self.f = open(self.filename, 'w')
        self.f.write(string)
        print(len(string))
        self.f.close()

    def read(self):
        object_reader_file = open(self.filename, 'r')
        # print(self.filename)
        text = object_reader_file.read()
        object_reader_file.close()
        return text

    def __add__(self, new):
        # print(tempfile.gettempdir())  # директория для временных файлов
        # print(new.filename)  # название файла второго
        # print(os.getcwd())  # текущая директория
        with open(self.filename, "r") as f1, open(new.filename, "r") as f2:
            text1 = f1.read()
            text2 = f2.read()
            all_text = text1 + text2
        tf = tempfile.NamedTemporaryFile()
        path = os.path.join(tempfile.gettempdir(), tf.name + ".txt")
        # print(path)
        with open(path, "w") as f:
            # print(all_text)
            f.write(all_text)
        return File(path)

    def __str__(self):
        return self.filename

    def __iter__(self):
        file = open(self.filename, "r")
        self.file_iter = list(iter(file.readlines()))
        # print(self.file_iter)
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.file_iter):
            self.count += 1
            return self.file_iter[self.count - 1]
        raise StopIteration


if __name__ == "__main__":
    f = File("ff.txt")
    c = File("tt.txt")
    c.write("ggggggg")
    f.write("hhhhhhh")
    s = f + c
    # print(s.read())
    for i in s:
        print(str(i))
# f.write("ssssssssssss")
# print(f.read())

# f = open("gf.txt",  'w')
# f.write("f jjjfgf ")
# f.close()

# object_reader_file = open("ff.txt", 'r')
# print("ff.txt")
# text = object_reader_file.read()
# object_reader_file.close()
# print(text)
