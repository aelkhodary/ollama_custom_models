# Import the chat function from the ollama library
# This library provides an interface to interact with Ollama language models
from ollama import chat

# Initialize a streaming chat session with the model
# - model: The name of the model to use ('thinking-model' supports internal reasoning)
# - messages: List of conversation messages (user query in this case)
# - think=True: Enables the model to show its internal reasoning/thinking process
# - stream=True: Returns responses incrementally as they're generated (not all at once)
stream = chat(
  model='thinking-model', #model='qwen3',
  messages=[{'role': 'user', 'content': 'How many letter r are in strawberry?'}],
  think=True,
  stream=True,
)

# Track whether we're currently in the "thinking" phase of the response
# This helps us format the output nicely by separating thinking from the final answer
in_thinking = False

# Process each chunk of the streamed response as it arrives
for chunk in stream:
  # Check if this chunk contains thinking content and we haven't started printing thinking yet
  # This triggers once at the beginning of the thinking phase
  if chunk.message.thinking and not in_thinking:
    in_thinking = True
    # Print a header to indicate the thinking section is starting
    print('Thinking:\n', end='')

  # If this chunk contains thinking content, print it character by character
  # The 'end=""' prevents newlines between chunks, creating a smooth stream
  if chunk.message.thinking:
    print(chunk.message.thinking, end='')
  # Once thinking is done, we start receiving the actual answer content
  elif chunk.message.content:
    # If we were just in thinking mode, print a separator before the answer
    if in_thinking:
      print('\n\nAnswer:\n', end='')
      in_thinking = False
    # Print the answer content as it streams in
    print(chunk.message.content, end='')