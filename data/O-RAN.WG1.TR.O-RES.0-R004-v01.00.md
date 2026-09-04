# O-RAN Work Group 1 (Use Cases and Overall Architecture) O-RAN Resiliency

Copyright $©$ 2025 by the O-RAN ALLIANCE e.V.

# Contents

List of figures .... 4

List of tables ... .4

Foreword... .5

Modal verbs terminology .....

Executive summary ...... ......................................................................................................................... .....5   
1 Scope .......   
2 References ................................................................................................................................................6   
2.1 Normative references...   
2.2 Informative references .. ................................................................................................................ 6   
3 Definition of terms, symbols and abbreviations.......................................................................................7   
3.1 Terms ....... ................................................................................................. 7   
3.2 Symbols .... ............................................................................ ...... 7   
3.3 Abbreviations....   
4 Objectives and requirements . ..................................................................................................................9   
4.1 4.1.1 Objectives .... Detailed Objectives ...................................................................................................................................... 9 ...................................................................................................... ..... 9   
5 Resiliency Architecture ..... ............................................................................................................ .....10   
5.1 Resiliency Concepts.. ............................................................................................................................. 10   
5.2 Resiliency Overview... ......................................................................................................................... ..... 10   
5.3 5.4 Resiliency development in O-RAN ................................................................................................................. 10Resiliency for NF failures ................................................................................................................................ 11   
5.4.1 Overview ......... .................................................................................................................................... 11   
5.4.2 5.4.3 O-RU failure.......O-DU failure ...... ..................................................................................................................................... 11   
................................................................................................................................... 11   
5.4.4 O-CU-CP failure .... .................................................................................................................................. 13   
5.4.5 O-CU-UP failure ........................................................................................................................................ 13   
5.5 Resiliency for interface failures ................................................................................................................... .... 14   
5.5.1 Overview ..... ............................................................................................................ ..... 14   
5.5.2 Generic aspects... ................ ............................................................................. . 14   
5.5.3 Control plane interface failures .. ............................................................................................................ . 15   
5.5.4 5.5.5 User Plane interface failures....................................................................................................................... 17Management plane interface failures.......................................................................................................... 18Transport layer failures ................................................................................................................................... 19   
5.6.1 Overview ........ ................................................................................................................................... 19   
5.6.2 Transport layer failure scenarios ... .................................................................................................. ..... 19   
5.6.3 Network function failure scenario ... .......................................... .... 20   
5.7 Cloud layer failures.. .................................................................................................... ..... 22   
6 Scenarios and considerations . .......................................................................................... ....22   
6.1 Service restoration time considerations .................... ................................................................................. ..... 22   
6.2 Deployment scenarios.. ......................................................................... .... 23   
6.2.1 Hierarchical deployment ...... ................. ............................................. .... 23   
6.2.2 Hybrid deployment... ............................................................................................................... 23   
6.2.3 Transport resiliency considerations ............................................................................................................ 23   
6.3 6.3.1 Considerations for resiliency ...........Backup options ........................... .................................................................................................................................................................................................. . 23. 24   
6.3.2 Redundant node options .......................................................................................................................... . 24   
6.3.3 Entities ...... ............................................................................................ . 25   
6.3.4 End-to-end aspects . ........................................... ... 25   
6.4 Relationships with rolling upgrade .. ............................................................................................ . 25   
6.4.1 Ove 25   
6.4.2 Redundant NF architectures .. ..................................................................... ... 26   
6.4.3 Resiliency technologies in cloud-native NFs ....................................................................................... .... 26   
6.4.4 Redundant transport paths.. .................................................................................. ... 26   
6.4.5 Monitoring and observability . ............................................................................................................. 26   
7 Potential resiliency solutions.... ...26   
7.1 Overview .... ..... 26   
7.2 Solution 1: Enhanced network resiliency through standby O-DU and adaptive cell activation managed   
by SMO..... ... 27   
7.2.1 Basic objective ... ..... 27   
7.2.2 Roles of involved entities .. ... 27   
7.2.3 Solution description ... ....... 28   
7.3 Solution 2: Enhanced network resiliency through the standby O-CU-CP and service restoration   
managed by the SMO . .. 36   
7.3.1 Basic objective ... ... 36   
7.3.2 Roles of involved entities .. .. 36   
7.3.3 Solution description ... .. 36   
7.4 Solution 3: Enhanced network resiliency through O-RU rehoming, leveraging the SMO framework's   
transport resiliency management capabilities. . ..... 43   
7.4.1 Basic objective ..... ... 43   
7.4.2 Roles of involved entities .. ... 43   
7.4.3 Solution description . .. 44   
7.5 Solution 4: Enhanced network resiliency for NF Deployment(s) in O-Cloud managed by the SMO   
Framework.... .... 51   
7.5.1 Basic objective ....... ...................................................................................................................... 51   
7.5.2 Roles of involved entities .... ............................................................................................ .... 51   
7.5.3 Solution description . .... 52   
7.6 Solution 5: Multi-Domain Recovery Service.................................................................................................. 57   
7.6.1 Basic objective ................ ......................................................................................................... 57   
7.6.2 Roles of involved entities .. ....................................................................................................... ... 58   
7.6.3 Solution description . ........................................................................................................ ... 58   
8 Summary and impacts identified.. ............................................................................. ..62   
8.1 Overview .. ............................................................................................................ .... 62   
8.2 Summary of evaluation.. .................................................................................................................... ... 62   
8.3 Impacts identified . ....................................................................................................................... .... 63   
Annex A: ..... .................................................. ....66   
..67

Annex (informative): Change history/Change request (history) ..

# List of figures

Figure 5.6-1: Transport layer failure scenario . . 20   
Figure 5.6-2: O-RAN network function failure scenario .... . 21   
Figure 5.6-3: NF failure recovery based on domain-scoped (localized) recovery scheme ..... . 21   
Figure 5.6-4: NF failure scenario with end-to-end recovery scheme..... . 22   
Figure 7.2.3-1: Enhanced network resiliency with SMO-managed standby O-DU... . 35   
Figure 7.3.3-1: Enhanced network resiliency with SMO-managed standby O-CU-CP. . 42   
Figure 7.4.1-1: SMO managed transport to support O-RU rehoming and network resiliency . . 43   
Figure 7.4.3-1: Transport configuration managed by SMO for network resiliency through O-RU rehoming. ... . 50   
Figure 7.5.3-1: SMO managed NF resiliency in O-Cloud deployment .... . 57   
Figure 7.6.3-1: Multi-Domain recovery procedure up to execution of APGF. . 62

# List of tables

Table 7.2.3-1: Enhanced network resiliency with SMO-managed standby O-DU . . 29   
Table 7.3.3-1: Enhanced network resiliency with SMO-managed standby O-CU-CP . . 37   
Table 7.4.3-1: Transport configuration managed by SMO for network resiliency through O-RU rehoming.. . 45   
Table 7.5.3-1: SMO managed NF resiliency in O-Cloud deployment.. . 53   
Table 7.6.3-1: Multi Domain Recovery Procedure. . 59   
Table 8.3-1: Impacts on various working groups . 63

# Foreword

This Technical Report (TR) has been produced by O-RAN ALLIANCE.

The content of the present document is subject to continuing work within O-RAN and may change following formal ORAN approval. Should the O-RAN ALLIANCE modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } \mathbf { X } = 0 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# Executive summary

O-RAN supports multi-vendor deployments where failures can occur at nodes (e.g., O-RAN Network Functions, interfaces, transport, and the O-Cloud). Solution providers typically manage recovery within their scope, making it crucial to standardize O-RAN resiliency features to ensure effective use of each provider's designs. This leads to a robust endto-end resiliency solution covering Fronthaul, RAN OAM, Network Functions, and O-Cloud infrastructure. Standardization also enables Service Management Orchestration to manage O-RAN components through interoperable interfaces, facilitating automated recovery from various scenarios.

Resiliency feature development should address various failure scenarios (e.g., node, interface, transport), back-up and recovery mechanisms, service criticality, different deployments (PNF and Cloud-based), resiliency controller responsibilities, and UE aspects. This holistic approach ensures a robust, adaptable resiliency feature capable of maintaining network integrity and service continuity across diverse operational challenges.

# 1 Scope

This document details and evaluates a variety of failure scenarios and the corresponding recovery mechanisms suited for multi-vendor network deployments. It also explores various O-RAN resiliency use cases, offering insights into how these strategies can be effectively applied across different deployment scenarios to ensure end-to-end resiliency within the ORAN framework.

# 2 References

# 2.1 Normative references

Not applicable.

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long term validity.

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area.

[i.1] O-RAN.WG1.TS.Use-Cases-Detailed-Specification: O-RAN Working Group 1, Use Cases Detail Specification.   
[i.2] 3GPP TS 23.501: System Architecture for the 5G System (5GS).   
[i.3] 3GPP TS 23.502: Procedures for the 5G System (5GS).   
[i.4] 3GPP TS 38.472: NG-RAN; F1 Signalling Transport.   
[i.5] O-RAN.WG6.TS.CADS: Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN.   
[i.6] O-RAN.WG6.TS.O2-GA&P.0: O2 General Aspects and Principles Specification.   
[i.7] O-RAN.WG4.TS.MP.0: O-RAN Management Plane Specification.   
[i.8] O-RAN.WG10.TS.O1-Interface: O-RAN O1 Interface Specification.   
[i.9] O-RAN.WG10.TS.OAM-Architecture: O-RAN Operations and Maintenance Architecture.   
[i.10] O-RAN.WG10.TS.PMeas: O-RAN O1 Performance Measurements Specification.   
[i.11] 3GPP TS 38.462: NG-RAN; E1 Signalling Transport.   
[i.12] O-RAN.WG3.TS.E2GAP: O-RAN E2 General Aspects and Principles (E2GAP).   
[i.13] O-RAN.WG4.TS.CUS.0: Control, User and Synchronisation Plane Specification.   
[i.14] O-RAN.WG2.TS.A1GAP: A1 interface: General Aspects and Principles.   
[i.15] 3GPP TS 38.401: NG-RAN; Architecture Description.   
[i.16] 3GPP TS 29.244: LTE; 5G; Interface between the Control Plane and the User Plane nodes. [i.17] 3GPP TS 36.420: LTE; E-UTRAN; X2 General Aspects and Principles   
[i.18] 3GPP TS 38.300: NR and NG-RAN Overall Description; Stage 2.   
[i.19] 3GPP TS 36.423: LTE; E-UTRAN; X2 Application Protocol (X2AP).   
[i.20] 3GPP TS 38.423: NG-RAN; Xn Application Protocol (XnAP).   
[i.21] 3GPP TS 38.413: NG-RAN; NG Application Protocol (NGAP).   
[i.22] 3GPP TS 38.473: NGRAN; F1 Application Protocol (F1AP).   
[i.23] 3GPP TS 38.414: NGRAN; F1 Application Protocol (F1AP).   
[i.24] 3GPP TS 36.424: LTE; E-UTRAN; X2 Data Transport.   
[i.25] 3GPP TS 38.420: NGRAN; Xn General Aspects and Principles.   
[i.26] O-RAN.WG9.XTRP-MGT.0: Management Interfaces for Transport Network Elements.   
[i.27] ORAN-WG9.XPSAAS.0: Xhaul Packet Switched Architectures and Solutions   
[i.28] O-RAN-WG6.ORCH-USE-CASES.0: Cloudification and Orchestration Use Cases and Requirements O-RAN Virtualized RAN

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the following terms apply:

Resiliency: Resiliency in O-RAN refers to the ability of the SMO to manage and maintain service continuity and quickly recover from failures through robust mechanisms like redundancy, fault management, and automated recovery procedures, ensuring uninterrupted service delivery within the O-RAN architecture even under adverse conditions.

Multi-Domain Recovery Service (MDRS): A service that queries RAN NF OAM and TE&IV services within SMO framework for data on topology, alarms, and load conditions followed by identifying or generating optimal AP(s) and sending AP details to relevant network domains.

Alternative Path (AP): A path that traverses across multiple network domains, including O-Cloud, O-RAN node, transport, and interfaces, while maintaining the original path endpoints.

Alternative Path generation Function (APGF): A function that identifies existing alternative paths (AP) and generates new AP information that can be utilized, assigns weights to each identified existing AP and new AP information, and selects an AP based on assigned weights.

Network Segmentation Function (NSF): A function that divides the network into network segments based on (bandwidth, latency, etc) and generates low-level information query for the relevant network segments to network topology, thus, allows an efficient retrieval of detailed network information for specific segments of the network.

# 3.2 Symbols

Void

3GPP Third Generation Partnership Project   
5GC 5G Core   
AAL Acceleration Abstraction Layer   
AI/ML Artificial Intelligence/Machine Learning   
ALD Antenna Line Device   
AMF Access and Mobility management Function   
AP Alternate Paths   
APGF Alternate Path Generation Function   
API Application Programming Interface   
CM Configuration Management   
CNF Cloudified Network Function   
CPU Central Processing Unit   
DHCP Dynamic Host Configuration Protocol   
DMS Deployment Management Services   
F1AP F1 Application Protocol   
FCAPS Fault, Configuration, Accounting, Performance, and Security   
FM Fault Management   
FOCOM Federated O-Cloud Management and Orchestration   
gNB gNodeB (Next Generation Node B applies to NR)   
GPU Graphics Processing Unit   
GTP-U GPRS Tunneling Protocol User Plane   
HDLC High-level Data Link Control   
IMS Infrastructure Management Services   
IP Internet Protocol   
IPFRR IP Fast Reroute   
K8S Kubernetes   
LBM Loop Back Message   
LCM Life Cycle Management   
LTE Long Term Evolution   
MA-PDU Multi-Access Protocol Data Unit   
MnF Management Function   
MNO Mobile Network Operator   
MnS Management Service   
MP M-Plane   
MRDC Multi-Radio Dual Connectivity   
NCI NR Cell Identity   
NE Network Element   
Near-RT RIC Near real time RAN Intelligent Controller   
NF Network Function   
NFO Network Function Orchestration   
NGAP Next Generation Application Protocol   
NG-C NG Control Plane   
NG-U NG User Plane   
NG-RAN Next Generation Radio Access Network   
NIC Network Interface Card   
Non-RT RIC Non-real time RAN Intelligent Controller   
NR 5G New Radio   
NRCGI NR Cell Global Identifier   
OAM Operation and Administration and Maintenance   
O-Cloud O-RAN Cloud   
O-CU-CP O-RAN Central Unit: Control Plane   
O-CU-UP O-RAN Central Unit: User Plane   
O-DU O-RAN Distributed Unit   
O-eNB O-RAN evolved Node B (applies to LTE)   
OFH Open Fronthaul   
O-RU O-RAN Radio Unit   
PM Performance Management   
QoS Quality of Service   
RACH Random Access Channel

<table><tr><td>RAN SCTP SDO SMO TE&amp;IV TNL TNLA TNM X2-C Xn-C Xn-U UDP UE UPF VNF WG</td><td>Radio Access Network Stream Control Transmission Protocol Standard Development Organization Service Management and Orchestration Topology Exposure and Inventory Management Transport Network Layer Transport Network Layer Adaptation Transport Network (TN) Manager X2 Control Plane Xn Control Plane Xn User Plane User Datagram Protocol</td></tr></table>

# 4 Objectives and requirements

# 4.1 Objectives

O-RAN supports multi-vendor deployments where failures can occur at various levels. This document captures the WG1 Resiliency study outcomes, outlining use cases where the SMO monitors criteria and triggers actions to reconfigure system components, minimizing the impact of component failures on service availability. It can also consider the scenarios with both single and multiple component failures, ensuring effective utilization of diverse designs from various solution providers. This leads to a robust end-to-end resiliency solution covering Fronthaul, RAN OAM, Network Functions, and O-Cloud infrastructure.

# 4.1.1 Detailed Objectives

Identify Gaps and Develop Recovery Mechanisms o Address gaps in recovery from network failures by enhancing service resiliency with robust mechanisms, ensuring quick recovery from outages and minimizing service interruptions.   
Consolidate Efforts Across Working Groups o Unify ongoing efforts from WG1, WG4, WG6, WG9, and WG11 to provide a holistic view of end-toend resiliency, integrating findings on shared O-RU resiliency, O-CU redundancy, and transport network redundancy.   
Investigate Current State and Identify Gaps o Examine current resiliency features, identify gaps in existing specifications, and produce a Technical Report on detailed requirements.   
Collaborate with Other Working Groups o Work with WG6 and WG10 to integrate resiliency requirements, ensuring O-RAN specifications cover common failures for end-to-end resiliency.   
Define Normative Specifications and Solutions o Gather use cases and potential solutions that would help deriving requirements for normative specifications to enhance O-RAN resiliency, focusing on redundancy mechanisms, fault detection, isolation techniques, and efficient failover mechanisms.

# 5 Resiliency Architecture

This clause covers general resiliency architecture, principle, policies, flows, outline, and heuristics for handling resiliency.

# 5.1 Resiliency Concepts

It describes the fundamental principles, strategies, and mechanisms designed to ensure system reliability and continuous service availability, despite failures or adverse conditions.

Redundant architectures: Implementing redundant paths and components to provide alternative routes or backups in case of failure.   
Fault detection and recovery: Using mechanisms for detecting faults and quickly recovering from failures to minimize downtime. Load balancing and failover: Distributing traffic and workloads across multiple nodes in NR Cells and optionally LTE cells prevent overloading any single component, enhancing resiliency by ensuring smooth failover and continuous service availability when failures occur.   
Proactive measures: Employing predictive analytics and monitoring tools to identify potential issues before they cause service interruptions.

# 5.2 Resiliency Overview

It provides a high-level summary or holistic view of how these resiliency concepts are implemented and managed within a specific network or system. It typically includes:

Network architecture and design: An overview of the network's architectural layout, focusing on use cases that allow effective utilization of redundant network elements, such as employing backup paths, redundant systems, and failover protocols without specifying internal designs of network elements.   
• Operational scenarios and use cases: Descriptions of various failure scenarios and the corresponding recovery processes. This may include specific examples like O-DU failures and the role of SMO in managing failover.   
• Management and control mechanisms: This clause outlines the control mechanism, emphasizing the role of the SMO in handling different types of failures. For example, managing the flow of carrier and cell switching, particularly at the O-DU level. Implementation strategies: Strategies for deploying and managing resiliency features, including details on interfaces, models, and configurations used to achieve resiliency in different parts of the network from an ORAN perspective. Performance metrics and monitoring: An overview of how performance is monitored and assessed to ensure resiliency, including the metrics used to gauge network health and the tools employed for continuous monitoring and fault detection. Creation and management of resiliency related policies by SMO.

# 5.3 Resiliency development in O-RAN

O-RAN Release 004 specifications do not provide sufficient coverage for end-to-end resiliency. However, there are several resiliency scenarios and use cases described, along with detailed analysis of O-DU level resiliency as part of the shared O-RU Work Item [i.1] and by WG9 from a transport perspective [i.26 and i.27]. However, these do not adequately explain how the SMO framework manages the cross-domain considerations, particularly those related to O-Cloud and transport. Furthermore, the specifications do not cover critical aspects such as interface failures, O-CU-CP failures, and O-Cloud NF Deployment failures, as well as how the role of SMO framework in effectively managing these various aspects of transport, O-Cloud, and NF/interface failures to ensure comprehensive end-to-end resiliency and minimize service interruption during various failure scenarios. Therefore, this technical report aims to address these gaps by examining resiliency scenarios, including NF and interface failures across various deployments. It also investigates crossdomain coordination involving transport, O-Cloud, and other relevant factors, as well as how the SMO framework effectively manages these challenges.

# 5.4 Resiliency for NF failures

# 5.4.1 Overview

