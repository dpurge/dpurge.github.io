# Identity and access management

## Microsoft Entra ID

Identity and access management service.
Enables you to sign in and access Microsoft cloud applications and cloud applications that you develop.

Provides:

- *Authentication*: verifying identity to access applications and resources; self-service password reset; multifactor authentication; a custom list of banned passwords; smart lockout services
- *Single sign-on*: one username and one password to access multiple applications
- *Application management*: manage cloud and on-premises apps
- *Device management*: registration of devices; enables devices to be managed through tools like Microsoft Intune; allows for device-based Conditional Access policies

You can connect on-prem Active Directory with Microsoft Entra ID, enabling a consistent identity experience between cloud and on-premises.

Microsoft Entra Connect synchronizes user identities between on-premises Active Directory and Microsoft Entra ID, so you can use SSO, multifactor authentication, self-service password reset under both systems.

## Microsoft Entra Domain Services

Provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/NTLM authentication.

Lets you run legacy applications in the cloud that can't use modern authentication methods.

Runs on a replica set - two Windows Server domain controllers deployed into your selected Azure region.
You don't manage, configure, or update these DCs. The Azure platform handles the DCs as part of the managed domain, including backups and encryption at rest using Azure Disk Encryption.

A managed domain performs a one-way synchronization from Microsoft Entra ID to Microsoft Entra Domain Services. You can create resources directly in the managed domain, but they aren't synchronized back to Microsoft Entra ID. In a hybrid environment with an on-premises AD DS environment, Microsoft Entra Connect synchronizes identity information with Microsoft Entra ID, which is then synchronized to the managed domain.

## Authentication methods

Single sign-on (SSO) enables a user to sign in one time and use that credential to access multiple resources and applications from different providers. For SSO to work, the different applications and providers must trust the initial authenticator.

Multifactor authentication is the process of prompting a user for an extra form (or factor) of identification during the sign-in process. MFA helps protect against a password compromise in situations where the password was compromised but the second factor wasn't.
Increases identity security by limiting the impact of credential exposure.

Passwordless authentication - the password is removed and replaced with something you have, plus something you are, or something you know.
Passwordless authentication needs to be set up on a device before it can work. Once it’s been registered or enrolled, Azure now knows that it’s associated with you. Now that the computer is known, once you provide something you know or are (such as a PIN or fingerprint), you can be authenticated without using a password.

Microsoft global Azure and Azure Government offer the following three passwordless authentication options that integrate with Microsoft Entra ID:

- Windows Hello for Business
- Microsoft Authenticator app
- FIDO2 security keys (FIDO2 security keys are typically USB devices, but could also use Bluetooth or NFC)

## Azure external identities

An external identity is a person, device, service, etc. that is outside your organization.
The external user’s identity provider manages their identity, and you manage access to your apps with Microsoft Entra ID or Azure AD B2C to keep your resources protected.

- Business to business (B2B) collaboration - external users use their preferred identity to sign-in to your applications; B2B collaboration users are represented in your directory, typically as guest users.
- B2B direct connect - mutual, two-way trust with another Microsoft Entra organization; B2B direct connect currently supports Teams shared channels, enabling external users to access your resources from within their home instances of Teams. B2B direct connect users aren't represented in your directory, but they're visible from within the Teams shared channel and can be monitored in Teams admin center reports.
- Microsoft Azure Active Directory business to customer (B2C)

## Azure conditional access

Conditional Access is a tool that Microsoft Entra ID uses to allow (or deny) access to resources based on identity signals. These signals include who the user is, where the user is, and what device the user is requesting access from.

A user might not be challenged for second authentication factor if they're at a known location. However, they might be challenged for a second authentication factor if their sign-in signals are unusual or they're at an unexpected location.

During sign-in, Conditional Access collects signals from the user, makes decisions based on those signals, and then enforces that decision by allowing or denying the access request or challenging for a multifactor authentication response.

The signal might be the user's location, the user's device, or the application that the user is trying to access.

## Azure role-based access control

Each role has an associated set of access permissions that relate to that role. When you assign individuals or groups to one or more roles, they receive all the associated access permissions.

Role-based access control is applied to a scope, which is a resource or set of resources that this access applies to.

Scopes:

- management group (a collection of multiple subscriptions)
- single subscription
- resource group
- single resource

Azure RBAC is hierarchical; when you grant access at a parent scope, those permissions are inherited by all child scopes.

Azure RBAC doesn't enforce access permissions at the application or data level.

## Zero Trust model

Zero Trust is a security model that assumes the worst case scenario and protects resources with that expectation. Zero Trust assumes breach at the outset, and then verifies each request as though it originated from an uncontrolled network.
