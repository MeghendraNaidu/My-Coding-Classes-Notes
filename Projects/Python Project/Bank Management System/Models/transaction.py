class Transaction:
    def __init__(self, txn_id, from_acc, to_acc, amount, txn_type, date):
        self.txn_id = txn_id
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.txn_type = txn_type
        self.date = date
