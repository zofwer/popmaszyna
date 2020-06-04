from pydub import AudioSegment
import os


class MusicHandler:
    def __init__(self, savepath):  # constructor for out object. Defined path to save file as savepath, saved_samples
        # is a list of detected samples, samples is a list of samples to merge, to_save is our buffer that will be
        # saved to file after we add samples to each other
        self.savepath = os.path.normpath(savepath)
        self.saved_samples = []
        self.samples = []
        self.to_save = AudioSegment.empty()

    def scanSavedSample(
            self):  # scanning dictionary 'samples' for samples
        for path in os.listdir('samples'):
            if path[-4:] == '.wav': # check if the file is .wav file
                full_path = os.path.join('samples', path)
                if os.path.isfile(full_path):
                    self.saved_samples.append(os.path.normpath(full_path))

    def printSavedSamples(self):  # printing all detected samples (inline for)
        return [print(f'{iteration+1}: {path}') for iteration, path in enumerate(self.saved_samples)]


    def returnSavedSamples(self):  # return all detected samples as iterable (inline for)
        return [(f'{iteration+1}: {path}') for iteration, path in enumerate(self.saved_samples)]

    def addSampleToMerge(self, num):  # append sample described as number in saved_samples list to samples
        return True if self.samples.append(self.saved_samples[num]) else False

    def mergeSamples(self):  # add all samples to buffer
        for sample in self.samples:
            self.to_save += AudioSegment.from_wav(sample)
        return self.to_save

    # def speed_change(self, speed=1.0, sound):
    #     new_framerate_sound = sound._spawn(sound.raw_data, overrides={
    #         "frame_rate": int(sound.frame_rate * speed)
    #     })
    #     return new_framerate_sound(sound.frame_rate)

    def saveMergedSamples(self):  # export buffer to file
        return True if self.to_save.export(self.savepath+'.wav', format='wav') else False
