"""
Type annotations for pinpoint-sms-voice-v2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Client
    from mypy_boto3_pinpoint_sms_voice_v2.paginator import (
        DescribeAccountAttributesPaginator,
        DescribeAccountLimitsPaginator,
        DescribeConfigurationSetsPaginator,
        DescribeKeywordsPaginator,
        DescribeOptOutListsPaginator,
        DescribeOptedOutNumbersPaginator,
        DescribePhoneNumbersPaginator,
        DescribePoolsPaginator,
        DescribeSenderIdsPaginator,
        DescribeSpendLimitsPaginator,
        ListPoolOriginationIdentitiesPaginator,
    )

    client: PinpointSMSVoiceV2Client = boto3.client("pinpoint-sms-voice-v2")

    describe_account_attributes_paginator: DescribeAccountAttributesPaginator = client.get_paginator("describe_account_attributes")
    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_configuration_sets_paginator: DescribeConfigurationSetsPaginator = client.get_paginator("describe_configuration_sets")
    describe_keywords_paginator: DescribeKeywordsPaginator = client.get_paginator("describe_keywords")
    describe_opt_out_lists_paginator: DescribeOptOutListsPaginator = client.get_paginator("describe_opt_out_lists")
    describe_opted_out_numbers_paginator: DescribeOptedOutNumbersPaginator = client.get_paginator("describe_opted_out_numbers")
    describe_phone_numbers_paginator: DescribePhoneNumbersPaginator = client.get_paginator("describe_phone_numbers")
    describe_pools_paginator: DescribePoolsPaginator = client.get_paginator("describe_pools")
    describe_sender_ids_paginator: DescribeSenderIdsPaginator = client.get_paginator("describe_sender_ids")
    describe_spend_limits_paginator: DescribeSpendLimitsPaginator = client.get_paginator("describe_spend_limits")
    list_pool_origination_identities_paginator: ListPoolOriginationIdentitiesPaginator = client.get_paginator("list_pool_origination_identities")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ConfigurationSetFilterTypeDef,
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
    KeywordFilterTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    OptedOutFilterTypeDef,
    PaginatorConfigTypeDef,
    PhoneNumberFilterTypeDef,
    PoolFilterTypeDef,
    PoolOriginationIdentitiesFilterTypeDef,
    SenderIdAndCountryTypeDef,
    SenderIdFilterTypeDef,
)

__all__ = (
    "DescribeAccountAttributesPaginator",
    "DescribeAccountLimitsPaginator",
    "DescribeConfigurationSetsPaginator",
    "DescribeKeywordsPaginator",
    "DescribeOptOutListsPaginator",
    "DescribeOptedOutNumbersPaginator",
    "DescribePhoneNumbersPaginator",
    "DescribePoolsPaginator",
    "DescribeSenderIdsPaginator",
    "DescribeSpendLimitsPaginator",
    "ListPoolOriginationIdentitiesPaginator",
)

class DescribeAccountAttributesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountAttributes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountattributespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountAttributesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountAttributes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountattributespaginator)
        """

class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountlimitspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountlimitspaginator)
        """

class DescribeConfigurationSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeConfigurationSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeconfigurationsetspaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationSetNames: List[str] = None,
        Filters: List["ConfigurationSetFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigurationSetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeConfigurationSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeconfigurationsetspaginator)
        """

class DescribeKeywordsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeKeywords)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describekeywordspaginator)
    """

    def paginate(
        self,
        *,
        OriginationIdentity: str,
        Keywords: List[str] = None,
        Filters: List["KeywordFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeKeywordsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeKeywords.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describekeywordspaginator)
        """

class DescribeOptOutListsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptOutLists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptoutlistspaginator)
    """

    def paginate(
        self, *, OptOutListNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOptOutListsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptOutLists.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptoutlistspaginator)
        """

class DescribeOptedOutNumbersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptedOutNumbers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptedoutnumberspaginator)
    """

    def paginate(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: List[str] = None,
        Filters: List["OptedOutFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOptedOutNumbersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptedOutNumbers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptedoutnumberspaginator)
        """

class DescribePhoneNumbersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePhoneNumbers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describephonenumberspaginator)
    """

    def paginate(
        self,
        *,
        PhoneNumberIds: List[str] = None,
        Filters: List["PhoneNumberFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePhoneNumbersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePhoneNumbers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describephonenumberspaginator)
        """

class DescribePoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describepoolspaginator)
    """

    def paginate(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["PoolFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describepoolspaginator)
        """

class DescribeSenderIdsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSenderIds)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describesenderidspaginator)
    """

    def paginate(
        self,
        *,
        SenderIds: List["SenderIdAndCountryTypeDef"] = None,
        Filters: List["SenderIdFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSenderIdsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSenderIds.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describesenderidspaginator)
        """

class DescribeSpendLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSpendLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describespendlimitspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpendLimitsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSpendLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describespendlimitspaginator)
        """

class ListPoolOriginationIdentitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.ListPoolOriginationIdentities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#listpooloriginationidentitiespaginator)
    """

    def paginate(
        self,
        *,
        PoolId: str,
        Filters: List["PoolOriginationIdentitiesFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoolOriginationIdentitiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.ListPoolOriginationIdentities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#listpooloriginationidentitiespaginator)
        """
