# Example 2: adds user input and detects intents.

import watson_developer_cloud

# Set up Conversation service.
conversation = watson_developer_cloud.ConversationV1(
  username = 'b4020613-3c01-4ac1-a7b7-53beb6db9d60', # replace with username from service key
  password = 'ReK6XW6CdrlN', # replace with password from service key
  version = '2017-05-26'
)
workspace_id = '6779e2fd-ab9e-47a0-84f8-7a155f568790' # replace with workspace ID

# Initialize with empty value to start the conversation.
user_input = ''
context = {}

# Main input/output loop
while True:

  # Send message to Conversation service.
  response = conversation.message(
    workspace_id = workspace_id,
    input = {
      'text': user_input
    },
    context = context
  )
  
  # If an intent was detected, print it to the console.
  if response['intents']:
    print('Detected intent: #' + response['intents'][0]['intent'])

  # Print the output from dialog, if any.
  if response['output']['text']:
    print(response['output']['text'][0])

  context = response['context']

  # Prompt for next round of input.
  user_input = input('>> ')



