from datetime import date
from model import Batch, OrderLine

def test_can_allocate_available_qty():
    batch = Batch('batch-01', 'test-table', qty=20, eta=date.today())
    orderLine = OrderLine('order-01', 'test-table', 2)

    batch.allocate(orderLine)

    assert batch.available_quantity == 18