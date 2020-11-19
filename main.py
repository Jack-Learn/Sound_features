import os
import librosa
from wav_plot import Wav_plot


def main():
    audio_path = 'D:\DATASET\鳥叫聲\白頭翁'
    audio_name = '國立臺北科技大學29.wav'
    # 讀檔
    sig, sr = librosa.load(os.path.join(audio_path, audio_name))
    # 設定參數
    wav_plot = Wav_plot(sig, sr, audio_name)

    # wav_plot.time_wave()
    wav_plot.Mel_spec()


if __name__ == "__main__":
    main()