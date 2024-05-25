from moviepy.editor import VideoFileClip
import speech_recognition as sr 

import env 
import deepl

# mp4からwavファイル生成
def create_wav(mp4_file):
    clip = VideoFileClip(mp4_file)
    clip.audio.write_audiofile('output.wav')

def translate_text():
    r = sr.Recognizer()
    api = env.os.environ.get('DEEPL_API')
    try:
        with sr.AudioFile('output.wav') as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language='en-US')
            deepl_text = deepl.deepl_text(api, text)
            print(deepl_text)
    except sr.UnknownValueError as e:
        print('音声が読み取れませんでした。', e)


if __name__ == '__main__':
    create_wav('8K9co4OYRlP5APKk.mp4')
    translate_text()

