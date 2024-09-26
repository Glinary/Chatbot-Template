# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# ---------- SECURE APIs AND IDs ---------- #
from actions.api.Database import Database
# ---------- SECURE API TOKEN ---------- #

    
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import logging

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        db = Database()
        dispatcher.utter_message(db.get_sample_response())

        # for event in tracker.events:
        #     if (event.get("event") == "user"):
        #         logging.info("SAW IT FROM ACTION")

        return []
        # # Extract latest user message
        # latest_user_event = None
        # latest_bot_event = None
        
        # for event in tracker.events:
        #     if (event.get("event") == "user"):
        #         latest_user_event = event
        #         format_user_event(event)
            # if event.get("event") == "bot":
            #     latest_bot_event = event
            #     format_bot_event(event, tracker)

#         # Log user event
#         if latest_user_event:
#             format_user_event(latest_user_event)

#         # Log bot event
#         # if latest_bot_event:
#         #     format_bot_event(latest_bot_event, tracker)

#         bot_event = {
#         "event": "bot",
#         "timestamp": tracker.latest_message.get("timestamp"),
#         "text": "test",
#         "data": None,
#         "message_id": None,
#         "parse_data": None,
#         }

#         logging.info(f"Bot Event: {bot_event}")

#         return []

# def format_user_event(latest_user_event):
#     user_event = {
#         "event": "user",
#         "timestamp": latest_user_event.get("timestamp") if latest_user_event else None,
#         "text": latest_user_event.get("text") if latest_user_event else None,
#         "message_id": latest_user_event.get("message_id") if latest_user_event else None,
#         "parse_data": latest_user_event.get("parse_data") if latest_user_event else None,
#         "data": None
#     }
    
#      # Log formatted events
#     logging.info(f"User Event: {user_event}")

#     return []

# def format_bot_event(latest_bot_event, tracker):
#     # Format the bot event
#     bot_event = {
#         "event": "bot",
#         "timestamp": tracker.latest_message.get("timestamp"),
#         "text": "test",
#         "data": None,
#         "message_id": None,
#         "parse_data": None,
#     }

#     # Log formatted events
#     logging.info(f"Bot Event: {bot_event}")

#     return []
       

