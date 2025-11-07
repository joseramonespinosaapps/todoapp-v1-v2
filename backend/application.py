import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=None)

# servir frontend v1
@app.route('/v1/', defaults={'path': ''})
@app.route('/v1/<path:path>')
def serve_v1(path):
    dist_folder = os.path.join(os.getcwd(), 'frontend-v1', 'dist')
    if path != "" and os.path.exists(os.path.join(dist_folder, path)):
        return send_from_directory(dist_folder, path)
    return send_from_directory(dist_folder, 'index.html')

# servir frontend v2
@app.route('/v2/', defaults={'path': ''})
@app.route('/v2/<path:path>')
def serve_v2(path):
    dist_folder = os.path.join(os.getcwd(), 'frontend-v2', 'dist')
    if path != "" and os.path.exists(os.path.join(dist_folder, path)):
        return send_from_directory(dist_folder, path)
    return send_from_directory(dist_folder, 'index.html')

