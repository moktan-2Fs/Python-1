from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import random as rd
import txttospee as txt
from ollama import chat
app = FastAPI()

my_posts = [{'title': 'titleof post 1',
             'content': 'contennt of post1',
             'id': 1},
            {'id': 2,
             'title': 'favourite food',
             'content': 'gundruk is my favourite food'}]


def ask_model(user: str) -> str:
    response = chat(model='llama3.1', messages=[
        {'role': 'user',
                 'content': user,
         }
    ])
    return response.message.content


class Post(BaseModel):
    title: str
    content: str


@app.get('/')
def root():
    return {'message': "Welcome to my fastapi learning localhost webpag1!!!!e"}


@app.get('/posts')
def get_post():
    return {'data': my_posts}


# @app.post('/createpost')
# def create_post(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {'newPost': f'Title: {payLoad['title']} Content: {payLoad['content']}'}

# title str, content str,


@app.post('/postss')
def cre_post(post: Post):
    post_dic = post.dict()
    post_dic['id'] = rd.randrange(111, 9999)
    c = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ#$@&*'
    po = ''.join(rd.choices(c, k=9))
    print(po)
    return f"{po} is your id. Please remember and store it somewhere.."


@app.post('/posts')
def create_new_post(new_post: Post):
    dict_post = new_post.dict()
    dict_post['id'] = rd.randrange(111, 9999999)
    my_posts.append(dict_post)
    model_ans = ask_model(new_post.content)
    for _ in my_posts:
        print(_)
    return {'Model::': model_ans}

def find_post(id):
    for di in my_posts:
        for key, value in di.items():
            if key['id'] == id:
                return di
            else:
                continue

@app.get("/posts/{id}")
def get_posts(id):
    find = find_post(id)
    return find