import os
import openai

from flask import Flask, render_template, request

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt_history="topic: pond\nhaiku: old pond. frog leaps in. water's sound.\n##\ntopic: monkey\nhaiku: the first cold shower. even the monkey seems to want. a little coat of straw.\n##\ntopic: banana\nhaiku: a yellow treat, brightening my day. sweet banana bliss.\n##\ntopic: contact lenses\nhaiku: tiny windows, invisible to all. clear sight in my eyes.\n##\ntopic: batman\nhaiku:  dark knight's cape, soaring the city night. saving the helpless ones.\n##\ntopic: william wallace\nhaiku:  Braveheart with courage, Scotland's hero of truth. William Wallace stands tall.\n##\n"

def get_response(prompt_history, new_topic):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_history + "topic: " + new_topic + "\nhaiku: ",
    temperature=0.8,
    max_tokens=498,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["##"]
  )
  return(response["choices"][0]["text"])
  

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    # Process user_message using your chatbot logic
    # Generate a response
    return render_template('index.html', message=user_message, response=get_response(prompt_history, user_message))

@app.route('/')
def home():
    return render_template('index.html', response='')

if __name__ == '__main__':
    app.run(debug=True)
