import MusicHandler
import random
import sys
import platform
system=platform.system() #checking the OS because windows uses different filepaths...
if system == "Windows":
    output_path='outputs'
else:
    output_path='outputs/'


def main():
    print("Witaj w sklejaku sampli!\nSklei on dla ciebie dostępne sample w dłuższy plik .wav")
    cont = True  # describes if we want to add more samples to merge
    outputpath = input('Zdefiniuj ścieżkę wyjściową (*.wav):\n')
    outputpath = output_path+outputpath
    musichandler = MusicHandler.MusicHandler(outputpath)  # creating object to work on
    musichandler.scanSavedSample()  # scanning for samples in folder "samples"

    while cont:
        option=''
        while option != '1' and option!= '2' and option!='q':
            option = input('Wpisz 1 aby dokleić konkretnego sampla\nWpisz 2 aby dokleić losowe sample'
                           '\nWpisz q aby wyjść\n')
        if option == 'q':
            cont=False
            break
        elif option=='1':
            print('Wpisz numer dostępnego sampla którego chcesz dokleić')
            musichandler.printSavedSamples()
            num = input('Numer sampla do dodania:\n')
            if not num.isdigit(): # protection from error coming from wrong input
                num=-1
            while int(num) < 1 or int(num) > len(musichandler.returnSavedSamples()): # if given number is invalid
                num = input('Podaj POPRAWNY numer sampla do dodania:\n') # ask for valid number again
                if not num.isdigit():
                    num = -1

            how_many=input('Ile razy dodać tego sampla? Wpisz 0 aby anulować dodanie go:\n')
            if not how_many.isdigit():
                how_many=-1
            while int(how_many) < 0:
                how_many=input('Podaj POPRAWNĄ liczbę:\n')
                if not how_many.isdigit():
                    how_many = -1

            if how_many != 0:
                for i in range(int(how_many)):
                    musichandler.addSampleToMerge(int(num)-1) # adding sample(s)
        elif option == '2':
            how_many = input('Ile losowych sampli dodać? Wpisz 0 aby anulować:\n')
            if not how_many.isdigit():
                how_many = -1
            while int(how_many) < 0:
                how_many = input('Podaj POPRAWNĄ liczbę:\n')
                if not how_many.isdigit():
                    how_many = -1
            if how_many != 0:
                for i in range(int(how_many)):
                    musichandler.addSampleToMerge(random.randint(0,len(musichandler.returnSavedSamples())-1))  # adding sample(s)

        decision = input('Czy chcesz kontynować sklejanie?\nWpisz 1 aby kontynuować, wpisz cokolwiek innego by skończyć.\n')
        if decision != '1':
            cont = False
            speed=input('Podaj jak zmienić tempo pliku wyjściowego. Wpisz 1 aby pozostało normalne.\n')
            if speed !='1':
                if float(speed) > 1:
                    musichandler.speed_change(float(speed))
                else:
                    print('Niestety program nie zwalnia plików, tempo pozostanie normalne.')
            print('Koniec')
        else:
            print('Kontynuujemy')

    try:

        musichandler.saveMergedSamples()  # exporting merged samples to output file
        print(f'Twoja sklejka została zapisana do {outputpath}')
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()


if __name__ == '__main__':
    main()