Resiliency for NF failures ensure service availability with minimal disruption by leveraging static or dynamic failover, session recovery, and robust redundancy mechanisms. An appropriate recovery mechanism can be employed for the critical interfaces like O1, Fronthaul, E2, and F1-C to ensure service with minimum disruption during link failures. For example, SCTP based transport redundancy for F1-C [i.4] and cloud-native deployments [i.5 and i.6] can leverage the various resiliency capabilities (e.g., Kubernetes based) to ensure high availability and implement failover mechanisms for NF, thereby enhancing the overall resiliency of the O-RAN Network. Multi-layered resiliency spans both physical and virtual components, supporting high-priority services with active-standby setups and an appropriate recovery action. This approach integrates cross-domain fault detection and configuration to support efficient service transitions and minimize service disruptions.

Protocols including for example TNL [i.3 and i.4], and additional appropriate recovery mechanisms, can be utilized to ensure that O-RAN networks meet robust resiliency objectives, and can be recovered from the diverse failure scenarios while maintaining service quality.

# 5.4.2 O-RU failure

This clause describes the impact of the O-RU to service availability, however O-RU itself is not an actor in resiliency scenarios.

This refers to a functional or hardware failure within the O-RU, one of the key components in the RAN infrastructure that facilitates signal transmission and reception between the user equipment and the network component, specifically the ODU. Failures in the O-RU can affect the connected users and associated applications. The O-DU can detect the O-RU failures using FM data such as alarms, CM notifications, and PM data reported by the O-RU through the open fronthaul M-plane interface [i.7]. In hybrid deployment, the SMO can also subscribe to O-RU alarms via open fronthaul M-plane interface as O-RU controller [i.7]. In hierarchical deployment, the O-DU can either independently act or forward failurerelated information to the SMO via the O1 interface [i.8], enabling the SMO to take appropriate actions to recover the ORU.

# 5.4.2.1 Impacts of O-RU failure

An O-RU failure can affect the operation of carrier(s), potentially affect cell availability and resulting in service degradation, such as reduced throughput. This failure affects the data flow between the affected cell of network and endusers, potentially leading to interruptions in data transmission, reduced throughput, and a decrease in overall network capacity. The impact of the failure can extend to multiple users, causing widespread connectivity loss, and degraded service quality.

# 5.4.2.2 O-RU recovery

O-RU recovery’s goal is to make resources needed for air interface handling available again. Restoration involves identifying the failure, executing recovery mechanisms like resetting the O-RU (if the fronthaul M-plane is still operational) and performing O-RU start-up procedure [i.7]. This process is crucial for reducing service downtime and restoring normal operations across affected sectors of the cells.

# 5.4.3 O-DU failure

The O-DU comprises the NF (hardware and/or software), MnF (hardware and/or software), and the associated hardware, such as cloud infrastructure for CNF deployment or dedicated physical hardware for PNF deployment [i.9]. Failures can occur in the NF and/or MnF and/or the hardware itself, such as due to a power outage, fiber cut, or equipment removal, leading to the complete inoperability of the O-DU.

MnF failure: The SMO can identify O-DU MnF failure by analyzing PM data from by the O-CU via O1 interface [i.10], as long as the F1 link between the O-CU and O-DU remains operational. Additionally, the O-CU can still be able to configure the O-DU via the F1 interface and knows about the resource status. When both the F1 connection between the O-CU and O-DU, and the O1 interface between the SMO and O-CU, are functional, the SMO can collect and correlate the PM metrics [i.10] received from the O-CU via the O1 interface with the O1 connection status to the O-DU. This helps determine if the MnF of the O-DU, or its connection, has failed, as the SMO detects that traffic is ongoing but cannot reach the O-DU through the O1 interface.

NF failure: If the NF fails and the O1 interface with the O-DU is still operational, the SMO can detect the failure directly through this interface. It can also identify the issue via performance management data from the O-CU, as the failure of the F1 interface and fault management (FM) data should also indicate the failure of the NF.

Complete O-DU failure: When both the MnF and NF [i.9] of the O-DU fail, the SMO can correlate the PM data from the O-CU with the O1 connection status, along with transport management data and PM data received via O2 interface in case of CNF deployment, to determine that the entire O-DU has failed. The PM data will show F1 failure due to the NF failure, and by correlating this with the O1 connection status, the SMO can conclude that the entire O-DU is inoperable.

# 5.4.3.1 Impacts of O-DU failure

O-DU plays a critical role in the RAN architecture, its failure leads to several specific impacts, which are outlined below:

Loss of connectivity to O-RU and UE communication

o Fronthaul disruption: The O-DU interfaces with the O-RU over the open fronthaul. If the O-DU fails, it results in the loss of connectivity between the O-RU and the O-DU.   
o UE session impact: All active sessions for connected UEs will be interrupted. If the O-DU fails completely, the UEs connected to that O-DU will experience a disruption or outage in service path, requiring them to reconnect to the network once the O-DU is restored or a backup system takes over.

C Degradation in network performance and capacity

o Cell outage: The O-DU failure can take down all the cells connected to it, effectively causing a localized network outage in the affected area. This leads to reduced network coverage and capacity, especially in regions where other O-DUs are not available to pick up the load.   
o Network congestion: If there are neighbouring O-DUs, the failure of one O-DU could lead to an overload on neighbouring units as UEs attempt to reconnect to other cells. This can result in degraded performance across the board.

Failure of critical control and management functions

o Impact on RAN control loops: The O-DU plays a crucial role in real-time control of radio resource management and scheduling. A failure here disrupts the flow of near real-time data and the execution of RAN control loops, impacting network optimizations, such as load balancing and interference management, carried out by the Near-RT RIC.   
o Fault management data loss: If the O-DU fails without an effective backup, any fault or performance management data that it was responsible for transmitting will be lost. This makes it harder for the SMO to diagnose the root cause and take corrective actions.

Reduced redundancy and resiliency

o Backup and recovery challenges: Depending on the network’s redundancy mechanisms, an O-DU failure might also expose gaps in resiliency. For instance, if there is no backup O-DU or if the backup O-DU fails to take over the operations in time, service restoration could be delayed.   
o Impact on Shared O-RU deployments: In shared O-RU deployments, if one O-DU fails, the shared ORU might still be operational but can only serve the remaining functional O-DUs. This scenario can lead to partial service loss or degraded performance in certain areas.

Reconfiguration and failover delays

o The time required to restore services after an O-DU failure largely depends on the architecture and resiliency strategies implemented, which include how services are recovered with the help of standby O-DUs. In cases where manual intervention is needed to restore the service or reconfigure the network elements, the recovery time would increase further, potentially reducing the network availability and affecting customer experience.   
o In conclusion, an O-DU failure triggers a wide range of impacts, including loss of communication, service degradation, compromised control mechanisms, and reduced resiliency, depending on the network architecture and failover mechanisms in place.

# 5.4.3.2 Cell service restoration

Cell service restoration after an O-DU failure involves re-establishing connectivity between the impacted O-RU, O-DU, O-CU, and ultimately the core network. This process includes activating backup O-DU, reactivating the affected cells, and utilizing resiliency mechanisms like active-standby configurations. It is desired for the cell restoration time to be as shortest as possible. The measures, such as recovery initiated by the SMO, can significantly minimize downtime and reduce service disruptions in the affected area.

# 5.4.4 O-CU-CP failure

# 5.4.4.1 Overview

A failure in the O-CU-CP of a O-RAN network can severely disrupt cell service by interrupting critical signalling between UE and the core network, leading to issues like failed call setups, handovers, and session management. This disruption can also cause subsequent mass signalling storms if UE session restoration is not supported by the O-CU-CP. Furthermore, the O-CU-CP loses connectivity with the SMO through the O1 interface, resulting in the loss of configurations from the SMO and the inability of the SMO to receive OAM data (CM, FM, and PM) from the O-CU-CP via the O1 interface [i.8]. Restoration processes for $\mathrm { g N B }$ , cell services, and user sessions are crucial to re-establish functionality, minimize disruptions, and ensure service continuity. The following outlines various aspects to consider in the event of an O-CUCP failure.

# 5.4.4.2 Impacts of O-CU-CP failure

The key impacts are described below.

Loss of UE sessions in gNB across many cells, as one O-CU-CP can serve many cells and O-DUs. Mass RACH from many UEs that lost connectivity to cells served by O-CU-CP and O-DUs with related mass NGAP signalling leading to signalling storm.

# 5.4.4.3 Cell services restoration

Restoring cell services in the O-RAN network involves re-establishing connectivity and functionality following a disruption or failure. This process is essential to minimize downtime and ensure the user’s experience of uninterrupted access to network services. Restoration efforts focus on both the Control Plane (O-CU-CP) and User Plane (O-CU-UP) components, addressing challenges such as stale UE contexts, missed signalling messages, and disrupted data flows. By efficiently restoring cell services, the network can quickly return to optimal performance, ensuring reliable communication and data services for users.

# 5.4.5 O-CU-UP failure

# 5.4.5.1 Impacts of O-CU-UP failure

An O-CU-UP failure in a 5G O-RAN network can disrupt the transmission of user data between the UE and the core network, leading to affected data sessions, reduced service quality, and potential data loss. Additionally, O-CU-UP can’t communicate with the SMO via the O1 interface.

# 5.5 Resiliency for interface failures

# 5.5.1 Overview

Resiliency for interface failures focuses on maintaining efficient network operations with minimal disruption, even in the event of physical or virtual interface issues in 5G systems. Key strategies include NIC card failures through physical and/or virtual NIC failovers, implementing dynamic IP routing with SCTP multihoming, and utilizing TNLA [i.2] to enhance control plane reliability. These methods leverage heartbeat mechanisms and multiple transport addresses to facilitate rapid failover and recovery. By adhering to 3GPP standards (e.g., TS 23.501 [i.2], TS 29.244 [i.16]), these approaches ensure service continuity and effectively minimize disruptions during failures.

# 5.5.2 Generic aspects

Resiliency for interface failures aims to ensure seamless network operations with minimum disruption, even when physical or virtual network interfaces experience issues. This requires deploying robust mechanisms to maintain service availability and reduce downtime.

Strategies for ensuring interface resiliency in 5G RAN systems focus on redundancy and load balancing, for e.g., utilizing Linux bonding for physical NICs and failover-capable virtual NICs in virtual environments. IP-level routing resilience is achieved through multiple IP addresses, SCTP multihoming, and dynamic protocols such as IP Fast Reroute. Control plane protocol stability is reinforced through TNLA, incorporating features like multiple transport addresses and heartbeat mechanisms. These reliability measures, outlined by 3GPP (for e.g., TS 23.501 [i.2] and TS 23.502 [i.3]) enable quick recovery from failures while minimizing service disruptions.

# 5.5.2.1 NIC failure - hardware or virtual interface failure

NIC failures can occur in both physical and virtualized environments due to hardware malfunction, driver issues, or connectivity disruptions. These failures result in the inability of the system to send or receive network traffic, potentially leading to service interruptions and degraded performance.

NIC failure mitigation ensures uninterrupted network connectivity in the event of hardware or virtual interface failures. For physical NICs, solutions such as Linux bonding aggregate multiple NICs into a single logical interface, providing redundancy and load balancing. In the event of a failure, traffic is automatically redirected to functioning NICs, with configurations like active-standby for failover or load balancing for enhanced throughput. In virtualized environments, failover-capable virtual NICs provide redundancy by switching traffic to backup NICs during a failure. The configurations such as NIC teaming, further ensure smooth failover and high availability. Together, these strategies are to improve the stability and reduce service disruption caused by NIC failures.

# 5.5.2.2 IP level routing failure

IP level routing failures occur when the primary network path becomes unavailable due to issues such as link disruption, node failure, or routing misconfigurations. These failures can lead to packet loss, increased latency, or total service interruptions, affecting critical network operations.

By leveraging multiple IP addresses, SCTP multihoming, dynamic routing protocols, and IPFRR, networks can achieve enhanced resilience against routing failures. These strategies ensure quick recovery, maintain traffic flow, and reduce service disruptions, improving overall reliability and user experience.

# 5.5.2.3 SCTP connection failure

SCTP connection failures can occur when the communication path between two endpoints is disrupted. This can result from physical link issues, routing failures, or misconfigurations. Such failures impact data transfer, control signalling, and application performance. SCTP, however, provides mechanisms like multihoming and retransmission strategies to recover from such failures [i.4].

Application protocol stability is enhanced through mechanisms like 3GPP TNLA, heartbeat monitoring, and redundant associations [i.4]. TNLA enables multihoming by supporting multiple transport addresses, allowing traffic to reroute through alternate paths if the primary path fails. Heartbeat mechanisms actively monitor path availability by exchanging regular signals between endpoints to detect and handle failures quickly. Redundant SCTP associations provide parallel connectivity and load balancing, ensuring uninterrupted data flow even during disruptions. These solutions collectively improve fault tolerance, enable fast recovery, and minimize service disruption, ensuring reliable traffic flow and high availability in 5G networks.

# 5.5.3 Control plane interface failures

# 5.5.3.1 Overview

Control plane interface failures occur when critical signalling interfaces like fronthaul C-Plane, F1-C, E1, X2-C, Xn-C, and $\mathrm { N g \mathrm { - } C }$ interface got affected, impacting communication and coordination between network functions such as O-CU, O-DU, O-RU, and AMF. These failures can disrupt UE session control, mobility, and bearer management, potentially affecting UE services. Resiliency can be maintained through redundant transport links [i.4 and i.11], various recovery mechanisms, and cloud-based backups, ensuring rapid failover and robust control-plane operations with minimal service impact.

# 5.5.3.2 F1-C interface failure

The F1-C interface links the O-CU-CP and O-DU, managing control-plane signalling for user and control data flows. Failures, including SCTP link issues, O-DU restarts, or F1AP application and protocol stack interruptions, can disrupt signalling and necessitate F1 Setup procedure. SMO could detect F1-C interface failures through O1 interface and react by triggering appropriate actions.

Resiliency can be achieved through methods like SCTP multi-homing for physical transport redundancy [i.4]. Additionally, application-level failover can be implemented using multiple TNL associations, allowing switch to a secondary F1AP application if the primary connection fails [i.4 and i.11].

# 5.5.3.3 E1 interface failure

The E1 interface links the O-CU-CP and O-CU-UP, handling signalling for split bearer control and user-plane state management. Failures, such as SCTP link loss, node restarts, or protocol stack issues, can affect the service bearers. SMO could detect E1 interface failure using alarm raised by O-CU and react by triggering appropriate actions.

Resiliency is ensured through various approaches such as redundant SCTP endpoints for physical transport redundancy [i.11], retry mechanisms, and failover support for E1 Setup. Additionally, application-level failover can be implemented using multiple TNL associations.

# 5.5.3.4 X2-C interface failure

The X2-C interface connects O-CU-CP and O-eNB [i.17], enabling inter-RAT signalling. Failures can affect handover operations, hence UE mobility. For NSA, failure on X2-C interface can further cause the UEs losing connection completely with the NR cells and falling back to single connection with the O-eNB. SMO could detect X2-C interface failures through O1 interface and react by triggering appropriate actions.

Resiliency can be achieved through methods such as SCTP multi-homing for physical transport redundancy, the application-level failover can be implemented using multiple TNL associations, allowing failover to a redundant X2-C links if the primary connection fails [i.19, i.15, i.18, and i.2].

# 5.5.3.5 Xn-C interface failure

The $\mathrm { X n - C }$ interface, as defined in [i.20], serves as a critical control plane interface between NG-RAN nodes, such as gNBs. It enables coordination between nodes for functions such as mobility management (e.g., handover), dynamic resource allocation, and load balancing. An $\mathrm { X n - C }$ interface failure arises when control signalling between connected NGRAN nodes is disrupted, which can be caused by transport or link losses, software or hardware malfunctions.

SMO could detect above Xn-C interface failures through O1 interface and react by triggering appropriate actions.

The Xn-C interface can utilize protocols such as SCTP for reliable signalling and communication between these nodes [i.20, i.15, i.18, and i.2].

An Xn-C interface failure disrupts coordination between NG-RAN nodes, leading to widespread implications across the RAN system, cell services, and user sessions:

RAN system: Loss of coordination hinders mobility management, distributed SON, energy savings, dual connectivity, and dynamic resource allocation, causing handover failures and uneven resource utilization with some cells experiencing congestion while others remain underused.   
Cell service: Service continuity is interrupted due to failed handovers, resulting in dropped calls, loss of throughput (due to dual connectivity failures), and degraded Quality of Service, especially in interference-prone edge scenarios.   
User sessions: User sessions may drop during mobility events, and isolated gNB operation can lead to lower throughput, higher latency, and inconsistent service quality.

# 5.5.3.6 NG-C interface failure

The NG-C interface is the control plane interface between the O-CU-CP and the AMF in the 5GC [i.21, i.15, i.18, and [i.2]]. This interface is crucial for signalling operations, such as session management, mobility handling, and resource allocation. NG-C uses the NGAP for its functionality. NG-C interface failure disrupts mobility management, resource allocation, and signalling, causing handover failures, service disruptions, and load imbalance. Users face dropped sessions, increased latency, and poor connectivity, significantly degrading the overall experience.

SMO could detect NG-C interface failures through O1 interface and react by triggering appropriate actions.

# 5.5.3.7 E2 interface failure

The E2 interface connects the Near-RT RIC and E2 node such as O-CU-CP, O-CU-UP, and O-DU. An E2 interface failure occurs when communication between the Near-RT RIC and any E2 Node is disrupted. This could be caused by transport link failures/issues, software malfunctions, or configuration error. While the specifics of such disruptions are not covered in detail within this technical report, detection mechanisms are in place on both the Near-RT RIC and E2 nodes. When detected, these entities can notify the SMO system through the O1 interface.

Even if either the E2 Node or the Near-RT RIC encounters a failure, the E2 Node retains the capability to provide fundamental services [i.12]. However, certain enhanced services may be temporarily unavailable due to their reliance on the Near-RT RIC. Examples of impacted services include:

Non-delivery of dynamic and static policies.   
• Loss of monitoring and control functions for certain optimization features.   
• Disruption in enforcement loops for policy execution.

The E2 interface design is to ensure that network priorities like service availability and performance stability remain largely intact, despite E2 interface disruptions. To support resiliency and prevent service outages (though with potential performance degradation due to unavailable xApp algorithms), further mechanisms can be employed for robust fault management and operational continuity.

# 5.5.3.8 Fronthaul C Plane Interface Failure

Fronthaul control plane failures can be detected through the O-RU’s C/U-Plane connectivity monitoring, which triggers the “C/U-plane logical connection faulty” alarm, or via the O-DU’s verification of C/U-Plane transport connectivity using Loop-back Protocol (IEEE 802.1Q) as outlined in [i.7]. These failures can also arise due to hardware issues in the ODU/O-RU or system shutdowns. The key impacts are described below.

A fronthaul control plane failure refers to the disruption in signalling communication between the O-DU and O-RU over the Control Plane in the O-RAN Fronthaul interface, which is critical for transmitting real-time control information [i.13]. This failure can lead to severe impacts on RAN networks, particularly in the Fronthaul perspective, including service degradation due to loss of scheduling, and an inability to update configurations dynamically.

# 5.5.3.9 A1 interface failure

The A1 interface is a crucial component of the O-RAN architecture, facilitating communication between the Non-RT RIC and the Near-RT RIC [i.14].

# 5.5.3.9.1 Impact of A1 interface failure

The impact of A1 interface failures on O-RAN networks can be significant, affecting various aspects of network performance and service delivery:

Policy management: The inability to create, update, or delete policies can lead to suboptimal RAN performance, missed Service Level Agreement (SLA) targets, and inefficient resource utilization. Enrichment information: Loss of access to critical enrichment data (e.g., traffic patterns, radio fingerprints) degrades the Near-RT RIC's decision-making capabilities, adversely affecting traffic steering and resource management.   
• Feedback loop: Disruption in feedback transmission prevents the non-RT RIC from assessing policy enforcement success, hindering effective policy fine-tuning.

