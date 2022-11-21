"""
Type annotations for cloudformation service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudformation import CloudFormationClient
    from mypy_boto3_cloudformation.waiter import (
        ChangeSetCreateCompleteWaiter,
        StackCreateCompleteWaiter,
        StackDeleteCompleteWaiter,
        StackExistsWaiter,
        StackImportCompleteWaiter,
        StackRollbackCompleteWaiter,
        StackUpdateCompleteWaiter,
        TypeRegistrationCompleteWaiter,
    )

    client: CloudFormationClient = boto3.client("cloudformation")

    change_set_create_complete_waiter: ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
    stack_create_complete_waiter: StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
    stack_delete_complete_waiter: StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
    stack_exists_waiter: StackExistsWaiter = client.get_waiter("stack_exists")
    stack_import_complete_waiter: StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
    stack_rollback_complete_waiter: StackRollbackCompleteWaiter = client.get_waiter("stack_rollback_complete")
    stack_update_complete_waiter: StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
    type_registration_complete_waiter: TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackRollbackCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)

class ChangeSetCreateCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#changesetcreatecompletewaiter)
    """

    def wait(
        self,
        *,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#changesetcreatecompletewaiter)
        """

class StackCreateCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackcreatecompletewaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackcreatecompletewaiter)
        """

class StackDeleteCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackdeletecompletewaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackdeletecompletewaiter)
        """

class StackExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackexistswaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackexistswaiter)
        """

class StackImportCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackimportcompletewaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackimportcompletewaiter)
        """

class StackRollbackCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackrollbackcompletewaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackrollbackcompletewaiter)
        """

class StackUpdateCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackupdatecompletewaiter)
    """

    def wait(
        self,
        *,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackupdatecompletewaiter)
        """

class TypeRegistrationCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#typeregistrationcompletewaiter)
    """

    def wait(self, *, RegistrationToken: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#typeregistrationcompletewaiter)
        """
