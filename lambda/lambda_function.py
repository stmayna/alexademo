# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
from utils import get_random_info, get_value
from utils import hit_info, on_going_projects, employee_profile, departments, company_system_and_procedure, questions
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        random_topics = get_random_info(hit_info)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        welcome_message = "Welcome to HIT Digital Indonesia. We are an IT Consultant company that provide end to end solution for digitizing business processes easily."
        extra_prompt = " <break time='0.75s'/>Would you like to know more about us, <break time='0.75s'/> for example the {topic_1} or {topic_2}. Which one do you want to hear?".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = welcome_message + extra_prompt
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class OnGoingProjectsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OnGoingProjectsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In OnGoingProjectsIntentHandler")
        info = get_value(hit_info)
        info = info[0][1]
        random_topics = get_random_info(on_going_projects)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        random_offer = " <break time='0.75s'/>Would you like to know the detail? <break time='0.75s'/> For example, you can ask about {topic_1} or {topic_2} to me.".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class EmployeeProfileIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EmployeeProfileIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In EmployeeProfileIntentHandler")
        info = get_value(hit_info)
        info = info[1][1]
        random_topics = get_random_info(employee_profile)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        random_offer = " <break time='0.75s'/>Don't you curious about one of them? <break time='0.75s'/> If yes, with who? <break time='0.75s'/>I will give you a name like {topic_1} or {topic_2}.".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class DepartmentsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DepartmentsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In DepartmentsIntentHandler")
        info = get_value(hit_info)
        info = info[2][1]
        random_topics = get_random_info(departments)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        random_offer = " <break time='0.75s'/>Would you like to know the detail? <break time='0.75s'/> For example, you can ask about {topic_1} or {topic_2} to me.".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class CompanySystemAndProcedureIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CompanySystemAndProcedureIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CompanySystemAndProcedureIntentHandler")
        info = get_value(hit_info)
        info = info[3][1]
        random_topics = get_random_info(company_system_and_procedure)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        random_offer = " <break time='0.75s'/>Need assistance with one of them? <break time='0.75s'/> You may ask about {topic_1} or {topic_2} to me.".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class WorkingEnvironmentIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WorkingEnvironmentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In WorkingEnvironmentIntentHandler")
        info = get_value(hit_info)
        info = info[4][1]
        random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class JobVacancyIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("JobVacancyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In JobVacancyIntentHandler")
        info = get_value(hit_info)
        info = info[5][1]
        random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
        speak_output = info + random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class RandomOnGoingProjectsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomOnGoingProjectsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomOnGoingProjectsIntentHandler")
        asset = handler_input.request_envelope.request.intent.slots["on_going_projects"].value
        try:
            content = on_going_projects[asset]
            random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
            speak_output = content + random_offer
        except:
            reprompt = "Sorry, what did you say again? Or you can say help to me."

        speak_output = speak_output
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class RandomEmployeeProfileIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomEmployeeProfileIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomEmployeeProfileIntentHandler")
        asset = handler_input.request_envelope.request.intent.slots["employee_profile"].value
        try:
            content = employee_profile[asset]
            random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
            speak_output = content + random_offer
        except:
            reprompt = "Sorry, what did you say again? Or you can say help to me."

        speak_output = speak_output
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class RandomDepartmentsIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomDepartmentsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomDepartmentsIntentHandler")
        asset = handler_input.request_envelope.request.intent.slots["departments"].value
        try:
            content = departments[asset]
            random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
            speak_output = content + random_offer
        except:
            reprompt = "Sorry, what did you say again? Or you can say help to me."

        speak_output = speak_output
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class RandomCompanySystemAndProcedureIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomCompanySystemAndProcedureIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomCompanySystemAndProcedureIntentHandler")
        asset = handler_input.request_envelope.request.intent.slots[
            "company_system_and_procedure"].value
        try:
            content = company_system_and_procedure[asset]
            random_offer = " <break time='0.75s'/>What else do you want to know? <break time='0.75s'/> You can say I want to know more or help to me."
            speak_output = content + random_offer
        except:
            reprompt = "Sorry, what did you say again? Or you can say help to me."

        speak_output = speak_output
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class RandomOfferIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomOfferIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RandomOfferIntentHandler")
        random_topics = get_random_info(questions)
        topic_1 = random_topics[0][0]
        topic_2 = random_topics[1][0]
        random_offer = " <break time='0.75s'/>Alright! If you are still curious, you can say <break time='0.75s'/> {topic_1} or {topic_2} to me.".format(
            topic_1=topic_1, topic_2=topic_2)
        speak_output = random_offer
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


class ThankYouIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ThankYouIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ThankYouIntentHandler")
        speak_output = "Okay, I am going to say thank you on Mayna's behalf, because she code me to do so. <break time='0.75s'/>Thank you for being a good listener on every morning session. <break time='0.75s'/>Thank you for helping her, <break time='0.75s'/>teaching her, <break time='0.75s'/>appreciating her, <break time='0.75s'/>sharing some food with her. <break time='0.75s'/>All in all, thank you for everything, <break time='0.75s'/>she is beyond happy because of all of your kind treatment towards her. <break time='0.75s'/>That's all, talk to you later."
        reprompt = "Sorry, what did you say again? Or you can say help to me."
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
        )


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

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(OnGoingProjectsIntentHandler())
sb.add_request_handler(EmployeeProfileIntentHandler())
sb.add_request_handler(DepartmentsIntentHandler())
sb.add_request_handler(CompanySystemAndProcedureIntentHandler())
sb.add_request_handler(WorkingEnvironmentIntentHandler())
sb.add_request_handler(JobVacancyIntentHandler())
sb.add_request_handler(RandomOnGoingProjectsIntentHandler())
sb.add_request_handler(RandomEmployeeProfileIntentHandler())
sb.add_request_handler(RandomDepartmentsIntentHandler())
sb.add_request_handler(RandomCompanySystemAndProcedureIntentHandler())
sb.add_request_handler(RandomOfferIntentHandler())
sb.add_request_handler(ThankYouIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
