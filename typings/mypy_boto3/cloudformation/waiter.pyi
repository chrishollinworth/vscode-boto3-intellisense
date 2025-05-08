"""
Type annotations for cloudformation service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudformation.client import CloudFormationClient
    from mypy_boto3_cloudformation.waiter import (
        ChangeSetCreateCompleteWaiter,
        StackCreateCompleteWaiter,
        StackDeleteCompleteWaiter,
        StackExistsWaiter,
        StackImportCompleteWaiter,
        StackRefactorCreateCompleteWaiter,
        StackRefactorExecuteCompleteWaiter,
        StackRollbackCompleteWaiter,
        StackUpdateCompleteWaiter,
        TypeRegistrationCompleteWaiter,
    )

    session = Session()
    client: CloudFormationClient = session.client("cloudformation")

    change_set_create_complete_waiter: ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
    stack_create_complete_waiter: StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
    stack_delete_complete_waiter: StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
    stack_exists_waiter: StackExistsWaiter = client.get_waiter("stack_exists")
    stack_import_complete_waiter: StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
    stack_refactor_create_complete_waiter: StackRefactorCreateCompleteWaiter = client.get_waiter("stack_refactor_create_complete")
    stack_refactor_execute_complete_waiter: StackRefactorExecuteCompleteWaiter = client.get_waiter("stack_refactor_execute_complete")
    stack_rollback_complete_waiter: StackRollbackCompleteWaiter = client.get_waiter("stack_rollback_complete")
    stack_update_complete_waiter: StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
    type_registration_complete_waiter: TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeChangeSetInputWaitTypeDef,
    DescribeStackRefactorInputWaitExtraTypeDef,
    DescribeStackRefactorInputWaitTypeDef,
    DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef,
    DescribeStacksInputWaitExtraExtraExtraExtraTypeDef,
    DescribeStacksInputWaitExtraExtraExtraTypeDef,
    DescribeStacksInputWaitExtraExtraTypeDef,
    DescribeStacksInputWaitExtraTypeDef,
    DescribeStacksInputWaitTypeDef,
    DescribeTypeRegistrationInputWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackRefactorCreateCompleteWaiter",
    "StackRefactorExecuteCompleteWaiter",
    "StackRollbackCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)

class ChangeSetCreateCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/ChangeSetCreateComplete.html#CloudFormation.Waiter.ChangeSetCreateComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#changesetcreatecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChangeSetInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/ChangeSetCreateComplete.html#CloudFormation.Waiter.ChangeSetCreateComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#changesetcreatecompletewaiter)
        """

class StackCreateCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackCreateComplete.html#CloudFormation.Waiter.StackCreateComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackcreatecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackCreateComplete.html#CloudFormation.Waiter.StackCreateComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackcreatecompletewaiter)
        """

class StackDeleteCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackDeleteComplete.html#CloudFormation.Waiter.StackDeleteComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackdeletecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackDeleteComplete.html#CloudFormation.Waiter.StackDeleteComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackdeletecompletewaiter)
        """

class StackExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackExists.html#CloudFormation.Waiter.StackExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackExists.html#CloudFormation.Waiter.StackExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackexistswaiter)
        """

class StackImportCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackImportComplete.html#CloudFormation.Waiter.StackImportComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackimportcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitExtraExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackImportComplete.html#CloudFormation.Waiter.StackImportComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackimportcompletewaiter)
        """

class StackRefactorCreateCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRefactorCreateComplete.html#CloudFormation.Waiter.StackRefactorCreateComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrefactorcreatecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStackRefactorInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRefactorCreateComplete.html#CloudFormation.Waiter.StackRefactorCreateComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrefactorcreatecompletewaiter)
        """

class StackRefactorExecuteCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRefactorExecuteComplete.html#CloudFormation.Waiter.StackRefactorExecuteComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrefactorexecutecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStackRefactorInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRefactorExecuteComplete.html#CloudFormation.Waiter.StackRefactorExecuteComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrefactorexecutecompletewaiter)
        """

class StackRollbackCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRollbackComplete.html#CloudFormation.Waiter.StackRollbackComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrollbackcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackRollbackComplete.html#CloudFormation.Waiter.StackRollbackComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackrollbackcompletewaiter)
        """

class StackUpdateCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackUpdateComplete.html#CloudFormation.Waiter.StackUpdateComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackupdatecompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/StackUpdateComplete.html#CloudFormation.Waiter.StackUpdateComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#stackupdatecompletewaiter)
        """

class TypeRegistrationCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/TypeRegistrationComplete.html#CloudFormation.Waiter.TypeRegistrationComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#typeregistrationcompletewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTypeRegistrationInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/waiter/TypeRegistrationComplete.html#CloudFormation.Waiter.TypeRegistrationComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters/#typeregistrationcompletewaiter)
        """
