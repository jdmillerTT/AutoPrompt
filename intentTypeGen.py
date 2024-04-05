import boto3

lex_client = boto3.client('lexv2-models', region_name='us-east-1')

def create_intent_with_service_requests_slot(bot_id, bot_version, locale_id, intent_name, slot_type_id):

    intent_body = {
        'botId': bot_id,
        'botVersion': bot_version,
        'localeId': locale_id,
        'intentName': intent_name,
        'description': "Intent for handling service requests",
        'sampleUtterances': [
            {"utterance": "I need to {serviceRequest}"},
            {"utterance": "{serviceRequest}"},
        ],
        'dialogCodeHook': {'enabled': False},
        'intentConfirmationSetting': {
            'promptSpecification': {
                'messageGroups': [{
                    'message': {
                'plainTextMessage': { 
                    'value': "Are you sure you want to proceed?"
                }}
                }],
                'maxRetries': 2,
                'allowInterrupt': True
            },
            'declinationResponse': {
                'messageGroups': [{
                    'message': {
                        'plainTextMessage': {
                    'value': "Okay, let's try something else."
                    }}
                }],
                'allowInterrupt': True
            },
            'active': True
        },
    }

    response = lex_client.create_intent(**intent_body)
    print(f"Created intent: {response['intentId']}")

create_intent_with_service_requests_slot(
    bot_id="HMKDMVK4QW",
    bot_version="DRAFT",
    locale_id="en_US",
    intent_name="HandleServiceRequestIntent",
    slot_type_id="794AMVP6Y9" 
)
