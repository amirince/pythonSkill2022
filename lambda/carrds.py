from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, get_supported_interfaces
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

APL_DOCUMENT_ID = "Hello"

APL_DOCUMENT_TOKEN = "documentToken"

DATASOURCE = {
    "simpleTextTemplateData": {
        "type": "object",
        "properties": {
            "backgroundImage": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/background-green.png",
            "foregroundImageLocation": "left",
            "foregroundImageSource": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/asparagus.jpeg",
            "headerTitle": "Asparagus",
            "headerSubtitle": "",
            "hintText": "Try, \"Alexa, next question\"",
            "headerAttributionImage": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/logo-world-of-plants-2.png",
            "primaryText": "This is a second text",
            "textAlignment": "start",
            "titleText": "This is a title text"
        }
    }
}

class SampleAPLRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("INTENT_NAME")(handler_input)

    def supports_apl(self, handler_input):
        # Checks whether APL is supported by the User's device
        supported_interfaces = get_supported_interfaces(
            handler_input)
        return supported_interfaces.alexa_presentation_apl != None

    def launch_screen(self, handler_input):
        # Only add APL directive if User's device supports APL
        if self.supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token=APL_DOCUMENT_TOKEN,
                    document={
                        "type": "Link",
                        "src": f"doc://alexa/apl/documents/{APL_DOCUMENT_ID}"
                    },
                    datasources=DATASOURCE
                )
            )

    def handle(self, handler_input):
        # Add APL Template if device is compatible
        self.launch_screen(handler_input)
        # Generate JSON Response
        return handler_input.response_builder.response

sb = SkillBuilder()
sb.add_request_handler(SampleAPLRequestHandler())
lambda_handler = sb.lambda_handler()


const Alexa = require("ask-sdk-core");

const DOCUMENT_ID = "Checks";

const datasource = {
    "simpleTextTemplateData": {
        "type": "object",
        "properties": {
            "backgroundImage": "https://d2o906d8ln7ui1.cloudfront.net/images/response_builder/background-green.png",
            "foregroundImageLocation": "bottom",
            "foregroundImageSource": "https://www.nwcu.com/storage/app/uploads/public/59f/107/891/59f1078919f18026736731.jpg",
            "headerTitle": "Checks",
            "headerSubtitle": "",
            "hintText": "Try, \"Alexa, next question\"",
            "headerAttributionImage": "",
            "primaryText": "Do you write checks and pay bills?",
            "textAlignment": "center",
            "titleText": "Question One"
        }
    }
};

const createDirectivePayload = (aplDocumentId, dataSources = {}, tokenId = "documentToken") => {
    return {
        type: "Alexa.Presentation.APL.RenderDocument",
        token: tokenId,
        document: {
            type: "Link",
            src: "doc://alexa/apl/documents/" + aplDocumentId
        },
        datasources: dataSources
    }
};

const SampleAPLRequestHandler = {
    canHandle(handlerInput) {
        // handle named intent
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'INTENT_NAME';
    },
    handle(handlerInput) {
        if (Alexa.getSupportedInterfaces(handlerInput.requestEnvelope)['Alexa.Presentation.APL']) {
            // generate the APL RenderDocument directive that will be returned from your skill
            const aplDirective = createDirectivePayload(DOCUMENT_ID, datasource);
            // add the RenderDocument directive to the responseBuilder
            handlerInput.responseBuilder.addDirective(aplDirective);
        }

        // send out skill response
        return handlerInput.responseBuilder.getResponse();
    }
};

exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(SampleAPLRequestHandler)
    .lambda();
    
    
    