import os
from dotenv import load_dotenv
from flask import Flask

def create_app():
    load_dotenv()

    rpchost = os.getenv("rpchost")
    rpcport = os.getenv("rpcport")
    rpcuser = os.getenv("rpcuser")
    rpcpass = os.getenv("rpcpass")

    if rpchost is None:
        rpchost = "localhost"

    if rpcport is None:
        rpcport = "8332"

    if rpcuser is None or rpcpass is None:
        print("RPC credentials not found on .env file")
        exit()

    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        RPC_URL=f"http://{rpcuser}:{rpcpass}@{rpchost}:{rpcport}"
    )

    from nobunaga.blueprints import index
    app.register_blueprint(index.bp)

    return app
