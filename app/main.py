import uvicorn
from app._init_ import create_app 

app = create_app()

if _name_=="_main_":
    uvicorn.run(app, host="0.0.0.0", reload=True)