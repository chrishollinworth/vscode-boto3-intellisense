"""
Type annotations for bedrock service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock.client import BedrockClient
    from mypy_boto3_bedrock.paginator import (
        ListAutomatedReasoningPoliciesPaginator,
        ListAutomatedReasoningPolicyBuildWorkflowsPaginator,
        ListAutomatedReasoningPolicyTestCasesPaginator,
        ListAutomatedReasoningPolicyTestResultsPaginator,
        ListCustomModelDeploymentsPaginator,
        ListCustomModelsPaginator,
        ListEnforcedGuardrailsConfigurationPaginator,
        ListEvaluationJobsPaginator,
        ListGuardrailsPaginator,
        ListImportedModelsPaginator,
        ListInferenceProfilesPaginator,
        ListMarketplaceModelEndpointsPaginator,
        ListModelCopyJobsPaginator,
        ListModelCustomizationJobsPaginator,
        ListModelImportJobsPaginator,
        ListModelInvocationJobsPaginator,
        ListPromptRoutersPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    session = Session()
    client: BedrockClient = session.client("bedrock")

    list_automated_reasoning_policies_paginator: ListAutomatedReasoningPoliciesPaginator = client.get_paginator("list_automated_reasoning_policies")
    list_automated_reasoning_policy_build_workflows_paginator: ListAutomatedReasoningPolicyBuildWorkflowsPaginator = client.get_paginator("list_automated_reasoning_policy_build_workflows")
    list_automated_reasoning_policy_test_cases_paginator: ListAutomatedReasoningPolicyTestCasesPaginator = client.get_paginator("list_automated_reasoning_policy_test_cases")
    list_automated_reasoning_policy_test_results_paginator: ListAutomatedReasoningPolicyTestResultsPaginator = client.get_paginator("list_automated_reasoning_policy_test_results")
    list_custom_model_deployments_paginator: ListCustomModelDeploymentsPaginator = client.get_paginator("list_custom_model_deployments")
    list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
    list_enforced_guardrails_configuration_paginator: ListEnforcedGuardrailsConfigurationPaginator = client.get_paginator("list_enforced_guardrails_configuration")
    list_evaluation_jobs_paginator: ListEvaluationJobsPaginator = client.get_paginator("list_evaluation_jobs")
    list_guardrails_paginator: ListGuardrailsPaginator = client.get_paginator("list_guardrails")
    list_imported_models_paginator: ListImportedModelsPaginator = client.get_paginator("list_imported_models")
    list_inference_profiles_paginator: ListInferenceProfilesPaginator = client.get_paginator("list_inference_profiles")
    list_marketplace_model_endpoints_paginator: ListMarketplaceModelEndpointsPaginator = client.get_paginator("list_marketplace_model_endpoints")
    list_model_copy_jobs_paginator: ListModelCopyJobsPaginator = client.get_paginator("list_model_copy_jobs")
    list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
    list_model_import_jobs_paginator: ListModelImportJobsPaginator = client.get_paginator("list_model_import_jobs")
    list_model_invocation_jobs_paginator: ListModelInvocationJobsPaginator = client.get_paginator("list_model_invocation_jobs")
    list_prompt_routers_paginator: ListPromptRoutersPaginator = client.get_paginator("list_prompt_routers")
    list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAutomatedReasoningPoliciesRequestPaginateTypeDef,
    ListAutomatedReasoningPoliciesResponseTypeDef,
    ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginateTypeDef,
    ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef,
    ListAutomatedReasoningPolicyTestCasesRequestPaginateTypeDef,
    ListAutomatedReasoningPolicyTestCasesResponseTypeDef,
    ListAutomatedReasoningPolicyTestResultsRequestPaginateTypeDef,
    ListAutomatedReasoningPolicyTestResultsResponseTypeDef,
    ListCustomModelDeploymentsRequestPaginateTypeDef,
    ListCustomModelDeploymentsResponseTypeDef,
    ListCustomModelsRequestPaginateTypeDef,
    ListCustomModelsResponseTypeDef,
    ListEnforcedGuardrailsConfigurationRequestPaginateTypeDef,
    ListEnforcedGuardrailsConfigurationResponseTypeDef,
    ListEvaluationJobsRequestPaginateTypeDef,
    ListEvaluationJobsResponseTypeDef,
    ListGuardrailsRequestPaginateTypeDef,
    ListGuardrailsResponseTypeDef,
    ListImportedModelsRequestPaginateTypeDef,
    ListImportedModelsResponseTypeDef,
    ListInferenceProfilesRequestPaginateTypeDef,
    ListInferenceProfilesResponseTypeDef,
    ListMarketplaceModelEndpointsRequestPaginateTypeDef,
    ListMarketplaceModelEndpointsResponseTypeDef,
    ListModelCopyJobsRequestPaginateTypeDef,
    ListModelCopyJobsResponseTypeDef,
    ListModelCustomizationJobsRequestPaginateTypeDef,
    ListModelCustomizationJobsResponseTypeDef,
    ListModelImportJobsRequestPaginateTypeDef,
    ListModelImportJobsResponseTypeDef,
    ListModelInvocationJobsRequestPaginateTypeDef,
    ListModelInvocationJobsResponseTypeDef,
    ListPromptRoutersRequestPaginateTypeDef,
    ListPromptRoutersResponseTypeDef,
    ListProvisionedModelThroughputsRequestPaginateTypeDef,
    ListProvisionedModelThroughputsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAutomatedReasoningPoliciesPaginator",
    "ListAutomatedReasoningPolicyBuildWorkflowsPaginator",
    "ListAutomatedReasoningPolicyTestCasesPaginator",
    "ListAutomatedReasoningPolicyTestResultsPaginator",
    "ListCustomModelDeploymentsPaginator",
    "ListCustomModelsPaginator",
    "ListEnforcedGuardrailsConfigurationPaginator",
    "ListEvaluationJobsPaginator",
    "ListGuardrailsPaginator",
    "ListImportedModelsPaginator",
    "ListInferenceProfilesPaginator",
    "ListMarketplaceModelEndpointsPaginator",
    "ListModelCopyJobsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListModelImportJobsPaginator",
    "ListModelInvocationJobsPaginator",
    "ListPromptRoutersPaginator",
    "ListProvisionedModelThroughputsPaginator",
)

if TYPE_CHECKING:
    _ListAutomatedReasoningPoliciesPaginatorBase = Paginator[
        ListAutomatedReasoningPoliciesResponseTypeDef
    ]
else:
    _ListAutomatedReasoningPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomatedReasoningPoliciesPaginator(_ListAutomatedReasoningPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicies.html#Bedrock.Paginator.ListAutomatedReasoningPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomatedReasoningPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomatedReasoningPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicies.html#Bedrock.Paginator.ListAutomatedReasoningPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListAutomatedReasoningPolicyBuildWorkflowsPaginatorBase = Paginator[
        ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef
    ]
else:
    _ListAutomatedReasoningPolicyBuildWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomatedReasoningPolicyBuildWorkflowsPaginator(
    _ListAutomatedReasoningPolicyBuildWorkflowsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyBuildWorkflows.html#Bedrock.Paginator.ListAutomatedReasoningPolicyBuildWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicybuildworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyBuildWorkflows.html#Bedrock.Paginator.ListAutomatedReasoningPolicyBuildWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicybuildworkflowspaginator)
        """

