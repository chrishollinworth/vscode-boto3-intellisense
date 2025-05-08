"""
Type annotations for redshift-serverless service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_redshift_serverless.client import RedshiftServerlessClient

    session = Session()
    client: RedshiftServerlessClient = session.client("redshift-serverless")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCustomDomainAssociationsPaginator,
    ListEndpointAccessPaginator,
    ListManagedWorkgroupsPaginator,
    ListNamespacesPaginator,
    ListRecoveryPointsPaginator,
    ListReservationOfferingsPaginator,
    ListReservationsPaginator,
    ListScheduledActionsPaginator,
    ListSnapshotCopyConfigurationsPaginator,
    ListSnapshotsPaginator,
    ListTableRestoreStatusPaginator,
    ListTracksPaginator,
    ListUsageLimitsPaginator,
    ListWorkgroupsPaginator,
)
from .type_defs import (
    ConvertRecoveryPointToSnapshotRequestTypeDef,
    ConvertRecoveryPointToSnapshotResponseTypeDef,
    CreateCustomDomainAssociationRequestTypeDef,
    CreateCustomDomainAssociationResponseTypeDef,
    CreateEndpointAccessRequestTypeDef,
    CreateEndpointAccessResponseTypeDef,
    CreateNamespaceRequestTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateReservationRequestTypeDef,
    CreateReservationResponseTypeDef,
    CreateScheduledActionRequestTypeDef,
    CreateScheduledActionResponseTypeDef,
    CreateSnapshotCopyConfigurationRequestTypeDef,
    CreateSnapshotCopyConfigurationResponseTypeDef,
    CreateSnapshotRequestTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateUsageLimitRequestTypeDef,
    CreateUsageLimitResponseTypeDef,
    CreateWorkgroupRequestTypeDef,
    CreateWorkgroupResponseTypeDef,
    DeleteCustomDomainAssociationRequestTypeDef,
    DeleteEndpointAccessRequestTypeDef,
    DeleteEndpointAccessResponseTypeDef,
    DeleteNamespaceRequestTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteScheduledActionRequestTypeDef,
    DeleteScheduledActionResponseTypeDef,
    DeleteSnapshotCopyConfigurationRequestTypeDef,
    DeleteSnapshotCopyConfigurationResponseTypeDef,
    DeleteSnapshotRequestTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteUsageLimitRequestTypeDef,
    DeleteUsageLimitResponseTypeDef,
    DeleteWorkgroupRequestTypeDef,
    DeleteWorkgroupResponseTypeDef,
    GetCredentialsRequestTypeDef,
    GetCredentialsResponseTypeDef,
    GetCustomDomainAssociationRequestTypeDef,
    GetCustomDomainAssociationResponseTypeDef,
    GetEndpointAccessRequestTypeDef,
    GetEndpointAccessResponseTypeDef,
    GetNamespaceRequestTypeDef,
    GetNamespaceResponseTypeDef,
    GetRecoveryPointRequestTypeDef,
    GetRecoveryPointResponseTypeDef,
    GetReservationOfferingRequestTypeDef,
    GetReservationOfferingResponseTypeDef,
    GetReservationRequestTypeDef,
    GetReservationResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetScheduledActionRequestTypeDef,
    GetScheduledActionResponseTypeDef,
    GetSnapshotRequestTypeDef,
    GetSnapshotResponseTypeDef,
    GetTableRestoreStatusRequestTypeDef,
    GetTableRestoreStatusResponseTypeDef,
    GetTrackRequestTypeDef,
    GetTrackResponseTypeDef,
    GetUsageLimitRequestTypeDef,
    GetUsageLimitResponseTypeDef,
    GetWorkgroupRequestTypeDef,
    GetWorkgroupResponseTypeDef,
    ListCustomDomainAssociationsRequestTypeDef,
    ListCustomDomainAssociationsResponseTypeDef,
    ListEndpointAccessRequestTypeDef,
    ListEndpointAccessResponseTypeDef,
    ListManagedWorkgroupsRequestTypeDef,
    ListManagedWorkgroupsResponseTypeDef,
    ListNamespacesRequestTypeDef,
    ListNamespacesResponseTypeDef,
    ListRecoveryPointsRequestTypeDef,
    ListRecoveryPointsResponseTypeDef,
    ListReservationOfferingsRequestTypeDef,
    ListReservationOfferingsResponseTypeDef,
    ListReservationsRequestTypeDef,
    ListReservationsResponseTypeDef,
    ListScheduledActionsRequestTypeDef,
    ListScheduledActionsResponseTypeDef,
    ListSnapshotCopyConfigurationsRequestTypeDef,
    ListSnapshotCopyConfigurationsResponseTypeDef,
    ListSnapshotsRequestTypeDef,
    ListSnapshotsResponseTypeDef,
    ListTableRestoreStatusRequestTypeDef,
    ListTableRestoreStatusResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTracksRequestTypeDef,
    ListTracksResponseTypeDef,
    ListUsageLimitsRequestTypeDef,
    ListUsageLimitsResponseTypeDef,
    ListWorkgroupsRequestTypeDef,
    ListWorkgroupsResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RestoreFromRecoveryPointRequestTypeDef,
    RestoreFromRecoveryPointResponseTypeDef,
    RestoreFromSnapshotRequestTypeDef,
    RestoreFromSnapshotResponseTypeDef,
    RestoreTableFromRecoveryPointRequestTypeDef,
    RestoreTableFromRecoveryPointResponseTypeDef,
    RestoreTableFromSnapshotRequestTypeDef,
    RestoreTableFromSnapshotResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCustomDomainAssociationRequestTypeDef,
    UpdateCustomDomainAssociationResponseTypeDef,
    UpdateEndpointAccessRequestTypeDef,
    UpdateEndpointAccessResponseTypeDef,
    UpdateNamespaceRequestTypeDef,
    UpdateNamespaceResponseTypeDef,
    UpdateScheduledActionRequestTypeDef,
    UpdateScheduledActionResponseTypeDef,
    UpdateSnapshotCopyConfigurationRequestTypeDef,
    UpdateSnapshotCopyConfigurationResponseTypeDef,
    UpdateSnapshotRequestTypeDef,
    UpdateSnapshotResponseTypeDef,
    UpdateUsageLimitRequestTypeDef,
    UpdateUsageLimitResponseTypeDef,
    UpdateWorkgroupRequestTypeDef,
    UpdateWorkgroupResponseTypeDef,
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

__all__ = ("RedshiftServerlessClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidPaginationException: Type[BotocoreClientError]
    Ipv6CidrBlockNotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RedshiftServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftServerlessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#generate_presigned_url)
        """

    def convert_recovery_point_to_snapshot(
        self, **kwargs: Unpack[ConvertRecoveryPointToSnapshotRequestTypeDef]
    ) -> ConvertRecoveryPointToSnapshotResponseTypeDef:
        """
        Converts a recovery point to a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/convert_recovery_point_to_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#convert_recovery_point_to_snapshot)
        """

    def create_custom_domain_association(
        self, **kwargs: Unpack[CreateCustomDomainAssociationRequestTypeDef]
    ) -> CreateCustomDomainAssociationResponseTypeDef:
        """
        Creates a custom domain association for Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_custom_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_custom_domain_association)
        """

    def create_endpoint_access(
        self, **kwargs: Unpack[CreateEndpointAccessRequestTypeDef]
    ) -> CreateEndpointAccessResponseTypeDef:
        """
        Creates an Amazon Redshift Serverless managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_endpoint_access)
        """

    def create_namespace(
        self, **kwargs: Unpack[CreateNamespaceRequestTypeDef]
    ) -> CreateNamespaceResponseTypeDef:
        """
        Creates a namespace in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_namespace)
        """

    def create_reservation(
        self, **kwargs: Unpack[CreateReservationRequestTypeDef]
    ) -> CreateReservationResponseTypeDef:
        """
        Creates an Amazon Redshift Serverless reservation, which gives you the option
        to commit to a specified number of Redshift Processing Units (RPUs) for a year
        at a discount from Serverless on-demand (OD) rates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_reservation)
        """

    def create_scheduled_action(
        self, **kwargs: Unpack[CreateScheduledActionRequestTypeDef]
    ) -> CreateScheduledActionResponseTypeDef:
        """
        Creates a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_scheduled_action)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestTypeDef]
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a snapshot of all databases in a namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_snapshot)
        """

    def create_snapshot_copy_configuration(
        self, **kwargs: Unpack[CreateSnapshotCopyConfigurationRequestTypeDef]
    ) -> CreateSnapshotCopyConfigurationResponseTypeDef:
        """
        Creates a snapshot copy configuration that lets you copy snapshots to another
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_snapshot_copy_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_snapshot_copy_configuration)
        """

    def create_usage_limit(
        self, **kwargs: Unpack[CreateUsageLimitRequestTypeDef]
    ) -> CreateUsageLimitResponseTypeDef:
        """
        Creates a usage limit for a specified Amazon Redshift Serverless usage type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_usage_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_usage_limit)
        """

    def create_workgroup(
        self, **kwargs: Unpack[CreateWorkgroupRequestTypeDef]
    ) -> CreateWorkgroupResponseTypeDef:
        """
        Creates an workgroup in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/create_workgroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#create_workgroup)
        """

    def delete_custom_domain_association(
        self, **kwargs: Unpack[DeleteCustomDomainAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom domain association for Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_custom_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_custom_domain_association)
        """

    def delete_endpoint_access(
        self, **kwargs: Unpack[DeleteEndpointAccessRequestTypeDef]
    ) -> DeleteEndpointAccessResponseTypeDef:
        """
        Deletes an Amazon Redshift Serverless managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_endpoint_access)
        """

    def delete_namespace(
        self, **kwargs: Unpack[DeleteNamespaceRequestTypeDef]
    ) -> DeleteNamespaceResponseTypeDef:
        """
        Deletes a namespace from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_namespace)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_resource_policy)
        """

    def delete_scheduled_action(
        self, **kwargs: Unpack[DeleteScheduledActionRequestTypeDef]
    ) -> DeleteScheduledActionResponseTypeDef:
        """
        Deletes a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_scheduled_action)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestTypeDef]
    ) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes a snapshot from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_snapshot)
        """

    def delete_snapshot_copy_configuration(
        self, **kwargs: Unpack[DeleteSnapshotCopyConfigurationRequestTypeDef]
    ) -> DeleteSnapshotCopyConfigurationResponseTypeDef:
        """
        Deletes a snapshot copy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_snapshot_copy_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_snapshot_copy_configuration)
        """

    def delete_usage_limit(
        self, **kwargs: Unpack[DeleteUsageLimitRequestTypeDef]
    ) -> DeleteUsageLimitResponseTypeDef:
        """
        Deletes a usage limit from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_usage_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_usage_limit)
        """

    def delete_workgroup(
        self, **kwargs: Unpack[DeleteWorkgroupRequestTypeDef]
    ) -> DeleteWorkgroupResponseTypeDef:
        """
        Deletes a workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/delete_workgroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#delete_workgroup)
        """

    def get_credentials(
        self, **kwargs: Unpack[GetCredentialsRequestTypeDef]
    ) -> GetCredentialsResponseTypeDef:
        """
        Returns a database user name and temporary password with temporary
        authorization to log in to Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_credentials)
        """

    def get_custom_domain_association(
        self, **kwargs: Unpack[GetCustomDomainAssociationRequestTypeDef]
    ) -> GetCustomDomainAssociationResponseTypeDef:
        """
        Gets information about a specific custom domain association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_custom_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_custom_domain_association)
        """

    def get_endpoint_access(
        self, **kwargs: Unpack[GetEndpointAccessRequestTypeDef]
    ) -> GetEndpointAccessResponseTypeDef:
        """
        Returns information, such as the name, about a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_endpoint_access)
        """

    def get_namespace(
        self, **kwargs: Unpack[GetNamespaceRequestTypeDef]
    ) -> GetNamespaceResponseTypeDef:
        """
        Returns information about a namespace in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_namespace)
        """

    def get_recovery_point(
        self, **kwargs: Unpack[GetRecoveryPointRequestTypeDef]
    ) -> GetRecoveryPointResponseTypeDef:
        """
        Returns information about a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_recovery_point)
        """

    def get_reservation(
        self, **kwargs: Unpack[GetReservationRequestTypeDef]
    ) -> GetReservationResponseTypeDef:
        """
        Gets an Amazon Redshift Serverless reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_reservation)
        """

    def get_reservation_offering(
        self, **kwargs: Unpack[GetReservationOfferingRequestTypeDef]
    ) -> GetReservationOfferingResponseTypeDef:
        """
        Returns the reservation offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_reservation_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_reservation_offering)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Returns a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_resource_policy)
        """

    def get_scheduled_action(
        self, **kwargs: Unpack[GetScheduledActionRequestTypeDef]
    ) -> GetScheduledActionResponseTypeDef:
        """
        Returns information about a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_scheduled_action)
        """

    def get_snapshot(
        self, **kwargs: Unpack[GetSnapshotRequestTypeDef]
    ) -> GetSnapshotResponseTypeDef:
        """
        Returns information about a specific snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_snapshot)
        """

    def get_table_restore_status(
        self, **kwargs: Unpack[GetTableRestoreStatusRequestTypeDef]
    ) -> GetTableRestoreStatusResponseTypeDef:
        """
        Returns information about a <code>TableRestoreStatus</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_table_restore_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_table_restore_status)
        """

    def get_track(self, **kwargs: Unpack[GetTrackRequestTypeDef]) -> GetTrackResponseTypeDef:
        """
        Get the Redshift Serverless version for a specified track.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_track.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_track)
        """

    def get_usage_limit(
        self, **kwargs: Unpack[GetUsageLimitRequestTypeDef]
    ) -> GetUsageLimitResponseTypeDef:
        """
        Returns information about a usage limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_usage_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_usage_limit)
        """

    def get_workgroup(
        self, **kwargs: Unpack[GetWorkgroupRequestTypeDef]
    ) -> GetWorkgroupResponseTypeDef:
        """
        Returns information about a specific workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_workgroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_workgroup)
        """

    def list_custom_domain_associations(
        self, **kwargs: Unpack[ListCustomDomainAssociationsRequestTypeDef]
    ) -> ListCustomDomainAssociationsResponseTypeDef:
        """
        Lists custom domain associations for Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_custom_domain_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_custom_domain_associations)
        """

    def list_endpoint_access(
        self, **kwargs: Unpack[ListEndpointAccessRequestTypeDef]
    ) -> ListEndpointAccessResponseTypeDef:
        """
        Returns an array of <code>EndpointAccess</code> objects and relevant
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_endpoint_access)
        """

    def list_managed_workgroups(
        self, **kwargs: Unpack[ListManagedWorkgroupsRequestTypeDef]
    ) -> ListManagedWorkgroupsResponseTypeDef:
        """
        Returns information about a list of specified managed workgroups in your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_managed_workgroups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_managed_workgroups)
        """

    def list_namespaces(
        self, **kwargs: Unpack[ListNamespacesRequestTypeDef]
    ) -> ListNamespacesResponseTypeDef:
        """
        Returns information about a list of specified namespaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_namespaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_namespaces)
        """

    def list_recovery_points(
        self, **kwargs: Unpack[ListRecoveryPointsRequestTypeDef]
    ) -> ListRecoveryPointsResponseTypeDef:
        """
        Returns an array of recovery points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_recovery_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_recovery_points)
        """

    def list_reservation_offerings(
        self, **kwargs: Unpack[ListReservationOfferingsRequestTypeDef]
    ) -> ListReservationOfferingsResponseTypeDef:
        """
        Returns the current reservation offerings in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_reservation_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_reservation_offerings)
        """

    def list_reservations(
        self, **kwargs: Unpack[ListReservationsRequestTypeDef]
    ) -> ListReservationsResponseTypeDef:
        """
        Returns a list of Reservation objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_reservations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_reservations)
        """

    def list_scheduled_actions(
        self, **kwargs: Unpack[ListScheduledActionsRequestTypeDef]
    ) -> ListScheduledActionsResponseTypeDef:
        """
        Returns a list of scheduled actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_scheduled_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_scheduled_actions)
        """

    def list_snapshot_copy_configurations(
        self, **kwargs: Unpack[ListSnapshotCopyConfigurationsRequestTypeDef]
    ) -> ListSnapshotCopyConfigurationsResponseTypeDef:
        """
        Returns a list of snapshot copy configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_snapshot_copy_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_snapshot_copy_configurations)
        """

    def list_snapshots(
        self, **kwargs: Unpack[ListSnapshotsRequestTypeDef]
    ) -> ListSnapshotsResponseTypeDef:
        """
        Returns a list of snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_snapshots)
        """

    def list_table_restore_status(
        self, **kwargs: Unpack[ListTableRestoreStatusRequestTypeDef]
    ) -> ListTableRestoreStatusResponseTypeDef:
        """
        Returns information about an array of <code>TableRestoreStatus</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_table_restore_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_table_restore_status)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_tags_for_resource)
        """

    def list_tracks(self, **kwargs: Unpack[ListTracksRequestTypeDef]) -> ListTracksResponseTypeDef:
        """
        List the Amazon Redshift Serverless versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_tracks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_tracks)
        """

    def list_usage_limits(
        self, **kwargs: Unpack[ListUsageLimitsRequestTypeDef]
    ) -> ListUsageLimitsResponseTypeDef:
        """
        Lists all usage limits within Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_usage_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_usage_limits)
        """

    def list_workgroups(
        self, **kwargs: Unpack[ListWorkgroupsRequestTypeDef]
    ) -> ListWorkgroupsResponseTypeDef:
        """
        Returns information about a list of specified workgroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/list_workgroups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#list_workgroups)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#put_resource_policy)
        """

    def restore_from_recovery_point(
        self, **kwargs: Unpack[RestoreFromRecoveryPointRequestTypeDef]
    ) -> RestoreFromRecoveryPointResponseTypeDef:
        """
        Restore the data from a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/restore_from_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#restore_from_recovery_point)
        """

    def restore_from_snapshot(
        self, **kwargs: Unpack[RestoreFromSnapshotRequestTypeDef]
    ) -> RestoreFromSnapshotResponseTypeDef:
        """
        Restores a namespace from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/restore_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#restore_from_snapshot)
        """

    def restore_table_from_recovery_point(
        self, **kwargs: Unpack[RestoreTableFromRecoveryPointRequestTypeDef]
    ) -> RestoreTableFromRecoveryPointResponseTypeDef:
        """
        Restores a table from a recovery point to your Amazon Redshift Serverless
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/restore_table_from_recovery_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#restore_table_from_recovery_point)
        """

    def restore_table_from_snapshot(
        self, **kwargs: Unpack[RestoreTableFromSnapshotRequestTypeDef]
    ) -> RestoreTableFromSnapshotResponseTypeDef:
        """
        Restores a table from a snapshot to your Amazon Redshift Serverless instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/restore_table_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#restore_table_from_snapshot)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or set of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#untag_resource)
        """

    def update_custom_domain_association(
        self, **kwargs: Unpack[UpdateCustomDomainAssociationRequestTypeDef]
    ) -> UpdateCustomDomainAssociationResponseTypeDef:
        """
        Updates an Amazon Redshift Serverless certificate associated with a custom
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_custom_domain_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_custom_domain_association)
        """

    def update_endpoint_access(
        self, **kwargs: Unpack[UpdateEndpointAccessRequestTypeDef]
    ) -> UpdateEndpointAccessResponseTypeDef:
        """
        Updates an Amazon Redshift Serverless managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_endpoint_access)
        """

    def update_namespace(
        self, **kwargs: Unpack[UpdateNamespaceRequestTypeDef]
    ) -> UpdateNamespaceResponseTypeDef:
        """
        Updates a namespace with the specified settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_namespace)
        """

    def update_scheduled_action(
        self, **kwargs: Unpack[UpdateScheduledActionRequestTypeDef]
    ) -> UpdateScheduledActionResponseTypeDef:
        """
        Updates a scheduled action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_scheduled_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_scheduled_action)
        """

    def update_snapshot(
        self, **kwargs: Unpack[UpdateSnapshotRequestTypeDef]
    ) -> UpdateSnapshotResponseTypeDef:
        """
        Updates a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_snapshot)
        """

    def update_snapshot_copy_configuration(
        self, **kwargs: Unpack[UpdateSnapshotCopyConfigurationRequestTypeDef]
    ) -> UpdateSnapshotCopyConfigurationResponseTypeDef:
        """
        Updates a snapshot copy configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_snapshot_copy_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_snapshot_copy_configuration)
        """

    def update_usage_limit(
        self, **kwargs: Unpack[UpdateUsageLimitRequestTypeDef]
    ) -> UpdateUsageLimitResponseTypeDef:
        """
        Update a usage limit in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_usage_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_usage_limit)
        """

    def update_workgroup(
        self, **kwargs: Unpack[UpdateWorkgroupRequestTypeDef]
    ) -> UpdateWorkgroupResponseTypeDef:
        """
        Updates a workgroup with the specified configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/update_workgroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#update_workgroup)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_domain_associations"]
    ) -> ListCustomDomainAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_endpoint_access"]
    ) -> ListEndpointAccessPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_workgroups"]
    ) -> ListManagedWorkgroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_namespaces"]
    ) -> ListNamespacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recovery_points"]
    ) -> ListRecoveryPointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reservation_offerings"]
    ) -> ListReservationOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scheduled_actions"]
    ) -> ListScheduledActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_snapshot_copy_configurations"]
    ) -> ListSnapshotCopyConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_snapshots"]
    ) -> ListSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_table_restore_status"]
    ) -> ListTableRestoreStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tracks"]
    ) -> ListTracksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_usage_limits"]
    ) -> ListUsageLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workgroups"]
    ) -> ListWorkgroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client/#get_paginator)
        """
