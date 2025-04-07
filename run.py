from app import create_app
import os
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("Please Set Mongo URI for MongoDB Atlas using export\nEnsure URI is Parsed!")
    exit(1)
    
app = create_app()
app.config['SECRET_KEY'] = os.urandom(32)
if __name__ == "__main__":
    app.run('0.0.0.0', port=1000, debug=True)