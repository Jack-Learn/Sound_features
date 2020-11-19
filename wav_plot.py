import matplotlib.pyplot as plt
from librosa import display


class Wav_plot():
    def __init__(self, sig, sr, audio_name):
        # super(Wav_plot, self).__init__()
        self.sig = sig
        self.sr = sr
        self.audio_name = audio_name

    # 時域波型
    def time_wave(self):
        plt.figure(figsize=(15, 5))
        display.waveplot(self.sig, sr=self.sr, x_axis='time')
        plt.ylabel('Amplitude')
        plt.title(self.audio_name, fontproperties="Microsoft JhengHei")
        plt.show()
