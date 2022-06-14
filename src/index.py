from main import Main

''' Sovelluksen käynnistys.
    Args:
        map_file : luku välillä 1 - 10, joka indikoi minkä kartta otetaan listalta.
        used_algorithm : luku välillä 1 - 2, 1 = A* ja 2 = JPS,
'''
def main():
    try:
        map_file = int(input("Anna kartan numero (1-10): "))
        if map_file not in range(1, 11):
            print("Väärä kartta. Valittu kartta numero 1. ")
            map_file = 1
    except Exception:
        print("Väärä muoto tai jokin meni pieleen. Valittu kartta numero 1. ")
        map_file = 1
    try:
        used_algorithm = int(input("Anna algoritmin koodi 1 = A* tai 2 = JPS: "))
        if used_algorithm not in [1,2]:
            print("Väärä koodi. Valittu algoritmi A*. ")
            used_algorithm = 1
    except Exception:
        print("Väärä muoto tai jokin meni pieleen. Valittu algoritmi A*. ")
        used_algorithm = 1
    if used_algorithm == 1:
        try:
            heuristic = int(input("Valistse heuristiikka. 1 = Manhattan, 2 = Euclidean, 3 = Diagonal: "))
            if heuristic not in [1,2,3]:
                print("Väärä koodi. Valittu heuriistikka - Euclidean. ")
                heuristic = 2
        except Exception:
            print("Väärä koodi. Valittu heuriistikka - Euclidean. ")
            heuristic = 2
    else:
        heuristic = 0
    run = Main(map_file, used_algorithm, heuristic)
    run.main()

if __name__ == '__main__':
    main()
