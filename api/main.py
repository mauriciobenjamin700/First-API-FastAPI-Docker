from fastapi import FastAPI

app = FastAPI(title="workoutApi")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app="main:app",host="0.0.0.0",port="8.0.0.0", log_level="info", reload=True)