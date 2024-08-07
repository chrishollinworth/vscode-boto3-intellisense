"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyRequestRequestTypeDef

    data: AddProfileKeyRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AttributeMatchingModelType,
    ConflictResolvingModelType,
    DataPullModeType,
    EventStreamDestinationStatusType,
    EventStreamStateType,
    FieldContentTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    JobScheduleDayOfTheWeekType,
    MarketoConnectorOperatorType,
    MatchTypeType,
    OperatorPropertiesKeysType,
    OperatorType,
    PartyTypeType,
    RuleBasedMatchingStatusType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatisticType,
    StatusType,
    TaskTypeType,
    TriggerTypeType,
    ZendeskConnectorOperatorType,
    logicalOperatorType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddProfileKeyRequestRequestTypeDef",
    "AddProfileKeyResponseTypeDef",
    "AdditionalSearchKeyTypeDef",
    "AddressTypeDef",
    "AppflowIntegrationTypeDef",
    "AppflowIntegrationWorkflowAttributesTypeDef",
    "AppflowIntegrationWorkflowMetricsTypeDef",
    "AppflowIntegrationWorkflowStepTypeDef",
    "AttributeDetailsTypeDef",
    "AttributeItemTypeDef",
    "AttributeTypesSelectorTypeDef",
    "AutoMergingTypeDef",
    "BatchTypeDef",
    "ConditionsTypeDef",
    "ConflictResolutionTypeDef",
    "ConnectorOperatorTypeDef",
    "ConsolidationTypeDef",
    "CreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEventStreamRequestRequestTypeDef",
    "CreateEventStreamResponseTypeDef",
    "CreateIntegrationWorkflowRequestRequestTypeDef",
    "CreateIntegrationWorkflowResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyRequestRequestTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectRequestRequestTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteProfileResponseTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DestinationSummaryTypeDef",
    "DetectProfileObjectTypeRequestRequestTypeDef",
    "DetectProfileObjectTypeResponseTypeDef",
    "DetectedProfileObjectTypeTypeDef",
    "DomainStatsTypeDef",
    "EventStreamDestinationDetailsTypeDef",
    "EventStreamSummaryTypeDef",
    "ExportingConfigTypeDef",
    "ExportingLocationTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FlowDefinitionTypeDef",
    "FoundByKeyValueTypeDef",
    "GetAutoMergingPreviewRequestRequestTypeDef",
    "GetAutoMergingPreviewResponseTypeDef",
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    "GetCalculatedAttributeForProfileResponseTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainResponseTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetIdentityResolutionJobRequestRequestTypeDef",
    "GetIdentityResolutionJobResponseTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetMatchesRequestRequestTypeDef",
    "GetMatchesResponseTypeDef",
    "GetProfileObjectTypeRequestRequestTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "GetSimilarProfilesRequestRequestTypeDef",
    "GetSimilarProfilesResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepsRequestRequestTypeDef",
    "GetWorkflowStepsResponseTypeDef",
    "IdentityResolutionJobTypeDef",
    "IncrementalPullConfigTypeDef",
    "IntegrationConfigTypeDef",
    "JobScheduleTypeDef",
    "JobStatsTypeDef",
    "ListAccountIntegrationsRequestRequestTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListCalculatedAttributeDefinitionItemTypeDef",
    "ListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    "ListCalculatedAttributeForProfileItemTypeDef",
    "ListCalculatedAttributesForProfileRequestRequestTypeDef",
    "ListCalculatedAttributesForProfileResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEventStreamsRequestRequestTypeDef",
    "ListEventStreamsResponseTypeDef",
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    "ListIdentityResolutionJobsResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsRequestRequestTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesRequestRequestTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsRequestRequestTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListRuleBasedMatchesRequestRequestTypeDef",
    "ListRuleBasedMatchesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkflowsItemTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MatchingRuleTypeDef",
    "MergeProfilesRequestRequestTypeDef",
    "MergeProfilesResponseTypeDef",
    "ObjectFilterTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectRequestRequestTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeRequestRequestTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "RangeTypeDef",
    "ResponseMetadataTypeDef",
    "RuleBasedMatchingRequestTypeDef",
    "RuleBasedMatchingResponseTypeDef",
    "S3ExportingConfigTypeDef",
    "S3ExportingLocationTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesRequestRequestTypeDef",
    "SearchProfilesResponseTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTypeDef",
    "ThresholdTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddressTypeDef",
    "UpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "WorkflowAttributesTypeDef",
    "WorkflowMetricsTypeDef",
    "WorkflowStepItemTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AddProfileKeyRequestRequestTypeDef = TypedDict(
    "AddProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": List[str],
        "DomainName": str,
    },
)

AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdditionalSearchKeyTypeDef = TypedDict(
    "AdditionalSearchKeyTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
    },
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

