import MusicHandler


def main():
    cont = True  # describes if we want to add more samples to merge
    outputpath = input('Define output filepath (*.wav):\n')
    musichandler = MusicHandler.MusicHandler(outputpath)  # creating object to work on
    musichandler.scanSavedSample()  # scanning for samples in folder "samples"

    while cont:
        musichandler.printSavedSamples()
        num = input('Number of sample:\n')
        musichandler.addSampleToMerge(int(num))
        dec = input('Do you want to contunue?\n')
        if int(dec) != 1:
            cont = False
            print('Stopped')
        else:
            print('Continuing')

    try:
        musichandler.mergeSamples()  # merging chosen samples into one file
        musichandler.saveMergedSamples()  # exporting merged samples to output file
        print(f'Saved file to ./{outputpath} :)')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
