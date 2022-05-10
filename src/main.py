from random import randrange
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

posts = [
    {"title": "post 1", "content": "content of post 1", "id": 1},
    {"title": "post 2", "content": "content of post 2", "id": 2},
]

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": posts}

@app.get("/posts/{id}")
async def get_post(id):
    post = find_post(id)
    return {"post_detail": post}

@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    posts.append(post_dict)
    return {"message": post}


def find_post(id):
    for post in posts:
        if post['id'] == id:
            return post
