from collections import deque
import time

class Order:
    def __init__(self, order_id, items, prep_time):
        self.order_id = order_id
        self.items = items
        self.prep_time = prep_time
        self.timestamp = time.time()

class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
        print(f"Order {order.order_id} added.")

    def complete_order(self):
        if self.queue:
            completed_order = self.queue.popleft()
            print(f"Order {completed_order.order_id} completed.")
            return completed_order
        else:
            print("No orders to complete.")
            return None


# Example orders
order1 = Order(1, ["burger", "fries"], 15)
order2 = Order(2, ["pizza"], 20)


order_queue = OrderQueue()

# Add orders to the queue
order_queue.add_order(order1)
order_queue.add_order(order2)

# Complete orders
order_queue.complete_order()
order_queue.complete_order()
order_queue.complete_order()  # Attempt to complete when no orders exist