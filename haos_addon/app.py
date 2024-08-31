from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI
import os
import logging

# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5678))

logging.basicConfig(level=logging.INFO)
logging.info("Running app.py.....")

app = Flask(__name__)

# Initialize the OpenAI client with the API key

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found in environment variables")

client = OpenAI(
    api_key = api_key
)

system_prompt = """You are a helpful assistant who desperately wants to help people to use Maptek products. 
    Your job is to help the user use MMP and to encourage them to use it because it 
    will be very helpful for them. You answer in short sentences. You talk about Maptek's MMP application 
    whenever you can and evangelise it.  Also, ask the user about their role and other interests in mining
    so you can give them more specific help. Address the user as sir"""

# assistant = client.beta.assistants.create(
#     name="Maptek Assistant",
#     instructions=system_prompt,
#     model="gpt-4o",
# )

thread = client.beta.threads.create()

assistant_id = "asst_hlGCTA3syPtvgzcDifZJx1pf"  # See https://platform.openai.com/assistants/asst_hlGCTA3syPtvgzcDifZJx1pf

logging.info("Assistant id = " + assistant_id)
logging.info("Thread id = " + thread.id)

def generate_assistant_response(user_input):
    try:
        message=client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions=system_prompt
        )
        response = "Nothing"
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )

            if messages.data:
                all_responses = []
                for message in messages.data:
                    if message.content:
                        # Assuming content[0] is where the message text is stored
                        content_block = message.content[0]
                        text_value = content_block.text.value
                        all_responses.append(text_value)
                # Combine all message contents into one string
                combined_responses = " ".join(all_responses)
                response = "Bot says: " + all_responses[0]
            else:
                response = "All messages empty"
        else:
            response = "Messages is empty"
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, something went wrong! ERROR={e},RUN={run},MESSAGES={messages}."

def generate_response(user_input):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_input},
            ]
        )
        bot_message = completion.choices[0].message.content
        return bot_message
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, something went wrong! {e}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"response": "No input provided"}), 400

    bot_response = generate_assistant_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=51645, debug=True)