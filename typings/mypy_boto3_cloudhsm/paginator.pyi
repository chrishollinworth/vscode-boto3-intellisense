"""
Type annotations for cloudhsm service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudhsm.client import CloudHSMClient
    from mypy_boto3_cloudhsm.paginator import (
        ListHapgsPaginator,
        ListHsmsPaginator,
        ListLunaClientsPaginator,
    )

    session = Session()
    client: CloudHSMClient = session.client("cloudhsm")

    list_hapgs_paginator: ListHapgsPaginator = client.get_paginator("list_hapgs")
    list_hsms_paginator: ListHsmsPaginator = client.get_paginator("list_hsms")
    list_luna_clients_paginator: ListLunaClientsPaginator = client.get_paginator("list_luna_clients")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListHapgsRequestPaginateTypeDef,
    ListHapgsResponseTypeDef,
    ListHsmsRequestPaginateTypeDef,
    ListHsmsResponseTypeDef,
    ListLunaClientsRequestPaginateTypeDef,
    ListLunaClientsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")

if TYPE_CHECKING:
    _ListHapgsPaginatorBase = Paginator[ListHapgsResponseTypeDef]
else:
    _ListHapgsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHapgsPaginator(_ListHapgsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListHapgs.html#CloudHSM.Paginator.ListHapgs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listhapgspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHapgsRequestPaginateTypeDef]
    ) -> PageIterator[ListHapgsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListHapgs.html#CloudHSM.Paginator.ListHapgs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listhapgspaginator)
        """

if TYPE_CHECKING:
    _ListHsmsPaginatorBase = Paginator[ListHsmsResponseTypeDef]
else:
    _ListHsmsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHsmsPaginator(_ListHsmsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListHsms.html#CloudHSM.Paginator.ListHsms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listhsmspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHsmsRequestPaginateTypeDef]
    ) -> PageIterator[ListHsmsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListHsms.html#CloudHSM.Paginator.ListHsms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listhsmspaginator)
        """

if TYPE_CHECKING:
    _ListLunaClientsPaginatorBase = Paginator[ListLunaClientsResponseTypeDef]
else:
    _ListLunaClientsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLunaClientsPaginator(_ListLunaClientsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListLunaClients.html#CloudHSM.Paginator.ListLunaClients)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listlunaclientspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLunaClientsRequestPaginateTypeDef]
    ) -> PageIterator[ListLunaClientsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/paginator/ListLunaClients.html#CloudHSM.Paginator.ListLunaClients.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators/#listlunaclientspaginator)
        """
