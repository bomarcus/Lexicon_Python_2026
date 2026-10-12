# Lab-9_A-3

# Create one object from each class and store them in the same list.

class EmailNotification:
    def send(self):
        return "Email"

class SMSNotification:
    def send(self):
        return "SMS"

class PushNotification:
    def send(self):
        return "Push"

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notifications = [
    email,
    sms,
    push
]
