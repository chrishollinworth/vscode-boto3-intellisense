"""
Type annotations for customer-profiles service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/literals.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.literals import ConflictResolvingModelType

    data: ConflictResolvingModelType = "RECENCY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConflictResolvingModelType",
    "DataPullModeType",
    "FieldContentTypeType",
    "GenderType",
    "IdentityResolutionJobStatusType",
    "JobScheduleDayOfTheWeekType",
    "MarketoConnectorOperatorType",
    "OperatorPropertiesKeysType",
    "PartyTypeType",
    "S3ConnectorOperatorType",
    "SalesforceConnectorOperatorType",
    "ServiceNowConnectorOperatorType",
    "SourceConnectorTypeType",
    "StandardIdentifierType",
    "StatusType",
    "TaskTypeType",
    "TriggerTypeType",
    "WorkflowTypeType",
    "ZendeskConnectorOperatorType",
    "logicalOperatorType",
)

ConflictResolvingModelType = Literal["RECENCY", "SOURCE"]
DataPullModeType = Literal["Complete", "Incremental"]
FieldContentTypeType = Literal["EMAIL_ADDRESS", "NAME", "NUMBER", "PHONE_NUMBER", "STRING"]
GenderType = Literal["FEMALE", "MALE", "UNSPECIFIED"]
IdentityResolutionJobStatusType = Literal[
    "COMPLETED", "FAILED", "FIND_MATCHING", "MERGING", "PARTIAL_SUCCESS", "PENDING", "PREPROCESSING"
]
JobScheduleDayOfTheWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
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
PartyTypeType = Literal["BUSINESS", "INDIVIDUAL", "OTHER"]
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
StatusType = Literal[
    "CANCELLED", "COMPLETE", "FAILED", "IN_PROGRESS", "NOT_STARTED", "RETRY", "SPLIT"
]
TaskTypeType = Literal["Arithmetic", "Filter", "Map", "Mask", "Merge", "Truncate", "Validate"]
TriggerTypeType = Literal["Event", "OnDemand", "Scheduled"]
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
