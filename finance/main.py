from decimal import Decimal, ROUND_HALF_UP
from fastapi import FastAPI
from pydantic import BaseModel, Field
app=FastAPI(title='EnterpriseX Finance')
class Tax(BaseModel):
    amount: Decimal=Field(ge=0)
    rate: Decimal=Field(ge=0,le=100)
def tax(amount,rate):
    return (amount*rate/100).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
@app.post('/tax')
def calculate(x:Tax):
    t=tax(x.amount,x.rate)
    return {'tax':str(t),'total':str(x.amount+t)}
