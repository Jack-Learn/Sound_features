import wave
import os
from scipy import signal
import librosa
import soundfile as sf

audio_path = 'D:\DATASET\冷氣故障聲'
audio_name = '國立臺北科技大學31.wav'
# 讀取wav
f = wave.open(os.path.join(audio_path, audio_name), mode='rb')
channels = f.getnchannels()
sampwidth = f.getsampwidth()
sr = f.getframerate()
n = f.getnframes()

sig, sr = librosa.load(os.path.join(audio_path, audio_name),
                       sr=44100,
                       duration=None)

f.close()

######################################## 濾波器 #######################################################
fx = 1024  #濾波器頻率
wn = 2 * fx / sr
b, a = signal.butter(8, wn, 'highpass')  #配置濾波器 8 表示濾波器的階數
# sig = signal.filtfilt(b, a, sig)  #data為要過濾的訊號
sf.write('stereo_file2.wav', sig, sr)

# # 寫入wav
# f = wave.open('weite_test.wav', 'wb')
# # 配置声道数、量化位数和取样频率
# f.setnchannels(channels)
# f.setsampwidth(sampwidth)
# f.setframerate(sr)
# # 将wav_data转换为二进制数据写入文件
# f.writeframes(sig)
# f.close()