from datetime import datetime
import env

welcome_message_by_time = {
    12: f"good morning {env.USERNAME}",
    18: f"good noon {env.USERNAME}",
    22: f"good afternoon {env.USERNAME}",
    6: f"good night {env.USERNAME}" 
}

### greet the user based on the day time
def greet_user(speakMethod):
    hour = datetime.now().hour

    for time, message in welcome_message_by_time.items():
        if (hour < time):
            speakMethod(message)
            break
    speakMethod("How can I help you")