_RequiredAppflowIntegrationTypeDef = TypedDict(
    "_RequiredAppflowIntegrationTypeDef",
    {
        "FlowDefinition": "FlowDefinitionTypeDef",
    },
)
_OptionalAppflowIntegrationTypeDef = TypedDict(
    "_OptionalAppflowIntegrationTypeDef",
    {
        "Batches": List["BatchTypeDef"],
    },
    total=False,
)

class AppflowIntegrationTypeDef(
    _RequiredAppflowIntegrationTypeDef, _OptionalAppflowIntegrationTypeDef
):
    pass

_RequiredAppflowIntegrationWorkflowAttributesTypeDef = TypedDict(
    "_RequiredAppflowIntegrationWorkflowAttributesTypeDef",
    {
        "SourceConnectorType": SourceConnectorTypeType,
        "ConnectorProfileName": str,
    },
)
_OptionalAppflowIntegrationWorkflowAttributesTypeDef = TypedDict(
    "_OptionalAppflowIntegrationWorkflowAttributesTypeDef",
    {
        "RoleArn": str,
    },
    total=False,
)

class AppflowIntegrationWorkflowAttributesTypeDef(
    _RequiredAppflowIntegrationWorkflowAttributesTypeDef,
    _OptionalAppflowIntegrationWorkflowAttributesTypeDef,
):
    pass

AppflowIntegrationWorkflowMetricsTypeDef = TypedDict(
    "AppflowIntegrationWorkflowMetricsTypeDef",
    {
        "RecordsProcessed": int,
        "StepsCompleted": int,
        "TotalSteps": int,
    },
)

AppflowIntegrationWorkflowStepTypeDef = TypedDict(
    "AppflowIntegrationWorkflowStepTypeDef",
    {
        "FlowName": str,
        "Status": StatusType,
        "ExecutionMessage": str,
        "RecordsProcessed": int,
        "BatchRecordsStartTime": str,
        "BatchRecordsEndTime": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)

AttributeDetailsTypeDef = TypedDict(
    "AttributeDetailsTypeDef",
    {
        "Attributes": List["AttributeItemTypeDef"],
        "Expression": str,
    },
)

AttributeItemTypeDef = TypedDict(
    "AttributeItemTypeDef",
    {
        "Name": str,
    },
)

_RequiredAttributeTypesSelectorTypeDef = TypedDict(
    "_RequiredAttributeTypesSelectorTypeDef",
    {
        "AttributeMatchingModel": AttributeMatchingModelType,
    },
)
_OptionalAttributeTypesSelectorTypeDef = TypedDict(
    "_OptionalAttributeTypesSelectorTypeDef",
    {
        "Address": List[str],
        "PhoneNumber": List[str],
        "EmailAddress": List[str],
    },
    total=False,
)

class AttributeTypesSelectorTypeDef(
    _RequiredAttributeTypesSelectorTypeDef, _OptionalAttributeTypesSelectorTypeDef
):
    pass

_RequiredAutoMergingTypeDef = TypedDict(
    "_RequiredAutoMergingTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalAutoMergingTypeDef = TypedDict(
    "_OptionalAutoMergingTypeDef",
    {
        "Consolidation": "ConsolidationTypeDef",
        "ConflictResolution": "ConflictResolutionTypeDef",
        "MinAllowedConfidenceScoreForMerging": float,
    },
    total=False,
)

class AutoMergingTypeDef(_RequiredAutoMergingTypeDef, _OptionalAutoMergingTypeDef):
    pass

BatchTypeDef = TypedDict(
    "BatchTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "Range": "RangeTypeDef",
        "ObjectCount": int,
        "Threshold": "ThresholdTypeDef",
    },
    total=False,
)

_RequiredConflictResolutionTypeDef = TypedDict(
    "_RequiredConflictResolutionTypeDef",
    {
        "ConflictResolvingModel": ConflictResolvingModelType,
    },
)
_OptionalConflictResolutionTypeDef = TypedDict(
    "_OptionalConflictResolutionTypeDef",
    {
        "SourceName": str,
    },
    total=False,
)

class ConflictResolutionTypeDef(
    _RequiredConflictResolutionTypeDef, _OptionalConflictResolutionTypeDef
):
    pass

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Marketo": MarketoConnectorOperatorType,
        "S3": S3ConnectorOperatorType,
        "Salesforce": SalesforceConnectorOperatorType,
        "ServiceNow": ServiceNowConnectorOperatorType,
        "Zendesk": ZendeskConnectorOperatorType,
    },
    total=False,
)

ConsolidationTypeDef = TypedDict(
    "ConsolidationTypeDef",
    {
        "MatchingAttributesList": List[List[str]],
    },
)

_RequiredCreateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
        "AttributeDetails": "AttributeDetailsTypeDef",
        "Statistic": StatisticType,
    },
)
_OptionalCreateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "Conditions": "ConditionsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCalculatedAttributeDefinitionRequestRequestTypeDef(
    _RequiredCreateCalculatedAttributeDefinitionRequestRequestTypeDef,
    _OptionalCreateCalculatedAttributeDefinitionRequestRequestTypeDef,
):
    pass

CreateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "AttributeDetails": "AttributeDetailsTypeDef",
        "Conditions": "ConditionsTypeDef",
        "Statistic": StatisticType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingRequestTypeDef",
        "RuleBasedMatching": "RuleBasedMatchingRequestTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "RuleBasedMatching": "RuleBasedMatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventStreamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "EventStreamName": str,
    },
)
_OptionalCreateEventStreamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventStreamRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEventStreamRequestRequestTypeDef(
    _RequiredCreateEventStreamRequestRequestTypeDef, _OptionalCreateEventStreamRequestRequestTypeDef
):
    pass

CreateEventStreamResponseTypeDef = TypedDict(
    "CreateEventStreamResponseTypeDef",
    {
        "EventStreamArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "IntegrationConfig": "IntegrationConfigTypeDef",
        "ObjectTypeName": str,
        "RoleArn": str,
    },
)
_OptionalCreateIntegrationWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationWorkflowRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateIntegrationWorkflowRequestRequestTypeDef(
    _RequiredCreateIntegrationWorkflowRequestRequestTypeDef,
    _OptionalCreateIntegrationWorkflowRequestRequestTypeDef,
):
    pass

CreateIntegrationWorkflowResponseTypeDef = TypedDict(
    "CreateIntegrationWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": PartyTypeType,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": GenderType,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": "AddressTypeDef",
        "ShippingAddress": "AddressTypeDef",
        "MailingAddress": "AddressTypeDef",
        "BillingAddress": "AddressTypeDef",
        "Attributes": Dict[str, str],
        "PartyTypeString": str,
        "GenderString": str,
    },
    total=False,
)

class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)

DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

DeleteIntegrationResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileKeyRequestRequestTypeDef = TypedDict(
    "DeleteProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": List[str],
        "DomainName": str,
    },
)

DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ProfileObjectUniqueKey": str,
        "ObjectTypeName": str,
        "DomainName": str,
    },
)

DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "DomainName": str,
    },
)

DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)

_RequiredDestinationSummaryTypeDef = TypedDict(
    "_RequiredDestinationSummaryTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
    },
)
_OptionalDestinationSummaryTypeDef = TypedDict(
    "_OptionalDestinationSummaryTypeDef",
    {
        "UnhealthySince": datetime,
    },
    total=False,
)

class DestinationSummaryTypeDef(
    _RequiredDestinationSummaryTypeDef, _OptionalDestinationSummaryTypeDef
):
    pass

DetectProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DetectProfileObjectTypeRequestRequestTypeDef",
    {
        "Objects": List[str],
        "DomainName": str,
    },
)

DetectProfileObjectTypeResponseTypeDef = TypedDict(
    "DetectProfileObjectTypeResponseTypeDef",
    {
        "DetectedProfileObjectTypes": List["DetectedProfileObjectTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectedProfileObjectTypeTypeDef = TypedDict(
    "DetectedProfileObjectTypeTypeDef",
    {
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
    },
    total=False,
)

DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {
        "ProfileCount": int,
        "MeteringProfileCount": int,
        "ObjectCount": int,
        "TotalSize": int,
    },
    total=False,
)

_RequiredEventStreamDestinationDetailsTypeDef = TypedDict(
    "_RequiredEventStreamDestinationDetailsTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
    },
)
_OptionalEventStreamDestinationDetailsTypeDef = TypedDict(
    "_OptionalEventStreamDestinationDetailsTypeDef",
    {
        "UnhealthySince": datetime,
        "Message": str,
    },
    total=False,
)

class EventStreamDestinationDetailsTypeDef(
    _RequiredEventStreamDestinationDetailsTypeDef, _OptionalEventStreamDestinationDetailsTypeDef
):
    pass

