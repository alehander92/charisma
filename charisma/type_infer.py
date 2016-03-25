#
# Function(
#   name='map'
#   args=Args([
#     Arg(name='a', type=ChaType('Int'))])
#   block=[
#     Assignment(
#       left=Name(name='out')
#       right=ListLiteral(elements=[]))
#      For(
#        index=Name(name='e')
#        sequence=Name(name='sequence')
#        block=[Call(function=Name('push'), args=[Name('out'), Call(function=Name('f'), args=[Name('e')])])])
#      Name('out')]))

from charisma.types import ChaType, ChaUnknownType
from charisma.runtime import Value, ChaRuntimeError

class Node:
    def infer(self, type_env):
        return ChaUnknownType

    def run(self, env):
        return ChaRuntimeError

class Function(Node):
    def infer(self, type_env):
        pass

    def run(self, env):
        pass

class Integer(Node):
    def infer(self, type_env):
        return ChaType('Integer')

    def run(self, env):
        return IntegerValue(self.value)


