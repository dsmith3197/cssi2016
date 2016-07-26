import Ninja 
import Game 

ninjas = [Ninja('Caro', 5, ['sword', 'dart']), Ninja('Bob', 5, ['sword', 'dart']), Ninja('Xun', 5, ['sword', 'dart']), Ninja('Carl', 5, ['sword', 'dart']), Ninja('Billy Bob', 5, ['sword', 'dart']), Ninja('Angela', 5, ['sword', 'dart']), Ninja('Spongebob', 5, ['sword', 'dart']), Ninja('Jacob', 5, ['sword', 'dart']), Ninja('James', 5, ['sword', 'dart']), Ninja('Nick', 5, ['sword', 'dart'])]

game = Game(ninjas)
game.play()