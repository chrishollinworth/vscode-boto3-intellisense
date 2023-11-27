"""
Type annotations for chime-sdk-voice service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_chime_sdk_voice import ChimeSDKVoiceClient
    from mypy_boto3_chime_sdk_voice.paginator import (
        ListSipMediaApplicationsPaginator,
        ListSipRulesPaginator,
    )

    client: ChimeSDKVoiceClient = boto3.client("chime-sdk-voice")

    list_sip_media_applications_paginator: ListSipMediaApplicationsPaginator = client.get_paginator("list_sip_media_applications")
    list_sip_rules_paginator: ListSipRulesPaginator = client.get_paginator("list_sip_rules")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListSipMediaApplicationsPaginator", "ListSipRulesPaginator")

class ListSipMediaApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipMediaApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsipmediaapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSipMediaApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipMediaApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsipmediaapplicationspaginator)
        """

class ListSipRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsiprulespaginator)
    """

    def paginate(
        self, *, SipMediaApplicationId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSipRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsiprulespaginator)
        """
