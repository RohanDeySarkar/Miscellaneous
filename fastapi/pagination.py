from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with your actual data source)
data = [
    {"id": 1, "name": "Product A"},
    {"id": 2, "name": "Product B"},
    {"id": 3, "name": "Product C"},
    {"id": 4, "name": "Product D"},
    {"id": 5, "name": "Product E"},
    {"id": 6, "name": "Product F"},
    {"id": 7, "name": "Product G"},
    {"id": 8, "name": "Product H"},
    {"id": 9, "name": "Product I"},
    {"id": 10, "name": "Product J"},
]

@app.route('/products', methods=['GET'])
def get_products():
    page = int(request.args.get('page', 1))  # Get page number from query parameter
    per_page = int(request.args.get('per_page', 10))  # Get items per page from query parameter

    start = (page - 1) * per_page
    end = start + per_page

    total_pages = (len(data) + per_page - 1) // per_page  # Calculate total pages

    return jsonify({
        'data': data[start:end],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': len(data),
            'total_pages': total_pages,
        }
    })

if __name__ == '__main__':
    app.run(debug=True)