import os
import librosa
from wav_plot import Wav_plot
import matplotlib.pyplot as plt


def main():
    audio_path = 'D:\DATASET\鳥叫聲\樹鵲'
    audio_name = '國立臺北大學 - 三峽校區2.wav'
    ## 讀檔
    sig, sr = librosa.load(os.path.join(audio_path, audio_name))
    ## 初始化參數
    audio1 = Wav_plot(sig, sr, audio_name)

    ## data augmentation
    ## Time Stretch(時間尺度變換)
    sig_ts = librosa.effects.time_stretch(sig,
                                          rate=1.2)  # rate > 1 加速，rate < 1 減速
    audio2 = Wav_plot(sig_ts, sr, 'Time Stretch')

    ## Pitch Shift
    sig_ps = librosa.effects.pitch_shift(sig, sr, n_steps=6)  # n_steps控制音調變化尺度
    audio3 = Wav_plot(sig_ps, sr, 'Pitch Shift')

    ## 畫圖
    # audio1.time_wave()
    # audio2.time_wave()
    # plt.show()
    # audio1.frequence_wavform()
    # audio3.frequence_wavform()
    # plt.show()
    audio1.Mel_spec()
    audio2.Mel_spec()
    audio3.Mel_spec()
    plt.show()


if __name__ == "__main__":
    main()