_RequiredEventStreamSummaryTypeDef = TypedDict(
    "_RequiredEventStreamSummaryTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
        "EventStreamArn": str,
        "State": EventStreamStateType,
    },
)
_OptionalEventStreamSummaryTypeDef = TypedDict(
    "_OptionalEventStreamSummaryTypeDef",
    {
        "StoppedSince": datetime,
        "DestinationSummary": "DestinationSummaryTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class EventStreamSummaryTypeDef(
    _RequiredEventStreamSummaryTypeDef, _OptionalEventStreamSummaryTypeDef
):
    pass

ExportingConfigTypeDef = TypedDict(
    "ExportingConfigTypeDef",
    {
        "S3Exporting": "S3ExportingConfigTypeDef",
    },
    total=False,
)

ExportingLocationTypeDef = TypedDict(
    "ExportingLocationTypeDef",
    {
        "S3Exporting": "S3ExportingLocationTypeDef",
    },
    total=False,
)

FieldSourceProfileIdsTypeDef = TypedDict(
    "FieldSourceProfileIdsTypeDef",
    {
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": str,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": str,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": str,
        "ShippingAddress": str,
        "MailingAddress": str,
        "BillingAddress": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredFlowDefinitionTypeDef = TypedDict(
    "_RequiredFlowDefinitionTypeDef",
    {
        "FlowName": str,
        "KmsArn": str,
        "SourceFlowConfig": "SourceFlowConfigTypeDef",
        "Tasks": List["TaskTypeDef"],
        "TriggerConfig": "TriggerConfigTypeDef",
    },
)
_OptionalFlowDefinitionTypeDef = TypedDict(
    "_OptionalFlowDefinitionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class FlowDefinitionTypeDef(_RequiredFlowDefinitionTypeDef, _OptionalFlowDefinitionTypeDef):
    pass

FoundByKeyValueTypeDef = TypedDict(
    "FoundByKeyValueTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
    },
    total=False,
)

_RequiredGetAutoMergingPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredGetAutoMergingPreviewRequestRequestTypeDef",
    {
        "DomainName": str,
        "Consolidation": "ConsolidationTypeDef",
        "ConflictResolution": "ConflictResolutionTypeDef",
    },
)
_OptionalGetAutoMergingPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalGetAutoMergingPreviewRequestRequestTypeDef",
    {
        "MinAllowedConfidenceScoreForMerging": float,
    },
    total=False,
)

class GetAutoMergingPreviewRequestRequestTypeDef(
    _RequiredGetAutoMergingPreviewRequestRequestTypeDef,
    _OptionalGetAutoMergingPreviewRequestRequestTypeDef,
):
    pass

GetAutoMergingPreviewResponseTypeDef = TypedDict(
    "GetAutoMergingPreviewResponseTypeDef",
    {
        "DomainName": str,
        "NumberOfMatchesInSample": int,
        "NumberOfProfilesInSample": int,
        "NumberOfProfilesWillBeMerged": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)

GetCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": "ConditionsTypeDef",
        "AttributeDetails": "AttributeDetailsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCalculatedAttributeForProfileRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "CalculatedAttributeName": str,
    },
)

GetCalculatedAttributeForProfileResponseTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "IsDataPartial": str,
        "Value": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": "DomainStatsTypeDef",
        "Matching": "MatchingResponseTypeDef",
        "RuleBasedMatching": "RuleBasedMatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)

GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "DomainName": str,
        "EventStreamArn": str,
        "CreatedAt": datetime,
        "State": EventStreamStateType,
        "StoppedSince": datetime,
        "DestinationDetails": "EventStreamDestinationDetailsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityResolutionJobRequestRequestTypeDef = TypedDict(
    "GetIdentityResolutionJobRequestRequestTypeDef",
    {
        "DomainName": str,
        "JobId": str,
    },
)

