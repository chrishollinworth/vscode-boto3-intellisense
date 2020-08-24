# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for resourcegroupstaggingapi service client

Usage::

    ```python
    import boto3
    from mypy_boto3_resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_resourcegroupstaggingapi.paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
)
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    DescribeReportCreationOutputTypeDef,
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    TagFilterTypeDef,
    TagResourcesOutputTypeDef,
    UntagResourcesOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsTaggingAPIClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    ConstraintViolationException: Type[Boto3ClientError]
    InternalServiceException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    PaginationTokenExpiredException: Type[Boto3ClientError]
    ThrottledException: Type[Boto3ClientError]


class ResourceGroupsTaggingAPIClient:
    """
    [ResourceGroupsTaggingAPI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.can_paginate)
        """

    def describe_report_creation(self) -> DescribeReportCreationOutputTypeDef:
        """
        [Client.describe_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.describe_report_creation)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.generate_presigned_url)
        """

    def get_compliance_summary(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        MaxResults: int = None,
        PaginationToken: str = None,
    ) -> GetComplianceSummaryOutputTypeDef:
        """
        [Client.get_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_compliance_summary)
        """

    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[TagFilterTypeDef] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
    ) -> GetResourcesOutputTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_resources)
        """

    def get_tag_keys(self, PaginationToken: str = None) -> GetTagKeysOutputTypeDef:
        """
        [Client.get_tag_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_keys)
        """

    def get_tag_values(self, Key: str, PaginationToken: str = None) -> GetTagValuesOutputTypeDef:
        """
        [Client.get_tag_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_values)
        """

    def start_report_creation(self, S3Bucket: str) -> Dict[str, Any]:
        """
        [Client.start_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.start_report_creation)
        """

    def tag_resources(
        self, ResourceARNList: List[str], Tags: Dict[str, str]
    ) -> TagResourcesOutputTypeDef:
        """
        [Client.tag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.tag_resources)
        """

    def untag_resources(
        self, ResourceARNList: List[str], TagKeys: List[str]
    ) -> UntagResourcesOutputTypeDef:
        """
        [Client.untag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.untag_resources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_summary"]
    ) -> GetComplianceSummaryPaginator:
        """
        [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_resources"]) -> GetResourcesPaginator:
        """
        [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tag_keys"]) -> GetTagKeysPaginator:
        """
        [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tag_values"]) -> GetTagValuesPaginator:
        """
        [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
