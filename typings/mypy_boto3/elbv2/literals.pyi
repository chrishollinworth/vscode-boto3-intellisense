"""
Type annotations for elbv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/literals.html)

Usage::

    ```python
    from mypy_boto3_elbv2.literals import ActionTypeEnumType

    data: ActionTypeEnumType = "authenticate-cognito"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionTypeEnumType",
    "AuthenticateCognitoActionConditionalBehaviorEnumType",
    "AuthenticateOidcActionConditionalBehaviorEnumType",
    "DescribeAccountLimitsPaginatorName",
    "DescribeListenerCertificatesPaginatorName",
    "DescribeListenersPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "DescribeRulesPaginatorName",
    "DescribeSSLPoliciesPaginatorName",
    "DescribeTargetGroupsPaginatorName",
    "IpAddressTypeType",
    "LoadBalancerAvailableWaiterName",
    "LoadBalancerExistsWaiterName",
    "LoadBalancerSchemeEnumType",
    "LoadBalancerStateEnumType",
    "LoadBalancerTypeEnumType",
    "LoadBalancersDeletedWaiterName",
    "ProtocolEnumType",
    "RedirectActionStatusCodeEnumType",
    "TargetDeregisteredWaiterName",
    "TargetHealthReasonEnumType",
    "TargetHealthStateEnumType",
    "TargetInServiceWaiterName",
    "TargetTypeEnumType",
)

ActionTypeEnumType = Literal[
    "authenticate-cognito", "authenticate-oidc", "fixed-response", "forward", "redirect"
]
AuthenticateCognitoActionConditionalBehaviorEnumType = Literal["allow", "authenticate", "deny"]
AuthenticateOidcActionConditionalBehaviorEnumType = Literal["allow", "authenticate", "deny"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeListenerCertificatesPaginatorName = Literal["describe_listener_certificates"]
DescribeListenersPaginatorName = Literal["describe_listeners"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
DescribeRulesPaginatorName = Literal["describe_rules"]
DescribeSSLPoliciesPaginatorName = Literal["describe_ssl_policies"]
DescribeTargetGroupsPaginatorName = Literal["describe_target_groups"]
IpAddressTypeType = Literal["dualstack", "ipv4"]
LoadBalancerAvailableWaiterName = Literal["load_balancer_available"]
LoadBalancerExistsWaiterName = Literal["load_balancer_exists"]
LoadBalancerSchemeEnumType = Literal["internal", "internet-facing"]
LoadBalancerStateEnumType = Literal["active", "active_impaired", "failed", "provisioning"]
LoadBalancerTypeEnumType = Literal["application", "gateway", "network"]
LoadBalancersDeletedWaiterName = Literal["load_balancers_deleted"]
ProtocolEnumType = Literal["GENEVE", "HTTP", "HTTPS", "TCP", "TCP_UDP", "TLS", "UDP"]
RedirectActionStatusCodeEnumType = Literal["HTTP_301", "HTTP_302"]
TargetDeregisteredWaiterName = Literal["target_deregistered"]
TargetHealthReasonEnumType = Literal[
    "Elb.InitialHealthChecking",
    "Elb.InternalError",
    "Elb.RegistrationInProgress",
    "Target.DeregistrationInProgress",
    "Target.FailedHealthChecks",
    "Target.HealthCheckDisabled",
    "Target.InvalidState",
    "Target.IpUnusable",
    "Target.NotInUse",
    "Target.NotRegistered",
    "Target.ResponseCodeMismatch",
    "Target.Timeout",
]
TargetHealthStateEnumType = Literal[
    "draining", "healthy", "initial", "unavailable", "unhealthy", "unused"
]
TargetInServiceWaiterName = Literal["target_in_service"]
TargetTypeEnumType = Literal["instance", "ip", "lambda"]
