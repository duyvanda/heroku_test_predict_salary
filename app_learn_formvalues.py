from flask import Flask,redirect,url_for, render_template, request, session,flash
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	int_features = []
	for x in request.form.values():
		int_features.append(x)
	output = int(int_features[0]) + int(int_features[1]) + int(int_features[2])
	return render_template('index.html', text='Employee Salary should be $ {}'.format(output))

# def predict():
#     experience = int([request.form['experience']][0])
#     test_score = int([request.form['test_score']][0])
#     interview_score = int([request.form['interview_score']][0])
#     final_features  = [[experience,test_score,interview_score]]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2)
#     return render_template('index.html', text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/predict',methods=['POST'])
# def predict():
#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2)
#     return render_template('index.html', text='Employee Salary should be $ {}'.format(output))