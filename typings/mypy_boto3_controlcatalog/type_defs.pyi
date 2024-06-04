"""
Type annotations for controlcatalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_controlcatalog.type_defs import AssociatedDomainSummaryTypeDef

    data: AssociatedDomainSummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociatedDomainSummaryTypeDef",
    "AssociatedObjectiveSummaryTypeDef",
    "CommonControlFilterTypeDef",
    "CommonControlSummaryTypeDef",
    "DomainResourceFilterTypeDef",
    "DomainSummaryTypeDef",
    "ListCommonControlsRequestRequestTypeDef",
    "ListCommonControlsResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListObjectivesRequestRequestTypeDef",
    "ListObjectivesResponseTypeDef",
    "ObjectiveFilterTypeDef",
    "ObjectiveResourceFilterTypeDef",
    "ObjectiveSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

AssociatedDomainSummaryTypeDef = TypedDict(
    "AssociatedDomainSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

AssociatedObjectiveSummaryTypeDef = TypedDict(
    "AssociatedObjectiveSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

CommonControlFilterTypeDef = TypedDict(
    "CommonControlFilterTypeDef",
    {
        "Objectives": List["ObjectiveResourceFilterTypeDef"],
    },
    total=False,
)

CommonControlSummaryTypeDef = TypedDict(
    "CommonControlSummaryTypeDef",
    {
        "Arn": str,
        "CreateTime": datetime,
        "Description": str,
        "Domain": "AssociatedDomainSummaryTypeDef",
        "LastUpdateTime": datetime,
        "Name": str,
        "Objective": "AssociatedObjectiveSummaryTypeDef",
    },
)

DomainResourceFilterTypeDef = TypedDict(
    "DomainResourceFilterTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "Arn": str,
        "CreateTime": datetime,
        "Description": str,
        "LastUpdateTime": datetime,
        "Name": str,
    },
)

ListCommonControlsRequestRequestTypeDef = TypedDict(
    "ListCommonControlsRequestRequestTypeDef",
    {
        "CommonControlFilter": "CommonControlFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCommonControlsResponseTypeDef = TypedDict(
    "ListCommonControlsResponseTypeDef",
    {
        "CommonControls": List["CommonControlSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectivesRequestRequestTypeDef = TypedDict(
    "ListObjectivesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ObjectiveFilter": "ObjectiveFilterTypeDef",
    },
    total=False,
)

ListObjectivesResponseTypeDef = TypedDict(
    "ListObjectivesResponseTypeDef",
    {
        "NextToken": str,
        "Objectives": List["ObjectiveSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectiveFilterTypeDef = TypedDict(
    "ObjectiveFilterTypeDef",
    {
        "Domains": List["DomainResourceFilterTypeDef"],
    },
    total=False,
)

ObjectiveResourceFilterTypeDef = TypedDict(
    "ObjectiveResourceFilterTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

ObjectiveSummaryTypeDef = TypedDict(
    "ObjectiveSummaryTypeDef",
    {
        "Arn": str,
        "CreateTime": datetime,
        "Description": str,
        "Domain": "AssociatedDomainSummaryTypeDef",
        "LastUpdateTime": datetime,
        "Name": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
