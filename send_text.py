from twilio.rest import TwilioRestClient

account_sid = "ACb289501c4227ba4d5d2c8bd9c659d50d" # Your Account SID from www.twilio.com/console
auth_token  = "20fefd865c5393fa2886ee0a5589fd61"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(]
    body="What's up superstar?",
    to="+7817209027",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
