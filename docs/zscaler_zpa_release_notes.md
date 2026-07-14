# ZPA リリースノート

> 最終更新: 2026-07-14 23:20 UTC
> ソース: https://help.zscaler.com/zpa/release-notes

---

## Release Upgrade Summary (2026)

This article provides a summary of all new features and enhancements per Zscaler cloud for the ZPA Admin Portal. To see scheduled maintenance updates for your cloud, visit the Trust Portal .

When Zscaler cloud and Admin Portal updates are deploying, some functionality will not be available until the deployment process completes.

### 関連記事（他年度）
- [Release Upgrade Summary (2026)](https://help.zscaler.com/zpa/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](https://help.zscaler.com/zpa/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](https://help.zscaler.com/zpa/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](https://help.zscaler.com/zpa/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](https://help.zscaler.com/zpa/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](https://help.zscaler.com/zpa/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](https://help.zscaler.com/zpa/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](https://help.zscaler.com/zpa/release-upgrade-summary-2019)

## 2026年 リリースノート一覧

Zscalerクラウド: private.zscaler.com


### July 14, 2026

#### journalctl Support for Remote Troubleshooting
Private Access (ZPA) supports the journalctl command for App Connectors, Private Service Edges, Private Cloud Controllers, and Network Connectors to collect service logs or full system logs for remote troubleshooting.

 See image. 

To learn more, see Accessing and Viewing Support Information or Configuring VPN Diagnostic Sessions .


### July 13, 2026

#### Get Network Interfaces Support for App Connectors
Private Access (ZPA) supports the Get Network Interfaces command to collect a list of network interfaces used by an App Connector to help with remote troubleshooting.

 See image. 

To learn more, see Accessing and Viewing Support Information .

#### Network Settings Configuration for App Connectors
Network settings for App Connectors help improve administrative efficiency and support secure integration. You can configure settings to perform remote commands that enable SSH on the OS, and also update software interface settings across Private Access (ZPA) virtual machines, such as AWS, Azure, and GCP.

 See image. 

To learn more, see About App Connector Groups .


### July 10, 2026

#### Agents Exclude Infrastructure Traffic from Flow Logs
Agents on the Windows operating system exclude infrastructure traffic (i.e., loopback IP addresses) from the flow logs, reducing noise and improving visibility. With this update, both Windows and Linux agents provide this streamlined flow data for organizations to monitor and analyze.

To learn more, see About Flow Logs .

#### Automatic Session Restore for Isolation
Isolated sessions now automatically restore their web pages if they time out on a user's device. If a session is idle for longer than the timeout of 10 minutes, the isolated page automatically refreshes itself. When this action occurs, the banner notification announcing the start of isolation is disabled. This feature is different from Persistent State, which is enabled per isolation profile to carry over data from an expired session to a new session.

#### Ubuntu Linux Support for Microsegmentation
Microsegmentation supports Ubuntu 26.04 LTS.

To learn more, see Supported Versions & OS Compatibility for Microsegmentation .

#### Windows Support for Microsegmentation
Microsegmentation supports Microsoft Windows Server 2025.

To learn more, see Supported Versions & OS Compatibility for Microsegmentation .


### July 01, 2026

#### Enterprise Browser for Zero Trust Browser
The Enterprise Browser feature for Zero Trust Browser is a way to protect users from everyday browser-based threats. Users can access private applications for their organization while utilizing browser protection for daily operations such as file transfer, data sharing, and cloud service authentication.

To learn more, see Understanding Enterprise Browser .


### June 29, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.55.1.

To learn more, see Understanding the Manager Software .


### June 23, 2026

#### Device Posture Profile Failure Notification
You can configure device posture profile failure notifications when you create an access policy. This feature notifies end users when a device posture check fails for associated Zscaler Client Connector posture profiles. Click Manage Notifications in the Add Access Policy window to set up notification messages in the Zscaler Client Connector Portal.

 See image. 

To learn more, see Configuring Access Policies .

#### New API Service to Monitor App Connector Health
A new Event Monitoring & Notification API service monitors the health of App Connectors to ensure optimal performance and helps you make informed decisions about resource allocations. You can monitor the following health diagnostics, App Connector status, and network detail events:
 
- CPU threshold violations
- Memory threshold violations
- Disk space alerts
- Bandwidth utilization events
- File descriptor exhaustion
- CPU starvation events
- Control connection disconnections
- Connection status (UP/DOWN)
- Private IP addresses
- Public IP addresses
- Authentication events
- Connector identity and grouping 
To learn more, see Understanding the Event Monitoring & Notification API .

#### Viewing Diagnostics for VPN Access Policy Data
On the Access Policy Data Diagnostics page, you can view comprehensive VPN access policy logs and diagnostic data. This page is designed to streamline troubleshooting and provide deeper visibility into organizational connectivity.

 See image. 

To learn more, see About VPN Access Policy Data Diagnostics .

#### Viewing Diagnostics for VPN Traffic Flow Logs
On the Traffic Flow Logs Diagnostics page, you can view comprehensive VPN connection traffic flow logs and diagnostic data. This page is designed to streamline troubleshooting and provide deeper visibility into organizational connectivity.

 See image. 

To learn more, see About VPN Traffic Flow Logs Diagnostics .

#### Viewing Diagnostics for VPN User Logs
On the User Logs Diagnostics page, you can view comprehensive VPN user connection logs and diagnostic data. This page is designed to streamline troubleshooting and provide deeper visibility into organizational connectivity.

 See image. 

To learn more, see About VPN User Logs Diagnostics .

#### VPN Service Edges Dashboard
The VPN Service Edges Dashboard shows the total number of Zscaler Client Connectors, Network Connectors, and VPN Service Edges and their total data transfer to help determine when more resources need to be added.

 See image.


### June 17, 2026

#### Log Streaming Service (LSS) Support in Microtenants
The Log Streaming Service (LSS) is supported at the Microtenant level. Admins can configure and manage log receivers in Microtenants. When the LSS is configured at the Microtenant level, shared application logs are visible for the respective LSS configuration of the Microtenant. If a Microtenant is disabled, then only audit logs are streamed to the log receiver.

 See image. 

To learn more, see About Microtenants , Sharing Defined Application Segments , and Configuring a Log Receiver .


### June 12, 2026

#### Resource Policy Rule Configuration Enhancements for Microsegmentation
There are several enhancements to resource policy rule configuration:
 
- Application Port Template: You can select destination ports that are in applications from the Application Catalog.
- Manual Ports: You have the option to manually select ports for the TCP port ranges instead of using default status ports. Additionally, you can choose to include all available TCP ports. 
To learn more, see Configuring Microsegmentation Policies .


### June 11, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.54.6.

To learn more, see Understanding the Manager Software .


### June 08, 2026

#### Support for AppProtection with Multimatch
AppProtection and Multimatch can be configured for the same application segment.

To learn more, see Configuring Defined Application Segments and Using Application Segment Multimatch .


### June 02, 2026

#### OAuth 2.0 Enrollment Support for Private Cloud Controllers
An update was released to support OAuth 2.0 enrollment for Private Cloud Controllers. OAuth 2.0 is the recommended method for enrollment for Private Access (ZPA), but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN zpa-oauth.private.zscaler.com must be allowlisted, and user devices must be allowed to make an outbound connection to the zpa-oauth.private.zscaler.com server. Refer to config.zscaler.com/private.zscaler.com/zpa (for the private.zscaler.com cloud) or config.zscaler.com/zpatwo.net/zpa (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Private Cloud Controller version 25.47.3.

Supported virtual machine (VM) images automatically have this feature enabled. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available. 

 The OAuth server only supports IPv4-based communication. If a Private Cloud Controller only has an IPV6 address, it cannot access the OAuth server. 

 See image. 

To learn more, see Configuring Private Cloud Controllers .

#### Updated Azure Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Microsoft Azure. These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see App Connector Software by Platform , Private Service Edge Software by Platform , and Private Cloud Controller Software by Platform .

#### Updated GCP Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Google Cloud Platform (GCP). These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see App Connector Software by Platform , Private Service Edge Software by Platform , and Private Cloud Controller Software by Platform .


### June 01, 2026

#### OAuth 2.0 Enrollment Support for Private Service Edges
An update was released to support OAuth 2.0 enrollment for Private Service Edges for Private Access (ZPA). OAuth 2.0 is the recommended method for enrollment for Private Access, but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN zpa-oauth.private.zscaler.com must be allowlisted, and user devices must be allowed to make an outbound connection to the zpa-oauth.private.zscaler.com server. Refer to config.zscaler.com/private.zscaler.com/zpa (for the private.zscaler.com cloud) or config.zscaler.com/zpatwo.net/zpa (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Private Service Edge version 25.48.4.

Supported virtual machine (VM) images automatically have this feature enabled with the exception of Docker. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available. 

 The OAuth server only supports IPv4-based communication. If a Private Service Edge only has an IPV6 address, it cannot access the OAuth server. 

 See image. 

 To learn more, see Configuring Private Service Edges .

#### Redactive Sensitive Text for Isolation in Private Access
Zero Trust Browser allows admins to enable the redaction of sensitive text data for configured Data Loss Prevention (DLP) engines and dictionaries based on the DLP configuration in an isolation profile.

 See image. 

To learn more, see Using Redactive Sensitive Text for Isolation and Creating Isolation Profiles for Private Access .


### May 29, 2026

#### OAuth 2.0 Enrollment Support for Network Connectors
An update was released to support OAuth 2.0 enrollment for Network Connectors. OAuth 2.0 is the recommended method for enrollment for Private Access (ZPA), but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN zpa-oauth.private.zscaler.com must be allowlisted, and user devices must be allowed to make an outbound connection to the zpa-oauth.private.zscaler.com server. Refer to config.zscaler.com/private.zscaler.com/zpa (for the private.zscaler.com cloud) or config.zscaler.com/zpatwo.net/zpa (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a minimum version of Manager software and Network Connector version 25.47.3.

Supported prebuilt images automatically have this feature enabled. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available. 

 The OAuth server only supports IPv4-based communication. If a Network Connector only has an IPV6 address, it cannot access the OAuth server. 

 See image. 

To learn more, see Configuring Network Connectors .


### May 28, 2026

#### Updated AWS Images for Private Service Edge and Private Cloud Controller
Updated Red Hat Enterprise Linux 9 Private Service Edge and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available for Amazon Web Services (AWS). These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

To learn more, see Private Service Edge Software by Platform and Private Cloud Controller Software by Platform .

#### High-Performance Hardware Appliances for App Connectors and Private Service Edges
High-performance and high-throughput hardware appliances are available for App Connectors and Private Service Edges for Private Access (ZPA) to provide connectivity between sites and users accessing large files, such as medical records or imaging files. These hardware appliances include:
 
- A single, high-performance App Connector or Private Service Edge.
- At least 3 Gbps throughput performance per appliance. 
To learn more, see Understanding ZPA Appliances .


### May 26, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.54.4.

To learn more, see Understanding the Manager Software .

#### Support for End User Migration to Authentication Service
An update was released to provide support for end user migration to Authentication Service. This update ensures that the set of existing Private Access (ZPA) end users and their entitlements remain accurate and consistent throughout the migration process. During migration, external IdP configurations are view only. After migration is complete, the following conditions apply:
 
- IdP configurations are inactive but can be restored if necessary.
- Private Access no longer syncs users from external IdPs, and new external IdP configurations are not allowed.
- Authentication Service becomes the identity service for all Zscaler products, centralizing all identity management. 
As part of this release, you can select the External IAM IdP (i.e., the external IdP attribute created in Authentication Service) when configuring a policy or a Microtenant.

To learn more, see Migrating Private Access End Users to Authentication Service , Migrating End Users to Authentication Service , Migrating Zscaler Service Admins to Authentication Service , Configuring Microtenants , Policies , and Support for End User Migration .


### May 22, 2026

#### Enhancements for Isolation User Experience Loading Page
The following updates have been made to the isolation experience for Zero Trust Browser:
 
- As you enter an isolated session, a static, temporary message appears in the middle of the web page as it loads to confirm you are entering an isolated session. Additionally, an animated green outline appears around the website border as the page loads.
See image.
- When the page has completely rendered, a temporary notification banner appears in the upper-right corner that displays a customized notification title. You can click the Show More link in the banner to view a message customized by the admin.
See image.
- A floating checkmark icon also appears when the page has completely rendered, and stays visible after the temporary notification banner disappears. This is a visual indicator that the isolation session is persisting and has not expired.
See image. 
To learn more, see Adding a Banner Theme for the Isolation End User Notification in ZIA .


### May 20, 2026

#### Updated OVA Images
Updated Red Hat Enterprise Linux 9 App Connector, Private Service Edge, and Private Cloud Controller STIG-hardened images with FIPS enabled by default are available. These image updates address the removal of FIPS enablement by Red Hat from the STIG playbook.

The following updated images are available:
 
- Nutanix for App Connector and Private Service Edge
- VMware 
To learn more, see App Connector Software by Platform , Private Service Edge Software by Platform , and Private Cloud Controller Software by Platform .


### May 19, 2026

#### Default AppProtection Profile and Recommended Controls
The AppProtection default profile was renamed to Recommended OWASP Top 10 Profile. When you add or edit an AppProtection profile, using the default profile automatically selects recommended controls for OWASP predefined controls and ThreatLabZ controls. You can also select the Use Recommended Controls checkbox for these two control types, and also select the option to automatically add ThreatLabZ recommended controls.

 See image. 

To learn more, see About AppProtection Profiles and Configuring AppProtection Profiles .


### May 18, 2026

#### Business Continuity Update
Improvements to LSS-based Log Streaming in Business Continuity were made to support log streaming across multiple Private Clouds.

To learn more, see About Private Clouds .

#### Resolved Issues
Fixed an issue where a proxy configured on a Windows OS resulted in AppProtection custom controls not being applied to HTTPS traffic.

To learn more, see About AppProtection Controls .


### May 11, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.54.2.

To learn more, see Understanding the Manager Software .


### May 08, 2026

#### Agent Telemetry Status Changes
Several new statuses are available for filtering Agent Telemetry results.

For agents, the following statuses are available:
 
- Up to Date: The new agent upgrade version number is either greater than or equal to the agent version number of its corresponding agent group.
- Pending: The new agent upgrade version number is less than the agent version number of its corresponding agent group.
- In Progress: The agent is actively upgrading, and will complete within 10 minutes of reaching this status.
- Forced Upgrade: The agent has manually been upgraded by an admin outside its configured upgrade schedule.
- Failed: An upgrade attempt has failed.
- N/A: The agent or its agent group is disabled. 
For agent groups, the following statuses are available:
 
- Up to Date: All agents are up-to-date.
- Pending: At least one agent in the agent group is in a pending status for the latest agent version.
- In Progress: At least one agent in the agent group is actively upgrading.
- In Progress with Failures: Multiple agents in an agent group are upgrading with some in a failed state and the remaining agents proceeding.
- Failed: All agents within an agent group have reached a failed state.
- Completed with Failures: All agents within an agent group have completed the upgrade process with some in a failed state.
- N/A: The agent group is disabled. 
To learn more, see About Agent Telemetry .

#### Rule Order for Microsegmentation Policies
Microsegmentation policy rules are now organized by order instead of by priority numbers. Admins can re-order rules at any time and as many times as needed. Any rule order changes are tracked in Event Logs.

 See image. 

To learn more, see Configuring Microsegmentation Policies and About Event Logs .


### May 04, 2026

#### Automated Manager Software Updates for App Connectors and Network Connectors
An update was released to support automated updates to the Manager software service for App Connector and Network Connector.

Automated Manager software updates are available with a Manager software version of 25.46.3 or later and an App Connector or Network Connector version of 25.46.3 or later.

The table includes the following updates:
 
- Version Profile: Displays the version profile applied to the App Connector or Network Connector. You can hover over the information icon under the Version Profile column heading to view the target version for the Manager software and App Connector or Network Connector software.

See image.
- Software Update: Displays the status of the App Connector or Network Connector update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.
- Manager Update: Displays the status of the Manager software update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.

See image.
- When viewing details for an App Connector or Network Connector, you can view the Last Manager Update time.

See image. 
To learn more, see About App Connectors or About Network Connectors .

Manager software updates are scheduled during the maintenance window for Private Access (ZPA) software updates.


### May 01, 2026

#### Hostname in VPN Connected Users
The client hostname was added to the VPN Connected Users page.

 See image. 

To learn more, see About VPN Connected Users .

#### Automated Operating System Updates
An update was released to support automated security updates to the RHEL 9 operating system (OS) for App Connector, Private Service Edge for Private Access (ZPA), Private Cloud Controller, and Network Connector. This includes security updates and full OS updates.

Automated OS updates are only available for prebuilt App Connector, Private Service Edge, Private Cloud Controller, and Network Connector images on RHEL 9.x. App Connectors, Private Service Edges, Private Cloud Controllers, and Network Connectors installed manually using an RPM file on a custom RHEL 9.x build are not supported.

OS security updates are scheduled during the maintenance window for Private Access software updates.

The following updates are available:
 
- OS Update Filter: Sorts the table based on the status of the OS update (Success, Failure, Scheduled, etc.).
- OS Update: Displays the status of the OS update. You can hover over the information icon next to the update status to view more information, such as the update window and status of the update (Scheduled, Not Scheduled, In Progress, Success, or Failure).

See image.
- When viewing details for an App Connector, Private Service Edge, Private Cloud Controller, and Network Connector, the following information has been added:
View the Last OS update time.
- View whether OS updates have been enabled. 
 See image. 
 
To learn more, see About App Connectors , About Private Service Edges , About Private Cloud Controllers , or About Network Connectors .


### April 21, 2026

#### Multiple Private Access Tenant Support with Authentication Service
An update was released to provide support for two Private Access (ZPA) tenants with a single Authentication Service tenant. Customers with more than one single Internet & SaaS (ZIA) and Private Access tenant can manage them in the Zscaler Admin Console.

 See image. 

To learn more, see Customizing Your Account Settings and Support for Integrating Two Private Access Tenants .


### April 16, 2026

#### Tag Management for Defined Application Segments
Private Access (ZPA) supports Tag Management, which enables you to create, organize, and manage tags for classifying and grouping resources more effectively. Tag Management standardizes tagging across environments to simplify policy configuration and improve visibility into related resources within Private Access. To learn more, see About Tag Management for Application Segments .

 See image. 

With Tag Management, you can configure namespaces to logically organize tags and avoid naming conflicts, as well as add and configure tags within those namespaces. When configuring namespaces, you can assign optional values to tags to enable discovery and logical grouping, and configure tag groups by grouping related tags using shared values. To learn more, see Configuring Tags and Namespaces for Application Segments .

 See image. 

Namespaces and tags can be assigned to defined application segments. To learn more, see Configuring Defined Application Segments .

 See image. 

Tag groups and tag values can be assigned to access policies. To learn more, see Configuring Access Policy .

 See image. 

The maximum number of tags that can be created per Microtenant is 25,000. The maximum number of tags that can be created per customer is 25,000. To learn more, see Ranges & Limitations .


### April 14, 2026

#### Enhancements to AI-Powered Recommendations
An update was released to provide the following enhancements to the AI-Powered Recommendations page:
 
- Recommendations are sorted into intuitive categories for User Groups, Observed Users, and Application Type to improve discoverability and allow users to focus on relevant recommendations based on specific organizational contexts.
- Recommendations achieving less than 75% attack surface reduction (ASR) are included to provide visibility of recommendations that can still provide substantial implementation value. The default list of 100 recommendations includes items below this threshold.
- The Recommendation Details drawer has been improved to provide deeper insights and actionable data, including:Top-level metrics for Current Configuration, AI Recommendation, and ASR.
- Human-readable explanations for grouping hosts and recommending specific user groups.
- Dedicated tabs of reorganized information for Hosts, Observed Users, and Recommended Users. 
 See image. 

Customers with the Segmentation add-on license can request to update the total number of recommendations from 100 to 500.

To learn more, see About AI-Powered Recommendations for Application Segments .


### April 09, 2026

#### Anti-Tamper Protection for the Microsegmentation Agent
Anti-tamper protection for the Microsegmentation agent ensures that the agent service (e.g., reporting, enforcement, and upgrades) can't be maliciously disabled or altered. This includes alterations attempted by an untrusted actor running with admin privileges.

#### Kubernetes Updates for Microsegmentation
Microsegmentation now extends support for Azure Kubernetes Service (AKS) and Google Kubernetes Engine (GKE). Customers can install the Microsegmentation agent for these services to gain visibility to Kubernetes inventory and flow logs.

To learn more About Kubernetes Clusters for Microsegmentation .

#### SLES 15 Support for Agent Installation in Microsegmentation
The Microsegmentation agent can now be installed on Suse Linux Enterprise Server 15.

To learn more, see Installing & Upgrading the Agent Manager and Supported Versions & OS Compatibility for Microsegmentation .


### April 02, 2026

#### VPN (for Legacy Apps) Resolved Issue
A fix was released to address a misconfiguration in /etc/logrotate.d/frr that caused the logrotate service not to start for Network Connectors and VPN Service Edges.

#### Client Browser for Zero Trust Browser
Zero Trust Browser has been updated with several significant changes to provide seamless and secure enterprise access from any browser. The solution consists of three primary components: a browser extension that handles web-based security and access, a lightweight agent that enforces device posture controls and advanced data protection during the session, and a cloud browser for accessing private applications in an isolated session.

Zero Trust Browser implements the following security features through the combined extension and agent:
 
- Adaptive App Access: Enforcement of device posture controls to ensure that only compliant devices can access sensitive business applications.
- Browser-Based Threat Protection: Robust defense against malicious extensions, identity-based attacks, and emerging web threats.
- Data Exfiltration Prevention: Advanced security controls, including screenshot protection and keystroke logger prevention.

#### Support for Secondary DNS Servers in Network Segments
If users access an application via FQDN, you can assign a secondary DNS server as a backup in Network segments. This ensures DNS resolution remains close to the VPN Service Edge's physical location.

This feature requires Zscaler Client Connector 4.9 or later on Windows.

 See image. 

To learn more, see Configuring Network Segments .

#### VPN (for Legacy Apps) Diagnostics
An update was released to support logs and diagnostics data to help you analyze and troubleshoot issues for the following:
 
- VPN traffic flow logs. To learn more, see Viewing Diagnostics for VPN Traffic Flow Logs.
- VPN user logs. To learn more, see Viewing Diagnostics for VPN User Logs.


### April 01, 2026

#### Client Connector Trusted Network Criteria Option
You can select Client Connector Trusted Network as a criteria option for the timeout policy. Client Connector Trusted Network allows users who are working from secure locations to be designated as part of a trusted network. This results in fewer reauthentication requests for trusted network users, as opposed to untrusted network users (e.g., road warriors, contractors, etc.) that require frequent reauthentication. You can view the analytics of Client Connector Trusted Networks by selecting the Timeout Policy Blocks on the User Activity Diagnostics page.

To learn more, see Configuring Timeout Policies .


### March 31, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and Private Service Edge for Private Access (ZPA) RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.53.4.

To learn more, see Understanding the Manager Software .

#### Private Link Services
Private Access (ZPA) supports private link domains, allowing administrators to configure domain patterns that match private link CNAME records, including services such as Azure Private Link. This enables Private Access to correctly identify and route traffic to resources hosted behind private link endpoints while avoiding unnecessary routing for non-private resources.
 
 See image. 
 
To learn more, see Configuring Private Link Domains .


### March 26, 2026

#### Provisioning Key Not Found Event Updates
Details for App Connector name, the time the App Connector was modified, and who modified the App Connector were added to the raw logs of the Provisioning Key Not Found event in Events Diagnostics.
 
- View example log. 
To learn more, see Viewing and Managing Events Diagnostics .

 {
 "priority":"high",
 "customerId":"75057594037927936",
 "system":"assistant",
 "eventName":"PROVISIONING_KEY_NOT_FOUND",
 "time":"1775529452642",
 "category":"Enrollment",
 "otherFields":{
 "Last Modified By":"3",
 "l_disp":"bad",
 "App Connector Name":"35T6t508gqg2VtgbaYYaK3TBu-1775529451633",
 "fingerprint":"ASwjgKAgKf0q7sgDu1bhNFpJeko",
 "message":"Enrollment failed due to non-existing provisioning key."
 },
 "rowId":"4090396760_2294306628"
}


### March 20, 2026

#### Updated Network Connector AWS Image
An updated Red Hat Enterprise Linux 9 Network Connector AWS image is available to support the upcoming release of OAuth 2.0 enrollment.

To learn more, see Network Connector Software by Platform .


### March 19, 2026

#### Updated Network Connector Azure Image
An updated Red Hat Enterprise Linux 9 Network Connector Microsoft Azure image is available to support the upcoming release of OAuth 2.0 enrollment.

To learn more, see Network Connector Software by Platform .


### March 18, 2026

#### False Positive Rule Removals for OWASP Predefined Controls
False positive rules are being removed from the following OWASP_CRS control versions:
 
- OWASP_CRS/4.8.0: 46 false positive rules
- OWASP_CRS/3.3.5: 68 false positive rules
- OWASP_CRS/3.3.0: 68 false positive rules 
Any AppProtection profiles with these rules configured still display the rules, but the rules themselves are ineffective. Contact your Zscaler Account team for more information.

#### Updated Network Connector VMware Image
An updated Red Hat Enterprise Linux 9 Network Connector VMware image is available to support the upcoming release of OAuth 2.0 enrollment.

To learn more, see Network Connector Software by Platform .

#### VPN Service Edge Available in China
For organizations with the VPN (for Legacy Apps) service enabled, a VPN Service Edge is available in Beijing, China. This VPN Service Edge is only available to users in China to access applications in China. It should not be used to connect to applications outside of China, nor for users outside of China to connect to applications within China.

To learn more, see Deploying VPN Service Edges in China or About VPN Service Edges .


### March 09, 2026

#### Application Type Classification for Application and User Group Relationships
A column for Application Types is available on the Application and User Group Relationships Usage page to provide visibility on application usage reporting. The application types are also available when viewing the CSV file of the downloaded reports.
 
 See image. 
 
To learn more, see Viewing Application and User Group Relationships .


### March 06, 2026

#### Updated GCP Images
Updated Red Hat Enterprise Linux 9 Google Cloud Platform (GCP) images are available in the GCP Marketplace for App Connector, Private Service Edge, Private Cloud Controller, and Network Connector.

To learn more, see App Connector Software by Platform , Private Service Edge Software by Platform , Private Cloud Controller Software by Platform , and Network Connector Software by Platform .


### March 05, 2026

#### Agent Group and Custom Tags for ML Resource Group Recommendations in Microsegmentation
Machine learning (ML) resource group recommendations have been updated to include custom type tags and agent groups.

 See images. 

To learn more, see About ML Recommendations for Resource Groups .

#### Replacing or Migrating Existing Network Connectors with Network Connectors that Support Redundancy
For customers who are not yet running Network Connectors that support redundancy, Zscaler strongly recommends replacing or migrating existing Network Connectors with redundancy-capable Network Connectors. Network Connectors that support redundancy resolve the following failure scenarios:
 
- A Network Connector link failureAn internal link failure towards customer routers
- An external link failure towards the VPN Service Edge 
- A complete Network Connector node failure
- A data center failure with traffic rerouting towards another data center
- Scaling - ECMP (equal-cost multi-path) load balancing across Network Connectors from the VPN Service Edges and customer routers towards the Network Connector 
The redundancy design is based on External Border Gateway Protocol (EBGP) routing.

To learn more, see High Availability and Redundancy in VPN (for Legacy Apps) and Replacing or Migrating Existing Network Connectors with Network Connectors that Support Redundancy .


### March 03, 2026

#### Added Languages for International Keyboard Support for Privileged Remote Access
If you are using a privileged console with an RDP protocol for Privileged Remote Access (PRA), Zscaler has added support for additional keyboard languages: English (UK), Belgian French, Brazilian Portuguese, Swiss French, Swiss German, Hungarian, Italian, Norwegian, Spanish Latin American, Swedish, and Turkish (Q layout).

#### Credential Agent Available for Privileged Remote Access
A new credential agent is available for Privileged Remote Access (PRA) that enables ZPA integration with external identity sources, including Active Directory and Microsoft Entra ID, for credential discovery.

To learn more, see Credential Management for Privileged Remote Access .

#### Credential Management for Privileged Remote Access
You can deploy a credential agent to automate the discovery, synchronization, and lifecycle management of privileged credentials for Privileged Remote Access (PRA) in the Zscaler Admin Console. After configuring the credential agent, you can:
 
- Automatically discover credentials using LDAP queries from Active Directory (AD) or search queries from Microsoft Entra AD.
- Rotate credentials to generate new passwords with defined security requirements.
- Create rotation policies to set rotation schedules for credentials.
- Apply filters to automatically identify and pull newly created credentials from the AD.
- Manage existing credentials, discovered credentials, and ignored credentials.
- Organize privileged credentials into credential pools for policy mapping and injection.


### February 25, 2026

#### Manager Software Updates
A recommended update was released that includes updated App Connector and ZPA Private Service Edge RPM packages for Red Hat Enterprise Linux 8.x and 9.x, and Private Cloud Controller and Network Connector RPM packages for Red Hat Enterprise Linux 9.x.

You can download the Manager software for App Connectors , ZPA Private Service Edges , Private Cloud Controllers , or Network Connectors from our repository. The Manager software version is 26.52.3.

To learn more, see Understanding the Manager Software .


### February 24, 2026

#### Support for VPN Tunnels Connected from ZPA Private Service Edges
This release includes an update that supports VPN tunnels for users connected to ZPA Private Service Edges. With this update, Zscaler Client Connector users connected to ZPA Private Service Edges use public VPN Service Edges provisioned for the tenant in the Zscaler cloud.

To learn more, see About VPN Service Edges .


### February 17, 2026

#### OAuth 2.0 Enrollment Support for App Connectors
An update was released to support OAuth 2.0 enrollment for App Connectors. OAuth 2.0 is the recommended method for enrollment for ZPA, but provisioning key enrollment is also supported. To use OAuth 2.0, the OAuth server FQDN zpa-oauth.private.zscaler.com must be allowlisted, and user devices must be allowed to make an outbound connection to the zpa-oauth.private.zscaler.com server. Refer to config.zscaler.com/private.zscaler.com/zpa (for the private.zscaler.com cloud) or config.zscaler.com/zpatwo.net/zpa (for the zpatwo.net cloud) for the IP address to add to the allowlist.

OAuth 2.0 support is available with a Manager software and App Connector version 25.48.4.

Supported virtual machine (VM) images automatically have this feature enabled with the exception of Kubernetes, OpenShift, and Docker. Provisioning key enrollment is also supported on all VM images. The image attempts to use OAuth enrollment tokens by default but applies a provisioning key first if one is available. 

 The OAuth server only supports IPv4-based communication. If an App Connector only has an IPV6 address, it cannot access the OAuth server. 

OAuth 2.0 enrollment includes the following features:
 
- The pages for adding App Connectors have been simplified so you only need to select an App Connector group and up to 20 OAuth 2.0 enrollment tokens. If you add an App Connector to a previously created App Connector group without a signing certificate, you can select a certificate and add enrollment tokens from this page. To learn more, see Configuring App Connectors.

See image.
- The App Connector Groups table contains a new column that shows the number of App Connectors associated with each App Connector group. To learn more, see About App Connector Groups.

See image.
- The App Connector Groups details page includes a tab that shows the App Connectors in the current group. To learn more, see About App Connector Groups.

See image.
- You can create App Connector groups before configuring App Connectors to help streamline the process. The following tabs are also available:

Details tab: Configure group settings, including an option to select a signing certificate. With the previous provisioning key enrollment, the signing certificate was associated with the provisioning key. With this release, the signing certificate is associated with an App Connector group.

If you have an App Connector group that has its signing certificate associated with a provisioning key, and you add a new App Connector to that group using OAuth 2.0, you must edit the group and add the signing certificate to it.
- Update Settings tab: Set a version profile, select how often updates occur, or pause updates for App Connectors in this group. 
These options are also available when editing App Connector groups.

 See image. 
 
- On the App Connector Provisioning Keys page, you can select a provisioning key name to view details for the key, edit the key, or edit properties for the enrollment certificate. To learn more, see About App Connector Provisioning Keys.

See image.
- The Add App Connector Provisioning Key page lets you create a provisioning key and associate a group and signing certificate with the key.

See image.


### February 11, 2026

#### Access Policies for VPN (for Legacy Apps)
VPN (for Legacy Apps) provides access policy rules that can allow or block network traffic on VPN Service Edges. To create a rule, you need to define the source and destination IP addresses as well as the protocol used. An address book consists of Classless Inter-Domain Routing (CIDRs) and IP addresses that can be used as a source or destination network in multiple policy rules to help organize the network resources to protect.

Per ZPA policy evaluation, VPN (for Legacy Apps) evaluates access policy rules using a top-down, specific-match principle. Traffic that doesn't match any access policy rule is blocked by default. If you are new to VPN (for Legacy Apps), you must create a policy rule to allow any traffic through the VPN tunnel.

VPN (for Legacy Apps) supports a maximum of 1,000 policy rules and 128 address book entries.

This release includes the following enhancements for access policies:
 
- You can view configured rules and their actions on the Rules page. You can also:
Search or filter rules.
- Add, edit, or delete rules.
- View how many additional source or destination networks are available. By default, two networks display but if there are more, the number of additional networks appears (e.g., +1).
- Select a value in the Rule Order column to change the order in which rules are evaluated. Rules are evaluated using a top-down, first-match principle.
- Select a rule name to view details for the rule. 
 See image. 
 
- When adding a rule for the source or destination network, you can manually enter it, import individual LAN/Client Subnet entries, or select entries from the address book. You can expand the list of added entries under the IP Address field.

If you manually enter or import LAN/Client Subnet entries, each time you update a Network segment, you must make a corresponding change to the access policy to add the LAN/Client Subnet entries. If you use the address book, any host or subnet added to the address book is automatically added to the access policy.

See image.
- On the Address Book page, you can view, search, add, edit, or delete defined sets of IP addresses and CIDRs.

See image.
- You can add a set of IP addresses or CIDRs to the address book. A set of addresses in the address book cannot be nested inside of other address books, but you can reuse IP addresses and CIDRs in different address books.

See image.


### February 06, 2026

#### Agent Age-Out for Microsegmentation
You can now configure a timer for the automatic age-out of disconnected agents for individual agent groups. When the timer is enabled, you can set the duration of days, hours, or minutes before access expires.

#### Kubernetes Clusters for Microsegmentation
Microsegmentation now provides visibility to resources such as deployments, statefulsets, replicasets, and daemonsets. When you deploy agents, you can view network flows in the Zscaler Private Access (ZPA) Admin Portal.

#### Tag Management for Microsegmentation
You can now use tags to annotate resources with metadata that can be used when defining membership criteria for resource groups. You can create namespaces, tag keys, and tag groups and assign them to managed resources. To learn more, see Configuring Resource Groups .


### February 03, 2026

#### Automated Manager Software Updates for Private Service Edges and Private Cloud Controller
An update was released to support automated updates to the Manager software and software updates for ZPA Private Service Edge and Private Cloud Controller.

Automated Manager software updates are available with a Manager software version of 25.46.3 or later and a ZPA Private Service Edge or Private Cloud Controller version of 25.46.3 or later.

The table includes the following updates:
 
- Version Profile: Displays the version profile applied to the ZPA Private Service Edge or Private Cloud Controller. You can hover over the information icon under the Version Profile column heading to view the target version for the Manager software and ZPA Private Service Edge or Private Cloud Controller software.

See image.
- Software Update: Displays the status of the ZPA Private Service Edge or Private Cloud Controller software update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.
- Manager Update: Displays the status of the Manager software update. You can hover over the information icon next to the update status to view more information, such as the scheduled version and upgrade window.

See image.
- When viewing details for a ZPA Private Service Edge or Private Cloud Controller, you can view the Last Manager Update time.

See image. 
To learn more, see About ZPA Private Service Edges or About Private Cloud Controllers .

Manager software updates are scheduled during the maintenance window for ZPA software updates.


### January 16, 2026

#### VPN Service Edge Software Update
This release fixes an intermittent issue with VPN redundancy where upgrading the VPN Service Edge caused it to lose the Border Gateway Protocol (BGP) override configuration file upon restart, which resulted in the BGP neighborship between the Network Connector and VPN Service Edge dropping until the configuration file was manually reuploaded.

To learn more, see About VPN Service Edges .


### January 13, 2026

#### Extranet Client Type Support
A new client type and criteria for Extranet is supported when configuring an access policy. The Extranet client type and criteria allow admins to assign an extranet to an application segment to provide a defined set of partners, and supports both location and sublocation for extranet traffic. The same functionality is supported via the cloud service API.
 
 See image. 
 
To learn more, see About Extranet , About Access Policy , and Configuring Access Policies .


### January 09, 2026

#### Application Tagging Support
An update was released to support adding more metadata for tagging applications to provide a more granular grouping and access management strategy.

To learn more, see Tag Management for Defined Application Segments .


### January 08, 2026

#### Using the Application Map for Microsegmentation
The Application Map for Microsegmentation is a visual representation of your network data and how it all works together. The interactive graph provides widgets for resource group, Public Internet, and VPC/VNET data that can aid in policy configuration and general resource maintenance.

 See image. 

To learn more, see Viewing the Application Map .
