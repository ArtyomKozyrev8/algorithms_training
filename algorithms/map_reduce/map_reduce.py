import os
from random import randint
from threading import Thread


class InputData:
    """Parent class for all input data subclasses"""
    def process_data(self):
        """should be implemented in child class. Process input data for Worker"""
        raise NotImplemented


class TextFileData(InputData):
    """Represent text file input"""
    def __init__(self, path):
        self.path = os.path.join(os.getcwd(), path)

    def process_data(self):
        with open(self.path, mode="r") as f:
            return f.read()


class Worker:
    """Parent Worker for all Map Reduce Worker Classes"""
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        """Should be implemented in child class. Map input data and calculate result"""
        raise NotImplemented

    def reduce(self):
        """Should be implemented in child class. Accumulate results from other workers in this worker"""
        raise NotImplemented


class WorkerLineCounter(Worker):
    """Worker for MapReduce which count lines in text file"""
    def map(self):
        lines = 0
        last = None
        for i in self.input_data.process_data():
            last = i
            if i == "\n":
                lines += 1
        if last != "\n" and last is not None:
            lines += 1

        self.result = lines

    def reduce(self, another):
        self.result += another.result


def create_files():
    """Populate current working directory with text files of random length"""
    for i in os.listdir():
        if i.startswith("text"):
            os.remove(os.path.join(os.getcwd(), i))

    for i in range(randint(0, 20)):
        lines = randint(0, 10000)
        with open(f"text-{i}.txt", mode="w") as f:
            for i in range(lines):
                f.write(f"{randint(0, 100000000)}\n")


def give_files():
    """file iterator for Map Reduce"""
    for i in os.listdir():
        if i.startswith("text"):
            yield i


if __name__ == '__main__':
    create_files()  # prepare sample data
    workers = []  # Mapreduce Workers
    for i in give_files():
        workers.append(WorkerLineCounter(TextFileData(i)))

    ths = []  # distribute workers between Threads just as example of use
    for i in workers:
        thr = Thread(target=i.map)
        ths.append(thr)
        thr.start()

    for i in ths:
        i.join()

    # reduce (accumulate) data from workers to one of them
    if len(workers) > 1:
        for i in workers[1::]:
            workers[0].reduce(i)
    if workers:
        print(workers[0].result)
    else:
        print("No files were provided")
    

