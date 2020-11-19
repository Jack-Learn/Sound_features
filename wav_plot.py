import matplotlib.pyplot as plt
from librosa import display
import librosa
import numpy as np


class Wav_plot():
    def __init__(self, sig, sr, audio_name):
        # super(Wav_plot, self).__init__()
        self.sig = sig
        self.sr = sr
        self.audio_name = audio_name

    # 時域波型
    def time_wave(self):
        plt.figure()
        display.waveplot(self.sig, sr=self.sr, x_axis='time')
        plt.ylabel('Amplitude')
        plt.title(self.audio_name, fontproperties="Microsoft JhengHei")
        # plt.show()

    def frequence_wavform(self):
        sp = np.fft.fft(self.sig)
        ampSP = np.abs(sp)
        phaseSP = np.unwrap(np.angle(sp))
        time_step = 1. / self.sr
        freqs = np.fft.fftfreq(sp.size, time_step)
        idx = np.argsort(freqs)  # from negative to positive
        title = 'frequence_wavform_' + self.audio_name
        plt.figure()
        plt.title(title)
        plt.plot(freqs[idx[len(idx) // 2:]], ampSP[idx[len(idx) // 2:]])
        plt.xlabel('Hz')
        plt.ylabel('Amplitude')

    #Spectrogram
    def spec(self):
        X = librosa.stft(self.sig)
        Xdb = librosa.amplitude_to_db(X, ref=1.0)
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(
            Xdb,
            sr=self.sr,
            x_axis='time',
            y_axis='linear',
            cmap='jet',
        )
        plt.colorbar(format=' %+2.0f dB ')  # 右邊的色度條
        title = 'spectrogram_' + self.audio_name
        plt.title(title, fontproperties="Microsoft JhengHei")
        plt.show()

    #MFCC Spectrogram
    def Mel_spec(self):
        # 取mfcc係數
        mfccs = librosa.feature.mfcc(y=self.sig, sr=self.sr, n_mfcc=22)
        #計算mel頻譜圖參數
        melspec = librosa.feature.melspectrogram(
            self.sig,
            self.sr,
            n_fft=2048,
            hop_length=512,
            n_mels=128,
        )
        # 轉換為對數刻度
        logmelspec = librosa.power_to_db(np.abs(melspec))
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(
            logmelspec,
            sr=self.sr,
            x_axis="time",
            y_axis='mel',
            cmap='jet',
        )
        plt.colorbar(format=' %+2.0f dB ')  # 右邊的色度條
        title = 'Mel spectrogram_' + self.audio_name
        plt.title(title, fontproperties="Microsoft JhengHei")
        plt.show()