# 5.5.4 User Plane interface failures

# 5.5.4.1 Overview

User plane interface failures occur when critical data-carrying interfaces like Fronthaul U-Plane, F1-U, X2-U, Xn-U, and NG-U experience disruptions, impacting the transport of traffic between network elements such as O-RU, O-DU, O-CUUP, and UPF. These failures can result in service interruptions, degraded Quality of Service (QoS), and loss of user plane session for User Equipment (UE). Resiliency is achieved through mechanisms such as dual connectivity (two O-CU-UP per UE), multi access PDU sessions (multiple UPFs per PDU session) as described in 3GPP 23.501, and session state recovery via cloud-native architectures. Fault detection and self-healing processes further ensure user-plane operations with minimal service impact.

# 5.5.4.2 F1-U interface failure

The F1-U interface connects the O-CU-UP and O-DU, facilitating the transfer of user-plane data packets between these network functions in the NG-RAN architecture. Operating over GTP-U, this interface ensures efficient and low-latency data forwarding for active sessions. Failures on the F1-U interface, such as GTP-U session interruptions, O-DU reboots, or transport link failures, can cause connection loss, service degradation, or session termination.

SMO could detect F1-U interface failures through O1 interface and react by triggering appropriate actions.

Resiliency can be achieved through mechanisms like path redundancy (transport related) using multiple GTP-U tunnels (i.e., dual-connectivity) as defined in [i.15 and i.22]. Additionally, load balancing across redundant paths and intelligent failover procedures ensure continuous data flow, minimizing the impact of transport layer disruptions.

# 5.5.4.3 NG-U interface failure

The NG-U interface is the user-plane interface between the O-CU-UP and the UPF in the 5G Core Network. This interface is responsible for forwarding data packets, enabling efficient data delivery for active sessions. NG-U operates using GTPU transport protocol [i.23], ensuring the transport of uplink and downlink data through reliable tunnelling. Failures on the NG-U interface, such as GTP-U tunnel breaks or transport network disruptions, can lead to user plane session disruption, impacting end-user experiences.

SMO could detect the NG-U interface failures through O1 interface based on the alarms raised by O-CU-UP and react by triggering appropriate actions.

Resiliency can be ensured by employing existing mechanisms like redundant GTP-U tunnels (i.e., MA-PDU sessions) as described in [i.2, i.15, i.18, and i.21]. Fault monitoring, proactive recovery, and load balancing further enhance the reliability and robustness of the NG-U interface, ensuring data delivery with minimum disruption in 5G networks.

# 5.5.4.4 X2-U interface failure

The X2-U interface connects the O-CU-UP and the O-eNB, facilitating user-plane data transfer in inter-RAT scenarios, such as LTE to NR handovers or dual connectivity deployments. It operates using GTP-U [i.24], ensuring transport of traffic with minimum disruption during active sessions.

Failures on the X2-U interface, such as GTP-U tunnel disruptions or transport link issues, can lead to packet loss, service interruptions, and degraded user experience.

SMO could detect X2-U interface failures through O1 interface based on the alarms raised by O-CU-UP and react by triggering appropriate actions.

Fault detection and session management can be employed to ensure minimal impact on user experience and uninterrupted data transport during mobility scenarios.

# 5.5.4.5 Xn-U interface failure

The Xn-U interface, as defined in [i.15 and i.25], supports user-plane data transport between NG-RAN nodes like gNBs during inter-gNB mobility events. Using GTP-U, it ensures efficient, low-latency data forwarding for handovers with minimum disruption. Failures, such as GTP-U tunnel disruptions or transport issues, can cause mobility interruptions, degraded QoS, and dropped user sessions.

SMO could detect Xn-U interface failures through O1 interface based on alarms raised by O-CU and react by triggering appropriate actions.

Resiliency can be achieved through redundant tunnels (i.e., MRDC) [i.2, i.15, i.18, and i.20], failover mechanisms, and robust monitoring and recovery processes, ensuring data delivery with minimum disruption and maintaining optimal mobility performance.

# 5.5.4.6 Fronthaul U plane interface failure

Fronthaul U plane interface failures disrupt IQ data transfer between the O-DU and O-RU [i.13], affecting user-plane services and degrading network performance. These failures arise from transport link disruptions or hardware malfunctions, leading to service interruptions, dropped user sessions, and increased latency. Detection mechanisms include reception window monitoring, Loop-Back Messages (LBM), and UDP Echo for transport verification. WG4 is expected to investigate the resiliency measures, such as redundant links, and dynamic buffering, ensuring recovery and minimum service disruption. These mechanisms are critical for maintaining robust and reliable network operations.

# 5.5.5 Management plane interface failures

Management interfaces like O1, O2, and the fronthaul M-plane can experience failures or degradation due to various factors, which are beyond the scope of this TR. These issues can be detected by the MnF of MnS Producers, such as OCU-CP, O-CU-UP, O-DU, O-RU, Near-RT RIC, and O-Cloud, as well as by the MnS Consumer (SMO) for their respective management interfaces using appropriate detection mechanisms. The following clauses describe how each interface failure can be identified and the associated impact.

# 5.5.5.1 O1 interface failure

O1 interface failure refers to the disruption or malfunction of the O1 interface within the O-RAN architecture. This interface plays a critical role in facilitating communication between the SMO framework and the O-RAN NFs, such as O-CU-CP, O-CU-UP and O-DU and managed elements like near RT-RIC, as specified in [i.9]. The detection of an O1 interface failure can be achieved through mechanisms like heartbeat management, as specified in [i.8]. The detecting and recovering from an O1 interface failure could involve several considerations, including how the NF handles FCAPS reporting during the disruption. For example, if the O1 interface fails during a PM data reporting period, the NF can store the collected metrics and report them once the O1 interface is restored.

In the event of failure, the SMO can initiate reconfiguration steps for the affected entities such as O-CU-CP, O-CU-UP, or O-DU. This process involves the MnS Consumers within the SMO framework and MnS Producers within the O-RAN Network Function, ensuring that the network elements are reconfigured and restored to operational status. The SMO framework plays a crucial role in this recovery process by orchestrating the necessary actions to maintain the service with minimum disruptions and robustness across the O-RAN network, thereby ensuring that the network functions are ready for service post-recovery.

# 5.5.5.2 O2 interface failure

In an O-RAN deployment, an O2 interface is used to enable the SMO as a consumer, managing both cloud infrastructure and cloud deployments [i.6]. A failure in the O2 interface between the SMO and O-Cloud disrupts resource management, orchestration, and applications within the O-Cloud. Such failures can be identified using appropriate mechanisms [i.6]. To ensure resiliency, the SMO detects faults through methods such as heartbeats and alarms, analyses its impact, and reconfigures workloads using local controllers or cached configurations. Backup system and redundant O-Cloud resources help to maintain the services with minimum disruption, preserving the critical workloads. Failure reporting procedures and effective failover mechanisms can be employed to minimize downtime and ensure rapid recovery.

# 5.5.5.3 Fronthaul M-plane interface failure

The fronthaul M-plane enables the O-DU to manage the O-RU in a hierarchical deployment and allows both the SMO and O-DU to manage the O-RU in a hybrid deployment. A failure in the fronthaul M-plane interface interrupts the management of the O-RU FCAPS operations. This failure can be detected through mechanisms such as alarms, notifications, and PM counters specified in [i.7]. The O-DU can evaluate the failure by itself or can coordinate with the SMO for evaluation. Based on the failure’s scope, O-DU can resolve it autonomously, or the SMO can initiate corrective actions, such as activating backup links, reallocating carriers, or reconfiguring the O-DU and O-RU to restore connectivity.

From a resiliency perspective, the O-DU can try to minimize the service disruption by appropriate recovery mechanisms. The SMO orchestrates these operations by interacting with the O-DU, ensuring that the cell services recovered with minimum interruptions. For scenarios involving shared O-RUs, the SMO can reassign the affected O-RU’s carriers to an alternate O-DU to mitigate service disruptions.

# 5.6 Transport layer failures

# 5.6.1 Overview

A transport layer failure in 5G and O-RAN networks is a disruption in the communication links—fronthaul, midhaul, or backhaul—that connect essential network components such as the O-CU, O-DU, and O-RU. These links are essential for reliable data transfer and signalling throughout the network, directly affecting performance and continuity. Recovery from transport layer failures is therefore a key aspect of O-RAN network resiliency. The following clause illustrates a transport node (TN) failure resiliency use-case and contrasts localized (domain-scoped) recovery methods with end-to-end recovery schemes, highlighting the advantages of the latter approach.

NOTE: How O-RAN entities interact with TN entities under study as part of transport inclusion work item.

# 5.6.2 Transport layer failure scenarios

Figure 5.6-1 illustrates a scenario in which the O-RU is connected to the O-DU via Site Fabric#1, which can consist of switches within the O-Cloud site network [i.5]. In this case, a failure occurs in Virtualized Switch #1 within Site Fabric $\# 1$ . This failure could be due to hardware malfunction, software errors, or network connectivity issues, disrupting the flow of data between the O-RU and O-DU. Since the O-RU and O-DU rely on this connection for the exchange of control and user data, any breakdown in Virtualized Switch #1 can lead to service interruptions and a degradation in network performance.

To recover from the above failure, a resiliency mechanism can be in place that allows the network to quickly identify and switch to an alternative virtualized switch within Site Fabric #1. This alternative switch is pre-configured to handle traffic in the event of such failures, enabling the O-RU and O-DU to maintain their communication without significant disruption. This rapid failover to an alternate switch minimizes service downtime and supports network continuity, demonstrating a critical aspect of O-RAN’s network resiliency strategy.

By having multiple virtualized switches and a mechanism to detect failures, the network can efficiently manage faults in key components, supporting high availability and reliability across O-RAN deployments.

