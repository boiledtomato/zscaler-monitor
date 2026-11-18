# セキュリティアドバイザリ

> 最終更新: 2026-11-18 23:17 UTC  
> ソース: https://trust.zscaler.com/

---

# Zscaler Trust - インシデント/アドバイザリ RSS

## Posture and Third-Party Apps Data Not Visible in AppTotal for SSPM Applications - zscaler.net, zscloud.net
- 公開: Wed, 18 Nov 2026 21:31:14 GMT
- ステータス: In Progress  カテゴリ: Recent incident
- URL: https://trust.zscaler.com/zscaler.net/posts/32786
- 影響: For SaaS applications onboarded for SSPM in ZIA, posture control results and third-party app visibility may not appear in the AppTotal portal. Only the following applications are currently visible:

 - Microsoft 365
 - Google Workspace
-  Okta
-  Jira
- Confluence
- Bitbucket
- Salesforce
- ServiceNow
- GitHub

All other applications onboarded via ZIA are affected.


Zscaler is investigating an issue where SaaS applications onboarded for SSPM in ZIA, other than those listed above, are not showing posture control results and third-party app visibility in the AppTotal portal. We will continue to provide updates here as the investigation progresses. For detailed updates, please check the Service Status section in your Zscaler customer support portal (CSP). Status changes and additional details will be posted there as they become available. Latest Update - Wed, 

---

## Urgent Maintenance : ZIdentity Service Upgrade - zslogin.net
- 公開: Wed, 18 Nov 2026 14:35:10 GMT
- ステータス: In Progress  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zslogin.net/posts/32781
- 影響: 

Zscaler will perform an urgent maintenance for the ZIdentity (ZID) Authentication service between 2:30 PM UTC and 4:30 PM UTC on November 18, 2026. This maintenance includes Java4shell vulnerability fixes. During the maintenance window, users may experience intermittent login or portal access issues for approximately 30–45 minutes. Following completion of the maintenance activities, service is expected to operate normally without customer intervention. If you experience any access issues after t

---

## ZIA Backup & Restore — Upcoming Change to Restore Window - zscaler.net, zscalerone.net, zscalertwo.net, zscloud.net, zscalerthree.net
- 公開: Wed, 18 Nov 2026 00:00:00 GMT
- ステータス:   カテゴリ: Advisory
- URL: https://trust.zscaler.com/zscaler.net/posts/32776
- 影響: 

ZIA Backup &amp; Restore — Upcoming Change to Restore Window What: Zscaler is introducing a 31-day rolling restore window for ZIA Backup &amp; Restore. Restore points older than 31 days will no longer be available for restore. Action Required: Review your restore points and refresh or recreate any you rely on — including your Golden Restore Point — if they are older than 31 days. Effective Date: Jan 4th, 2027 Important: This change does not affect your day-to-day ZIA policy configuration, traffi

---

## ZTB-US-M4 Cloud Maintenance - ztb-us-m4
- 公開: Wed, 18 Nov 2026 06:55:12 GMT
- ステータス: Upcoming  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/ztb-us-m4/posts/32771
- 影響: 

Zscaler will be performing cloud maintenance activity for ZTB-US-M4 to deliver continued improvements in performance, stability, and security. Maintenance window: Wed, 18 Nov 2026 07:00:00 UTC &nbsp; Duration: 2 hours No service downtime is anticipated during this maintenance window, and services are expected to remain available. However, as with any maintenance activity, there remains a limited risk of intermittent impact or brief disruption. We appreciate your understanding and cooperation.

---

## Additions to Zscaler Aggregate & Hub IP Address Ranges - zscaler.net, zscalerone.net, zscalertwo.net, zscloud.net, zscalerthree.net, zdxcloud.net
- 公開: Wed, 18 Nov 2026 00:59:21 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32766
- 影響: 

Dear Zscaler Customer, In accordance with&nbsp; Zscaler Service Continuity Policy and per email notification sent on&nbsp; November 17, 2026 , we would like to notify you of the additions to the Zscaler Hub IP Addresses and Zscaler Aggregate IP Address Ranges as listed below. These would be effective anytime on or after January 16, 2027; 60 days or more from the date the first email notification is sent. Please update your firewall policy rules and any upstream Access Control Lists (ACLs) to all

---

## Upcoming Service Location Expansion - zscaler.net, zscalertwo.net, zscloud.net, zscalerthree.net, private.zscaler.com, zpatwo.net
- 公開: Wed, 18 Nov 2026 00:49:57 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32761
- 影響: 

