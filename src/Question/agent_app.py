import json

# paths
User_Name = "iz"
DB_path = "../DataSave"
template_path = f"{DB_path}/DB-sample.json"
humanity_save_path = f"{DB_path}/User/{User_Name}/humanity.json"



sample_data = ""
with open(template_path,"r",encoding="utf-8")as f:
    for i in f.readlines():
        sample_data += i 

prompt = f"""
「
幼少期に何があったか,
周囲の人の様子,
コンプレックス等の自分のあまり伝えなかった点,
性格の特徴,
信念・価値観,
趣味・興味,
対人関係のスタイル,
感情の反応,
理想・夢,
過去の失敗と学び,
内面の葛藤,
感情のトリガー,
行動のパターン,
思考プロセス,
言動の癖,
価値観の変遷,
自己認識,
対立と解決の方法,
対人関係の歴史,
将来への不安と希望,
容姿
」以上の内容をインタビューをして、以下の`sample-user.json`のようにjson形式でレポートにまとめてください
またインタビューをする際は1つずつ質問してください。

例
```sample-user.json
{sample_data}
```
"""
print(prompt)

#これじゃなくて

# for i in data['questions']:

#     answerOverLine = input(f"今回の質問です。\n{i}はなんですか?")
#     data['answers'][i] = answerOverLine
#     print(f"{i}:{data['answers'][i]}")



# File入力
# with open(humanity_save_path,"w")as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)