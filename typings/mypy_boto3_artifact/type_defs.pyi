"""
Type annotations for artifact service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_artifact.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AcceptanceTypeType,
    AgreementTypeType,
    CustomerAgreementStateType,
    NotificationSubscriptionStatusType,
    PublishedStateType,
    UploadStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountSettingsTypeDef",
    "CustomerAgreementSummaryTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetReportMetadataRequestTypeDef",
    "GetReportMetadataResponseTypeDef",
    "GetReportRequestTypeDef",
    "GetReportResponseTypeDef",
    "GetTermForReportRequestTypeDef",
    "GetTermForReportResponseTypeDef",
    "ListCustomerAgreementsRequestPaginateTypeDef",
    "ListCustomerAgreementsRequestTypeDef",
    "ListCustomerAgreementsResponseTypeDef",
    "ListReportsRequestPaginateTypeDef",
    "ListReportsRequestTypeDef",
    "ListReportsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountSettingsRequestTypeDef",
    "PutAccountSettingsResponseTypeDef",
    "ReportDetailTypeDef",
    "ReportSummaryTypeDef",
    "ResponseMetadataTypeDef",
)

class AccountSettingsTypeDef(TypedDict):
    notificationSubscriptionStatus: NotRequired[NotificationSubscriptionStatusType]

CustomerAgreementSummaryTypeDef = TypedDict(
    "CustomerAgreementSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "agreementArn": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "organizationArn": NotRequired[str],
        "effectiveStart": NotRequired[datetime],
        "effectiveEnd": NotRequired[datetime],
        "state": NotRequired[CustomerAgreementStateType],
        "description": NotRequired[str],
        "acceptanceTerms": NotRequired[List[str]],
        "terminateTerms": NotRequired[List[str]],
        "type": NotRequired[AgreementTypeType],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetReportMetadataRequestTypeDef(TypedDict):
    reportId: str
    reportVersion: NotRequired[int]

ReportDetailTypeDef = TypedDict(
    "ReportDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "periodStart": NotRequired[datetime],
        "periodEnd": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "lastModifiedAt": NotRequired[datetime],
        "deletedAt": NotRequired[datetime],
        "state": NotRequired[PublishedStateType],
        "arn": NotRequired[str],
        "series": NotRequired[str],
        "category": NotRequired[str],
        "companyName": NotRequired[str],
        "productName": NotRequired[str],
        "termArn": NotRequired[str],
        "version": NotRequired[int],
        "acceptanceType": NotRequired[AcceptanceTypeType],
        "sequenceNumber": NotRequired[int],
        "uploadState": NotRequired[UploadStateType],
        "statusMessage": NotRequired[str],
    },
)

class GetReportRequestTypeDef(TypedDict):
    reportId: str
    termToken: str
    reportVersion: NotRequired[int]

class GetTermForReportRequestTypeDef(TypedDict):
    reportId: str
    reportVersion: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCustomerAgreementsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListReportsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ReportSummaryTypeDef = TypedDict(
    "ReportSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "state": NotRequired[PublishedStateType],
        "arn": NotRequired[str],
        "version": NotRequired[int],
        "uploadState": NotRequired[UploadStateType],
        "description": NotRequired[str],
        "periodStart": NotRequired[datetime],
        "periodEnd": NotRequired[datetime],
        "series": NotRequired[str],
        "category": NotRequired[str],
        "companyName": NotRequired[str],
        "productName": NotRequired[str],
        "statusMessage": NotRequired[str],
        "acceptanceType": NotRequired[AcceptanceTypeType],
    },
)

class PutAccountSettingsRequestTypeDef(TypedDict):
    notificationSubscriptionStatus: NotRequired[NotificationSubscriptionStatusType]

class GetAccountSettingsResponseTypeDef(TypedDict):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportResponseTypeDef(TypedDict):
    documentPresignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTermForReportResponseTypeDef(TypedDict):
    documentPresignedUrl: str
    termToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomerAgreementsResponseTypeDef(TypedDict):
    customerAgreements: List[CustomerAgreementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutAccountSettingsResponseTypeDef(TypedDict):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportMetadataResponseTypeDef(TypedDict):
    reportDetails: ReportDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomerAgreementsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReportsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReportsResponseTypeDef(TypedDict):
    reports: List[ReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
