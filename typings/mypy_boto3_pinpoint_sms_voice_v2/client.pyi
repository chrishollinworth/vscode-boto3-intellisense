"""
Type annotations for pinpoint-sms-voice-v2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Client

    client: PinpointSMSVoiceV2Client = boto3.client("pinpoint-sms-voice-v2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DestinationCountryParameterKeyType,
    EventTypeType,
    KeywordActionType,
    MessageTypeType,
    NumberCapabilityType,
    RequestableNumberTypeType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)
from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    ListPoolOriginationIdentitiesPaginator,
)
from .type_defs import (
    AssociateOriginationIdentityResultTypeDef,
    CloudWatchLogsDestinationTypeDef,
    ConfigurationSetFilterTypeDef,
    CreateConfigurationSetResultTypeDef,
    CreateEventDestinationResultTypeDef,
    CreateOptOutListResultTypeDef,
    CreatePoolResultTypeDef,
    DeleteConfigurationSetResultTypeDef,
    DeleteDefaultMessageTypeResultTypeDef,
    DeleteDefaultSenderIdResultTypeDef,
    DeleteEventDestinationResultTypeDef,
    DeleteKeywordResultTypeDef,
    DeleteOptedOutNumberResultTypeDef,
    DeleteOptOutListResultTypeDef,
    DeletePoolResultTypeDef,
    DeleteTextMessageSpendLimitOverrideResultTypeDef,
    DeleteVoiceMessageSpendLimitOverrideResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAccountLimitsResultTypeDef,
    DescribeConfigurationSetsResultTypeDef,
    DescribeKeywordsResultTypeDef,
    DescribeOptedOutNumbersResultTypeDef,
    DescribeOptOutListsResultTypeDef,
    DescribePhoneNumbersResultTypeDef,
    DescribePoolsResultTypeDef,
    DescribeSenderIdsResultTypeDef,
    DescribeSpendLimitsResultTypeDef,
    DisassociateOriginationIdentityResultTypeDef,
    KeywordFilterTypeDef,
    KinesisFirehoseDestinationTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    OptedOutFilterTypeDef,
    PhoneNumberFilterTypeDef,
    PoolFilterTypeDef,
    PoolOriginationIdentitiesFilterTypeDef,
    PutKeywordResultTypeDef,
    PutOptedOutNumberResultTypeDef,
    ReleasePhoneNumberResultTypeDef,
    RequestPhoneNumberResultTypeDef,
    SenderIdAndCountryTypeDef,
    SenderIdFilterTypeDef,
    SendTextMessageResultTypeDef,
    SendVoiceMessageResultTypeDef,
    SetDefaultMessageTypeResultTypeDef,
    SetDefaultSenderIdResultTypeDef,
    SetTextMessageSpendLimitOverrideResultTypeDef,
    SetVoiceMessageSpendLimitOverrideResultTypeDef,
    SnsDestinationTypeDef,
    TagTypeDef,
    UpdateEventDestinationResultTypeDef,
    UpdatePhoneNumberResultTypeDef,
    UpdatePoolResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PinpointSMSVoiceV2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PinpointSMSVoiceV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceV2Client exceptions.
        """
    def associate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = None
    ) -> AssociateOriginationIdentityResultTypeDef:
        """
        Associates the specified origination identity with a pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.associate_origination_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#associate_origination_identity)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#close)
        """
    def create_configuration_set(
        self, *, ConfigurationSetName: str, Tags: List["TagTypeDef"] = None, ClientToken: str = None
    ) -> CreateConfigurationSetResultTypeDef:
        """
        Creates a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_configuration_set)
        """
    def create_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        MatchingEventTypes: List[EventTypeType],
        CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef" = None,
        KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef" = None,
        SnsDestination: "SnsDestinationTypeDef" = None,
        ClientToken: str = None
    ) -> CreateEventDestinationResultTypeDef:
        """
        Creates a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_event_destination)
        """
    def create_opt_out_list(
        self, *, OptOutListName: str, Tags: List["TagTypeDef"] = None, ClientToken: str = None
    ) -> CreateOptOutListResultTypeDef:
        """
        Creates a new opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_opt_out_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_opt_out_list)
        """
    def create_pool(
        self,
        *,
        OriginationIdentity: str,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreatePoolResultTypeDef:
        """
        Creates a new pool and associates the specified origination identity to the
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_pool)
        """
    def delete_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> DeleteConfigurationSetResultTypeDef:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_configuration_set)
        """
    def delete_default_message_type(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultMessageTypeResultTypeDef:
        """
        Deletes an existing default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_message_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_default_message_type)
        """
    def delete_default_sender_id(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultSenderIdResultTypeDef:
        """
        Deletes an existing default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_default_sender_id)
        """
    def delete_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> DeleteEventDestinationResultTypeDef:
        """
        Deletes an existing event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_event_destination)
        """
    def delete_keyword(
        self, *, OriginationIdentity: str, Keyword: str
    ) -> DeleteKeywordResultTypeDef:
        """
        Deletes an existing keyword from an origination phone number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_keyword)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_keyword)
        """
    def delete_opt_out_list(self, *, OptOutListName: str) -> DeleteOptOutListResultTypeDef:
        """
        Deletes an existing opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opt_out_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_opt_out_list)
        """
    def delete_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> DeleteOptedOutNumberResultTypeDef:
        """
        Deletes an existing opted out destination phone number from the specified opt-
        out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opted_out_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_opted_out_number)
        """
    def delete_pool(self, *, PoolId: str) -> DeletePoolResultTypeDef:
        """
        Deletes an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_pool)
        """
    def delete_text_message_spend_limit_override(
        self,
    ) -> DeleteTextMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_text_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_text_message_spend_limit_override)
        """
    def delete_voice_message_spend_limit_override(
        self,
    ) -> DeleteVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account level monthly spend limit override for sending voice
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_voice_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_voice_message_spend_limit_override)
        """
    def describe_account_attributes(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_account_attributes)
        """
    def describe_account_limits(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAccountLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint SMS Voice V2 resource quotas for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_account_limits)
        """
    def describe_configuration_sets(
        self,
        *,
        ConfigurationSetNames: List[str] = None,
        Filters: List["ConfigurationSetFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeConfigurationSetsResultTypeDef:
        """
        Describes the specified configuration sets or all in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_configuration_sets)
        """
    def describe_keywords(
        self,
        *,
        OriginationIdentity: str,
        Keywords: List[str] = None,
        Filters: List["KeywordFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeKeywordsResultTypeDef:
        """
        Describes the specified keywords or all keywords on your origination phone
        number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_keywords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_keywords)
        """
    def describe_opt_out_lists(
        self, *, OptOutListNames: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeOptOutListsResultTypeDef:
        """
        Describes the specified opt-out list or all opt-out lists in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opt_out_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_opt_out_lists)
        """
    def describe_opted_out_numbers(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: List[str] = None,
        Filters: List["OptedOutFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeOptedOutNumbersResultTypeDef:
        """
        Describes the specified opted out destination numbers or all opted out
        destination numbers in an opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opted_out_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_opted_out_numbers)
        """
    def describe_phone_numbers(
        self,
        *,
        PhoneNumberIds: List[str] = None,
        Filters: List["PhoneNumberFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribePhoneNumbersResultTypeDef:
        """
        Describes the specified origination phone number, or all the phone numbers in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_phone_numbers)
        """
    def describe_pools(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["PoolFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribePoolsResultTypeDef:
        """
        Retrieves the specified pools or all pools associated with your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_pools)
        """
    def describe_sender_ids(
        self,
        *,
        SenderIds: List["SenderIdAndCountryTypeDef"] = None,
        Filters: List["SenderIdFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSenderIdsResultTypeDef:
        """
        Describes the specified SenderIds or all SenderIds associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_sender_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_sender_ids)
        """
    def describe_spend_limits(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeSpendLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint monthly spend limits for sending voice and
        text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_spend_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_spend_limits)
        """
    def disassociate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = None
    ) -> DisassociateOriginationIdentityResultTypeDef:
        """
        Removes the specified origination identity from an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.disassociate_origination_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#disassociate_origination_identity)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#generate_presigned_url)
        """
    def list_pool_origination_identities(
        self,
        *,
        PoolId: str,
        Filters: List["PoolOriginationIdentitiesFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPoolOriginationIdentitiesResultTypeDef:
        """
        Lists all associated origination identities in your pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_pool_origination_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#list_pool_origination_identities)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        List all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#list_tags_for_resource)
        """
    def put_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
        KeywordMessage: str,
        KeywordAction: KeywordActionType = None
    ) -> PutKeywordResultTypeDef:
        """
        Creates or updates a keyword configuration on an origination phone number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_keyword)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#put_keyword)
        """
    def put_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> PutOptedOutNumberResultTypeDef:
        """
        Creates an opted out destination phone number in the opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_opted_out_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#put_opted_out_number)
        """
    def release_phone_number(self, *, PhoneNumberId: str) -> ReleasePhoneNumberResultTypeDef:
        """
        Releases an existing origination phone number in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#release_phone_number)
        """
    def request_phone_number(
        self,
        *,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        NumberCapabilities: List[NumberCapabilityType],
        NumberType: RequestableNumberTypeType,
        OptOutListName: str = None,
        PoolId: str = None,
        RegistrationId: str = None,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> RequestPhoneNumberResultTypeDef:
        """
        Request an origination phone number for use in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#request_phone_number)
        """
    def send_text_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str = None,
        MessageBody: str = None,
        MessageType: MessageTypeType = None,
        Keyword: str = None,
        ConfigurationSetName: str = None,
        MaxPrice: str = None,
        TimeToLive: int = None,
        Context: Dict[str, str] = None,
        DestinationCountryParameters: Dict[DestinationCountryParameterKeyType, str] = None,
        DryRun: bool = None
    ) -> SendTextMessageResultTypeDef:
        """
        Creates a new text message and sends it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_text_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_text_message)
        """
    def send_voice_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str = None,
        MessageBodyTextType: VoiceMessageBodyTextTypeType = None,
        VoiceId: VoiceIdType = None,
        ConfigurationSetName: str = None,
        MaxPricePerMinute: str = None,
        TimeToLive: int = None,
        Context: Dict[str, str] = None,
        DryRun: bool = None
    ) -> SendVoiceMessageResultTypeDef:
        """
        Allows you to send a request that sends a text message through Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_voice_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_voice_message)
        """
    def set_default_message_type(
        self, *, ConfigurationSetName: str, MessageType: MessageTypeType
    ) -> SetDefaultMessageTypeResultTypeDef:
        """
        Sets the default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_message_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_default_message_type)
        """
    def set_default_sender_id(
        self, *, ConfigurationSetName: str, SenderId: str
    ) -> SetDefaultSenderIdResultTypeDef:
        """
        Sets default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_default_sender_id)
        """
    def set_text_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetTextMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_text_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_text_message_spend_limit_override)
        """
    def set_voice_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending voice messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_voice_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_voice_message_spend_limit_override)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or overwrites only the specified tags for the specified Amazon Pinpoint SMS
        Voice, version 2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the association of the specified tags from an Amazon Pinpoint SMS Voice
        V2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#untag_resource)
        """
    def update_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        Enabled: bool = None,
        MatchingEventTypes: List[EventTypeType] = None,
        CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef" = None,
        KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef" = None,
        SnsDestination: "SnsDestinationTypeDef" = None
    ) -> UpdateEventDestinationResultTypeDef:
        """
        Updates an existing event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_event_destination)
        """
    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TwoWayEnabled: bool = None,
        TwoWayChannelArn: str = None,
        SelfManagedOptOutsEnabled: bool = None,
        OptOutListName: str = None,
        DeletionProtectionEnabled: bool = None
    ) -> UpdatePhoneNumberResultTypeDef:
        """
        Updates the configuration of an existing origination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_phone_number)
        """
    def update_pool(
        self,
        *,
        PoolId: str,
        TwoWayEnabled: bool = None,
        TwoWayChannelArn: str = None,
        SelfManagedOptOutsEnabled: bool = None,
        OptOutListName: str = None,
        SharedRoutesEnabled: bool = None,
        DeletionProtectionEnabled: bool = None
    ) -> UpdatePoolResultTypeDef:
        """
        Updates the configuration of an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_pool)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_attributes"]
    ) -> DescribeAccountAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountattributespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountlimitspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_sets"]
    ) -> DescribeConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeConfigurationSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeconfigurationsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_keywords"]
    ) -> DescribeKeywordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeKeywords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describekeywordspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opt_out_lists"]
    ) -> DescribeOptOutListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptOutLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptoutlistspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opted_out_numbers"]
    ) -> DescribeOptedOutNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptedOutNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptedoutnumberspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_phone_numbers"]
    ) -> DescribePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePhoneNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describephonenumberspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_pools"]) -> DescribePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describepoolspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sender_ids"]
    ) -> DescribeSenderIdsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSenderIds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describesenderidspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spend_limits"]
    ) -> DescribeSpendLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSpendLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describespendlimitspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pool_origination_identities"]
    ) -> ListPoolOriginationIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.ListPoolOriginationIdentities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#listpooloriginationidentitiespaginator)
        """
