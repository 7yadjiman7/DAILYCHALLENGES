class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    # Step 2
    def call(self, other_phone):
        record = f"{self.phone_number} called {other_phone.phone_number}"
        print(record)
        self.call_history.append(record)

    # Step 3
    def show_call_history(self):
        print("--- Call History ---")
        for record in self.call_history:
            print(record)

    # Step 5
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: '{content}'")

    # Step 6a: messages send by phone
    def show_outgoing_messages(self):
        print(f"--- Outgoing messages from {self.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"  To {msg['to']}: '{msg['content']}'")

    # Step 6b: messages receive by phone
    def show_incoming_messages(self):
        print(f"--- Incoming messages to {self.phone_number} ---")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"  From {msg['from']}: '{msg['content']}'")

    # Step 6c: messages receive from specifique number
    def show_messages_from(self, other_phone):
        print(f"--- Messages received from {other_phone.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(f"  '{msg['content']}'")


# Step 7: Tests
phone1 = Phone("07-00-00-00-01")
phone2 = Phone("07-00-00-00-02")
phone3 = Phone("07-00-00-00-03")

# Appels
phone1.call(phone2)
phone1.call(phone3)
phone2.call(phone1)

phone1.show_call_history()

# Messages
phone1.send_message(phone2, "Salut, ça va ?")
phone1.send_message(phone2, "On se retrouve à 18h ?")
phone2.send_message(phone1, "Oui, pas de problème !")
phone3.send_message(phone1, "Tu es disponible demain ?")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)