![](images/28e8379eafcbe9199f9bed92775c0489023d05e22b0bda0024585d2e1bfe6b65.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.6-1: Transport layer failure scenario

# 5.6.2.1 Domain-scoped (localised) recovery scheme

An alternative virtualized switch within Site Fabric #1, such as Virtualized Switch #2, $\# 3$ , or $\# 4$ , is designated to take over the functions of Virtualized Switch #1. However, switches $\# 2$ , #3 or #4 may already be facing technical issues or operating near capacity, which could make them less suitable as replacements for Switch #1. Hence, a localized, or domain-scoped, recovery solution can be sub-optimal.

# 5.6.2.2 End-to-end recovery scheme

By utilizing comprehensive, network-wide visibility with access to real-time event logs for deployed resources and their utilization levels, a virtual switch from Site Fabric $\# 2$ is selected as the recovery switch for the failed Switch #1. Hence the end-to-end recovery scheme provides a more robust recovery solution than the localized recovery scheme.

# 5.6.3 Network function failure scenario

# 5.6.3.1 Overview

Recovery from failures in the O-RAN network function domain is considered as a critical requirement of O-RAN network Resiliency.

The following clause provides an example of O-RAN NF failure and compares the domain-scoped recovery (localized) scheme to the end-to-end recovery scheme, showing the advantage of the latter approach.

# 5.6.3.2 O-DU failure example

Figure 5.6-2 presents a scenario in which the O-RU is initially connected to O-DU #1, while O-DU #2 is the designated as the backup O-DU. O-DU #3 is not designated as backup O-DU, however, it is a possible alternative to O-DU #1. The dotted lines in the figure indicate that an alternative connection can be established between the NFs connected with the dotted line. At some point in time, O-DU #1 fails, and an alternative O-DU is needed. The following two clauses describe domain-scoped and end-to-end recovery solutions.

![](images/94d3cb7b7efd89aa785719a2c341e986d1803f34c2b6b4a88566ae8d2ebc29f2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.6-2: O-RAN network function failure scenario

# 5.6.3.2.1 Domain-scoped (localised) recovery scenario

In a network function (O-DU) failure scenario, a domain-scoped (localized) recovery solution might involve switching to a designated backup, such as O-DU $\# 2$ . However, if O-DU #2 is already overloaded, this recovery approach may be less than ideal. Figure 5.6-3 illustrates this recovery scheme.

![](images/d09ee2d6655811d68ddec6edb44a455fe8eca050c512a10cb9e6901449444a4b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.6-3: NF failure recovery based on domain-scoped (localized) recovery scheme

# 5.6.3.2.2 End-to-end recovery scenario

In the event of an O-DU failure, a recovery solution leveraging network-wide visibility and real-time access to event logs for resource deployment and utilization levels can reroute the O-RU to an underutilized O-DU (O-DU #3). This is achieved by reconfiguring the O-CU, adjusting the underlying transport layer, and updating entries in the DHCP server, as illustrated in Figure 5.6-4. When the O-RU detects it can no longer communicate with O-DU #1, it initiates a reset and performs a DHCP query to obtain the IP address of O-DU #3. This process allows the O-RU to establish a new connection with the available O-DU #3, making this recovery scheme more effective than a localized, domain-scoped recovery approach.

![](images/86539ca88305acbf0f84df9577b4fd1cadd92142a2a5751d2577376bdfea2fa5.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.6-4: NF failure scenario with end-to-end recovery scheme

# 5.7 Cloud layer failures

The following are the types of failures that can occur at the cloud layer in O-RAN systems, which can be mitigated through effective resiliency solutions:

Infrastructure related failures: Examples include O-Cloud failure, O-Cloud site failure, node cluster failure, other resource failure   
• IMS related failures: Examples include IMS software failure, IMS software update failure, O2-IMS interface failure and IMS provisioning procedure failures   
• DMS related failures: Examples include DMS control-plane failure, DMS control-plane upgrading failure, DMS deployment-plane failure, NF Deployment LCM failure   
O-Cloud application related failures: Examples include pod failure, VM failure, NF deployment failure

These categories highlight potential disruptions that could affect system functionality and service continuity. They indicate the impact on running services, understanding the importance of identifying these issues to develop targeted mitigation strategies. By understanding these failure scenarios and their implications, this chapter lays the groundwork for proposing solutions that enhance the robustness and reliability of O-Cloud deployments.

# 6 Scenarios and considerations

# 6.1 Service restoration time considerations

Service restoration time is an important factor that plays a critical role in resiliency. There are several critical factors that affect service restoration time after an O-DU failure:

Failover mechanisms: Networks using automatic failover mechanisms with pre-configured backup O-DUs reduce service restoration times. In contrast, systems with manual or dynamic reconfigurations experience longer delays.   
• IP switchover and NF coordination: IP switchover and NF coordination with the resiliency controller are essential for re-establishing the service.   
• Backup strategies: 1:1 (one backup per O-DU) offers faster recovery but are more resource-intensive. Alternatively, n:1 (one backup for multiple O-DUs) is more economical but involves reconfiguration time.

Service recovery time varies based on the network's resiliency strategy, architecture, and complexity, typically ranging from seconds to minutes.

# 6.2 Deployment scenarios

This clause discusses the different deployment scenarios in O-RAN — hierarchical and hybrid — and their impact on resiliency. Each deployment presents unique challenges and opportunities for fault detection, recovery the service with minimum interruptions. The SMO's role in coordinating these efforts is crucial to ensuring network stability and minimizing disruptions across these deployments.

# 6.2.1 Hierarchical deployment

In a hierarchical deployment, resiliency is achieved by assigning specific roles to each entity. For example, it is recommended that O-DU can detect faults by analyzing FM and PM data and manage some failure mitigation in O-RU and configuration based on its capability. The SMO, as the O1 MnS Consumer, acts as a centralized entity to oversee these actions and provide guidance to O-DU in the form of policies and/or configuration details to ensure coordinated failure mitigation. This approach facilitates fault isolation, allowing localized handling of faults at the O-DU level, thereby preventing them from affecting the entire network. For step-by-step recovery, if an O-DU fails, services can be rehomed to another O-DU, or a standby O-DU can be activated.

This approach facilitates a distributed recovery mechanism to ensure network resiliency against failures. It also ensures quick recovery, as actions are partially executed at the NF level. For example, the O-DU can detect alarms and perform recovery actions. The O-RAN hierarchical deployment offers significant advantages for resiliency from an OAM perspective. By clearly defining roles and responsibilities, it simplifies management, enhances fault detection and isolation, and supports structured recovery mechanisms. The centralized oversight provided by the SMO ensures consistent policies and coordinated actions, further enhancing network resiliency. This structured and proactive approach makes the hierarchical deployment a robust solution for maintaining network stability and minimizing service disruptions. In this deployment, the SMO configures the O-RU through the O-DU, with the O-DU playing a key role in managing ORUs and handling configurations.

The hierarchical deployment facilitates a controlled and centralized recovery process, where the SMO and O-DU collaborate to restore services after failures. If the O-DU fails, the SMO can reassign configuration tasks to another ODU, making the O-DU a critical node for ensuring resiliency.

# 6.2.2 Hybrid deployment

From an OAM perspective, achieving resiliency in an O-RAN hybrid deployment necessitates coordination between the SMO and the O-DU for managing the O-RU, as well as the integration of centralized and distributed components.

NOTE: The specific roles and responsibilities of the SMO and O-DU in managing the O-RU within a hybrid deployment are currently under discussion within O-RAN and have yet to be finalized. Once these responsibilities are defined, this clause will be revisited and updated accordingly.

# 6.2.3 Transport resiliency considerations

Transport networks play a crucial role in ensuring reliability and recovery, utilizing redundancy protocols such as e.g., SCTP multi-homing [i.4], and other mechanisms to enable potential failover across fronthaul, midhaul, and backhaul links. Additionally, robust alarm delivery and telemetry monitoring are vital for maintaining service continuity in hierarchical and hybrid deployments.

# 6.3 Considerations for resiliency

Ensuring resiliency in O-RAN deployments involves robust planning across various network entities, including RAN nodes (O-RU, O-DU, O-CU), interfaces, transport layers, and the O-Cloud infrastructure. The SMO plays a critical role in managing the state, and recovery of these components, coordinating failovers and service restoration. Resiliency strategies like active-standby configurations are crucial for minimizing service disruptions. End-to-end OAM processes, including performance monitoring and fault management, further enhance the network's ability to recover from failures and maintain service with minimum disruption.

# 6.3.1 Backup options

The SMO serves as the resiliency controller, playing a critical role in minimizing service disruptions caused by failures. It manages the switchover to backup units and resources, ensuring uninterrupted service across the network. To achieve this, the SMO ensures resiliency by managing resilient instances for network functions such as O-DU and O-CU. This is accomplished through backup mechanisms like software-based backups and hardware-based backups, to maintain service continuity.

# 6.3.1.1 Software-based backup

Involves creating snapshots or backups of the software configurations, which can be utilized to recover the service in case of failure. For example, NF software images, container images, or application states.

# 6.3.1.2 Hardware-based backup

Dedicated standby hardware components along with associated software that can take over in case of failure. This is usually more costly but provides a quicker recovery.

# 6.3.2 Redundant node options

To ensure the resiliency in an end-to-end O-RAN systems, the redundant or standby node options are necessary to quickly recover from the failures, but at the associated cost.

The standby node or NF can have the same capabilities as the active NF. The SMO can manage this depending on the resiliency scenarios and deployments. The above can be quantified in terms of the management of carrier resources, associated throughput, the number of UEs, and the number of cells/sectors.

In a scenario where a standby O-DU is unavailable, malfunctioning, or experiencing issues such as port failures or Mplane connectivity problems, it cannot be utilized for recovery. In such cases, the SMO may need to explore alternative recovery strategies like having more than one resilient O-DU instance, but end-to-end service availability might not be fully restored if no functional back-up O-DU is available. In a scenario with multiple back-up O-DU instances, SMO can decide which O-DU can take over the O-RU operation based on the traffic requirements and network conditions.

For example, the O-DU resiliency options can consider the following.

Active-standby – If the active O-DU fails, the standby O-DU is activated. The M-plane connection with the ORU can remain active, enabling the standby O-DU to take over the O-RU services as quickly as possible. In this scenario, resources can either be pre-allocated or allocated only after a failure occurs depending on the deployment. The active and standby O-DUs can be connected to the same O-CU (Intra O-CU) or different O-CUs (Inter OCU) depending on the deployment. The example standby configuration options include $1 { + } 1$ , N (Active) $+ \mathrm { \sf K }$ (Standby), and $_ { \mathrm { N + 1 } }$ (All active with 1 hot spare).

# 6.3.2.1 $1 + 1$ redundancy

Each active node has a dedicated standby node and it is simple but can be resource-intensive and expensive.

# 6.3.2.2 $N + 1$ redundancy

One standby node serves multiple active nodes. This is more resource-efficient and cost effective for managing failovers.

# 6.3.2.3 $\mathsf { N } { + } \mathsf { M }$ redundancy

There are multiple standby nodes (M) for the SMO to utilize in the event of failure in one or more active nodes (N). This is a trade-off between the cost of resiliency and the probability of successful service recovery, with the goal of minimizing service outages.

# 6.3.3 Entities

Entities that can be involved in O-RAN network resiliency procedure are as follows:

• RAN nodes: Includes O-RU, O-DU, and O-CU, which are critical O-RAN network functions.   
• Interfaces: Resiliency considerations include handling failures or degradations in the functionalities supported over interfaces such as A1, O1, O2, E2, and R1.   
• Transport: Network layer and port redundancy are key for maintaining transport resiliency.   
• O-Cloud: The infrastructure layer, comprising a platform that abstracts the underlying physical resources (e.g., CPUs, GPUs, storage, and data centers), enables a virtualized and resilient environment for hosting containers and clusters. This environment serves as the foundation for deploying network functions, such as O-DU and O-CU, and is integral to ensuring O-Cloud resiliency.   
NOTE: The O2 interface is crucial for managing O-Cloud resources and ensuring resiliency. The role of SMO in handling O-Cloud resiliency is addressed as part of the WG6 Resiliency WI.   
RIC: The RIC, including Non-RT RIC and Near-RT RIC, plays a vital role in network management.   
• SMO: Acts as the central resiliency controller, managing state, failovers, and service restoration

# 6.3.4 End-to-end aspects

End-to-end OAM aspects for resiliency focus on the monitoring, management, and orchestration of key components within O-RAN system to minimize service disruptions. This includes fault detection, performance monitoring, and proactive maintenance for critical components such as O-RU, O-DU, and associated network services. It also covers the cloud infrastructure in the case of CNF deployment, as well as the interfaces like fronthaul and O1. The SMO plays a critical role in managing these aspects, ensuring service disruptions minimized as much as possible by appropriate recovery mechanisms.

SMO can leverage the AI/ML capabilities to enhance decision-making during resiliency scenarios. This enables the SMO to efficiently recover service paths and restore service availability while minimizing disruptions. This approach strengthens resiliency across various O-RAN deployment scenarios, ensuring collaboration with the SMO, and resiliency strategies to safeguard service availability effectively.

Key components of this resiliency approach include:

Performance monitoring and fault detection: Utilizing supervisory controls to detect failures at multiple elements involved in service path, and VNF and cloud infrastructure in case of cloud deployment, as well as across O-RU, O-DU, and OCU nodes.

Recovery mechanisms: Employing manual or automated healing processes that restore service upon detection of failures, including switchover to backup systems or reconfiguring NFs such as O-CUs and O-DUs.

Resiliency models: Implementing resiliency strategies as described in clause 6.3.2, sparing across network functions and transport systems to minimize downtime. This covers not only the physical node failovers but also VNF and CNF, to ensure resiliency in various deployments.

# 6.4 Relationships with rolling upgrade

# 6.4.1 Overview

Ensuring resiliency during rolling upgrades in a 5G network is critical to maintaining uninterrupted service for users while upgrading network components incrementally. Rolling upgrades in 5G networks involve updating software, hardware, or configurations in a phased manner to avoid downtime and ensure continuous service availability. Many resiliency techniques for protecting 5G network against failures are key enablers for resilient rolling upgrade also. Below are the key resiliency technologies and strategies for rolling upgrades in 5G mobile networks.

# 6.4.2 Redundant NF architectures

Redundant architecture ensures that multiple instances of critical network components (e.g. O-DU, O-CU-CP) are available to handle traffic and prevent service down time not only due to unexpected failures but also due to rolling upgrades. High availability distributing traffic across redundant instances. Service interruption in one instance during the upgrading will not affect the entire system thus ensure service continuity.

Both active-standby or active-active NF redundancy architecture can be approached. In active-standby configuration, new NFs take over the UE traffic when a NF fails or being shut down due to upgrading. In active-active configuration, critical UE traffic is steered to healthy network functions that were serving other users before a failure or upgrading happens to a NF. The rolling upgrading case, the new NF taking over the traffic can be the newer version of application or equipment to be upgraded to or the older version to be fallback to. Cross-region redundancy, e.g. deploy active and standby O-CUCPs and O-CU-UPs in different regional data, may be also required to prevent single regional failures during upgrading.

Existing redundant and failover features supported in O-RAN and 3GPP, e.g. OFH shared O-RU for redundancy, $\mathrm { F } 1 / \mathrm { X } 2 / \mathrm { X n } / \mathrm { N g }$ interface multi-TNL associations and failovers, are important techniques to support rolling upgrade also. It ensures standby NF instances are brought in and connected with other NFs automatically and the service recovers quickly or is completely uninterrupted during the upgrading.

# 6.4.3 Resiliency technologies in cloud-native NFs

5G networks increasingly rely on cloud-native principles, such as containerization and microservices, for scalability and flexibility. Cloud-native architecture enables rolling upgrades of individual microservices without affecting the entire NF. Automated scaling ensures network capacity is not affected during failures or upgrading. Automated failover mechanisms ensure existing traffic and context are hand overed to other healthy microservice instances seamlessly with less effort and service interruption during the upgrading. Load balancers distribute traffic across multiple instances of an application, traffic is routed away from instances being updated to ensure uninterrupted service.

Rollback mechanisms allow reverting to a previous version of software or configurations if issues are detected during rolling upgrades. It minimizes downtime and service disruptions in case of failures during the upgrading. For example, the related cloud technologies include:

C Kubernetes rollback   
• Version control for network configurations (e.g., GitOps)   
• Other cloud-native rollback tools

# 6.4.4 Redundant transport paths

Redundant network paths ensure that traffic can be rerouted in case of failures during upgrades. It prevents single points of failure in the transport network and ensures continuous connectivity during upgrades.

# 6.4.5 Monitoring and observability

Performance monitoring and fault management data provide insights into the health and performance of the 5G network during either unexpected failures or rolling upgrades. Detecting and mitigating issues in real-time is important. Automated rollback in case of failures is needed if issues cannot be mitigated in time with other solutions. AI/ML and analytics could be important tools to detect and diagnosis issues in real-time for quicker response and minimized the service impact.

# 7 Potential resiliency solutions

# 7.1 Overview

This clause outlines the potential resiliency solutions managed by SMO. These solutions include the resiliency of O-DU and O-CU-CP, utilizing standby O-DU and O-CU-CP, and leveraging the transport resiliency capabilities for rehoming O-RUs from one O-DU to another. Additionally, it addresses the resiliency of NF Deployment(s) within O-Cloud. End

to-end resiliency can be achieved through cross-domain orchestration, and automated or operator-managed service continuity. The following sub clauses describe the various resiliency solutions that can be used for resilient O-RAN networks to minimize the service interruptions during the failure.

# 7.2 Solution 1: Enhanced network resiliency through standby ODU and adaptive cell activation managed by SMO

# 7.2.1 Basic objective

This clause details the mechanisms by which the SMO framework manages the recovery of an O-RU and associated user services in the event of an O-DU failure (complete or partial). The SMO can trigger an O-DU switchover in response to a failure affecting the O-RU. The focus is on ensuring system recovery when the active O-DU becomes non-operational (Operational State $=$ Disabled).

Two primary deployment scenarios can be considered:

Active-standby: In this setup, when the active O-DU fails, the SMO can trigger a switchover to a standby ODU, allowing services to continue with minimal disruption.   
Active-active: Here, services can dynamically be rehomed or resource shifting from the failed O-DU to another O-DU, ensuring service with minimum disruption. However, due to the higher deployment cost compared to the previous option, this solution emphasizes active-standby deployments.

NOTE: The "active-active" does not imply that the same cells are operational in both O-DUs; instead, it refers to another O-DU that has its management plane fully operational and ready to take over.

The actors involved can include the SMO, O-CU, O-DUs, and O-RU, which work together to maintain service continuity against O-DU failures.

This solution can also include the SMO framework to manage more complex failure scenarios, such as simultaneous failures of multiple O-DUs, partial failures, or interface disruptions (like the FH-M/CU Plane, F1, E2, and O1). These scenarios might involve the reallocation of resources and reconfiguration of O-RUs to ensure service stability.

The clause can also explore resiliency strategies for different redundancy scenarios, including $_ { \mathrm { N + 1 } }$ and $\mathbf { N } { + } \mathbf { M }$ , where N represents active O-DUs, and M represents standby O-DUs. These can also be applicable in both single and multi-operator Shared O-RU deployments and are designed to optimize resource utilization while ensuring high availability [i.1].

This solution describes the switch-over of the standby O-DU to become the new active O-DU.

# 7.2.2 Roles of involved entities

The description below outlines the actors involved:

1) O-RU:

The O-RU can help in detection of the O-DU connectivity/availability seen from O-RU perspective during a resiliency recovery operation. For example, in the event of an active O-DU experiencing a complete or partial failure, or other failures such as software, interface or others as defined in clause 4.20.1.12 of [i.1], the O-RU can help identify which connections are still functional by reporting the active Netconf status.

2) O-DUs (active/standby O-DUs):

The O-DUs connected to the O-RU play a significant role during a resiliency operation. The active O-DU can serve as the primary unit, managing essential LCM and FCAPS functions and managing the HDLC stack for ALDs connected to the O-RU. In the event of the active O-DU's failure, the other O-DUs connected to the ORU take over to restore services for end users. If the host O-DU fails, the other connected O-DUs step in to manage the associated O-RUs and ensure the service with minimum disruption.

3) O-CU:

O-CU receives cell related configurations from SMO and available cell details from O-DU(s). Based on the available resources reported by O-DU and desired availability of cells received from SMO, the O-CU activates or deactivates the cells in the O-DU using F1 interface.

4) SMO:

The SMO assigns initial roles to the O-DUs (active, standby) or resiliency pairs based on the operator's decisions.

The SMO can be responsible for making high-level decisions related to failures and various resiliency scenarios, including the management of O-DUs when they are taken out of service, whether intentionally or permanently, which impacts O-RU operations. It addresses a range of resiliency challenges such as maintenance, software upgrades, network failures, power outages, and communication link disruptions. Additionally, the operator can use the SMO to switch roles between the currently serving O-DU and another O-DU, designating the latter as the new primary.

# 7.2.3 Solution description

The solution for the O-DU resiliency use case is to recover the O-RU operation and associated services to the users as soon as possible. The O-DU resiliency use case solution is described in Table 7.2.3-1.

Table 7.2.3-1: Enhanced network resiliency with SMO-managed standby O-DU   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification To provide the O-DU instance to the same level of functionality as failed</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>or degraded O-DU instance as soon as possible by reconfiguring the system to use standby O-DU. The SMO periodically monitors the status of O1 interface and, when a complete and irecoverable link failure is detected, triggers automatic failover to a standby O-DU. The potential solution can be the SMO configures standby O-DU to replace the failed O-DU.</td><td></td></tr><tr><td>Actors and Roles</td><td>This is a service impacting use case. O-RU: The O-RU handles the fronthaul and air interfaces and the reporting of performance counters and failures via FH M-plane interface. O-DUs (Active/Standby O-DUs): • All the O-DUs connected to the O-RU are actors that are involved in O-DU Resiliency scenario. O-DU receives cell(s) and associated carriers configurations from SMO and coordinates with O-CU-CP for the activation. O-CU: O-CU receives cell related configurations from SMO and available cell details from O-DU(s). Based on the available resources reported by O-DU and desired availability of cells received from SMO, the O-CU activates or deactivates the cells in the O-DU using F1 interface. SMO: The SMO configures the role of O-DUs as active or standby O-DUs and informs these roles to O-RU through O-DU in hierarchical deployment. It makes high-level decisions related to resiliency scenarios described in Clause 7.2.1.</td><td></td></tr><tr><td>Assumptions</td><td>It is assumed that when the active O-DU fails, there will still be at least one standby O-DU with or without an active Netconf session with the O- RU to restore the services to end user. Several scenarios can trigger the O-DU resiliency use case, as detailed in Clause 7.2.1. This use case addresses complete or partial failures of an O-DU, performance degradation, and other broader issues, with the</td><td></td></tr><tr><td>Begins when</td><td>primary objective of maintaining the operational integrity of the O-RU and O-DU system despite the active O-DU's failure or other disruptions, such as O1 interface failures. This use case is triggered when the primary O-DU encounters any of the above conditions, resulting in its Operational State becoming "disabled" 01 between SMO and O-CU-CP is up and running O-DU#1 is configured to active role with O1 up and running O1 towards SMO.</td><td></td></tr><tr><td>Preconditions</td><td>O-DU#2 is configured to standby role or not configured at all, if it is available the O1 between SMO and O-DU#2 is up and running. SMO has valid subscriptions for alarms, PM counters, and notifications to O-DU#1's, and O-DU#2's if it is connected via O1 interface.</td><td></td></tr><tr><td>Alt Step 1 (M) notifications.</td><td>O-DU#1 (PARTIAL/COMPLETE) FAILURE DETECTION SMO uses the O1 interface to monitors O-DU#1 and detect the service degradation by analyzing the performance counters, alarms, and</td><td>WG10.O1-Interface [i.8]; Use Case</td></tr><tr><td colspan="1" rowspan="1">Alt Step 2 (M)</td><td colspan="1" rowspan="1">The SMO recognizes O1 interface failure or complete O-DU#1 failurethrough FM and/or PM data.See NOTE 1, NOTE 2.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Partial O-DU failure: SMO analyses the notifications / faults / PMcounters from O-DU#1 and detect the partial failure or performancedegradation.Complete O-DU failure or O1 interface failure: SMO analysesnotifications / faults / PM Counters from O-CU-CP to determine ifO-CU-CP has connectivity to O-DU#1 via F1 interfaceCell(s) served by the O-DU#1 with lost O1 interface has beencommunicated by O-DU#1 to O-CU-CP via F1 interface assubject of removal.The result of this step is used by SMO to decide to switch services fromO-DU#1 to O-DU#2 upon detecting failures in Steps 1 and 2.See NOTE 3.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];Use case</td></tr></table>

<table><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The result of this step is used by SMO to decide to switch services fromO-DU#1 to O-DU#2 upon detecting failures in Steps 1 and 2.See NOTE 3.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">CELL(S)AI</td><td colspan="1" rowspan="1">CELL(S) AND ASSOCIATED CARRIERS DEACTIVATION AND OPTIONALLY REMOVE THEM</td><td colspan="1" rowspan="1">REMOVETHEM</td></tr><tr><td colspan="1" rowspan="1">Alt Step 4a (M)</td><td colspan="1" rowspan="1">The SMO uses O1 interface to request O-DU#1 to lock the cell(s)and remove corresponding carrier(s) resources.The O-DU#1 notifies SMO about the status of performed operations.See NOTE 4, NOTE 5.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 4b (M)</td><td colspan="1" rowspan="1">O-DU#1 deactivate the [tr]x-array-carriers as described in Clause 15.3 ofWG4-MP specification and optionally remove the [tr]x-array-carriersresources.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];WG4.OFH.M-Plane[i.7], Clause 15.3;Use case</td></tr><tr><td colspan="1" rowspan="1">Step 4c (M)</td><td colspan="1" rowspan="1">The O-DU#1 notifies the SMO about the status change for cell(s)indicated in Step 4a.See NOTE 6.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Alt Step 5 (M)</td><td colspan="1" rowspan="1">Depending on results determined in Step 3, the SMO uses the O1interface to request O-CU-CP to terminate the F1 interface with the failedO-DU, i.e., O-DU#1.See NOTE 7.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">RECOVER O-RU OPERATION</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-DU#2 to connect with O-CU-CP.The O-DU informs SMO about result of above mentioned operationusing O1 interface.See NOTE 8.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">O-DU#2 becomes the active O-DU to recover the associated O-RUoperations and associated user services.See NOTE 9.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">●  SMO creates and configures the cell(s) associated with O-DU#2 onO-CU-CP through the O1 interface.The O-CU-CP informs SMO about the results of above mentionedoperations through the O1 interface.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8]Use case</td></tr><tr><td colspan="1" rowspan="1">Step 9 (O)</td><td colspan="1" rowspan="1">The SMO configures O-DU#2 with cell(s) corresponding to cell(s)configured to O-CU-CP in Step 5.The SMO provides O-DU#2 with mapping between carrier(s)resources and cell(s) resources.The O-DU#2 informs the results of the above operations to the SMOthrough the O1 interface.See NOTE 10, NOTE 11, NOTE 12.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 10 (O)</td><td colspan="1" rowspan="1">O-DU#2 configures the [tr]x-array-carriers and activates on O-RU asdescribed in Clause 15.3 of WG4-MP specification.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];WG4.OFH.M-Plane[i.7], Clause 15.3;</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The O-RU informs the results of the above operations to the O-DUthrough the OFH M-plane interface.</td><td colspan="1" rowspan="1">Use case</td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">For the cell(s) successfully activated in result of Step 5, the O-CU-CPnotifies the SMO on their activation status via the O1 interface.</td><td colspan="1" rowspan="1">WG10.O1-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">O-DU#2 notifies the SMO on the cell(s) and corresponding carrier(s)activation status via the O1 interface.The O-DU#2 becomes ready to offer services now.See NOTE 13, NOTE 14.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">The SMO makes subscriptions to performance counters andnotifications if O-DU#2 was not configured as stated in Pre-condition.SMO collects the performance counters and notifications from O-DU#2 via the O1 interface.See NOTE 15.</td><td colspan="1" rowspan="1">WG10.01-Interface[i.8];Use case</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The use case ends when the standby O-DU, O-DU#2 shown in the flowdiagram has taken over for the previously active O-DU, O-DU#1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many exceptions. Some of these include:If the O-RU fails during a switch overIf the standby O-DU#2 also becomes unavailable when it is due tobecome active.If any event messaging for the fl ow is lostIf configuration was not done properlyIf the standby O-DU losses the configuration data from the configurationreplica.If the active O-DU returns to service while the standby O-DU is trying tobecome the active O-DU.If the connectivity, or functionality of the management system (SMO)becomes unavailable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SUCCESSFUL POST-CONDITION – On a successful post-condition, theO-RU is connected to the newly active O-DU i.e., O-DU#2, the O-DU#2has started its functions successfully and has properly synchronised withthe O-RU. System utilizing O-DU#2 is ready to accept UEs and providethem with services. Failed O-DU#1 is successfully replaced by O-DU#2in service path.FAlLURE POST-CONDITION – If one of the various exception casesoccurs, there are a variety of failure post conditions. If no O-DUs areavailable and the O-RU is orphaned no service is available and the O-RU could shut down operations. If misconfiguration occurs the O-RU willrespond accordingly. If there are ever two active O-DUs, the O-RU willoperate accordingly.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1. Prior accepting O1</td></tr></table>

NOTE 1: Prior accepting O1 interface failure SMO may apply timer or retry to establish O1 connection with affected O-DU several times. Exact number of re-attempts and value of timer is not subject of this TR.

NOTE 2: It is assumed that O-DU as MnS producer is also able to detect O1 failure and take autonomous reset in case lack of management plane caused by O1 failure. This assumption is taken to avoid uncertainty caused by lack of ability for management system to assess how services are impacted by O-DU without available management interface.

NOTE 3: The logic applied by SMO in this decision process is not subject of this Technical Report.

NOTE 4: The process of cell deactivation/removal between O-CU-CP and O-DU#1 utilizes F1 interface. Related communication over F1 interface is not the subject of this TR.

NOTE 5: SMO's logic employed to decide if cell will be locked or removed is not subject of this CR.

NOTE 6: The process of cell deactivation/removal between O-CU-CP and O-DU#1 utilizes F1 interface. Related communication over F1 interface is not the subject of this TR.

NOTE 7: SMO's logic employed to terminate the F1 interface is not subject of this TR. The success or failure of the F1 termination does not impact the rest of the steps.

NOTE 8: Provisioning of TNL configuration by SMO to O-DU#2 is the enabler for the F1 establishment between O-DU#2 and O-CU-CP.

NOTE 9: There are preconditions that are relevant and necessary for this to happen. It is necessary that a call home between the O-RU and standby O-DU i.e., O-DU#2, and the replication of the configuration information has occurred, and that the O-DU#2 has the configuration of the O-DU#1.

NOTE 10: If F1 is established, the O-DU#2 informs the O-CU-CP about cell(s) availability using the F1 interface. Related communications over F1 interface is not the subject of this TR.

NOTE 11: In hierarchical deployment in this step SMO also provides O-DU with configuration for O-RUs served by this O-DU.

NOTE 12: F1 interface is used to exchange information needed for cell activation between O-CU-CP and O-DU.

NOTE 13: Following the transition, O-RU operations are restored with O-DU#2, reestablishing services to users with the CUS-Plane up and running.

NOTE 14: The recovery time is influenced by the deployment architecture (hierarchical and hybrid), as well as factors such as IP switchover, interface reconfiguration (e.g., O1, OFH, and F1), and failure detection mechanisms. Systems must consider these delays and optimize activation sequences to reduce downtime during failure events.

NOTE 15: The transition of the active role from O-DU#2 back to O-DU#1 involves the same steps as the initial transition from the O-DU#1 to O-DU#2, with the exception of which O-DU is to be activated. This activity is initiated based on a trigger from the SMO and/or the operator's decision.

The flow diagram of the resiliency use case is given in Figure 7.2.3-1.

@startuml   
!pragma teoz true   
skin rose   
skinparam ParticipantPadding 5   
skinparam BoxPadding 10   
skinparam defaultFontSize 14   
Box "Operator" #Lightblue Actor operator as "Operations Actor"   
End box   
Box “Service Management and Orchestration” #gold Participant SMO_a as "SMO\n(non-RT RIC)" end box   
Box “O-RAN Network Functions” #lightpink Participant OCU as "O-CU-CP" Participant ODU1 as “O-DU#1” Participant ODU2 as "O-DU#2" Participant ORU as "O-RU"

End box

Note over operator, ODU2 <B>PRECONDITIONS:</B> 1. O1 between SMO and O-CU-CP is up and running 2. O1 supervision is running between SMO and O-DU#1 3. O1 supervision is running between SMO and O-DU#2 4. SMO subscribed for O1 data to O-DU#1 and O-DU#2 if connected via O1 interface.   
End Note   
$= =$ BEGIN O-DU RESILIENCY USE CASE $= =$   
$= =$ O-DU#1 (PARTIAL/COMPLETE) FAILURE DETECTION $= =$ Alt Partial failure or performance degradation   
SMO_a $< - >$ ODU1 : [1] <<O1>> Service degradation due to O-DU#1 failure detected Else Complete O-DU failure or O1 interface failure   
SMO_a $< - >$ ODU1 : [2] $< < 0 1 > >$ Link between SMO and O-DU#1 has failed   
End alt   
Note over SMO_a, ODU2   
[3] SMO decides to move services to O-DU#2   
End note   
$= =$ CELL(S) AND ASSOCIATED CARRIERS DEACTIVATION AND OPTIONALLY REMOVE $= =$   
loop For each cell that requires deactivation   
alt Partially failed O-DU and is reachable to SMO via O1 interface   
par   
SMO_a $< - >$ ODU1 : [4a] $< < 0 1 > >$ Lock the cell(s) and remove resources   
note over OCU, ODU1   
$< < \mathrm { E } 1 > >$ Cell deactivation or removal   
End note   
ODU1 $<$ ->ORU : [4b] <<OFH>> Deactivate [tr]x-array-carriers and optionally remove them End par   
ODU1 $- >$ SMO_a : [4c] <<O1>> Cell state change notification   
else Completely failed O-DU and not reachable to SMO via O1 interface   
SMO_a $< - >$ OCU : [5] $< < 0 1 > >$ Terminate the F1 interface with O-DU#1   
end alt   
end loop   
$= =$ O-DU#2 RECOVERS THE O-RU OPERATIONS AND USER SERVICES $= =$   
loop For each cell that requires creation and activation on O-DU#2   
par   
SMO_a $- >$ ODU2 : [6] $< < 0 1 > >$ TNL configuration to O-DU#2 (Take active role)   
note over OCU, ODU2: Enabler for F1 establishment   
ODU2 <- ODU2 : [7] Standby O-DU#2 becomes\n the active O-DU   
else   
SMO_a <-> OCU : [8] $< < 0 1 > >$ Creation and configuration of cell   
else   
opt   
SMO_a<->ODU2 : [9] <<O1>> Cell and carrier(s) configuration to O-DU#2   
note over OCU, ODU2 : F1 messaging (if F1 is established, for cell to be reported by ODU#2 to O-CU-CP)   
ODU2 <-> ORU : [10] <<OFH>> Configuration of [tr]x-array-carriers   
end opt   
end par   
... \*\*Wait until: All above steps are completed successfully\*\* ..   
SMO_a <- OCU : [11] $< < 0 1 > >$ Cell(s) activated   
SMO_a <- ODU2 : [12] <<O1>> Cell and corresponding carrier(s) activated   
end loop   
Note over ORU, ODU2   
O-DU is now active and ready for services.   
O-RU is operational again, connected, in service   
(M-Plane, CUS-Plane is up and running.   
end Note   
SMO_a<->ODU2: [13] <<O1>> Subscription to performance counters from O-DU#2 note over SMO_a, ODU2   
Active role transition from O-DU#2 to O-DU#1 involves same steps as transitioned from O-DU#1 to O-DU#2, except which O-DU to be activated. This activity is based on trigger from SMO and/or operator’s decision.   
end note   
$= =$ END O-DU RESILIENCY USE CASE $= =$   
@enduml

![](images/ff0136ea0d2609ddebe7b81c5e806977b35ba02e9e09fd39a333e88789a5b8da.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.2.3-1: Enhanced network resiliency with SMO-managed standby O-DU

# 7.3 Solution 2: Enhanced network resiliency through the standby OCU-CP and service restoration managed by the SMO

# 7.3.1 Basic objective

This solution outlines the system behaviour for ensuring resiliency in O-CU-CP failure recovery within O-RAN networks. It addresses complete loss of management or partial failures causing service interruptions while the O1 interface remains active. The framework enables operators to detect failures and restore services through appropriate recovery actions. The focus is on maintaining network resiliency and minimizing disruptions, while root cause analysis is outside the solution's scope.

The objective is to provide an effective approach for operators to manage and recover from failures, ensuring robust network operations.

# 7.3.2 Roles of involved entities

The description below outlines the actors involved:

1) SMO

a. SMO assigns initial roles to O-CU-CPs (active, standby) or resiliency pairs based on operator decisions.   
b. It facilitates high-level decision-making during failures and resiliency scenarios, including managing O-CU-CP during partial or complete failures, interface disruptions, and planned maintenance.   
c. SMO enables service recovery by transitioning operations from the active O-CU-CP to a standby OCU-CP, minimizing service disruption for end users.

2) O-CU-CPs

a. O-CU-CP receives cell-related configurations from the SMO and cell availability details from the ODU(s). Based on the resource availability reported by the O-DU and the desired cell availability specified by the SMO, the O-CU-CP manages the activation or deactivation of cells in the O-DU via the F1 interface.   
b. O-CU-CP periodically reports the alarms and performance measurement counters to SMO via O1 interface.   
c. Active and standby O-CU-CPs are essential for resiliency, allowing the SMO to configure the standby to restore services after failure. This transition activates the affected cells, ensuring minimal service disruption for users.

3) O-DU

All O-DUs connected to the O-CU-CP are vital for recovery operations during resiliency scenarios. If the O1 interface remains operational, the SMO can analyse OAM data to identify O-CU-CP failures and reconfigure ODUs to migrate services to the standby O-CU-CP, minimizing disruption.

4) O-RU

