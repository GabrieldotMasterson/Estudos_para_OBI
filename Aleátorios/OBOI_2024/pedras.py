import sys

pedras = int(sys.stdin.readline())

if pedras%3 == 0 or pedras%3 > 1:
    print('Enzo')
else:
    print('Lalic')
