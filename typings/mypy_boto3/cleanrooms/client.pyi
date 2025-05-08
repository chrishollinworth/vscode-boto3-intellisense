"""
Type annotations for cleanrooms service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cleanrooms.client import CleanRoomsServiceClient

    session = Session()
    client: CleanRoomsServiceClient = session.client("cleanrooms")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAnalysisTemplatesPaginator,
    ListCollaborationAnalysisTemplatesPaginator,
    ListCollaborationConfiguredAudienceModelAssociationsPaginator,
    ListCollaborationIdNamespaceAssociationsPaginator,
    ListCollaborationPrivacyBudgetsPaginator,
    ListCollaborationPrivacyBudgetTemplatesPaginator,
    ListCollaborationsPaginator,
    ListConfiguredAudienceModelAssociationsPaginator,
    ListConfiguredTableAssociationsPaginator,
    ListConfiguredTablesPaginator,
    ListIdMappingTablesPaginator,
    ListIdNamespaceAssociationsPaginator,
    ListMembershipsPaginator,
    ListMembersPaginator,
    ListPrivacyBudgetsPaginator,
    ListPrivacyBudgetTemplatesPaginator,
    ListProtectedJobsPaginator,
    ListProtectedQueriesPaginator,
    ListSchemasPaginator,
)
from .type_defs import (
    BatchGetCollaborationAnalysisTemplateInputTypeDef,
    BatchGetCollaborationAnalysisTemplateOutputTypeDef,
    BatchGetSchemaAnalysisRuleInputTypeDef,
    BatchGetSchemaAnalysisRuleOutputTypeDef,
    BatchGetSchemaInputTypeDef,
    BatchGetSchemaOutputTypeDef,
    CreateAnalysisTemplateInputTypeDef,
    CreateAnalysisTemplateOutputTypeDef,
    CreateCollaborationInputTypeDef,
    CreateCollaborationOutputTypeDef,
    CreateConfiguredAudienceModelAssociationInputTypeDef,
    CreateConfiguredAudienceModelAssociationOutputTypeDef,
    CreateConfiguredTableAnalysisRuleInputTypeDef,
    CreateConfiguredTableAnalysisRuleOutputTypeDef,
    CreateConfiguredTableAssociationAnalysisRuleInputTypeDef,
    CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef,
    CreateConfiguredTableAssociationInputTypeDef,
    CreateConfiguredTableAssociationOutputTypeDef,
    CreateConfiguredTableInputTypeDef,
    CreateConfiguredTableOutputTypeDef,
    CreateIdMappingTableInputTypeDef,
    CreateIdMappingTableOutputTypeDef,
    CreateIdNamespaceAssociationInputTypeDef,
    CreateIdNamespaceAssociationOutputTypeDef,
    CreateMembershipInputTypeDef,
    CreateMembershipOutputTypeDef,
    CreatePrivacyBudgetTemplateInputTypeDef,
    CreatePrivacyBudgetTemplateOutputTypeDef,
    DeleteAnalysisTemplateInputTypeDef,
    DeleteCollaborationInputTypeDef,
    DeleteConfiguredAudienceModelAssociationInputTypeDef,
    DeleteConfiguredTableAnalysisRuleInputTypeDef,
    DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef,
    DeleteConfiguredTableAssociationInputTypeDef,
    DeleteConfiguredTableInputTypeDef,
    DeleteIdMappingTableInputTypeDef,
    DeleteIdNamespaceAssociationInputTypeDef,
    DeleteMemberInputTypeDef,
    DeleteMembershipInputTypeDef,
    DeletePrivacyBudgetTemplateInputTypeDef,
    GetAnalysisTemplateInputTypeDef,
    GetAnalysisTemplateOutputTypeDef,
    GetCollaborationAnalysisTemplateInputTypeDef,
    GetCollaborationAnalysisTemplateOutputTypeDef,
    GetCollaborationConfiguredAudienceModelAssociationInputTypeDef,
    GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef,
    GetCollaborationIdNamespaceAssociationInputTypeDef,
    GetCollaborationIdNamespaceAssociationOutputTypeDef,
    GetCollaborationInputTypeDef,
    GetCollaborationOutputTypeDef,
    GetCollaborationPrivacyBudgetTemplateInputTypeDef,
    GetCollaborationPrivacyBudgetTemplateOutputTypeDef,
    GetConfiguredAudienceModelAssociationInputTypeDef,
    GetConfiguredAudienceModelAssociationOutputTypeDef,
    GetConfiguredTableAnalysisRuleInputTypeDef,
    GetConfiguredTableAnalysisRuleOutputTypeDef,
    GetConfiguredTableAssociationAnalysisRuleInputTypeDef,
    GetConfiguredTableAssociationAnalysisRuleOutputTypeDef,
    GetConfiguredTableAssociationInputTypeDef,
    GetConfiguredTableAssociationOutputTypeDef,
    GetConfiguredTableInputTypeDef,
    GetConfiguredTableOutputTypeDef,
    GetIdMappingTableInputTypeDef,
    GetIdMappingTableOutputTypeDef,
    GetIdNamespaceAssociationInputTypeDef,
    GetIdNamespaceAssociationOutputTypeDef,
    GetMembershipInputTypeDef,
    GetMembershipOutputTypeDef,
    GetPrivacyBudgetTemplateInputTypeDef,
    GetPrivacyBudgetTemplateOutputTypeDef,
    GetProtectedJobInputTypeDef,
    GetProtectedJobOutputTypeDef,
    GetProtectedQueryInputTypeDef,
    GetProtectedQueryOutputTypeDef,
    GetSchemaAnalysisRuleInputTypeDef,
    GetSchemaAnalysisRuleOutputTypeDef,
    GetSchemaInputTypeDef,
    GetSchemaOutputTypeDef,
    ListAnalysisTemplatesInputTypeDef,
    ListAnalysisTemplatesOutputTypeDef,
    ListCollaborationAnalysisTemplatesInputTypeDef,
    ListCollaborationAnalysisTemplatesOutputTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef,
    ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef,
    ListCollaborationIdNamespaceAssociationsInputTypeDef,
    ListCollaborationIdNamespaceAssociationsOutputTypeDef,
    ListCollaborationPrivacyBudgetsInputTypeDef,
    ListCollaborationPrivacyBudgetsOutputTypeDef,
    ListCollaborationPrivacyBudgetTemplatesInputTypeDef,
    ListCollaborationPrivacyBudgetTemplatesOutputTypeDef,
    ListCollaborationsInputTypeDef,
    ListCollaborationsOutputTypeDef,
    ListConfiguredAudienceModelAssociationsInputTypeDef,
    ListConfiguredAudienceModelAssociationsOutputTypeDef,
    ListConfiguredTableAssociationsInputTypeDef,
    ListConfiguredTableAssociationsOutputTypeDef,
    ListConfiguredTablesInputTypeDef,
    ListConfiguredTablesOutputTypeDef,
    ListIdMappingTablesInputTypeDef,
    ListIdMappingTablesOutputTypeDef,
    ListIdNamespaceAssociationsInputTypeDef,
    ListIdNamespaceAssociationsOutputTypeDef,
    ListMembershipsInputTypeDef,
    ListMembershipsOutputTypeDef,
    ListMembersInputTypeDef,
    ListMembersOutputTypeDef,
    ListPrivacyBudgetsInputTypeDef,
    ListPrivacyBudgetsOutputTypeDef,
    ListPrivacyBudgetTemplatesInputTypeDef,
    ListPrivacyBudgetTemplatesOutputTypeDef,
    ListProtectedJobsInputTypeDef,
    ListProtectedJobsOutputTypeDef,
    ListProtectedQueriesInputTypeDef,
    ListProtectedQueriesOutputTypeDef,
    ListSchemasInputTypeDef,
    ListSchemasOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PopulateIdMappingTableInputTypeDef,
    PopulateIdMappingTableOutputTypeDef,
    PreviewPrivacyImpactInputTypeDef,
    PreviewPrivacyImpactOutputTypeDef,
    StartProtectedJobInputTypeDef,
    StartProtectedJobOutputTypeDef,
    StartProtectedQueryInputTypeDef,
    StartProtectedQueryOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateAnalysisTemplateInputTypeDef,
    UpdateAnalysisTemplateOutputTypeDef,
    UpdateCollaborationInputTypeDef,
    UpdateCollaborationOutputTypeDef,
    UpdateConfiguredAudienceModelAssociationInputTypeDef,
    UpdateConfiguredAudienceModelAssociationOutputTypeDef,
    UpdateConfiguredTableAnalysisRuleInputTypeDef,
    UpdateConfiguredTableAnalysisRuleOutputTypeDef,
    UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef,
    UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef,
    UpdateConfiguredTableAssociationInputTypeDef,
    UpdateConfiguredTableAssociationOutputTypeDef,
    UpdateConfiguredTableInputTypeDef,
    UpdateConfiguredTableOutputTypeDef,
    UpdateIdMappingTableInputTypeDef,
    UpdateIdMappingTableOutputTypeDef,
    UpdateIdNamespaceAssociationInputTypeDef,
    UpdateIdNamespaceAssociationOutputTypeDef,
    UpdateMembershipInputTypeDef,
    UpdateMembershipOutputTypeDef,
    UpdatePrivacyBudgetTemplateInputTypeDef,
    UpdatePrivacyBudgetTemplateOutputTypeDef,
    UpdateProtectedJobInputTypeDef,
    UpdateProtectedJobOutputTypeDef,
    UpdateProtectedQueryInputTypeDef,
    UpdateProtectedQueryOutputTypeDef,
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

__all__ = ("CleanRoomsServiceClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms.html#CleanRoomsService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CleanRoomsServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms.html#CleanRoomsService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#generate_presigned_url)
        """

    def batch_get_collaboration_analysis_template(
        self, **kwargs: Unpack[BatchGetCollaborationAnalysisTemplateInputTypeDef]
    ) -> BatchGetCollaborationAnalysisTemplateOutputTypeDef:
        """
        Retrieves multiple analysis templates within a collaboration by their Amazon
        Resource Names (ARNs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/batch_get_collaboration_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#batch_get_collaboration_analysis_template)
        """

    def batch_get_schema(
        self, **kwargs: Unpack[BatchGetSchemaInputTypeDef]
    ) -> BatchGetSchemaOutputTypeDef:
        """
        Retrieves multiple schemas by their identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/batch_get_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#batch_get_schema)
        """

    def batch_get_schema_analysis_rule(
        self, **kwargs: Unpack[BatchGetSchemaAnalysisRuleInputTypeDef]
    ) -> BatchGetSchemaAnalysisRuleOutputTypeDef:
        """
        Retrieves multiple analysis rule schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/batch_get_schema_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#batch_get_schema_analysis_rule)
        """

    def create_analysis_template(
        self, **kwargs: Unpack[CreateAnalysisTemplateInputTypeDef]
    ) -> CreateAnalysisTemplateOutputTypeDef:
        """
        Creates a new analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_analysis_template)
        """

    def create_collaboration(
        self, **kwargs: Unpack[CreateCollaborationInputTypeDef]
    ) -> CreateCollaborationOutputTypeDef:
        """
        Creates a new collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_collaboration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_collaboration)
        """

    def create_configured_audience_model_association(
        self, **kwargs: Unpack[CreateConfiguredAudienceModelAssociationInputTypeDef]
    ) -> CreateConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Provides the details necessary to create a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_configured_audience_model_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_configured_audience_model_association)
        """

    def create_configured_table(
        self, **kwargs: Unpack[CreateConfiguredTableInputTypeDef]
    ) -> CreateConfiguredTableOutputTypeDef:
        """
        Creates a new configured table resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_configured_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_configured_table)
        """

    def create_configured_table_analysis_rule(
        self, **kwargs: Unpack[CreateConfiguredTableAnalysisRuleInputTypeDef]
    ) -> CreateConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Creates a new analysis rule for a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_configured_table_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_configured_table_analysis_rule)
        """

    def create_configured_table_association(
        self, **kwargs: Unpack[CreateConfiguredTableAssociationInputTypeDef]
    ) -> CreateConfiguredTableAssociationOutputTypeDef:
        """
        Creates a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_configured_table_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_configured_table_association)
        """

    def create_configured_table_association_analysis_rule(
        self, **kwargs: Unpack[CreateConfiguredTableAssociationAnalysisRuleInputTypeDef]
    ) -> CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef:
        """
        Creates a new analysis rule for an associated configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_configured_table_association_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_configured_table_association_analysis_rule)
        """

    def create_id_mapping_table(
        self, **kwargs: Unpack[CreateIdMappingTableInputTypeDef]
    ) -> CreateIdMappingTableOutputTypeDef:
        """
        Creates an ID mapping table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_id_mapping_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_id_mapping_table)
        """

    def create_id_namespace_association(
        self, **kwargs: Unpack[CreateIdNamespaceAssociationInputTypeDef]
    ) -> CreateIdNamespaceAssociationOutputTypeDef:
        """
        Creates an ID namespace association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_id_namespace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_id_namespace_association)
        """

    def create_membership(
        self, **kwargs: Unpack[CreateMembershipInputTypeDef]
    ) -> CreateMembershipOutputTypeDef:
        """
        Creates a membership for a specific collaboration identifier and joins the
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_membership)
        """

    def create_privacy_budget_template(
        self, **kwargs: Unpack[CreatePrivacyBudgetTemplateInputTypeDef]
    ) -> CreatePrivacyBudgetTemplateOutputTypeDef:
        """
        Creates a privacy budget template for a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/create_privacy_budget_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#create_privacy_budget_template)
        """

    def delete_analysis_template(
        self, **kwargs: Unpack[DeleteAnalysisTemplateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_analysis_template)
        """

    def delete_collaboration(
        self, **kwargs: Unpack[DeleteCollaborationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_collaboration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_collaboration)
        """

    def delete_configured_audience_model_association(
        self, **kwargs: Unpack[DeleteConfiguredAudienceModelAssociationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides the information necessary to delete a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_configured_audience_model_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_configured_audience_model_association)
        """

    def delete_configured_table(
        self, **kwargs: Unpack[DeleteConfiguredTableInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_configured_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_configured_table)
        """

    def delete_configured_table_analysis_rule(
        self, **kwargs: Unpack[DeleteConfiguredTableAnalysisRuleInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_configured_table_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_configured_table_analysis_rule)
        """

    def delete_configured_table_association(
        self, **kwargs: Unpack[DeleteConfiguredTableAssociationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_configured_table_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_configured_table_association)
        """

    def delete_configured_table_association_analysis_rule(
        self, **kwargs: Unpack[DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an analysis rule for a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_configured_table_association_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_configured_table_association_analysis_rule)
        """

    def delete_id_mapping_table(
        self, **kwargs: Unpack[DeleteIdMappingTableInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an ID mapping table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_id_mapping_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_id_mapping_table)
        """

    def delete_id_namespace_association(
        self, **kwargs: Unpack[DeleteIdNamespaceAssociationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an ID namespace association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_id_namespace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_id_namespace_association)
        """

    def delete_member(self, **kwargs: Unpack[DeleteMemberInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified member from a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_member.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_member)
        """

    def delete_membership(self, **kwargs: Unpack[DeleteMembershipInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_membership)
        """

    def delete_privacy_budget_template(
        self, **kwargs: Unpack[DeletePrivacyBudgetTemplateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a privacy budget template for a specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/delete_privacy_budget_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#delete_privacy_budget_template)
        """

    def get_analysis_template(
        self, **kwargs: Unpack[GetAnalysisTemplateInputTypeDef]
    ) -> GetAnalysisTemplateOutputTypeDef:
        """
        Retrieves an analysis template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_analysis_template)
        """

    def get_collaboration(
        self, **kwargs: Unpack[GetCollaborationInputTypeDef]
    ) -> GetCollaborationOutputTypeDef:
        """
        Returns metadata about a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_collaboration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_collaboration)
        """

    def get_collaboration_analysis_template(
        self, **kwargs: Unpack[GetCollaborationAnalysisTemplateInputTypeDef]
    ) -> GetCollaborationAnalysisTemplateOutputTypeDef:
        """
        Retrieves an analysis template within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_collaboration_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_collaboration_analysis_template)
        """

    def get_collaboration_configured_audience_model_association(
        self, **kwargs: Unpack[GetCollaborationConfiguredAudienceModelAssociationInputTypeDef]
    ) -> GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Retrieves a configured audience model association within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_collaboration_configured_audience_model_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_collaboration_configured_audience_model_association)
        """

    def get_collaboration_id_namespace_association(
        self, **kwargs: Unpack[GetCollaborationIdNamespaceAssociationInputTypeDef]
    ) -> GetCollaborationIdNamespaceAssociationOutputTypeDef:
        """
        Retrieves an ID namespace association from a specific collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_collaboration_id_namespace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_collaboration_id_namespace_association)
        """

    def get_collaboration_privacy_budget_template(
        self, **kwargs: Unpack[GetCollaborationPrivacyBudgetTemplateInputTypeDef]
    ) -> GetCollaborationPrivacyBudgetTemplateOutputTypeDef:
        """
        Returns details about a specified privacy budget template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_collaboration_privacy_budget_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_collaboration_privacy_budget_template)
        """

    def get_configured_audience_model_association(
        self, **kwargs: Unpack[GetConfiguredAudienceModelAssociationInputTypeDef]
    ) -> GetConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Returns information about a configured audience model association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_configured_audience_model_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_configured_audience_model_association)
        """

    def get_configured_table(
        self, **kwargs: Unpack[GetConfiguredTableInputTypeDef]
    ) -> GetConfiguredTableOutputTypeDef:
        """
        Retrieves a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_configured_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_configured_table)
        """

    def get_configured_table_analysis_rule(
        self, **kwargs: Unpack[GetConfiguredTableAnalysisRuleInputTypeDef]
    ) -> GetConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Retrieves a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_configured_table_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_configured_table_analysis_rule)
        """

    def get_configured_table_association(
        self, **kwargs: Unpack[GetConfiguredTableAssociationInputTypeDef]
    ) -> GetConfiguredTableAssociationOutputTypeDef:
        """
        Retrieves a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_configured_table_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_configured_table_association)
        """

    def get_configured_table_association_analysis_rule(
        self, **kwargs: Unpack[GetConfiguredTableAssociationAnalysisRuleInputTypeDef]
    ) -> GetConfiguredTableAssociationAnalysisRuleOutputTypeDef:
        """
        Retrieves the analysis rule for a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_configured_table_association_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_configured_table_association_analysis_rule)
        """

    def get_id_mapping_table(
        self, **kwargs: Unpack[GetIdMappingTableInputTypeDef]
    ) -> GetIdMappingTableOutputTypeDef:
        """
        Retrieves an ID mapping table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_id_mapping_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_id_mapping_table)
        """

    def get_id_namespace_association(
        self, **kwargs: Unpack[GetIdNamespaceAssociationInputTypeDef]
    ) -> GetIdNamespaceAssociationOutputTypeDef:
        """
        Retrieves an ID namespace association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_id_namespace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_id_namespace_association)
        """

    def get_membership(
        self, **kwargs: Unpack[GetMembershipInputTypeDef]
    ) -> GetMembershipOutputTypeDef:
        """
        Retrieves a specified membership for an identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_membership)
        """

    def get_privacy_budget_template(
        self, **kwargs: Unpack[GetPrivacyBudgetTemplateInputTypeDef]
    ) -> GetPrivacyBudgetTemplateOutputTypeDef:
        """
        Returns details for a specified privacy budget template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_privacy_budget_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_privacy_budget_template)
        """

    def get_protected_job(
        self, **kwargs: Unpack[GetProtectedJobInputTypeDef]
    ) -> GetProtectedJobOutputTypeDef:
        """
        Returns job processing metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_protected_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_protected_job)
        """

    def get_protected_query(
        self, **kwargs: Unpack[GetProtectedQueryInputTypeDef]
    ) -> GetProtectedQueryOutputTypeDef:
        """
        Returns query processing metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_protected_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_protected_query)
        """

    def get_schema(self, **kwargs: Unpack[GetSchemaInputTypeDef]) -> GetSchemaOutputTypeDef:
        """
        Retrieves the schema for a relation within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_schema)
        """

    def get_schema_analysis_rule(
        self, **kwargs: Unpack[GetSchemaAnalysisRuleInputTypeDef]
    ) -> GetSchemaAnalysisRuleOutputTypeDef:
        """
        Retrieves a schema analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_schema_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_schema_analysis_rule)
        """

    def list_analysis_templates(
        self, **kwargs: Unpack[ListAnalysisTemplatesInputTypeDef]
    ) -> ListAnalysisTemplatesOutputTypeDef:
        """
        Lists analysis templates that the caller owns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_analysis_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_analysis_templates)
        """

    def list_collaboration_analysis_templates(
        self, **kwargs: Unpack[ListCollaborationAnalysisTemplatesInputTypeDef]
    ) -> ListCollaborationAnalysisTemplatesOutputTypeDef:
        """
        Lists analysis templates within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaboration_analysis_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaboration_analysis_templates)
        """

    def list_collaboration_configured_audience_model_associations(
        self, **kwargs: Unpack[ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef]
    ) -> ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef:
        """
        Lists configured audience model associations within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaboration_configured_audience_model_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaboration_configured_audience_model_associations)
        """

    def list_collaboration_id_namespace_associations(
        self, **kwargs: Unpack[ListCollaborationIdNamespaceAssociationsInputTypeDef]
    ) -> ListCollaborationIdNamespaceAssociationsOutputTypeDef:
        """
        Returns a list of the ID namespace associations in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaboration_id_namespace_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaboration_id_namespace_associations)
        """

    def list_collaboration_privacy_budget_templates(
        self, **kwargs: Unpack[ListCollaborationPrivacyBudgetTemplatesInputTypeDef]
    ) -> ListCollaborationPrivacyBudgetTemplatesOutputTypeDef:
        """
        Returns an array that summarizes each privacy budget template in a specified
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaboration_privacy_budget_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaboration_privacy_budget_templates)
        """

    def list_collaboration_privacy_budgets(
        self, **kwargs: Unpack[ListCollaborationPrivacyBudgetsInputTypeDef]
    ) -> ListCollaborationPrivacyBudgetsOutputTypeDef:
        """
        Returns an array that summarizes each privacy budget in a specified
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaboration_privacy_budgets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaboration_privacy_budgets)
        """

    def list_collaborations(
        self, **kwargs: Unpack[ListCollaborationsInputTypeDef]
    ) -> ListCollaborationsOutputTypeDef:
        """
        Lists collaborations the caller owns, is active in, or has been invited to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_collaborations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_collaborations)
        """

    def list_configured_audience_model_associations(
        self, **kwargs: Unpack[ListConfiguredAudienceModelAssociationsInputTypeDef]
    ) -> ListConfiguredAudienceModelAssociationsOutputTypeDef:
        """
        Lists information about requested configured audience model associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_configured_audience_model_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_configured_audience_model_associations)
        """

    def list_configured_table_associations(
        self, **kwargs: Unpack[ListConfiguredTableAssociationsInputTypeDef]
    ) -> ListConfiguredTableAssociationsOutputTypeDef:
        """
        Lists configured table associations for a membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_configured_table_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_configured_table_associations)
        """

    def list_configured_tables(
        self, **kwargs: Unpack[ListConfiguredTablesInputTypeDef]
    ) -> ListConfiguredTablesOutputTypeDef:
        """
        Lists configured tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_configured_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_configured_tables)
        """

    def list_id_mapping_tables(
        self, **kwargs: Unpack[ListIdMappingTablesInputTypeDef]
    ) -> ListIdMappingTablesOutputTypeDef:
        """
        Returns a list of ID mapping tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_id_mapping_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_id_mapping_tables)
        """

    def list_id_namespace_associations(
        self, **kwargs: Unpack[ListIdNamespaceAssociationsInputTypeDef]
    ) -> ListIdNamespaceAssociationsOutputTypeDef:
        """
        Returns a list of ID namespace associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_id_namespace_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_id_namespace_associations)
        """

    def list_members(self, **kwargs: Unpack[ListMembersInputTypeDef]) -> ListMembersOutputTypeDef:
        """
        Lists all members within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_members)
        """

    def list_memberships(
        self, **kwargs: Unpack[ListMembershipsInputTypeDef]
    ) -> ListMembershipsOutputTypeDef:
        """
        Lists all memberships resources within the caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_memberships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_memberships)
        """

    def list_privacy_budget_templates(
        self, **kwargs: Unpack[ListPrivacyBudgetTemplatesInputTypeDef]
    ) -> ListPrivacyBudgetTemplatesOutputTypeDef:
        """
        Returns detailed information about the privacy budget templates in a specified
        membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_privacy_budget_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_privacy_budget_templates)
        """

    def list_privacy_budgets(
        self, **kwargs: Unpack[ListPrivacyBudgetsInputTypeDef]
    ) -> ListPrivacyBudgetsOutputTypeDef:
        """
        Returns detailed information about the privacy budgets in a specified
        membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_privacy_budgets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_privacy_budgets)
        """

    def list_protected_jobs(
        self, **kwargs: Unpack[ListProtectedJobsInputTypeDef]
    ) -> ListProtectedJobsOutputTypeDef:
        """
        Lists protected jobs, sorted by most recent job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_protected_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_protected_jobs)
        """

    def list_protected_queries(
        self, **kwargs: Unpack[ListProtectedQueriesInputTypeDef]
    ) -> ListProtectedQueriesOutputTypeDef:
        """
        Lists protected queries, sorted by the most recent query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_protected_queries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_protected_queries)
        """

    def list_schemas(self, **kwargs: Unpack[ListSchemasInputTypeDef]) -> ListSchemasOutputTypeDef:
        """
        Lists the schemas for relations within a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_schemas)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists all of the tags that have been added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#list_tags_for_resource)
        """

    def populate_id_mapping_table(
        self, **kwargs: Unpack[PopulateIdMappingTableInputTypeDef]
    ) -> PopulateIdMappingTableOutputTypeDef:
        """
        Defines the information that's necessary to populate an ID mapping table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/populate_id_mapping_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#populate_id_mapping_table)
        """

    def preview_privacy_impact(
        self, **kwargs: Unpack[PreviewPrivacyImpactInputTypeDef]
    ) -> PreviewPrivacyImpactOutputTypeDef:
        """
        An estimate of the number of aggregation functions that the member who can
        query can run given epsilon and noise parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/preview_privacy_impact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#preview_privacy_impact)
        """

    def start_protected_job(
        self, **kwargs: Unpack[StartProtectedJobInputTypeDef]
    ) -> StartProtectedJobOutputTypeDef:
        """
        Creates a protected job that is started by Clean Rooms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/start_protected_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#start_protected_job)
        """

    def start_protected_query(
        self, **kwargs: Unpack[StartProtectedQueryInputTypeDef]
    ) -> StartProtectedQueryOutputTypeDef:
        """
        Creates a protected query that is started by Clean Rooms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/start_protected_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#start_protected_query)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#untag_resource)
        """

    def update_analysis_template(
        self, **kwargs: Unpack[UpdateAnalysisTemplateInputTypeDef]
    ) -> UpdateAnalysisTemplateOutputTypeDef:
        """
        Updates the analysis template metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_analysis_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_analysis_template)
        """

    def update_collaboration(
        self, **kwargs: Unpack[UpdateCollaborationInputTypeDef]
    ) -> UpdateCollaborationOutputTypeDef:
        """
        Updates collaboration metadata and can only be called by the collaboration
        owner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_collaboration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_collaboration)
        """

    def update_configured_audience_model_association(
        self, **kwargs: Unpack[UpdateConfiguredAudienceModelAssociationInputTypeDef]
    ) -> UpdateConfiguredAudienceModelAssociationOutputTypeDef:
        """
        Provides the details necessary to update a configured audience model
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_configured_audience_model_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_configured_audience_model_association)
        """

    def update_configured_table(
        self, **kwargs: Unpack[UpdateConfiguredTableInputTypeDef]
    ) -> UpdateConfiguredTableOutputTypeDef:
        """
        Updates a configured table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_configured_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_configured_table)
        """

    def update_configured_table_analysis_rule(
        self, **kwargs: Unpack[UpdateConfiguredTableAnalysisRuleInputTypeDef]
    ) -> UpdateConfiguredTableAnalysisRuleOutputTypeDef:
        """
        Updates a configured table analysis rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_configured_table_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_configured_table_analysis_rule)
        """

    def update_configured_table_association(
        self, **kwargs: Unpack[UpdateConfiguredTableAssociationInputTypeDef]
    ) -> UpdateConfiguredTableAssociationOutputTypeDef:
        """
        Updates a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_configured_table_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_configured_table_association)
        """

    def update_configured_table_association_analysis_rule(
        self, **kwargs: Unpack[UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef]
    ) -> UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef:
        """
        Updates the analysis rule for a configured table association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_configured_table_association_analysis_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_configured_table_association_analysis_rule)
        """

    def update_id_mapping_table(
        self, **kwargs: Unpack[UpdateIdMappingTableInputTypeDef]
    ) -> UpdateIdMappingTableOutputTypeDef:
        """
        Provides the details that are necessary to update an ID mapping table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_id_mapping_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_id_mapping_table)
        """

    def update_id_namespace_association(
        self, **kwargs: Unpack[UpdateIdNamespaceAssociationInputTypeDef]
    ) -> UpdateIdNamespaceAssociationOutputTypeDef:
        """
        Provides the details that are necessary to update an ID namespace association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_id_namespace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_id_namespace_association)
        """

    def update_membership(
        self, **kwargs: Unpack[UpdateMembershipInputTypeDef]
    ) -> UpdateMembershipOutputTypeDef:
        """
        Updates a membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_membership)
        """

    def update_privacy_budget_template(
        self, **kwargs: Unpack[UpdatePrivacyBudgetTemplateInputTypeDef]
    ) -> UpdatePrivacyBudgetTemplateOutputTypeDef:
        """
        Updates the privacy budget template for the specified membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_privacy_budget_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_privacy_budget_template)
        """

    def update_protected_job(
        self, **kwargs: Unpack[UpdateProtectedJobInputTypeDef]
    ) -> UpdateProtectedJobOutputTypeDef:
        """
        Updates the processing of a currently running job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_protected_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_protected_job)
        """

    def update_protected_query(
        self, **kwargs: Unpack[UpdateProtectedQueryInputTypeDef]
    ) -> UpdateProtectedQueryOutputTypeDef:
        """
        Updates the processing of a currently running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/update_protected_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#update_protected_query)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_analysis_templates"]
    ) -> ListAnalysisTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_analysis_templates"]
    ) -> ListCollaborationAnalysisTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_configured_audience_model_associations"]
    ) -> ListCollaborationConfiguredAudienceModelAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_id_namespace_associations"]
    ) -> ListCollaborationIdNamespaceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_privacy_budget_templates"]
    ) -> ListCollaborationPrivacyBudgetTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_privacy_budgets"]
    ) -> ListCollaborationPrivacyBudgetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaborations"]
    ) -> ListCollaborationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_audience_model_associations"]
    ) -> ListConfiguredAudienceModelAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_table_associations"]
    ) -> ListConfiguredTableAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_tables"]
    ) -> ListConfiguredTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_id_mapping_tables"]
    ) -> ListIdMappingTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_id_namespace_associations"]
    ) -> ListIdNamespaceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_members"]
    ) -> ListMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_memberships"]
    ) -> ListMembershipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_privacy_budget_templates"]
    ) -> ListPrivacyBudgetTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_privacy_budgets"]
    ) -> ListPrivacyBudgetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protected_jobs"]
    ) -> ListProtectedJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protected_queries"]
    ) -> ListProtectedQueriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schemas"]
    ) -> ListSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/client/#get_paginator)
        """
