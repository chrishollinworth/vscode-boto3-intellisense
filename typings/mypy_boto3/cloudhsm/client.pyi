"""
Type annotations for cloudhsm service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudhsm.client import CloudHSMClient

    session = Session()
    client: CloudHSMClient = session.client("cloudhsm")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListHapgsPaginator, ListHsmsPaginator, ListLunaClientsPaginator
from .type_defs import (
    AddTagsToResourceRequestTypeDef,
    AddTagsToResourceResponseTypeDef,
    CreateHapgRequestTypeDef,
    CreateHapgResponseTypeDef,
    CreateHsmRequestTypeDef,
    CreateHsmResponseTypeDef,
    CreateLunaClientRequestTypeDef,
    CreateLunaClientResponseTypeDef,
    DeleteHapgRequestTypeDef,
    DeleteHapgResponseTypeDef,
    DeleteHsmRequestTypeDef,
    DeleteHsmResponseTypeDef,
    DeleteLunaClientRequestTypeDef,
    DeleteLunaClientResponseTypeDef,
    DescribeHapgRequestTypeDef,
    DescribeHapgResponseTypeDef,
    DescribeHsmRequestTypeDef,
    DescribeHsmResponseTypeDef,
    DescribeLunaClientRequestTypeDef,
    DescribeLunaClientResponseTypeDef,
    GetConfigRequestTypeDef,
    GetConfigResponseTypeDef,
    ListAvailableZonesResponseTypeDef,
    ListHapgsRequestTypeDef,
    ListHapgsResponseTypeDef,
    ListHsmsRequestTypeDef,
    ListHsmsResponseTypeDef,
    ListLunaClientsRequestTypeDef,
    ListLunaClientsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModifyHapgRequestTypeDef,
    ModifyHapgResponseTypeDef,
    ModifyHsmRequestTypeDef,
    ModifyHsmResponseTypeDef,
    ModifyLunaClientRequestTypeDef,
    ModifyLunaClientResponseTypeDef,
    RemoveTagsFromResourceRequestTypeDef,
    RemoveTagsFromResourceResponseTypeDef,
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

__all__ = ("CloudHSMClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    CloudHsmInternalException: Type[BotocoreClientError]
    CloudHsmServiceException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]

class CloudHSMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudHSMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#generate_presigned_url)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceRequestTypeDef]
    ) -> AddTagsToResourceResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#add_tags_to_resource)
        """

    def create_hapg(self, **kwargs: Unpack[CreateHapgRequestTypeDef]) -> CreateHapgResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/create_hapg.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#create_hapg)
        """

    def create_hsm(self, **kwargs: Unpack[CreateHsmRequestTypeDef]) -> CreateHsmResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/create_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#create_hsm)
        """

    def create_luna_client(
        self, **kwargs: Unpack[CreateLunaClientRequestTypeDef]
    ) -> CreateLunaClientResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/create_luna_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#create_luna_client)
        """

    def delete_hapg(self, **kwargs: Unpack[DeleteHapgRequestTypeDef]) -> DeleteHapgResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/delete_hapg.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#delete_hapg)
        """

    def delete_hsm(self, **kwargs: Unpack[DeleteHsmRequestTypeDef]) -> DeleteHsmResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/delete_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#delete_hsm)
        """

    def delete_luna_client(
        self, **kwargs: Unpack[DeleteLunaClientRequestTypeDef]
    ) -> DeleteLunaClientResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/delete_luna_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#delete_luna_client)
        """

    def describe_hapg(
        self, **kwargs: Unpack[DescribeHapgRequestTypeDef]
    ) -> DescribeHapgResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/describe_hapg.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#describe_hapg)
        """

    def describe_hsm(
        self, **kwargs: Unpack[DescribeHsmRequestTypeDef]
    ) -> DescribeHsmResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/describe_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#describe_hsm)
        """

    def describe_luna_client(
        self, **kwargs: Unpack[DescribeLunaClientRequestTypeDef]
    ) -> DescribeLunaClientResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/describe_luna_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#describe_luna_client)
        """

    def get_config(self, **kwargs: Unpack[GetConfigRequestTypeDef]) -> GetConfigResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/get_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#get_config)
        """

    def list_available_zones(self) -> ListAvailableZonesResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/list_available_zones.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#list_available_zones)
        """

    def list_hapgs(self, **kwargs: Unpack[ListHapgsRequestTypeDef]) -> ListHapgsResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/list_hapgs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#list_hapgs)
        """

    def list_hsms(self, **kwargs: Unpack[ListHsmsRequestTypeDef]) -> ListHsmsResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/list_hsms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#list_hsms)
        """

    def list_luna_clients(
        self, **kwargs: Unpack[ListLunaClientsRequestTypeDef]
    ) -> ListLunaClientsResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/list_luna_clients.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#list_luna_clients)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#list_tags_for_resource)
        """

    def modify_hapg(self, **kwargs: Unpack[ModifyHapgRequestTypeDef]) -> ModifyHapgResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/modify_hapg.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#modify_hapg)
        """

    def modify_hsm(self, **kwargs: Unpack[ModifyHsmRequestTypeDef]) -> ModifyHsmResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/modify_hsm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#modify_hsm)
        """

    def modify_luna_client(
        self, **kwargs: Unpack[ModifyLunaClientRequestTypeDef]
    ) -> ModifyLunaClientResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/modify_luna_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#modify_luna_client)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceRequestTypeDef]
    ) -> RemoveTagsFromResourceResponseTypeDef:
        """
        This is documentation for <b>AWS CloudHSM Classic</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#remove_tags_from_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hapgs"]
    ) -> ListHapgsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_hsms"]
    ) -> ListHsmsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_luna_clients"]
    ) -> ListLunaClientsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client/#get_paginator)
        """
