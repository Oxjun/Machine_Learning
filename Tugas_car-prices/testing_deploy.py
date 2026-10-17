
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Memuat model hasil training
joblib_model = joblib.load("gbr_model.joblib")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API Prediksi Harga Mobil aktif"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        body = request.get_json()

        if not body or "data" not in body:
            return jsonify({"error": "Input harus berisi key data"}), 400

        data = np.asarray(body["data"], dtype=float)

        if data.ndim != 2:
            return jsonify({"error": "Data harus berupa array 2 dimensi"}), 400

        if data.shape[1] != joblib_model.n_features_in_:
            return jsonify({
                "error": "Jumlah fitur tidak sesuai",
                "jumlah_fitur_dibutuhkan": int(joblib_model.n_features_in_),
                "jumlah_fitur_dikirim": int(data.shape[1])
            }), 400

        prediction = joblib_model.predict(data)

        return jsonify({"prediction": prediction.tolist()})

    except Exception as error:
        return jsonify({"error": str(error)}), 400

if __name__ == "__main__":
    app.run(debug=True)
