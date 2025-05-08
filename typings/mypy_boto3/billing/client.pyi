"""
Type annotations for billing service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_billing.client import BillingClient

    session = Session()
    client: BillingClient = session.client("billing")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListBillingViewsPaginator, ListSourceViewsForBillingViewPaginator
from .type_defs import (
    CreateBillingViewRequestTypeDef,
    CreateBillingViewResponseTypeDef,
    DeleteBillingViewRequestTypeDef,
    DeleteBillingViewResponseTypeDef,
    GetBillingViewRequestTypeDef,
    GetBillingViewResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListBillingViewsRequestTypeDef,
    ListBillingViewsResponseTypeDef,
    ListSourceViewsForBillingViewRequestTypeDef,
    ListSourceViewsForBillingViewResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBillingViewRequestTypeDef,
    UpdateBillingViewResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BillingClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BillingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing.html#Billing.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing.html#Billing.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#generate_presigned_url)
        """

    def create_billing_view(
        self, **kwargs: Unpack[CreateBillingViewRequestTypeDef]
    ) -> CreateBillingViewResponseTypeDef:
        """
        Creates a billing view with the specified billing view attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/create_billing_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#create_billing_view)
        """

    def delete_billing_view(
        self, **kwargs: Unpack[DeleteBillingViewRequestTypeDef]
    ) -> DeleteBillingViewResponseTypeDef:
        """
        Deletes the specified billing view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/delete_billing_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#delete_billing_view)
        """

    def get_billing_view(
        self, **kwargs: Unpack[GetBillingViewRequestTypeDef]
    ) -> GetBillingViewResponseTypeDef:
        """
        Returns the metadata associated to the specified billing view ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/get_billing_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#get_billing_view)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Returns the resource-based policy document attached to the resource in
        <code>JSON</code> format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#get_resource_policy)
        """

    def list_billing_views(
        self, **kwargs: Unpack[ListBillingViewsRequestTypeDef]
    ) -> ListBillingViewsResponseTypeDef:
        """
        Lists the billing views available for a given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/list_billing_views.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#list_billing_views)
        """

    def list_source_views_for_billing_view(
        self, **kwargs: Unpack[ListSourceViewsForBillingViewRequestTypeDef]
    ) -> ListSourceViewsForBillingViewResponseTypeDef:
        """
        Lists the source views (managed Amazon Web Services billing views) associated
        with the billing view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/list_source_views_for_billing_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#list_source_views_for_billing_view)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags associated with the billing view resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        An API operation for adding one or more tags (key-value pairs) to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#untag_resource)
        """

    def update_billing_view(
        self, **kwargs: Unpack[UpdateBillingViewRequestTypeDef]
    ) -> UpdateBillingViewResponseTypeDef:
        """
        An API to update the attributes of the billing view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/update_billing_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#update_billing_view)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_billing_views"]
    ) -> ListBillingViewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_views_for_billing_view"]
    ) -> ListSourceViewsForBillingViewPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billing/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/client/#get_paginator)
        """
