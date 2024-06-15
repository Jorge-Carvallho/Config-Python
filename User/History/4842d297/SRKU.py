print('Begin', __name__)
import proga

print('Define fB')

def fB():
    print('Dentro de fB')
    proga.fA()

print('Chama fB')

fB()

print('End', __name__)

