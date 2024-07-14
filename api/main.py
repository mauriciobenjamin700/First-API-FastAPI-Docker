from fastapi import FastAPI

from api.routers import api_router

app = FastAPI(title="workoutApi")
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app="main:app",host="0.0.0.0",port="8.0.0.0", log_level="info", reload=True)