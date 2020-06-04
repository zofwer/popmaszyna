import MusicHandler

def main():
    print("Witaj w sklejaku sampli!\nSklei on dla ciebie dostępne sample w dłuższy plik .wav")
    cont = True  # describes if we want to add more samples to merge
    outputpath = input('Zdefiniuj ścieżkę wyjściową (*.wav):\n')
    musichandler = MusicHandler.MusicHandler(outputpath)  # creating object to work on
    musichandler.scanSavedSample()  # scanning for samples in folder "samples"

    while cont:
        print('Wpisz numer dostępnego sampla którego chcesz dokleić')
        musichandler.printSavedSamples()
        num = input('Numer sampla do dodania:\n')
        while int(num) < 1 or int(num) > len(musichandler.returnSavedSamples()): # if given number is invalid
            num = input('Podaj POPRAWNY numer sampla do dodania:\n') # ask for valid number again
        musichandler.addSampleToMerge(int(num)-1)
        decision = input('Czy chcesz kontynować sklejanie?\n')
        if int(decision) != 1:
            cont = False
            print('Koniec')
        else:
            print('Kontynuujemy')

    try:
        musichandler.mergeSamples()  # merging chosen samples into one file
        musichandler.saveMergedSamples()  # exporting merged samples to output file
        print(f'Twoja sklejka została zapisana do ./{outputpath}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
