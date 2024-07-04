"""
Type annotations for cleanrooms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cleanrooms import CleanRoomsServiceClient

    client: CleanRoomsServiceClient = boto3.client("cleanrooms")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AnalysisRuleTypeType,
    CollaborationQueryLogStatusType,
    ConfiguredTableAnalysisRuleTypeType,
    FilterableMemberStatusType,
    MemberAbilityType,
    MembershipQueryLogStatusType,
    MembershipStatusType,
    PrivacyBudgetTemplateAutoRefreshType,
    ProtectedQueryStatusType,
)
from .paginator import (
    ListAnalysisTemplatesPaginator,
    ListCollaborationAnalysisTemplatesPaginator,
    ListCollaborationConfiguredAudienceModelAssociationsPaginator,
    ListCollaborationPrivacyBudgetsPaginator,
    ListCollaborationPrivacyBudgetTemplatesPaginator,
    ListCollaborationsPaginator,
    ListConfiguredAudienceModelAssociationsPaginator,
    ListConfiguredTableAssociationsPaginator,
    ListConfiguredTablesPaginator,
    ListMembershipsPaginator,
    ListMembersPaginator,
    ListPrivacyBudgetsPaginator,
    ListPrivacyBudgetTemplatesPaginator,
    ListProtectedQueriesPaginator,
    ListSchemasPaginator,
)
from .type_defs import (
    AnalysisParameterTypeDef,
    AnalysisSourceTypeDef,
    BatchGetCollaborationAnalysisTemplateOutputTypeDef,
    BatchGetSchemaAnalysisRuleOutputTypeDef,
    BatchGetSchemaOutputTypeDef,
    ConfiguredTableAnalysisRulePolicyTypeDef,
    CreateAnalysisTemplateOutputTypeDef,
    CreateCollaborationOutputTypeDef,
    CreateConfiguredAudienceModelAssociationOutputTypeDef,
    CreateConfiguredTableAnalysisRuleOutputTypeDef,
    CreateConfiguredTableAssociationOutputTypeDef,
    CreateConfiguredTableOutputTypeDef,
    CreateMembershipOutputTypeDef,
    CreatePrivacyBudgetTemplateOutputTypeDef,
    DataEncryptionMetadataTypeDef,
    GetAnalysisTemplateOutputTypeDef,
    GetCollaborationAnalysisTemplateOutputTypeDef,
    GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef,
    GetCollaborationOutputTypeDef,
    GetCollaborationPrivacyBudgetTemplateOutputTypeDef,
    GetConfiguredAudienceModelAssociationOutputTypeDef,
    GetConfiguredTableAnalysisRuleOutputTypeDef,
    GetConfiguredTableAssociationOutputTypeDef,
    GetConfiguredTableOutputTypeDef,
    GetMembershipOutputTypeDef,
    GetPrivacyBudgetTemplateOutputTypeDef,
    GetProtectedQueryOutputTypeDef,
    GetSchemaAnalysisRuleOutputTypeDef,
    GetSchemaOutputTypeDef,
    ListAnalysisTemplatesOutputTypeDef,
    ListCollaborationAnalysisTemplatesOutputTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef,
    ListCollaborationPrivacyBudgetsOutputTypeDef,
    ListCollaborationPrivacyBudgetTemplatesOutputTypeDef,
    ListCollaborationsOutputTypeDef,
    ListConfiguredAudienceModelAssociationsOutputTypeDef,
    ListConfiguredTableAssociationsOutputTypeDef,
    ListConfiguredTablesOutputTypeDef,
    ListMembershipsOutputTypeDef,
    ListMembersOutputTypeDef,
    ListPrivacyBudgetsOutputTypeDef,
    ListPrivacyBudgetTemplatesOutputTypeDef,
    ListProtectedQueriesOutputTypeDef,
    ListSchemasOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MembershipPaymentConfigurationTypeDef,
    MembershipProtectedQueryResultConfigurationTypeDef,
    MemberSpecificationTypeDef,
    PaymentConfigurationTypeDef,
    PreviewPrivacyImpactOutputTypeDef,
    PreviewPrivacyImpactParametersInputTypeDef,
    PrivacyBudgetTemplateParametersInputTypeDef,
    PrivacyBudgetTemplateUpdateParametersTypeDef,
    ProtectedQueryResultConfigurationTypeDef,
    ProtectedQuerySQLParametersTypeDef,
    SchemaAnalysisRuleRequestTypeDef,
    StartProtectedQueryOutputTypeDef,
    TableReferenceTypeDef,
    UpdateAnalysisTemplateOutputTypeDef,
    UpdateCollaborationOutputTypeDef,
    UpdateConfiguredAudienceModelAssociationOutputTypeDef,
    UpdateConfiguredTableAnalysisRuleOutputTypeDef,
    UpdateConfiguredTableAssociationOutputTypeDef,
    UpdateConfiguredTableOutputTypeDef,
    UpdateMembershipOutputTypeDef,
    UpdatePrivacyBudgetTemplateOutputTypeDef,
    UpdateProtectedQueryOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CleanRoomsServiceClient",)

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
    ValidationException: Type[BotocoreClientError]

class CleanRoomsServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CleanRoomsServiceClient exceptions.
        """

    def batch_get_collaboration_analysis_template(
        self, *, collaborationIdentifier: str, analysisTemplateArns: List[str]
    ) -> BatchGetCollaborationAnalysisTemplateOutputTypeDef:
        """
        Retrieves multiple analysis templates within a collaboration by their Amazon
        Resource Names (ARNs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.batch_get_collaboration_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#batch_get_collaboration_analysis_template)
        """

    def batch_get_schema(
        self, *, collaborationIdentifier: str, names: List[str]
    ) -> BatchGetSchemaOutputTypeDef:
        """
        Retrieves multiple schemas by their identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.batch_get_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#batch_get_schema)
        """

    def batch_get_schema_analysis_rule(
        self,
        *,
        collaborationIdentifier: str,
        schemaAnalysisRuleRequests: List["SchemaAnalysisRuleRequestTypeDef"]
    ) -> BatchGetSchemaAnalysisRuleOutputTypeDef:
        """
        Retrieves multiple analysis rule schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.batch_get_schema_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#batch_get_schema_analysis_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#close)
        """

    def create_analysis_template(
        self,
        *,
        membershipIdentifier: str,
        name: str,
        format: Literal["SQL"],
        source: "AnalysisSourceTypeDef",
        description: str = None,
        tags: Dict[str, str] = None,
        analysisParameters: List["AnalysisParameterTypeDef"] = None
    ) -> CreateAnalysisTemplateOutputTypeDef:
        """
        Creates a new analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_analysis_template)
        """

    def create_collaboration(
        self,
        *,
        members: List["MemberSpecificationTypeDef"],
        name: str,
        description: str,
        creatorMemberAbilities: List[MemberAbilityType],
        creatorDisplayName: str,
        queryLogStatus: CollaborationQueryLogStatusType,
        dataEncryptionMetadata: "DataEncryptionMetadataTypeDef" = None,
        tags: Dict[str, str] = None,
        creatorPaymentConfiguration: "PaymentConfigurationTypeDef" = None
    ) -> CreateCollaborationOutputTypeDef:
        """
        Creates a new collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_collaboration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_collaboration)
        """

    def create_configured_audience_model_association(
        self,
        *,
        membershipIdentifier: str,
        configuredAudienceModelArn: str,
        configuredAudienceModelAssociationName: str,
        manageResourcePolicies: bool,
        tags: Dict[str, str] = None,
        description: str = None
    ) -> CreateConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Provides the details necessary to create a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_configured_audience_model_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_configured_audience_model_association)
        """

    def create_configured_table(
        self,
        *,
        name: str,
        tableReference: "TableReferenceTypeDef",
        allowedColumns: List[str],
        analysisMethod: Literal["DIRECT_QUERY"],
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateConfiguredTableOutputTypeDef:
        """
        Creates a new configured table resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_configured_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_configured_table)
        """

    def create_configured_table_analysis_rule(
        self,
        *,
        configuredTableIdentifier: str,
        analysisRuleType: ConfiguredTableAnalysisRuleTypeType,
        analysisRulePolicy: "ConfiguredTableAnalysisRulePolicyTypeDef"
    ) -> CreateConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Creates a new analysis rule for a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_configured_table_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_configured_table_analysis_rule)
        """

    def create_configured_table_association(
        self,
        *,
        name: str,
        membershipIdentifier: str,
        configuredTableIdentifier: str,
        roleArn: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateConfiguredTableAssociationOutputTypeDef:
        """
        Creates a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_configured_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_configured_table_association)
        """

    def create_membership(
        self,
        *,
        collaborationIdentifier: str,
        queryLogStatus: MembershipQueryLogStatusType,
        tags: Dict[str, str] = None,
        defaultResultConfiguration: "MembershipProtectedQueryResultConfigurationTypeDef" = None,
        paymentConfiguration: "MembershipPaymentConfigurationTypeDef" = None
    ) -> CreateMembershipOutputTypeDef:
        """
        Creates a membership for a specific collaboration identifier and joins the
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_membership)
        """

    def create_privacy_budget_template(
        self,
        *,
        membershipIdentifier: str,
        autoRefresh: PrivacyBudgetTemplateAutoRefreshType,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        parameters: "PrivacyBudgetTemplateParametersInputTypeDef",
        tags: Dict[str, str] = None
    ) -> CreatePrivacyBudgetTemplateOutputTypeDef:
        """
        Creates a privacy budget template for a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.create_privacy_budget_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#create_privacy_budget_template)
        """

    def delete_analysis_template(
        self, *, membershipIdentifier: str, analysisTemplateIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_analysis_template)
        """

    def delete_collaboration(self, *, collaborationIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_collaboration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_collaboration)
        """

    def delete_configured_audience_model_association(
        self, *, configuredAudienceModelAssociationIdentifier: str, membershipIdentifier: str
    ) -> Dict[str, Any]:
        """
        Provides the information necessary to delete a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_configured_audience_model_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_configured_audience_model_association)
        """

    def delete_configured_table(self, *, configuredTableIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_configured_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_configured_table)
        """

    def delete_configured_table_analysis_rule(
        self,
        *,
        configuredTableIdentifier: str,
        analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    ) -> Dict[str, Any]:
        """
        Deletes a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_configured_table_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_configured_table_analysis_rule)
        """

    def delete_configured_table_association(
        self, *, configuredTableAssociationIdentifier: str, membershipIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_configured_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_configured_table_association)
        """

    def delete_member(self, *, collaborationIdentifier: str, accountId: str) -> Dict[str, Any]:
        """
        Removes the specified member from a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_member)
        """

    def delete_membership(self, *, membershipIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_membership)
        """

    def delete_privacy_budget_template(
        self, *, membershipIdentifier: str, privacyBudgetTemplateIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a privacy budget template for a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.delete_privacy_budget_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#delete_privacy_budget_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#generate_presigned_url)
        """

    def get_analysis_template(
        self, *, membershipIdentifier: str, analysisTemplateIdentifier: str
    ) -> GetAnalysisTemplateOutputTypeDef:
        """
        Retrieves an analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_analysis_template)
        """

    def get_collaboration(self, *, collaborationIdentifier: str) -> GetCollaborationOutputTypeDef:
        """
        Returns metadata about a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_collaboration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_collaboration)
        """

    def get_collaboration_analysis_template(
        self, *, collaborationIdentifier: str, analysisTemplateArn: str
    ) -> GetCollaborationAnalysisTemplateOutputTypeDef:
        """
        Retrieves an analysis template within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_collaboration_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_collaboration_analysis_template)
        """

    def get_collaboration_configured_audience_model_association(
        self, *, collaborationIdentifier: str, configuredAudienceModelAssociationIdentifier: str
    ) -> GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Retrieves a configured audience model association within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_collaboration_configured_audience_model_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_collaboration_configured_audience_model_association)
        """

    def get_collaboration_privacy_budget_template(
        self, *, collaborationIdentifier: str, privacyBudgetTemplateIdentifier: str
    ) -> GetCollaborationPrivacyBudgetTemplateOutputTypeDef:
        """
        Returns details about a specified privacy budget template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_collaboration_privacy_budget_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_collaboration_privacy_budget_template)
        """

    def get_configured_audience_model_association(
        self, *, configuredAudienceModelAssociationIdentifier: str, membershipIdentifier: str
    ) -> GetConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Returns information about a configured audience model association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_configured_audience_model_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_configured_audience_model_association)
        """

    def get_configured_table(
        self, *, configuredTableIdentifier: str
    ) -> GetConfiguredTableOutputTypeDef:
        """
        Retrieves a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_configured_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_configured_table)
        """

    def get_configured_table_analysis_rule(
        self,
        *,
        configuredTableIdentifier: str,
        analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    ) -> GetConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Retrieves a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_configured_table_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_configured_table_analysis_rule)
        """

    def get_configured_table_association(
        self, *, configuredTableAssociationIdentifier: str, membershipIdentifier: str
    ) -> GetConfiguredTableAssociationOutputTypeDef:
        """
        Retrieves a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_configured_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_configured_table_association)
        """

    def get_membership(self, *, membershipIdentifier: str) -> GetMembershipOutputTypeDef:
        """
        Retrieves a specified membership for an identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_membership)
        """

    def get_privacy_budget_template(
        self, *, membershipIdentifier: str, privacyBudgetTemplateIdentifier: str
    ) -> GetPrivacyBudgetTemplateOutputTypeDef:
        """
        Returns details for a specified privacy budget template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_privacy_budget_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_privacy_budget_template)
        """

    def get_protected_query(
        self, *, membershipIdentifier: str, protectedQueryIdentifier: str
    ) -> GetProtectedQueryOutputTypeDef:
        """
        Returns query processing metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_protected_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_protected_query)
        """

    def get_schema(self, *, collaborationIdentifier: str, name: str) -> GetSchemaOutputTypeDef:
        """
        Retrieves the schema for a relation within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_schema)
        """

    def get_schema_analysis_rule(
        self, *, collaborationIdentifier: str, name: str, type: AnalysisRuleTypeType
    ) -> GetSchemaAnalysisRuleOutputTypeDef:
        """
        Retrieves a schema analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.get_schema_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#get_schema_analysis_rule)
        """

    def list_analysis_templates(
        self, *, membershipIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListAnalysisTemplatesOutputTypeDef:
        """
        Lists analysis templates that the caller owns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_analysis_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_analysis_templates)
        """

    def list_collaboration_analysis_templates(
        self, *, collaborationIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListCollaborationAnalysisTemplatesOutputTypeDef:
        """
        Lists analysis templates within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_collaboration_analysis_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_collaboration_analysis_templates)
        """

    def list_collaboration_configured_audience_model_associations(
        self, *, collaborationIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef:
        """
        Lists configured audience model associations within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_collaboration_configured_audience_model_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_collaboration_configured_audience_model_associations)
        """

    def list_collaboration_privacy_budget_templates(
        self, *, collaborationIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListCollaborationPrivacyBudgetTemplatesOutputTypeDef:
        """
        Returns an array that summarizes each privacy budget template in a specified
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_collaboration_privacy_budget_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_collaboration_privacy_budget_templates)
        """

    def list_collaboration_privacy_budgets(
        self,
        *,
        collaborationIdentifier: str,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCollaborationPrivacyBudgetsOutputTypeDef:
        """
        Returns an array that summarizes each privacy budget in a specified
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_collaboration_privacy_budgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_collaboration_privacy_budgets)
        """

    def list_collaborations(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        memberStatus: FilterableMemberStatusType = None
    ) -> ListCollaborationsOutputTypeDef:
        """
        Lists collaborations the caller owns, is active in, or has been invited to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_collaborations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_collaborations)
        """

    def list_configured_audience_model_associations(
        self, *, membershipIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListConfiguredAudienceModelAssociationsOutputTypeDef:
        """
        Lists information about requested configured audience model associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_configured_audience_model_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_configured_audience_model_associations)
        """

    def list_configured_table_associations(
        self, *, membershipIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListConfiguredTableAssociationsOutputTypeDef:
        """
        Lists configured table associations for a membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_configured_table_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_configured_table_associations)
        """

    def list_configured_tables(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListConfiguredTablesOutputTypeDef:
        """
        Lists configured tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_configured_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_configured_tables)
        """

    def list_members(
        self, *, collaborationIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListMembersOutputTypeDef:
        """
        Lists all members within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_members)
        """

    def list_memberships(
        self, *, nextToken: str = None, maxResults: int = None, status: MembershipStatusType = None
    ) -> ListMembershipsOutputTypeDef:
        """
        Lists all memberships resources within the caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_memberships)
        """

    def list_privacy_budget_templates(
        self, *, membershipIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrivacyBudgetTemplatesOutputTypeDef:
        """
        Returns detailed information about the privacy budget templates in a specified
        membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_privacy_budget_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_privacy_budget_templates)
        """

    def list_privacy_budgets(
        self,
        *,
        membershipIdentifier: str,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        nextToken: str = None,
        maxResults: int = None
    ) -> ListPrivacyBudgetsOutputTypeDef:
        """
        Returns detailed information about the privacy budgets in a specified
        membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_privacy_budgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_privacy_budgets)
        """

    def list_protected_queries(
        self,
        *,
        membershipIdentifier: str,
        status: ProtectedQueryStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListProtectedQueriesOutputTypeDef:
        """
        Lists protected queries, sorted by the most recent query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_protected_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_protected_queries)
        """

    def list_schemas(
        self,
        *,
        collaborationIdentifier: str,
        schemaType: Literal["TABLE"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListSchemasOutputTypeDef:
        """
        Lists the schemas for relations within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_schemas)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists all of the tags that have been added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#list_tags_for_resource)
        """

    def preview_privacy_impact(
        self, *, membershipIdentifier: str, parameters: "PreviewPrivacyImpactParametersInputTypeDef"
    ) -> PreviewPrivacyImpactOutputTypeDef:
        """
        An estimate of the number of aggregation functions that the member who can query
        can run given epsilon and noise parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.preview_privacy_impact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#preview_privacy_impact)
        """

    def start_protected_query(
        self,
        *,
        type: Literal["SQL"],
        membershipIdentifier: str,
        sqlParameters: "ProtectedQuerySQLParametersTypeDef",
        resultConfiguration: "ProtectedQueryResultConfigurationTypeDef" = None
    ) -> StartProtectedQueryOutputTypeDef:
        """
        Creates a protected query that is started by Clean Rooms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.start_protected_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#start_protected_query)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#untag_resource)
        """

    def update_analysis_template(
        self, *, membershipIdentifier: str, analysisTemplateIdentifier: str, description: str = None
    ) -> UpdateAnalysisTemplateOutputTypeDef:
        """
        Updates the analysis template metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_analysis_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_analysis_template)
        """

    def update_collaboration(
        self, *, collaborationIdentifier: str, name: str = None, description: str = None
    ) -> UpdateCollaborationOutputTypeDef:
        """
        Updates collaboration metadata and can only be called by the collaboration
        owner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_collaboration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_collaboration)
        """

    def update_configured_audience_model_association(
        self,
        *,
        configuredAudienceModelAssociationIdentifier: str,
        membershipIdentifier: str,
        description: str = None,
        name: str = None
    ) -> UpdateConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Provides the details necessary to update a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_configured_audience_model_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_configured_audience_model_association)
        """

    def update_configured_table(
        self, *, configuredTableIdentifier: str, name: str = None, description: str = None
    ) -> UpdateConfiguredTableOutputTypeDef:
        """
        Updates a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_configured_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_configured_table)
        """

    def update_configured_table_analysis_rule(
        self,
        *,
        configuredTableIdentifier: str,
        analysisRuleType: ConfiguredTableAnalysisRuleTypeType,
        analysisRulePolicy: "ConfiguredTableAnalysisRulePolicyTypeDef"
    ) -> UpdateConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Updates a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_configured_table_analysis_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_configured_table_analysis_rule)
        """

    def update_configured_table_association(
        self,
        *,
        configuredTableAssociationIdentifier: str,
        membershipIdentifier: str,
        description: str = None,
        roleArn: str = None
    ) -> UpdateConfiguredTableAssociationOutputTypeDef:
        """
        Updates a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_configured_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_configured_table_association)
        """

    def update_membership(
        self,
        *,
        membershipIdentifier: str,
        queryLogStatus: MembershipQueryLogStatusType = None,
        defaultResultConfiguration: "MembershipProtectedQueryResultConfigurationTypeDef" = None
    ) -> UpdateMembershipOutputTypeDef:
        """
        Updates a membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_membership)
        """

    def update_privacy_budget_template(
        self,
        *,
        membershipIdentifier: str,
        privacyBudgetTemplateIdentifier: str,
        privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"],
        parameters: "PrivacyBudgetTemplateUpdateParametersTypeDef" = None
    ) -> UpdatePrivacyBudgetTemplateOutputTypeDef:
        """
        Updates the privacy budget template for the specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_privacy_budget_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_privacy_budget_template)
        """

    def update_protected_query(
        self,
        *,
        membershipIdentifier: str,
        protectedQueryIdentifier: str,
        targetStatus: Literal["CANCELLED"]
    ) -> UpdateProtectedQueryOutputTypeDef:
        """
        Updates the processing of a currently running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Client.update_protected_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client.html#update_protected_query)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_analysis_templates"]
    ) -> ListAnalysisTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListAnalysisTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listanalysistemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collaboration_analysis_templates"]
    ) -> ListCollaborationAnalysisTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationAnalysisTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationanalysistemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collaboration_configured_audience_model_associations"]
    ) -> ListCollaborationConfiguredAudienceModelAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationConfiguredAudienceModelAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationconfiguredaudiencemodelassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collaboration_privacy_budget_templates"]
    ) -> ListCollaborationPrivacyBudgetTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgetTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgettemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collaboration_privacy_budgets"]
    ) -> ListCollaborationPrivacyBudgetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborationPrivacyBudgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationprivacybudgetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collaborations"]
    ) -> ListCollaborationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListCollaborations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listcollaborationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configured_audience_model_associations"]
    ) -> ListConfiguredAudienceModelAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredAudienceModelAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredaudiencemodelassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configured_table_associations"]
    ) -> ListConfiguredTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTableAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtableassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configured_tables"]
    ) -> ListConfiguredTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListConfiguredTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listconfiguredtablespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_memberships"]
    ) -> ListMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listmembershipspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_privacy_budget_templates"]
    ) -> ListPrivacyBudgetTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgetTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgettemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_privacy_budgets"]
    ) -> ListPrivacyBudgetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListPrivacyBudgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprivacybudgetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protected_queries"]
    ) -> ListProtectedQueriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListProtectedQueries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listprotectedqueriespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanrooms.html#CleanRoomsService.Paginator.ListSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/paginators.html#listschemaspaginator)
        """
