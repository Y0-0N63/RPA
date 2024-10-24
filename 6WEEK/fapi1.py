from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() : 
  return{"Hello" : "World"} 

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0) :
  return {"item_id" : item_id, "name" : name, "age" : age}

from fastapi import Form
@app.post("/user")
# ... = 데이터 필수 입력란, 없으면 error(fasAPI이 지정한 것 not 파이썬 문법)
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
  return {"msg": f"{major} {name}님 ({studentcode}) 반갑습니다."}


# 항상 맨 밑에 와야 함!!
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__' :
  import uvicorn
  uvicorn.run(app, host = '127.0.0.1', port = 8000, log_level = "info")