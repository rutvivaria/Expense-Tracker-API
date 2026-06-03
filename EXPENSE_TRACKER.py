from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

exp=[]
expense_id = 0

class Expenses(BaseModel):
    #expense_id: int
    expense_name: str
    expense_type: str
    expense_description: str
    expense_price: float
    expense_payment_type: str

@app.post("/PostExpense/")
def add_expense(expense: Expenses):
    global expense_id 
    expense_id += 1
    expense_data = expense.dict()
    expense_data["expense_id"] = expense_id
    exp.append(expense_data)
    return {
        "msg": "Expense added successfully",
        "data": exp  
    }

 

@app.get("/GetExpense/")
def get_expense():
    return {
        "msg": "Expense data recieved successfully",
        "data": exp
    }

@app.get("/getExpenseById/{expense_id}")
def get_expense_by_id(expense_id: int):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            return {
                "msg": "Expense data recieved auccessfully",
                "data": expense 
            }
    return{
            "msg": "expense not found"
        }

@app.put("/PutExpenseByid/{expense_id}")
def update(expense_id: int,updated_expense: Expenses):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            expense["expense_name"] = updated_expense.expense_name
            expense[" expense_type"] =  updated_expense.expense_type
            expense["expense_description"] = updated_expense.expense_description
            expense["expense_price"] = updated_expense.expense_price
            expense["expense_payment_type"] = updated_expense.expense_payment_type
            return {
                "msg": "Expense data updated successfully",
                "data": expense
            }
    return{
            "msg": "expense data not found"
        }

@app.delete("/deleteExpense/{expense_id}")
def delete_expense(expense_id: int):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            exp.remove(expense)
            return {
                "msg": "expense data deleted successfully",
                "data": exp 
            }
    return{
            "msg": "expense data not found"
        }


@app.delete("/deleteAllexpense/")
def delete_all_expenses():
    exp.clear()
    return {
        "msg": "All expenses deleted successfully",
        "data": exp
    }

@app.delete("/SoftDeleteExpense/{expense_id}")
def soft_delete_expense(expense_id: int):
    for expense in exp:
        if expense["expense_id"] == expense_id:
            expense["is_deleted"] = True
            return {
                "msg": "expense soft data deleted successfully",
                "data": exp 
            }
    return{
            "msg": "expense data not found"
        }