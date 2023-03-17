def user_schema(user) -> dict:
    return {
        "uuid": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }

