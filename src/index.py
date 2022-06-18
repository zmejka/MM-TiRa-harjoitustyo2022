''' Sovelluksen käynnistys.
    Args:
        map_file : luku välillä 1 - 10, joka indikoi minkä kartta otetaan listalta.
        used_algorithm : luku välillä 1 - 2, 1 = A*, 2 = JPS, 3 = Dijkstra
        heuristic : luku välillä 1 - 3, 1 = manhattan, 2 = euclidean, 3 = diagonal.
'''
from main import Main

def main():
    try:
        map_file = int(input("Anna kartan numero (1-10): "))
        if map_file not in range(1, 11):
            print("Väärä kartta. Valittu kartta numero 1. ")
            map_file = 1
    except TypeError:
        print("Väärä muoto tai jokin meni pieleen. Valittu kartta numero 1. ")
        map_file = 1
    try:
        used_algorithm = int(input("Anna algoritmin koodi 1 = A*, 2 = JPS, 3 = Dijkstra: "))
        if used_algorithm not in range(1, 4):
            print("Väärä koodi. Valittu algoritmi A*. ")
            used_algorithm = 1
    except TypeError:
        print("Väärä muoto tai jokin meni pieleen. Valittu algoritmi A*. ")
        used_algorithm = 1
    if used_algorithm == 1:
        try:
            heuristic = int(input("Heuristiikka. 1= Manhattan, 2= Euclidean, 3= Diagonal: "))
            if heuristic not in [1,2,3]:
                print("Väärä koodi. Valittu heuriistikka - Euclidean. ")
                heuristic = 2
        except TypeError:
            print("Väärä koodi. Valittu heuriistikka - Euclidean. ")
            heuristic = 2
    else:
        heuristic = 0
    run = Main(map_file, used_algorithm, heuristic)
    run.main()

if __name__ == '__main__':
    main()
