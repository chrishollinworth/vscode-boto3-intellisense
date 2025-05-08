"""
Type annotations for frauddetector service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_frauddetector.client import FraudDetectorClient

    session = Session()
    client: FraudDetectorClient = session.client("frauddetector")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchCreateVariableRequestTypeDef,
    BatchCreateVariableResultTypeDef,
    BatchGetVariableRequestTypeDef,
    BatchGetVariableResultTypeDef,
    CancelBatchImportJobRequestTypeDef,
    CancelBatchPredictionJobRequestTypeDef,
    CreateBatchImportJobRequestTypeDef,
    CreateBatchPredictionJobRequestTypeDef,
    CreateDetectorVersionRequestTypeDef,
    CreateDetectorVersionResultTypeDef,
    CreateListRequestTypeDef,
    CreateModelRequestTypeDef,
    CreateModelVersionRequestTypeDef,
    CreateModelVersionResultTypeDef,
    CreateRuleRequestTypeDef,
    CreateRuleResultTypeDef,
    CreateVariableRequestTypeDef,
    DeleteBatchImportJobRequestTypeDef,
    DeleteBatchPredictionJobRequestTypeDef,
    DeleteDetectorRequestTypeDef,
    DeleteDetectorVersionRequestTypeDef,
    DeleteEntityTypeRequestTypeDef,
    DeleteEventRequestTypeDef,
    DeleteEventsByEventTypeRequestTypeDef,
    DeleteEventsByEventTypeResultTypeDef,
    DeleteEventTypeRequestTypeDef,
    DeleteExternalModelRequestTypeDef,
    DeleteLabelRequestTypeDef,
    DeleteListRequestTypeDef,
    DeleteModelRequestTypeDef,
    DeleteModelVersionRequestTypeDef,
    DeleteOutcomeRequestTypeDef,
    DeleteRuleRequestTypeDef,
    DeleteVariableRequestTypeDef,
    DescribeDetectorRequestTypeDef,
    DescribeDetectorResultTypeDef,
    DescribeModelVersionsRequestTypeDef,
    DescribeModelVersionsResultTypeDef,
    GetBatchImportJobsRequestTypeDef,
    GetBatchImportJobsResultTypeDef,
    GetBatchPredictionJobsRequestTypeDef,
    GetBatchPredictionJobsResultTypeDef,
    GetDeleteEventsByEventTypeStatusRequestTypeDef,
    GetDeleteEventsByEventTypeStatusResultTypeDef,
    GetDetectorsRequestTypeDef,
    GetDetectorsResultTypeDef,
    GetDetectorVersionRequestTypeDef,
    GetDetectorVersionResultTypeDef,
    GetEntityTypesRequestTypeDef,
    GetEntityTypesResultTypeDef,
    GetEventPredictionMetadataRequestTypeDef,
    GetEventPredictionMetadataResultTypeDef,
    GetEventPredictionRequestTypeDef,
    GetEventPredictionResultTypeDef,
    GetEventRequestTypeDef,
    GetEventResultTypeDef,
    GetEventTypesRequestTypeDef,
    GetEventTypesResultTypeDef,
    GetExternalModelsRequestTypeDef,
    GetExternalModelsResultTypeDef,
    GetKMSEncryptionKeyResultTypeDef,
    GetLabelsRequestTypeDef,
    GetLabelsResultTypeDef,
    GetListElementsRequestTypeDef,
    GetListElementsResultTypeDef,
    GetListsMetadataRequestTypeDef,
    GetListsMetadataResultTypeDef,
    GetModelsRequestTypeDef,
    GetModelsResultTypeDef,
    GetModelVersionRequestTypeDef,
    GetModelVersionResultTypeDef,
    GetOutcomesRequestTypeDef,
    GetOutcomesResultTypeDef,
    GetRulesRequestTypeDef,
    GetRulesResultTypeDef,
    GetVariablesRequestTypeDef,
    GetVariablesResultTypeDef,
    ListEventPredictionsRequestTypeDef,
    ListEventPredictionsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PutDetectorRequestTypeDef,
    PutEntityTypeRequestTypeDef,
    PutEventTypeRequestTypeDef,
    PutExternalModelRequestTypeDef,
    PutKMSEncryptionKeyRequestTypeDef,
    PutLabelRequestTypeDef,
    PutOutcomeRequestTypeDef,
    SendEventRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDetectorVersionMetadataRequestTypeDef,
    UpdateDetectorVersionRequestTypeDef,
    UpdateDetectorVersionStatusRequestTypeDef,
    UpdateEventLabelRequestTypeDef,
    UpdateListRequestTypeDef,
    UpdateModelRequestTypeDef,
    UpdateModelVersionRequestTypeDef,
    UpdateModelVersionResultTypeDef,
    UpdateModelVersionStatusRequestTypeDef,
    UpdateRuleMetadataRequestTypeDef,
    UpdateRuleVersionRequestTypeDef,
    UpdateRuleVersionResultTypeDef,
    UpdateVariableRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("FraudDetectorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FraudDetectorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FraudDetectorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#generate_presigned_url)
        """

    def batch_create_variable(
        self, **kwargs: Unpack[BatchCreateVariableRequestTypeDef]
    ) -> BatchCreateVariableResultTypeDef:
        """
        Creates a batch of variables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/batch_create_variable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#batch_create_variable)
        """

    def batch_get_variable(
        self, **kwargs: Unpack[BatchGetVariableRequestTypeDef]
    ) -> BatchGetVariableResultTypeDef:
        """
        Gets a batch of variables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/batch_get_variable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#batch_get_variable)
        """

    def cancel_batch_import_job(
        self, **kwargs: Unpack[CancelBatchImportJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an in-progress batch import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/cancel_batch_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#cancel_batch_import_job)
        """

    def cancel_batch_prediction_job(
        self, **kwargs: Unpack[CancelBatchPredictionJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the specified batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/cancel_batch_prediction_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#cancel_batch_prediction_job)
        """

    def create_batch_import_job(
        self, **kwargs: Unpack[CreateBatchImportJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a batch import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_batch_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_batch_import_job)
        """

    def create_batch_prediction_job(
        self, **kwargs: Unpack[CreateBatchPredictionJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_batch_prediction_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_batch_prediction_job)
        """

    def create_detector_version(
        self, **kwargs: Unpack[CreateDetectorVersionRequestTypeDef]
    ) -> CreateDetectorVersionResultTypeDef:
        """
        Creates a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_detector_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_detector_version)
        """

    def create_list(self, **kwargs: Unpack[CreateListRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_list)
        """

    def create_model(self, **kwargs: Unpack[CreateModelRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a model using the specified model type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_model)
        """

    def create_model_version(
        self, **kwargs: Unpack[CreateModelVersionRequestTypeDef]
    ) -> CreateModelVersionResultTypeDef:
        """
        Creates a version of the model using the specified model type and model id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_model_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_model_version)
        """

    def create_rule(self, **kwargs: Unpack[CreateRuleRequestTypeDef]) -> CreateRuleResultTypeDef:
        """
        Creates a rule for use with the specified detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_rule)
        """

    def create_variable(self, **kwargs: Unpack[CreateVariableRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/create_variable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#create_variable)
        """

    def delete_batch_import_job(
        self, **kwargs: Unpack[DeleteBatchImportJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified batch import job ID record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_batch_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_batch_import_job)
        """

    def delete_batch_prediction_job(
        self, **kwargs: Unpack[DeleteBatchPredictionJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_batch_prediction_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_batch_prediction_job)
        """

    def delete_detector(self, **kwargs: Unpack[DeleteDetectorRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_detector)
        """

    def delete_detector_version(
        self, **kwargs: Unpack[DeleteDetectorVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_detector_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_detector_version)
        """

    def delete_entity_type(
        self, **kwargs: Unpack[DeleteEntityTypeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_entity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_entity_type)
        """

    def delete_event(self, **kwargs: Unpack[DeleteEventRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_event)
        """

    def delete_event_type(self, **kwargs: Unpack[DeleteEventTypeRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_event_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_event_type)
        """

    def delete_events_by_event_type(
        self, **kwargs: Unpack[DeleteEventsByEventTypeRequestTypeDef]
    ) -> DeleteEventsByEventTypeResultTypeDef:
        """
        Deletes all events of a particular event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_events_by_event_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_events_by_event_type)
        """

    def delete_external_model(
        self, **kwargs: Unpack[DeleteExternalModelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a SageMaker model from Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_external_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_external_model)
        """

    def delete_label(self, **kwargs: Unpack[DeleteLabelRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_label.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_label)
        """

    def delete_list(self, **kwargs: Unpack[DeleteListRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the list, provided it is not used in a rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_list)
        """

    def delete_model(self, **kwargs: Unpack[DeleteModelRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_model)
        """

    def delete_model_version(
        self, **kwargs: Unpack[DeleteModelVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_model_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_model_version)
        """

    def delete_outcome(self, **kwargs: Unpack[DeleteOutcomeRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an outcome.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_outcome.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_outcome)
        """

    def delete_rule(self, **kwargs: Unpack[DeleteRuleRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_rule)
        """

    def delete_variable(self, **kwargs: Unpack[DeleteVariableRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/delete_variable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#delete_variable)
        """

    def describe_detector(
        self, **kwargs: Unpack[DescribeDetectorRequestTypeDef]
    ) -> DescribeDetectorResultTypeDef:
        """
        Gets all versions for a specified detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/describe_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#describe_detector)
        """

    def describe_model_versions(
        self, **kwargs: Unpack[DescribeModelVersionsRequestTypeDef]
    ) -> DescribeModelVersionsResultTypeDef:
        """
        Gets all of the model versions for the specified model type or for the
        specified model type and model ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/describe_model_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#describe_model_versions)
        """

    def get_batch_import_jobs(
        self, **kwargs: Unpack[GetBatchImportJobsRequestTypeDef]
    ) -> GetBatchImportJobsResultTypeDef:
        """
        Gets all batch import jobs or a specific job of the specified ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_batch_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_batch_import_jobs)
        """

    def get_batch_prediction_jobs(
        self, **kwargs: Unpack[GetBatchPredictionJobsRequestTypeDef]
    ) -> GetBatchPredictionJobsResultTypeDef:
        """
        Gets all batch prediction jobs or a specific job if you specify a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_batch_prediction_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_batch_prediction_jobs)
        """

    def get_delete_events_by_event_type_status(
        self, **kwargs: Unpack[GetDeleteEventsByEventTypeStatusRequestTypeDef]
    ) -> GetDeleteEventsByEventTypeStatusResultTypeDef:
        """
        Retrieves the status of a <code>DeleteEventsByEventType</code> action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_delete_events_by_event_type_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_delete_events_by_event_type_status)
        """

    def get_detector_version(
        self, **kwargs: Unpack[GetDetectorVersionRequestTypeDef]
    ) -> GetDetectorVersionResultTypeDef:
        """
        Gets a particular detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_detector_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_detector_version)
        """

    def get_detectors(
        self, **kwargs: Unpack[GetDetectorsRequestTypeDef]
    ) -> GetDetectorsResultTypeDef:
        """
        Gets all detectors or a single detector if a <code>detectorId</code> is
        specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_detectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_detectors)
        """

    def get_entity_types(
        self, **kwargs: Unpack[GetEntityTypesRequestTypeDef]
    ) -> GetEntityTypesResultTypeDef:
        """
        Gets all entity types or a specific entity type if a name is specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_entity_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_entity_types)
        """

    def get_event(self, **kwargs: Unpack[GetEventRequestTypeDef]) -> GetEventResultTypeDef:
        """
        Retrieves details of events stored with Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_event)
        """

    def get_event_prediction(
        self, **kwargs: Unpack[GetEventPredictionRequestTypeDef]
    ) -> GetEventPredictionResultTypeDef:
        """
        Evaluates an event against a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_event_prediction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_event_prediction)
        """

    def get_event_prediction_metadata(
        self, **kwargs: Unpack[GetEventPredictionMetadataRequestTypeDef]
    ) -> GetEventPredictionMetadataResultTypeDef:
        """
        Gets details of the past fraud predictions for the specified event ID, event
        type, detector ID, and detector version ID that was generated in the specified
        time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_event_prediction_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_event_prediction_metadata)
        """

    def get_event_types(
        self, **kwargs: Unpack[GetEventTypesRequestTypeDef]
    ) -> GetEventTypesResultTypeDef:
        """
        Gets all event types or a specific event type if name is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_event_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_event_types)
        """

    def get_external_models(
        self, **kwargs: Unpack[GetExternalModelsRequestTypeDef]
    ) -> GetExternalModelsResultTypeDef:
        """
        Gets the details for one or more Amazon SageMaker models that have been
        imported into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_external_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_external_models)
        """

    def get_kms_encryption_key(self) -> GetKMSEncryptionKeyResultTypeDef:
        """
        Gets the encryption key if a KMS key has been specified to be used to encrypt
        content in Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_kms_encryption_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_kms_encryption_key)
        """

    def get_labels(self, **kwargs: Unpack[GetLabelsRequestTypeDef]) -> GetLabelsResultTypeDef:
        """
        Gets all labels or a specific label if name is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_labels)
        """

    def get_list_elements(
        self, **kwargs: Unpack[GetListElementsRequestTypeDef]
    ) -> GetListElementsResultTypeDef:
        """
        Gets all the elements in the specified list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_list_elements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_list_elements)
        """

    def get_lists_metadata(
        self, **kwargs: Unpack[GetListsMetadataRequestTypeDef]
    ) -> GetListsMetadataResultTypeDef:
        """
        Gets the metadata of either all the lists under the account or the specified
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_lists_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_lists_metadata)
        """

    def get_model_version(
        self, **kwargs: Unpack[GetModelVersionRequestTypeDef]
    ) -> GetModelVersionResultTypeDef:
        """
        Gets the details of the specified model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_model_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_model_version)
        """

    def get_models(self, **kwargs: Unpack[GetModelsRequestTypeDef]) -> GetModelsResultTypeDef:
        """
        Gets one or more models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_models)
        """

    def get_outcomes(self, **kwargs: Unpack[GetOutcomesRequestTypeDef]) -> GetOutcomesResultTypeDef:
        """
        Gets one or more outcomes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_outcomes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_outcomes)
        """

    def get_rules(self, **kwargs: Unpack[GetRulesRequestTypeDef]) -> GetRulesResultTypeDef:
        """
        Get all rules for a detector (paginated) if <code>ruleId</code> and
        <code>ruleVersion</code> are not specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_rules)
        """

    def get_variables(
        self, **kwargs: Unpack[GetVariablesRequestTypeDef]
    ) -> GetVariablesResultTypeDef:
        """
        Gets all of the variables or the specific variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/get_variables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#get_variables)
        """

    def list_event_predictions(
        self, **kwargs: Unpack[ListEventPredictionsRequestTypeDef]
    ) -> ListEventPredictionsResultTypeDef:
        """
        Gets a list of past predictions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/list_event_predictions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#list_event_predictions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Lists all tags associated with the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#list_tags_for_resource)
        """

    def put_detector(self, **kwargs: Unpack[PutDetectorRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates a detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_detector)
        """

    def put_entity_type(self, **kwargs: Unpack[PutEntityTypeRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates an entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_entity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_entity_type)
        """

    def put_event_type(self, **kwargs: Unpack[PutEventTypeRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates an event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_event_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_event_type)
        """

    def put_external_model(
        self, **kwargs: Unpack[PutExternalModelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates an Amazon SageMaker model endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_external_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_external_model)
        """

    def put_kms_encryption_key(
        self, **kwargs: Unpack[PutKMSEncryptionKeyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Specifies the KMS key to be used to encrypt content in Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_kms_encryption_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_kms_encryption_key)
        """

    def put_label(self, **kwargs: Unpack[PutLabelRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_label.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_label)
        """

    def put_outcome(self, **kwargs: Unpack[PutOutcomeRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates an outcome.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/put_outcome.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#put_outcome)
        """

    def send_event(self, **kwargs: Unpack[SendEventRequestTypeDef]) -> Dict[str, Any]:
        """
        Stores events in Amazon Fraud Detector without generating fraud predictions for
        those events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/send_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#send_event)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#untag_resource)
        """

    def update_detector_version(
        self, **kwargs: Unpack[UpdateDetectorVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_detector_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_detector_version)
        """

    def update_detector_version_metadata(
        self, **kwargs: Unpack[UpdateDetectorVersionMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the detector version's description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_detector_version_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_detector_version_metadata)
        """

    def update_detector_version_status(
        self, **kwargs: Unpack[UpdateDetectorVersionStatusRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the detector version's status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_detector_version_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_detector_version_status)
        """

    def update_event_label(
        self, **kwargs: Unpack[UpdateEventLabelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified event with a new label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_event_label.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_event_label)
        """

    def update_list(self, **kwargs: Unpack[UpdateListRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_list)
        """

    def update_model(self, **kwargs: Unpack[UpdateModelRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates model description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_model)
        """

    def update_model_version(
        self, **kwargs: Unpack[UpdateModelVersionRequestTypeDef]
    ) -> UpdateModelVersionResultTypeDef:
        """
        Updates a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_model_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_model_version)
        """

    def update_model_version_status(
        self, **kwargs: Unpack[UpdateModelVersionStatusRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the status of a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_model_version_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_model_version_status)
        """

    def update_rule_metadata(
        self, **kwargs: Unpack[UpdateRuleMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a rule's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_rule_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_rule_metadata)
        """

    def update_rule_version(
        self, **kwargs: Unpack[UpdateRuleVersionRequestTypeDef]
    ) -> UpdateRuleVersionResultTypeDef:
        """
        Updates a rule version resulting in a new rule version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_rule_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_rule_version)
        """

    def update_variable(self, **kwargs: Unpack[UpdateVariableRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector/client/update_variable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client/#update_variable)
        """
