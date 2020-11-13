import os
import librosa


def main():
    audio_path = ''
    audio_name = '' 

def load_audio(audio_path,audio_name):
    sig, sr = librosa.load(os.path.join(audio_path,audio_name)) 


if __name__ == "__main__":
    main()