from pydantic import BaseModel


class BankCustomerData(BaseModel):
    CreditScore: float
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Loyalty: float
    Geography_Germany: int
    Geography_Spain: int

    model_config = {
        "json_schema_extra": {
            "examples": [
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
            ]
        }
    }
