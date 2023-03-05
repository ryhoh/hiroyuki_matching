import json
import random
import sys

from misskey import Misskey
import tweepy


"""
コンテンツ（ことば）を生成する
"""
def generate_kotoba() -> str:
    hiragana = [
        'ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お',
        'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご',
        'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ',
        'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど',
        'な', 'に', 'ぬ', 'ね', 'の',
        'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ',
        'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ',
        'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん', 'ゔ', 'ゕ', 'ゖ'
    ]
    weights = [
        1, 10, 1, 10, 1, 10, 1, 10, 1, 10,
        10, 3, 10, 3, 10, 3, 10, 3, 10, 3,
        10, 3, 10, 3, 10, 3, 10, 3, 10, 3,
        10, 3, 10, 3, 5, 10, 3, 10, 3, 10, 3,
        10, 10, 10, 10, 10,
        10, 3, 3, 10, 3, 3, 10, 3, 3, 10, 3, 3, 10, 3, 3,
        10, 10, 10, 10, 10, 2, 10, 2, 10, 2, 10,
        10, 10, 10, 10, 10, 1, 10, 1, 1, 1, 10, 1, 1, 1
    ]
    result = "".join(random.choices(hiragana, weights=weights, k=3))  # 最初の3文字

    if random.randint(0, 1) == 1:  # 50%の確率で4文字にする
        result += random.choice(hiragana)
    return result


"""
Twitter API を認証して利用できる状態にする

@param credential_path 認証情報のパス
@return tweepyライブラリのAPIオブジェクト

"""
def twit_auth_ret_api(credential_path: str):
    with open(credential_path, 'r') as f:
        credential = json.load(f)
    
    return tweepy.Client(
        bearer_token=None,
        consumer_key=credential["API key"],
        consumer_secret=credential["API Secret"],
        access_token=credential["Token"],
        access_token_secret=credential["Token Secret"],
    )


"""
Twitter 向けメイン処理
"""
def twit_main():
    api = twit_auth_ret_api('credential.json')
    content = generate_kotoba()
    api.create_tweet(text=content)
    print('tweeted "%s"' % content)


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
def msky_main():
    token = msky_token('credential.json')
    api = Misskey('misskey.io', i=token)
    content = generate_kotoba()
    api.notes_create(text=content)
    print('noted "%s"' % content)


"""
botメイン関数

"""
def main():
    # misskey も twitter も、1回の起動で1度だけ投稿
    if sys.argv[1] == 'misskey':
        msky_main()
    elif sys.argv[1] == 'twitter':
        twit_main()
    elif sys.argv[1] == 'all':
        msky_main()
        twit_main()
    else:
        print('invalid argument')

if __name__ == '__main__':
    main()
