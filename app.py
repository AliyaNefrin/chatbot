from flask import Flask, request, jsonify

app = Flask(__name__)

menu={
    "Biriyani":{"price":250,"available":True},
    "Tandoori Chicken":{"price":350,"available":True},
    "Butter Naan":{"price":40,"available":True},
    "Dragon chicken":{"price":250,"available":False}
}

@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json()
    dish = req["queryResult"]["parameters"]["dish"]
    if dish in menu:
        price = menu[dish]["price"]
        available = "available" if menu[dish]["available"] else"not available"
        response = f"The price of {dish} is ₹{price}. It is currently {available}."
    else:
        response = f"Sorry, we don't have {dish} on our menu."
    return jsonify({"fulfillmentText:response"})

if __name__=='__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)


  