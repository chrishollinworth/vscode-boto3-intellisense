# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for resourcegroupstaggingapi service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient
    from mypy_boto3_resourcegroupstaggingapi.paginator import (
        GetComplianceSummaryPaginator,
        GetResourcesPaginator,
        GetTagKeysPaginator,
        GetTagValuesPaginator,
    )

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")

    get_compliance_summary_paginator: GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_tag_keys_paginator: GetTagKeysPaginator = client.get_paginator("get_tag_keys")
    get_tag_values_paginator: GetTagValuesPaginator = client.get_paginator("get_tag_values")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
)


class GetComplianceSummaryPaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
    """

    def paginate(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetComplianceSummaryOutputTypeDef]:
        """
        [GetComplianceSummary.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
    """

    def paginate(
        self,
        TagFilters: List[TagFilterTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourcesOutputTypeDef]:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources.paginate)
        """


class GetTagKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTagKeysOutputTypeDef]:
        """
        [GetTagKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys.paginate)
        """


class GetTagValuesPaginator(Boto3Paginator):
    """
    [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
    """

    def paginate(
        self, Key: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTagValuesOutputTypeDef]:
        """
        [GetTagValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues.paginate)
        """
