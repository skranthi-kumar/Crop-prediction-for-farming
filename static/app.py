# # 

# from flask import Flask, request, render_template
# import numpy as np
# import pickle

# # Importing model and scalers
# model = pickle.load(open('model.pkl', 'rb'))
# sc = pickle.load(open('standscaler.pkl', 'rb'))
# ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# # Creating Flask app
# app = Flask(__name__)

# # Define root route to render index.html
# @app.route('/')
# def index():
#     return render_template("index.html")

# # Define route to handle form submission and predict crop
# @app.route("/predict", methods=['POST'])
# def predict():
#     # Get user input data from the form
#     N = float(request.form['Nitrogen'])
#     P = float(request.form['Phosporus'])
#     K = float(request.form['Potassium'])
#     temp = float(request.form['Temperature'])
#     humidity = float(request.form['Humidity'])
#     ph = float(request.form['Ph'])
#     rainfall = float(request.form['Rainfall'])

#     # Scale the input data
#     input_data = np.array([N, P, K, temp, humidity, ph, rainfall]).reshape(1, -1)
#     scaled_data = sc.transform(ms.transform(input_data))

#     # Predict crop using the model
#     prediction = model.predict(scaled_data)

#     # Dictionary mapping crop IDs to crop names
#     crop_dict = {
#         1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
#         8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
#         14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
#         19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
#     }

#     # Get the crop name based on the prediction
#     if prediction[0] in crop_dict:
#         crop = crop_dict[prediction[0]]
#         result = "{} is the best crop to be cultivated right there".format(crop)
#     else:
#         result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    
#     # Render index.html template with the prediction result
#     return render_template('index.html', result=result)

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, request, render_template
import numpy as np
import pickle

# Importing model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Creating Flask app
app = Flask(__name__)

# Define root route to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# Define route to handle form submission and predict crop
@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get user input data from the form
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        # Validate input data (add additional checks as needed)
        if not (0 <= temp <= 50 and 0 <= humidity <= 100 and 0 <= ph <= 14):
            raise ValueError("Invalid input values")

        # Scale the input data
        input_data = np.array([N, P, K, temp, humidity, ph, rainfall]).reshape(1, -1)
        scaled_data = sc.transform(ms.transform(input_data))

        # Predict crop using the model
        prediction = model.predict(scaled_data)

        # Dictionary mapping crop IDs to crop names
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        # Get the crop name based on the prediction
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = "{} is the best crop to be cultivated right there".format(crop)
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    
    except Exception as e:
        result = f"Error: {str(e)}"

    # Render index.html template with the prediction result
    return render_template('index.html', result=result)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=50001)


# from flask import Flask, request, render_template
# import numpy as np
# import pickle

# # Importing model and scalers
# model = pickle.load(open('model.pkl', 'rb'))
# sc = pickle.load(open('standscaler.pkl', 'rb'))
# ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# # Define a dictionary mapping crop IDs to image filenames
# crop_images = {
#     1: 'Rice.jpg',
#     2: 'Maize.jpg',
#     3: 'Jute.jpg',
#     4: 'Cotton.jpg',
#     5: 'Coconut.jpg',
#     6: 'Papaya.jpg',
#     7: 'Orange.jpg',
#     8: 'Apple.jpg',
#     9: 'Muskmelon.jpg',
#     10: 'Watermelon.jpg',
#     11: 'Grapes.jpg',
#     12: 'Mango.jpg',
#     13: 'Banana.jpg',
#     14: 'Pomegranate.jpg',
#     15: 'Lentil.jpg',
#     16: 'Blackgram.jpg',
#     17: 'Mungbean.jpg',
#     18: 'Mothbeans.jpg',
#     19: 'Pigeonpeas.jpg',
#     20: 'Kidneybeans.jpg',
#     21: 'Chickpea.jpg',
#     22: 'Coffee.jpg'
# }

# # Creating Flask app
# app = Flask(__name__)

# # Define root route to render index.html
# @app.route('/')
# def index():
#     return render_template("index.html")

# # Define route to handle form submission and predict crop
# @app.route("/predict", methods=['POST'])
# def predict():
#     try:
#         # Get user input data from the form
#         N = float(request.form['Nitrogen'])
#         P = float(request.form['Phosporus'])
#         K = float(request.form['Potassium'])
#         temp = float(request.form['Temperature'])
#         humidity = float(request.form['Humidity'])
#         ph = float(request.form['Ph'])
#         rainfall = float(request.form['Rainfall'])

#         # Validate input data (add additional checks as needed)
#         if not (0 <= temp <= 50 and 0 <= humidity <= 100 and 0 <= ph <= 14):
#             raise ValueError("Invalid input values")

#         # Scale the input data
#         input_data = np.array([N, P, K, temp, humidity, ph, rainfall]).reshape(1, -1)
#         scaled_data = sc.transform(ms.transform(input_data))

#         # Predict crop using the model
#         prediction = model.predict(scaled_data)

#         # Get the crop name and image filename based on the prediction
#         if prediction[0] in crop_images:
#             crop_name = crop_images[prediction[0]]
#             image_path = f"static/{crop_name}"
#             result = f"{crop_name} is the best crop to be cultivated right there"
#         else:
#             result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

#     except Exception as e:
#         result = f"Error: {str(e)}"

#     # Render index.html template with the prediction result and image path
#     return render_template('index.html', result=result, image_path=image_path)

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
