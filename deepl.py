import requests 


def deepl_text(api, text):
    source_lang = 'EN'
    target_lang = 'JA'

    params = {
        'auth_key': api,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    response = requests.post('https://api-free.deepl.com/v2/translate', data=params)
    result = response.json()['translations'][0]['text']

    print(result)