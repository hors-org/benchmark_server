from fastapi import FastAPI, Response

bing_page = open("bing.html").read()
so_page = open("so.html").read()


app = FastAPI()


@app.get("/search/")
async def bing_search():
    return Response(content=bing_page, media_type="text/html")



# stackoverflow link begins with `questions`
@app.get("/questions/{id}/{name}")
async def get_question(id: int, name: str):
    # the parameter is useless.
    return Response(content=so_page, media_type="text/html")
