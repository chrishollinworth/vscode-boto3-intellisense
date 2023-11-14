"""
Type annotations for chime-sdk-voice service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_voice.literals import AlexaSkillStatusType

    data: AlexaSkillStatusType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlexaSkillStatusType",
    "CallLegTypeType",
    "CallingNameStatusType",
    "CapabilityType",
    "ErrorCodeType",
    "GeoMatchLevelType",
    "LanguageCodeType",
    "ListSipMediaApplicationsPaginatorName",
    "ListSipRulesPaginatorName",
    "NotificationTargetType",
    "NumberSelectionBehaviorType",
    "OrderedPhoneNumberStatusType",
    "OriginationRouteProtocolType",
    "PhoneNumberAssociationNameType",
    "PhoneNumberOrderStatusType",
    "PhoneNumberOrderTypeType",
    "PhoneNumberProductTypeType",
    "PhoneNumberStatusType",
    "PhoneNumberTypeType",
    "ProxySessionStatusType",
    "SipRuleTriggerTypeType",
    "VoiceConnectorAwsRegionType",
)

AlexaSkillStatusType = Literal["ACTIVE", "INACTIVE"]
CallLegTypeType = Literal["Callee", "Caller"]
CallingNameStatusType = Literal["Unassigned", "UpdateFailed", "UpdateInProgress", "UpdateSucceeded"]
CapabilityType = Literal["SMS", "Voice"]
ErrorCodeType = Literal[
    "AccessDenied",
    "BadRequest",
    "Conflict",
    "Forbidden",
    "Gone",
    "NotFound",
    "PhoneNumberAssociationsExist",
    "PreconditionFailed",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "ServiceUnavailable",
    "Throttled",
    "Throttling",
    "Unauthorized",
    "Unprocessable",
    "VoiceConnectorGroupAssociationsExist",
]
GeoMatchLevelType = Literal["AreaCode", "Country"]
LanguageCodeType = Literal["en-US"]
ListSipMediaApplicationsPaginatorName = Literal["list_sip_media_applications"]
ListSipRulesPaginatorName = Literal["list_sip_rules"]
NotificationTargetType = Literal["EventBridge", "SNS", "SQS"]
NumberSelectionBehaviorType = Literal["AvoidSticky", "PreferSticky"]
OrderedPhoneNumberStatusType = Literal["Acquired", "Failed", "Processing"]
OriginationRouteProtocolType = Literal["TCP", "UDP"]
PhoneNumberAssociationNameType = Literal["SipRuleId", "VoiceConnectorGroupId", "VoiceConnectorId"]
PhoneNumberOrderStatusType = Literal[
    "CancelRequested",
    "Cancelled",
    "ChangeRequested",
    "Exception",
    "FOC",
    "Failed",
    "Partial",
    "PendingDocuments",
    "Processing",
    "Submitted",
    "Successful",
]
PhoneNumberOrderTypeType = Literal["New", "Porting"]
PhoneNumberProductTypeType = Literal["SipMediaApplicationDialIn", "VoiceConnector"]
PhoneNumberStatusType = Literal[
    "AcquireFailed",
    "AcquireInProgress",
    "Assigned",
    "Cancelled",
    "DeleteFailed",
    "DeleteInProgress",
    "PortinCancelRequested",
    "PortinInProgress",
    "ReleaseFailed",
    "ReleaseInProgress",
    "Unassigned",
]
PhoneNumberTypeType = Literal["Local", "TollFree"]
ProxySessionStatusType = Literal["Closed", "InProgress", "Open"]
SipRuleTriggerTypeType = Literal["RequestUriHostname", "ToPhoneNumber"]
VoiceConnectorAwsRegionType = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-west-2",
]
