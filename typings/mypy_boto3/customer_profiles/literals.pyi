"""
Type annotations for customer-profiles service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/literals.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.literals import AttributeMatchingModelType

    data: AttributeMatchingModelType = "MANY_TO_MANY"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeMatchingModelType",
    "ConflictResolvingModelType",
    "DataPullModeType",
    "EventStreamDestinationStatusType",
    "EventStreamStateType",
    "FieldContentTypeType",
    "GenderType",
    "IdentityResolutionJobStatusType",
    "JobScheduleDayOfTheWeekType",
    "ListEventStreamsPaginatorName",
    "MarketoConnectorOperatorType",
    "MatchTypeType",
    "OperatorPropertiesKeysType",
    "OperatorType",
    "PartyTypeType",
    "RuleBasedMatchingStatusType",
    "S3ConnectorOperatorType",
    "SalesforceConnectorOperatorType",
    "ServiceNowConnectorOperatorType",
    "SourceConnectorTypeType",
    "StandardIdentifierType",
    "StatisticType",
    "StatusType",
    "TaskTypeType",
    "TriggerTypeType",
    "UnitType",
    "WorkflowTypeType",
    "ZendeskConnectorOperatorType",
    "logicalOperatorType",
)

AttributeMatchingModelType = Literal["MANY_TO_MANY", "ONE_TO_ONE"]
ConflictResolvingModelType = Literal["RECENCY", "SOURCE"]
DataPullModeType = Literal["Complete", "Incremental"]
EventStreamDestinationStatusType = Literal["HEALTHY", "UNHEALTHY"]
EventStreamStateType = Literal["RUNNING", "STOPPED"]
FieldContentTypeType = Literal["EMAIL_ADDRESS", "NAME", "NUMBER", "PHONE_NUMBER", "STRING"]
GenderType = Literal["FEMALE", "MALE", "UNSPECIFIED"]
IdentityResolutionJobStatusType = Literal[
    "COMPLETED", "FAILED", "FIND_MATCHING", "MERGING", "PARTIAL_SUCCESS", "PENDING", "PREPROCESSING"
]
JobScheduleDayOfTheWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
ListEventStreamsPaginatorName = Literal["list_event_streams"]
MarketoConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "GREATER_THAN",
    "LESS_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
MatchTypeType = Literal["ML_BASED_MATCHING", "RULE_BASED_MATCHING"]
OperatorPropertiesKeysType = Literal[
    "CONCAT_FORMAT",
    "DATA_TYPE",
    "DESTINATION_DATA_TYPE",
    "LOWER_BOUND",
    "MASK_LENGTH",
    "MASK_VALUE",
    "MATH_OPERATION_FIELDS_ORDER",
    "SOURCE_DATA_TYPE",
    "SUBFIELD_CATEGORY_MAP",
    "TRUNCATE_LENGTH",
    "UPPER_BOUND",
    "VALIDATION_ACTION",
    "VALUE",
    "VALUES",
]
OperatorType = Literal["EQUAL_TO", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL_TO"]
PartyTypeType = Literal["BUSINESS", "INDIVIDUAL", "OTHER"]
RuleBasedMatchingStatusType = Literal["ACTIVE", "IN_PROGRESS", "PENDING"]
S3ConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SalesforceConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
ServiceNowConnectorOperatorType = Literal[
    "ADDITION",
    "BETWEEN",
    "CONTAINS",
    "DIVISION",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NOT_EQUAL_TO",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
SourceConnectorTypeType = Literal["Marketo", "S3", "Salesforce", "Servicenow", "Zendesk"]
StandardIdentifierType = Literal[
    "ASSET", "CASE", "LOOKUP_ONLY", "NEW_ONLY", "ORDER", "PROFILE", "SECONDARY", "UNIQUE"
]
StatisticType = Literal[
    "AVERAGE",
    "COUNT",
    "FIRST_OCCURRENCE",
    "LAST_OCCURRENCE",
    "MAXIMUM",
    "MAX_OCCURRENCE",
    "MINIMUM",
    "SUM",
]
StatusType = Literal[
    "CANCELLED", "COMPLETE", "FAILED", "IN_PROGRESS", "NOT_STARTED", "RETRY", "SPLIT"
]
TaskTypeType = Literal["Arithmetic", "Filter", "Map", "Mask", "Merge", "Truncate", "Validate"]
TriggerTypeType = Literal["Event", "OnDemand", "Scheduled"]
UnitType = Literal["DAYS"]
WorkflowTypeType = Literal["APPFLOW_INTEGRATION"]
ZendeskConnectorOperatorType = Literal[
    "ADDITION",
    "DIVISION",
    "GREATER_THAN",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "MULTIPLICATION",
    "NO_OP",
    "PROJECTION",
    "SUBTRACTION",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NUMERIC",
]
logicalOperatorType = Literal["AND", "OR"]