GetIdentityResolutionJobResponseTypeDef = TypedDict(
    "GetIdentityResolutionJobResponseTypeDef",
    {
        "DomainName": str,
        "JobId": str,
        "Status": IdentityResolutionJobStatusType,
        "Message": str,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "LastUpdatedAt": datetime,
        "JobExpirationTime": datetime,
        "AutoMerging": "AutoMergingTypeDef",
        "ExportingLocation": "ExportingLocationTypeDef",
        "JobStats": "JobStatsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

GetIntegrationResponseTypeDef = TypedDict(
    "GetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMatchesRequestRequestTypeDef = TypedDict(
    "_RequiredGetMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetMatchesRequestRequestTypeDef = TypedDict(
    "_OptionalGetMatchesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetMatchesRequestRequestTypeDef(
    _RequiredGetMatchesRequestRequestTypeDef, _OptionalGetMatchesRequestRequestTypeDef
):
    pass

GetMatchesResponseTypeDef = TypedDict(
    "GetMatchesResponseTypeDef",
    {
        "NextToken": str,
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List["MatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

GetProfileObjectTypeResponseTypeDef = TypedDict(
    "GetProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "MaxAvailableProfileObjectCount": int,
        "MaxProfileObjectCount": int,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeTemplateRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    {
        "TemplateId": str,
    },
)

GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSimilarProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredGetSimilarProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MatchType": MatchTypeType,
        "SearchKey": str,
        "SearchValue": str,
    },
)
_OptionalGetSimilarProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalGetSimilarProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetSimilarProfilesRequestRequestTypeDef(
    _RequiredGetSimilarProfilesRequestRequestTypeDef,
    _OptionalGetSimilarProfilesRequestRequestTypeDef,
):
    pass

GetSimilarProfilesResponseTypeDef = TypedDict(
    "GetSimilarProfilesResponseTypeDef",
    {
        "ProfileIds": List[str],
        "MatchId": str,
        "MatchType": MatchTypeType,
        "RuleLevel": int,
        "ConfidenceScore": float,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Status": StatusType,
        "ErrorDescription": str,
        "StartDate": datetime,
        "LastUpdatedAt": datetime,
        "Attributes": "WorkflowAttributesTypeDef",
        "Metrics": "WorkflowMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowStepsRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowStepsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)
_OptionalGetWorkflowStepsRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowStepsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetWorkflowStepsRequestRequestTypeDef(
    _RequiredGetWorkflowStepsRequestRequestTypeDef, _OptionalGetWorkflowStepsRequestRequestTypeDef
):
    pass

GetWorkflowStepsResponseTypeDef = TypedDict(
    "GetWorkflowStepsResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Items": List["WorkflowStepItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityResolutionJobTypeDef = TypedDict(
    "IdentityResolutionJobTypeDef",
    {
        "DomainName": str,
        "JobId": str,
        "Status": IdentityResolutionJobStatusType,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "JobStats": "JobStatsTypeDef",
        "ExportingLocation": "ExportingLocationTypeDef",
        "Message": str,
    },
    total=False,
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": str,
    },
    total=False,
)

IntegrationConfigTypeDef = TypedDict(
    "IntegrationConfigTypeDef",
    {
        "AppflowIntegration": "AppflowIntegrationTypeDef",
    },
    total=False,
)

JobScheduleTypeDef = TypedDict(
    "JobScheduleTypeDef",
    {
        "DayOfTheWeek": JobScheduleDayOfTheWeekType,
        "Time": str,
    },
)

JobStatsTypeDef = TypedDict(
    "JobStatsTypeDef",
    {
        "NumberOfProfilesReviewed": int,
        "NumberOfMatchesFound": int,
        "NumberOfMergesDone": int,
    },
    total=False,
)

_RequiredListAccountIntegrationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountIntegrationsRequestRequestTypeDef",
    {
        "Uri": str,
    },
)
_OptionalListAccountIntegrationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncludeHidden": bool,
    },
    total=False,
)

class ListAccountIntegrationsRequestRequestTypeDef(
    _RequiredListAccountIntegrationsRequestRequestTypeDef,
    _OptionalListAccountIntegrationsRequestRequestTypeDef,
):
    pass

ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCalculatedAttributeDefinitionItemTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionItemTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredListCalculatedAttributeDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListCalculatedAttributeDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCalculatedAttributeDefinitionsRequestRequestTypeDef(
    _RequiredListCalculatedAttributeDefinitionsRequestRequestTypeDef,
    _OptionalListCalculatedAttributeDefinitionsRequestRequestTypeDef,
):
    pass

ListCalculatedAttributeDefinitionsResponseTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    {
        "Items": List["ListCalculatedAttributeDefinitionItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCalculatedAttributeForProfileItemTypeDef = TypedDict(
    "ListCalculatedAttributeForProfileItemTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "IsDataPartial": str,
        "Value": str,
    },
    total=False,
)

_RequiredListCalculatedAttributesForProfileRequestRequestTypeDef = TypedDict(
    "_RequiredListCalculatedAttributesForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
    },
)
_OptionalListCalculatedAttributesForProfileRequestRequestTypeDef = TypedDict(
    "_OptionalListCalculatedAttributesForProfileRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListCalculatedAttributesForProfileRequestRequestTypeDef(
    _RequiredListCalculatedAttributesForProfileRequestRequestTypeDef,
    _OptionalListCalculatedAttributesForProfileRequestRequestTypeDef,
):
    pass

ListCalculatedAttributesForProfileResponseTypeDef = TypedDict(
    "ListCalculatedAttributesForProfileResponseTypeDef",
    {
        "Items": List["ListCalculatedAttributeForProfileItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainItemTypeDef = TypedDict(
    "_RequiredListDomainItemTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalListDomainItemTypeDef = TypedDict(
    "_OptionalListDomainItemTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class ListDomainItemTypeDef(_RequiredListDomainItemTypeDef, _OptionalListDomainItemTypeDef):
    pass

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Items": List["ListDomainItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventStreamsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventStreamsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListEventStreamsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventStreamsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEventStreamsRequestRequestTypeDef(
    _RequiredListEventStreamsRequestRequestTypeDef, _OptionalListEventStreamsRequestRequestTypeDef
):
    pass

ListEventStreamsResponseTypeDef = TypedDict(
    "ListEventStreamsResponseTypeDef",
    {
        "Items": List["EventStreamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityResolutionJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityResolutionJobsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListIdentityResolutionJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityResolutionJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIdentityResolutionJobsRequestRequestTypeDef(
    _RequiredListIdentityResolutionJobsRequestRequestTypeDef,
    _OptionalListIdentityResolutionJobsRequestRequestTypeDef,
):
    pass

ListIdentityResolutionJobsResponseTypeDef = TypedDict(
    "ListIdentityResolutionJobsResponseTypeDef",
    {
        "IdentityResolutionJobsList": List["IdentityResolutionJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntegrationItemTypeDef = TypedDict(
    "_RequiredListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalListIntegrationItemTypeDef = TypedDict(
    "_OptionalListIntegrationItemTypeDef",
    {
        "ObjectTypeName": str,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
    },
    total=False,
)

class ListIntegrationItemTypeDef(
    _RequiredListIntegrationItemTypeDef, _OptionalListIntegrationItemTypeDef
):
    pass

_RequiredListIntegrationsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntegrationsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListIntegrationsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncludeHidden": bool,
    },
    total=False,
)

class ListIntegrationsRequestRequestTypeDef(
    _RequiredListIntegrationsRequestRequestTypeDef, _OptionalListIntegrationsRequestRequestTypeDef
):
    pass

ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileObjectTypeItemTypeDef = TypedDict(
    "_RequiredListProfileObjectTypeItemTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalListProfileObjectTypeItemTypeDef = TypedDict(
    "_OptionalListProfileObjectTypeItemTypeDef",
    {
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "MaxProfileObjectCount": int,
        "MaxAvailableProfileObjectCount": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

class ListProfileObjectTypeItemTypeDef(
    _RequiredListProfileObjectTypeItemTypeDef, _OptionalListProfileObjectTypeItemTypeDef
):
    pass

ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
    },
    total=False,
)

ListProfileObjectTypeTemplatesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeTemplateItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileObjectTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListProfileObjectTypesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListProfileObjectTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListProfileObjectTypesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProfileObjectTypesRequestRequestTypeDef(
    _RequiredListProfileObjectTypesRequestRequestTypeDef,
    _OptionalListProfileObjectTypesRequestRequestTypeDef,
):
    pass

ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {
        "ObjectTypeName": str,
        "ProfileObjectUniqueKey": str,
        "Object": str,
    },
    total=False,
)

_RequiredListProfileObjectsRequestRequestTypeDef = TypedDict(
    "_RequiredListProfileObjectsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "ProfileId": str,
    },
)
_OptionalListProfileObjectsRequestRequestTypeDef = TypedDict(
    "_OptionalListProfileObjectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ObjectFilter": "ObjectFilterTypeDef",
    },
    total=False,
)

class ListProfileObjectsRequestRequestTypeDef(
    _RequiredListProfileObjectsRequestRequestTypeDef,
    _OptionalListProfileObjectsRequestRequestTypeDef,
):
    pass

ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {
        "Items": List["ListProfileObjectsItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRuleBasedMatchesRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleBasedMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListRuleBasedMatchesRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleBasedMatchesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRuleBasedMatchesRequestRequestTypeDef(
    _RequiredListRuleBasedMatchesRequestRequestTypeDef,
    _OptionalListRuleBasedMatchesRequestRequestTypeDef,
):
    pass

ListRuleBasedMatchesResponseTypeDef = TypedDict(
    "ListRuleBasedMatchesResponseTypeDef",
    {
        "MatchIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsItemTypeDef = TypedDict(
    "ListWorkflowsItemTypeDef",
    {
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "WorkflowId": str,
        "Status": StatusType,
        "StatusDescription": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)

_RequiredListWorkflowsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListWorkflowsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowsRequestRequestTypeDef",
    {
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Status": StatusType,
        "QueryStartDate": Union[datetime, str],
        "QueryEndDate": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListWorkflowsRequestRequestTypeDef(
    _RequiredListWorkflowsRequestRequestTypeDef, _OptionalListWorkflowsRequestRequestTypeDef
):
    pass

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Items": List["ListWorkflowsItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

MatchItemTypeDef = TypedDict(
    "MatchItemTypeDef",
    {
        "MatchId": str,
        "ProfileIds": List[str],
        "ConfidenceScore": float,
    },
    total=False,
)

_RequiredMatchingRequestTypeDef = TypedDict(
    "_RequiredMatchingRequestTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalMatchingRequestTypeDef = TypedDict(
    "_OptionalMatchingRequestTypeDef",
    {
        "JobSchedule": "JobScheduleTypeDef",
        "AutoMerging": "AutoMergingTypeDef",
        "ExportingConfig": "ExportingConfigTypeDef",
    },
    total=False,
)

class MatchingRequestTypeDef(_RequiredMatchingRequestTypeDef, _OptionalMatchingRequestTypeDef):
    pass

MatchingResponseTypeDef = TypedDict(
    "MatchingResponseTypeDef",
    {
        "Enabled": bool,
        "JobSchedule": "JobScheduleTypeDef",
        "AutoMerging": "AutoMergingTypeDef",
        "ExportingConfig": "ExportingConfigTypeDef",
    },
    total=False,
)

MatchingRuleTypeDef = TypedDict(
    "MatchingRuleTypeDef",
    {
        "Rule": List[str],
    },
)

_RequiredMergeProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredMergeProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MainProfileId": str,
        "ProfileIdsToBeMerged": List[str],
    },
)
_OptionalMergeProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalMergeProfilesRequestRequestTypeDef",
    {
        "FieldSourceProfileIds": "FieldSourceProfileIdsTypeDef",
    },
    total=False,
)

class MergeProfilesRequestRequestTypeDef(
    _RequiredMergeProfilesRequestRequestTypeDef, _OptionalMergeProfilesRequestRequestTypeDef
):
    pass

MergeProfilesResponseTypeDef = TypedDict(
    "MergeProfilesResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectFilterTypeDef = TypedDict(
    "ObjectFilterTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
    },
)

ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": str,
        "Target": str,
        "ContentType": FieldContentTypeType,
    },
    total=False,
)

ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": List[StandardIdentifierType],
        "FieldNames": List[str],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": str,
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": PartyTypeType,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": GenderType,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": "AddressTypeDef",
        "ShippingAddress": "AddressTypeDef",
        "MailingAddress": "AddressTypeDef",
        "BillingAddress": "AddressTypeDef",
        "Attributes": Dict[str, str],
        "FoundByItems": List["FoundByKeyValueTypeDef"],
        "PartyTypeString": str,
        "GenderString": str,
    },
    total=False,
)

_RequiredPutIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalPutIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationRequestRequestTypeDef",
    {
        "Uri": str,
        "ObjectTypeName": str,
        "Tags": Dict[str, str],
        "FlowDefinition": "FlowDefinitionTypeDef",
        "ObjectTypeNames": Dict[str, str],
    },
    total=False,
)

class PutIntegrationRequestRequestTypeDef(
    _RequiredPutIntegrationRequestRequestTypeDef, _OptionalPutIntegrationRequestRequestTypeDef
):
    pass

PutIntegrationResponseTypeDef = TypedDict(
    "PutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProfileObjectRequestRequestTypeDef = TypedDict(
    "PutProfileObjectRequestRequestTypeDef",
    {
        "ObjectTypeName": str,
        "Object": str,
        "DomainName": str,
    },
)

PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalPutProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutProfileObjectTypeRequestRequestTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "MaxProfileObjectCount": int,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "Tags": Dict[str, str],
    },
    total=False,
)

class PutProfileObjectTypeRequestRequestTypeDef(
    _RequiredPutProfileObjectTypeRequestRequestTypeDef,
    _OptionalPutProfileObjectTypeRequestRequestTypeDef,
):
    pass

PutProfileObjectTypeResponseTypeDef = TypedDict(
    "PutProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "MaxProfileObjectCount": int,
        "MaxAvailableProfileObjectCount": int,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRuleBasedMatchingRequestTypeDef = TypedDict(
    "_RequiredRuleBasedMatchingRequestTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalRuleBasedMatchingRequestTypeDef = TypedDict(
    "_OptionalRuleBasedMatchingRequestTypeDef",
    {
        "MatchingRules": List["MatchingRuleTypeDef"],
        "MaxAllowedRuleLevelForMerging": int,
        "MaxAllowedRuleLevelForMatching": int,
        "AttributeTypesSelector": "AttributeTypesSelectorTypeDef",
        "ConflictResolution": "ConflictResolutionTypeDef",
        "ExportingConfig": "ExportingConfigTypeDef",
    },
    total=False,
)

class RuleBasedMatchingRequestTypeDef(
    _RequiredRuleBasedMatchingRequestTypeDef, _OptionalRuleBasedMatchingRequestTypeDef
):
    pass

RuleBasedMatchingResponseTypeDef = TypedDict(
    "RuleBasedMatchingResponseTypeDef",
    {
        "Enabled": bool,
        "MatchingRules": List["MatchingRuleTypeDef"],
        "Status": RuleBasedMatchingStatusType,
        "MaxAllowedRuleLevelForMerging": int,
        "MaxAllowedRuleLevelForMatching": int,
        "AttributeTypesSelector": "AttributeTypesSelectorTypeDef",
        "ConflictResolution": "ConflictResolutionTypeDef",
        "ExportingConfig": "ExportingConfigTypeDef",
    },
    total=False,
)

_RequiredS3ExportingConfigTypeDef = TypedDict(
    "_RequiredS3ExportingConfigTypeDef",
    {
        "S3BucketName": str,
    },
)
_OptionalS3ExportingConfigTypeDef = TypedDict(
    "_OptionalS3ExportingConfigTypeDef",
    {
        "S3KeyName": str,
    },
    total=False,
)

class S3ExportingConfigTypeDef(
    _RequiredS3ExportingConfigTypeDef, _OptionalS3ExportingConfigTypeDef
):
    pass

S3ExportingLocationTypeDef = TypedDict(
    "S3ExportingLocationTypeDef",
    {
        "S3BucketName": str,
        "S3KeyName": str,
    },
    total=False,
)

_RequiredS3SourcePropertiesTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3SourcePropertiesTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesTypeDef",
    {
        "BucketPrefix": str,
    },
    total=False,
)

