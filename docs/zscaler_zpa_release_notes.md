# ZPA リリースノート

> 最終更新: 2026-07-15 23:31 UTC  
> ソース: https://help.zscaler.com/zpa/release-notes

---

# ZPA Release Notes Index


## Internet & SaaS (ZIA) Release Notes

### Internet & SaaS Service Release Notes
- [Release Upgrade Summary (2026)](/zia/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](/zia/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](/zia/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](/zia/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](/zia/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](/zia/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](/zia/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](/zia/release-upgrade-summary-2019)

### Zscaler Endpoint DLP Release Notes
- [Zscaler Endpoint DLP Release Summary (2026)](/zia/zscaler-endpoint-dlp-release-summary-2026)

## Private Access (ZPA) Release Notes

### ZPA Service Release Notes
- [Release Upgrade Summary (2026)](/zpa/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](/zpa/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](/zpa/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](/zpa/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](/zpa/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](/zpa/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](/zpa/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](/zpa/release-upgrade-summary-2019)

### ZPA App Connector Release Notes
- [App Connector Release Summary (2026)](/zpa/app-connector-release-summary-2026)
- [App Connector Release Summary (2025)](/zpa/app-connector-release-summary-2025)
- [App Connector Release Summary (2024)](/zpa/app-connector-release-summary-2024)
- [App Connector Release Summary (2023)](/zpa/app-connector-release-summary-2023)
- [App Connector Release Summary (2022)](/zpa/app-connector-release-summary-2022)
- [App Connector Release Summary (2021)](/zpa/app-connector-release-summary-2021)
- [App Connector Release Summary (2020)](/zpa/app-connector-release-summary-2020)

### ZPA Private Service Edge Release Notes
- [ZPA Private Service Edge Release Summary (2026)](/zpa/zpa-private-service-edge-release-summary-2026)
- [ZPA Private Service Edge Release Summary (2025)](/zpa/zpa-private-service-edge-release-summary-2025)
- [ZPA Private Service Edge Release Summary (2024)](/zpa/zpa-private-service-edge-release-summary-2024)
- [ZPA Private Service Edge Release Summary (2023)](/zpa/zpa-private-service-edge-release-summary-2023)
- [ZPA Private Service Edge Release Summary (2022)](/zpa/zpa-private-service-edge-release-summary-2022)
- [ZPA Private Service Edge Release Summary (2021)](/zpa/zpa-private-service-edge-release-summary-2021)
- [ZPA Private Service Edge Release Summary (2020)](/zpa/zpa-private-service-edge-release-summary-2020)

## Digital Experience Monitoring (ZDX) Release Notes

## Workflow Automation Release Notes

## Data Security Posture Management (DSPM) Release Notes


# ZPA 2026 Release Upgrade Summary

