"""
Type annotations for redshift-serverless service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_redshift_serverless.type_defs import AssociationTypeDef

    data: AssociationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    LogExportType,
    ManagedWorkgroupStatusType,
    NamespaceStatusType,
    OfferingTypeType,
    PerformanceTargetStatusType,
    SnapshotStatusType,
    StateType,
    UsageLimitBreachActionType,
    UsageLimitPeriodType,
    UsageLimitUsageTypeType,
    WorkgroupStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociationTypeDef",
    "ConfigParameterTypeDef",
    "ConvertRecoveryPointToSnapshotRequestTypeDef",
    "ConvertRecoveryPointToSnapshotResponseTypeDef",
    "CreateCustomDomainAssociationRequestTypeDef",
    "CreateCustomDomainAssociationResponseTypeDef",
    "CreateEndpointAccessRequestTypeDef",
    "CreateEndpointAccessResponseTypeDef",
    "CreateNamespaceRequestTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateReservationRequestTypeDef",
    "CreateReservationResponseTypeDef",
    "CreateScheduledActionRequestTypeDef",
    "CreateScheduledActionResponseTypeDef",
    "CreateSnapshotCopyConfigurationRequestTypeDef",
    "CreateSnapshotCopyConfigurationResponseTypeDef",
    "CreateSnapshotRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateSnapshotScheduleActionParametersOutputTypeDef",
    "CreateSnapshotScheduleActionParametersTypeDef",
    "CreateUsageLimitRequestTypeDef",
    "CreateUsageLimitResponseTypeDef",
    "CreateWorkgroupRequestTypeDef",
    "CreateWorkgroupResponseTypeDef",
    "DeleteCustomDomainAssociationRequestTypeDef",
    "DeleteEndpointAccessRequestTypeDef",
    "DeleteEndpointAccessResponseTypeDef",
    "DeleteNamespaceRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteScheduledActionRequestTypeDef",
    "DeleteScheduledActionResponseTypeDef",
    "DeleteSnapshotCopyConfigurationRequestTypeDef",
    "DeleteSnapshotCopyConfigurationResponseTypeDef",
    "DeleteSnapshotRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteUsageLimitRequestTypeDef",
    "DeleteUsageLimitResponseTypeDef",
    "DeleteWorkgroupRequestTypeDef",
    "DeleteWorkgroupResponseTypeDef",
    "EndpointAccessTypeDef",
    "EndpointTypeDef",
    "GetCredentialsRequestTypeDef",
    "GetCredentialsResponseTypeDef",
    "GetCustomDomainAssociationRequestTypeDef",
    "GetCustomDomainAssociationResponseTypeDef",
    "GetEndpointAccessRequestTypeDef",
    "GetEndpointAccessResponseTypeDef",
    "GetNamespaceRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetRecoveryPointRequestTypeDef",
    "GetRecoveryPointResponseTypeDef",
    "GetReservationOfferingRequestTypeDef",
    "GetReservationOfferingResponseTypeDef",
    "GetReservationRequestTypeDef",
    "GetReservationResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetScheduledActionRequestTypeDef",
    "GetScheduledActionResponseTypeDef",
    "GetSnapshotRequestTypeDef",
    "GetSnapshotResponseTypeDef",
    "GetTableRestoreStatusRequestTypeDef",
    "GetTableRestoreStatusResponseTypeDef",
    "GetTrackRequestTypeDef",
    "GetTrackResponseTypeDef",
    "GetUsageLimitRequestTypeDef",
    "GetUsageLimitResponseTypeDef",
    "GetWorkgroupRequestTypeDef",
    "GetWorkgroupResponseTypeDef",
    "ListCustomDomainAssociationsRequestPaginateTypeDef",
    "ListCustomDomainAssociationsRequestTypeDef",
    "ListCustomDomainAssociationsResponseTypeDef",
    "ListEndpointAccessRequestPaginateTypeDef",
    "ListEndpointAccessRequestTypeDef",
    "ListEndpointAccessResponseTypeDef",
    "ListManagedWorkgroupsRequestPaginateTypeDef",
    "ListManagedWorkgroupsRequestTypeDef",
    "ListManagedWorkgroupsResponseTypeDef",
    "ListNamespacesRequestPaginateTypeDef",
    "ListNamespacesRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListRecoveryPointsRequestPaginateTypeDef",
    "ListRecoveryPointsRequestTypeDef",
    "ListRecoveryPointsResponseTypeDef",
    "ListReservationOfferingsRequestPaginateTypeDef",
    "ListReservationOfferingsRequestTypeDef",
    "ListReservationOfferingsResponseTypeDef",
    "ListReservationsRequestPaginateTypeDef",
    "ListReservationsRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListScheduledActionsRequestPaginateTypeDef",
    "ListScheduledActionsRequestTypeDef",
    "ListScheduledActionsResponseTypeDef",
    "ListSnapshotCopyConfigurationsRequestPaginateTypeDef",
    "ListSnapshotCopyConfigurationsRequestTypeDef",
    "ListSnapshotCopyConfigurationsResponseTypeDef",
    "ListSnapshotsRequestPaginateTypeDef",
    "ListSnapshotsRequestTypeDef",
    "ListSnapshotsResponseTypeDef",
    "ListTableRestoreStatusRequestPaginateTypeDef",
    "ListTableRestoreStatusRequestTypeDef",
    "ListTableRestoreStatusResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTracksRequestPaginateTypeDef",
    "ListTracksRequestTypeDef",
    "ListTracksResponseTypeDef",
    "ListUsageLimitsRequestPaginateTypeDef",
    "ListUsageLimitsRequestTypeDef",
    "ListUsageLimitsResponseTypeDef",
    "ListWorkgroupsRequestPaginateTypeDef",
    "ListWorkgroupsRequestTypeDef",
    "ListWorkgroupsResponseTypeDef",
    "ManagedWorkgroupListItemTypeDef",
    "NamespaceTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceTargetTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RecoveryPointTypeDef",
    "ReservationOfferingTypeDef",
    "ReservationTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromRecoveryPointRequestTypeDef",
    "RestoreFromRecoveryPointResponseTypeDef",
    "RestoreFromSnapshotRequestTypeDef",
    "RestoreFromSnapshotResponseTypeDef",
    "RestoreTableFromRecoveryPointRequestTypeDef",
    "RestoreTableFromRecoveryPointResponseTypeDef",
    "RestoreTableFromSnapshotRequestTypeDef",
    "RestoreTableFromSnapshotResponseTypeDef",
    "ScheduleOutputTypeDef",
    "ScheduleTypeDef",
    "ScheduleUnionTypeDef",
    "ScheduledActionAssociationTypeDef",
    "ScheduledActionResponseTypeDef",
    "ServerlessTrackTypeDef",
    "SnapshotCopyConfigurationTypeDef",
    "SnapshotTypeDef",
    "TableRestoreStatusTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetActionOutputTypeDef",
    "TargetActionTypeDef",
    "TargetActionUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCustomDomainAssociationRequestTypeDef",
    "UpdateCustomDomainAssociationResponseTypeDef",
    "UpdateEndpointAccessRequestTypeDef",
    "UpdateEndpointAccessResponseTypeDef",
    "UpdateNamespaceRequestTypeDef",
    "UpdateNamespaceResponseTypeDef",
    "UpdateScheduledActionRequestTypeDef",
    "UpdateScheduledActionResponseTypeDef",
    "UpdateSnapshotCopyConfigurationRequestTypeDef",
    "UpdateSnapshotCopyConfigurationResponseTypeDef",
    "UpdateSnapshotRequestTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "UpdateTargetTypeDef",
    "UpdateUsageLimitRequestTypeDef",
    "UpdateUsageLimitResponseTypeDef",
    "UpdateWorkgroupRequestTypeDef",
    "UpdateWorkgroupResponseTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WorkgroupTypeDef",
)

class AssociationTypeDef(TypedDict):
    customDomainCertificateArn: NotRequired[str]
    customDomainCertificateExpiryTime: NotRequired[datetime]
    customDomainName: NotRequired[str]
    workgroupName: NotRequired[str]

class ConfigParameterTypeDef(TypedDict):
    parameterKey: NotRequired[str]
    parameterValue: NotRequired[str]

class TagTypeDef(TypedDict):
    key: str
    value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SnapshotTypeDef(TypedDict):
    accountsWithProvisionedRestoreAccess: NotRequired[List[str]]
    accountsWithRestoreAccess: NotRequired[List[str]]
    actualIncrementalBackupSizeInMegaBytes: NotRequired[float]
    adminPasswordSecretArn: NotRequired[str]
    adminPasswordSecretKmsKeyId: NotRequired[str]
    adminUsername: NotRequired[str]
    backupProgressInMegaBytes: NotRequired[float]
    currentBackupRateInMegaBytesPerSecond: NotRequired[float]
    elapsedTimeInSeconds: NotRequired[int]
    estimatedSecondsToCompletion: NotRequired[int]
    kmsKeyId: NotRequired[str]
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    ownerAccount: NotRequired[str]
    snapshotArn: NotRequired[str]
    snapshotCreateTime: NotRequired[datetime]
    snapshotName: NotRequired[str]
    snapshotRemainingDays: NotRequired[int]
    snapshotRetentionPeriod: NotRequired[int]
    snapshotRetentionStartTime: NotRequired[datetime]
    status: NotRequired[SnapshotStatusType]
    totalBackupSizeInMegaBytes: NotRequired[float]

class CreateCustomDomainAssociationRequestTypeDef(TypedDict):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class CreateEndpointAccessRequestTypeDef(TypedDict):
    endpointName: str
    subnetIds: Sequence[str]
    workgroupName: str
    ownerAccount: NotRequired[str]
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class NamespaceTypeDef(TypedDict):
    adminPasswordSecretArn: NotRequired[str]
    adminPasswordSecretKmsKeyId: NotRequired[str]
    adminUsername: NotRequired[str]
    creationDate: NotRequired[datetime]
    dbName: NotRequired[str]
    defaultIamRoleArn: NotRequired[str]
    iamRoles: NotRequired[List[str]]
    kmsKeyId: NotRequired[str]
    logExports: NotRequired[List[LogExportType]]
    namespaceArn: NotRequired[str]
    namespaceId: NotRequired[str]
    namespaceName: NotRequired[str]
    status: NotRequired[NamespaceStatusType]

class CreateReservationRequestTypeDef(TypedDict):
    capacity: int
    offeringId: str
    clientToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class CreateSnapshotCopyConfigurationRequestTypeDef(TypedDict):
    destinationRegion: str
    namespaceName: str
    destinationKmsKeyId: NotRequired[str]
    snapshotRetentionPeriod: NotRequired[int]

class SnapshotCopyConfigurationTypeDef(TypedDict):
    destinationKmsKeyId: NotRequired[str]
    destinationRegion: NotRequired[str]
    namespaceName: NotRequired[str]
    snapshotCopyConfigurationArn: NotRequired[str]
    snapshotCopyConfigurationId: NotRequired[str]
    snapshotRetentionPeriod: NotRequired[int]

class CreateUsageLimitRequestTypeDef(TypedDict):
    amount: int
    resourceArn: str
    usageType: UsageLimitUsageTypeType
    breachAction: NotRequired[UsageLimitBreachActionType]
    period: NotRequired[UsageLimitPeriodType]

class UsageLimitTypeDef(TypedDict):
    amount: NotRequired[int]
    breachAction: NotRequired[UsageLimitBreachActionType]
    period: NotRequired[UsageLimitPeriodType]
    resourceArn: NotRequired[str]
    usageLimitArn: NotRequired[str]
    usageLimitId: NotRequired[str]
    usageType: NotRequired[UsageLimitUsageTypeType]

class PerformanceTargetTypeDef(TypedDict):
    level: NotRequired[int]
    status: NotRequired[PerformanceTargetStatusType]

class DeleteCustomDomainAssociationRequestTypeDef(TypedDict):
    customDomainName: str
    workgroupName: str

class DeleteEndpointAccessRequestTypeDef(TypedDict):
    endpointName: str

class DeleteNamespaceRequestTypeDef(TypedDict):
    namespaceName: str
    finalSnapshotName: NotRequired[str]
    finalSnapshotRetentionPeriod: NotRequired[int]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class DeleteScheduledActionRequestTypeDef(TypedDict):
    scheduledActionName: str

class DeleteSnapshotCopyConfigurationRequestTypeDef(TypedDict):
    snapshotCopyConfigurationId: str

class DeleteSnapshotRequestTypeDef(TypedDict):
    snapshotName: str

class DeleteUsageLimitRequestTypeDef(TypedDict):
    usageLimitId: str

class DeleteWorkgroupRequestTypeDef(TypedDict):
    workgroupName: str

class VpcSecurityGroupMembershipTypeDef(TypedDict):
    status: NotRequired[str]
    vpcSecurityGroupId: NotRequired[str]

class GetCredentialsRequestTypeDef(TypedDict):
    customDomainName: NotRequired[str]
    dbName: NotRequired[str]
    durationSeconds: NotRequired[int]
    workgroupName: NotRequired[str]

class GetCustomDomainAssociationRequestTypeDef(TypedDict):
    customDomainName: str
    workgroupName: str

class GetEndpointAccessRequestTypeDef(TypedDict):
    endpointName: str

class GetNamespaceRequestTypeDef(TypedDict):
    namespaceName: str

class GetRecoveryPointRequestTypeDef(TypedDict):
    recoveryPointId: str

class RecoveryPointTypeDef(TypedDict):
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    recoveryPointCreateTime: NotRequired[datetime]
    recoveryPointId: NotRequired[str]
    totalSizeInMegaBytes: NotRequired[float]
    workgroupName: NotRequired[str]

class GetReservationOfferingRequestTypeDef(TypedDict):
    offeringId: str

class ReservationOfferingTypeDef(TypedDict):
    currencyCode: NotRequired[str]
    duration: NotRequired[int]
    hourlyCharge: NotRequired[float]
    offeringId: NotRequired[str]
    offeringType: NotRequired[OfferingTypeType]
    upfrontCharge: NotRequired[float]

class GetReservationRequestTypeDef(TypedDict):
    reservationId: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class ResourcePolicyTypeDef(TypedDict):
    policy: NotRequired[str]
    resourceArn: NotRequired[str]

class GetScheduledActionRequestTypeDef(TypedDict):
    scheduledActionName: str

class GetSnapshotRequestTypeDef(TypedDict):
    ownerAccount: NotRequired[str]
    snapshotArn: NotRequired[str]
    snapshotName: NotRequired[str]

class GetTableRestoreStatusRequestTypeDef(TypedDict):
    tableRestoreRequestId: str

class TableRestoreStatusTypeDef(TypedDict):
    message: NotRequired[str]
    namespaceName: NotRequired[str]
    newTableName: NotRequired[str]
    progressInMegaBytes: NotRequired[int]
    recoveryPointId: NotRequired[str]
    requestTime: NotRequired[datetime]
    snapshotName: NotRequired[str]
    sourceDatabaseName: NotRequired[str]
    sourceSchemaName: NotRequired[str]
    sourceTableName: NotRequired[str]
    status: NotRequired[str]
    tableRestoreRequestId: NotRequired[str]
    targetDatabaseName: NotRequired[str]
    targetSchemaName: NotRequired[str]
    totalDataInMegaBytes: NotRequired[int]
    workgroupName: NotRequired[str]

class GetTrackRequestTypeDef(TypedDict):
    trackName: str

class GetUsageLimitRequestTypeDef(TypedDict):
    usageLimitId: str

class GetWorkgroupRequestTypeDef(TypedDict):
    workgroupName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCustomDomainAssociationsRequestTypeDef(TypedDict):
    customDomainCertificateArn: NotRequired[str]
    customDomainName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEndpointAccessRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    ownerAccount: NotRequired[str]
    vpcId: NotRequired[str]
    workgroupName: NotRequired[str]

class ListManagedWorkgroupsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sourceArn: NotRequired[str]

class ManagedWorkgroupListItemTypeDef(TypedDict):
    creationDate: NotRequired[datetime]
    managedWorkgroupId: NotRequired[str]
    managedWorkgroupName: NotRequired[str]
    sourceArn: NotRequired[str]
    status: NotRequired[ManagedWorkgroupStatusType]

class ListNamespacesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListReservationOfferingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListReservationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListScheduledActionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    namespaceName: NotRequired[str]
    nextToken: NotRequired[str]

class ScheduledActionAssociationTypeDef(TypedDict):
    namespaceName: NotRequired[str]
    scheduledActionName: NotRequired[str]

class ListSnapshotCopyConfigurationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    namespaceName: NotRequired[str]
    nextToken: NotRequired[str]

class ListTableRestoreStatusRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    namespaceName: NotRequired[str]
    nextToken: NotRequired[str]
    workgroupName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTracksRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListUsageLimitsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resourceArn: NotRequired[str]
    usageType: NotRequired[UsageLimitUsageTypeType]

class ListWorkgroupsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    ownerAccount: NotRequired[str]

class NetworkInterfaceTypeDef(TypedDict):
    availabilityZone: NotRequired[str]
    ipv6Address: NotRequired[str]
    networkInterfaceId: NotRequired[str]
    privateIpAddress: NotRequired[str]
    subnetId: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    policy: str
    resourceArn: str

class RestoreFromRecoveryPointRequestTypeDef(TypedDict):
    namespaceName: str
    recoveryPointId: str
    workgroupName: str

class RestoreFromSnapshotRequestTypeDef(TypedDict):
    namespaceName: str
    workgroupName: str
    adminPasswordSecretKmsKeyId: NotRequired[str]
    manageAdminPassword: NotRequired[bool]
    ownerAccount: NotRequired[str]
    snapshotArn: NotRequired[str]
    snapshotName: NotRequired[str]

class RestoreTableFromRecoveryPointRequestTypeDef(TypedDict):
    namespaceName: str
    newTableName: str
    recoveryPointId: str
    sourceDatabaseName: str
    sourceTableName: str
    workgroupName: str
    activateCaseSensitiveIdentifier: NotRequired[bool]
    sourceSchemaName: NotRequired[str]
    targetDatabaseName: NotRequired[str]
    targetSchemaName: NotRequired[str]

class RestoreTableFromSnapshotRequestTypeDef(TypedDict):
    namespaceName: str
    newTableName: str
    snapshotName: str
    sourceDatabaseName: str
    sourceTableName: str
    workgroupName: str
    activateCaseSensitiveIdentifier: NotRequired[bool]
    sourceSchemaName: NotRequired[str]
    targetDatabaseName: NotRequired[str]
    targetSchemaName: NotRequired[str]

class ScheduleOutputTypeDef(TypedDict):
    at: NotRequired[datetime]
    cron: NotRequired[str]

class UpdateTargetTypeDef(TypedDict):
    trackName: NotRequired[str]
    workgroupVersion: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCustomDomainAssociationRequestTypeDef(TypedDict):
    customDomainCertificateArn: str
    customDomainName: str
    workgroupName: str

class UpdateEndpointAccessRequestTypeDef(TypedDict):
    endpointName: str
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class UpdateNamespaceRequestTypeDef(TypedDict):
    namespaceName: str
    adminPasswordSecretKmsKeyId: NotRequired[str]
    adminUserPassword: NotRequired[str]
    adminUsername: NotRequired[str]
    defaultIamRoleArn: NotRequired[str]
    iamRoles: NotRequired[Sequence[str]]
    kmsKeyId: NotRequired[str]
    logExports: NotRequired[Sequence[LogExportType]]
    manageAdminPassword: NotRequired[bool]

class UpdateSnapshotCopyConfigurationRequestTypeDef(TypedDict):
    snapshotCopyConfigurationId: str
    snapshotRetentionPeriod: NotRequired[int]

class UpdateSnapshotRequestTypeDef(TypedDict):
    snapshotName: str
    retentionPeriod: NotRequired[int]

class UpdateUsageLimitRequestTypeDef(TypedDict):
    usageLimitId: str
    amount: NotRequired[int]
    breachAction: NotRequired[UsageLimitBreachActionType]

class ConvertRecoveryPointToSnapshotRequestTypeDef(TypedDict):
    recoveryPointId: str
    snapshotName: str
    retentionPeriod: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateNamespaceRequestTypeDef(TypedDict):
    namespaceName: str
    adminPasswordSecretKmsKeyId: NotRequired[str]
    adminUserPassword: NotRequired[str]
    adminUsername: NotRequired[str]
    dbName: NotRequired[str]
    defaultIamRoleArn: NotRequired[str]
    iamRoles: NotRequired[Sequence[str]]
    kmsKeyId: NotRequired[str]
    logExports: NotRequired[Sequence[LogExportType]]
    manageAdminPassword: NotRequired[bool]
    redshiftIdcApplicationArn: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotRequestTypeDef(TypedDict):
    namespaceName: str
    snapshotName: str
    retentionPeriod: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotScheduleActionParametersOutputTypeDef(TypedDict):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: NotRequired[int]
    tags: NotRequired[List[TagTypeDef]]

class CreateSnapshotScheduleActionParametersTypeDef(TypedDict):
    namespaceName: str
    snapshotNamePrefix: str
    retentionPeriod: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateCustomDomainAssociationResponseTypeDef(TypedDict):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialsResponseTypeDef(TypedDict):
    dbPassword: str
    dbUser: str
    expiration: datetime
    nextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomDomainAssociationResponseTypeDef(TypedDict):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomDomainAssociationsResponseTypeDef(TypedDict):
    associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomDomainAssociationResponseTypeDef(TypedDict):
    customDomainCertificateArn: str
    customDomainCertificateExpiryTime: datetime
    customDomainName: str
    workgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConvertRecoveryPointToSnapshotResponseTypeDef(TypedDict):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResponseTypeDef(TypedDict):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(TypedDict):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotResponseTypeDef(TypedDict):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSnapshotsResponseTypeDef(TypedDict):
    snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateSnapshotResponseTypeDef(TypedDict):
    snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNamespaceResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamespacesResponseTypeDef(TypedDict):
    namespaces: List[NamespaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RestoreFromRecoveryPointResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    recoveryPointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromSnapshotResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    ownerAccount: str
    snapshotName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNamespaceResponseTypeDef(TypedDict):
    namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsRequestTypeDef(TypedDict):
    endTime: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    nextToken: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]

class ListSnapshotsRequestTypeDef(TypedDict):
    endTime: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    nextToken: NotRequired[str]
    ownerAccount: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]

class ScheduleTypeDef(TypedDict):
    at: NotRequired[TimestampTypeDef]
    cron: NotRequired[str]

class CreateSnapshotCopyConfigurationResponseTypeDef(TypedDict):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotCopyConfigurationResponseTypeDef(TypedDict):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSnapshotCopyConfigurationsResponseTypeDef(TypedDict):
    snapshotCopyConfigurations: List[SnapshotCopyConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateSnapshotCopyConfigurationResponseTypeDef(TypedDict):
    snapshotCopyConfiguration: SnapshotCopyConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageLimitResponseTypeDef(TypedDict):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUsageLimitResponseTypeDef(TypedDict):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUsageLimitResponseTypeDef(TypedDict):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsageLimitsResponseTypeDef(TypedDict):
    usageLimits: List[UsageLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateUsageLimitResponseTypeDef(TypedDict):
    usageLimit: UsageLimitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkgroupRequestTypeDef(TypedDict):
    namespaceName: str
    workgroupName: str
    baseCapacity: NotRequired[int]
    configParameters: NotRequired[Sequence[ConfigParameterTypeDef]]
    enhancedVpcRouting: NotRequired[bool]
    ipAddressType: NotRequired[str]
    maxCapacity: NotRequired[int]
    port: NotRequired[int]
    pricePerformanceTarget: NotRequired[PerformanceTargetTypeDef]
    publiclyAccessible: NotRequired[bool]
    securityGroupIds: NotRequired[Sequence[str]]
    subnetIds: NotRequired[Sequence[str]]
    tags: NotRequired[Sequence[TagTypeDef]]
    trackName: NotRequired[str]

class UpdateWorkgroupRequestTypeDef(TypedDict):
    workgroupName: str
    baseCapacity: NotRequired[int]
    configParameters: NotRequired[Sequence[ConfigParameterTypeDef]]
    enhancedVpcRouting: NotRequired[bool]
    ipAddressType: NotRequired[str]
    maxCapacity: NotRequired[int]
    port: NotRequired[int]
    pricePerformanceTarget: NotRequired[PerformanceTargetTypeDef]
    publiclyAccessible: NotRequired[bool]
    securityGroupIds: NotRequired[Sequence[str]]
    subnetIds: NotRequired[Sequence[str]]
    trackName: NotRequired[str]

class GetRecoveryPointResponseTypeDef(TypedDict):
    recoveryPoint: RecoveryPointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsResponseTypeDef(TypedDict):
    recoveryPoints: List[RecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetReservationOfferingResponseTypeDef(TypedDict):
    reservationOffering: ReservationOfferingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReservationOfferingsResponseTypeDef(TypedDict):
    reservationOfferingsList: List[ReservationOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReservationTypeDef(TypedDict):
    capacity: NotRequired[int]
    endDate: NotRequired[datetime]
    offering: NotRequired[ReservationOfferingTypeDef]
    reservationArn: NotRequired[str]
    reservationId: NotRequired[str]
    startDate: NotRequired[datetime]
    status: NotRequired[str]

class GetResourcePolicyResponseTypeDef(TypedDict):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableRestoreStatusResponseTypeDef(TypedDict):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableRestoreStatusResponseTypeDef(TypedDict):
    tableRestoreStatuses: List[TableRestoreStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RestoreTableFromRecoveryPointResponseTypeDef(TypedDict):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromSnapshotResponseTypeDef(TypedDict):
    tableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomDomainAssociationsRequestPaginateTypeDef(TypedDict):
    customDomainCertificateArn: NotRequired[str]
    customDomainName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEndpointAccessRequestPaginateTypeDef(TypedDict):
    ownerAccount: NotRequired[str]
    vpcId: NotRequired[str]
    workgroupName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedWorkgroupsRequestPaginateTypeDef(TypedDict):
    sourceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNamespacesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecoveryPointsRequestPaginateTypeDef(TypedDict):
    endTime: NotRequired[TimestampTypeDef]
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReservationOfferingsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReservationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListScheduledActionsRequestPaginateTypeDef(TypedDict):
    namespaceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSnapshotCopyConfigurationsRequestPaginateTypeDef(TypedDict):
    namespaceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSnapshotsRequestPaginateTypeDef(TypedDict):
    endTime: NotRequired[TimestampTypeDef]
    namespaceArn: NotRequired[str]
    namespaceName: NotRequired[str]
    ownerAccount: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTableRestoreStatusRequestPaginateTypeDef(TypedDict):
    namespaceName: NotRequired[str]
    workgroupName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTracksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsageLimitsRequestPaginateTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    usageType: NotRequired[UsageLimitUsageTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkgroupsRequestPaginateTypeDef(TypedDict):
    ownerAccount: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedWorkgroupsResponseTypeDef(TypedDict):
    managedWorkgroups: List[ManagedWorkgroupListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListScheduledActionsResponseTypeDef(TypedDict):
    scheduledActions: List[ScheduledActionAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class VpcEndpointTypeDef(TypedDict):
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    vpcEndpointId: NotRequired[str]
    vpcId: NotRequired[str]

class ServerlessTrackTypeDef(TypedDict):
    trackName: NotRequired[str]
    updateTargets: NotRequired[List[UpdateTargetTypeDef]]
    workgroupVersion: NotRequired[str]

class TargetActionOutputTypeDef(TypedDict):
    createSnapshot: NotRequired[CreateSnapshotScheduleActionParametersOutputTypeDef]

class TargetActionTypeDef(TypedDict):
    createSnapshot: NotRequired[CreateSnapshotScheduleActionParametersTypeDef]

ScheduleUnionTypeDef = Union[ScheduleTypeDef, ScheduleOutputTypeDef]

class CreateReservationResponseTypeDef(TypedDict):
    reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservationResponseTypeDef(TypedDict):
    reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReservationsResponseTypeDef(TypedDict):
    reservationsList: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EndpointAccessTypeDef(TypedDict):
    address: NotRequired[str]
    endpointArn: NotRequired[str]
    endpointCreateTime: NotRequired[datetime]
    endpointName: NotRequired[str]
    endpointStatus: NotRequired[str]
    port: NotRequired[int]
    subnetIds: NotRequired[List[str]]
    vpcEndpoint: NotRequired[VpcEndpointTypeDef]
    vpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    workgroupName: NotRequired[str]

class EndpointTypeDef(TypedDict):
    address: NotRequired[str]
    port: NotRequired[int]
    vpcEndpoints: NotRequired[List[VpcEndpointTypeDef]]

class GetTrackResponseTypeDef(TypedDict):
    track: ServerlessTrackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTracksResponseTypeDef(TypedDict):
    tracks: List[ServerlessTrackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ScheduledActionResponseTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    namespaceName: NotRequired[str]
    nextInvocations: NotRequired[List[datetime]]
    roleArn: NotRequired[str]
    schedule: NotRequired[ScheduleOutputTypeDef]
    scheduledActionDescription: NotRequired[str]
    scheduledActionName: NotRequired[str]
    scheduledActionUuid: NotRequired[str]
    startTime: NotRequired[datetime]
    state: NotRequired[StateType]
    targetAction: NotRequired[TargetActionOutputTypeDef]

TargetActionUnionTypeDef = Union[TargetActionTypeDef, TargetActionOutputTypeDef]

class CreateEndpointAccessResponseTypeDef(TypedDict):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEndpointAccessResponseTypeDef(TypedDict):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEndpointAccessResponseTypeDef(TypedDict):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointAccessResponseTypeDef(TypedDict):
    endpoints: List[EndpointAccessTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEndpointAccessResponseTypeDef(TypedDict):
    endpoint: EndpointAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkgroupTypeDef(TypedDict):
    baseCapacity: NotRequired[int]
    configParameters: NotRequired[List[ConfigParameterTypeDef]]
    creationDate: NotRequired[datetime]
    crossAccountVpcs: NotRequired[List[str]]
    customDomainCertificateArn: NotRequired[str]
    customDomainCertificateExpiryTime: NotRequired[datetime]
    customDomainName: NotRequired[str]
    endpoint: NotRequired[EndpointTypeDef]
    enhancedVpcRouting: NotRequired[bool]
    ipAddressType: NotRequired[str]
    maxCapacity: NotRequired[int]
    namespaceName: NotRequired[str]
    patchVersion: NotRequired[str]
    pendingTrackName: NotRequired[str]
    port: NotRequired[int]
    pricePerformanceTarget: NotRequired[PerformanceTargetTypeDef]
    publiclyAccessible: NotRequired[bool]
    securityGroupIds: NotRequired[List[str]]
    status: NotRequired[WorkgroupStatusType]
    subnetIds: NotRequired[List[str]]
    trackName: NotRequired[str]
    workgroupArn: NotRequired[str]
    workgroupId: NotRequired[str]
    workgroupName: NotRequired[str]
    workgroupVersion: NotRequired[str]

class CreateScheduledActionResponseTypeDef(TypedDict):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScheduledActionResponseTypeDef(TypedDict):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetScheduledActionResponseTypeDef(TypedDict):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduledActionResponseTypeDef(TypedDict):
    scheduledAction: ScheduledActionResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledActionRequestTypeDef(TypedDict):
    namespaceName: str
    roleArn: str
    schedule: ScheduleUnionTypeDef
    scheduledActionName: str
    targetAction: TargetActionUnionTypeDef
    enabled: NotRequired[bool]
    endTime: NotRequired[TimestampTypeDef]
    scheduledActionDescription: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]

class UpdateScheduledActionRequestTypeDef(TypedDict):
    scheduledActionName: str
    enabled: NotRequired[bool]
    endTime: NotRequired[TimestampTypeDef]
    roleArn: NotRequired[str]
    schedule: NotRequired[ScheduleUnionTypeDef]
    scheduledActionDescription: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    targetAction: NotRequired[TargetActionUnionTypeDef]

class CreateWorkgroupResponseTypeDef(TypedDict):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkgroupResponseTypeDef(TypedDict):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkgroupResponseTypeDef(TypedDict):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkgroupsResponseTypeDef(TypedDict):
    workgroups: List[WorkgroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateWorkgroupResponseTypeDef(TypedDict):
    workgroup: WorkgroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
