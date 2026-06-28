from abc import ABC


class User(ABC):
    def __init__(self, name, email, nid):
        self.naem = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        