import whisper 

import deepl 
import env

model = whisper.load_model('large')
result = model.transcribe('Untitled (2).mp4')
print(f"英文: {result['text']}")

deepl.deepl_text(env.os.environ.get('DEEPL_API'), result['text'])