if TYPE_CHECKING:
    _ListAutomatedReasoningPolicyTestCasesPaginatorBase = Paginator[
        ListAutomatedReasoningPolicyTestCasesResponseTypeDef
    ]
else:
    _ListAutomatedReasoningPolicyTestCasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomatedReasoningPolicyTestCasesPaginator(
    _ListAutomatedReasoningPolicyTestCasesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyTestCases.html#Bedrock.Paginator.ListAutomatedReasoningPolicyTestCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicytestcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyTestCasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomatedReasoningPolicyTestCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyTestCases.html#Bedrock.Paginator.ListAutomatedReasoningPolicyTestCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicytestcasespaginator)
        """

if TYPE_CHECKING:
    _ListAutomatedReasoningPolicyTestResultsPaginatorBase = Paginator[
        ListAutomatedReasoningPolicyTestResultsResponseTypeDef
    ]
else:
    _ListAutomatedReasoningPolicyTestResultsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomatedReasoningPolicyTestResultsPaginator(
    _ListAutomatedReasoningPolicyTestResultsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyTestResults.html#Bedrock.Paginator.ListAutomatedReasoningPolicyTestResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicytestresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyTestResultsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomatedReasoningPolicyTestResultsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListAutomatedReasoningPolicyTestResults.html#Bedrock.Paginator.ListAutomatedReasoningPolicyTestResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listautomatedreasoningpolicytestresultspaginator)
        """

if TYPE_CHECKING:
    _ListCustomModelDeploymentsPaginatorBase = Paginator[ListCustomModelDeploymentsResponseTypeDef]
else:
    _ListCustomModelDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomModelDeploymentsPaginator(_ListCustomModelDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListCustomModelDeployments.html#Bedrock.Paginator.ListCustomModelDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listcustommodeldeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomModelDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomModelDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListCustomModelDeployments.html#Bedrock.Paginator.ListCustomModelDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listcustommodeldeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListCustomModelsPaginatorBase = Paginator[ListCustomModelsResponseTypeDef]
else:
    _ListCustomModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomModelsPaginator(_ListCustomModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListCustomModels.html#Bedrock.Paginator.ListCustomModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listcustommodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListCustomModels.html#Bedrock.Paginator.ListCustomModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listcustommodelspaginator)
        """

if TYPE_CHECKING:
    _ListEnforcedGuardrailsConfigurationPaginatorBase = Paginator[
        ListEnforcedGuardrailsConfigurationResponseTypeDef
    ]
else:
    _ListEnforcedGuardrailsConfigurationPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnforcedGuardrailsConfigurationPaginator(
    _ListEnforcedGuardrailsConfigurationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListEnforcedGuardrailsConfiguration.html#Bedrock.Paginator.ListEnforcedGuardrailsConfiguration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listenforcedguardrailsconfigurationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnforcedGuardrailsConfigurationRequestPaginateTypeDef]
    ) -> PageIterator[ListEnforcedGuardrailsConfigurationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListEnforcedGuardrailsConfiguration.html#Bedrock.Paginator.ListEnforcedGuardrailsConfiguration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listenforcedguardrailsconfigurationpaginator)
        """

if TYPE_CHECKING:
    _ListEvaluationJobsPaginatorBase = Paginator[ListEvaluationJobsResponseTypeDef]
else:
    _ListEvaluationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEvaluationJobsPaginator(_ListEvaluationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListEvaluationJobs.html#Bedrock.Paginator.ListEvaluationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listevaluationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEvaluationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListEvaluationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListEvaluationJobs.html#Bedrock.Paginator.ListEvaluationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listevaluationjobspaginator)
        """

if TYPE_CHECKING:
    _ListGuardrailsPaginatorBase = Paginator[ListGuardrailsResponseTypeDef]
else:
    _ListGuardrailsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGuardrailsPaginator(_ListGuardrailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListGuardrails.html#Bedrock.Paginator.ListGuardrails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listguardrailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGuardrailsRequestPaginateTypeDef]
    ) -> PageIterator[ListGuardrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListGuardrails.html#Bedrock.Paginator.ListGuardrails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listguardrailspaginator)
        """

if TYPE_CHECKING:
    _ListImportedModelsPaginatorBase = Paginator[ListImportedModelsResponseTypeDef]
else:
    _ListImportedModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportedModelsPaginator(_ListImportedModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListImportedModels.html#Bedrock.Paginator.ListImportedModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listimportedmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportedModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListImportedModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListImportedModels.html#Bedrock.Paginator.ListImportedModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listimportedmodelspaginator)
        """

if TYPE_CHECKING:
    _ListInferenceProfilesPaginatorBase = Paginator[ListInferenceProfilesResponseTypeDef]
else:
    _ListInferenceProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInferenceProfilesPaginator(_ListInferenceProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListInferenceProfiles.html#Bedrock.Paginator.ListInferenceProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listinferenceprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInferenceProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListInferenceProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListInferenceProfiles.html#Bedrock.Paginator.ListInferenceProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listinferenceprofilespaginator)
        """

if TYPE_CHECKING:
    _ListMarketplaceModelEndpointsPaginatorBase = Paginator[
        ListMarketplaceModelEndpointsResponseTypeDef
    ]
else:
    _ListMarketplaceModelEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMarketplaceModelEndpointsPaginator(_ListMarketplaceModelEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListMarketplaceModelEndpoints.html#Bedrock.Paginator.ListMarketplaceModelEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmarketplacemodelendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMarketplaceModelEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListMarketplaceModelEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListMarketplaceModelEndpoints.html#Bedrock.Paginator.ListMarketplaceModelEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmarketplacemodelendpointspaginator)
        """

if TYPE_CHECKING:
    _ListModelCopyJobsPaginatorBase = Paginator[ListModelCopyJobsResponseTypeDef]
else:
    _ListModelCopyJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelCopyJobsPaginator(_ListModelCopyJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelCopyJobs.html#Bedrock.Paginator.ListModelCopyJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelcopyjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelCopyJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelCopyJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelCopyJobs.html#Bedrock.Paginator.ListModelCopyJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelcopyjobspaginator)
        """

if TYPE_CHECKING:
    _ListModelCustomizationJobsPaginatorBase = Paginator[ListModelCustomizationJobsResponseTypeDef]
else:
    _ListModelCustomizationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelCustomizationJobsPaginator(_ListModelCustomizationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelCustomizationJobs.html#Bedrock.Paginator.ListModelCustomizationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelcustomizationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelCustomizationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelCustomizationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelCustomizationJobs.html#Bedrock.Paginator.ListModelCustomizationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelcustomizationjobspaginator)
        """

if TYPE_CHECKING:
    _ListModelImportJobsPaginatorBase = Paginator[ListModelImportJobsResponseTypeDef]
else:
    _ListModelImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelImportJobsPaginator(_ListModelImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelImportJobs.html#Bedrock.Paginator.ListModelImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelImportJobs.html#Bedrock.Paginator.ListModelImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListModelInvocationJobsPaginatorBase = Paginator[ListModelInvocationJobsResponseTypeDef]
else:
    _ListModelInvocationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListModelInvocationJobsPaginator(_ListModelInvocationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelInvocationJobs.html#Bedrock.Paginator.ListModelInvocationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelinvocationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListModelInvocationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListModelInvocationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListModelInvocationJobs.html#Bedrock.Paginator.ListModelInvocationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listmodelinvocationjobspaginator)
        """

if TYPE_CHECKING:
    _ListPromptRoutersPaginatorBase = Paginator[ListPromptRoutersResponseTypeDef]
else:
    _ListPromptRoutersPaginatorBase = Paginator  # type: ignore[assignment]

class ListPromptRoutersPaginator(_ListPromptRoutersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListPromptRouters.html#Bedrock.Paginator.ListPromptRouters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listpromptrouterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPromptRoutersRequestPaginateTypeDef]
    ) -> PageIterator[ListPromptRoutersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListPromptRouters.html#Bedrock.Paginator.ListPromptRouters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listpromptrouterspaginator)
        """

if TYPE_CHECKING:
    _ListProvisionedModelThroughputsPaginatorBase = Paginator[
        ListProvisionedModelThroughputsResponseTypeDef
    ]
else:
    _ListProvisionedModelThroughputsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProvisionedModelThroughputsPaginator(_ListProvisionedModelThroughputsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListProvisionedModelThroughputs.html#Bedrock.Paginator.ListProvisionedModelThroughputs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listprovisionedmodelthroughputspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProvisionedModelThroughputsRequestPaginateTypeDef]
    ) -> PageIterator[ListProvisionedModelThroughputsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/paginator/ListProvisionedModelThroughputs.html#Bedrock.Paginator.ListProvisionedModelThroughputs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators/#listprovisionedmodelthroughputspaginator)
        """
