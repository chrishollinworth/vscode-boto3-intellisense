"""
Type annotations for resourcegroupstaggingapi service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient

    session = Session()
    client: ResourceGroupsTaggingAPIClient = session.client("resourcegroupstaggingapi")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
)
from .type_defs import (
    DescribeReportCreationOutputTypeDef,
    GetComplianceSummaryInputTypeDef,
    GetComplianceSummaryOutputTypeDef,
    GetResourcesInputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysInputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesInputTypeDef,
    GetTagValuesOutputTypeDef,
    StartReportCreationInputTypeDef,
    TagResourcesInputTypeDef,
    TagResourcesOutputTypeDef,
    UntagResourcesInputTypeDef,
    UntagResourcesOutputTypeDef,
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

__all__ = ("ResourceGroupsTaggingAPIClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    PaginationTokenExpiredException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]

class ResourceGroupsTaggingAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResourceGroupsTaggingAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#generate_presigned_url)
        """

    def describe_report_creation(self) -> DescribeReportCreationOutputTypeDef:
        """
        Describes the status of the <code>StartReportCreation</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/describe_report_creation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#describe_report_creation)
        """

    def get_compliance_summary(
        self, **kwargs: Unpack[GetComplianceSummaryInputTypeDef]
    ) -> GetComplianceSummaryOutputTypeDef:
        """
        Returns a table that shows counts of resources that are noncompliant with their
        tag policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_compliance_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_compliance_summary)
        """

    def get_resources(
        self, **kwargs: Unpack[GetResourcesInputTypeDef]
    ) -> GetResourcesOutputTypeDef:
        """
        Returns all the tagged or previously tagged resources that are located in the
        specified Amazon Web Services Region for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_resources)
        """

    def get_tag_keys(self, **kwargs: Unpack[GetTagKeysInputTypeDef]) -> GetTagKeysOutputTypeDef:
        """
        Returns all tag keys currently in use in the specified Amazon Web Services
        Region for the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_tag_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_tag_keys)
        """

    def get_tag_values(
        self, **kwargs: Unpack[GetTagValuesInputTypeDef]
    ) -> GetTagValuesOutputTypeDef:
        """
        Returns all tag values for the specified key that are used in the specified
        Amazon Web Services Region for the calling account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_tag_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_tag_values)
        """

    def start_report_creation(
        self, **kwargs: Unpack[StartReportCreationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Generates a report that lists all tagged resources in the accounts across your
        organization and tells whether each resource is compliant with the effective
        tag policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/start_report_creation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#start_report_creation)
        """

    def tag_resources(
        self, **kwargs: Unpack[TagResourcesInputTypeDef]
    ) -> TagResourcesOutputTypeDef:
        """
        Applies one or more tags to the specified resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/tag_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#tag_resources)
        """

    def untag_resources(
        self, **kwargs: Unpack[UntagResourcesInputTypeDef]
    ) -> UntagResourcesOutputTypeDef:
        """
        Removes the specified tags from the specified resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/untag_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#untag_resources)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_compliance_summary"]
    ) -> GetComplianceSummaryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resources"]
    ) -> GetResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_tag_keys"]
    ) -> GetTagKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_tag_values"]
    ) -> GetTagValuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/client/#get_paginator)
        """
