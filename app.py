# 1. Import libraries
import uvicorn
from fastapi import FastAPI
from BankCustomerData import BankCustomerData
import pickle

# 2. Create app and classifier objects
app = FastAPI()
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


# 4. Route with a parameter, returns the parameter in a message
@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Welcome {name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the Churn prediction with confidence
@app.post('/predict')
def predict_churn(data: BankCustomerData):
    data = data.model_dump()
    print(data)
    # print('Hello')

    CreditScore = data['CreditScore']
    Balance = data['Balance']
    NumOfProducts = data['NumOfProducts']
    HasCrCard = data['HasCrCard']
    IsActiveMember = data['IsActiveMember']
    EstimatedSalary = data['EstimatedSalary']
    Loyalty = data['Loyalty']
    Geography_Germany = data['Geography_Germany']
    Geography_Spain = data['Geography_Spain']

    prediction = classifier.predict([[CreditScore, Balance, NumOfProducts, HasCrCard, IsActiveMember,
                                      EstimatedSalary, Loyalty, Geography_Germany, Geography_Spain]])
    print(prediction)

    if prediction:
        prediction = 'Customer will leave the Bank'
    else:
        prediction = 'Customer will continue with the Bank'

    return {
        'Prediction Text:': prediction
    }


# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)


'''
input A, output 1
{
  "CreditScore": 0.658,
  "Balance": 0.30512014,
  "NumOfProducts": 0,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 0.9240317 ,
  "Loyalty": 0.20769231,
  "Geography_Germany": 1,
  "Geography_Spain": 0
}

input B, output 0
{
  "CreditScore": 0.658,
  "Balance": 0.30512014,
  "NumOfProducts": 0,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 0.9240317 ,
  "Loyalty": 0.20769231,
  "Geography_Germany": 0,
  "Geography_Spain": 1
}
'''
