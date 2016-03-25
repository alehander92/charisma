class ChaType:
    def __init__(self, name):
        self.name = name

class ChaUnknownType_(ChaType):
    pass

ChaUnknownType = ChaUnknownType_('Unknown')
