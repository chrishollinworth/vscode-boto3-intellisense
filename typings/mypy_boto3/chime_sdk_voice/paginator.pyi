"""
Type annotations for chime-sdk-voice service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_chime_sdk_voice.client import ChimeSDKVoiceClient
    from mypy_boto3_chime_sdk_voice.paginator import (
        ListSipMediaApplicationsPaginator,
        ListSipRulesPaginator,
    )

    session = Session()
    client: ChimeSDKVoiceClient = session.client("chime-sdk-voice")

    list_sip_media_applications_paginator: ListSipMediaApplicationsPaginator = client.get_paginator("list_sip_media_applications")
    list_sip_rules_paginator: ListSipRulesPaginator = client.get_paginator("list_sip_rules")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListSipMediaApplicationsRequestPaginateTypeDef,
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesRequestPaginateTypeDef,
    ListSipRulesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListSipMediaApplicationsPaginator", "ListSipRulesPaginator")

if TYPE_CHECKING:
    _ListSipMediaApplicationsPaginatorBase = Paginator[ListSipMediaApplicationsResponseTypeDef]
else:
    _ListSipMediaApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSipMediaApplicationsPaginator(_ListSipMediaApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/paginator/ListSipMediaApplications.html#ChimeSDKVoice.Paginator.ListSipMediaApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators/#listsipmediaapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSipMediaApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSipMediaApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/paginator/ListSipMediaApplications.html#ChimeSDKVoice.Paginator.ListSipMediaApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators/#listsipmediaapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListSipRulesPaginatorBase = Paginator[ListSipRulesResponseTypeDef]
else:
    _ListSipRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSipRulesPaginator(_ListSipRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/paginator/ListSipRules.html#ChimeSDKVoice.Paginator.ListSipRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators/#listsiprulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSipRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListSipRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/paginator/ListSipRules.html#ChimeSDKVoice.Paginator.ListSipRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators/#listsiprulespaginator)
        """
