from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('titanic_survival_model.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    features = pd.DataFrame([data])

    features['Age'] = features['Age'].astype(float)
    features['Sex'] = features['Sex'].map({'male': 0, 'female': 1})
    features['Fare'] = features['Fare'].astype(float)
    features['SibSp'] = features['SibSp'].astype(int)
    features['Parch'] = features['Parch'].astype(int)
    features['Pclass'] = features['Pclass'].astype(int)

    features['Embarked_Q'] = 1 if features['Embarked'].iloc[0] == 'Q' else 0
    features['Embarked_S'] = 1 if features['Embarked'].iloc[0] == 'S' else 0
    features.drop('Embarked', axis=1, inplace=True)

    final_features = features[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S']]

    prediction = model.predict(final_features)

    result = 'Sobreviveria' if prediction[0] == 1 else 'Não sobreviveria'

    return render_template('index.html', prediction_text=f'Resultado: Você {result}')

# if __name__ == '__main__':
#    app.run(debug=True)