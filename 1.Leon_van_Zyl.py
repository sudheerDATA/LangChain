# Import necessary libraries
from langchain_openai import ChatOpenAI  # Import the ChatOpenAI class from the langchain_openai package to interact with OpenAI's models
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()  # Loads environment variables from a .env file into the script's environment

# Initialize the ChatOpenAI model with specific parameters
llm = ChatOpenAI(
    model_name='gpt-4',  # Specify the model to use, in this case GPT-4
    temperature=0.7,  # Control the randomness of the responses: 0.0 is deterministic, 1.0 is highly random
    max_tokens=50,  # Set the maximum number of tokens (words) in the response to 50
    #verbose=True  # Enable verbose mode for detailed output about the model's operations
)

# Print a separator for clarity in output
print('#----------response_invoke------------#')  # Print a header to separate the output of the single response section

# Get a single response from the model for the input query
response_invoke = llm.invoke('How are you')  # Invoke the model with the query "How are you" and get a response
print(response_invoke)  # Print the response from the model

# Print a separator for clarity in output
print('#----------response_batch------------#')  # Print a header to separate the output of the batch responses section

# Get responses for a batch of queries
response_batch = llm.batch(['How are you', 'Tell me a joke about AI'])  # Process multiple queries at once and get their responses
print(response_batch)  # Print the batch responses

# Print a separator for clarity in output
print('#------------response_stream----------#')  # Print a header to separate the output of the streaming responses section

# Stream responses for a single query
response_stream = llm.stream('Hello, How are you')  # Stream the response for the query "Hello, How are you"
# Iterate over the streamed chunks and print each one
for chunk in response_stream:  # Loop through each chunk of the streaming response
    print(chunk.content, end='', flush=True)  # Print the content of each chunk immediately without adding a newline, flush the buffer to ensure immediate output