The O-RU enables the operation of [tr]x-array carriers linked to the cells managed by the O-DU in conjunction with the O-CU-CP. Additionally, the O-RU plays a crucial role in maintaining the fronthaul and air interfaces, working in coordination with the O-DU to support the recovery of the cells managed by the O-CU-CP.

# 7.3.3 Solution description

The solution for the O-CU-CP resiliency use case is to recover the cell(s) served by the associated O-DUs and O-RUs, which is detailed in Table 7.3.3-1.

Table 7.3.3-1: Enhanced network resiliency with SMO-managed standby O-CU-CP   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;Uses&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The goal of this sub use case solution is for the SMO to manage O-CU-CP failure and to restore services to the best possible level.This is a service impacting use case.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">SMO:The SMO is responsible for configuring the active and standby rolesfor O-CU-CPs, as well as orchestrating recovery processes in theevent of an O-CU-CP failure. It makes high-level decisions forscenarios outlined in Clause 7.x, including failure management,resiliency handling, and service continuity.O-CU-CP:O-CU-CP receives cell(s) related configurations from the SMO andcell(s) resources availability information from O-DU(s). Based onthe resource availability reported by the O-DU and the desired cellavailability specified by the SMO, the O-CU-CP manages theactivation or deactivation of cells in the O-DU via the F1 interface.O-DUs (Active/Standby O-DUs):All the O-DUs connected to the O-CU-CP are responsible formanaging cell(s) resources, where these resources are configuredby the SMO via O1 interface, as needed. Additionally, the O-DU isresponsible for configuring [tr]x-array-carrier(s) in the O-RU.Furthermore, the O-DU can support the SMO in getting the O-CU-CP status through FM and PM data via O1 interface.O-RU:The O-RU handles the fronthaul and air interfaces and the reportingof performance counters and failures.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">It is assumed that in the event of an active O-CU-CP failure, at least onestandby O-CU-CP will be available to ensure service recovery for users.The resiliency mechanisms are designed to take over the operation ofthe cell(s) associated with the connected O-DUs, restoring services toend users with minimal disruption.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The O-CU-CP Resiliency use case can be triggered by various scenarios,as outlined in Clause 7.x. These scenarios include complete or partialfailures of an O-CU-CP, performance degradation, and other criticalissues. The primary goal of this use case is to ensure the continuedoperational integrity of the O-RU and O-DU system, even in the event ofan active O-CU-CP failure or disruptions such as interface failures (e.g.,F1, E2, and O1).This use case is activated when the Primary O-CU-CP experiences anyof above conditions, leading to its Operational State being set tó"disabled".</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Preconditions</td><td colspan="1" rowspan="1">1)  O-CU-CP#1 is configured to take active role with up and runningO1 towards SMO.2)  F1 interface between O-CU-CP#1 and O-DU is established.$\  O-CU-CP#2 is configured to take standby role with up andrunning O1 towards SMO or not configured at all.See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">BEGIN O-CU-CP RESILIENCY USE CASEO-CU-CP RESILIENCY USE CASE – O-CU-CP#1 FAILURE (COMPLETE/PARTIAL)</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">The SMO analyses alarms and performance management data to detectand identify the failure of O-CU-CP#1.</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">SMO decides to switch services from O-CU-CP#1 to O-CU-CP#2 upondetecting a partial failure in O-CU-CP#1. For example, SMO detectspartial O-CU-CP#1 failure based on alarms and/or PM counters that canreceive through the O1 interface from O-CU-CP#1.See NOTE 2.</td><td colspan="1" rowspan="1">WG10.O1 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">CE</td><td colspan="1" rowspan="1">CELL REMOVAL FOR EACH O-DU COOPERATING WITH AFFECTED O-CU-CP#1FOR EACH CELL THAT REQUIRES REMOVAL ON PARTICULAR O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">The SMO requests O-DU to deactivate and optionally remove the cell(s)associated with O-CU-CP#1 via O1 interface and to release thecorresponding resources respectively.See NOTE 3.</td><td colspan="1" rowspan="1">WG10.O1 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">The O-DU deactivates the [tr]x-array-carrier(s) associated with thecell(s) managed by O-CU-CP#1 in Step 3. The process fordeactivating the [tr]x-array-carrier(s) is illustrated in Figure 15.3.2-0bof O-RAN.WG4.MP specification.The O-DU receives notifications regarding the outcome of thedeactivation operation.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [i.7],Clause 15.3.</td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">For the cell(s) configurations requested in Step 3, O-DU sends anotification to the SMO via the O1 interface, indicating whether therequest(s) were successfully fulfiled, partilly fulfiled, or failed.See NOTE 4.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">CELL CRRAT</td><td colspan="1" rowspan="1">CELL CREATION AND ACTIVATION FOR EACH O-DU INTENDED TO COOPERATE WITH O-CU-CUP#2FOR EACH CELL THAT REQUIRES CREATION AND ACTIVATION ON PARTICULAR O-DU</td><td colspan="1" rowspan="1">VLARO--U-CUP#2</td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-DU to connect with O-CU-CP#2,providing necessary details such as transport parameters,connection requirements, and configurations for performancemanagement.The O-DU informs the results of the above operations to the SMOthrough the O1 interface.See NOTE 5.</td><td colspan="1" rowspan="1">WG10.O1 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">The SMO configures O-CU-CP#2 to get it into service path.SMO creates and configures the cell(s) to O-CU-CP#2 through theO1 interface. O-CU-CP#2 is provided with necessary configurationincluding transport details, cell(s) configuration, configurationneeded to connect with O-DU, configuration for PerformanceManagement and so on.The O-CU-CP#2 informs the results of the above operations to theSMO through the O1 interface.</td><td colspan="1" rowspan="1">WG10.01 interface[1.8]</td></tr><tr><td colspan="1" rowspan="1">Step 8 (M/O)</td><td colspan="1" rowspan="1">The SMO creates cell(s) objects if neededThe SMO manages the setup of cell(s) and corresponding carrier(s)resources in O-DU, which are associated with the respective cell(s)managed by O-CU-CP#2 as part of Step 5.The O-DU informs the results of the above operations to the SMOthrough the O1 interface.See NOTE 6, NOTE 7.</td><td colspan="1" rowspan="1">WG10.O1 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">The O-DU configures and activates the [tr]x-array-carrier(s) on the O-RU in accordance with the activation sequence depicted in Figure 15.3.2-0aof the O-RAN.WG4.MP.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [i.7],Clause 15.3.</td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">The SMO sends an activation request for the cell(s) configuredsuccessfully in Steps 7 and 8 to O-CU-CP#2.The O-CU-CP#2 confirms the reception of activation request fromSMO through the O1 interface.See NOTE 8.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">For the cell(s) activation request in Step 7, O-CU-CP#2 notifies the SMOon their activation status via the O1 interface. The standby O-CU-CP i.e.,O-CU-CP#2 is ready to offer services.</td><td colspan="1" rowspan="1">WG10.O1 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">The SMO subscribes and collects the alarms and performance countersfrom O-CU-CP#2 via the O1 interface.See NOTE 9.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Use Case ends when the standby O-CU-CP, O-CU-CP#2 shown inthe flow diagram has taken over for the previously active O-CU-CP, O-CU-CP#1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many exceptions. Some of these include:If the Standby O-CU-CP#2 fails during switch over or becomesunavailable when it is due to become active.If any event messaging for the flow is lost If configuration was not done properlyIf the Standby O-CU-CP losses the configuration data from theconfiguration replica.If the active O-CU-CP returns to service while the Standby O-CU-CP istrying to become the active O-CU-CP.If the connectivity, or functionality of the management system (SMO)becomes unavailable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">Post Conditions</td><td colspan="1" rowspan="1">SUCCESSFUL POST-CONDITION– On a successful post-condition, theO-DU is connected to the newly active O-CU-CP, the newly active O-CU-CP is operational and has properly connected and synchronised with theO-DU.FAILURE POST-CONDITION – If one of the various exception casesoccurs, there are a variety of failure post conditions. If no O-CU-CPs areavailable and the O-DU is disconnected, service will be unavailable, and</td><td colspan="1" rowspan="2"></td></tr><tr><td colspan="1" rowspan="1">the O-DU could shut down operations. If misconfiguration occurs the O-DU will respond accordingly. If there are ever two active O-CU-CPs, theO-DU will operate accordingly.</td></tr></table>

NOTE 1: O-CU-CP#2 is not present if is deployed as VNF.

NOTE 2: There might be multiple other O-DUs, but only one active O-DU. The management system, SMO, shall know, coordinate, and ensure that there is only one active O-DU.

NOTE 3: Cell deactivation/removal between O-CU-CP#1 and O-DU via F1 interface, where the O-DU informs the O-CU-CP#1 about the released resources through the same interface [i.4]. Related communications involved over F1 interface is not the subject of this TR.

NOTE 4: This use case defines only the steps if Step 3 is successfully accomplished.

NOTE 5: SMO provides TNL configuration to O-DU, which is the enabler for the F1 establishment.

NOTE 6: F1 setup procedure done after O-DU configured by SMO. If F1is established, and cells and their corresponding carriers are configured and available for service, the O-DU informs the O-CU-CP#2 about cell(s) availability using the F1 interface [i.4]. Related communications involved over F1 interface is not the subject of this TR.

NOTE 7: O-DU configures cell(s) and associated carrier(s) and then activates the [tr]x-array-carrier(s) in the ORU via the Fronthaul M-plane [i.7].

NOTE 8: O-CU-CP#2 utilizes F1 to get the information from the O-DU about cell(s) availability for activation. O-CU-CP#2 triggers the activation of these cell(s) (NRCGI(s)) on the O-DU as soon as the corresponding resources become available, which then activates corresponding carrier(s) on the O-RU. The O-DU communicates the activation status back to the O-CU using the F1 interface. Once activated, the O-RU becomes operational with O-DU#1, with the cell on air and ready to serve UEs [i.4]. Related communications involved over F1 interface is not the subject of this TR.

NOTE 9: The transition of the active role from O-CU-CP#2 back to O-CU-CP#1 involves the same steps as the initial transition from the O-CU-CP#1 to O-CU-CP#2, except for which O-CU-CP is to be activated. This activity is initiated based on a trigger from the SMO and/or the operator's decision.

The flow diagram of the O-CU-CP resiliency use case is given in Figure 7.3.3-1.

![](images/d8d55216d5ba068f16c7061174b6305cd857161fc6ab6854f8efb012b2437625.jpg)

> **Image Summary:** (Summary not available)


loop Cell removal, for each O-DU cooperating with affected O-CU-CP#1

