"""
Type annotations for outposts service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_outposts.client import OutpostsClient

    session = Session()
    client: OutpostsClient = session.client("outposts")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetOutpostInstanceTypesPaginator,
    GetOutpostSupportedInstanceTypesPaginator,
    ListAssetInstancesPaginator,
    ListAssetsPaginator,
    ListBlockingInstancesForCapacityTaskPaginator,
    ListCapacityTasksPaginator,
    ListCatalogItemsPaginator,
    ListOrdersPaginator,
    ListOutpostsPaginator,
    ListSitesPaginator,
)
from .type_defs import (
    CancelCapacityTaskInputTypeDef,
    CancelOrderInputTypeDef,
    CreateOrderInputTypeDef,
    CreateOrderOutputTypeDef,
    CreateOutpostInputTypeDef,
    CreateOutpostOutputTypeDef,
    CreateSiteInputTypeDef,
    CreateSiteOutputTypeDef,
    DeleteOutpostInputTypeDef,
    DeleteSiteInputTypeDef,
    GetCapacityTaskInputTypeDef,
    GetCapacityTaskOutputTypeDef,
    GetCatalogItemInputTypeDef,
    GetCatalogItemOutputTypeDef,
    GetConnectionRequestTypeDef,
    GetConnectionResponseTypeDef,
    GetOrderInputTypeDef,
    GetOrderOutputTypeDef,
    GetOutpostInputTypeDef,
    GetOutpostInstanceTypesInputTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostOutputTypeDef,
    GetOutpostSupportedInstanceTypesInputTypeDef,
    GetOutpostSupportedInstanceTypesOutputTypeDef,
    GetSiteAddressInputTypeDef,
    GetSiteAddressOutputTypeDef,
    GetSiteInputTypeDef,
    GetSiteOutputTypeDef,
    ListAssetInstancesInputTypeDef,
    ListAssetInstancesOutputTypeDef,
    ListAssetsInputTypeDef,
    ListAssetsOutputTypeDef,
    ListBlockingInstancesForCapacityTaskInputTypeDef,
    ListBlockingInstancesForCapacityTaskOutputTypeDef,
    ListCapacityTasksInputTypeDef,
    ListCapacityTasksOutputTypeDef,
    ListCatalogItemsInputTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersInputTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsInputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesInputTypeDef,
    ListSitesOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartCapacityTaskInputTypeDef,
    StartCapacityTaskOutputTypeDef,
    StartConnectionRequestTypeDef,
    StartConnectionResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateOutpostInputTypeDef,
    UpdateOutpostOutputTypeDef,
    UpdateSiteAddressInputTypeDef,
    UpdateSiteAddressOutputTypeDef,
    UpdateSiteInputTypeDef,
    UpdateSiteOutputTypeDef,
    UpdateSiteRackPhysicalPropertiesInputTypeDef,
    UpdateSiteRackPhysicalPropertiesOutputTypeDef,
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

__all__ = ("OutpostsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OutpostsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OutpostsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#generate_presigned_url)
        """

    def cancel_capacity_task(
        self, **kwargs: Unpack[CancelCapacityTaskInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the capacity task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/cancel_capacity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#cancel_capacity_task)
        """

    def cancel_order(self, **kwargs: Unpack[CancelOrderInputTypeDef]) -> Dict[str, Any]:
        """
        Cancels the specified order for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/cancel_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#cancel_order)
        """

    def create_order(self, **kwargs: Unpack[CreateOrderInputTypeDef]) -> CreateOrderOutputTypeDef:
        """
        Creates an order for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/create_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#create_order)
        """

    def create_outpost(
        self, **kwargs: Unpack[CreateOutpostInputTypeDef]
    ) -> CreateOutpostOutputTypeDef:
        """
        Creates an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/create_outpost.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#create_outpost)
        """

    def create_site(self, **kwargs: Unpack[CreateSiteInputTypeDef]) -> CreateSiteOutputTypeDef:
        """
        Creates a site for an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/create_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#create_site)
        """

    def delete_outpost(self, **kwargs: Unpack[DeleteOutpostInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/delete_outpost.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#delete_outpost)
        """

    def delete_site(self, **kwargs: Unpack[DeleteSiteInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/delete_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#delete_site)
        """

    def get_capacity_task(
        self, **kwargs: Unpack[GetCapacityTaskInputTypeDef]
    ) -> GetCapacityTaskOutputTypeDef:
        """
        Gets details of the specified capacity task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_capacity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_capacity_task)
        """

    def get_catalog_item(
        self, **kwargs: Unpack[GetCatalogItemInputTypeDef]
    ) -> GetCatalogItemOutputTypeDef:
        """
        Gets information about the specified catalog item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_catalog_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_catalog_item)
        """

    def get_connection(
        self, **kwargs: Unpack[GetConnectionRequestTypeDef]
    ) -> GetConnectionResponseTypeDef:
        """
        Amazon Web Services uses this action to install Outpost servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_connection)
        """

    def get_order(self, **kwargs: Unpack[GetOrderInputTypeDef]) -> GetOrderOutputTypeDef:
        """
        Gets information about the specified order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_order)
        """

    def get_outpost(self, **kwargs: Unpack[GetOutpostInputTypeDef]) -> GetOutpostOutputTypeDef:
        """
        Gets information about the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_outpost.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_outpost)
        """

    def get_outpost_instance_types(
        self, **kwargs: Unpack[GetOutpostInstanceTypesInputTypeDef]
    ) -> GetOutpostInstanceTypesOutputTypeDef:
        """
        Gets the instance types for the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_outpost_instance_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_outpost_instance_types)
        """

    def get_outpost_supported_instance_types(
        self, **kwargs: Unpack[GetOutpostSupportedInstanceTypesInputTypeDef]
    ) -> GetOutpostSupportedInstanceTypesOutputTypeDef:
        """
        Gets the instance types that an Outpost can support in
        <code>InstanceTypeCapacity</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_outpost_supported_instance_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_outpost_supported_instance_types)
        """

    def get_site(self, **kwargs: Unpack[GetSiteInputTypeDef]) -> GetSiteOutputTypeDef:
        """
        Gets information about the specified Outpost site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_site)
        """

    def get_site_address(
        self, **kwargs: Unpack[GetSiteAddressInputTypeDef]
    ) -> GetSiteAddressOutputTypeDef:
        """
        Gets the site address of the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_site_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_site_address)
        """

    def list_asset_instances(
        self, **kwargs: Unpack[ListAssetInstancesInputTypeDef]
    ) -> ListAssetInstancesOutputTypeDef:
        """
        A list of Amazon EC2 instances, belonging to all accounts, running on the
        specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_asset_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_asset_instances)
        """

    def list_assets(self, **kwargs: Unpack[ListAssetsInputTypeDef]) -> ListAssetsOutputTypeDef:
        """
        Lists the hardware assets for the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_assets)
        """

    def list_blocking_instances_for_capacity_task(
        self, **kwargs: Unpack[ListBlockingInstancesForCapacityTaskInputTypeDef]
    ) -> ListBlockingInstancesForCapacityTaskOutputTypeDef:
        """
        A list of Amazon EC2 instances running on the Outpost and belonging to the
        account that initiated the capacity task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_blocking_instances_for_capacity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_blocking_instances_for_capacity_task)
        """

    def list_capacity_tasks(
        self, **kwargs: Unpack[ListCapacityTasksInputTypeDef]
    ) -> ListCapacityTasksOutputTypeDef:
        """
        Lists the capacity tasks for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_capacity_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_capacity_tasks)
        """

    def list_catalog_items(
        self, **kwargs: Unpack[ListCatalogItemsInputTypeDef]
    ) -> ListCatalogItemsOutputTypeDef:
        """
        Lists the items in the catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_catalog_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_catalog_items)
        """

    def list_orders(self, **kwargs: Unpack[ListOrdersInputTypeDef]) -> ListOrdersOutputTypeDef:
        """
        Lists the Outpost orders for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_orders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_orders)
        """

    def list_outposts(
        self, **kwargs: Unpack[ListOutpostsInputTypeDef]
    ) -> ListOutpostsOutputTypeDef:
        """
        Lists the Outposts for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_outposts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_outposts)
        """

    def list_sites(self, **kwargs: Unpack[ListSitesInputTypeDef]) -> ListSitesOutputTypeDef:
        """
        Lists the Outpost sites for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_sites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_sites)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#list_tags_for_resource)
        """

    def start_capacity_task(
        self, **kwargs: Unpack[StartCapacityTaskInputTypeDef]
    ) -> StartCapacityTaskOutputTypeDef:
        """
        Starts the specified capacity task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/start_capacity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#start_capacity_task)
        """

    def start_connection(
        self, **kwargs: Unpack[StartConnectionRequestTypeDef]
    ) -> StartConnectionResponseTypeDef:
        """
        Amazon Web Services uses this action to install Outpost servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/start_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#start_connection)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#untag_resource)
        """

    def update_outpost(
        self, **kwargs: Unpack[UpdateOutpostInputTypeDef]
    ) -> UpdateOutpostOutputTypeDef:
        """
        Updates an Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/update_outpost.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#update_outpost)
        """

    def update_site(self, **kwargs: Unpack[UpdateSiteInputTypeDef]) -> UpdateSiteOutputTypeDef:
        """
        Updates the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/update_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#update_site)
        """

    def update_site_address(
        self, **kwargs: Unpack[UpdateSiteAddressInputTypeDef]
    ) -> UpdateSiteAddressOutputTypeDef:
        """
        Updates the address of the specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/update_site_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#update_site_address)
        """

    def update_site_rack_physical_properties(
        self, **kwargs: Unpack[UpdateSiteRackPhysicalPropertiesInputTypeDef]
    ) -> UpdateSiteRackPhysicalPropertiesOutputTypeDef:
        """
        Update the physical and logistical details for a rack at a site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/update_site_rack_physical_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#update_site_rack_physical_properties)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_outpost_instance_types"]
    ) -> GetOutpostInstanceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_outpost_supported_instance_types"]
    ) -> GetOutpostSupportedInstanceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_instances"]
    ) -> ListAssetInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assets"]
    ) -> ListAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_blocking_instances_for_capacity_task"]
    ) -> ListBlockingInstancesForCapacityTaskPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_capacity_tasks"]
    ) -> ListCapacityTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_catalog_items"]
    ) -> ListCatalogItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_orders"]
    ) -> ListOrdersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_outposts"]
    ) -> ListOutpostsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sites"]
    ) -> ListSitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/client/#get_paginator)
        """
