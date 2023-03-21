import json
import random
import sys

from misskey import Misskey


sentence_list = [
    'なんだろう、', 'うそつくの', 'やめてもらっていいですか？',
    '不快感を', '覚えた自分に', '驚いたんだよね',
    'それって', 'あなたの', '感想ですよね？',
    'なんか', 'そういうデータ', 'あるんですか？',
    'うそはうそであると', '見抜ける人でないと', '（掲示板を使うのは）難しい',
    'はいか、', 'いいえで', '答えてください',
]

answer_list = set([
    "".join(sentence_list[i:i+3])
    for i in range(0, len(sentence_list), 3)
])


"""
misskey 向けメイン処理
"""
def msky_main():
    token = msky_token('credential.json')
    api = Misskey('misskey.io', i=token)
    content = generate_kotoba()
    content = effect(content)
    api.notes_create(text=content)
    print('noted "%s"' % content)


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
コンテンツ（ことば）を生成する
"""
def generate_kotoba() -> str:
    result = "".join(random.sample(sentence_list, k=3))
    return result


"""
フキダシをつける
一致時に確定演出をつける
"""
def effect(word):
    if word in answer_list:
        result = "$[rainbow $[tada %s]]" % word
    else:
        result = word
    result = ":left_side_balloon_with_tail:" + result
    return result


"""
botメイン関数

"""
def main():
    msky_main()


if __name__ == '__main__':
    main()
