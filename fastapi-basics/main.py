from fastapi import FastAPI, HTTPException
from schema import CreateUserSchema, UpdateUserSchema

app = FastAPI()

# In-memory database (dictionary) of users
users_db = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
    3: {"name": "Charlie", "email": "charlie@example.com"},
}

# Static Route
@app.get("/")
def home():
    return {"message": "Welcome to the homepage!"}

# Dynamic Route to fetch user details
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "user_data": user}

# Route to list all users
@app.get("/users")
def list_users(name: str = None, email: str = None):
    if name:
        filtered_users = []
        for  user in users_db.values():
            if user["name"] == name:
                filtered_users.append(user)
        
        return filtered_users
    return {"users": users_db}

# Route to add a new user
@app.post("/users")
def add_user(body: CreateUserSchema):
    user_id = max(users_db.keys()) + 1
    
    users_db[user_id] = {"name": body.name, "email": body.email}
    return {"message": "User added successfully", "user_data": users_db[user_id]}

# Route to update user details
@app.put("/users/{user_id}")
def update_user(user_id: int, body: UpdateUserSchema):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if body.name:
        user["name"] = body.name
    if body.email:
        user["email"] = body.email

    return {"message": "User updated successfully", "user_data": user}