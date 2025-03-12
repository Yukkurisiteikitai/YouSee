from typing import Generator, Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_google_vertexai import ChatVertexAI

DEFAULT_MESSAGE = "What is baseball?"
MODEL = "gemini-1.5-flash-preview-0514"

app = FastAPI()
model = ChatVertexAI(model_name=MODEL, streaming=True)


@app.post("/run_stream")
def stream_response(message: Optional[str] = None) -> StreamingResponse:
    if message is None:
        message = DEFAULT_MESSAGE
    gene = model.stream(message)
    chunk = text_response(gene)

    return StreamingResponse(
        chunk,
        status_code=200,
        headers=None,
        media_type=None,
        background=None,
    )


def text_response(gene: Generator):
    for chunk in gene:
        yield chunk.content
        yield "\n\n--------------------------\n\n"  # ストリーミングの区切りがわかるように



def stream_data(data: str) -> Generator[str, None, None]:
    for word in data:
        yield word
        time.sleep(0.02)

response = requests.post(
            url=URL,
            params=data,
            headers={'accept': 'application/json'},
            stream=True,
        )
st.write_stream(stream_data(response.text))

