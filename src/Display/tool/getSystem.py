import openai

openai.api_key = "sk-************************************************"

def chat(text,
         messages=None,
         settings="",
         max_tokens=2000,
         temperature=1.,
         top_p=.1,
         presence_penalty=0.,
         frequency_penalty=0.):

    # やり取りの管理
    messages = messages if messages is not None else []
    if settings and not messages:
        messages.append({"role": "system", "content": settings})
    messages.append({'role': 'user', 'content': text})


    # APIを叩く、streamをTrueに
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        stream=True
    )
    
    # 返答を受け取り、逐次yield
    response_text = "" 
    for chunk in resp:
        if chunk:
            content = chunk['choices'][0]['delta'].get('content')
            if content:
                response_text += content
                yield content
    else:  #˜
        messages += [{'role': 'assistant', 'content': response_text}]