"""
Type annotations for ivs-realtime service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ivs_realtime.client import IvsrealtimeClient
    from mypy_boto3_ivs_realtime.paginator import (
        ListIngestConfigurationsPaginator,
        ListPublicKeysPaginator,
    )

    session = Session()
    client: IvsrealtimeClient = session.client("ivs-realtime")

    list_ingest_configurations_paginator: ListIngestConfigurationsPaginator = client.get_paginator("list_ingest_configurations")
    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListIngestConfigurationsRequestPaginateTypeDef,
    ListIngestConfigurationsResponseTypeDef,
    ListPublicKeysRequestPaginateTypeDef,
    ListPublicKeysResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListIngestConfigurationsPaginator", "ListPublicKeysPaginator")

if TYPE_CHECKING:
    _ListIngestConfigurationsPaginatorBase = Paginator[ListIngestConfigurationsResponseTypeDef]
else:
    _ListIngestConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIngestConfigurationsPaginator(_ListIngestConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/paginator/ListIngestConfigurations.html#Ivsrealtime.Paginator.ListIngestConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators/#listingestconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIngestConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListIngestConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/paginator/ListIngestConfigurations.html#Ivsrealtime.Paginator.ListIngestConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators/#listingestconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListPublicKeysPaginatorBase = Paginator[ListPublicKeysResponseTypeDef]
else:
    _ListPublicKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListPublicKeysPaginator(_ListPublicKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/paginator/ListPublicKeys.html#Ivsrealtime.Paginator.ListPublicKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators/#listpublickeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPublicKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs-realtime/paginator/ListPublicKeys.html#Ivsrealtime.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators/#listpublickeyspaginator)
        """