smo->odu : <<O1>> Deactivate and optionally remove associated cell   
Note over ocu1, odu   
$< < \mathrm { E } 1 > >$ Cell deactivation / removal between O-CU-CP#1 and O-DU   
End note   
odu<->oru : <<FH MPlane>> [tr]x-array-carrier(s) deactivation   
odu->smo : $< < 0 1 > >$ Result notification   
End loop   
End loop   
End group   
loop Cell creation and activation for each O-DU intended to cooperate with O-CU-CP#2 loop for each cell that requires creation and activation on particular O-DU   
par   
smo<->odu : <<O1>> TNL configuration to O-DU   
note over odu, ocu2: Enabler for F1 establishment   
else   
smo<->ocu2 : <<O1>> Creation and configuration of cell(s) to O-CU-CP#2   
else   
opt   
smo<->odu : <<O1>> Cell and carrier(s) configuration to O-DU   
end opt   
note over odu, ocu2: F1 messaging (if F1 is established)   
odu<->oru : <<FH MPlane>> [tr]x-array-carrier(s) configuration and activation   
else   
smo<->ocu2: <<O1>> Cell activation   
note over odu, ocu2: F1 messaging (if F1 is established, for cell \nreported by O-DU to O-CU-CP in step 6)   
end par   
... \*\*Wait until: All above steps are completed successfully\*\* ...   
smo <- ocu2 : $< < 0 1 > >$ Cell activated   
note over ocu2, oru   
The cell(s) associated with O-CU-CP#2 and corresponding   
carrier(s) are fully operational and ready to deliver services   
End note   
smo<->ocu2: <<O1>> SMO collects alarms and performance counters from O-CU-CP#2   
end loop

end loop

Note over smo, ocu2   
Active role transition from O-CU-CP#2 to O-CU-CP#1 involves same steps transitioned from O-CU-CP#1 to O-CU-CP#2, except whichever O-CU-CP to be configured and activated. This activity is based on trigger from SMO and/or operator’s decision.   
end note

$= =$ END O-CU-CP RESILIENCY USE CASE $= =$

![](images/fe747c2190ae0845697263d28781e6a2b0dc0f07c77b0db0aebe793d866aa8b2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.3.3-1: Enhanced network resiliency with SMO-managed standby O-CU-CP

# 7.4 Solution 3: Enhanced network resiliency through O-RU rehoming, leveraging the SMO framework's transport resiliency management capabilities.

# 7.4.1 Basic objective

This solution describes how the SMO framework monitors FM and PM datas from transport networks and various network functions (O-RU, O-DU, O-CU-CP, O-CU-UP) to detect failures and facilitate the rehoming of O-RUs from failed ODUs to operational ones. The rehoming process involves reconnecting O-RUs with the operational O-DU through either pre-configured transport paths or those configured by the transport network manager, based on policies provided by the SMO. Once alternate transport paths are established, O-RUs connect to the new O-DU via M-plane. SMO configures the necessary transport and cell/carrier resources to restore services.

O-RU rehoming can be initiated proactively, based on failure predictions, performance degradation detection, planned maintenance (e.g., O-DU software updates), or resource utilization status (for load balancing or capacity optimization). Alternatively, it can be triggered reactively in response to failures or unexpected events such as disasters. The process is part of SMO-driven automation to minimize service impact during maintenance or network disruptions.

In case of scenario based on resource utilization, if network function resources (e.g., CPU, memory, I/O) fall below a defined threshold (e.g., $20 \%$ ), SMO identifies underutilized O-DUs. For example, during non-peak hours (e.g., $2 4 { : } 0 0 -$ 05:00) in locations like shopping malls or stadiums, aggregated O-RUs connected to specific O-DUs may experience low utilization. SMO evaluates the target O-DU's capacity to ensure it can accommodate additional O-RUs before rehoming. This enables the shutdown of underutilized O-DUs, saving energy, especially in cloud-native deployments.

O-RU rehoming can be utilized during planned maintenance, such as O-DU software upgrades, by redirecting O-RUs to another O-DU.

The transport path resiliency ensures minimal service disruption during maintenance or unexpected failures that occur with O-DU(s). Overall, the SMO orchestrates these processes to improve network resiliency as shown in Figure 7.4.1-1.

![](images/cc250a6f09f7e623f927a0fa3ffa2e564d53de647ad0ed0fdd32c77e7f6a5e21.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.4.1-1: SMO managed transport to support O-RU rehoming and network resiliency

# 7.4.2 Roles of involved entities

The description below outlines the actors involved:

1) SMO:

a. SMO plays a crucial role by managing the transport network manager and providing the necessary policies for transport path configuration, thereby enabling O-RU rehoming. SMO orchestrates the entire O-RU rehoming use case by monitoring PM/FM data, managing transport paths, and coordinating network functions based on the scenarios mentioned in Clause 7.4.1.   
b. It facilitates high-level decision-making during failures and resiliency scenarios, including managing O-DUs during partial failures, interface disruptions, and planned maintenance.   
c. SMO enables service recovery through transitioning operations by rehoming the O-RUs from one ODU to another O-DU (i.e., active to standby), minimizing service disruption for end users.

2) Transport network manager (TN manager):

a. The transport network manager acts as a key enabler, assisting the SMO in orchestrating transport path changes and ensuring transport path reconfiguration to facilitate the O-RU rehoming.   
b. SMO can manage the transport network manager and provide policies/configurations for an appropriate transport path configuration to facilitate O-RU rehoming.

3) O-CU-CP:

O-CU receives cell related configurations from SMO and available cell details from O-DU(s). Based on the available resources reported by O-DU and desired availability of cells received from SMO, the O-CU activates or deactivates the cells in the O-DU using F1 interface.

4) O-DUs (Active/Standby O-DUs):

a. The O-DU plays a significant role in O-RU rehoming.   
b. The active O-DU (O-DU#1) serves as the primary unit, manages the cell resources, handling essential lifecycle management and FCAPS functions of the associated O-RUs. It also manages the HDLC stack for AISG communication with Antenna Line Devices (ALDs) connected to the O-RU.   
c. To ensure resiliency during O-RU rehoming or failure scenarios, a standby O-DU (O-DU#2) is available to take over the services and O-RU operations from the active O-DU (O-DU#1). The standby O-DU can be pre-configured or configured dynamically by the SMO. This takeover occurs in situations such as partial failure of O-DU#1, underutilization of O-DU#1, planned maintenance, or displacement scenarios.

5) O-RU:

The O-RU allows for (among others) the operation of [tr]x-array carriers associated with the cell(s) managed by the O-DU. The O-RU plays a crucial role in maintaining the fronthaul and air interfaces, working in coordination with the O-DU to support the recovery of the cells managed by the O-DU.

# 7.4.3 Solution description

The solution describes the O-RU rehoming. This solution leverages transport resiliency to recover user services and ORU operations, which is detailed in Table 7.4.3-1.

Table 7.4.3-1: Transport configuration managed by SMO for network resiliency through O-RU rehoming   
BEGIN O-RU REHOMING USE CASE   

<table><tr><td>Use Case Stage</td><td colspan="2">Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>The goal of this solution is for the SMO to manage the O-RU rehoming by leveraging its transport resiliency management capabilities, this is to restore services to the best possible level. This is a service impacting use case.</td><td></td><td></td></tr><tr><td>Actors and Roles</td><td colspan="2">SMO: The SMO enhances network resiliency by collecting FM/PM data to detect or predict failures and then re-homes O-RUs between O- DUs. This process is facilitated by the SMO&#x27;s management of the transport network and its associated policies. Transport network manager (TN manager): The transport network manager uses SMO policies/configurations to manage transport paths, facilitating O-RU rehoming and enhancing network resiliency. O-CU-CP: O-CU-CP receives cell(s) related configurations from the SMO and cell(s) resources availability information from O-DU(s). Based on the resource availability reported by the O-DU and the desired cell availability specified by the SMO, the O-CU-CP manages the activation or deactivation of cells in the O-DU via the F1 interface. O-DUs (active/standby O-DUs): O-DUs are responsible for managing cell(s) resources, where these resources are configured by the SMO via O1 interface, as needed. The O-DU is also responsible for managing the O-RU operations, for e.g., configuring [tr]x-array-carriers. Furthermore, the O-DU can support the SMO O-RU rehoming during the scenarios described in Clauses 7.4.1 and 7.4.2. O-RU:</td><td></td></tr><tr><td>Assumptions</td><td>network manager.</td><td>reporting of performance counters and failures. To ensure service continuity during active O-DU failures or proactive maintenance, it is assumed that at least one O-DU remains available for O-RUs to re-home to. It is assumed that the SMO have the capability to manage the transport network manager for the transport path configuration. SMO subscribed for CM, FM, and PM datas from NFs and transport A partial failure of the active O-DU (i.e., O-DU#1) occurs. Performance degradation is detected in the active O-DU.</td><td></td></tr><tr><td>Begins when</td><td>1) 2)</td><td>Planned maintenance or displacement of the active O-DU. Underutilization of the active O-DU. Energy saving measures require a O-RU rehoming. Other critical issues necessitate O-RU rehoming. Transport network manager is part of the SMO framework. SMO is aware of the O-DU (i.e., O-DU#2) to which the O-RUs Data reporting to SMO: Network functions (O-RU, O-DU, and</td><td></td></tr><tr><td>Preconditions</td><td>to be rehomed. 3) 4) details. 5)</td><td>O-CU-CP) report Performance Measurement (PM) data (e.g., counters)&#x27;and Fault Management (FM) data (e.g., alarms, notifications) to the SMO via the O1 interface. SMO has the transport network and network topology related SMO has an active O1 session with both O-DU#1 and O- DU#2, if O-DU#2 is configured as standby O-DU. BEGIN O-RUREHOMING U</td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>SMO analyses CM, FM, and PM data from NFs (O-CU/O-DU/O-RU) and transport network to assess network `conditions andidentify the need for rehoming.SMO analyses the above reported data to assess the resourceutilization status of NF i.e., O-DU#1.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>The SMO evaluates O-DU#2&#x27;s available resources before triggering O-RU rehoming. This ensures O-DU#2 can handle the increased load dueto the rehomed O-RUs.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>SMO decides to rehome the O-RU(s) from O-DU#1 to O-DU#2 basedon the trigger scenarios mentioned in both Clause 7.4.1 and “BeginsWhen&quot; of this table.See NOTE 1.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Step 4 (0)</td><td rowspan=1 colspan=1>The SMO, using the information from Steps 1-3 and based on operator&#x27;srequirements, generates the O-RU rehoming policy and configurationdetails for TN manager.See NOTE 2.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Step 5 (0)</td><td rowspan=1 colspan=1>●  SMO initiates rehoming in coordination with the Transport NetworkManager.The SMO provides the O-RU rehoming policy and/or configurationdetails to the TN manager, to enable transport path reconfiguration.The SMO can leverage its policy, performance management, andconfiguration management services to execute this process.See NOTE 3.</td><td rowspan=1 colspan=1>O-RAN.WG9.XTRP-MGT.0 [i.26],Annex C and Annex E;</td></tr></table>

# CELL(S) DEACTIVATION AND REMOVAL FOR EACH REHOMING O-RU COOPERATING WITH O-DU#1FOR EACH CELL THAT REQUIRES DEACTIVATION AND/OR REMOVAL

<table><tr><td rowspan=1 colspan=1>Step 6 (M)</td><td rowspan=1 colspan=1>The SMO uses O1 interface to request O-DU#1 to lock the cell(s)and remove corresponding resources.The O-DU informs the results of the above operations to the SMOthrough the O1 interface.See NOTE 4, NOTE 5.</td><td rowspan=1 colspan=1>WG10.O1 interface[i.8]</td></tr><tr><td rowspan=1 colspan=1>Step 7 (0)</td><td rowspan=1 colspan=1>O-DU uses the fronthaul M-plane to deactivate and remove the [tr]x-array-carriers associated with the cell(s) resources that are locked andremoved in Step 6.</td><td rowspan=1 colspan=1>WG4.FH M-Plane [i.7],Clauses 15.3.2 and9.1.6</td></tr><tr><td rowspan=1 colspan=1>Step 8 (M)</td><td rowspan=1 colspan=1>The O-DU#1 notifies the SMO about the status change for cell(s)indicated in Step 6.See NOTE 4.</td><td rowspan=1 colspan=1>WG10.O1 interface[i.8]</td></tr><tr><td rowspan=1 colspan=1>Step 9 (0)</td><td rowspan=1 colspan=1>●  Prior to O-RU rehoming, the SMO interacts with the TransportNetwork Manager via APls to migrate to transport paths. Thisinvolves terminating the existing transport path between O-RUs andthe source O-DU i.e., O-DU#1.SMO triggers the above API call if it did not provide thepolicy/configuration details to the TN manager in Step 5.See NOTE 6.</td><td rowspan=1 colspan=1>O-RAN.WG9.XTRP-MGT.0 [i.26],Annex C and Annex E;ORAN-WG9.XPSAAS.0 [i.27],Clause 13;Use Case.</td></tr></table>

<table><tr><td colspan="3" rowspan="1">CELL(S) AND CORRESPONDING RESOURCES CONFIGURATION AND ACTIVATION FOR EACH O-RUCOOPERATNG WITH O-DU#2</td></tr><tr><td colspan="2" rowspan="1">FOR EACH CELL THAT REQUIRES CONFIGURATION AND ACTIVATION</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">If the SMO did not provide policy/configuration details to the TN manager in Step 5, it will send a trigger to the TN manager, including transportdetails, to generate alternate transport paths for rehoming O-RUs to theO-DU#2.See NOTE 7.</td><td colspan="1" rowspan="1">O-RAN.WG9.XTRP-MGT.0 [i.26],Annex C and Annex E;ORAN-WG9.XPSAAS.0 [i.27],Clause 13;Use Case.</td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">SMO creates and configures the cell(s) associated with O-DU#2 onO-CU-CP through the O1 interface.The O-CU-CP informs SMO about the results of above-mentionedoperations through the O1 interface.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8];Use Case</td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">configured to O-CU-CP in Step 6.The SMO provides O-DU#2 with mapping between carrier(s)resources and cell(s) resources.The O-DU#2 informs the results of the above operations to the SMOthrough the O1 interface.See NOTE 8, NOTE 9, NOTE 10.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8];Use Case.</td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">For the cell(s) successfully activated in result of Step 11, the O-CU-CPnotifies the SMO on their activation status via the O1 interface.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8];Use Case.</td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">The O-DU configures and activates the [tr]x-array-carrier(s) on the O-RU in accordance with the activation sequence depicted in Figure15.3.2-0a of the O-RAN.WG4.MP specification.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [i.7],Clause 15.3.</td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">●  O-DU#2 notifies the SMO on the cell(s) and correspondingcarrier(s) activation status via the O1 interface.O-DU#2 is operational and providing services, having integrated theO-RUs previously associated with O-DU#1.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8];Use Case.</td></tr><tr><td colspan="1" rowspan="1">Step 16 (0)</td><td colspan="1" rowspan="1">Once the services are rehomed from O-DU#1 to O-DU#2, the O-DU#1 can be shut down or decommissioned to achieve powersavings.A shutdown procedure for O-DU#1 is initiated in cases of energysaving requirements, planned maintenance, or displacementactivities.See NOTE 11.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8];Use Case.</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The use case ends upon completion of O-RU rehoming from O-DU#1 toO-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many exceptions. Some of these include:If the O-DU#2 fails during rehoming or becomes unavailable when it isdue to become active. If any event messaging for the flow is lost If configuration was not done properlyIf the O-DU#2 losses the configuration data from the configurationreplica.If the connectivity, or functionality of the management system (SMO)becomes unavailable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SUCCESSFUL POST-CONDITION – On a successful post-condition,the O-RU(s) are connected to the newly active O-DU i.e., O-DU#2, theO-RU(s) are operational and has properly connected and synchronisedwith the O-DU#2.FAILURE POST-CONDITION – If one of the various exception casesoccurs, there are a variety of failure post conditions. If no O-DUs areavailable and the O-RU(s) are disconnected, service will be unavailable,and the O-RU could perform autonomous reset. If misconfigurationoccurs the O-RU(s) will respond accordingly.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1. The loqic applied by the SMO in this decision process is not subiect of this Technical Report</td></tr></table>

NOTE 2: The logic applied by the SMO in generating policies or configuration details is not the subject of this Technical Report.

NOTE 3: The SMO delivers TN manager with O-RU rehoming policies and/or configuration details. Which interface it use to deliver the policies and/or configuration details is not the subject of this Technical Report. This is accomplished using either the O1 interface, the O2 interface, or a newly defined interface. The determination of which interface is used for this purpose is beyond the scope of this Technical Report.

NOTE 4: The process of cell deactivation/removal between O-CU-CP and O-DU#1 utilizes F1 interface.   
Related communication over F1 interface is not the subject of this Technical Report.

NOTE 5: SMO's logic employed to decide if cell will be locked or removed is not subject of this Technical Report.

NOTE 6: TN manager tears down the connection between aggregated O-RUs and O-DU#1 for rehoming them to O-DU#2. The specific logic used by the TN manager to perform this disconnection is not the subject of this Technical Report.

NOTE 7: TN manager generates alternate transport paths for O-RUs associated with the impacted O-DU (i.e., O-DU#1) to enable rehoming to a new O-DU (i.e., O-DU#2). The specific logic used by the TN manager to perform this transport generation is not the subject of this Technical Report.

NOTE 8: If F1 is established, the O-DU#2 informs the O-CU-CP about cell(s) availability using the F1 interface. Related communications over F1 interface are not the subject of this TR.

NOTE 9: In hierarchical deployment in this step SMO also provides O-DU with configuration for O-RUs served by this O-DU.

NOTE 10: F1 interface is used to exchange information needed for cell activation between O-CU-CP and O-DU.

NOTE 11: If services are to be switched back to O-DU#1, steps 1-16 can be repeated as appropriate.

The flow diagram of the SMO managed the transport resiliency solution for O-RU rehoming is given in Figure 7.4.3-1.

@startuml !pragma teoz true skin rose skinparam ParticipantPadding 5 skinparam BoxPadding 10 skinparam defaultFontSize 14 skinparam sequenceMessageAlign center autonumber Box "Personnel\nPower saving Host" #Lightblue Actor operator as "Operations Actor" End box Box “Service Management and Orchestration\n(non RT RIC)” #gold Participant SMO_a as "SMO\n(non-RT RIC)" End box Box “Transport Network” #gold Participant TNM as "TN_Manager” End box Box “O-RAN Network Funtion” #lightpink Participant OCU as "O-CU-CP" Participant ODU1 as “O-DU\n(#1)” participant ORU as "O-RU1..n" Participant ODU2 as "O-DU\n(#2)" End box Note over operator, ODU2 <B>PRECONDITIONS:</B>   
1) Transport network manager is part of the SMO framework.   
2) SMO is aware of the O-DU to which the O-RUs to be rehomed.   
3) SMO subscribed to receive FM, PM, and CM datas from NFs and TN Manager.   
4) SMO has the transport network and network topology related details.   
5) SMO has active O1 session with O-DU#1 and O-DU#2. End note $= =$ Begin O-RU rehoming use case $= =$   
Group SMO as MnS Consumer consume FM, PM, and CM data and makes decision   
SMO_a->SMO_a: Analyse the FCAPS data \nrelated to O-DU#1   
SMO_a->SMO_a: Analyse the O-DU#2 resource availability   
SMO_a->SMO_a: Decides to rehome the O-RU(s) from \nO-DU#1 to O-DU#2 (Assuming O-DU#2   
\nhas sufficient resources)   
SMO_a->SMO_a: Prepare a O-RU rehoming policy/\nconfigurations for TN Manager   
opt   
SMO_a<->TNM: $< < \bigcirc 1$ /O2/new IF>> Provides a policy/configurations for \nalternate path   
generation to provision rehoming   
End opt   
End Group   
loop Rehoming - Cell(s) deactivation and removal of corresponding resources for each O-RU   
cooperatng with affected O-DU#1   
par   
SMO_a<->ODU1: $< < 0 1 > >$ Lock the Cell(s) and corresponding carrier(s) resources   
note over OCU, ODU1   
<<F1>> Cell deactivation or removal   
End note   
opt   
ODU1<->ORU: <<FH M-Plane>> [tr]x-array-carrier(s) \ndeactivation and removal   
end opt   
SMO_a<-ODU1: <<O1>> Cell(s) and corresponding carrier(s) resource status update   
notification   
End par   
opt   
SMO_a<->TNM: <<O1/O2/new IF>> Request for tearing down the \nconnections of O-RU with O  
DU#1   
End opt   
Note over TNM,ORU   
TN Manager tears down the connection between aggregated   
O-RUs and O-DU#1 for rehoming them to O-DU#2   
End Note   
End Loop   
Loop Rehoming - Cell(s) and corresponding resources configuration and activation for each   
O-RU cooperatng with O-DU#2   
opt   
SMO_a<->TNM: <<O1/O2/new IF>> Establish the transport \nconnections of O-RU with O-DU#2   
end opt   
Note over TNM,ODU2   
TN Manager establishes the connection between   
aggregated O-RUs and O-DU#2 for rehoming services   
End Note   
par   
SMO_a<->OCU: <<O1>> O-DU#2 associated Cell(s) configuration   
opt   
SMO_a<->ODU2: <<O1 $\mathord { \left. \mathrm { ‰} \right. } > >$ Cell(s) and corresponding carrier(s) resources configuration   
note over OCU, ODU2 : F1 messaging (if F1 is established, for \ncell to be reported by O  
DU#2 to O-CU-CP)   
end opt   
End par   
SMO_a<-OCU: $< < 0 1 > >$ Cell(s) status update notification   
ODU2<->ORU: <<FH M-Plane>> [tr]x-array-carrier(s) \nconfiguration and activation   
SMO_a<-ODU2: <<O1>> Cell(s) and corresponding carrier(s) resource status update   
notification   
End loop

note over ORU, ODU2 : Rehomed O-RU(s) become active \nand ready to offer services opt Energy Saving/Planned maintenance/Displacement SMO_a->ODU1: $< < 0 1 > >$ O-DU#1 shutdown End opt $= =$ End of O-RU rehoming use case $= =$

Note over SMO_a, ODU2   
If the services to be switched back to O-DU#1, the above steps can be repeated appropriately.

![](images/11aef812d8ce5f10c33f43976d8ad1452a6a90717bdc2f7fbc713da11b505aaf.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.4.3-1: Transport configuration managed by SMO for network resiliency through O-RU rehoming.

# 7.5 Solution 4: Enhanced network resiliency for NF Deployment(s) in O-Cloud managed by the SMO Framework

# 7.5.1 Basic objective

To address NF Deployment(s) failure in O-Cloud, this solution ensures rapid redeployment of the affected NF.

Once the SMO framework detects the failure through RAN OAM, FOCOM, and NFO, SMO coordinates with FOCOM and NFO for an automated recovery process, for e.g., instructing DMS to recreate the NF Deployment(s). This enables efficient, automated recovery, minimizing service disruption without manual intervention.

# 7.5.2 Roles of involved entities

The description below outlines the actors involved:

1) SMO

a. SMO facilitates high-level decision-making based on the operator’s policies or requirements during various failures and resiliency scenarios, which includes managing CNF deployment during partial or complete failures of O-Cloud infrastructure, NF Deployment(s), and application/instance, interface disruptions, and planned maintenance.   
b. SMO enables service recovery by transitioning operations from the failed NF to newly created NF, minimizing service disruption for end users.

2) O-Cloud

