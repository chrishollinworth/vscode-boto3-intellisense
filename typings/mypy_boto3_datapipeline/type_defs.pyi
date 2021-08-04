"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import ActivatePipelineInputRequestTypeDef

    data: ActivatePipelineInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import OperatorTypeType, TaskStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActivatePipelineInputRequestTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "CreatePipelineOutputTypeDef",
    "DeactivatePipelineInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DescribeObjectsInputRequestTypeDef",
    "DescribeObjectsOutputTypeDef",
    "DescribePipelinesInputRequestTypeDef",
    "DescribePipelinesOutputTypeDef",
    "EvaluateExpressionInputRequestTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionInputRequestTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "ListPipelinesOutputTypeDef",
    "OperatorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "PollForTaskInputRequestTypeDef",
    "PollForTaskOutputTypeDef",
    "PutPipelineDefinitionInputRequestTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "QueryObjectsInputRequestTypeDef",
    "QueryObjectsOutputTypeDef",
    "QueryTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ReportTaskProgressInputRequestTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatInputRequestTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SelectorTypeDef",
    "SetStatusInputRequestTypeDef",
    "SetTaskStatusInputRequestTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidatePipelineDefinitionInputRequestTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
)

_RequiredActivatePipelineInputRequestTypeDef = TypedDict(
    "_RequiredActivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalActivatePipelineInputRequestTypeDef = TypedDict(
    "_OptionalActivatePipelineInputRequestTypeDef",
    {
        "parameterValues": List["ParameterValueTypeDef"],
        "startTimestamp": Union[datetime, str],
    },
    total=False,
)

class ActivatePipelineInputRequestTypeDef(
    _RequiredActivatePipelineInputRequestTypeDef, _OptionalActivatePipelineInputRequestTypeDef
):
    pass

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredCreatePipelineInputRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineInputRequestTypeDef",
    {
        "name": str,
        "uniqueId": str,
    },
)
_OptionalCreatePipelineInputRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineInputRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePipelineInputRequestTypeDef(
    _RequiredCreatePipelineInputRequestTypeDef, _OptionalCreatePipelineInputRequestTypeDef
):
    pass

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipelineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeactivatePipelineInputRequestTypeDef = TypedDict(
    "_RequiredDeactivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalDeactivatePipelineInputRequestTypeDef = TypedDict(
    "_OptionalDeactivatePipelineInputRequestTypeDef",
    {
        "cancelActive": bool,
    },
    total=False,
)

class DeactivatePipelineInputRequestTypeDef(
    _RequiredDeactivatePipelineInputRequestTypeDef, _OptionalDeactivatePipelineInputRequestTypeDef
):
    pass

DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
    },
)

_RequiredDescribeObjectsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": List[str],
    },
)
_OptionalDescribeObjectsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeObjectsInputRequestTypeDef",
    {
        "evaluateExpressions": bool,
        "marker": str,
    },
    total=False,
)

class DescribeObjectsInputRequestTypeDef(
    _RequiredDescribeObjectsInputRequestTypeDef, _OptionalDescribeObjectsInputRequestTypeDef
):
    pass

DescribeObjectsOutputTypeDef = TypedDict(
    "DescribeObjectsOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelinesInputRequestTypeDef = TypedDict(
    "DescribePipelinesInputRequestTypeDef",
    {
        "pipelineIds": List[str],
    },
)

DescribePipelinesOutputTypeDef = TypedDict(
    "DescribePipelinesOutputTypeDef",
    {
        "pipelineDescriptionList": List["PipelineDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluateExpressionInputRequestTypeDef = TypedDict(
    "EvaluateExpressionInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectId": str,
        "expression": str,
    },
)

EvaluateExpressionOutputTypeDef = TypedDict(
    "EvaluateExpressionOutputTypeDef",
    {
        "evaluatedExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFieldTypeDef = TypedDict(
    "_RequiredFieldTypeDef",
    {
        "key": str,
    },
)
_OptionalFieldTypeDef = TypedDict(
    "_OptionalFieldTypeDef",
    {
        "stringValue": str,
        "refValue": str,
    },
    total=False,
)

class FieldTypeDef(_RequiredFieldTypeDef, _OptionalFieldTypeDef):
    pass

_RequiredGetPipelineDefinitionInputRequestTypeDef = TypedDict(
    "_RequiredGetPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalGetPipelineDefinitionInputRequestTypeDef = TypedDict(
    "_OptionalGetPipelineDefinitionInputRequestTypeDef",
    {
        "version": str,
    },
    total=False,
)

class GetPipelineDefinitionInputRequestTypeDef(
    _RequiredGetPipelineDefinitionInputRequestTypeDef,
    _OptionalGetPipelineDefinitionInputRequestTypeDef,
):
    pass

GetPipelineDefinitionOutputTypeDef = TypedDict(
    "GetPipelineDefinitionOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "document": str,
        "signature": str,
    },
    total=False,
)

ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "marker": str,
    },
    total=False,
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelineIdList": List["PipelineIdNameTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperatorTypeDef = TypedDict(
    "OperatorTypeDef",
    {
        "type": OperatorTypeType,
        "values": List[str],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterAttributeTypeDef = TypedDict(
    "ParameterAttributeTypeDef",
    {
        "key": str,
        "stringValue": str,
    },
)

ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef",
    {
        "id": str,
        "attributes": List["ParameterAttributeTypeDef"],
    },
)

ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "id": str,
        "stringValue": str,
    },
)

_RequiredPipelineDescriptionTypeDef = TypedDict(
    "_RequiredPipelineDescriptionTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List["FieldTypeDef"],
    },
)
_OptionalPipelineDescriptionTypeDef = TypedDict(
    "_OptionalPipelineDescriptionTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PipelineDescriptionTypeDef(
    _RequiredPipelineDescriptionTypeDef, _OptionalPipelineDescriptionTypeDef
):
    pass

