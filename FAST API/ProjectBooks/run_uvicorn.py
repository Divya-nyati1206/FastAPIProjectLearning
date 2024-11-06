import uvicorn

if __name__ == "__main__":
    uvicorn.run("books:app", reload=True)