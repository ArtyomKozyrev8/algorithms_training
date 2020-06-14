from algorithms.queue.queue_impl import MyQueue

def hot_potato(counter: int, names: list) -> None:
    assert isinstance(counter, int), "Counter should be integer"
    assert isinstance(names, list), "names should be list"
    if not names:
        print("names is an empty list")
        return
    # form MyQueue
    q = MyQueue()
    for i in names[::-1]:
        q.enqueue(i)

    while len(q) > 1:
        print(f"Start point: {q}")
        for i in range(1, counter + 1):
            temp = q.dequeue()
            q.enqueue(temp)
            print(f"One step: {q}")
        print(f"Removed: {q.dequeue()}")
    print(f"The last one: {q}")

if __name__ == '__main__':
    hot_potato(2, [1, 2, 3, 4, 5])


