from flask import Flask, jsonify, send_file, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Ruta de la documentación Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/services/spec'

# Ruta al fichero api_doc.yaml generado anteriormente
SWAGGER_FILE = 'api_doc.yaml'

# Blueprint para la documentación Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Pruebas"
    }
)

# Registrar el blueprint de Swagger UI
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Ruta para servir el fichero api_doc.yaml
@app.route(API_URL)
def send_spec():
    return send_file(SWAGGER_FILE, mimetype='text/yaml')

# Rutas de ejemplo (puedes ajustarlas según tu API)
@app.route('/posts', methods=['GET'])
def get_posts():
    # Lógica para obtener posts
    posts = [{"id": 1, "title": "Post 1"}, {"id": 2, "title": "Post 2"}]
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    # Lógica para obtener un post por ID
    print(post_id)
    post = {"id": post_id, "title": f"Post {post_id}"}
    return jsonify(post)

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Lógica para actualizar un post por ID
    # (Esta es solo una respuesta de ejemplo)
    updated_post = {"id": post_id, "title": f"Updated Post {post_id}"}
    return jsonify(updated_post)

if __name__ == '__main__':
    app.run(debug=True)
