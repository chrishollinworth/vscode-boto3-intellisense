"""
Type annotations for datazone service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datazone.client import DataZoneClient

    session = Session()
    client: DataZoneClient = session.client("datazone")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAssetFiltersPaginator,
    ListAssetRevisionsPaginator,
    ListConnectionsPaginator,
    ListDataProductRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListDomainUnitsForParentPaginator,
    ListEntityOwnersPaginator,
    ListEnvironmentActionsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListJobRunsPaginator,
    ListLineageEventsPaginator,
    ListLineageNodeHistoryPaginator,
    ListMetadataGenerationRunsPaginator,
    ListNotificationsPaginator,
    ListPolicyGrantsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectProfilesPaginator,
    ListProjectsPaginator,
    ListRulesPaginator,
    ListSubscriptionGrantsPaginator,
    ListSubscriptionRequestsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionTargetsPaginator,
    ListTimeSeriesDataPointsPaginator,
    SearchGroupProfilesPaginator,
    SearchListingsPaginator,
    SearchPaginator,
    SearchTypesPaginator,
    SearchUserProfilesPaginator,
)
from .type_defs import (
    AcceptPredictionsInputTypeDef,
    AcceptPredictionsOutputTypeDef,
    AcceptSubscriptionRequestInputTypeDef,
    AcceptSubscriptionRequestOutputTypeDef,
    AddEntityOwnerInputTypeDef,
    AddPolicyGrantInputTypeDef,
    AssociateEnvironmentRoleInputTypeDef,
    CancelMetadataGenerationRunInputTypeDef,
    CancelSubscriptionInputTypeDef,
    CancelSubscriptionOutputTypeDef,
    CreateAssetFilterInputTypeDef,
    CreateAssetFilterOutputTypeDef,
    CreateAssetInputTypeDef,
    CreateAssetOutputTypeDef,
    CreateAssetRevisionInputTypeDef,
    CreateAssetRevisionOutputTypeDef,
    CreateAssetTypeInputTypeDef,
    CreateAssetTypeOutputTypeDef,
    CreateConnectionInputTypeDef,
    CreateConnectionOutputTypeDef,
    CreateDataProductInputTypeDef,
    CreateDataProductOutputTypeDef,
    CreateDataProductRevisionInputTypeDef,
    CreateDataProductRevisionOutputTypeDef,
    CreateDataSourceInputTypeDef,
    CreateDataSourceOutputTypeDef,
    CreateDomainInputTypeDef,
    CreateDomainOutputTypeDef,
    CreateDomainUnitInputTypeDef,
    CreateDomainUnitOutputTypeDef,
    CreateEnvironmentActionInputTypeDef,
    CreateEnvironmentActionOutputTypeDef,
    CreateEnvironmentInputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentProfileInputTypeDef,
    CreateEnvironmentProfileOutputTypeDef,
    CreateFormTypeInputTypeDef,
    CreateFormTypeOutputTypeDef,
    CreateGlossaryInputTypeDef,
    CreateGlossaryOutputTypeDef,
    CreateGlossaryTermInputTypeDef,
    CreateGlossaryTermOutputTypeDef,
    CreateGroupProfileInputTypeDef,
    CreateGroupProfileOutputTypeDef,
    CreateListingChangeSetInputTypeDef,
    CreateListingChangeSetOutputTypeDef,
    CreateProjectInputTypeDef,
    CreateProjectMembershipInputTypeDef,
    CreateProjectOutputTypeDef,
    CreateProjectProfileInputTypeDef,
    CreateProjectProfileOutputTypeDef,
    CreateRuleInputTypeDef,
    CreateRuleOutputTypeDef,
    CreateSubscriptionGrantInputTypeDef,
    CreateSubscriptionGrantOutputTypeDef,
    CreateSubscriptionRequestInputTypeDef,
    CreateSubscriptionRequestOutputTypeDef,
    CreateSubscriptionTargetInputTypeDef,
    CreateSubscriptionTargetOutputTypeDef,
    CreateUserProfileInputTypeDef,
    CreateUserProfileOutputTypeDef,
    DeleteAssetFilterInputTypeDef,
    DeleteAssetInputTypeDef,
    DeleteAssetTypeInputTypeDef,
    DeleteConnectionInputTypeDef,
    DeleteConnectionOutputTypeDef,
    DeleteDataProductInputTypeDef,
    DeleteDataSourceInputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteDomainInputTypeDef,
    DeleteDomainOutputTypeDef,
    DeleteDomainUnitInputTypeDef,
    DeleteEnvironmentActionInputTypeDef,
    DeleteEnvironmentBlueprintConfigurationInputTypeDef,
    DeleteEnvironmentInputTypeDef,
    DeleteEnvironmentProfileInputTypeDef,
    DeleteFormTypeInputTypeDef,
    DeleteGlossaryInputTypeDef,
    DeleteGlossaryTermInputTypeDef,
    DeleteListingInputTypeDef,
    DeleteProjectInputTypeDef,
    DeleteProjectMembershipInputTypeDef,
    DeleteProjectProfileInputTypeDef,
    DeleteRuleInputTypeDef,
    DeleteSubscriptionGrantInputTypeDef,
    DeleteSubscriptionGrantOutputTypeDef,
    DeleteSubscriptionRequestInputTypeDef,
    DeleteSubscriptionTargetInputTypeDef,
    DeleteTimeSeriesDataPointsInputTypeDef,
    DisassociateEnvironmentRoleInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAssetFilterInputTypeDef,
    GetAssetFilterOutputTypeDef,
    GetAssetInputTypeDef,
    GetAssetOutputTypeDef,
    GetAssetTypeInputTypeDef,
    GetAssetTypeOutputTypeDef,
    GetConnectionInputTypeDef,
    GetConnectionOutputTypeDef,
    GetDataProductInputTypeDef,
    GetDataProductOutputTypeDef,
    GetDataSourceInputTypeDef,
    GetDataSourceOutputTypeDef,
    GetDataSourceRunInputTypeDef,
    GetDataSourceRunOutputTypeDef,
    GetDomainInputTypeDef,
    GetDomainOutputTypeDef,
    GetDomainUnitInputTypeDef,
    GetDomainUnitOutputTypeDef,
    GetEnvironmentActionInputTypeDef,
    GetEnvironmentActionOutputTypeDef,
    GetEnvironmentBlueprintConfigurationInputTypeDef,
    GetEnvironmentBlueprintConfigurationOutputTypeDef,
    GetEnvironmentBlueprintInputTypeDef,
    GetEnvironmentBlueprintOutputTypeDef,
    GetEnvironmentCredentialsInputTypeDef,
    GetEnvironmentCredentialsOutputTypeDef,
    GetEnvironmentInputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentProfileInputTypeDef,
    GetEnvironmentProfileOutputTypeDef,
    GetFormTypeInputTypeDef,
    GetFormTypeOutputTypeDef,
    GetGlossaryInputTypeDef,
    GetGlossaryOutputTypeDef,
    GetGlossaryTermInputTypeDef,
    GetGlossaryTermOutputTypeDef,
    GetGroupProfileInputTypeDef,
    GetGroupProfileOutputTypeDef,
    GetIamPortalLoginUrlInputTypeDef,
    GetIamPortalLoginUrlOutputTypeDef,
    GetJobRunInputTypeDef,
    GetJobRunOutputTypeDef,
    GetLineageEventInputTypeDef,
    GetLineageEventOutputTypeDef,
    GetLineageNodeInputTypeDef,
    GetLineageNodeOutputTypeDef,
    GetListingInputTypeDef,
    GetListingOutputTypeDef,
    GetMetadataGenerationRunInputTypeDef,
    GetMetadataGenerationRunOutputTypeDef,
    GetProjectInputTypeDef,
    GetProjectOutputTypeDef,
    GetProjectProfileInputTypeDef,
    GetProjectProfileOutputTypeDef,
    GetRuleInputTypeDef,
    GetRuleOutputTypeDef,
    GetSubscriptionGrantInputTypeDef,
    GetSubscriptionGrantOutputTypeDef,
    GetSubscriptionInputTypeDef,
    GetSubscriptionOutputTypeDef,
    GetSubscriptionRequestDetailsInputTypeDef,
    GetSubscriptionRequestDetailsOutputTypeDef,
    GetSubscriptionTargetInputTypeDef,
    GetSubscriptionTargetOutputTypeDef,
    GetTimeSeriesDataPointInputTypeDef,
    GetTimeSeriesDataPointOutputTypeDef,
    GetUserProfileInputTypeDef,
    GetUserProfileOutputTypeDef,
    ListAssetFiltersInputTypeDef,
    ListAssetFiltersOutputTypeDef,
    ListAssetRevisionsInputTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListConnectionsInputTypeDef,
    ListConnectionsOutputTypeDef,
    ListDataProductRevisionsInputTypeDef,
    ListDataProductRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesInputTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsInputTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesInputTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsInputTypeDef,
    ListDomainsOutputTypeDef,
    ListDomainUnitsForParentInputTypeDef,
    ListDomainUnitsForParentOutputTypeDef,
    ListEntityOwnersInputTypeDef,
    ListEntityOwnersOutputTypeDef,
    ListEnvironmentActionsInputTypeDef,
    ListEnvironmentActionsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsInputTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsInputTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesInputTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsInputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListJobRunsInputTypeDef,
    ListJobRunsOutputTypeDef,
    ListLineageEventsInputTypeDef,
    ListLineageEventsOutputTypeDef,
    ListLineageNodeHistoryInputTypeDef,
    ListLineageNodeHistoryOutputTypeDef,
    ListMetadataGenerationRunsInputTypeDef,
    ListMetadataGenerationRunsOutputTypeDef,
    ListNotificationsInputTypeDef,
    ListNotificationsOutputTypeDef,
    ListPolicyGrantsInputTypeDef,
    ListPolicyGrantsOutputTypeDef,
    ListProjectMembershipsInputTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectProfilesInputTypeDef,
    ListProjectProfilesOutputTypeDef,
    ListProjectsInputTypeDef,
    ListProjectsOutputTypeDef,
    ListRulesInputTypeDef,
    ListRulesOutputTypeDef,
    ListSubscriptionGrantsInputTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsInputTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsInputTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsInputTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTimeSeriesDataPointsInputTypeDef,
    ListTimeSeriesDataPointsOutputTypeDef,
    PostLineageEventInputTypeDef,
    PostLineageEventOutputTypeDef,
    PostTimeSeriesDataPointsInputTypeDef,
    PostTimeSeriesDataPointsOutputTypeDef,
    PutEnvironmentBlueprintConfigurationInputTypeDef,
    PutEnvironmentBlueprintConfigurationOutputTypeDef,
    RejectPredictionsInputTypeDef,
    RejectPredictionsOutputTypeDef,
    RejectSubscriptionRequestInputTypeDef,
    RejectSubscriptionRequestOutputTypeDef,
    RemoveEntityOwnerInputTypeDef,
    RemovePolicyGrantInputTypeDef,
    RevokeSubscriptionInputTypeDef,
    RevokeSubscriptionOutputTypeDef,
    SearchGroupProfilesInputTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInputTypeDef,
    SearchListingsInputTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchTypesInputTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesInputTypeDef,
    SearchUserProfilesOutputTypeDef,
    StartDataSourceRunInputTypeDef,
    StartDataSourceRunOutputTypeDef,
    StartMetadataGenerationRunInputTypeDef,
    StartMetadataGenerationRunOutputTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAssetFilterInputTypeDef,
    UpdateAssetFilterOutputTypeDef,
    UpdateConnectionInputTypeDef,
    UpdateConnectionOutputTypeDef,
    UpdateDataSourceInputTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateDomainInputTypeDef,
    UpdateDomainOutputTypeDef,
    UpdateDomainUnitInputTypeDef,
    UpdateDomainUnitOutputTypeDef,
    UpdateEnvironmentActionInputTypeDef,
    UpdateEnvironmentActionOutputTypeDef,
    UpdateEnvironmentInputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentProfileInputTypeDef,
    UpdateEnvironmentProfileOutputTypeDef,
    UpdateGlossaryInputTypeDef,
    UpdateGlossaryOutputTypeDef,
    UpdateGlossaryTermInputTypeDef,
    UpdateGlossaryTermOutputTypeDef,
    UpdateGroupProfileInputTypeDef,
    UpdateGroupProfileOutputTypeDef,
    UpdateProjectInputTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateProjectProfileInputTypeDef,
    UpdateProjectProfileOutputTypeDef,
    UpdateRuleInputTypeDef,
    UpdateRuleOutputTypeDef,
    UpdateSubscriptionGrantStatusInputTypeDef,
    UpdateSubscriptionGrantStatusOutputTypeDef,
    UpdateSubscriptionRequestInputTypeDef,
    UpdateSubscriptionRequestOutputTypeDef,
    UpdateSubscriptionTargetInputTypeDef,
    UpdateSubscriptionTargetOutputTypeDef,
    UpdateUserProfileInputTypeDef,
    UpdateUserProfileOutputTypeDef,
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

__all__ = ("DataZoneClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DataZoneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataZoneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#generate_presigned_url)
        """

    def accept_predictions(
        self, **kwargs: Unpack[AcceptPredictionsInputTypeDef]
    ) -> AcceptPredictionsOutputTypeDef:
        """
        Accepts automatically generated business-friendly metadata for your Amazon
        DataZone assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/accept_predictions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_predictions)
        """

    def accept_subscription_request(
        self, **kwargs: Unpack[AcceptSubscriptionRequestInputTypeDef]
    ) -> AcceptSubscriptionRequestOutputTypeDef:
        """
        Accepts a subscription request to a specific asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/accept_subscription_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_subscription_request)
        """

    def add_entity_owner(self, **kwargs: Unpack[AddEntityOwnerInputTypeDef]) -> Dict[str, Any]:
        """
        Adds the owner of an entity (a domain unit).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/add_entity_owner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#add_entity_owner)
        """

    def add_policy_grant(self, **kwargs: Unpack[AddPolicyGrantInputTypeDef]) -> Dict[str, Any]:
        """
        Adds a policy grant (an authorization policy) to a specified entity, including
        domain units, environment blueprint configurations, or environment profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/add_policy_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#add_policy_grant)
        """

    def associate_environment_role(
        self, **kwargs: Unpack[AssociateEnvironmentRoleInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the environment role in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/associate_environment_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#associate_environment_role)
        """

    def cancel_metadata_generation_run(
        self, **kwargs: Unpack[CancelMetadataGenerationRunInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the metadata generation run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/cancel_metadata_generation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#cancel_metadata_generation_run)
        """

    def cancel_subscription(
        self, **kwargs: Unpack[CancelSubscriptionInputTypeDef]
    ) -> CancelSubscriptionOutputTypeDef:
        """
        Cancels the subscription to the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/cancel_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#cancel_subscription)
        """

    def create_asset(self, **kwargs: Unpack[CreateAssetInputTypeDef]) -> CreateAssetOutputTypeDef:
        """
        Creates an asset in Amazon DataZone catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset)
        """

    def create_asset_filter(
        self, **kwargs: Unpack[CreateAssetFilterInputTypeDef]
    ) -> CreateAssetFilterOutputTypeDef:
        """
        Creates a data asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_asset_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_filter)
        """

    def create_asset_revision(
        self, **kwargs: Unpack[CreateAssetRevisionInputTypeDef]
    ) -> CreateAssetRevisionOutputTypeDef:
        """
        Creates a revision of the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_asset_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_revision)
        """

    def create_asset_type(
        self, **kwargs: Unpack[CreateAssetTypeInputTypeDef]
    ) -> CreateAssetTypeOutputTypeDef:
        """
        Creates a custom asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_asset_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_type)
        """

    def create_connection(
        self, **kwargs: Unpack[CreateConnectionInputTypeDef]
    ) -> CreateConnectionOutputTypeDef:
        """
        Creates a new connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_connection)
        """

    def create_data_product(
        self, **kwargs: Unpack[CreateDataProductInputTypeDef]
    ) -> CreateDataProductOutputTypeDef:
        """
        Creates a data product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_data_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_product)
        """

    def create_data_product_revision(
        self, **kwargs: Unpack[CreateDataProductRevisionInputTypeDef]
    ) -> CreateDataProductRevisionOutputTypeDef:
        """
        Creates a data product revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_data_product_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_product_revision)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceInputTypeDef]
    ) -> CreateDataSourceOutputTypeDef:
        """
        Creates an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_source)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainInputTypeDef]
    ) -> CreateDomainOutputTypeDef:
        """
        Creates an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_domain)
        """

    def create_domain_unit(
        self, **kwargs: Unpack[CreateDomainUnitInputTypeDef]
    ) -> CreateDomainUnitOutputTypeDef:
        """
        Creates a domain unit in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_domain_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_domain_unit)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentInputTypeDef]
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Create an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment)
        """

    def create_environment_action(
        self, **kwargs: Unpack[CreateEnvironmentActionInputTypeDef]
    ) -> CreateEnvironmentActionOutputTypeDef:
        """
        Creates an action for the environment, for example, creates a console link for
        an analytics tool that is available in this environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_environment_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment_action)
        """

    def create_environment_profile(
        self, **kwargs: Unpack[CreateEnvironmentProfileInputTypeDef]
    ) -> CreateEnvironmentProfileOutputTypeDef:
        """
        Creates an Amazon DataZone environment profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_environment_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment_profile)
        """

    def create_form_type(
        self, **kwargs: Unpack[CreateFormTypeInputTypeDef]
    ) -> CreateFormTypeOutputTypeDef:
        """
        Creates a metadata form type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_form_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_form_type)
        """

    def create_glossary(
        self, **kwargs: Unpack[CreateGlossaryInputTypeDef]
    ) -> CreateGlossaryOutputTypeDef:
        """
        Creates an Amazon DataZone business glossary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_glossary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary)
        """

    def create_glossary_term(
        self, **kwargs: Unpack[CreateGlossaryTermInputTypeDef]
    ) -> CreateGlossaryTermOutputTypeDef:
        """
        Creates a business glossary term.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_glossary_term.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary_term)
        """

    def create_group_profile(
        self, **kwargs: Unpack[CreateGroupProfileInputTypeDef]
    ) -> CreateGroupProfileOutputTypeDef:
        """
        Creates a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_group_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_group_profile)
        """

    def create_listing_change_set(
        self, **kwargs: Unpack[CreateListingChangeSetInputTypeDef]
    ) -> CreateListingChangeSetOutputTypeDef:
        """
        Publishes a listing (a record of an asset at a given time) or removes a listing
        from the catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_listing_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_listing_change_set)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectInputTypeDef]
    ) -> CreateProjectOutputTypeDef:
        """
        Creates an Amazon DataZone project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project)
        """

    def create_project_membership(
        self, **kwargs: Unpack[CreateProjectMembershipInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_project_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project_membership)
        """

    def create_project_profile(
        self, **kwargs: Unpack[CreateProjectProfileInputTypeDef]
    ) -> CreateProjectProfileOutputTypeDef:
        """
        Creates a project profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_project_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project_profile)
        """

    def create_rule(self, **kwargs: Unpack[CreateRuleInputTypeDef]) -> CreateRuleOutputTypeDef:
        """
        Creates a rule in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_rule)
        """

    def create_subscription_grant(
        self, **kwargs: Unpack[CreateSubscriptionGrantInputTypeDef]
    ) -> CreateSubscriptionGrantOutputTypeDef:
        """
        Creates a subsscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_subscription_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_grant)
        """

    def create_subscription_request(
        self, **kwargs: Unpack[CreateSubscriptionRequestInputTypeDef]
    ) -> CreateSubscriptionRequestOutputTypeDef:
        """
        Creates a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_subscription_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_request)
        """

    def create_subscription_target(
        self, **kwargs: Unpack[CreateSubscriptionTargetInputTypeDef]
    ) -> CreateSubscriptionTargetOutputTypeDef:
        """
        Creates a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_subscription_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_target)
        """

    def create_user_profile(
        self, **kwargs: Unpack[CreateUserProfileInputTypeDef]
    ) -> CreateUserProfileOutputTypeDef:
        """
        Creates a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/create_user_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_user_profile)
        """

    def delete_asset(self, **kwargs: Unpack[DeleteAssetInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes an asset in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset)
        """

    def delete_asset_filter(
        self, **kwargs: Unpack[DeleteAssetFilterInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_asset_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset_filter)
        """

    def delete_asset_type(self, **kwargs: Unpack[DeleteAssetTypeInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes an asset type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_asset_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset_type)
        """

    def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionInputTypeDef]
    ) -> DeleteConnectionOutputTypeDef:
        """
        Deletes and connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_connection)
        """

    def delete_data_product(
        self, **kwargs: Unpack[DeleteDataProductInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a data product in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_data_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_data_product)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceInputTypeDef]
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Deletes a data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_data_source)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainInputTypeDef]
    ) -> DeleteDomainOutputTypeDef:
        """
        Deletes a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_domain)
        """

    def delete_domain_unit(self, **kwargs: Unpack[DeleteDomainUnitInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_domain_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_domain_unit)
        """

    def delete_environment(
        self, **kwargs: Unpack[DeleteEnvironmentInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment)
        """

    def delete_environment_action(
        self, **kwargs: Unpack[DeleteEnvironmentActionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an action for the environment, for example, deletes a console link for
        an analytics tool that is available in this environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_environment_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_action)
        """

    def delete_environment_blueprint_configuration(
        self, **kwargs: Unpack[DeleteEnvironmentBlueprintConfigurationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_environment_blueprint_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_blueprint_configuration)
        """

    def delete_environment_profile(
        self, **kwargs: Unpack[DeleteEnvironmentProfileInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_environment_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_profile)
        """

    def delete_form_type(self, **kwargs: Unpack[DeleteFormTypeInputTypeDef]) -> Dict[str, Any]:
        """
        Delets and metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_form_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_form_type)
        """

    def delete_glossary(self, **kwargs: Unpack[DeleteGlossaryInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_glossary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary)
        """

    def delete_glossary_term(
        self, **kwargs: Unpack[DeleteGlossaryTermInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_glossary_term.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary_term)
        """

    def delete_listing(self, **kwargs: Unpack[DeleteListingInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a listing (a record of an asset at a given time).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_listing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_listing)
        """

    def delete_project(self, **kwargs: Unpack[DeleteProjectInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project)
        """

    def delete_project_membership(
        self, **kwargs: Unpack[DeleteProjectMembershipInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_project_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project_membership)
        """

    def delete_project_profile(
        self, **kwargs: Unpack[DeleteProjectProfileInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a project profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_project_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project_profile)
        """

    def delete_rule(self, **kwargs: Unpack[DeleteRuleInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a rule in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_rule)
        """

    def delete_subscription_grant(
        self, **kwargs: Unpack[DeleteSubscriptionGrantInputTypeDef]
    ) -> DeleteSubscriptionGrantOutputTypeDef:
        """
        Deletes and subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_subscription_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_grant)
        """

    def delete_subscription_request(
        self, **kwargs: Unpack[DeleteSubscriptionRequestInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_subscription_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_request)
        """

    def delete_subscription_target(
        self, **kwargs: Unpack[DeleteSubscriptionTargetInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_subscription_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_target)
        """

    def delete_time_series_data_points(
        self, **kwargs: Unpack[DeleteTimeSeriesDataPointsInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified time series form for the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/delete_time_series_data_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_time_series_data_points)
        """

    def disassociate_environment_role(
        self, **kwargs: Unpack[DisassociateEnvironmentRoleInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the environment role in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/disassociate_environment_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#disassociate_environment_role)
        """

    def get_asset(self, **kwargs: Unpack[GetAssetInputTypeDef]) -> GetAssetOutputTypeDef:
        """
        Gets an Amazon DataZone asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset)
        """

    def get_asset_filter(
        self, **kwargs: Unpack[GetAssetFilterInputTypeDef]
    ) -> GetAssetFilterOutputTypeDef:
        """
        Gets an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_asset_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset_filter)
        """

    def get_asset_type(
        self, **kwargs: Unpack[GetAssetTypeInputTypeDef]
    ) -> GetAssetTypeOutputTypeDef:
        """
        Gets an Amazon DataZone asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_asset_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset_type)
        """

    def get_connection(
        self, **kwargs: Unpack[GetConnectionInputTypeDef]
    ) -> GetConnectionOutputTypeDef:
        """
        Gets a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_connection)
        """

    def get_data_product(
        self, **kwargs: Unpack[GetDataProductInputTypeDef]
    ) -> GetDataProductOutputTypeDef:
        """
        Gets the data product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_data_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_product)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceInputTypeDef]
    ) -> GetDataSourceOutputTypeDef:
        """
        Gets an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source)
        """

    def get_data_source_run(
        self, **kwargs: Unpack[GetDataSourceRunInputTypeDef]
    ) -> GetDataSourceRunOutputTypeDef:
        """
        Gets an Amazon DataZone data source run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_data_source_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source_run)
        """

    def get_domain(self, **kwargs: Unpack[GetDomainInputTypeDef]) -> GetDomainOutputTypeDef:
        """
        Gets an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_domain)
        """

    def get_domain_unit(
        self, **kwargs: Unpack[GetDomainUnitInputTypeDef]
    ) -> GetDomainUnitOutputTypeDef:
        """
        Gets the details of the specified domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_domain_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_domain_unit)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentInputTypeDef]
    ) -> GetEnvironmentOutputTypeDef:
        """
        Gets an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment)
        """

    def get_environment_action(
        self, **kwargs: Unpack[GetEnvironmentActionInputTypeDef]
    ) -> GetEnvironmentActionOutputTypeDef:
        """
        Gets the specified environment action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_action)
        """

    def get_environment_blueprint(
        self, **kwargs: Unpack[GetEnvironmentBlueprintInputTypeDef]
    ) -> GetEnvironmentBlueprintOutputTypeDef:
        """
        Gets an Amazon DataZone blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint)
        """

    def get_environment_blueprint_configuration(
        self, **kwargs: Unpack[GetEnvironmentBlueprintConfigurationInputTypeDef]
    ) -> GetEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Gets the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment_blueprint_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint_configuration)
        """

    def get_environment_credentials(
        self, **kwargs: Unpack[GetEnvironmentCredentialsInputTypeDef]
    ) -> GetEnvironmentCredentialsOutputTypeDef:
        """
        Gets the credentials of an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_credentials)
        """

    def get_environment_profile(
        self, **kwargs: Unpack[GetEnvironmentProfileInputTypeDef]
    ) -> GetEnvironmentProfileOutputTypeDef:
        """
        Gets an evinronment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_environment_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_profile)
        """

    def get_form_type(self, **kwargs: Unpack[GetFormTypeInputTypeDef]) -> GetFormTypeOutputTypeDef:
        """
        Gets a metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_form_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_form_type)
        """

    def get_glossary(self, **kwargs: Unpack[GetGlossaryInputTypeDef]) -> GetGlossaryOutputTypeDef:
        """
        Gets a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_glossary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary)
        """

    def get_glossary_term(
        self, **kwargs: Unpack[GetGlossaryTermInputTypeDef]
    ) -> GetGlossaryTermOutputTypeDef:
        """
        Gets a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_glossary_term.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary_term)
        """

    def get_group_profile(
        self, **kwargs: Unpack[GetGroupProfileInputTypeDef]
    ) -> GetGroupProfileOutputTypeDef:
        """
        Gets a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_group_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_group_profile)
        """

    def get_iam_portal_login_url(
        self, **kwargs: Unpack[GetIamPortalLoginUrlInputTypeDef]
    ) -> GetIamPortalLoginUrlOutputTypeDef:
        """
        Gets the data portal URL for the specified Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_iam_portal_login_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_iam_portal_login_url)
        """

    def get_job_run(self, **kwargs: Unpack[GetJobRunInputTypeDef]) -> GetJobRunOutputTypeDef:
        """
        The details of the job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_job_run)
        """

    def get_lineage_event(
        self, **kwargs: Unpack[GetLineageEventInputTypeDef]
    ) -> GetLineageEventOutputTypeDef:
        """
        Describes the lineage event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_lineage_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_lineage_event)
        """

    def get_lineage_node(
        self, **kwargs: Unpack[GetLineageNodeInputTypeDef]
    ) -> GetLineageNodeOutputTypeDef:
        """
        Gets the data lineage node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_lineage_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_lineage_node)
        """

    def get_listing(self, **kwargs: Unpack[GetListingInputTypeDef]) -> GetListingOutputTypeDef:
        """
        Gets a listing (a record of an asset at a given time).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_listing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_listing)
        """

    def get_metadata_generation_run(
        self, **kwargs: Unpack[GetMetadataGenerationRunInputTypeDef]
    ) -> GetMetadataGenerationRunOutputTypeDef:
        """
        Gets a metadata generation run in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_metadata_generation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_metadata_generation_run)
        """

    def get_project(self, **kwargs: Unpack[GetProjectInputTypeDef]) -> GetProjectOutputTypeDef:
        """
        Gets a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_project)
        """

    def get_project_profile(
        self, **kwargs: Unpack[GetProjectProfileInputTypeDef]
    ) -> GetProjectProfileOutputTypeDef:
        """
        The details of the project profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_project_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_project_profile)
        """

    def get_rule(self, **kwargs: Unpack[GetRuleInputTypeDef]) -> GetRuleOutputTypeDef:
        """
        Gets the details of a rule in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_rule)
        """

    def get_subscription(
        self, **kwargs: Unpack[GetSubscriptionInputTypeDef]
    ) -> GetSubscriptionOutputTypeDef:
        """
        Gets a subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription)
        """

    def get_subscription_grant(
        self, **kwargs: Unpack[GetSubscriptionGrantInputTypeDef]
    ) -> GetSubscriptionGrantOutputTypeDef:
        """
        Gets the subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_subscription_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_grant)
        """

    def get_subscription_request_details(
        self, **kwargs: Unpack[GetSubscriptionRequestDetailsInputTypeDef]
    ) -> GetSubscriptionRequestDetailsOutputTypeDef:
        """
        Gets the details of the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_subscription_request_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_request_details)
        """

    def get_subscription_target(
        self, **kwargs: Unpack[GetSubscriptionTargetInputTypeDef]
    ) -> GetSubscriptionTargetOutputTypeDef:
        """
        Gets the subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_subscription_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_target)
        """

    def get_time_series_data_point(
        self, **kwargs: Unpack[GetTimeSeriesDataPointInputTypeDef]
    ) -> GetTimeSeriesDataPointOutputTypeDef:
        """
        Gets the existing data point for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_time_series_data_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_time_series_data_point)
        """

    def get_user_profile(
        self, **kwargs: Unpack[GetUserProfileInputTypeDef]
    ) -> GetUserProfileOutputTypeDef:
        """
        Gets a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_user_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_user_profile)
        """

    def list_asset_filters(
        self, **kwargs: Unpack[ListAssetFiltersInputTypeDef]
    ) -> ListAssetFiltersOutputTypeDef:
        """
        Lists asset filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_asset_filters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_asset_filters)
        """

    def list_asset_revisions(
        self, **kwargs: Unpack[ListAssetRevisionsInputTypeDef]
    ) -> ListAssetRevisionsOutputTypeDef:
        """
        Lists the revisions for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_asset_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_asset_revisions)
        """

    def list_connections(
        self, **kwargs: Unpack[ListConnectionsInputTypeDef]
    ) -> ListConnectionsOutputTypeDef:
        """
        Lists connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_connections)
        """

    def list_data_product_revisions(
        self, **kwargs: Unpack[ListDataProductRevisionsInputTypeDef]
    ) -> ListDataProductRevisionsOutputTypeDef:
        """
        Lists data product revisions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_data_product_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_product_revisions)
        """

    def list_data_source_run_activities(
        self, **kwargs: Unpack[ListDataSourceRunActivitiesInputTypeDef]
    ) -> ListDataSourceRunActivitiesOutputTypeDef:
        """
        Lists data source run activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_data_source_run_activities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_run_activities)
        """

    def list_data_source_runs(
        self, **kwargs: Unpack[ListDataSourceRunsInputTypeDef]
    ) -> ListDataSourceRunsOutputTypeDef:
        """
        Lists data source runs in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_data_source_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_runs)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesInputTypeDef]
    ) -> ListDataSourcesOutputTypeDef:
        """
        Lists data sources in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_data_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_sources)
        """

    def list_domain_units_for_parent(
        self, **kwargs: Unpack[ListDomainUnitsForParentInputTypeDef]
    ) -> ListDomainUnitsForParentOutputTypeDef:
        """
        Lists child domain units for the specified parent domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_domain_units_for_parent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_domain_units_for_parent)
        """

    def list_domains(self, **kwargs: Unpack[ListDomainsInputTypeDef]) -> ListDomainsOutputTypeDef:
        """
        Lists Amazon DataZone domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_domains)
        """

    def list_entity_owners(
        self, **kwargs: Unpack[ListEntityOwnersInputTypeDef]
    ) -> ListEntityOwnersOutputTypeDef:
        """
        Lists the entity (domain units) owners.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_entity_owners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_entity_owners)
        """

    def list_environment_actions(
        self, **kwargs: Unpack[ListEnvironmentActionsInputTypeDef]
    ) -> ListEnvironmentActionsOutputTypeDef:
        """
        Lists existing environment actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_environment_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_actions)
        """

    def list_environment_blueprint_configurations(
        self, **kwargs: Unpack[ListEnvironmentBlueprintConfigurationsInputTypeDef]
    ) -> ListEnvironmentBlueprintConfigurationsOutputTypeDef:
        """
        Lists blueprint configurations for a Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_environment_blueprint_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprint_configurations)
        """

    def list_environment_blueprints(
        self, **kwargs: Unpack[ListEnvironmentBlueprintsInputTypeDef]
    ) -> ListEnvironmentBlueprintsOutputTypeDef:
        """
        Lists blueprints in an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_environment_blueprints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprints)
        """

    def list_environment_profiles(
        self, **kwargs: Unpack[ListEnvironmentProfilesInputTypeDef]
    ) -> ListEnvironmentProfilesOutputTypeDef:
        """
        Lists Amazon DataZone environment profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_environment_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_profiles)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsInputTypeDef]
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists Amazon DataZone environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environments)
        """

    def list_job_runs(self, **kwargs: Unpack[ListJobRunsInputTypeDef]) -> ListJobRunsOutputTypeDef:
        """
        Lists job runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_job_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_job_runs)
        """

    def list_lineage_events(
        self, **kwargs: Unpack[ListLineageEventsInputTypeDef]
    ) -> ListLineageEventsOutputTypeDef:
        """
        Lists lineage events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_lineage_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_lineage_events)
        """

    def list_lineage_node_history(
        self, **kwargs: Unpack[ListLineageNodeHistoryInputTypeDef]
    ) -> ListLineageNodeHistoryOutputTypeDef:
        """
        Lists the history of the specified data lineage node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_lineage_node_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_lineage_node_history)
        """

    def list_metadata_generation_runs(
        self, **kwargs: Unpack[ListMetadataGenerationRunsInputTypeDef]
    ) -> ListMetadataGenerationRunsOutputTypeDef:
        """
        Lists all metadata generation runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_metadata_generation_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_metadata_generation_runs)
        """

    def list_notifications(
        self, **kwargs: Unpack[ListNotificationsInputTypeDef]
    ) -> ListNotificationsOutputTypeDef:
        """
        Lists all Amazon DataZone notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_notifications)
        """

    def list_policy_grants(
        self, **kwargs: Unpack[ListPolicyGrantsInputTypeDef]
    ) -> ListPolicyGrantsOutputTypeDef:
        """
        Lists policy grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_policy_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_policy_grants)
        """

    def list_project_memberships(
        self, **kwargs: Unpack[ListProjectMembershipsInputTypeDef]
    ) -> ListProjectMembershipsOutputTypeDef:
        """
        Lists all members of the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_project_memberships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_project_memberships)
        """

    def list_project_profiles(
        self, **kwargs: Unpack[ListProjectProfilesInputTypeDef]
    ) -> ListProjectProfilesOutputTypeDef:
        """
        Lists project profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_project_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_project_profiles)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsInputTypeDef]
    ) -> ListProjectsOutputTypeDef:
        """
        Lists Amazon DataZone projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_projects)
        """

    def list_rules(self, **kwargs: Unpack[ListRulesInputTypeDef]) -> ListRulesOutputTypeDef:
        """
        Lists existing rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_rules)
        """

    def list_subscription_grants(
        self, **kwargs: Unpack[ListSubscriptionGrantsInputTypeDef]
    ) -> ListSubscriptionGrantsOutputTypeDef:
        """
        Lists subscription grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_subscription_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_grants)
        """

    def list_subscription_requests(
        self, **kwargs: Unpack[ListSubscriptionRequestsInputTypeDef]
    ) -> ListSubscriptionRequestsOutputTypeDef:
        """
        Lists Amazon DataZone subscription requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_subscription_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_requests)
        """

    def list_subscription_targets(
        self, **kwargs: Unpack[ListSubscriptionTargetsInputTypeDef]
    ) -> ListSubscriptionTargetsOutputTypeDef:
        """
        Lists subscription targets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_subscription_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_targets)
        """

    def list_subscriptions(
        self, **kwargs: Unpack[ListSubscriptionsInputTypeDef]
    ) -> ListSubscriptionsOutputTypeDef:
        """
        Lists subscriptions in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscriptions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for the specified resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_tags_for_resource)
        """

    def list_time_series_data_points(
        self, **kwargs: Unpack[ListTimeSeriesDataPointsInputTypeDef]
    ) -> ListTimeSeriesDataPointsOutputTypeDef:
        """
        Lists time series data points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/list_time_series_data_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_time_series_data_points)
        """

    def post_lineage_event(
        self, **kwargs: Unpack[PostLineageEventInputTypeDef]
    ) -> PostLineageEventOutputTypeDef:
        """
        Posts a data lineage event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/post_lineage_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#post_lineage_event)
        """

    def post_time_series_data_points(
        self, **kwargs: Unpack[PostTimeSeriesDataPointsInputTypeDef]
    ) -> PostTimeSeriesDataPointsOutputTypeDef:
        """
        Posts time series data points to Amazon DataZone for the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/post_time_series_data_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#post_time_series_data_points)
        """

    def put_environment_blueprint_configuration(
        self, **kwargs: Unpack[PutEnvironmentBlueprintConfigurationInputTypeDef]
    ) -> PutEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Writes the configuration for the specified environment blueprint in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/put_environment_blueprint_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#put_environment_blueprint_configuration)
        """

    def reject_predictions(
        self, **kwargs: Unpack[RejectPredictionsInputTypeDef]
    ) -> RejectPredictionsOutputTypeDef:
        """
        Rejects automatically generated business-friendly metadata for your Amazon
        DataZone assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/reject_predictions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_predictions)
        """

    def reject_subscription_request(
        self, **kwargs: Unpack[RejectSubscriptionRequestInputTypeDef]
    ) -> RejectSubscriptionRequestOutputTypeDef:
        """
        Rejects the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/reject_subscription_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_subscription_request)
        """

    def remove_entity_owner(
        self, **kwargs: Unpack[RemoveEntityOwnerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes an owner from an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/remove_entity_owner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#remove_entity_owner)
        """

    def remove_policy_grant(
        self, **kwargs: Unpack[RemovePolicyGrantInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a policy grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/remove_policy_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#remove_policy_grant)
        """

    def revoke_subscription(
        self, **kwargs: Unpack[RevokeSubscriptionInputTypeDef]
    ) -> RevokeSubscriptionOutputTypeDef:
        """
        Revokes a specified subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/revoke_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#revoke_subscription)
        """

    def search(self, **kwargs: Unpack[SearchInputTypeDef]) -> SearchOutputTypeDef:
        """
        Searches for assets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/search.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search)
        """

    def search_group_profiles(
        self, **kwargs: Unpack[SearchGroupProfilesInputTypeDef]
    ) -> SearchGroupProfilesOutputTypeDef:
        """
        Searches group profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/search_group_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_group_profiles)
        """

    def search_listings(
        self, **kwargs: Unpack[SearchListingsInputTypeDef]
    ) -> SearchListingsOutputTypeDef:
        """
        Searches listings (records of an asset at a given time) in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/search_listings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_listings)
        """

    def search_types(self, **kwargs: Unpack[SearchTypesInputTypeDef]) -> SearchTypesOutputTypeDef:
        """
        Searches for types in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/search_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_types)
        """

    def search_user_profiles(
        self, **kwargs: Unpack[SearchUserProfilesInputTypeDef]
    ) -> SearchUserProfilesOutputTypeDef:
        """
        Searches user profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/search_user_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_user_profiles)
        """

    def start_data_source_run(
        self, **kwargs: Unpack[StartDataSourceRunInputTypeDef]
    ) -> StartDataSourceRunOutputTypeDef:
        """
        Start the run of the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/start_data_source_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#start_data_source_run)
        """

    def start_metadata_generation_run(
        self, **kwargs: Unpack[StartMetadataGenerationRunInputTypeDef]
    ) -> StartMetadataGenerationRunOutputTypeDef:
        """
        Starts the metadata generation run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/start_metadata_generation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#start_metadata_generation_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Untags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#untag_resource)
        """

    def update_asset_filter(
        self, **kwargs: Unpack[UpdateAssetFilterInputTypeDef]
    ) -> UpdateAssetFilterOutputTypeDef:
        """
        Updates an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_asset_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_asset_filter)
        """

    def update_connection(
        self, **kwargs: Unpack[UpdateConnectionInputTypeDef]
    ) -> UpdateConnectionOutputTypeDef:
        """
        Updates a connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_connection)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceInputTypeDef]
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_data_source)
        """

    def update_domain(
        self, **kwargs: Unpack[UpdateDomainInputTypeDef]
    ) -> UpdateDomainOutputTypeDef:
        """
        Updates a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_domain)
        """

    def update_domain_unit(
        self, **kwargs: Unpack[UpdateDomainUnitInputTypeDef]
    ) -> UpdateDomainUnitOutputTypeDef:
        """
        Updates the domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_domain_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_domain_unit)
        """

    def update_environment(
        self, **kwargs: Unpack[UpdateEnvironmentInputTypeDef]
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates the specified environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment)
        """

    def update_environment_action(
        self, **kwargs: Unpack[UpdateEnvironmentActionInputTypeDef]
    ) -> UpdateEnvironmentActionOutputTypeDef:
        """
        Updates an environment action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_environment_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment_action)
        """

    def update_environment_profile(
        self, **kwargs: Unpack[UpdateEnvironmentProfileInputTypeDef]
    ) -> UpdateEnvironmentProfileOutputTypeDef:
        """
        Updates the specified environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_environment_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment_profile)
        """

    def update_glossary(
        self, **kwargs: Unpack[UpdateGlossaryInputTypeDef]
    ) -> UpdateGlossaryOutputTypeDef:
        """
        Updates the business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_glossary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary)
        """

    def update_glossary_term(
        self, **kwargs: Unpack[UpdateGlossaryTermInputTypeDef]
    ) -> UpdateGlossaryTermOutputTypeDef:
        """
        Updates a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_glossary_term.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary_term)
        """

    def update_group_profile(
        self, **kwargs: Unpack[UpdateGroupProfileInputTypeDef]
    ) -> UpdateGroupProfileOutputTypeDef:
        """
        Updates the specified group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_group_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_group_profile)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectInputTypeDef]
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates the specified project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_project)
        """

    def update_project_profile(
        self, **kwargs: Unpack[UpdateProjectProfileInputTypeDef]
    ) -> UpdateProjectProfileOutputTypeDef:
        """
        Updates a project profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_project_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_project_profile)
        """

    def update_rule(self, **kwargs: Unpack[UpdateRuleInputTypeDef]) -> UpdateRuleOutputTypeDef:
        """
        Updates a rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_rule)
        """

    def update_subscription_grant_status(
        self, **kwargs: Unpack[UpdateSubscriptionGrantStatusInputTypeDef]
    ) -> UpdateSubscriptionGrantStatusOutputTypeDef:
        """
        Updates the status of the specified subscription grant status in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_subscription_grant_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_grant_status)
        """

    def update_subscription_request(
        self, **kwargs: Unpack[UpdateSubscriptionRequestInputTypeDef]
    ) -> UpdateSubscriptionRequestOutputTypeDef:
        """
        Updates a specified subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_subscription_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_request)
        """

    def update_subscription_target(
        self, **kwargs: Unpack[UpdateSubscriptionTargetInputTypeDef]
    ) -> UpdateSubscriptionTargetOutputTypeDef:
        """
        Updates the specified subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_subscription_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_target)
        """

    def update_user_profile(
        self, **kwargs: Unpack[UpdateUserProfileInputTypeDef]
    ) -> UpdateUserProfileOutputTypeDef:
        """
        Updates the specified user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/update_user_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_user_profile)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_filters"]
    ) -> ListAssetFiltersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_revisions"]
    ) -> ListAssetRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connections"]
    ) -> ListConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_product_revisions"]
    ) -> ListDataProductRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_source_run_activities"]
    ) -> ListDataSourceRunActivitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_source_runs"]
    ) -> ListDataSourceRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domain_units_for_parent"]
    ) -> ListDomainUnitsForParentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entity_owners"]
    ) -> ListEntityOwnersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environment_actions"]
    ) -> ListEnvironmentActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environment_blueprint_configurations"]
    ) -> ListEnvironmentBlueprintConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environment_blueprints"]
    ) -> ListEnvironmentBlueprintsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environment_profiles"]
    ) -> ListEnvironmentProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_runs"]
    ) -> ListJobRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lineage_events"]
    ) -> ListLineageEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_lineage_node_history"]
    ) -> ListLineageNodeHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metadata_generation_runs"]
    ) -> ListMetadataGenerationRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_notifications"]
    ) -> ListNotificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_grants"]
    ) -> ListPolicyGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_project_memberships"]
    ) -> ListProjectMembershipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_project_profiles"]
    ) -> ListProjectProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscription_grants"]
    ) -> ListSubscriptionGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscription_requests"]
    ) -> ListSubscriptionRequestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscription_targets"]
    ) -> ListSubscriptionTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_time_series_data_points"]
    ) -> ListTimeSeriesDataPointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_group_profiles"]
    ) -> SearchGroupProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_listings"]
    ) -> SearchListingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search"]
    ) -> SearchPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_types"]
    ) -> SearchTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_user_profiles"]
    ) -> SearchUserProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """
