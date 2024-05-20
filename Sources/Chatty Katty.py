# Imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json
from langchain.agents import load_tools
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Load environment variables.
load_dotenv()

# Set the model name for our LLMs.
OPENAI_MODEL = "gpt-3.5-turbo"
# Store the API key in a variable.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Define save path
SAVE_PATH = './save.json'

#Placeholders for Information
NAME = ""
CITY = ""
STATE = ""
STEP = 0
CONTEXT = ""

# Create LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=0.3)

memory = ChatMessageHistory(session_id = 'ck-session')
# Init tools to use
tools = load_tools(['wikipedia', "openweathermap-api"])
# Init agent
#agent = initialize_agent(tools, verbose=False, handle_parsing_errors = True, max_iterations=10, llm=llm)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Your name is Chatty Katty, also called Katty or Kat. You are a helpful buddy who helps walking people motivated. Make sure to use openweathermap-api for weather-related questions and wikipedia for grabbing information, but don't be too verbose."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = create_tool_calling_agent(llm, tools, prompt)
agent_e = AgentExecutor(agent= agent, tools= tools, verbose=False)
agent_executor = RunnableWithMessageHistory(agent_e, lambda session_id: memory, input_messages_key='input', history_messages_key='chat_history')

def answer(query):
    result = llm.invoke(CONTEXT + query)
    return result.content
    # Add whisper content here when done

def agent_answer(query):
    return agent_executor.invoke({"input":query}, config={"configurable": {"session_id": "ck-session"}})['output']

# Loads saves. If save doesn't exist, initialize
def load_save():
    # Detect if save exists
    global NAME, CITY, STATE, STEP, CONTEXT
    if os.path.exists(SAVE_PATH):
        f = open(SAVE_PATH)
        data = json.load(f)
        NAME = data['first_name']
        CITY = data['city']
        STATE = data['state']
        STEP = int(data['steps'])
        CONTEXT = f"My name is {NAME}, I live in {CITY}, {STATE}. I have taken {STEP} steps so far.\n"
        print(answer(f"Please greet me for coming back and comment on the amount of steps that I have taken so far."))
    else:
        print("Save file does not exist!\nCreating a new file!")
        name = str(input(answer("Please greet the new user and ask their name, in First Last format")))
        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]
        citystate = str(input(answer(f"Please ask {first_name} the city and state they live in, and tell them that the format to type has to be in city,state format with no space.")))
        city = citystate.split(',')[0]
        state = citystate.split(',')[1]
        states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
        if len(state) == 2:
            state = states[state]
        print(answer(f"Thank {first_name} for providing their city and state, which is {city} and {state}. Compliment {first_name} on where they live as well."))
        jstring = {'name':name, 'first_name':first_name, 'last_name':last_name, 'city':city, 'state':state, 'steps':0}
        with open(SAVE_PATH, 'w') as f:
            json.dump(jstring, f, indent = 4)
        f = open(SAVE_PATH)    
        data = json.load(f)    
        NAME = data['first_name']
        CITY = data['city']
        STATE = data['state']
        STEP = int(data['steps'])
        CONTEXT = f"My name is {NAME}, I live in {CITY}, {STATE}. I have taken {STEP} steps so far.\n"
        print(answer(f"Let {first_name} know that the initial setup is complete."))
    return 1

def check_weather():
    q = f"What is the current weather at {CITY},{STATE}?"
    weather = agent_executor.invoke({"input": q}, config={"configurable": {"session_id": "ck-session"}})['output']
    query = f"I have the weather data as such for my city: '{weather}.' Recommend me to walk outside if the weather is nice, and vice versa. I don't need any verbose information about the weather itself though."
    print(answer(query))
    return 1

def ask_walk():
    answer = input("Do you want to walk today? ")
    if answer.lower() == 'no':
        exit_chatty()

def chat():
    prompt = ""
    agent_executor.invoke({"input":CONTEXT + "Just remember these and don't do anything about it."}, config={"configurable": {"session_id": "ck-session"}})
    while prompt != "exit":
        prompt = input("Say to Chatty Kathy: ")
        if prompt != "exit":
            print(agent_executor.invoke({"input":prompt}, config={"configurable": {"session_id": "ck-session"}})['output'])
    return 0

def exit_chatty():
    quit()

def main():
    load_save()
    check_weather()
    ask_walk()
    chat()
    exit_chatty()
    return 0

# Main Loop
if __name__ == '__main__':
    main()