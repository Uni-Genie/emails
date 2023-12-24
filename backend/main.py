# from nylas import APIClient
# import os

# nylas = APIClient(
#     os.environ.get("CLIENT_ID"),
#     os.environ.get("CLIENT_SECRET"),
#     os.environ.get("ACCESS_TOKEN")
# )
# # Return all messages found in the user's inbox
# # nylas.messages.all()

# # Return messages that are filtered by specified arguments
# nylas.messages.where(to='swag@example.com')
# # Available filters: subject, to, from_, cc, bcc, in_, unread,
# # starred, filename, thread_id, received_before, received_after

# # Use offset, and limit to paginate the results
# nylas.messages.where(limit=10, offset=5)

# # Expanded view returns additional header information (see below)
# nylas.messages.where(view='expanded')

# # Return all messages that meet a specified search criteria
# nylas.messages.search('swag@example.com')

# # Return the most recent message
# message = nylas.messages.first()


# # The following attributes are available for the message object
# message.id
# message.object
# message.account_id
# message.thread_id
# message.subject
# message.from_
# message.to
# message.cc
# message.bcc
# message.date
# message.unread
# message.starred
# message.snippet
# message.body
# message.files
# message.events
# message.folder
# message.labels
# message.received_at

# # Get expanded view for a specific message
# # Replace {id} with the appropriate message id
# message = nylas.messages.where(view='expanded').get(id='{id}')

# # These are available in expanded view only.
# message.headers['Message-Id']
# message.headers['References']
# message.headers['In-Reply-To']



# Load your env variables
from dotenv import load_dotenv
load_dotenv()

# Import your dependencies
from nylas import APIClient
import os

# Initialize your Nylas API client
nylas1 = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN")
)

res = nylas1.messages.all()
res_json = [item.as_json(enforce_read_only=False) for item in res]
print(res_json)