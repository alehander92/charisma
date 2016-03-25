class Value:
    def nice(self):
        return 'Value'

class IntegerValue(Value):
    def nice(self):
        return str(self.value)
