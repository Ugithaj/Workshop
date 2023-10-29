from numpy import exp, array, random, dot
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
app = FastAPI()
# 3 inputs, one output neural node
synaptic_weights = 2 * random.random((3, 1)) - 1
inputs1= []
#for i in range(3):
 #   value = float(input("Enter a value for color (RGB value in decimal): "))
   # inputs1.append(value)
# Sigmoid (activation function)
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Tinking: multiply inputs with weights
def think(inputs1, synaptic_weights):
  return sigmoid(dot(inputs1, synaptic_weights))

# Training data (we'll use these in a bit)
#train_inputs = array([[0.9, 0.1, 0.1], [0.1, 0.6, 0.2], [0.4, 0.1, 0.1], [0.6, 0.8, 0.1]])
#train_outputs = array([[1, 0, 1, 0]]).T

@app.post("/get_weight/")
async def get_weight_endpoint(
   red_weight: float=Form(...),
   green_weight: float= Form(...),
   blue_weight: float= Form(...)
   ):
   synaptic_weights = [red_weight, green_weight, blue_weight]
   inputs1=array([0.8, 0.3, 0.1])
   return "The color percentage is:", think(inputs1, synaptic_weights)
   #return {"Considering new situation [0.8, 0.3, 0.1] -> ?:", print(think(array([0.8, 0.3, 0.1])))}  
    #return {"Considering new situation [0.2, 0.7, 0.3] -> ?:", print(think(array([0.2, 0.7, 0.3])))}  
       
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>Weigt Input</title>
    </head>
    <body>
        <h1>Weight Input</h1>
        <form method="post" action="/get_weight/">
            <label for="red_weight">Red Weight:</label>
            <input type="number"  name="red_weight" required><br>

            <label for="green_weight">Green Weight:</label>
            <input type="number" name="green_weight" required><br>

            <label for "blue_weight">Blue Weight:</label>
            <input type="number" name="blue_weight" required><br>

            <input type="submit" value="get_weight">
        </form>
    </body>
    </html>
    """
           
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    