Dear Zscaler Customer, In accordance with&nbsp; Zscaler Service Continuity Policy and per email notification sent on&nbsp; November 17, 2026 , we would like to notify you of the upcoming expansion at the service location listed below. This would be available anytime on or after January 16, 2027; 60 days or more from the date the first email notification is sent. Please update your firewall policy rules and any upstream Access Control Lists (ACLs) to allow the new IP address ranges to avoid any s

---

## Connectivity Issues to the Sydney III Data Center - zscaler.net, zscalertwo.net, zscalerthree.net
- 公開: Wed, 18 Nov 2026 00:20:39 GMT
- ステータス: Monitoring  カテゴリ: Recent incident
- URL: https://trust.zscaler.com/zscaler.net/posts/32756
- 影響: Users whose traffic is forwarded to the Sydney III data center may experience increased latency, slower application response times, or brief interruptions to internet access and active calls.

Zscaler is currently investigating reports of an issue with its Sydney III datacenter. If you’re currently experiencing any traffic impacting issues please failover to your secondary DC or any other alternate DC. For more information, please refer to the following support article. &nbsp; We will continue to provide updates here as the investigation progresses. For detailed updates, please check the Service Status section in your Zscaler customer support portal (CSP). Status changes and updates w

---

## Zscaler Update on CVE-2026-114938 - Java4Shell Flaw in OpenJDK - zscaler.net, zscalerone.net, zscalertwo.net, zscloud.net, zscalerthree.net, private.zscaler.com, zdxcloud.net, zpatwo.net, app.zsdpc.net, app.eu.zsdpc.net, zpabeta.net, zsdkone.net, zscalerrisk.net, admin.zscaleranalytics.net, zslogin.net, app.avalor.io, app.eu.avalor.io, app.aps.avalor.io, ztb-us-m2, ztb-us-m3 (beta), ztb-us-m4, ztb-us-m7, ztb-euc-m1, ztb-in-m1, pulsar, quasar, prod3, prod4, prod5, prod6, zseclipse.net, zsaiguard.net, app.in.zsdpc.net, ai-console.zscaler.com
- 公開: Tue, 17 Nov 2026 00:00:00 GMT
- ステータス:   カテゴリ: Advisory
- URL: https://trust.zscaler.com/zscaler.net/posts/32751
- 影響: 

Zscaler is aware of&nbsp;CVE-2026-114938,&nbsp;Java4Shell Flaw in OpenJDK.&nbsp; Our Security and Engineering teams are investigating potential impact of CVE-2026-114938 and associated downstream dependencies. We will update this post as new information emerges. Zscaler recommends that customers patch affected OpenJDK installations to the&nbsp; latest vendor provided version to address this vulnerability in their environment. Update Wed, 18 Nov 2026 20:15:15 UTC &nbsp; Zscaler has already patche

---

## San Francisco IV (SJC4) Datacenter Network Maintenance - zscaler.net, zscalertwo.net, zscloud.net, zscalerthree.net
- 公開: Tue, 17 Nov 2026 07:00:26 GMT
- ステータス: Upcoming  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32746
- 影響: During the maintenance, traffic will failover to redundant devices in the same datacenter, however intermittent connections and connection reestablishment may be observed.

Zscaler will be performing hardware maintenance in San Francisco IV (SJC4) Datacenter. Maintenance window: &nbsp; &nbsp;Start: &nbsp;2026-11-19 02:00 UTC &nbsp; &nbsp;End: &nbsp; 2026-11-19 06:00 UTC &nbsp; &nbsp;(Local Time 2026-11-18 18:00 - 2026-11-18 22:00)

---

## Reminder Notification for Upcoming New Data Center and Changes - zscaler.net, zscalertwo.net, zscloud.net, zscalerthree.net, private.zscaler.com, zpatwo.net
- 公開: Mon, 16 Nov 2026 23:06:44 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32741
- 影響: 

Dear Customer,&nbsp; In accordance with the&nbsp; Zscaler Service Continuity Policy and as previously announced via&nbsp; email notification and&nbsp; Trust&nbsp; on October 1,&nbsp;2026, we would like to remind you of the upcoming new data center and IP allocation changes at the locations listed below. These would be available anytime on or after November 30, 2026. Please update your firewall policy rules and any upstream access control lists to allow the new and remove the legacy IP address ra

---

## ZTB-IN-M1 Cloud Maintenance - ztb-in-m1
- 公開: Mon, 16 Nov 2026 11:04:11 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/ztb-in-m1/posts/32736
- 影響: 

