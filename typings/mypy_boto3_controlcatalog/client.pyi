"""
Type annotations for controlcatalog service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_controlcatalog.client import ControlCatalogClient

    session = Session()
    client: ControlCatalogClient = session.client("controlcatalog")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCommonControlsPaginator,
    ListControlsPaginator,
    ListDomainsPaginator,
    ListObjectivesPaginator,
)
from .type_defs import (
    GetControlRequestTypeDef,
    GetControlResponseTypeDef,
    ListCommonControlsRequestTypeDef,
    ListCommonControlsResponseTypeDef,
    ListControlsRequestTypeDef,
    ListControlsResponseTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResponseTypeDef,
    ListObjectivesRequestTypeDef,
    ListObjectivesResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ControlCatalogClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ControlCatalogClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog.html#ControlCatalog.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlCatalogClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog.html#ControlCatalog.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#generate_presigned_url)
        """

    def get_control(self, **kwargs: Unpack[GetControlRequestTypeDef]) -> GetControlResponseTypeDef:
        """
        Returns details about a specific control, most notably a list of Amazon Web
        Services Regions where this control is supported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/get_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#get_control)
        """

    def list_common_controls(
        self, **kwargs: Unpack[ListCommonControlsRequestTypeDef]
    ) -> ListCommonControlsResponseTypeDef:
        """
        Returns a paginated list of common controls from the Amazon Web Services
        Control Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/list_common_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#list_common_controls)
        """

    def list_controls(
        self, **kwargs: Unpack[ListControlsRequestTypeDef]
    ) -> ListControlsResponseTypeDef:
        """
        Returns a paginated list of all available controls in the Amazon Web Services
        Control Catalog library.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/list_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#list_controls)
        """

    def list_domains(
        self, **kwargs: Unpack[ListDomainsRequestTypeDef]
    ) -> ListDomainsResponseTypeDef:
        """
        Returns a paginated list of domains from the Amazon Web Services Control
        Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#list_domains)
        """

    def list_objectives(
        self, **kwargs: Unpack[ListObjectivesRequestTypeDef]
    ) -> ListObjectivesResponseTypeDef:
        """
        Returns a paginated list of objectives from the Amazon Web Services Control
        Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/list_objectives.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#list_objectives)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_common_controls"]
    ) -> ListCommonControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_controls"]
    ) -> ListControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_objectives"]
    ) -> ListObjectivesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client/#get_paginator)
        """
