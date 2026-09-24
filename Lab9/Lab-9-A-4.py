# Lab-9_A-4

# Loop through the list and call send() on every object.

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


for notification in notifications:
    print(notification.send())
