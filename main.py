import json
import random
import sys

from misskey import Misskey


"""
コンテンツ（ことば）を生成する
"""
def generate_kotoba(base_word) -> str:
    result = "".join(random.sample(base_word, k=len(base_word)))
    return result


"""
一致時に確定演出をつける
"""
def effect(word):
    if word == "よさのあきこ":
        result = "$[rainbow %s]\n$[x2 $[tada :yosano_party:]$[tada :yosano_akiko:]$[tada :yosano_party:]]" % word
    elif word == "レターパック":
        result = "$[rainbow %s]\n$[x2 $[tada :send_money:]]" % word
    else:
        result = word
    return result


"""
misskey トークンを返す

@param credential_path 認証情報のパス
@return トークン

"""
def msky_token(credential_path: str):
    with open(credential_path, 'r') as f:
        credential = json.load(f)
    
    return credential["misskey token"]


"""
misskey 向けメイン処理
"""
def msky_main(base_word):
    token = msky_token('credential.json')
    api = Misskey('misskey.io', i=token)
    content = generate_kotoba(base_word)
    content = effect(content)
    api.notes_create(text=content)
    print('noted "%s"' % content)


"""
botメイン関数

"""
def main(base_word):
    msky_main(base_word)


if __name__ == '__main__':
    main(sys.argv[1])
