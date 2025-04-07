from app import create_app
import os
MONGO_USER_NAME = os.getenv("MONGO_USER_NAME")
MONGO_PASS = os.getenv("MONGO_PASS")
if not MONGO_USER_NAME or MONGO_PASS:
    print("Please Set Username and Password for MongoDB Atlas!")
    exit(1)
    
app = create_app()
app.config['SECRET_KEY'] = os.urandom(32)
if __name__ == "__main__":
    app.run('0.0.0.0', port=1000, debug=True)