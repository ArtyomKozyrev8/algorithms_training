"""
I simulate how printer print n pages in the exercise.
The idea of the simulation is that we have a certain number of tasks.
Each task is provided every 180 seconds in a random moment within the 180 seconds interval.
One task is composed of number of pages to print, pages number can be  from 1 to 20 pages per Task.
Printer have several printing speeds.
"""

from random import randint
from algorithms.queue.queue_impl import MyQueue


class Task:
    """Represents the printing Taks"""
    def __init__(self, task_number: int, exp_global_time: int):
        """
        task_number - is the Task order number in our experiment
        exp_global_time - is the time passed from experiment started
        pages_number - is the number of pages to print, can range from 1 to 20 inclusively
        created_at_time - is the moment when task was created from experiment start,
        tasks are created every 180 seconds.
        """
        assert isinstance(task_number, int), "task_number should be integer"
        assert task_number > 0, "task_number should be > 0"
        assert isinstance(exp_global_time, int), "experiment global time should be integer"
        assert  exp_global_time >= 0, "experiment global time should be >= 0"
        self.task_number = task_number
        self.pages_number = randint(1, 20)
        self.global_time = exp_global_time # is used in __repr__ for Trouble Shooting
        self.created_at_time = randint(0, 180) + exp_global_time

    def __repr__(self):
        return f"Task # {self.task_number}(Pages: {self.pages_number} Created: {self.created_at_time} Interval Start: {self.global_time})"


class Printer:
    """The class simulates work of printer"""
    def __init__(self, speed: int = 5):
        """
        last_finished_time - time when last Task was finished used to find out if printer was busy when new Task arrived
        print_queue - printer's task Queueu
        :param speed: number of seconds to print page
        """
        assert isinstance(speed, int), "Printer speed should be integer"
        assert speed in [5, 10, 20, 30, 60], "Printer speed can be 1 page every 5, 10, 20, 30, 60 seconds"
        self.speed = speed
        self.last_finished_time = 0
        self.print_queue = MyQueue()

    def tick(self):
        """simulates how printer do tasks"""
        while not self.print_queue.is_empty():
            current_task = self.print_queue.dequeue()
            # check whether printer was busy when a new Task arrived
            if self.last_finished_time <= current_task.created_at_time:
                self.last_finished_time = current_task.created_at_time

            print(f"Start doing {current_task} at {self.last_finished_time}")
            self.last_finished_time += current_task.pages_number * self.speed
            print(f"Finished doing {current_task} at {self.last_finished_time}\n")

    def add_task(self, task: Task) -> None:
        """Adds Task to the printer Queue"""
        self.print_queue.enqueue(task)


if __name__ == '__main__':
    pr = Printer(30)
    global_time = 0 # experiment start time
    for i in range(1, 21):  # let's create 20 tasks
        task = Task(i, global_time)
        pr.add_task(task)
        global_time += 180 # add new Task to printer every 180 seconds
    pr.tick() # demonstrate how tasks are done
