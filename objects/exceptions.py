from werkzeug.exceptions import NotFound

class InvalidCurrency(Exception):
    pass

class InsufficientFunds(Exception):
    pass

class InsufficientData(Exception):
    pass

class InvalidRole(Exception):
    pass

class Confuse(Exception):
    pass

class InvalidData(Exception):
    pass