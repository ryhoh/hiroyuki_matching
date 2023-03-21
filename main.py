import json
import random
import sys

from misskey import Misskey


emoji_list = {
    "よ": ":_yo:",
    "さ": ":_sa:",
    "の": ":_no:",
    "あ": ":_a:",
    "き": ":_ki:",
    "こ": ":_ko:",
    "レ": ":_re:",
    "タ": ":_ta:",
    "ー": ":_prolong:",
    "パ": ":_pa:",
    "ッ": ":_ltsu:",
    "ク": ":_ku:",
    "で": ":_de:",
    "現金": "::",
    "送れ": "::",
}


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
        result = "$[spin.left,speed=2s $[position.x=2 $[spin.speed=1s \
$[position.x=2 $[spin.left,speed=2s $[rainbow 　　　　　%s]]]]]]\
\n\n$[x2 $[rainbow $[tada :yosano_party:]$[tada :yosano_akiko:]$[tada :yosano_party:]]]" % word
    elif word == "レターパック":
        result = "$[spin.left,speed=2s $[position.x=2 $[spin.speed=1s \
$[position.x=2 $[spin.left,speed=2s $[rainbow 　　　　　%s]]]]]]\
\n\n$[rainbow $[tada :send_money:]]" % word
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
    content = msky_emoji_replace(content)
    api.notes_create(text=content)
    print('noted "%s"' % content)


"""
Misskey カスタム絵文字に置き換える
"""
def msky_emoji_replace(content):
    for emoji in emoji_list:
        content = content.replace(emoji, emoji_list[emoji])
    return content


"""
botメイン関数

"""
def main(base_word):
    msky_main(base_word)


if __name__ == '__main__':
    main(sys.argv[1])
