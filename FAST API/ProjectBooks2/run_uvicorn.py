import uvicorn

if __name__ == "__main__":
    uvicorn.run("books2:app", reload=True)