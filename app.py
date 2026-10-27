from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('car_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs from form (example subset of features)
        data = {
            'enginesize': float(form_val('enginesize')),
            'horsepower': float(form_val('horsepower')),
            'curbweight': float(form_val('curbweight')),
            'highwaympg': float(form_val('highwaympg')),
            'citympg': float(form_val('citympg')),
            'wheelbase': float(form_val('wheelbase')),
            'carwidth': float(form_val('carwidth')),
            'fueltype': request.form.get('fueltype', 'gas'),
            'aspiration': request.form.get('aspiration', 'std'),
            'doornumber': request.form.get('doornumber', 'four'),
            'carbody': request.form.get('carbody', 'sedan'),
            'drivewheel': request.form.get('drivewheel', 'fwd'),
            'enginelocation': request.form.get('enginelocation', 'front'),
            'enginetype': request.form.get('enginetype', 'ohc'),
            'cylindernumber': request.form.get('cylindernumber', 'four'),
            'fuelsystem': request.form.get('fuelsystem', 'mpfi'),
            'brand': request.form.get('brand', 'toyota'),

            'boreratio': float(request.form.get('boreratio', 3.15)),
            'compressionratio': float(request.form.get('compressionratio', 9.0)),
            'stroke': float(request.form.get('stroke', 3.4)),
            'carlength': float(request.form.get('carlength', 175.0)),
            'peakrpm': float(request.form.get('peakrpm', 5000)),
            'carheight': float(request.form.get('carheight', 53.0)),
            'symboling': int(request.form.get('symboling', 0))
        }
        
        df_input = pd.DataFrame([data])
        prediction = model.predict(df_input)[0]
        return render_template('index.html', prediction_text=f"Estimated Car Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

def form_val(key):
    val = request.form.get(key)
    return val if val else 0.0

if __name__ == '__main__':
    app.run(debug=True)
