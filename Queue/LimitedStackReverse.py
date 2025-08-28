
def reverseQueue(Queue):
    if Queue.isEmpty():
        return
    else:
        item=Queue.dequeue()
        reverseQueue(Queue)
        Queue.enqueue(item)
        return Queue