PipelineIdNameTypeDef = TypedDict(
    "PipelineIdNameTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List["FieldTypeDef"],
    },
)

_RequiredPollForTaskInputRequestTypeDef = TypedDict(
    "_RequiredPollForTaskInputRequestTypeDef",
    {
        "workerGroup": str,
    },
)
_OptionalPollForTaskInputRequestTypeDef = TypedDict(
    "_OptionalPollForTaskInputRequestTypeDef",
    {
        "hostname": str,
        "instanceIdentity": "InstanceIdentityTypeDef",
    },
    total=False,
)

class PollForTaskInputRequestTypeDef(
    _RequiredPollForTaskInputRequestTypeDef, _OptionalPollForTaskInputRequestTypeDef
):
    pass

PollForTaskOutputTypeDef = TypedDict(
    "PollForTaskOutputTypeDef",
    {
        "taskObject": "TaskObjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutPipelineDefinitionInputRequestTypeDef = TypedDict(
    "_RequiredPutPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": List["PipelineObjectTypeDef"],
    },
)
_OptionalPutPipelineDefinitionInputRequestTypeDef = TypedDict(
    "_OptionalPutPipelineDefinitionInputRequestTypeDef",
    {
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
    },
    total=False,
)

class PutPipelineDefinitionInputRequestTypeDef(
    _RequiredPutPipelineDefinitionInputRequestTypeDef,
    _OptionalPutPipelineDefinitionInputRequestTypeDef,
):
    pass

PutPipelineDefinitionOutputTypeDef = TypedDict(
    "PutPipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredQueryObjectsInputRequestTypeDef = TypedDict(
    "_RequiredQueryObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "sphere": str,
    },
)
_OptionalQueryObjectsInputRequestTypeDef = TypedDict(
    "_OptionalQueryObjectsInputRequestTypeDef",
    {
        "query": "QueryTypeDef",
        "marker": str,
        "limit": int,
    },
    total=False,
)

class QueryObjectsInputRequestTypeDef(
    _RequiredQueryObjectsInputRequestTypeDef, _OptionalQueryObjectsInputRequestTypeDef
):
    pass

QueryObjectsOutputTypeDef = TypedDict(
    "QueryObjectsOutputTypeDef",
    {
        "ids": List[str],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "selectors": List["SelectorTypeDef"],
    },
    total=False,
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tagKeys": List[str],
    },
)

_RequiredReportTaskProgressInputRequestTypeDef = TypedDict(
    "_RequiredReportTaskProgressInputRequestTypeDef",
    {
        "taskId": str,
    },
)
_OptionalReportTaskProgressInputRequestTypeDef = TypedDict(
    "_OptionalReportTaskProgressInputRequestTypeDef",
    {
        "fields": List["FieldTypeDef"],
    },
    total=False,
)

class ReportTaskProgressInputRequestTypeDef(
    _RequiredReportTaskProgressInputRequestTypeDef, _OptionalReportTaskProgressInputRequestTypeDef
):
    pass

ReportTaskProgressOutputTypeDef = TypedDict(
    "ReportTaskProgressOutputTypeDef",
    {
        "canceled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReportTaskRunnerHeartbeatInputRequestTypeDef = TypedDict(
    "_RequiredReportTaskRunnerHeartbeatInputRequestTypeDef",
    {
        "taskrunnerId": str,
    },
)
_OptionalReportTaskRunnerHeartbeatInputRequestTypeDef = TypedDict(
    "_OptionalReportTaskRunnerHeartbeatInputRequestTypeDef",
    {
        "workerGroup": str,
        "hostname": str,
    },
    total=False,
)

class ReportTaskRunnerHeartbeatInputRequestTypeDef(
    _RequiredReportTaskRunnerHeartbeatInputRequestTypeDef,
    _OptionalReportTaskRunnerHeartbeatInputRequestTypeDef,
):
    pass

ReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    {
        "terminate": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "fieldName": str,
        "operator": "OperatorTypeDef",
    },
    total=False,
)

SetStatusInputRequestTypeDef = TypedDict(
    "SetStatusInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": List[str],
        "status": str,
    },
)

_RequiredSetTaskStatusInputRequestTypeDef = TypedDict(
    "_RequiredSetTaskStatusInputRequestTypeDef",
    {
        "taskId": str,
        "taskStatus": TaskStatusType,
    },
)
_OptionalSetTaskStatusInputRequestTypeDef = TypedDict(
    "_OptionalSetTaskStatusInputRequestTypeDef",
    {
        "errorId": str,
        "errorMessage": str,
        "errorStackTrace": str,
    },
    total=False,
)

class SetTaskStatusInputRequestTypeDef(
    _RequiredSetTaskStatusInputRequestTypeDef, _OptionalSetTaskStatusInputRequestTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TaskObjectTypeDef = TypedDict(
    "TaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, "PipelineObjectTypeDef"],
    },
    total=False,
)

_RequiredValidatePipelineDefinitionInputRequestTypeDef = TypedDict(
    "_RequiredValidatePipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": List["PipelineObjectTypeDef"],
    },
)
_OptionalValidatePipelineDefinitionInputRequestTypeDef = TypedDict(
    "_OptionalValidatePipelineDefinitionInputRequestTypeDef",
    {
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
    },
    total=False,
)

class ValidatePipelineDefinitionInputRequestTypeDef(
    _RequiredValidatePipelineDefinitionInputRequestTypeDef,
    _OptionalValidatePipelineDefinitionInputRequestTypeDef,
):
    pass

ValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "ValidatePipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "id": str,
        "errors": List[str],
    },
    total=False,
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "id": str,
        "warnings": List[str],
    },
    total=False,
)
