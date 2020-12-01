import os
import librosa
from wav_plot import Wav_plot
import matplotlib.pyplot as plt
from scipy import signal


def main():
    audio_path = 'D:\DATASET\冷氣故障聲'
    audio_name = '國立臺北科技大學31.wav'

    # load audio
    sig, sr = librosa.load(os.path.join(audio_path, audio_name), sr=10000)
    ####################################################################################################
    #濾波器
    # fx = 512  #濾波器頻率
    # wn = 2 * fx / sr
    # b, a = signal.butter(8, wn, 'highpass')  #配置濾波器 8 表示濾波器的階數
    # sig = signal.filtfilt(b, a, sig)  #data為要過濾的訊號
    ####################################################################################################
    # 初始化參數
    audio = Wav_plot(sig, sr, audio_name)
    ####################################################################################################
    # data augmentation
    # 對聲音進行擴增
    # Time Stretch(時間尺度變換)
    sig_ts = librosa.effects.time_stretch(sig,
                                          rate=0.8)  # rate > 1 加速，rate < 1 減速
    ts = Wav_plot(sig_ts, sr, 'Time Stretch')
    # Pitch Shift
    sig_ps = librosa.effects.pitch_shift(sig, sr,
                                         n_steps=24)  # n_steps控制音調變化尺度
    ps = Wav_plot(sig_ps, sr, 'Pitch Shift')
    ####################################################################################################

    ## 畫圖
    audio.Mel_spec(fmax=sr / 2)  #fmax跟採樣頻率有關，若fmax提高。採樣頻率也要提高，否則高頻會被切掉
    # audio.frequence_wavform()
    # ts.Mel_spec(fmax=sr / 2)
    # ps.Mel_spec(fmax=sr / 2)
    # audio.Mel_spec(fmax=sr / 2, augment=True)
    plt.show()


if __name__ == "__main__":
    main()