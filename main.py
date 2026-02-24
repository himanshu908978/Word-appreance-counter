from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from logic import word_counter,print_lineno

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials = True,
    allow_methods=["*"],
)
class data(BaseModel):
    inp:str
    tar:str

@app.post("/word_counter")
def line_no_of_word(datainp:data):
    inp=datainp.inp
    tar=datainp.tar
    word_line = word_counter(inp,tar)
    # print_lineno(word_line)
    return word_line
