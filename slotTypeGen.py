import xml.etree.ElementTree as ET
import json
import boto3

lex_client = boto3.client('lexv2-models', aws_access_key_id='AKIAVRUVR25M7JOX53FL', aws_secret_access_key='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', region_name='us-east-1')

sitemap_xml_path = 'TestSiteMap.xml'

tree = ET.parse(sitemap_xml_path)
root = tree.getroot()

service_names = [url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}name').text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')]

slot_type_values = [{"sampleValue": {"value": name}} for name in service_names]

slot_type_json = {
    "slotTypeName": "ServiceRequests",
    "description": "Types of service requests available",
    "slotTypeValues": slot_type_values,
    "valueSelectionSetting": {
        "resolutionStrategy": "OriginalValue"
    },
    "botId": "HMKDMVK4QW",
    "botVersion": "DRAFT",
    "localeId": "en_US"
}

file_name = 'slot_type_json.json'

with open(file_name, 'w') as json_file:
    json.dump(slot_type_json, json_file, indent=4)

print(f"Slot type JSON has been saved to {file_name}")