"""
Type annotations for fis service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_fis.client import FISClient

    session = Session()
    client: FISClient = session.client("fis")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListActionsPaginator,
    ListExperimentResolvedTargetsPaginator,
    ListExperimentsPaginator,
    ListExperimentTemplatesPaginator,
    ListTargetAccountConfigurationsPaginator,
    ListTargetResourceTypesPaginator,
)
from .type_defs import (
    CreateExperimentTemplateRequestTypeDef,
    CreateExperimentTemplateResponseTypeDef,
    CreateTargetAccountConfigurationRequestTypeDef,
    CreateTargetAccountConfigurationResponseTypeDef,
    DeleteExperimentTemplateRequestTypeDef,
    DeleteExperimentTemplateResponseTypeDef,
    DeleteTargetAccountConfigurationRequestTypeDef,
    DeleteTargetAccountConfigurationResponseTypeDef,
    GetActionRequestTypeDef,
    GetActionResponseTypeDef,
    GetExperimentRequestTypeDef,
    GetExperimentResponseTypeDef,
    GetExperimentTargetAccountConfigurationRequestTypeDef,
    GetExperimentTargetAccountConfigurationResponseTypeDef,
    GetExperimentTemplateRequestTypeDef,
    GetExperimentTemplateResponseTypeDef,
    GetSafetyLeverRequestTypeDef,
    GetSafetyLeverResponseTypeDef,
    GetTargetAccountConfigurationRequestTypeDef,
    GetTargetAccountConfigurationResponseTypeDef,
    GetTargetResourceTypeRequestTypeDef,
    GetTargetResourceTypeResponseTypeDef,
    ListActionsRequestTypeDef,
    ListActionsResponseTypeDef,
    ListExperimentResolvedTargetsRequestTypeDef,
    ListExperimentResolvedTargetsResponseTypeDef,
    ListExperimentsRequestTypeDef,
    ListExperimentsResponseTypeDef,
    ListExperimentTargetAccountConfigurationsRequestTypeDef,
    ListExperimentTargetAccountConfigurationsResponseTypeDef,
    ListExperimentTemplatesRequestTypeDef,
    ListExperimentTemplatesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetAccountConfigurationsRequestTypeDef,
    ListTargetAccountConfigurationsResponseTypeDef,
    ListTargetResourceTypesRequestTypeDef,
    ListTargetResourceTypesResponseTypeDef,
    StartExperimentRequestTypeDef,
    StartExperimentResponseTypeDef,
    StopExperimentRequestTypeDef,
    StopExperimentResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateExperimentTemplateRequestTypeDef,
    UpdateExperimentTemplateResponseTypeDef,
    UpdateSafetyLeverStateRequestTypeDef,
    UpdateSafetyLeverStateResponseTypeDef,
    UpdateTargetAccountConfigurationRequestTypeDef,
    UpdateTargetAccountConfigurationResponseTypeDef,
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

__all__ = ("FISClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FISClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FISClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#generate_presigned_url)
        """

    def create_experiment_template(
        self, **kwargs: Unpack[CreateExperimentTemplateRequestTypeDef]
    ) -> CreateExperimentTemplateResponseTypeDef:
        """
        Creates an experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/create_experiment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#create_experiment_template)
        """

    def create_target_account_configuration(
        self, **kwargs: Unpack[CreateTargetAccountConfigurationRequestTypeDef]
    ) -> CreateTargetAccountConfigurationResponseTypeDef:
        """
        Creates a target account configuration for the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/create_target_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#create_target_account_configuration)
        """

    def delete_experiment_template(
        self, **kwargs: Unpack[DeleteExperimentTemplateRequestTypeDef]
    ) -> DeleteExperimentTemplateResponseTypeDef:
        """
        Deletes the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/delete_experiment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#delete_experiment_template)
        """

    def delete_target_account_configuration(
        self, **kwargs: Unpack[DeleteTargetAccountConfigurationRequestTypeDef]
    ) -> DeleteTargetAccountConfigurationResponseTypeDef:
        """
        Deletes the specified target account configuration of the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/delete_target_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#delete_target_account_configuration)
        """

    def get_action(self, **kwargs: Unpack[GetActionRequestTypeDef]) -> GetActionResponseTypeDef:
        """
        Gets information about the specified FIS action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_action)
        """

    def get_experiment(
        self, **kwargs: Unpack[GetExperimentRequestTypeDef]
    ) -> GetExperimentResponseTypeDef:
        """
        Gets information about the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_experiment)
        """

    def get_experiment_target_account_configuration(
        self, **kwargs: Unpack[GetExperimentTargetAccountConfigurationRequestTypeDef]
    ) -> GetExperimentTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_experiment_target_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_experiment_target_account_configuration)
        """

    def get_experiment_template(
        self, **kwargs: Unpack[GetExperimentTemplateRequestTypeDef]
    ) -> GetExperimentTemplateResponseTypeDef:
        """
        Gets information about the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_experiment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_experiment_template)
        """

    def get_safety_lever(
        self, **kwargs: Unpack[GetSafetyLeverRequestTypeDef]
    ) -> GetSafetyLeverResponseTypeDef:
        """
        Gets information about the specified safety lever.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_safety_lever.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_safety_lever)
        """

    def get_target_account_configuration(
        self, **kwargs: Unpack[GetTargetAccountConfigurationRequestTypeDef]
    ) -> GetTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_target_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_target_account_configuration)
        """

    def get_target_resource_type(
        self, **kwargs: Unpack[GetTargetResourceTypeRequestTypeDef]
    ) -> GetTargetResourceTypeResponseTypeDef:
        """
        Gets information about the specified resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_target_resource_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_target_resource_type)
        """

    def list_actions(
        self, **kwargs: Unpack[ListActionsRequestTypeDef]
    ) -> ListActionsResponseTypeDef:
        """
        Lists the available FIS actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_actions)
        """

    def list_experiment_resolved_targets(
        self, **kwargs: Unpack[ListExperimentResolvedTargetsRequestTypeDef]
    ) -> ListExperimentResolvedTargetsResponseTypeDef:
        """
        Lists the resolved targets information of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_experiment_resolved_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_experiment_resolved_targets)
        """

    def list_experiment_target_account_configurations(
        self, **kwargs: Unpack[ListExperimentTargetAccountConfigurationsRequestTypeDef]
    ) -> ListExperimentTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_experiment_target_account_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_experiment_target_account_configurations)
        """

    def list_experiment_templates(
        self, **kwargs: Unpack[ListExperimentTemplatesRequestTypeDef]
    ) -> ListExperimentTemplatesResponseTypeDef:
        """
        Lists your experiment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_experiment_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_experiment_templates)
        """

    def list_experiments(
        self, **kwargs: Unpack[ListExperimentsRequestTypeDef]
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists your experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_experiments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_experiments)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_tags_for_resource)
        """

    def list_target_account_configurations(
        self, **kwargs: Unpack[ListTargetAccountConfigurationsRequestTypeDef]
    ) -> ListTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_target_account_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_target_account_configurations)
        """

    def list_target_resource_types(
        self, **kwargs: Unpack[ListTargetResourceTypesRequestTypeDef]
    ) -> ListTargetResourceTypesResponseTypeDef:
        """
        Lists the target resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/list_target_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#list_target_resource_types)
        """

    def start_experiment(
        self, **kwargs: Unpack[StartExperimentRequestTypeDef]
    ) -> StartExperimentResponseTypeDef:
        """
        Starts running an experiment from the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/start_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#start_experiment)
        """

    def stop_experiment(
        self, **kwargs: Unpack[StopExperimentRequestTypeDef]
    ) -> StopExperimentResponseTypeDef:
        """
        Stops the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/stop_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#stop_experiment)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#untag_resource)
        """

    def update_experiment_template(
        self, **kwargs: Unpack[UpdateExperimentTemplateRequestTypeDef]
    ) -> UpdateExperimentTemplateResponseTypeDef:
        """
        Updates the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/update_experiment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#update_experiment_template)
        """

    def update_safety_lever_state(
        self, **kwargs: Unpack[UpdateSafetyLeverStateRequestTypeDef]
    ) -> UpdateSafetyLeverStateResponseTypeDef:
        """
        Updates the specified safety lever state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/update_safety_lever_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#update_safety_lever_state)
        """

    def update_target_account_configuration(
        self, **kwargs: Unpack[UpdateTargetAccountConfigurationRequestTypeDef]
    ) -> UpdateTargetAccountConfigurationResponseTypeDef:
        """
        Updates the target account configuration for the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/update_target_account_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#update_target_account_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_actions"]
    ) -> ListActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_experiment_resolved_targets"]
    ) -> ListExperimentResolvedTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_experiment_templates"]
    ) -> ListExperimentTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_target_account_configurations"]
    ) -> ListTargetAccountConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_target_resource_types"]
    ) -> ListTargetResourceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/client/#get_paginator)
        """
