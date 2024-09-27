from flask import Flask, request, jsonify
from chains import router_chain

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process_request():
    data = request.json
    query = data.get("query")
    mode = data.get("mode", "chat")  # Default mode is 'chat'

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Route to the appropriate chain based on the mode
    response = router_chain(query, mode)

    return jsonify({"response": response}), 200


# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
