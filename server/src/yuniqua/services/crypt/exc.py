from src.yuniqua.base.exc import YuniquaBaseException

__all__ = ["ObjectForCryptNotProvidedException", "BadObjectTypeProvidedException"]


class ObjectForCryptNotProvidedException(YuniquaBaseException):
    def __init__(self):
        super().__init__(f"Object For Crypt Not Provided")


class BadObjectTypeProvidedException(YuniquaBaseException):
    def __init__(self):
        super().__init__(f"Bad object type")
