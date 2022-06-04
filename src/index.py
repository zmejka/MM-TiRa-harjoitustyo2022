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

    run = Main(map_file, used_algorithm)

    run.main()

if __name__ == '__main__':
    main()
