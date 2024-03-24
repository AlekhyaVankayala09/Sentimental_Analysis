import flask
from flask import Flask, render_template, request
import joblib

class ReviewApp(Flask):
    def __init__(self, *args, **kwargs):
        super(ReviewApp, self).__init__(*args, **kwargs)
        self.route('/', methods=['GET'])(self.home)
        self.route('/prediction', methods=['GET', 'POST'])(self.prediction)
        self.model = joblib.load('models/naive_bayes.pkl')

    def home(self):
        return render_template('home.html')

    def prediction(self):
        if request.method == 'POST':
            rev = request.form.get('reviews')
            data_point = [rev]
            prediction = self.model.predict(data_point)
            if prediction[0] == 1:
                result = "😄 Positive Review 😄"
            else:
                result = "☹️ Negative Review ☹️"
            return render_template('result.html', prediction=result)
        return render_template('result.html', prediction="")

app = ReviewApp(__name__)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