This article provides a summary of all new features and enhancements per Zscaler cloud for the ZPA Admin Portal. To see scheduled maintenance updates for your cloud, visit the [Trust Portal](https://trust.zscaler.com/).

When Zscaler cloud and Admin Portal updates are deploying, some functionality will not be available until the deployment process completes.

## July 14, 2026

### Feature Available

#### journalctl Support for Remote Troubleshooting
Private Access (ZPA) supports the `journalctl` command for App Connectors, Private Service Edges, Private Cloud Controllers, and Network Connectors to collect service logs or full system logs for remote troubleshooting.

[See image.](#add-session)

To learn more, see [Accessing and Viewing Support Information](/zpa/accessing-and-viewing-support-information) or [Configuring VPN Diagnostic Sessions](/zpa/configuring-vpn-diagnostics-sessions).

![JOURNALCTL feature in the Add Session page](/sites/default/files/downloads/zpa/vpn-legacy-apps/vpn-configuration/configuring-network-segments/zpa-add-session-journalctl.png "The Add Session page")

## July 13, 2026

## July 10, 2026

### Feature Available

#### Agents Exclude Infrastructure Traffic from Flow Logs
Agents on the Windows operating system exclude infrastructure traffic (i.e., loopback IP addresses) from the flow logs, reducing noise and improving visibility. With this update, both Windows and Linux agents provide this streamlined flow data for organizations to monitor and analyze.

To learn more, see [About Flow Logs](/zpa/about-flow-logs).

### Feature Available

#### Automatic Session Restore for Isolation
Isolated sessions now automatically restore their web pages if they time out on a user's device. If a session is idle for longer than the timeout of 10 minutes, the isolated page automatically refreshes itself. When this action occurs, the banner notification announcing the start of isolation is disabled. This feature is different from Persistent State, which is enabled per isolation profile to carry over data from an expired session to a new session.

### Feature Available

#### Ubuntu Linux Support for Microsegmentation
Microsegmentation supports Ubuntu 26.04 LTS.

To learn more, see [Supported Versions & OS Compatibility for Microsegmentation](/zpa/supported-versions-os-compatibility-microsegmentation).

### Feature Available

#### Windows Support for Microsegmentation
Microsegmentation supports Microsoft Windows Server 2025.

To learn more, see [Supported Versions & OS Compatibility for Microsegmentation](/zpa/supported-versions-os-compatibility-microsegmentation).

## July 01, 2026

## June 29, 2026

### Feature Available

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for [App Connectors](/zpa/app-connector-deployment-guide-linux), [Private Service Edges](/zpa/private-service-edge-deployment-guide-linux), [Private Cloud Controllers](/zpa/private-cloud-controller-deployment-guide-linux), or [Network Connectors](/zpa/network-connector-deployment-guide-linux) from our repository. The Manager software version is 26.55.1.

To learn more, see [Understanding the Manager Software](/zpa/about-manager-software#managerUpgrades).

## June 23, 2026

## June 17, 2026

## June 12, 2026

### Feature Available

#### Resource Policy Rule Configuration Enhancements for Microsegmentation
There are several enhancements to resource policy rule configuration:

* Application Port Template: You can select destination ports that are in applications from the [Application Catalog](/zpa/about-application-catalog-microsegmentation).
* Manual Ports: You have the option to manually select ports for the TCP port ranges instead of using default status ports. Additionally, you can choose to include all available TCP ports.

To learn more, see [Configuring Microsegmentation Policies](/zpa/configuring-microsegmentation-policies).

## June 11, 2026

### Feature Available

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for [App Connectors](/zpa/app-connector-deployment-guide-linux), [Private Service Edges](/zpa/private-service-edge-deployment-guide-linux), [Private Cloud Controllers](/zpa/private-cloud-controller-deployment-guide-linux), or [Network Connectors](/zpa/network-connector-deployment-guide-linux) from our repository. The Manager software version is 26.54.6.

To learn more, see [Understanding the Manager Software](/zpa/understanding-manager-software).

## June 08, 2026

## June 02, 2026

### Feature Available

#### OAuth 2.0 Enrollment Support for Private Cloud Controllers
An update was released to support OAuth 2.0 enrollment for Private Cloud Controllers. OAuth 2.0 is the recommended method for enrollment for Private Access (ZPA), but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN `zpa-oauth.private.zscaler.com` must be allowlisted, and user devices must be allowed to make an outbound connection to the `zpa-oauth.private.zscaler.com` server. Refer to [config.zscaler.com/private.zscaler.com/zpa](https://config.zscaler.com/private.zscaler.com/zpa) (for the private.zscaler.com cloud) or [config.zscaler.com/zpatwo.net/zpa](https://config.zscaler.com/zpatwo.net/zpa) (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Private Cloud Controller version 25.47.3.

Supported virtual machine (VM) images automatically have this feature enabled. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available.   
  
The OAuth server only supports IPv4-based communication. If a Private Cloud Controller only has an IPV6 address, it cannot access the OAuth server.

[See image.](#add-enrollment-token)

To learn more, see [Configuring Private Cloud Controllers](/zpa/configuring-private-cloud-controllers).

![Add Private Cloud Controllers page](/sites/default/files/downloads/zpa/app-connector-management/app-connector-deployment-guides-supported-platforms/connector-deployment-guide-centos-oracle-and-redhat/zpa-pcc-add-pcc-xc.png "Add Private Cloud Controllers page in the Zscaler Admin Console")

### Feature Available

#### Updated Azure Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Microsoft Azure. These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see [App Connector Software by Platform](/zpa/zpa-app-connector-software-by-platform), [Private Service Edge Software by Platform](/zpa/private-service-edge-software-by-platform), and [Private Cloud Controller Software by Platform](/zpa/private-cloud-controller-software-platform).

### Feature Available

#### Updated GCP Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Google Cloud Platform (GCP). These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see [App Connector Software by Platform](/zpa/zpa-app-connector-software-by-platform), [Private Service Edge Software by Platform](/zpa/private-service-edge-software-by-platform), and [Private Cloud Controller Software by Platform](/zpa/private-cloud-controller-software-platform).

## June 01, 2026

### Feature Available

#### OAuth 2.0 Enrollment Support for Private Service Edges
An update was released to support OAuth 2.0 enrollment for Private Service Edges for Private Access (ZPA). OAuth 2.0 is the recommended method for enrollment for Private Access, but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN `zpa-oauth.private.zscaler.com` must be allowlisted, and user devices must be allowed to make an outbound connection to the `zpa-oauth.private.zscaler.com` server. Refer to [config.zscaler.com/private.zscaler.com/zpa](https://config.zscaler.com/private.zscaler.com/zpa) (for the private.zscaler.com cloud) or [config.zscaler.com/zpatwo.net/zpa](https://config.zscaler.com/zpatwo.net/zpa) (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Private Service Edge version 25.48.4.

Supported virtual machine (VM) images automatically have this feature enabled with the exception of Docker. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available.   
  
The OAuth server only supports IPv4-based communication. If a Private Service Edge only has an IPV6 address, it cannot access the OAuth server.

[See image.](#image)

To learn more, see [Configuring Private Service Edges](/zpa/configuring-service-edges).

![How to add a Private Service Edge ](/sites/default/files/downloads/zpa/vpn-legacy-apps/network-connector-deployment-guides-supported-platforms/network-connector-deployment-guide-linux/zpa-pse-add-pse-oauth.png "How to add a Private Service Edge ")

## May 29, 2026

### Feature Available

#### OAuth 2.0 Enrollment Support for Network Connectors
An update was released to support OAuth 2.0 enrollment for Network Connectors. OAuth 2.0 is the recommended method for enrollment for Private Access (ZPA), but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN `zpa-oauth.private.zscaler.com` must be allowlisted, and user devices must be allowed to make an outbound connection to the `zpa-oauth.private.zscaler.com` server. Refer to [config.zscaler.com/private.zscaler.com/zpa](https://config.zscaler.com/private.zscaler.com/zpa) (for the private.zscaler.com cloud) or [config.zscaler.com/zpatwo.net/zpa](https://config.zscaler.com/zpatwo.net/zpa) (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Network Connector version 25.47.3.

Supported prebuilt images automatically have this feature enabled. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available.   
  
The OAuth server only supports IPv4-based communication. If a Network Connector only has an IPV6 address, it cannot access the OAuth server.

[See image.](#add-enrollment-token)

To learn more, see [Configuring Network Connectors](/zpa/configuring-network-connectors).

![Add Network Connectors page](/sites/default/files/downloads/zpa/private-service-edge-management/private-service-edge-deployment-guides-supported-platforms/service-edge-deployment-guide-vmware/zpa-add-network-connectors.png "Add Network Connectors page in the Zscaler Admin Console")

## May 28, 2026

### Feature Available

#### Updated AWS Images for Private Service Edge and Private Cloud Controller
Updated Red Hat Enterprise Linux 9 Private Service Edge and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Amazon Web Services (AWS). These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see [Private Service Edge Software by Platform](/zpa/private-service-edge-software-by-platform) and [Private Cloud Controller Software by Platform](/zpa/private-cloud-controller-software-platform).

## May 26, 2026

### Feature Available

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for [App Connectors](/zpa/app-connector-deployment-guide-linux), [Private Service Edges](/zpa/private-service-edge-deployment-guide-linux), [Private Cloud Controllers](/zpa/private-cloud-controller-deployment-guide-linux), or [Network Connectors](/zpa/network-connector-deployment-guide-linux) from our repository. The Manager software version is 26.54.4.

To learn more, see [Understanding the Manager Software](/zpa/about-manager-software#managerUpgrades).

## May 22, 2026

### Feature Available

#### Enhancements for Isolation User Experience Loading Page
The following updates have been made to the isolation experience for Zero Trust Browser:

* As you enter an isolated session, a static, temporary message appears in the middle of the web page as it loads to confirm you are entering an isolated session. Additionally, an animated green outline appears around the website border as the page loads.  
  [See image.](#Entering-Zero-Trust-Mode)
* When the page has completely rendered, a [temporary notification banner](/zero-trust-browser/profiles/profile-notifications) appears in the upper-right corner that displays a customized notification title. You can click the Show More link in the banner to view a message customized by the admin.  
  [See image.](#Zero-Trust-Mode-Icon-and-Notification-Banner-condensed)
* A floating checkmark icon also appears when the page has completely rendered, and stays visible after the temporary notification banner disappears. This is a visual indicator that the isolation session is persisting and has not expired.  
  [See image.](#Zero-Trust-Mode-icon-and-expanded-message)

To learn more, see [Adding a Banner Theme for the Isolation End User Notification in ZIA](/zero-trust-browser/adding-banner-theme-isolation-end-user-notification-zia).

![A view of a web page entering Zero Trust Mode. ](/sites/default/files/downloads/zero-trust-browser/profiles/profile-notifications/adding-banner-theme-isolation-end-user-notification-zia/Entering-Zero-Trust-Mode_message_green-outline.png "A green outline appears around the web page as a notification message temporarily loads.")

![A view of a web page after it has completely loaded while in an isolated session.](/sites/default/files/downloads/zero-trust-browser/end-user-isolation-experience/user-experience-modes-isolation/UX-Phase-0_Notification-Banner-Show-More_squircles.png "The web page shows the temporary notification banner that appears when the user is in Zero Trust Mode and the active session icon at the bottom of the page.")

![A view of a web page after it has completely loaded while in an isolated session.](/sites/default/files/downloads/zero-trust-browser/end-user-isolation-experience/user-experience-modes-isolation/UX-Phase-0_Notification-Banner_Expanded_squircles.png "The web page shows the fully expanded temporary notification banner that appears when the user is in Zero Trust Mode and the active session icon at the bottom of the page.")

## May 20, 2026

### Feature Available

#### Updated OVA Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available. These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

The following updated images are available:

* Nutanix for App Connector and Private Service Edge
* VMware

To learn more, see [App Connector Software by Platform](/zpa/zpa-app-connector-software-by-platform), [Private Service Edge Software by Platform](/zpa/private-service-edge-software-by-platform), and [Private Cloud Controller Software by Platform](/zpa/private-cloud-controller-software-platform).

## May 19, 2026

## May 18, 2026

### Feature Available

#### Business Continuity Update
Improvements to LSS-based Log Streaming in Business Continuity were made to support log streaming across multiple Private Clouds.

To learn more, see [About Private Clouds](/zpa/about-private-clouds).

### Feature Available

#### Resolved Issues
Fixed an issue where a proxy configured on a Windows OS resulted in AppProtection custom controls not being applied to HTTPS traffic.

To learn more, see [About AppProtection Controls](/zpa/about-appprotection-controls).

## May 11, 2026

### Feature Available

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for [App Connectors](/zpa/app-connector-deployment-guide-linux), [Private Service Edges](/zpa/private-service-edge-deployment-guide-linux), [Private Cloud Controllers](/zpa/private-cloud-controller-deployment-guide-linux), or [Network Connectors](/zpa/network-connector-deployment-guide-linux) from our repository. The Manager software version is 26.54.2.

To learn more, see [Understanding the Manager Software](/zpa/about-manager-software#managerUpgrades).

## May 08, 2026

### Feature Available

#### Agent Telemetry Status Changes
Several new statuses are available for filtering Agent Telemetry results.

For agents, the following statuses are available:

* Up to Date: The new agent upgrade version number is either greater than or equal to the agent version number of its corresponding agent group.
* Pending: The new agent upgrade version number is less than the agent version number of its corresponding agent group.
* In Progress: The agent is actively upgrading, and will complete within 10 minutes of reaching this status.
* Forced Upgrade: The agent has manually been upgraded by an admin outside its configured upgrade schedule.
* Failed: An upgrade attempt has failed.
* N/A: The agent or its agent group is disabled.

For agent groups, the following statuses are available:

* Up to Date: All agents are up-to-date.
* Pending: At least one agent in the agent group is in a pending status for the latest agent version.
* In Progress: At least one agent in the agent group is actively upgrading.
* In Progress with Failures: Multiple agents in an agent group are upgrading with some in a failed state and the remaining agents proceeding.
* Failed: All agents within an agent group have reached a failed state.
* Completed with Failures: All agents within an agent group have completed the upgrade process with some in a failed state.
* N/A: The agent group is disabled.

To learn more, see [About Agent Telemetry](/zpa/about-agent-telemetry).

### Feature Available

#### Rule Order for Microsegmentation Policies
Microsegmentation policy rules are now organized by order instead of by priority numbers. Admins can re-order rules at any time and as many times as needed. Any rule order changes are tracked in Event Logs.

[See image.](#Edit-Rule-Order)

To learn more, see [Configuring Microsegmentation Policies](/zpa/configuring-microsegmentation-policies) and [About Event Logs](/zpa/about-event-logs).

![A view of the Edit Rule Order drawer.](/sites/default/files/downloads/zpa/microsegmentation/policy/editing-microsegmentation-policies/Edit-Rule-Order.png "The list shows the ability to enter a different order number for policy rules.")

## May 04, 2026

### Feature Available

#### Automated Manager Software Updates for App Connectors and Network Connectors
An update was released to support automated updates to the Manager software service for App Connector and Network Connector.

Automated Manager software updates are available with a Manager software version of 25.46.3 or later and an App Connector or Network Connector version of 25.46.3 or later.

The table includes the following updates:

* Version Profile: Displays the version profile applied to the App Connector or Network Connector. You can hover over the information icon under the Version Profile column heading to view the target version for the Manager software and App Connector or Network Connector software.

  [See image.](#version-profile)
* Software Update: Displays the status of the App Connector or Network Connector update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.
* Manager Update: Displays the status of the Manager software update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.

  [See image.](#mgr-update)
* When viewing details for an App Connector or Network Connector, you can view the Last Manager Update time.

  [See image.](#appc-details)

To learn more, see [About App Connectors](/zpa/about-connectors) or [About Network Connectors](/zpa/about-network-connectors).

Manager software updates are scheduled during the maintenance window for Private Access (ZPA) software updates.

![Version Profile Tooltip on the App Connectors Page in the ZPA Admin Portal](/sites/default/files/downloads/zpa/release-notes/zpa-service-release-notes/release-upgrade-summary-2025/zpa-appc-table-mgr-software.png "App Connector Page in the ZPA Admin Portal")

![Manager Software Tooltip on the App Connectors Page in the ZPA Admin Portal](/sites/default/files/downloads/zpa/release-notes/zpa-service-release-notes/release-upgrade-summary-2026/zpa-appc-table-mgr-software-aum.png "App Connectors Page in the ZPA Admin Portal")

![App Connector Details in the ZPA Admin Portal](/sites/default/files/downloads/zpa/release-notes/zpa-service-release-notes/release-upgrade-summary-2026/appc-table-details-aum_0.png "App Connector Details in the ZPA Admin Portal")

## May 01, 2026

### Feature Available

#### Hostname in VPN Connected Users
The client hostname was added to the VPN Connected Users page.

[See image.](#image)

To learn more, see [About VPN Connected Users](/zpa/about-vpn-connected-users).

![VPN Connected Users Page in the Zscaler Admin Console](/sites/default/files/downloads/zpa/release-notes/zpa-service-release-notes/release-upgrade-summary-2026/zpa-vpn-connected-user-hostname.png "VPN Connected Users Page in the Zscaler Admin Console")

## April 21, 2026

### Feature Available

#### Multiple Private Access Tenant Support with Authentication Service
An update was released to provide support for two Private Access (ZPA) tenants with a single Authentication Service tenant. Customers with more than one single Internet & SaaS (ZIA) and Private Access tenant can manage them in the Zscaler Admin Console.

[See image.](#account-settings)

To learn more, see [Customizing Your Account Settings](/unified/customizing-your-account-settings) and [Support for Integrating Two Private Access Tenants](/node/1538629).

![Changing the Default Private Access Cloud within the Zscaler Admin Console](/sites/default/files/downloads/zpa/authentication/identity-management/about-scim-groups/xc-account-settings-menu-rn.png "Changing the Default Private Access Cloud in the Account Settings Menu")

## April 16, 2026

## April 14, 2026

## April 09, 2026

### Feature Available

#### Anti-Tamper Protection for the Microsegmentation Agent
Anti-tamper protection for the Microsegmentation agent ensures that the agent service (e.g., reporting, enforcement, and upgrades) can't be maliciously disabled or altered. This includes alterations attempted by an untrusted actor running with admin privileges.

### Feature Available

#### Kubernetes Updates for Microsegmentation
Microsegmentation now extends support for Azure Kubernetes Service (AKS) and Google Kubernetes Engine (GKE). Customers can install the Microsegmentation agent for these services to gain visibility to Kubernetes inventory and flow logs.

To learn more [About Kubernetes Clusters for Microsegmentation](/zpa/about-kubernetes-clusters-microsegmentation).

### Feature Available

#### SLES 15 Support for Agent Installation in Microsegmentation
The Microsegmentation agent can now be installed on Suse Linux Enterprise Server 15.

To learn more, see [Installing & Upgrading the Agent Manager](/zpa/installing-upgrading-agent-manager) and [Supported Versions & OS Compatibility for Microsegmentation](/zpa/supported-versions-os-compatibility-microsegmentation).

## April 02, 2026

### Feature Available

#### VPN (for Legacy Apps) Resolved Issue
A fix was released to address a misconfiguration in `/etc/logrotate.d/frr` that caused the logrotate service not to start for Network Connectors and VPN Service Edges.

## April 01, 2026

### Feature Available

#### Client Connector Trusted Network Criteria Option
You can select Client Connector Trusted Network as a criteria option for the timeout policy. Client Connector Trusted Network allows users who are working from secure locations to be designated as part of a trusted network. This results in fewer reauthentication requests for trusted network users, as opposed to untrusted network users (e.g., road warriors, contractors, etc.) that require frequent reauthentication. You can view the analytics of Client Connector Trusted Networks by selecting the Timeout Policy Blocks on the User Activity Diagnostics page.

To learn more, see [Configuring Timeout Policies](/zpa/configuring-timeout-policies).

## March 31, 2026

### Feature Available

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for [App Connectors](/zpa/app-connector-deployment-guide-linux), [Private Service Edges](/zpa/private-service-edge-deployment-guide-linux), [Private Cloud Controllers](/zpa/private-cloud-controller-deployment-guide-linux), or [Network Connectors](/zpa/network-connector-deployment-guide-linux) from our repository. The Manager software version is 26.53.4.

To learn more, see [Understanding the Manager Software](/zpa/about-manager-software#managerUpgrades).