a. Provides virtualized infrastructure resources (compute, storage, networking) to host and manage ORAN Network Functions.   
b. Monitors infrastructure-level faults and resource usage, supporting automated self-healing or triggering SMO management actions.   
c. Maintains resiliency through redundancy and high availability mechanisms.   
d. Includes IMS, providing infrastructure resource management and fault/performance reporting, directly interfacing with FOCOM via the O2ims interface.   
e. Includes DMS, responsible for deployment and configuration of Network Functions, directly interfacing with NFO via the O2dms interface.

3) FOCOM

a. Integrates fault detection, configuration control, and performance monitoring of infrastructure.   
b. Provides visibility of fault, configuration, and performance data, generates alarms, and supports automated or manual recovery actions.   
c. Directly interfaces with IMS via the O2ims interface to ensure continuous and resilient infrastructure management.

4) IMS

a. Provides standardized interfaces between SMO and O-Cloud, ensuring uniform infrastructure management.   
b. Facilitates resource allocation, fault monitoring, performance data collection, and configuration tasks.   
c. Directly communicates infrastructure status, performance metrics, and faults to FOCOM via the O2ims interface.

5) NFO

a. Manages the lifecycle of Network Functions (NFs), including instantiation, scaling, healing, upgrading, and termination.   
b. Implement resiliency policies by orchestrating failover or redeployment upon detection of NF-level faults.   
c. Directly interfaces with DMS via the O2dms interface to manage NF deployments effectively.

6) DMS

a. Manages deployment and configuration of virtualized Network Functions onto O-Cloud resources. b. Ensures NF instantiation and resource allocation adhere to resiliency and performance requirements. c. Directly communicates NF Deployment(s) status and receives lifecycle instructions from NFO via the O2dms interface.

7) NF

a. Represents individual O-RAN elements (e.g., O-CU-CP, O-CU-UP, O-DU) providing specific network capabilities.   
b. Continuously reports operational status, performance data, and fault conditions via O1 and O2 interface for comprehensive management.

8) O-RU

The O-RU enables the operation of [tr]x-array carriers linked to the cells managed by the NF. The O-RU plays a crucial role in maintaining the fronthaul and air interfaces, working in coordination with the NF to support the recovery of the cells managed by the NF.

# 7.5.3 Solution description

The solution outlines how the SMO framework manages a quick automated recovery of a failed NF in O-Cloud deployment by coordinating with IMS and DMS to recover the NF from failures, thereby reducing service disruption without the need for manual intervention. The solution is detailed in Table 7.5.3-1.

Table 7.5.3-1: SMO managed NF resiliency in O-Cloud deployment   
BEGIN O-CLOUD NF FAILURE RECOVERY USE CASE   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>Related use</td></tr><tr><td>Goal</td><td>The goal of this solution is for the SMO to manage the NF failure in O- Cloud deployment to restore services to the best possible level. This is a service impacting use case. SMO:</td><td></td></tr><tr><td rowspan="8">Actors and Roles</td><td>The SMO is responsible for coordinating with RAN OAM, FOCOM, and NFO to manage NF failures and restore services. This is achieved by providing configuration and policies to IMS and DMS through FOCOM and NFO, respectively. O-Cloud:</td><td rowspan="9">O-RAN.WG6.TS.02- GA&amp;P.0 [i.6]; Use Case</td></tr><tr><td>The platform virtualizes resources for O-RAN network functions and monitors infrastructure health, enabling self-healing. It also includes IMS and DMS components for resource management, deployment,</td></tr><tr><td>and configuration, interfacing with FOCOM and NFO respectively. FOCOM: FOCOM integrates infrastructure monitoring, control, and recovery,</td></tr><tr><td>interfacing with IMS via O2ims for resilient management. IMS: IMS, via the O2ims interface, facilitate communication between SMO and O-Cloud, providing resource management, monitoring,</td></tr><tr><td>and fault reporting to FOCOM. NFO: The NFO manages the lifecycle, resiliency, and deployment of</td></tr><tr><td>Network Functions through the O2dms interface. DMS: DMS manages NF Deployment(s) and configuration on O-Cloud,</td></tr><tr><td>ensuring performance and communicating with NFO via O2dms. NF: O-RAN Network Functions provide network capabilities， support resiliency, and report status via the O1 and O2 interfaces. NF Deployment(s)#1 is impacted or Old NF Deployment/Deployments</td></tr><tr><td>(Whole NF instance) and NF Deployment(s)#2 is the New NF Deployment/Deployments (Whole NF instance). O-RU: The O-RU handles the fronthaul and air interfaces and the reporting of performance counters and failures.</td></tr><tr><td>To ensure service continuity, at least one Network Function is assumed to be created/deployed or already available as redundant NF Deployment(s) upon NiF Deployment(s)#1 failure.</td><td colspan="2"></td></tr><tr><td>Assumptions</td><td>The resiliency mechanisms are available to take over the operation of the cell(s) associated with the impacted NFs, restoring services to end users with minimal disruption.</td><td rowspan="3"></td></tr><tr><td>Begins when</td><td>SMO detects a NF Deployment/Deployments (Whole NF instance) failure in O-Cloud through RAN OAM, FOcOM, and NFO. 1) Cluster is provisioned and a NF Deployment(s) (Whole NF</td></tr><tr><td>2) Preconditions 3)</td><td>Instance) is running. SMO subscribed to alarms and performance counters from O- Cloud via O2ims and O2dms interfaces. SMO subscribed to alarms and performance counters from NF via O1 interface.</td></tr></table>

SMO DETECTS THE NF RELATED FAILURES FAILURE GRANULARITY – CLOUD INFRASTRUCTURE, CLOUD DEPLOYMENT, AND NF INSTANCE LEVEL   

<table><tr><td rowspan=1 colspan=1>Alt Step 1a (O)</td><td rowspan=1 colspan=1>The network function deployed in the O-Cloud can experience failuresarising from challenges associated with cloud-native network functiondeployment (NF Deployment(s) (Whole NF Instance)). For example, thedeployed application (Whole NF instance) might fail due to deploymentand onboarding related issues caused by various factors. However, theroot cause of such failures is not the subject of this TR.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Alt Step 1b (O)</td><td rowspan=1 colspan=1>The network function instance running in the O-Cloud environment canexperience failures arising from challenges associated with networkfunction application (Whole NF instance). For example, the deployedapplication (Whole NF instance) might fail due to various factors.However, the root cause of such failures is not the subject of this TR.</td><td rowspan=1 colspan=1>Use Case</td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>The SMO analyses CM, FM, and PM data from O-Cloud and networkfunction applications, collected via RAN OAM, FOCOM, and NFO usingO1/02 interfaces (IMS/DMS).</td><td rowspan=1 colspan=1>O-RAN.WG6.ORCH-USE-CASES,Clauses 3.7 and 3.8[i.28]</td></tr></table>

<table><tr><td>Alt Step 3 (M)</td><td>The SMO uses the O1 interface to detect a failure in the network function instance, if any.</td><td>O-RAN.WG6.TS.O2- GA&amp;P.0 [i.6]; Use Case</td></tr><tr><td>Step 4 (M)</td><td>The SMO uses the O2 interface (O2IMS/O2DMS) to detect issues in NF Deployment(s) and/or infrastructure resource problems in coordination with IMS and DMS.</td><td>O-RAN.WG6.TS.02- GA&amp;P.0 [i.6]; WG10.01 interface [i.8]; Use Case.</td></tr><tr><td rowspan="2">Step 5 (O)</td><td>The SMO uses the O1 interface to lock or deactivates, and/or removes the cell(s) and carrier(s) resources associated an impacted NF instance. Additionally, the O-DU can use the Fronthaul M-plane interface to</td><td rowspan="2">WG10.O1 interface [i.8] Use Case.</td></tr><tr><td>disable the [tr]x-array-carriers and, optionally, remove the [tr]x- array-carriers resources in O-RU. This process is only applicable if the impacted NF instance remains</td></tr><tr><td></td><td>accessible by the SMO via the O1 interface. See NOTE 2, NOTE 3.</td><td></td></tr></table>

# SMO COORDINATES WITH O-CLOUD AND NF INSTANCE FOR NF RECOVERY FROM FAILURES NF FAILURE RECOVERY – CLOUD INFRASTRUCTURE, CLOUD DEPLOYMENT, AND NF INSTANCE LEVEL

<table><tr><td colspan="1" rowspan="1">Alt Step 6a (M)</td><td colspan="1" rowspan="1">The SMO uses the O2 interface (O2IMS/O2DMS) to detect issues in NFDeployment(s) and/or infrastructure resource problems in coordinationwith iMS and DMS. The DMS recreates NF Deployment(s)#2 onalternative infrastructure resources.</td><td colspan="1" rowspan="1">O-RAN.WG6.ORCH-USE-CASES, Clause3.2.1 [i.28];Use Case</td></tr><tr><td colspan="1" rowspan="1">Alt Step 6b (M)</td><td colspan="1" rowspan="1">If the SMO detects the NF Deployment failure is not infrastructure-related, it instructs DMS via NFO to recreate NF Deployment(s)#2 on thesame infrastructure. The DMS recreates NF Deployment(s)#2 on thesame infrastructure.</td><td colspan="1" rowspan="1">O-RAN.WG6.ORCH-USE-CASES, Clause3.2.1 [i.28];Use Case</td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">The SMO can optionally configure NF Deployment(s)#2 with theappropriate cell(s) and associated carrier(s), and unlocks/activates themonce the resources are ready, using the O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">NF Deployment(s)#2 is now operational and ready to offer services.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">The SMO collects alarms and performance counters from the O-Cloudvia the O2ims and O2dms interfaces, and from NF instances via the O1interface, through subscription mechanisms.</td><td colspan="1" rowspan="1">WG10.01 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Use Case ends when the newly created NF recovers the userservices from impacted NF.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many exceptions. Some of these include: If the newly created NF fails during switch over or becomes unavailablewhen it is due to become active.</td><td colspan="1" rowspan="1"></td></tr><tr><td></td><td>If any event messaging for the flow is lost If configuration was not done properly If the NF Deployment(s)#2 loses the configuration data from the configuration replica. If the NF Deployment(s)#1 returns to service while the NF Deployment(s)#2 is trying to become active. If the connectivity, or functionality of the management system (SMO)</td><td></td></tr><tr><td>Post Conditions could take autonomous reset. If misconfiguration occurs the O-RU wil respond accordingly.</td><td>SUCCESSFUL POST-CONDITION – On a successful post-condition, the O-RUs are connected to the new NF i.e., NF Deployment(s)#2, it is operational and has properly connected and synchronised with the O- RU. FAlLURE POST-CONDITION – If one of the various exception cases occurs, there are a variety of failure post conditions. If no NFs are available or disconnected, service will be unavailable, and the O-RU</td><td></td></tr></table>

NOTE 2: The process of cell deactivation/removal between O-CU-CP and O-DU#1 utilizes F1 interface. Related communication over F1 interface is not the subject of this TR.

NOTE 3: SMO's logic employed to decide if cell will be locked or removed is not subject of this TR.

NOTE 4: The specific interactions between the SMO and IMS, the utilization FOCOM services within the SMO framework for O-Cloud infrastructure failure recovery, or the detailed methods employed for the NF recovery is not the subject of this TR.

NOTE 5: The specific interactions between the SMO and DMS, the utilization NFO services within the SMO framework for O-Cloud deployment failure recovery, or the detailed methods employed for the NF recovery is not the subject of this TR.

NOTE 6: The specific actions taken by DMS to recover from NF failures by automatically recreating a new NF and deploying it into the network, are not the subject of this TR.

NOTE 7: The specific mechanisms by which the SMO framework utilizes its services to recover user services in O-Cloud NF Deployment(s)—including the migration of those services from an impacted NF to newly created NF— are not the subject of this TR.

The flow diagram of the O-Cloud NF deployment resiliency use case is given in Figure 7.5.3-1.

# @startuml

!pragma teoz true skin rose skinparam ParticipantPadding skinparam BoxPadding 10 skinparam defaultFontSize 14

Box "Operator" #Lightblue Actor operator as "Operations Actor" End box

box “Service Management and Orchestration Framework” #gold Participant focom as "FOCOM”

participant nfo as "NFO" participant oam as “RAN\nOAM”

end box

box "O-Cloud" #lightseagreen participant ims as "IMS" participant dms as “DMS" participant nf1 as "NF Deployment(s)#1" participant nf2 as "NF Deployment(s)#2"   
end box Participant oru as "O-RU"

note over focom, oru <B>PRECONDITIONS:</B>

2. SMO subscribed to CM notifications, alarms, and performance counters from O-Cloud via O2 IMS and O2 DMS interfaces

3. SMO subscribed to alarms and performance counters from NF via O1 interface end note

$= =$ BEGIN O-CLOUD NF FAILURE RECOVERY USE CASE $= =$ opt

alt NF Deployment(s) failure   
note over nf1: [1a] NF Deployment(s) goes down   
Else Whole NF instance failure   
note over nf1: [1b] NF instance failure   
End alt   
End opt   
Group SMO detecting the NF related failures (infra, deployment, and instance)   
ref over focom, oam: [2] SMO analyses the alarms and PM data \n[O-RAN.WG6.ORCH-USE-CASES,   
Clauses 3.7 and 3.8]   
Note over oam, nf1: [3] $< < 0 1 > >$ NF instance failure if any   
Note over nfo, nf1: [4] $< < 0 2 > >$ SMO detects issues with NF Deployment(s)#1 and   
infrastructure resource with IMS and DMS if any

End group

Opt If SMO has detected NF instance failure and the impacted NF instance is still   
reachable to the SMO through O1 interface   
Note over oam, oru: [5] $< < 0 1 > >$ SMO lock/deactivates and/or removes cell(s) and associated   
carriers of the failed NF   
End opt

Group SMO coordinates for the NF recovery from failures (infra, deployment, and instance)

Alt If SMO has detected issues with the NF Deployment   
alt if SMO has detected the issue is caused by infrascture resource failure (e.g. node   
failure, cluster failure, site failure)   
ref over focom,nf2 : [6a] Recreate new NF Deployment i.e., NF Deployment(s)#2, on   
alternative infrastructure resource \n[O-RAN.WG6.ORCH-USE-CASES, Clause 3.2.1]   
else   
ref over focom,nf2 : [6b] Recreate new NF Deployment i.e., NF Deployment(s)#2, on the   
same infrastructure resource \n[O-RAN.WG6.ORCH-USE-CASES, Clause 3.2.1]   
end alt   
End alt

opt if NF instance need to be reconfigured

Note over oam, oru: [7] <<O1>> SMO configures NF Deployment(s)#2 with cell(s) and   
associated carriers, \nunlock and activate the cell(s) when their resources are ready for   
activation   
End opt

End group

Note over nf2: [8] NF Deployment(s)#2 ready \nto offer services

