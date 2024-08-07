"""
Type annotations for artifact service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/type_defs.html)

Usage::

    ```python
    from mypy_boto3_artifact.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AcceptanceTypeType,
    NotificationSubscriptionStatusType,
    PublishedStateType,
    UploadStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountSettingsTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetReportMetadataRequestRequestTypeDef",
    "GetReportMetadataResponseTypeDef",
    "GetReportRequestRequestTypeDef",
    "GetReportResponseTypeDef",
    "GetTermForReportRequestRequestTypeDef",
    "GetTermForReportResponseTypeDef",
    "ListReportsRequestRequestTypeDef",
    "ListReportsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountSettingsRequestRequestTypeDef",
    "PutAccountSettingsResponseTypeDef",
    "ReportDetailTypeDef",
    "ReportSummaryTypeDef",
    "ResponseMetadataTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "notificationSubscriptionStatus": NotificationSubscriptionStatusType,
    },
    total=False,
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReportMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetReportMetadataRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
_OptionalGetReportMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetReportMetadataRequestRequestTypeDef",
    {
        "reportVersion": int,
    },
    total=False,
)

class GetReportMetadataRequestRequestTypeDef(
    _RequiredGetReportMetadataRequestRequestTypeDef, _OptionalGetReportMetadataRequestRequestTypeDef
):
    pass

GetReportMetadataResponseTypeDef = TypedDict(
    "GetReportMetadataResponseTypeDef",
    {
        "reportDetails": "ReportDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReportRequestRequestTypeDef = TypedDict(
    "_RequiredGetReportRequestRequestTypeDef",
    {
        "reportId": str,
        "termToken": str,
    },
)
_OptionalGetReportRequestRequestTypeDef = TypedDict(
    "_OptionalGetReportRequestRequestTypeDef",
    {
        "reportVersion": int,
    },
    total=False,
)

class GetReportRequestRequestTypeDef(
    _RequiredGetReportRequestRequestTypeDef, _OptionalGetReportRequestRequestTypeDef
):
    pass

GetReportResponseTypeDef = TypedDict(
    "GetReportResponseTypeDef",
    {
        "documentPresignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTermForReportRequestRequestTypeDef = TypedDict(
    "_RequiredGetTermForReportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
_OptionalGetTermForReportRequestRequestTypeDef = TypedDict(
    "_OptionalGetTermForReportRequestRequestTypeDef",
    {
        "reportVersion": int,
    },
    total=False,
)

class GetTermForReportRequestRequestTypeDef(
    _RequiredGetTermForReportRequestRequestTypeDef, _OptionalGetTermForReportRequestRequestTypeDef
):
    pass

GetTermForReportResponseTypeDef = TypedDict(
    "GetTermForReportResponseTypeDef",
    {
        "documentPresignedUrl": str,
        "termToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsRequestRequestTypeDef = TypedDict(
    "ListReportsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListReportsResponseTypeDef = TypedDict(
    "ListReportsResponseTypeDef",
    {
        "reports": List["ReportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutAccountSettingsRequestRequestTypeDef = TypedDict(
    "PutAccountSettingsRequestRequestTypeDef",
    {
        "notificationSubscriptionStatus": NotificationSubscriptionStatusType,
    },
    total=False,
)

PutAccountSettingsResponseTypeDef = TypedDict(
    "PutAccountSettingsResponseTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportDetailTypeDef = TypedDict(
    "ReportDetailTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "periodStart": datetime,
        "periodEnd": datetime,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "deletedAt": datetime,
        "state": PublishedStateType,
        "arn": str,
        "series": str,
        "category": str,
        "companyName": str,
        "productName": str,
        "termArn": str,
        "version": int,
        "acceptanceType": AcceptanceTypeType,
        "sequenceNumber": int,
        "uploadState": UploadStateType,
        "statusMessage": str,
    },
    total=False,
)

ReportSummaryTypeDef = TypedDict(
    "ReportSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "state": PublishedStateType,
        "arn": str,
        "version": int,
        "uploadState": UploadStateType,
        "description": str,
        "periodStart": datetime,
        "periodEnd": datetime,
        "series": str,
        "category": str,
        "companyName": str,
        "productName": str,
        "statusMessage": str,
        "acceptanceType": AcceptanceTypeType,
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
