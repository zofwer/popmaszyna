from pydub import AudioSegment
import os


class MusicHandler:
    def __init__(self, savepath):  # constructor for out object. Defined path to save file as savepath, saved_samples
        # is a list of detected samples, samples is a list of samples to merge, to_save is our buffer that will be
        # saved to file
        self.savepath = os.path.normpath(savepath)
        self.saved_samples = []
        self.samples = []
        self.to_save = AudioSegment.empty()

    def scanSavedSample(
            self):  # scanning dictionary 'samples' for samples XD, you might add checking, if founded file is .wav
        for path in os.listdir('samples'):
            full_path = os.path.join('samples', path)
            if os.path.isfile(full_path):
                self.saved_samples.append(os.path.normpath(full_path))

    def printSavedSamples(self):  # printing all detected samples (inline for)
        return [print(f'{iteration}: {path}') for iteration, path in enumerate(self.saved_samples)]

    def addSampleToMerge(self, num):  # append sample described as number in saved_samples list to samples
        return True if self.samples.append(self.saved_samples[num]) else False

    def mergeSamples(self):  # add all samples to buffer
        for sample in self.samples:
            self.to_save += AudioSegment.from_wav(sample)

        return self.to_save

    def saveMergedSamples(self):  # export buffer to file
        return True if self.to_save.export(self.savepath, format='wav') else False
