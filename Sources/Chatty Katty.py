# Imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json

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

# Loads saves. If save doesn't exist, initialize
def load_save():
    # Detect if save exists
    if os.path.exists(SAVE_PATH):
        print("Save file detected!")
        f = open(SAVE_PATH)
        data = json.load(f)
        query = f"Please greet {data['name']} for coming back and comment on the amount of steps that {data['name']} took so far, which is {data['steps']}"
        result = llm.invoke(query)
        print(result.content)
    else:
        print("Save file does not exist!\nCreating a new file!")
        query = "Please greet the new user and ask their name"
        result = llm.invoke(query)
        name = str(input(result.content))
        query = f"Thank {name} for providing their name and ask for which city and state {name} is from and ask to type city and state with city,state format."
        result = llm.invoke(query)
        citystate = str(input(result.content))
        city = citystate.split(',')[0]
        state = citystate.split(',')[1]
        query = f"Thank {name} for providing their city and state, which is {city} and {state}. Compliment {name} on where they live as well."
        result = llm.invoke(query)
        print(result.content)
        jstring = {'name':name, 'city':city, 'state':state, 'steps':0}
        with open(SAVE_PATH, 'w') as f:
            json.dump(jstring, f, indent = 4)
        query = f"Let {name} know that the initial setup is complete."
        result = llm.invoke(query)
        print(result.content)
    return 1


def main():
    load_save()
    return 0

# Main Loop
if __name__ == '__main__':
    main()