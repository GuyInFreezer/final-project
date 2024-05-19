# Imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json
from langchain.agents import initialize_agent, load_tools

# Load environment variables.
load_dotenv()

# Set the model name for our LLMs.
OPENAI_MODEL = "gpt-3.5-turbo"
# Store the API key in a variable.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Define save path
SAVE_PATH = './save.json'
# Create LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=0.3)
# Init tools to use
tools = load_tools(['wikipedia', "openweathermap-api"], llm=llm)
# Init agent
agent = initialize_agent(tools, verbose=True, handle_parsing_errors = True, max_iterations=10, llm=llm)

def answer(query):
    result = llm.invoke(query)
    return result.content
    # Add whisper content here when done

# Loads saves. If save doesn't exist, initialize
def load_save():
    # Detect if save exists
    if os.path.exists(SAVE_PATH):
        print("Save file detected!")
        f = open(SAVE_PATH)
        data = json.load(f)
        print(answer(f"Please greet {data['name']} for coming back and comment on the amount of steps that {data['name']} took so far, which is {data['steps']}"))
    else:
        print("Save file does not exist!\nCreating a new file!")
        name = str(input(answer("Please greet the new user and ask their name")))
        citystate = str(input(answer(f"Please greet {data['name']} for coming back and comment on the amount of steps that {data['name']} took so far, which is {data['steps']}")))
        city = citystate.split(',')[0]
        state = citystate.split(',')[1]
        print(answer(f"Thank {name} for providing their city and state, which is {city} and {state}. Compliment {name} on where they live as well."))
        jstring = {'name':name, 'city':city, 'state':state, 'steps':0}
        with open(SAVE_PATH, 'w') as f:
            json.dump(jstring, f, indent = 4)
        print(answer(f"Let {name} know that the initial setup is complete."))
    return 1

def check_weather():
    f = open(SAVE_PATH)
    data = json.load(f)
    weather = agent.run({"input": f"What is the current weather at {data['city']}, {data['state']}?"})
    query = f"I have the weather data as such for my city: '{weather}.' Recommend me to walk outside if the weather is nice, and vice versa. I don't need any verbose information about the weather itself though."
    result = llm.invoke(query)
    return result.content

def chat():
    prompt = ""
    while prompt != "exit":
        prompt = input("Say to Chatty Kathy: ")
        print(answer(prompt))
    return 0

def exit_chatty():
    f = open(SAVE_PATH)
    data = json.load(f)
    print(answer(f"Say goodbye to {data['name']}"))
    quit()

def main():
    load_save()
    print(check_weather())
    chat()
    exit_chatty()
    return 0

# Main Loop
if __name__ == '__main__':
    main()