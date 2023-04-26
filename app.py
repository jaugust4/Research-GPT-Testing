from flask import Flask, render_template, request
import openai

# Set up local flask server
app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '#insert your openai api key here'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the json POST request
    message = request.json.get("message")
    
    # THIS IS WHERE YOU CAN CHANGE PREVIOUS INPUT AND CREATE FORMATTED RESPONSES
    # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
    message = "Respond as if we are having a casual conversation to the following prompt: " + message

    # Send the message to OpenAI's API and receive the response
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    # return the response
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()