"""
Type annotations for appconfigdata service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appconfigdata.type_defs import GetLatestConfigurationRequestTypeDef

    data: GetLatestConfigurationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from botocore.response import StreamingBody

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetLatestConfigurationRequestTypeDef",
    "GetLatestConfigurationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartConfigurationSessionRequestTypeDef",
    "StartConfigurationSessionResponseTypeDef",
)

class GetLatestConfigurationRequestTypeDef(TypedDict):
    ConfigurationToken: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class StartConfigurationSessionRequestTypeDef(TypedDict):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ConfigurationProfileIdentifier: str
    RequiredMinimumPollIntervalInSeconds: NotRequired[int]

class GetLatestConfigurationResponseTypeDef(TypedDict):
    NextPollConfigurationToken: str
    NextPollIntervalInSeconds: int
    ContentType: str
    Configuration: StreamingBody
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartConfigurationSessionResponseTypeDef(TypedDict):
    InitialConfigurationToken: str
    ResponseMetadata: ResponseMetadataTypeDef