Zscaler will be performing cloud maintenance activity for ZTB-IN-M1 to deliver continued improvements in performance, stability, and security. Maintenance window: &nbsp; Mon, 16 Nov 2026 12:30:00 UTC &nbsp; Duration: 4 hours No service downtime is anticipated during this maintenance window, and services are expected to remain available. However, as with any maintenance activity, there remains a limited risk of intermittent impact or brief disruption. We appreciate your understanding and cooperat

---

## ZTB-US-M4 Cloud Maintenance - ztb-us-m4
- 公開: Mon, 16 Nov 2026 06:01:50 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/ztb-us-m4/posts/32731
- 影響: 

Zscaler will be performing cloud maintenance activity for ZTB-US-M4 to deliver continued improvements in performance, stability, and security. Maintenance window: &nbsp; Tue, 17 Nov 2026 06:30:00 UTC &nbsp; Duration: 4 hours No service downtime is anticipated during this maintenance window, and services are expected to remain available. However, as with any maintenance activity, there remains a limited risk of intermittent impact or brief disruption. We appreciate your understanding and cooperat

---

## Scheduled Maintenance Extended - zdxcloud.net
- 公開: Sat, 14 Nov 2026 17:14:41 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zdxcloud.net/posts/32726
- 影響: 

The Zscaler Site Reliability Engineering team will be extending the scheduled maintenance of the zdxcloud.net cloud by 4 hours. As part of our standard maintenance process, all logs will be collected and available after maintenance has been completed. Please contact Zscaler Support if you have additional questions. Update - Sat, 14 Nov 2026 20:59:33 UTC This activity has been completed. Please contact Zscaler Support if you have additional questions.

---

## Munich I Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 23:31:28 GMT
- ステータス: Postponed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32721
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Munich I (MUC1) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 20, 5:00 pm PST (November 21, 1:00 UTC) End time is November 20, 7:00 pm PST (November 21, 3:00 UTC) Update 11/18: Maintenance Postponed

---

## Dusseldorf I Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 23:24:41 GMT
- ステータス: Upcoming  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32716
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Dusseldorf I (DUS1) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 19, 5:00 pm PST (November 20, 1:00 UTC) End time is November 19, 7:00 pm PST (November 20, 3:00 UTC)

---

## Frankfurt IV Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 23:19:41 GMT
- ステータス: Upcoming  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32711
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Frankfurt IV (FRA4) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 18, 5:00 pm PST (November 19, 1:00 UTC) End time is November 18, 7:00 pm PST (November 19, 3:00 UTC)

---

## Washington I Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 23:06:45 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32706
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Washington I (WAS1) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 17, 7:00 pm PST (November 18, 3:00 UTC) End time is November 17, 9:00 pm PST (November 18, 5:00 UTC) Update - Wed, 18 Nov 2026 08:58:42 UTC This activity has been completed. Please contact 

---

## Singapore IV Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 22:50:36 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32701
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Singapore IV (SIN4) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 17, 12:00 pm PST (November 17, 20:00 UTC) End time is November 17, 2:00 pm PST (November 17, 22:00 UTC) Update - Tue, 17 Nov 2026 23:36:13 UTC This activity has been completed. Please conta

---

## Chennai II Datacenter Scheduled Maintenance - IPv6 Enablement - zscaler.net
- 公開: Fri, 13 Nov 2026 22:43:48 GMT
- ステータス: Completed  カテゴリ: Scheduled maintenance
- URL: https://trust.zscaler.com/zscaler.net/posts/32696
- 影響: 

Zscaler will enable IPv6 for VPN and UVPN services at the Chennai II (MAA2) Data Center. Services will be restarted in phases during the scheduled maintenance window to minimize disruption. Other Zscaler sites and Zscaler Services will continue to operate normally. Maintenance Window: Start time is November 16, 12:00 pm PST (November 16, 20:00 UTC) End time is November 16, 2:00 pm PST (November 16, 22:00 UTC) Update - Mon, 16 Nov 2026 22:16:37 UTC This activity has been completed. Please contact

---

## ZTB API Service Issues in AMER (ZTB-US-M4) Cloud - ztb-us-m4
- 公開: Fri, 13 Nov 2026 17:11:10 GMT
- ステータス: Monitoring  カテゴリ: Recent incident
- URL: https://trust.zscaler.com/ztb-us-m4/posts/32691
- 影響: 

Zscaler has detected an issue with its ztb-us-m4 Cloud.&nbsp; We will continue to provide updates here as the investigation progresses. For detailed updates, please check the Service Status section in your Zscaler customer support portal (CSP). Status changes and additional details will be posted there as they become available.

---
