"""
Type annotations for datazone service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_datazone import DataZoneClient

    client: DataZoneClient = boto3.client("datazone")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ChangeActionType,
    DataAssetActivityStatusType,
    DataSourceRunStatusType,
    DataSourceStatusType,
    DomainStatusType,
    EnableSettingType,
    EnvironmentStatusType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    NotificationTypeType,
    SortKeyType,
    SortOrderType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TaskStatusType,
    TypesSearchScopeType,
    UserDesignationType,
    UserProfileStatusType,
    UserProfileTypeType,
    UserSearchTypeType,
    UserTypeType,
)
from .paginator import (
    ListAssetRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListNotificationsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectsPaginator,
    ListSubscriptionGrantsPaginator,
    ListSubscriptionRequestsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionTargetsPaginator,
    SearchGroupProfilesPaginator,
    SearchListingsPaginator,
    SearchPaginator,
    SearchTypesPaginator,
    SearchUserProfilesPaginator,
)
from .type_defs import (
    AcceptChoiceTypeDef,
    AcceptPredictionsOutputTypeDef,
    AcceptRuleTypeDef,
    AcceptSubscriptionRequestOutputTypeDef,
    AssetTargetNameMapTypeDef,
    CancelSubscriptionOutputTypeDef,
    CreateAssetOutputTypeDef,
    CreateAssetRevisionOutputTypeDef,
    CreateAssetTypeOutputTypeDef,
    CreateDataSourceOutputTypeDef,
    CreateDomainOutputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentProfileOutputTypeDef,
    CreateFormTypeOutputTypeDef,
    CreateGlossaryOutputTypeDef,
    CreateGlossaryTermOutputTypeDef,
    CreateGroupProfileOutputTypeDef,
    CreateListingChangeSetOutputTypeDef,
    CreateProjectOutputTypeDef,
    CreateSubscriptionGrantOutputTypeDef,
    CreateSubscriptionRequestOutputTypeDef,
    CreateSubscriptionTargetOutputTypeDef,
    CreateUserProfileOutputTypeDef,
    DataSourceConfigurationInputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteDomainOutputTypeDef,
    DeleteSubscriptionGrantOutputTypeDef,
    EnvironmentParameterTypeDef,
    FailureCauseTypeDef,
    FilterClauseTypeDef,
    FormEntryInputTypeDef,
    FormInputTypeDef,
    GetAssetOutputTypeDef,
    GetAssetTypeOutputTypeDef,
    GetDataSourceOutputTypeDef,
    GetDataSourceRunOutputTypeDef,
    GetDomainOutputTypeDef,
    GetEnvironmentBlueprintConfigurationOutputTypeDef,
    GetEnvironmentBlueprintOutputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentProfileOutputTypeDef,
    GetFormTypeOutputTypeDef,
    GetGlossaryOutputTypeDef,
    GetGlossaryTermOutputTypeDef,
    GetGroupProfileOutputTypeDef,
    GetIamPortalLoginUrlOutputTypeDef,
    GetListingOutputTypeDef,
    GetProjectOutputTypeDef,
    GetSubscriptionGrantOutputTypeDef,
    GetSubscriptionOutputTypeDef,
    GetSubscriptionRequestDetailsOutputTypeDef,
    GetSubscriptionTargetOutputTypeDef,
    GetUserProfileOutputTypeDef,
    GrantedEntityInputTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    MemberTypeDef,
    ModelTypeDef,
    PredictionConfigurationTypeDef,
    PutEnvironmentBlueprintConfigurationOutputTypeDef,
    RecommendationConfigurationTypeDef,
    RejectChoiceTypeDef,
    RejectPredictionsOutputTypeDef,
    RejectRuleTypeDef,
    RejectSubscriptionRequestOutputTypeDef,
    RevokeSubscriptionOutputTypeDef,
    ScheduleConfigurationTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInItemTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchSortTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesOutputTypeDef,
    SingleSignOnTypeDef,
    StartDataSourceRunOutputTypeDef,
    SubscribedListingInputTypeDef,
    SubscribedPrincipalInputTypeDef,
    SubscriptionTargetFormTypeDef,
    TermRelationsTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateDomainOutputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentProfileOutputTypeDef,
    UpdateGlossaryOutputTypeDef,
    UpdateGlossaryTermOutputTypeDef,
    UpdateGroupProfileOutputTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSubscriptionGrantStatusOutputTypeDef,
    UpdateSubscriptionRequestOutputTypeDef,
    UpdateSubscriptionTargetOutputTypeDef,
    UpdateUserProfileOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataZoneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataZoneClient exceptions.
        """
    def accept_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        acceptChoices: List["AcceptChoiceTypeDef"] = None,
        acceptRule: "AcceptRuleTypeDef" = None,
        clientToken: str = None,
        revision: str = None
    ) -> AcceptPredictionsOutputTypeDef:
        """
        Accepts automatically generated business-friendly metadata for your Amazon
        DataZone assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.accept_predictions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#accept_predictions)
        """
    def accept_subscription_request(
        self, *, domainIdentifier: str, identifier: str, decisionComment: str = None
    ) -> AcceptSubscriptionRequestOutputTypeDef:
        """
        Accepts a subscription request to a specific asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.accept_subscription_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#accept_subscription_request)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#can_paginate)
        """
    def cancel_subscription(
        self, *, domainIdentifier: str, identifier: str
    ) -> CancelSubscriptionOutputTypeDef:
        """
        Cancels the subscription to the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.cancel_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#cancel_subscription)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#close)
        """
    def create_asset(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        typeIdentifier: str,
        clientToken: str = None,
        description: str = None,
        externalIdentifier: str = None,
        formsInput: List["FormInputTypeDef"] = None,
        glossaryTerms: List[str] = None,
        predictionConfiguration: "PredictionConfigurationTypeDef" = None,
        typeRevision: str = None
    ) -> CreateAssetOutputTypeDef:
        """
        Creates an asset in Amazon DataZone catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_asset)
        """
    def create_asset_revision(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str,
        clientToken: str = None,
        description: str = None,
        formsInput: List["FormInputTypeDef"] = None,
        glossaryTerms: List[str] = None,
        predictionConfiguration: "PredictionConfigurationTypeDef" = None,
        typeRevision: str = None
    ) -> CreateAssetRevisionOutputTypeDef:
        """
        Creates a revision of the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_asset_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_asset_revision)
        """
    def create_asset_type(
        self,
        *,
        domainIdentifier: str,
        formsInput: Dict[str, "FormEntryInputTypeDef"],
        name: str,
        owningProjectIdentifier: str,
        description: str = None
    ) -> CreateAssetTypeOutputTypeDef:
        """
        Creates a custom asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_asset_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_asset_type)
        """
    def create_data_source(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        name: str,
        projectIdentifier: str,
        type: str,
        assetFormsInput: List["FormInputTypeDef"] = None,
        clientToken: str = None,
        configuration: "DataSourceConfigurationInputTypeDef" = None,
        description: str = None,
        enableSetting: EnableSettingType = None,
        publishOnImport: bool = None,
        recommendation: "RecommendationConfigurationTypeDef" = None,
        schedule: "ScheduleConfigurationTypeDef" = None
    ) -> CreateDataSourceOutputTypeDef:
        """
        Creates an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_data_source)
        """
    def create_domain(
        self,
        *,
        domainExecutionRole: str,
        name: str,
        clientToken: str = None,
        description: str = None,
        kmsKeyIdentifier: str = None,
        singleSignOn: "SingleSignOnTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateDomainOutputTypeDef:
        """
        Creates an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_domain)
        """
    def create_environment(
        self,
        *,
        domainIdentifier: str,
        environmentProfileIdentifier: str,
        name: str,
        projectIdentifier: str,
        description: str = None,
        glossaryTerms: List[str] = None,
        userParameters: List["EnvironmentParameterTypeDef"] = None
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Create an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_environment)
        """
    def create_environment_profile(
        self,
        *,
        domainIdentifier: str,
        environmentBlueprintIdentifier: str,
        name: str,
        projectIdentifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        description: str = None,
        userParameters: List["EnvironmentParameterTypeDef"] = None
    ) -> CreateEnvironmentProfileOutputTypeDef:
        """
        Creates an Amazon DataZone environment profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_environment_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_environment_profile)
        """
    def create_form_type(
        self,
        *,
        domainIdentifier: str,
        model: "ModelTypeDef",
        name: str,
        owningProjectIdentifier: str,
        description: str = None,
        status: FormTypeStatusType = None
    ) -> CreateFormTypeOutputTypeDef:
        """
        Creates a metadata form type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_form_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_form_type)
        """
    def create_glossary(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        clientToken: str = None,
        description: str = None,
        status: GlossaryStatusType = None
    ) -> CreateGlossaryOutputTypeDef:
        """
        Creates an Amazon DataZone business glossary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_glossary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_glossary)
        """
    def create_glossary_term(
        self,
        *,
        domainIdentifier: str,
        glossaryIdentifier: str,
        name: str,
        clientToken: str = None,
        longDescription: str = None,
        shortDescription: str = None,
        status: GlossaryTermStatusType = None,
        termRelations: "TermRelationsTypeDef" = None
    ) -> CreateGlossaryTermOutputTypeDef:
        """
        Creates a business glossary term.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_glossary_term)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_glossary_term)
        """
    def create_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str, clientToken: str = None
    ) -> CreateGroupProfileOutputTypeDef:
        """
        Creates a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_group_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_group_profile)
        """
    def create_listing_change_set(
        self,
        *,
        action: ChangeActionType,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: Literal["ASSET"],
        clientToken: str = None,
        entityRevision: str = None
    ) -> CreateListingChangeSetOutputTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/datazo
        ne-2018-05-10/CreateListingChangeSet>`_ **Request Syntax** response =
        client.create_listing_change_set( action='PUBLISH'|'UNPUBLISH',
        clientToken='string', domainIdentifier='string', en...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_listing_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_listing_change_set)
        """
    def create_project(
        self,
        *,
        domainIdentifier: str,
        name: str,
        description: str = None,
        glossaryTerms: List[str] = None
    ) -> CreateProjectOutputTypeDef:
        """
        Creates an Amazon DataZone project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_project)
        """
    def create_project_membership(
        self,
        *,
        designation: UserDesignationType,
        domainIdentifier: str,
        member: "MemberTypeDef",
        projectIdentifier: str
    ) -> Dict[str, Any]:
        """
        Creates a project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_project_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_project_membership)
        """
    def create_subscription_grant(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        grantedEntity: "GrantedEntityInputTypeDef",
        subscriptionTargetIdentifier: str,
        assetTargetNames: List["AssetTargetNameMapTypeDef"] = None,
        clientToken: str = None
    ) -> CreateSubscriptionGrantOutputTypeDef:
        """
        Creates a subsscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_subscription_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_subscription_grant)
        """
    def create_subscription_request(
        self,
        *,
        domainIdentifier: str,
        requestReason: str,
        subscribedListings: List["SubscribedListingInputTypeDef"],
        subscribedPrincipals: List["SubscribedPrincipalInputTypeDef"],
        clientToken: str = None
    ) -> CreateSubscriptionRequestOutputTypeDef:
        """
        Creates a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_subscription_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_subscription_request)
        """
    def create_subscription_target(
        self,
        *,
        applicableAssetTypes: List[str],
        authorizedPrincipals: List[str],
        domainIdentifier: str,
        environmentIdentifier: str,
        manageAccessRole: str,
        name: str,
        subscriptionTargetConfig: List["SubscriptionTargetFormTypeDef"],
        type: str,
        clientToken: str = None,
        provider: str = None
    ) -> CreateSubscriptionTargetOutputTypeDef:
        """
        Creates a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_subscription_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_subscription_target)
        """
    def create_user_profile(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str,
        clientToken: str = None,
        userType: UserTypeType = None
    ) -> CreateUserProfileOutputTypeDef:
        """
        Creates a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.create_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#create_user_profile)
        """
    def delete_asset(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Delets an asset in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_asset)
        """
    def delete_asset_type(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes an asset type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_asset_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_asset_type)
        """
    def delete_data_source(
        self, *, domainIdentifier: str, identifier: str, clientToken: str = None
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Deletes a data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_data_source)
        """
    def delete_domain(
        self, *, identifier: str, clientToken: str = None
    ) -> DeleteDomainOutputTypeDef:
        """
        Deletes a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_domain)
        """
    def delete_environment(self, *, domainIdentifier: str, identifier: str) -> None:
        """
        Deletes an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_environment)
        """
    def delete_environment_blueprint_configuration(
        self, *, domainIdentifier: str, environmentBlueprintIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_environment_blueprint_configuration)
        """
    def delete_environment_profile(self, *, domainIdentifier: str, identifier: str) -> None:
        """
        Deletes an environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_environment_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_environment_profile)
        """
    def delete_form_type(self, *, domainIdentifier: str, formTypeIdentifier: str) -> Dict[str, Any]:
        """
        Delets and metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_form_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_form_type)
        """
    def delete_glossary(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_glossary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_glossary)
        """
    def delete_glossary_term(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_glossary_term)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_glossary_term)
        """
    def delete_listing(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/DeleteListing>`_
        **Request Syntax** response = client.delete_listing( domainIdentifier='string',
        identifier='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_listing)
        """
    def delete_project(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_project)
        """
    def delete_project_membership(
        self, *, domainIdentifier: str, member: "MemberTypeDef", projectIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_project_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_project_membership)
        """
    def delete_subscription_grant(
        self, *, domainIdentifier: str, identifier: str
    ) -> DeleteSubscriptionGrantOutputTypeDef:
        """
        Deletes and subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_subscription_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_subscription_grant)
        """
    def delete_subscription_request(self, *, domainIdentifier: str, identifier: str) -> None:
        """
        Deletes a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_subscription_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_subscription_request)
        """
    def delete_subscription_target(
        self, *, domainIdentifier: str, environmentIdentifier: str, identifier: str
    ) -> None:
        """
        Deletes a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.delete_subscription_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#delete_subscription_target)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#generate_presigned_url)
        """
    def get_asset(
        self, *, domainIdentifier: str, identifier: str, revision: str = None
    ) -> GetAssetOutputTypeDef:
        """
        Gets an Amazon DataZone asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_asset)
        """
    def get_asset_type(
        self, *, domainIdentifier: str, identifier: str, revision: str = None
    ) -> GetAssetTypeOutputTypeDef:
        """
        Gets an Amazon DataZone asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_asset_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_asset_type)
        """
    def get_data_source(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetDataSourceOutputTypeDef:
        """
        Gets an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_data_source)
        """
    def get_data_source_run(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetDataSourceRunOutputTypeDef:
        """
        Gets an Amazon DataZone data source run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_data_source_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_data_source_run)
        """
    def get_domain(self, *, identifier: str) -> GetDomainOutputTypeDef:
        """
        Gets an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_domain)
        """
    def get_environment(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentOutputTypeDef:
        """
        Gets an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_environment)
        """
    def get_environment_blueprint(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentBlueprintOutputTypeDef:
        """
        Gets an Amazon DataZone blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_environment_blueprint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_environment_blueprint)
        """
    def get_environment_blueprint_configuration(
        self, *, domainIdentifier: str, environmentBlueprintIdentifier: str
    ) -> GetEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Gets the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_environment_blueprint_configuration)
        """
    def get_environment_profile(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentProfileOutputTypeDef:
        """
        Gets an evinronment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_environment_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_environment_profile)
        """
    def get_form_type(
        self, *, domainIdentifier: str, formTypeIdentifier: str, revision: str = None
    ) -> GetFormTypeOutputTypeDef:
        """
        Gets a metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_form_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_form_type)
        """
    def get_glossary(self, *, domainIdentifier: str, identifier: str) -> GetGlossaryOutputTypeDef:
        """
        Gets a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_glossary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_glossary)
        """
    def get_glossary_term(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetGlossaryTermOutputTypeDef:
        """
        Gets a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_glossary_term)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_glossary_term)
        """
    def get_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str
    ) -> GetGroupProfileOutputTypeDef:
        """
        Gets a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_group_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_group_profile)
        """
    def get_iam_portal_login_url(
        self, *, domainIdentifier: str
    ) -> GetIamPortalLoginUrlOutputTypeDef:
        """
        Gets the data portal URL for the specified Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_iam_portal_login_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_iam_portal_login_url)
        """
    def get_listing(
        self, *, domainIdentifier: str, identifier: str, listingRevision: str = None
    ) -> GetListingOutputTypeDef:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/GetListing>`_
        **Request Syntax** response = client.get_listing( domainIdentifier='string',
        identifier='string', listingRevision='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_listing)
        """
    def get_project(self, *, domainIdentifier: str, identifier: str) -> GetProjectOutputTypeDef:
        """
        Gets a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_project)
        """
    def get_subscription(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionOutputTypeDef:
        """
        Gets a subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_subscription)
        """
    def get_subscription_grant(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionGrantOutputTypeDef:
        """
        Gets the subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_subscription_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_subscription_grant)
        """
    def get_subscription_request_details(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionRequestDetailsOutputTypeDef:
        """
        Gets the details of the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_subscription_request_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_subscription_request_details)
        """
    def get_subscription_target(
        self, *, domainIdentifier: str, environmentIdentifier: str, identifier: str
    ) -> GetSubscriptionTargetOutputTypeDef:
        """
        Gets the subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_subscription_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_subscription_target)
        """
    def get_user_profile(
        self, *, domainIdentifier: str, userIdentifier: str, type: UserProfileTypeType = None
    ) -> GetUserProfileOutputTypeDef:
        """
        Gets a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.get_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#get_user_profile)
        """
    def list_asset_revisions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAssetRevisionsOutputTypeDef:
        """
        Lists the revisions for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_asset_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_asset_revisions)
        """
    def list_data_source_run_activities(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        maxResults: int = None,
        nextToken: str = None,
        status: DataAssetActivityStatusType = None
    ) -> ListDataSourceRunActivitiesOutputTypeDef:
        """
        Lists data source run activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_data_source_run_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_data_source_run_activities)
        """
    def list_data_source_runs(
        self,
        *,
        dataSourceIdentifier: str,
        domainIdentifier: str,
        maxResults: int = None,
        nextToken: str = None,
        status: DataSourceRunStatusType = None
    ) -> ListDataSourceRunsOutputTypeDef:
        """
        Lists data source runs in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_data_source_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_data_source_runs)
        """
    def list_data_sources(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        environmentIdentifier: str = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        status: DataSourceStatusType = None,
        type: str = None
    ) -> ListDataSourcesOutputTypeDef:
        """
        Lists data sources in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_data_sources)
        """
    def list_domains(
        self, *, maxResults: int = None, nextToken: str = None, status: DomainStatusType = None
    ) -> ListDomainsOutputTypeDef:
        """
        Lists Amazon DataZone domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_domains)
        """
    def list_environment_blueprint_configurations(
        self, *, domainIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListEnvironmentBlueprintConfigurationsOutputTypeDef:
        """
        Lists blueprint configurations for a Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_environment_blueprint_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_environment_blueprint_configurations)
        """
    def list_environment_blueprints(
        self,
        *,
        domainIdentifier: str,
        managed: bool = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None
    ) -> ListEnvironmentBlueprintsOutputTypeDef:
        """
        Lists blueprints in an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_environment_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_environment_blueprints)
        """
    def list_environment_profiles(
        self,
        *,
        domainIdentifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        environmentBlueprintIdentifier: str = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        projectIdentifier: str = None
    ) -> ListEnvironmentProfilesOutputTypeDef:
        """
        Lists Amazon DataZone environment profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_environment_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_environment_profiles)
        """
    def list_environments(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        environmentBlueprintIdentifier: str = None,
        environmentProfileIdentifier: str = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        provider: str = None,
        status: EnvironmentStatusType = None
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists Amazon DataZone environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_environments)
        """
    def list_notifications(
        self,
        *,
        domainIdentifier: str,
        type: NotificationTypeType,
        afterTimestamp: Union[datetime, str] = None,
        beforeTimestamp: Union[datetime, str] = None,
        maxResults: int = None,
        nextToken: str = None,
        subjects: List[str] = None,
        taskStatus: TaskStatusType = None
    ) -> ListNotificationsOutputTypeDef:
        """
        Lists all Amazon DataZone notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_notifications)
        """
    def list_project_memberships(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["NAME"] = None,
        sortOrder: SortOrderType = None
    ) -> ListProjectMembershipsOutputTypeDef:
        """
        Lists all members of the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_project_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_project_memberships)
        """
    def list_projects(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        userIdentifier: str = None
    ) -> ListProjectsOutputTypeDef:
        """
        Lists Amazon DataZone projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_projects)
        """
    def list_subscription_grants(
        self,
        *,
        domainIdentifier: str,
        environmentId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        subscribedListingId: str = None,
        subscriptionId: str = None,
        subscriptionTargetId: str = None
    ) -> ListSubscriptionGrantsOutputTypeDef:
        """
        Lists subscription grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_subscription_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_subscription_grants)
        """
    def list_subscription_requests(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        owningProjectId: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        status: SubscriptionRequestStatusType = None,
        subscribedListingId: str = None
    ) -> ListSubscriptionRequestsOutputTypeDef:
        """
        Lists Amazon DataZone subscription requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_subscription_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_subscription_requests)
        """
    def list_subscription_targets(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None
    ) -> ListSubscriptionTargetsOutputTypeDef:
        """
        Lists subscription targets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_subscription_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_subscription_targets)
        """
    def list_subscriptions(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        owningProjectId: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        status: SubscriptionStatusType = None,
        subscribedListingId: str = None,
        subscriptionRequestIdentifier: str = None
    ) -> ListSubscriptionsOutputTypeDef:
        """
        Lists subscriptions in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_subscriptions)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for the specified resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#list_tags_for_resource)
        """
    def put_environment_blueprint_configuration(
        self,
        *,
        domainIdentifier: str,
        enabledRegions: List[str],
        environmentBlueprintIdentifier: str,
        manageAccessRoleArn: str = None,
        provisioningRoleArn: str = None,
        regionalParameters: Dict[str, Dict[str, str]] = None
    ) -> PutEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Writes the configuration for the specified environment blueprint in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.put_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#put_environment_blueprint_configuration)
        """
    def reject_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str = None,
        rejectChoices: List["RejectChoiceTypeDef"] = None,
        rejectRule: "RejectRuleTypeDef" = None,
        revision: str = None
    ) -> RejectPredictionsOutputTypeDef:
        """
        Rejects automatically generated business-friendly metadata for your Amazon
        DataZone assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.reject_predictions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#reject_predictions)
        """
    def reject_subscription_request(
        self, *, domainIdentifier: str, identifier: str, decisionComment: str = None
    ) -> RejectSubscriptionRequestOutputTypeDef:
        """
        Rejects the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.reject_subscription_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#reject_subscription_request)
        """
    def revoke_subscription(
        self, *, domainIdentifier: str, identifier: str, retainPermissions: bool = None
    ) -> RevokeSubscriptionOutputTypeDef:
        """
        Revokes a specified subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.revoke_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#revoke_subscription)
        """
    def search(
        self,
        *,
        domainIdentifier: str,
        searchScope: InventorySearchScopeType,
        additionalAttributes: List[Literal["FORMS"]] = None,
        filters: "FilterClauseTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        owningProjectIdentifier: str = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None
    ) -> SearchOutputTypeDef:
        """
        Searches for assets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#search)
        """
    def search_group_profiles(
        self,
        *,
        domainIdentifier: str,
        groupType: GroupSearchTypeType,
        maxResults: int = None,
        nextToken: str = None,
        searchText: str = None
    ) -> SearchGroupProfilesOutputTypeDef:
        """
        Searches group profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.search_group_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#search_group_profiles)
        """
    def search_listings(
        self,
        *,
        domainIdentifier: str,
        additionalAttributes: List[Literal["FORMS"]] = None,
        filters: "FilterClauseTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None
    ) -> SearchListingsOutputTypeDef:
        """
        Searches listings in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.search_listings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#search_listings)
        """
    def search_types(
        self,
        *,
        domainIdentifier: str,
        managed: bool,
        searchScope: TypesSearchScopeType,
        filters: "FilterClauseTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None
    ) -> SearchTypesOutputTypeDef:
        """
        Searches for types in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.search_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#search_types)
        """
    def search_user_profiles(
        self,
        *,
        domainIdentifier: str,
        userType: UserSearchTypeType,
        maxResults: int = None,
        nextToken: str = None,
        searchText: str = None
    ) -> SearchUserProfilesOutputTypeDef:
        """
        Searches user profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.search_user_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#search_user_profiles)
        """
    def start_data_source_run(
        self, *, dataSourceIdentifier: str, domainIdentifier: str, clientToken: str = None
    ) -> StartDataSourceRunOutputTypeDef:
        """
        Start the run of the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.start_data_source_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#start_data_source_run)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#untag_resource)
        """
    def update_data_source(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        assetFormsInput: List["FormInputTypeDef"] = None,
        configuration: "DataSourceConfigurationInputTypeDef" = None,
        description: str = None,
        enableSetting: EnableSettingType = None,
        name: str = None,
        publishOnImport: bool = None,
        recommendation: "RecommendationConfigurationTypeDef" = None,
        schedule: "ScheduleConfigurationTypeDef" = None
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_data_source)
        """
    def update_domain(
        self,
        *,
        identifier: str,
        clientToken: str = None,
        description: str = None,
        domainExecutionRole: str = None,
        name: str = None,
        singleSignOn: "SingleSignOnTypeDef" = None
    ) -> UpdateDomainOutputTypeDef:
        """
        Updates a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_domain)
        """
    def update_environment(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str = None,
        glossaryTerms: List[str] = None,
        name: str = None
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates the specified environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_environment)
        """
    def update_environment_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        description: str = None,
        name: str = None,
        userParameters: List["EnvironmentParameterTypeDef"] = None
    ) -> UpdateEnvironmentProfileOutputTypeDef:
        """
        Updates the specified environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_environment_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_environment_profile)
        """
    def update_glossary(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str = None,
        description: str = None,
        name: str = None,
        status: GlossaryStatusType = None
    ) -> UpdateGlossaryOutputTypeDef:
        """
        Updates the business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_glossary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_glossary)
        """
    def update_glossary_term(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        glossaryIdentifier: str = None,
        longDescription: str = None,
        name: str = None,
        shortDescription: str = None,
        status: GlossaryTermStatusType = None,
        termRelations: "TermRelationsTypeDef" = None
    ) -> UpdateGlossaryTermOutputTypeDef:
        """
        Updates a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_glossary_term)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_glossary_term)
        """
    def update_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str, status: GroupProfileStatusType
    ) -> UpdateGroupProfileOutputTypeDef:
        """
        Updates the specified group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_group_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_group_profile)
        """
    def update_project(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str = None,
        glossaryTerms: List[str] = None,
        name: str = None
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates the specified project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_project)
        """
    def update_subscription_grant_status(
        self,
        *,
        assetIdentifier: str,
        domainIdentifier: str,
        identifier: str,
        status: SubscriptionGrantStatusType,
        failureCause: "FailureCauseTypeDef" = None,
        targetName: str = None
    ) -> UpdateSubscriptionGrantStatusOutputTypeDef:
        """
        Updates the status of the specified subscription grant status in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_subscription_grant_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_subscription_grant_status)
        """
    def update_subscription_request(
        self, *, domainIdentifier: str, identifier: str, requestReason: str
    ) -> UpdateSubscriptionRequestOutputTypeDef:
        """
        Updates a specified subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_subscription_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_subscription_request)
        """
    def update_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
        applicableAssetTypes: List[str] = None,
        authorizedPrincipals: List[str] = None,
        manageAccessRole: str = None,
        name: str = None,
        provider: str = None,
        subscriptionTargetConfig: List["SubscriptionTargetFormTypeDef"] = None
    ) -> UpdateSubscriptionTargetOutputTypeDef:
        """
        Updates the specified subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_subscription_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_subscription_target)
        """
    def update_user_profile(
        self,
        *,
        domainIdentifier: str,
        status: UserProfileStatusType,
        userIdentifier: str,
        type: UserProfileTypeType = None
    ) -> UpdateUserProfileOutputTypeDef:
        """
        Updates the specified user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Client.update_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/client.html#update_user_profile)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_revisions"]
    ) -> ListAssetRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListAssetRevisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listassetrevisionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_run_activities"]
    ) -> ListDataSourceRunActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRunActivities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunactivitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_runs"]
    ) -> ListDataSourceRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprint_configurations"]
    ) -> ListEnvironmentBlueprintConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprints"]
    ) -> ListEnvironmentBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_profiles"]
    ) -> ListEnvironmentProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notifications"]
    ) -> ListNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListNotifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listnotificationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_memberships"]
    ) -> ListProjectMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListProjectMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectmembershipspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_grants"]
    ) -> ListSubscriptionGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionGrants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiongrantspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_requests"]
    ) -> ListSubscriptionRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionRequests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionrequestspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_targets"]
    ) -> ListSubscriptionTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiontargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.ListSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.Search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_group_profiles"]
    ) -> SearchGroupProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.SearchGroupProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchgroupprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_listings"]) -> SearchListingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.SearchListings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchlistingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_types"]) -> SearchTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.SearchTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchtypespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_user_profiles"]
    ) -> SearchUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/datazone.html#DataZone.Paginator.SearchUserProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchuserprofilespaginator)
        """