class S3SourcePropertiesTypeDef(
    _RequiredS3SourcePropertiesTypeDef, _OptionalS3SourcePropertiesTypeDef
):
    pass

_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {
        "EnableDynamicFieldUpdate": bool,
        "IncludeDeletedRecords": bool,
    },
    total=False,
)

class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass

_RequiredScheduledTriggerPropertiesTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalScheduledTriggerPropertiesTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesTypeDef",
    {
        "DataPullMode": DataPullModeType,
        "ScheduleStartTime": Union[datetime, str],
        "ScheduleEndTime": Union[datetime, str],
        "Timezone": str,
        "ScheduleOffset": int,
        "FirstExecutionFrom": Union[datetime, str],
    },
    total=False,
)

class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass

_RequiredSearchProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "KeyName": str,
        "Values": List[str],
    },
)
_OptionalSearchProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AdditionalSearchKeys": List["AdditionalSearchKeyTypeDef"],
        "LogicalOperator": logicalOperatorType,
    },
    total=False,
)

class SearchProfilesRequestRequestTypeDef(
    _RequiredSearchProfilesRequestRequestTypeDef, _OptionalSearchProfilesRequestRequestTypeDef
):
    pass

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Items": List["ProfileTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Marketo": "MarketoSourcePropertiesTypeDef",
        "S3": "S3SourcePropertiesTypeDef",
        "Salesforce": "SalesforceSourcePropertiesTypeDef",
        "ServiceNow": "ServiceNowSourcePropertiesTypeDef",
        "Zendesk": "ZendeskSourcePropertiesTypeDef",
    },
    total=False,
)

