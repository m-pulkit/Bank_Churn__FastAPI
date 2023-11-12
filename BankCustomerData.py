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
