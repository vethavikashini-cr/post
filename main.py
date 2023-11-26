from fastapi import FastAPI, Response

# I like to launch directly and not use the standard FastAPI startup
import uvicorn
from fastapi import FastAPI, HTTPException
import uvicorn
app = FastAPI()

# In-memory "database" for demonstration purposes
fake_db = {
    1: {"userID": "1", "postID": "1", "postContent": "Hello there!"},
    2: {"userID": "2", "postID": "2", "postContent": "How are you?"},
    3: {"userID": "3", "postID": "3", "postContent": "Nice catching up!"},
}

# GET request to retrieve an item by ID
@app.get("/posts/{post_id}")
def read_item(item_id: int):
    item = fake_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"post_id": item_id, "post_info": item}

# POST request to create a new item
@app.post("/posts/")
def create_item(item_info: dict):
    item_id = max(fake_db.keys(), default=0) + 1
    fake_db[item_id] = item_info
    return {"post_id": item_id, "item_info": item_info}

# PUT request to update an existing item by ID
@app.put("/posts/{post_id}")
def update_item(item_id: int, updated_info: dict):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id].update(updated_info)
    return {"post_id": item_id, "updated_info": updated_info}

# DELETE request to delete an item by ID
@app.delete("/posts/{post_id}")
def delete_item(item_id: int):
    item = fake_db.pop(item_id, None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "deleted_item": item}




uvicorn.run(app, host="0.0.0.0", port=8012)
