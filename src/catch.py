import openai

openai.api_base = "http://localhost:1234/v1"  # LM Studio の API エンドポイント
openai.api_key = "lm-studio"  # APIキーは空欄でOK

converty = []  # 会話履歴を保持するため、ループの外で定義


def ask(question):
    converty.append({"role": "user", "content": question})  # "user" の発言を追加

    try:
        completion = openai.ChatCompletion.create(
            model="deepseek-r1-distill-llama-8b",  # LM Studio で動作しているモデル名
            messages=converty
        )

        answer = completion.choices[0].message.content
        converty.append({"role": "assistant", "content": answer})  # スペル修正済み

        print(answer)

    except Exception as e:
        print("Error:", e)