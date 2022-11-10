from datetime import datetime
import env

welcome_message_by_time = {
    12: f"guten Morgen {env.USERNAME}",
    18: f"gute Mittag {env.USERNAME}",
    22: f"guten Abend {env.USERNAME}",
    6: f"gute Nacht {env.USERNAME}" 
}

### great the user based on the day time
def greet_user(speakMethod):
    hour = datetime.now().hour

    for time, message in welcome_message_by_time:
        if (hour > time):
            speakMethod(message)
            break
    speakMethod("Wie kann ich dir helfen?")

