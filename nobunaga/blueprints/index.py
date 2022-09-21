from flask import Blueprint, render_template
from ..utils.rpcutils import RPC

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    blockchaininfo = RPC("getblockchaininfo")
    networkinfo = RPC("getnetworkinfo")
    mempoolinfo = RPC("getmempoolinfo")

    if networkinfo is None or networkinfo is None or mempoolinfo is None:
        return "disconnected"

    networks = [n["name"] for n in networkinfo["networks"] if n["reachable"]]
    networks = ', '.join(networks)

    return render_template(
        'index.html', 
        blockchaininfo=blockchaininfo,
        networkinfo=networkinfo,
        mempoolinfo=mempoolinfo,
        networks=networks
        )
