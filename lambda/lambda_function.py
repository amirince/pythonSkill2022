# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import numpy as np
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

from ask_sdk_model import dialog
from ask_sdk_model.dialog import (ElicitSlotDirective, DelegateDirective)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


################################################################################
#                           Temp Code                                          #
################################################################################

currentScore=0
temp=''
def scoring(userResponse):
    global currentScore
    currentScore+=1

################################################################################
#                          LaunchRequestHandler                                #
################################################################################

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to the VOICE FAQ Survey"
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionOneIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionOne': 
                            {
                                'name': 'questionOne',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                
                # .add_directive(
                #     directive=dialog.DelegateDirective({
                #         'name': 'QuestionTenIntent',
                #         'confirmation_status': 'NONE',
                #         'slots': {
                #             'questionTen': 
                #             {
                #                 'name': 'questionTen',
                #                 'confirmation_status': 'NONE',
                #                 'resolutions': None,
                #                 'slot_value': None,
                #                 'value': None
                #             }
                #         }
                #     })
                # )
                
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )

################################################################################
#                          Question Intents                                    #
################################################################################

class QuestionOneIntentHandler(AbstractRequestHandler):
    """Handler for QuestionOne Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionOneIntent")(handler_input)

    def handle(self, handler_input):
        questionOne = handler_input.request_envelope.request.intent.slots  #Method works
        print("User Response:")
        #print(questionOne['questionOne'])
        temp=questionOne['questionOne']
        # print(temp['value'])
        
        scoring(questionOne['questionOne'])
        # print(questionOne['questionOne']['value']
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionTwoIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionTwo': 
                            {
                                'name': 'questionTwo',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionTwoIntentHandler(AbstractRequestHandler):
    """Handler for QuestionTwo Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionTwoIntent")(handler_input)

    def handle(self, handler_input):
        questionTwo = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionTwo)
        #print(questionTwo['questionTwo']['value'])
        scoring(questionTwo['questionTwo'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionThreeIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionThree': 
                            {
                                'name': 'questionThree',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionThreeIntentHandler(AbstractRequestHandler):
    """Handler for QuestionThree Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionThreeIntent")(handler_input)

    def handle(self, handler_input):
        questionThree = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionThree)
        #print(questionThree['questionThree']['value'])
        scoring(questionThree['questionThree'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionFourIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionFour': 
                            {
                                'name': 'questionFour',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionFourIntentHandler(AbstractRequestHandler):
    """Handler for QuestionFour Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionFourIntent")(handler_input)

    def handle(self, handler_input):
        questionFour = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionFour)
        scoring(questionFour['questionFour'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionFiveIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionFive': 
                            {
                                'name': 'questionFive',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionFiveIntentHandler(AbstractRequestHandler):
    """Handler for QuestionFive Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionFiveIntent")(handler_input)

    def handle(self, handler_input):
        questionFive = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionFive)
        scoring(questionFive['questionFive'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionSixIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionSix': 
                            {
                                'name': 'questionSix',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionSixIntentHandler(AbstractRequestHandler):
    """Handler for QuestionSix Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionSixIntent")(handler_input)

    def handle(self, handler_input):
        questionSix = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionSix)
        scoring(questionSix['questionSix'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionSevenIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionSeven': 
                            {
                                'name': 'questionSeven',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionSevenIntentHandler(AbstractRequestHandler):
    """Handler for QuestionSeven Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionSevenIntent")(handler_input)

    def handle(self, handler_input):
        questionSeven = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionSeven)
        scoring(questionSeven['questionSeven'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionEightIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionEight': 
                            {
                                'name': 'questionEight',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionEightIntentHandler(AbstractRequestHandler):
    """Handler for QuestionEight Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionEightIntent")(handler_input)

    def handle(self, handler_input):
        questionEight = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionEight)
        scoring(questionEight['questionEight'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionNineIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionNine': 
                            {
                                'name': 'questionNine',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionNineIntentHandler(AbstractRequestHandler):
    """Handler for QuestionNine Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionNineIntent")(handler_input)

    def handle(self, handler_input):
        questionNine= handler_input.request_envelope.request.intent.slots  #Method works
        print(questionNine)
        scoring(questionNine['questionNine'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'QuestionTenIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'questionTen': 
                            {
                                'name': 'questionTen',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class QuestionTenIntentHandler(AbstractRequestHandler):
    """Handler for QuestionTen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuestionTenIntent")(handler_input)

    def handle(self, handler_input):
        questionTen = handler_input.request_envelope.request.intent.slots  #Method works
        print(questionTen)
        scoring(questionTen['questionTen'])
        return (
            handler_input.response_builder
                .add_directive(
                    directive=dialog.DelegateDirective({
                        'name': 'scoringIntent',
                        'confirmation_status': 'NONE',
                        'slots': {
                            'scoring': 
                            {
                                'name': 'scoring',
                                'confirmation_status': 'NONE',
                                'resolutions': None,
                                'slot_value': None,
                                'value': None
                            }
                        }
                    })
                )
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class scoringIntentHandler(AbstractRequestHandler):
    """Handler for QuestionTen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("scoringIntent")(handler_input)

    def handle(self, handler_input):
        global currentScore
        speak_output="Your score is " + str(currentScore)
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

################################################################################
#                          Default Functions                                   #
################################################################################

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

################################################################################
#                          Skill Builder                                       #
################################################################################

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(QuestionOneIntentHandler())
sb.add_request_handler(QuestionTwoIntentHandler())
sb.add_request_handler(QuestionThreeIntentHandler())
sb.add_request_handler(QuestionFourIntentHandler())
sb.add_request_handler(QuestionFiveIntentHandler())
sb.add_request_handler(QuestionSixIntentHandler())
sb.add_request_handler(QuestionSevenIntentHandler())
sb.add_request_handler(QuestionEightIntentHandler())
sb.add_request_handler(QuestionNineIntentHandler())
sb.add_request_handler(QuestionTenIntentHandler())
sb.add_request_handler(scoringIntentHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()