![](images/23b4c4dd6efbad06ac34efa906f3793f1db25cf7dbb64fd43128309003c53d99.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.5.3-1: SMO managed NF resiliency in O-Cloud deployment

# 7.6 Solution 5: Multi-Domain Recovery Service

# 7.6.1 Basic objective

The following solution applies to the path failure scenario described in clause 5.6. The details of multi-domain recovery service procedures are described below.

When a traffic failure is identified, e.g., by the SMO or the network operator, the SMO can trigger a recovery process by providing the details of the failed path to a recovery service, such as the MDRS, within the SMO. In response, the recovery service queries the RAN NF OAM and TE&IV services for information pertaining to network topology, alarms/events, loading, along with operator defined policies. The recovery service uses this information to identify existing Alternative Path (AP), e.g. using available backup hardware, and if possible, can generate the new AP(s) information.

AP generation can be the responsibility of a function, alternate path generation function (APGF), within the MDRS. Once the information AP is determined, the MDRS configures the relevant network domains, e.g. via O1/O2/new interface, to enable the recovery with the AP.

# 7.6.2 Roles of involved entities

The description below outlines the actors involved:

Transport network Manager (TN Manager):

Uses SMO policies/configurations to manage transport paths, facilitating updated configuration from SMO to be applied (directly or indirectly) to the transport network nodes. Notifies the SMO when a transport node failure occurs, e.g. in the transport path between O-RU and O-DU.

SMO:

Accountable for delivering data on existing failed paths to the MDRS_API and receiving updates on AP identification and successful reconfiguration implementation. Triggers MDRS process when notified by TN Manager when transport network failures occur.

# RAN-NF-OAM:

Collects, aggregates and exposes network-wide events and alarms of network objects (including and not limited to infrastructure, platform, application and transport).

TE&IV:

Pulls, stores and exposes a detailed (high-level and low level) network information, network objects including utilization parameters.

MDRS_API:

Queries RAN NF OAM service and TE&IV service to gather data on topology, alarms, and load conditions followed by identifying or generating optimal AP(s) and sending AP details to relevant network domains.

APGF:

Identifies existing alternative paths (AP) and generates new AP information that can be utilized, assigns weights to each identified existing AP and new AP information, and selects an AP based on assigned weights.

NSF:

Divides the network into network segments based on (bandwidth, latency, etc) and generates low-level information query for the relevant network segments to network topology, thus, allows an efficient retrieval of detailed network information for specific segments of the network.

# 7.6.3 Solution description

The solution described in Table 7.6.3-1.

Table 7.6.3-1: Multi Domain Recovery Procedure   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>The goal of this sub use case solution is to determination / generation an optimal alternative path and implement it via reconfiguration, once a failure in the following domains is discovered: O-Cloud, O-RAN node, transport and interfaces This is a service impacting use case.</td><td></td></tr><tr><td>Assumptions Begins when</td><td>Transport Network Manager (TN Manager): Uses SMO policies/ configurations to manage transport paths, facilitating updated configuration from SMO to be applied (directly or indirectly) to the transport network nodes. Notifies the SMO when a transport node failure occurs, e.g. in the transport path between O-RU and O-DU. SMO: Accountable for delivering data on existing failed paths to the MDRS_API and receiving updates on AP identification and successful reconfiguration implementation. Triggers MDRS process when notified by Queries RAN NF OAM service and TE&amp;IV service to gather data on topology, alarms, and load conditions followed by identifying or generating optimal AP(s) and sending AP details to relevant network domains. APGF: Identifies existing alternative paths (AP) and generates new AP information that can be utilized, assigns weights to each identified existing AP and new AP information, and selects an AP based on assigned weights NSF: Divides the network into network segments based on (bandwidth, latency, etc) and generates Low-Level information query for the relevant network segments to network topology, thus, allows an eficient retrieval of detailed network information for specific segments of the network ● In the event of an active path failure, it is expected that a relevant</td><td rowspan="3">SMO service captures the failed path data and transmit it to the TE&amp;lV service supports API schemas of the following queries: High- The MDRS use case can be triggered by a relevant SMO service to</td></tr><tr><td>TN Manager when transport network failures occur. RAN-NF-OAM: Collects, aggregates and exposes network-wide events and alarms of network objects (including and not limited to infrastructure, platform, application and transport). Actors and Roles</td></tr><tr><td>TE&amp;IV: Pulls, stores and exposes a detailed (high-level and low level) network information, network objects including utilization parameters. MDRS_API:</td></tr><tr><td colspan="3" rowspan="1">BEGIN THE USE CASE</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">The SMO analyses alarms and performance management data, asdefined for O1 interface [i.8] and OFH M-Plane [i.7],See NOTE 1.</td><td colspan="1" rowspan="1">WG4.FH   M-Plane[i.7];WG10.01 interface[i.8]</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">The SMO initiates Alternative Path (AP) determination / generation bysending MDRS API a Network Path failure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">MDRS API requests High-Level Network topology data from TE&amp;lV</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">TE&amp;IV provides MDRS_API with the requested High-Level Networktopology data</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">NSF function execution</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">MDRS_API requests network events &amp; alarms based on relevant (for AP)logical network segment/s from RAN NF OAM</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">RAN NF OAM replies MDRS_API with the requested network events &amp;alarms based on relevant (for AP) logical network segments.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">MDRS API requests low-level network topology data from TE&amp;lV</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">TE&amp;IV replies MDRS_API with the requested low-level network topologydata</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">MDRS_API initiates APGF function execution by providing low-levelnetwork topology data, events &amp; alarms and objects loading information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">APGF function execution.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Successful AP determination / generation by APGF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">APGF updates MDRS API with determined / generated AP data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">Adjusting the underlying configuration to align with the AP.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Reconfiguration succeeded</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">MDRS_API updates SMO indicating successful reconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Reconfiguration failed</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">MDRS_API updates SMO indicating failed reconfiguration</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Alternative Path determination / generation failed</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">APGF updates MDRS APl indicating that the APGF execution had failed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">MDRS API updates SMO indicating that the APGF execution had failed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The use case ends upon completion of the TN Manager reconfiguring thetransport network to implement the AP determined by MDRS.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many exceptions. Some of these include:●   If the connectivity, or functionality of the management system(SMO) becomes unavailable. If the TN Manager loses connectivity, e.g. via O1 interface, toSMO.●   If TE&amp;IV data is outdated, or mismatched, with the actualtransport network configuration hence causing inaccurate APdetermination.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SUCCESSFUL POST-CONDITION – On a successful post-condition, thetransport network is configured according to the AP and connectivity isrestored within the network.FAlLURE POST-CONDITION – one of the various exception casesoccurs, there are a variety of failure post conditions. if the SMOconnectivity is lost then the indication from the TN Manager of thetransport node failure is not received by SMO, hence no connectivityrecovery is initiated. Another repercussion of stale data in TE&amp;lV is thedetermined AP is not compatible with the existing transport network.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: The logic applied by the SMO in this decision process is not subject of this technical report.</td></tr></table>

<table><tr><td>@startuml</td></tr><tr><td>!pragma teoz true</td></tr><tr><td></td></tr><tr><td>skin rose</td></tr></table>

skinparam ParticipantPadding 5 skinparam BoxPadding 10 skinparam defaultFontSize 14 autonumber

Box "Service Management and Orchestration Framework" #gold Participant smo as "SMO\n(non-RT RIC)" Participant ranoam as "RAN NF OAM" Participant teiv as "TE&IV" Participant mdrs as "MDRS" Participant apgf as "APGF"   
End box   
Box "Transport Network" #lightpink Participant tnm as "TN_Manager"   
End box   
Note over smo, teiv <b>PRECONDITIONS:</b> 1. MDRS is part of SMO framework. 2. APGF is either part of SMO framework or external to SMO framework   
End Note   
$= =$ BEGIN TRANSPORT RESILIENCY USE CASE $\underline { { \underline { { \mathbf { 1 } } } } } = = \underline { { \underline { { \mathbf { 1 } } } } }$   
tnm $- >$ smo : Trigger network condition analysis   
smo $- >$ mdrs : Initiate alternate path   
mdrs -> teiv : Queries high level NT info   
teiv $- >$ mdrs : High level NT info   
note right   
read HL NT info   
for relevant segment   
end note   
mdrs $- >$ mdrs : NSF execution   
mdrs -> ranoam : Queries network events & alarms   
ranoam $- >$ mdrs : Network events & alarms   
mdrs -> teiv : Queries low level network topology info   
teiv -> mdrs : Low level network topology info   
mdrs $- >$ apgf : Initiate APGF \n(Low-Level network topology data \nevents/alarms \nand   
objects loading info)   
apgf $- >$ apgf: APGF execution   
$= =$ Successful AP determination/generation by APGF $\mathop { \bf { \bar { \Sigma } } } = =$   
apgf $- >$ mdrs : APGF updates MDRS API with determined/generated AP data   
note right of mdrs : Adjusting the underlying configuration to align with the AP   
$= =$ Reconfiguration succeeded $\mathbf { \partial } = = \mathbf { \partial }$   
mdrs $- >$ smo : Reconfiguration succeeded   
smo $- >$ tnm : AP configuration   
tnm -> smo : Reconfiguration succeeded   
$= =$ Reconfiguration failed $\Longleftarrow =$ $- >$

$= = .$ Alternative path determination/generation failed $\mathbf { \partial } = = \mathbf { \partial }$ apgf $- >$ mdrs : APGF updates MDRS API the APGF execution failed mdrs $- >$ smo : Alternative path determination/generation failed @enduml

![](images/86ded66070863ed27e9a1caa5f093f89a69a958f2bd44f90040fd35e6385e9ec.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.6.3-1: Multi-Domain recovery procedure up to execution of APGF

# 8 Summary and impacts identified

# 8.1 Overview

This clause provides a summary of the technical report and discusses the impacts on various working groups required to implement end to end resiliency in a standardized manner.

# 8.2 Summary of evaluation

This Technical Report describes various aspects of resiliency, including the resiliency architecture and its application to O-RAN network elements, network functions, interfaces, O-Cloud NF deployment, and transport layer failures. It also describes the various scenarios and considerations, explores various back-up options, and interaction between resiliency and rolling upgrade processes, along with potential resiliency solutions.

This Technical Report focuses on several key aspects, including the impact of resiliency on O-RAN architecture, triggers for initiating resiliency actions, and various failure scenarios, with particular focus on failures involving the O1 interface, network functions, O-RU rehoming, and O-Cloud NF deployments. It describes the various scenarios and considerations, including resiliency in different deployments such as hierarchical and hybrid O-RU deployment, and Shared O-RU management, highlighting the entities involved and potential resiliency approaches. The report also explores both basic and advanced resiliency use case solutions related to O-DU, O-CU-CP, and O1 interface failures, aiming to ensure robust operations through fault and performance management and standardized recovery mechanisms across O-RU, O-DU, and O-CU nodes. Moreover, this TR describes the NF failure recovery in the O-Cloud deployment and SMO managed transport network for O-RU rehoming solutions.

The report identifies areas for potential enhancements to O1 interface, fault management, information and data models, O-Cloud infrastructure and deployment, and transport networks to support predictive monitoring, redundancy, and failover workflows. The proposed solutions focus on enhancing resiliency within network functions such as O-DU and O-CU-CP, O-Cloud NF deployment, and leveraging the transport network capabilities for network function rehoming with the goal of minimizing the service disruptions and also achieving end-to-end service continuity.

# 8.3 Impacts identified

The potential impacts on the various working groups and associated scope from a resiliency perspective can include the following:

Table 8.3-1: Impacts on various working groups   

<table><tr><td rowspan=1 colspan=1>Workinggroup</td><td rowspan=1 colspan=1>Scope</td><td rowspan=1 colspan=1>Impacts</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>WG1</td><td rowspan=1 colspan=1>ArchitectureUCTG</td><td rowspan=1 colspan=1>Interfaces       andcomponents/nodesUse cases</td><td rowspan=1 colspan=1>Investigate the inclusion of a Resiliency Controller/Orchestrator as part of the SMO framework, particularlywithin the context of the Transport Network Inclusion andDecoupled SMO works.Describe potential resiliency use cases and solutions for O-RAN interfaces and network functions failures</td></tr><tr><td rowspan=3 colspan=1>WG6</td><td rowspan=3 colspan=1>O-Cloudinfrastructureand  Networkfunction</td><td rowspan=1 colspan=1>02interface andnodes       (clusternodes/VM      andnetwork function thatis deployed in thecluster or VM)</td><td rowspan=3 colspan=1>●   Identify failure scenarios: Identify potential O-Cloudfailure scenarios and their impact to O-Cloudservices. Provide a detailed description of potentialfailure scenarios affecting the infrastructure, IMS,DMS, and O-Cloud applications. The identifiedfailure scenarios covers infrastructure resource level(for example, server failure, network outage, clusterfailure, data centre failure), the IMS software level(for example, signallingfailure, O-Cloudprovisioning procedure failure, IMS software failuresetc), the DMS level (for example, DMS control planeand deployment plane failures etc), and the O-Cloudapplication level (for example, NF Deploymentfailure, application workload failure etc).Study recovery solutions and identify requirements:For each identified failure scenario, study thepotential recovery or auto healing solutions. Thesesolutions identify the end-to-end steps required in/between SMO and O-Cloud to restore the systemto a functional state. As a result of the study,requirements on SMO, O-Cloud, O-Cloudapplication and O2 interface are identified.</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td>WG9</td><td></td><td colspan="2"></td><td>(Transport</td><td>Extend O2 IMS and O2 DMS capabilities: Identify</td><td>and propose extensions to the O2 IMS and O2 DMS capabilities that will improve the efficiency and effectiveness of failure recovery. This includes specifying the necessary modifications to these systems to support the defined recovery use cases. Develop Stage 2 and Stage 3 O2 specifications: Create detailed Stage 2 and Stage 3 procedures, information and data models for the identified requirements.</td></tr><tr><td></td><td>Transport</td><td colspan="2" rowspan="3">Transport-related aspects Network Inclusion Work Item)</td><td rowspan="3">O1 Interface</td><td rowspan="3">complete failures; specify the interface between SMO and the transport manager for these actions as part of Transport Network Inclusion Work Item.</td><td>Analyse transport-level failure scenarios in detail and define related use cases and requirements. Define use cases and solutions for SMO-managed transport networks, including how the transport manager receives policies, triggers, or configurations to rehome network functions during partial or</td></tr><tr><td>WG10</td><td>Cover generic network function (including O-RU, O- DU, and O-CU-CP) rehoming use cases with focus on Fronthaul/Mid-haul transport path management</td></tr><tr><td rowspan="5">01 interface and OAM</td><td>and the resulting impacts.</td></tr><tr><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4">OAM Architecture</td><td>The potential enhancements to be addressed are: · Fault management: Typical FM enhancements such as switchover states, backup activation metrics, and recovery operations in fault notifications.</td></tr><tr><td></td><td>Performance management: Updates to allow enhanced streaming of performance metrics to facilitate early detection of degradations.</td></tr><tr><td></td><td>Configuration management: Support for configurations in case of switchover scenarios to minimize downtime during failures.</td></tr><tr><td>different components.</td><td>Reuse the existing architecture for performance degradation detection and mitigation and disaster recovery, including the roles and interactions of</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td>Define use cases and scenarios within the existing architecture to support automated or operator-driven recovery processes, system reconfiguration to adapt to changing network conditions, and resiliency</td></tr><tr><td></td><td>actions such as switchover, backup activation, and fault isolation in the OAM architecture. Add provisions for managing resiliency across hybrid and hierarchical deployments, ensuring seamless interaction between SMO and Network</td></tr></table>

<table><tr><td></td><td>O1 NRM</td><td>to</td><td>Extend the network resource model and attributes related performance degradation/fault detection and management, mitigation and disaster recovery.</td></tr><tr><td rowspan="5"></td><td rowspan="5">O1 PM</td><td>●</td><td>Resiliency attributes: Inclusion of new attributes for representing redundancy configurations, such as active/standby roles for O-DU/O-CU and geo- redundancy.</td></tr><tr><td></td><td>Expansion of resource states to include resiliency-specific states like &quot;standby&quot; and &quot;failed&quot; for managed elements.</td></tr><tr><td></td><td>Failure and availability notifications: Enhanced notification mechanisms for the updates on network function failures, cell availability, and recovery actions.</td></tr><tr><td></td><td>Analyse the existing performance measurements (PM Counters) that can be utilized to detect performance degradation and its mitigation.</td></tr><tr><td></td><td>Identify the additional performance counters to be defined. For example, recovery time and data loss in case of disaster recovery. Inventory management related impacts to store the</td></tr><tr><td rowspan="4"></td><td>TE&amp;IV</td><td>resiliency back-up inventory and topology. Introduce attributes for resiliency planning, such as backup capacity and redundancy allocations.</td></tr><tr><td>●</td><td>Enhanced topology representation: Update the TE&amp;IV model to Incorporate new topology relationships, including active/standby network</td></tr><tr><td></td><td>nodes, redundancy configurations (for example, active/standby links), and shared O-RU deployments, while enabling tracking of redundancy status.</td></tr><tr><td></td><td>Dynamic inventory updates: Enable inventory updates reflecting changes due to failover or switchover actions.</td></tr><tr><td></td><td></td><td>Data consistency: Ensure resiliency-related metadata (for example, backup states) accurately reflected in inventory systems.</td></tr></table>

The proposed enhancements aim to incorporate resiliency-related aspects and impacts outlined in the Technical Report into specifications across the above-mentioned impacted working groups, aligning with the resiliency objectives to ensure end-to-end resiliency in O-RAN deployments. Key focus areas include the integration of predictive mechanisms, optimized/standardized recovery processes, and robust fault and performance management. Together, these improvements enable the O-RAN network deployment to maintain services to users with minimal disruptions during the above-mentioned failure scenarios.

# Annex A:

Void

# Annex (informative): Change history/Change request (history)

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2024-08-22</td><td rowspan=1 colspan=1>00.04</td><td rowspan=1 colspan=1>Baseline version of WG1 UCTG Technical Report on O-RAN Resiliency</td></tr><tr><td rowspan=1 colspan=1>2025-02-12</td><td rowspan=1 colspan=1>00.05</td><td rowspan=1 colspan=1>The following CRs are implemented. RMI.AO CR-0005 – O-DU resiliencyRMI.AO CR-0007 - O-DU failureRMI.AO CR-0008 – Resiliency scenario and considerationsRMI.AO CR-0009 – Resiliency for NE and NF failures and O-RU failuresRMI.AO CR-0010 – Resiliency for interface failuresBMN.AO CR-0010 – MDRS (Multi-Domain Recovery Service)RMI.AO CR-0011 – Management plane interface failuresRMI.AO CR-0012 – Deployment scenariosRMI.AO CR-0013 – Various considerations for resiliency10) RMI.AO CR-0014 – Transport resiliency considerations11) RMI.AO CR-0015 – Cell service restoration12)RMI.AO CR-0016 – O-CU-CP and O-CU-UP Failure13)RMI.AO CR-0017 – Control plane interfaces failure14)RMI.AO CR-0018 – User plane interfaces Failure15)RMI.AO CR-0019 – Cloud Iayer failures16)RMI.AO CR-0020 – Relationships with rolling upgrade17)RMI.AO CR-0021 – A1 interface failures</td></tr><tr><td rowspan=1 colspan=1>2025-05-21</td><td rowspan=1 colspan=1>00.06</td><td rowspan=1 colspan=1>The following CRs are implemented.1) RMI.AOCR-0022 – O-CU Resiliency use case solution2) RMI.AO CR-0024 – Using the transport resiliency solution to enable seamless O-RUrehoming</td></tr><tr><td rowspan=1 colspan=1>2025-05-30</td><td rowspan=1 colspan=1>00.07</td><td rowspan=1 colspan=1>The following CRs are implemented.1) RMI.AO°CR-0025 – O-Cloud NF Deployment Resiliency use case solution2) RMI CR-0026 – Update to O-DU Resiliency use case solution</td></tr><tr><td rowspan=1 colspan=1>2025-06-06</td><td rowspan=1 colspan=1>00.08</td><td rowspan=1 colspan=1>●  RMI CR-0027 – TR summary and impacts identified●  Editorial fixes</td></tr><tr><td rowspan=1 colspan=1>2025-06-12</td><td rowspan=1 colspan=1>00.09</td><td rowspan=1 colspan=1>• The following CRs are implemented.1) BMN.AO CR-0011 – MDRS use case solution2)RMI CR-0028 – Remove gNB restoration clause3)RMI CR-0029 – Update Clause 7.1 - Potential resiliency solutions clause overview4) RMI CR-0030 – Update Clause 5.3 - Resiliency development in O-RAN• Editorial fixes</td></tr><tr><td rowspan=1 colspan=1>2025-06-26</td><td rowspan=1 colspan=1>00.10</td><td rowspan=1 colspan=1>• The following CRs are implemented.1. RMI CR-0031 – Remove NE in Clause 5.4 - Resiliency for NE and NF failures2. RMI CR-0032 – Address Nokia&#x27;s comments to the TR (v00.09)• Editorial fixes including list of tables and list of figures update</td></tr><tr><td rowspan=1 colspan=1>2025-07-10</td><td rowspan=1 colspan=1>00.00.11</td><td rowspan=1 colspan=1>Clean version</td></tr><tr><td rowspan=1 colspan=1>2025-07-21</td><td rowspan=1 colspan=1>00.00.12</td><td rowspan=1 colspan=1>Editorial fixes based on the comments raised during vote.</td></tr><tr><td rowspan=1 colspan=1>2025-07-21</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>First version of O-RAN Resiliency TR.</td></tr></table>