_RequiredSourceFlowConfigTypeDef = TypedDict(
    "_RequiredSourceFlowConfigTypeDef",
    {
        "ConnectorType": SourceConnectorTypeType,
        "SourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
    },
)
_OptionalSourceFlowConfigTypeDef = TypedDict(
    "_OptionalSourceFlowConfigTypeDef",
    {
        "ConnectorProfileName": str,
        "IncrementalPullConfig": "IncrementalPullConfigTypeDef",
    },
    total=False,
)

class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, _OptionalSourceFlowConfigTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "SourceFields": List[str],
        "TaskType": TaskTypeType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "ConnectorOperator": "ConnectorOperatorTypeDef",
        "DestinationField": str,
        "TaskProperties": Dict[OperatorPropertiesKeysType, str],
    },
    total=False,
)

class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": str,
        "Operator": OperatorType,
    },
)

_RequiredTriggerConfigTypeDef = TypedDict(
    "_RequiredTriggerConfigTypeDef",
    {
        "TriggerType": TriggerTypeType,
    },
)
_OptionalTriggerConfigTypeDef = TypedDict(
    "_OptionalTriggerConfigTypeDef",
    {
        "TriggerProperties": "TriggerPropertiesTypeDef",
    },
    total=False,
)

class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, _OptionalTriggerConfigTypeDef):
    pass

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": "ScheduledTriggerPropertiesTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

_RequiredUpdateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)
_OptionalUpdateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "Conditions": "ConditionsTypeDef",
    },
    total=False,
)

class UpdateCalculatedAttributeDefinitionRequestRequestTypeDef(
    _RequiredUpdateCalculatedAttributeDefinitionRequestRequestTypeDef,
    _OptionalUpdateCalculatedAttributeDefinitionRequestRequestTypeDef,
):
    pass

UpdateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": "ConditionsTypeDef",
        "AttributeDetails": "AttributeDetailsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestRequestTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingRequestTypeDef",
        "RuleBasedMatching": "RuleBasedMatchingRequestTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class UpdateDomainRequestRequestTypeDef(
    _RequiredUpdateDomainRequestRequestTypeDef, _OptionalUpdateDomainRequestRequestTypeDef
):
    pass

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "RuleBasedMatching": "RuleBasedMatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
    },
)
_OptionalUpdateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestRequestTypeDef",
    {
        "AdditionalInformation": str,
        "AccountNumber": str,
        "PartyType": PartyTypeType,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": GenderType,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": "UpdateAddressTypeDef",
        "ShippingAddress": "UpdateAddressTypeDef",
        "MailingAddress": "UpdateAddressTypeDef",
        "BillingAddress": "UpdateAddressTypeDef",
        "Attributes": Dict[str, str],
        "PartyTypeString": str,
        "GenderString": str,
    },
    total=False,
)

class UpdateProfileRequestRequestTypeDef(
    _RequiredUpdateProfileRequestRequestTypeDef, _OptionalUpdateProfileRequestRequestTypeDef
):
    pass

UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkflowAttributesTypeDef = TypedDict(
    "WorkflowAttributesTypeDef",
    {
        "AppflowIntegration": "AppflowIntegrationWorkflowAttributesTypeDef",
    },
    total=False,
)

WorkflowMetricsTypeDef = TypedDict(
    "WorkflowMetricsTypeDef",
    {
        "AppflowIntegration": "AppflowIntegrationWorkflowMetricsTypeDef",
    },
    total=False,
)

WorkflowStepItemTypeDef = TypedDict(
    "WorkflowStepItemTypeDef",
    {
        "AppflowIntegration": "AppflowIntegrationWorkflowStepTypeDef",
    },
    total=False,
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
