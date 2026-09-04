# O-RAN.WG1.TS.Use-Cases-Detailed-Specification-R004-v18.00

# O-RAN Work Group 1 (Use Cases and Overall Architecture)

# Use Cases Detailed Specification

Copyright $©$ 2025 by the O-RAN ALLIANCE e.V.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material of this specification for your personal use, or copy the material of this specification for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, Germany

# Contents

Foreword......... ............................................................................................................................ ........5   
Modal verbs terminology ......................................................................................................................... ........5   
Introduction ........................................................................................................................................................5   
1 Scope ........................................................................................................................................................6   
2 References ................................................................................................................................................6   
2.1 Normative references ......................................................................................................................................... 6   
2.2 Informative references ....................................................................................................................................... 8   
3 Definition of terms, symbols and abbreviations.......................................................................................9   
3.1 Terms ................................................................................................................................................................. 9   
3.2 Symbols ........................................................................................................................................................... 10   
3.3 Abbreviations................................................................................................................................................... 10   
4   
4.1 Context-based dynamic HO management for V2X ......................................................................................... 11   
4.1.1 Background and goal of the use case ......................................................................................................... 11   
4.1.2 Entities/resources involved in the use case ................................................................................................ 11   
4.1.3 Solutions..................................................................................................................................................... 12   
4.1.4 Required data ............ ........................................................................................................... 14   
4.2 Flight path based dynamic UAV radio resource allocation ............................................................................. 14   
4.2.1 Background and goal of the use case ......................................................................................................... 14   
4.2.2 Entities/resources involved in the use case ................................................................................................ 15   
4.2.3 Solutions.......... ....................................................................................... 16   
4.2.4 Required data .........   
4.3 Radio resource allocation for UAV application scenario................................................................................. 17   
4.3.1 Background and goal of the use case ......................................................................................................... 18   
4.3.2 Entities/resources involved in the use case ................................................................................................ 19   
4.3.3 Solutions..................................................................................................................................................... 20   
4.3.4 Required data ............................................................................................................................................. 21   
4.4 QoE optimization ............................................................................................................................................. 21   
4.4.1 Background and goal of the use case ......................................................................................................... 21   
4.4.2 Entities/resources involved in the use case ............................................................................................... . 22   
4.4.3 Solutions............... ................................................................................................... 22   
4.4.4 Required data . 2 8   
4.5 Traffic steering..... . 29   
4.5.1 Background and goal of the use case ... . 29   
4.5.2 Entities/resources involved in the use case ....... .............................................................................. . 30   
4.5.3 Solutions..... . 30   
4.5.4 Required data .... . 35   
4.6 Massive MIMO optimization..... . 36   
4.6.1 Background and goal of the use case .... ....... 36   
4.6.2 Entities/resources involved in the use case . . 37   
4.6.3 Solutions...... . 39   
4.6.4 Required data ..... . 47   
4.7 RAN sharing ............. ................................................................................... . 50   
4.7.1 Background and goal of the use case .. . 50   
4.7.2 Entities/resources involved in the use case . . 51   
4.7.3 Solutions...... . 52   
4.7.4 Required data ...... .............................................. ... 54   
4.8 QoS based resource optimization.... . 55   
4.8.1 Background and goal of the use case ......................................................................................................... 55   
4.8.2 Entities/resources involved in the use case ................................................................................................ 55   
4.8.3 Solutions.................. ............................................................................................................ 56   
4.8.4 Required data ....... ........................................................................................ ....... 57   
4.9 RAN slice SLA assurance............. ....................................................................................... ........ 58   
4.9.1 Background and goal of the use case ..... ........ 58   
4.9.2 Entities/resources involved in the use case . .. 58   
4.9.3 Solutions................... .......................................................................................................... .. 59   
4.9.4 Required data ..... . 65   
4.10 Multi-vendor slices ........ ................................................................................................ 68   
4.10.1 Background and goal of the use case .. ... 68   
4.10.2 Entities/resources involved in the use case ................................................................................................ 69   
4.10.3 4.10.4 Solutions.....................Required data ............. ................................................................................................................................................................ ........ 69........ 76   
4.11 4.11.1 Dynamic spectrum sharing (DSS) ................................................................................................................... 76Background and goal of the use case ......................................................................................................... 76   
4.11.2 Entities/resources involved in the use case ....................................................................................... . 78   
4.11.3 Solutions............. ............................................................................................. ..... 79   
4.11.4 Required data ... .......................................................... . 81   
4.12 NSSI resource allocation optimization ....... ................................................................................................... 83   
4.12.1 4.12.2 Background and goal of the use case ......................................................................................................... 83Entities/resources involved in the use case ................................................................................................ 85   
4.12.3 Solutions....... ...................................................................... . 85   
4.12.4 Required data ..... ....................................................................................... ..... 87   
4.13 Local indoor positioning in RAN ....... ........................................................................................... 88   
4.13.1 4.13.2 Background and goal of the use case ......................................................................................................... 88Entities/resources involved in the use case ................................................................................................ 88   
4.13.3 4.13.4 Solutions.............. .............................................................................. ........ 89........ 91   
Required data .....................................................................................................................................   
4.14 Massive SU/MU-MIMO grouping optimization .. ........................................................... . 92   
4.15 O-RAN signalling storm protection ................................................................................................................. 92   
4.15.1 Background and goal of the use case ......................................................................................................... 92   
4.15.2 4.15.3 4.15.4 Entities/resources involved in the use case .....Solutions.......................................................... .................................................................................... ....... 93....... 93..... 100   
4.16 Congestion prediction and management ..... ...................................................................................... 100   
4.17 Industrial IoT optimization ..... ...................................................................... ... 101   
4.18 4.19 BBU pooling to achieve RAN elasticity ........................................................................................................ 101Integrated SON function within the O-RAN framework ............................................................................... 101   
4.19.1 4.19.2 Background and goal of the use case. ..................Entities/resources involved in the use case .......... . 101   
.................................................................................... 102   
4.19.3 Solutions.... .................................................................. . 104   
4.19.4 Required data ....... ................................................................................................................................. 114   
4.20 4.20.1 Shared O-RU ................................................................................................................................................. 115Background and goal of the use case ....................................................................................................... 115   
4.20.2 Entity/resources involved in the use case... ............................................................................. ..... 126   
4.20.3 Solution ......... ................................................................................................. 134   
4.20.4 Required data .......... ................................................................................................................. 226   
4.21 4.21.1 Network energy saving .................................................................................................................................. 228Background and goal of the use case ....................................................................................................... 228   
4.21.2 Entities/resources involved in the use case ...................................................................................... . 229   
4.21.3 Solutions............ .................................................................................................... 229   
4.21.4 4.22 MU-MIMO optimization ........ Required data .. ................................................................................................................ 238 ........................................................................ . 236   
4.22.1 Background and goal of the use case ....................................................................................................... 238   
4.22.2 Entities/resources involved in the use case . ................................................................................. ... 239   
4.22.3 4.22.4 Solutions................................................................................................................................................... 239Required data ........................................................................................................................................... 241   
4.23 4.24 Sharing Non-RT RIC data with the core........................................................................................................ 241Industrial vision SLA assurance .................................................................................................................... 242   
4.24.1 4.24.2 Background and goal of the use case ....................................................................................................... 242Entities/resources involved in the use case .............................................................................................. 242   
4.24.3 Solutions......... ........................................................................... . 243   
4.24.4 Required data ............... ............................................................................................... . 245   
4.25 Void ........ .. 245   
4.26 Interference detection, prediction and optimization...... ................................................................... ..... 245   
4.26.1 Background and goal of the use case .. .. 246   
4.26.2 4.26.3 Entities/resources involved in the use case ....Solutions......................................................... ............................................................................ ... 246... 247... 259   
4.27 Communication and computing integrated networks . ......................................................................... ... 260   
4.27.1 Background and goal of the use case . .................................................................................. .. 260   
4.27.2 Entities/resources involved in the use case ......................................................................................... ... 264   
4.27.3 Solutions.... ............................................................................ .. 266   
4.27.4 Required data . .................................................................................... ... 275   
Annex A (informative): Additional information ..... ......................................................... ..279   
A.1 Traffic steering use case A1 interface usage example . ............................................. ... 279   
Annex (informative): Change history/Change request (history) . ..281

# Foreword

This Technical Specification (TS) has been produced by WG1 of the O-RAN ALLIANCE.

The content of the present document is subject to continuing work within O-RAN and may change following formal ORAN approval. Should the O-RAN ALLIANCE modify the contents of the present document, it will be re-released by ORAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } \mathbf { X } = 0 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# Introduction

This document provides O-RAN WG1 detailed use case descriptions. Any multi-WG use case defined in O-RAN is expected to be documented in “O-RAN WG1 Use Case Analysis Report” and if the use case is to be studied further, it will be covered in this document in detail, and then in relevant WGs.

# 1 Scope

The present document specifies the top-level use cases as defined by O-RAN WG1 UCTG (Use Case Task Group). For each use case, the document describes the motivation, resources, steps involved, and the data requirements. These toplevel use cases are further detailed in relevant WGs along with the requirements for O-RAN components and their interfaces.

# 2 References

# 2.1 Normative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are necessary for the application of the present document.

<table><tr><td>[1] 3GPP TS 22.261: &quot;Service requirements for the 5G system; Stage 1&quot;</td></tr><tr><td></td></tr><tr><td>[2] 3GPP TS 23.501: &quot;System architecture for the 5G System (5GS); Stage 2&quot;</td></tr><tr><td>[3] 3GPP TS 28.310: &quot;Management and orchestration; Energy efficiency of 5G&quot;</td></tr><tr><td>[4] 3GPP TS 28.530: &quot;Management and orchestration; Concepts, use cases and requirements&quot;</td></tr><tr><td>[5] 3GPP TS 28.541: &quot;Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3&quot;</td></tr><tr><td>[6] 3GPP TS 28.552: &quot;Management and orchestration; 5G performance measurements&quot;</td></tr><tr><td>[7] 3GPP TS 28.554: &quot;Management and orchestration; 5G end to end Key Performance Indicators</td></tr><tr><td>(KPI)&quot;&#x27; [8] 3GPP TS 28.622: &quot;Telecommunication management; Generic Network Resource Model (NRM)</td></tr><tr><td>Integration Reference Point (IRP); Information Service (IS)&quot; 3GPP TS 28.624: &quot;Telecommunication management; State management data definition Integration</td></tr><tr><td>[9] Reference Point (IRP); Requirements&quot;&quot;</td></tr><tr><td>[10] 3GPP TS 28.625: &quot;Telecommunication management; State Management Data Definition Integration Reference Point (IRP); Information Service (IS)&quot;</td></tr><tr><td>[11] 3GPP TS 28.626: &quot;Telecommunication management; State management data definition Integration</td></tr><tr><td>Reference Point (IRP); Solution Set (SS) definitions&quot; [12] 3GPP TS 37.340: “Evolved Universal Terrestrial Radio Access (E-UTRA) and NR; Multi-</td></tr><tr><td>connectivity; Overall Description; Stage 2&quot;</td></tr><tr><td>[13] 3GPP TS 38.211: &quot;NR; Physical channels and modulation&quot; [14] 3GPP TS 38.213: &quot;NR; Physical layer procedures for control&quot;</td></tr></table>

[15]

ETSI EN 302 637-2: “Intelligent Transport Systems (ITS); Vehicular Communications; Basic Set of Applications; Part 2: Specification of Cooperative Awareness Basic Service”, Release 1, November 2010

[16]

ETSI EN 302 637-3: “Intelligent Transport Systems (ITS); Vehicular Communications; Basic Set of Applications; Part 3: Specifications of Decentralized Environmental Notification Basic Service”, Release 1, November 2014

GSMA NG.116: “Generic Network Slice Template”, Version 2.0, October 2019

ITU-T X.731: “Information technology - Open Systems Interconnection - Systems management: State management function”

RFC 8348: “A YANG Data Model for Hardware Management”

3GPP TS 28.313: “Management and orchestration; Self-Organizing Networks (SON) for 5G networks”

3GPP TS 28.532: “Management and orchestration; Generic management services”

3GPP TS 23.502: “Procedures for the 5G System (5GS); Stage 2”

ETSI GS NFV IFA013: “Management and Orchestration; Os-Ma-nfvo reference point - Interface and Information Model Specification”, v4.4.1, Release 4, March 2023

[24]

ETSI GS NFV IFA008: “Management and Orchestration; Ve-Vnfm reference point - Interface and Information Model Specification”, v4.3.1, Release 4, May 2022

O-RAN WG5.O-DU-O1: “O1 Interface specification for O-DU”, Version R003-V09, December 9, 2023

O-RAN.WG6.ORCH-USE-CASES: “Cloudification and Orchestration Use Cases and Requirements for O-RAN Virtualized RAN”

O-RAN.WG10.OAM-Architecture: “O-RAN Working Group 10, O-RAN Operations and Maintenance Architecture”

O-RAN.WG4.MP: “O-RAN Working Group 4 (Open Fronthaul Interfaces WG), Management Plane Specification”

O-RAN.WG4.CUS.0-v02.00: “O-RAN Fronthaul Working Group, Control, User and Synchronization Plane Specification”

3GPP TS 36.423: “Evolved Universal Terrestrial Radio Access Network (E-UTRAN); X2 application protocol (X2AP)”

3GPP TS 36.314: “Evolved Universal Terrestrial Radio Access (E-UTRA); Layer 2 – Measurements”

3GPP TS 32.425: “Telecommunication management; Performance Management (PM); Performance measurements; Evolved Universal Terrestrial Radio Access Network (E-UTRAN)”

3GPP TS 36.300: “Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2”

3GPP TS 23.401: “General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”

3GPP TS 23.203: “Policy and charging control architecture”

3GPP TS 36.214: “Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer; Measurements”

[38] 3GPP TS 36.331: “Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification”   
[39] O-RAN.WG11.TS.Security-Requirements-Specification.0-R004-v11.00: “Security Requirements and Controls Specifications”   
[40] 3GPP TS 28.623: “Telecommunication management; Generic Network Resource Model (NRM) Integration Reference Point (IRP); Solution Set (SS) definitions”   
[41] 3GPP TS 28.662: “Telecommunication management; Generic Radio Access Network (RAN) Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)”   
[42] O-RAN.WG6.TS.O-CLOUD-IM: “O-RAN Work Group 6 (Cloudification and Orchestration Workgroup), O-Cloud Information Model”

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

<table><tr><td>[i.1]</td><td>3GPP TR 21.905: &quot;Vocabulary for 3GPP Specifications&#x27;&quot;</td></tr><tr><td>[i.2]</td><td>3GPP TR 37.817: &quot;Evolved Universal Terrestrial Radio Access (E-UTRA) and NR; Study on enhancement for Data Collection for NR and EN-DC&quot;</td></tr><tr><td>[i.3]</td><td>3GPP TR 38.889: &quot;Study on NR-based access to unlicensed spectrum&quot;</td></tr><tr><td>[i.4]</td><td>3GPP TR 38.913: &quot;Study on Scenarios and Requirements for Next Generation Access Technologies&#x27;&quot;</td></tr><tr><td>[i.5]</td><td>ETSI ES 203 228: &quot;Environmental Engineering (EE); Assessment of mobile network energy efficiency&quot;, V1.3.1, October 2020</td></tr><tr><td>[i.6]</td><td>Chih-Lin I, Guanding Yu, Shuangfeng Han, Geoffrey Ye Li, &quot;Green and Software-defined Wireless</td></tr><tr><td>[i.7]</td><td>Networks: From Theory to Practice&quot;, Cambridge University Press, 2019 ETSI White Paper No. 54, &quot;Evolving NFV towards the next decade&quot;, May, 2023</td></tr><tr><td>[i.8]</td><td>ETSI GS MEC 003: “Multi-access Edge Computing (MEC); Framework and Reference</td></tr><tr><td>[i.9]</td><td>Architecture&quot; ITU-T Y.IMT2020-CNC-req, Recommendation, &quot;Requirements of coordination of computing and</td></tr><tr><td>[i.10]</td><td>networking for IMT-2020 and beyond&quot; 3GPP TS 28.538: &quot;Management and orchestration; Edge Computing Management (ECM)&quot;</td></tr><tr><td>[i.11]</td><td>https://www.synopsys.com/automotive/autonomous-driving-levels.html</td></tr><tr><td>[i.12]</td><td>3GPP TS 22.186: &quot;Enhancement of 3GPP support for V2X scenarios; Stage 1&quot;</td></tr><tr><td>[i.13]</td><td>3GPP TR 26.928: &quot;Extended Reality (XR) in 5G&quot;</td></tr><tr><td>[i.14]</td><td>3GPP TR 38.885: “NR; Study on NR Vehicle-to-Everything (V2X)&quot;</td></tr></table>

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms and definitions [given in [i.1] and the following] apply. A term defined in the present document takes precedence over the definition of the same term, if any, in [i.1].

A1: Interface between Non-RT RIC and Near-RT RIC to enable policy-driven guidance of Near-RT RIC applications/functions, and support AI/ML workflow.

A1 policy: Type of declarative policies expressed using formal statements that enable the Non-RT RIC function in the SMO to guide the Near-RT RIC function, and hence the RAN, towards better fulfilment of the RAN intent.

A1 enrichment information: Information utilized by Near-RT RIC that is collected or derived at SMO/Non-RT RIC either from non-network data sources or from network functions themselves.

E2: Interface connecting the Near-RT RIC and one or more O-CU-CPs, one or more O-CU-UPs, and one or more ODUs.

E2 node: A logical node terminating E2 interface. In the present document, O-RAN nodes terminating E2 interface are:

- for NR access: O-CU-CP, O-CU-UP, O-DU or any combination.   
- for E-UTRA access: O-eNB.

FCAPS: Fault, Configuration, Accounting, Performance, Security.

Intents: A declarative policy to steer or guide the behavior of RAN functions, allowing the RAN function to calculate the optimal result to achieve stated objective.

Near-RT RIC: O-RAN Near-Real-Time RAN Intelligent Controller: A logical function that enables near-real-time control and optimization of RAN elements and resources via fine-grained data collection and actions over E2 interface.

Non-RT RIC: O-RAN Non-Real-Time RAN Intelligent Controller: A logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policybased guidance of applications/features in Near-RT RIC.

O-CU: O-RAN Central Unit: A logical node hosting O-CU-CP and O-CU-UP.

O-CU-CP: O-RAN Central Unit – Control Plane: A logical node hosting the RRC and the control plane part of the PDCP protocol.

O-CU-UP: O-RAN Central Unit – User Plane: A logical node hosting the user plane part of the PDCP protocol and the SDAP protocol.

O-DU: O-RAN Distributed Unit: A logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

O-RU: O-RAN Radio Unit: A logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

O1: Interface between management entities (SMO/EMS/MANO) and O-RAN managed elements, for operation and management, by which FCAPS management, software management, file management can be achieved.

O2: Interface between management entities and the O-Cloud for supporting O-RAN virtual network functions.

RAN: Generally referred as Radio Access Network. In terms of this document, any component below Near-RT RIC per O-RAN architecture, including O-CU/O-DU/O-RU.

Shared O-RU: An O-RU that is able to be configured to operate with one or more O-DUs operated by one or more mobile network operators.

# 3.2 Symbols

Void

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations [given in [i.1] and the following] apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in [i.1].

<table><tr><td>AI/ML</td><td>Artificial Intelligence/Machine Learning</td></tr><tr><td>AISG</td><td>Antenna Interface Standards Group</td></tr><tr><td>CAM</td><td>Cooperative Awareness Message</td></tr><tr><td>DENM</td><td>Decentralized Environmental Notification Message</td></tr><tr><td>eNB</td><td>eNodeB (applies to LTE)</td></tr><tr><td>gNB</td><td>gNodeB (applies to NR)</td></tr><tr><td>KPI</td><td>Key Performance Indicator</td></tr><tr><td>MIMO</td><td>Multiple Input, Multiple Output</td></tr><tr><td>mTLS</td><td>Multiplexed Transport Layer Security</td></tr><tr><td>NACM</td><td>NETCONF Access Control Model</td></tr><tr><td>NRT</td><td>Neighbor Relation Table</td></tr><tr><td>O-CU</td><td>O-RAN Central Unit</td></tr><tr><td>O-DU</td><td>O-RAN Distributed Unit</td></tr><tr><td>O-RU</td><td>O-RAN Radio Unit</td></tr><tr><td>PRB</td><td>Physical Resource Block</td></tr><tr><td>QoE</td><td>Quality of Experience</td></tr><tr><td>RAN</td><td>Radio Access Network</td></tr><tr><td>RIC</td><td>O-RAN RAN Intelligent Controller</td></tr><tr><td>SINR</td><td>Signal-to-Interference-plus-Noise Ratio</td></tr><tr><td>SMO</td><td>Service Management and Orchestration</td></tr><tr><td>TLS</td><td>Transport Layer Security</td></tr><tr><td>UAV</td><td>Unmanned Aerial Vehicle</td></tr><tr><td>V2X</td><td>Vehicle to Everything</td></tr></table>

# 4 Use cases

# 4.1 Context-based dynamic HO management for V2X

This use case provides the background, motivation, and requirements for the context-based dynamic HO management for V2X use case, allowing operators to adjust radio resource allocation policies through the O-RAN architecture, reducing latency and improving radio resource utilization.

# 4.1.1 Background and goal of the use case

V2X communication allows for numerous potential benefits such as increasing the overall road safety, reducing emissions, and saving time. Part of the V2X architecture is the V2X UE (SIM $^ +$ device attached to vehicle) which communicates with the V2X Application Server (V2X AS). The exchanged information comprises Cooperative Awareness Messages (CAMs), (from UE to V2X AS) [15], radio cell IDs, connection IDs, and basic radio measurements (RSRP, RSPQ, etc.)

As vehicles traverse along a highway, due to their high speed and the heterogeneous natural environment V2X UEs are handed over frequently, at times in a suboptimal way, which can cause handover (HO) anomalies: e.g., short stay, pingpong, and remote cell. Such suboptimal HO sequences substantially impair the functionality of V2X applications. Since HO sequences are mainly determined by the Neighbour Relation Tables (NRTs), maintained by the xNBs, there is hardly room for UE-level customization.

This UC aims to present a method to avoid and/or resolve problematic HO scenarios by using past navigation and radio statistics in order to customize HO sequences on a UE level. To this end, the AI/ML functionality that is enabled by the Near-RT RIC is employed.

# 4.1.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve necessary performance, configuration, and other data for constructing/training relevant AI/ML models that will be deployed in Near-RT RIC to assist in the V2X HO management function. For example, this could be a clustering algorithm that classifies traffic situations and radio conditions that (probably) do or do not lead to HO anomalies.   
b) Support deployment and update of AI/ML models into Near-RT RIC xApp.   
c) Support communication of intents and policies (system-level and UE-level) from Non-RT RIC to Near-RT RIC.   
d) Support communication of non-RAN data to enrich control functions in Near-RT RIC (enrichment data).

2) Near-RT RIC:

a) Support update of AI/ML models retrieved from Non-RT RIC.   
b) Support interpretation and execution of intents and policies from Non-RT RIC.   
c) Support necessary performance, configuration, and other data for defining and updating intents and policies for tuning relevant AI/ML models.   
d) Support communication of configuration parameters to RAN.

3) RAN:

a) Support data collection with required granularity to SMO over O1 interface.   
b) Support near-real-time configuration-based optimization of HO parameters over E2 interface.   
c) Report necessary performance, configuration, and other data for performing real-time V2X HO optimization in the Near-RT RIC over E2 interface.

4) V2X application server:

a) Support data collection with required granularity from V2X UE over V1 interface. b) Support communication of real-time traffic related data about V2X UE to Non-RT RIC as en

# 4.1.3 Solutions

# 4.1.3.1 Context-based dynamic handover management for V2X

The context of the context-based dynamic handover management for V2X use case is captured in table 4.1.3.1-1.

Table 4.1.3.1-1: Context-based dynamic handover management for V2X   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Drive V2X UE HOs in RAN according to defined intents, policies, andconfiguration while enabling Al/ML-based solutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: RAN policy control function.Near-RT RIC: RAN policy enforcement function.RAN: Policy enforcement for configuration updates.SMO: Termination point for O1 interface.V2X AS: Termination point for V1 interface and enrichment data provider.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1, O1, E2 interface connectivity is established.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational.SMO has established the data collection and sharing process, and Non-RT RIChas access to this data.Non-RT RIC analyzes the historical data from RAN and V2X AS for training therelevant AI/ML models to be deployed or updated in the Near-RT RIC, as wellas Al/ML models required for real-time optimization of configuration and policies.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Non-RT RIC deploys/updates the Al/ML model in the Near-RT RIC via O1 or Non-RT RIC assigns/update the AI/ML model for the Near-RT RIC xApp via A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC communicates relevant policies/intents and enrichment data to theNear-RT RIC over the A1 interface. The enrichment data from the non-RAN datacan include V2X UE location, trajectory, navigation information, GPS data,CAMs, DENMs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">The Near-RT RIC receives the relevant info from the Non-RT RIC over the A1interface and from the RAN over the E2 interface, interprets the policies andupdates the AI/ML models.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">The Near-RT RIC infers optimal RAN configuration (UE-specific NRTs)according to the trained Al/ML models and communicates the result to the RANover E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">RAN deploys the configuration received from the Near-RT RIC over the E2interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4</td><td colspan="1" rowspan="1">If required, Non-RT RIC can configure specific performance measurement datato be collected from RAN to assess the performance of the V2X HO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">management function in Near-RT RIC, or to assess the outcome of the appliedpolicies and configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC monitors the performance of the V2X HO related function in Near-RT RIC by collecting and monitoring the relevant performance KPls andcounters from the RAN and the V2X AS.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the context-based dynamic handover management for V2X use case is given in figure 4.1.3.1-1.

![](images/7f38c9cc54b8ae590096646a05c3856b1d85a355d75beae9931e724f02aeb644.jpg)

> **Image Summary:** {"entities": ["xAPI Interface", "O-RAN Fronthaul API", "RAN Intelligent Controller (RIC)", "O-DU", "O-RU", "O-CU", "O-RAN Architecture", "Non-RT RIC", "Near-RT RIC", "Far-RT RIC", "gNB", "O-RAN Alliance"], "relationships": ["O-RAN Alliance → O-RAN Architecture: Defined by", "O-RAN Architecture → xAPI Interface: Uses", "O-RAN Architecture → O-DU: Contains", "O-RAN Architecture → O-RU: Contains", "O-RU → O-DU: Fronthaul API", "O-DU → O-CU: Fronthaul API", "Near-RT RIC → O-DU: A1 interface", "Near-RT RIC → O-CU: A1 interface", "Non-RT RIC → O-DU: A1 interface", "Non-RT RIC → O-CU: A1 interface", "Far-RT RIC → O-CU: A1 interface", "O-RU → Near-RT RIC: E2 interface", "O-CU → Near-RT RIC: E2 interface", "O-RU → Non-RT RIC: E2 interface", "O-CU → Non-RT RIC: E2 interface", "O-RU → Far-RT RIC: E2 interface", "O-CU → Far-RT RIC: E2 interface", "gNB → O-RAN Alliance: Uses"], "hierarchy": ["gNB = O-RU + O-DU + O-CU", "O-CU = CU-CP + CU-UP (Not Shown)"], "flows": [], "notes": ["Figure 1. O-RAN Architecture and RIC Interaction", "xAPI Interface: Standardized API for control and configuration", "RAN Intelligent Controller (RIC): Software component that optimizes RAN performance and behavior", "Note: Interaction with O-RU & O-CU is via A1 Interface. RIC can interact with O-RU via E2 Interface."]}
  
Figure 4.1.3.1-1: Context-based dynamic handover management for V2X flow diagram

# 4.1.4 Required data

The measurement counters and KPIs (as defined by 3GPP) shall be appropriately aggregated by cell, QoS type, slice, etc.

1) Measurement reports with RSRP/RSRQ/CQI information for serving and neighboring cells.   
2) UE connection and mobility/handover statistics with indication of successful and failed handovers and error codes etc.   
3) V2X related data: position, velocity, direction, navigation data, CAMs, DENMs as specified in ETSI EN 302 637-3 [16] and in [i.5].

# 4.2 Flight path based dynamic UAV radio resource allocation

This use case provides the background, motivation, and requirements for the support the use case of flight path based dynamic UAV radio resource allocation, allowing operators to adjust radio resource allocation policies through the ORAN architecture, reducing unnecessary handover and improving radio resource utilization.

# 4.2.1 Background and goal of the use case

The field trials’ results show that the coverage for low altitude is good and can provide various services for terrestrial UEs with good performance. However, since the site along the flight is mainly for terrestrial UEs, the altitude of the UAV is always not within the main lobe of the ground station antenna. And the side lobes give rise to the phenomenon of scattered cell associations particularly noticeable in the sky. The cell association pattern on the ground is ideally contiguous area where the best cell is most often the one closest to the UE. As the UE move up in height, the antenna side lobes start to be visible, and there is a possibility of the best cell no longer being the closest one. The cell association pattern in this particular scenario becomes fragmented especially at the height of $3 0 0 \mathrm { m }$ and above. Hence, at higher altitudes, several challenges that lead to a different radio environment are:

a) LOS propagation/uplink interference b) Poor KPI caused by antenna side lobes for base stations c) Sudden drop in signal strength

These challenges directly impact on the mobility performance of the drone and the service experience of the user. Hence, we would like to support the use case of flight path based dynamic UAV radio resource allocation to resolve the above issues.

Non-Real-Time RIC can retrieve necessary of aerial vehicles related measurement metrics from network based on UE’s measurement report and SMO, and flight path information of aerial vehicle, climate information, flight forbidden/limitation area information and space load information etc. from application, e.g., UTM (Unmanned Traffic Management) for constructing/training relevant AI/ML model that will be deployed in RAN. For example, this could be UL/DL interference from/to aerial vehicles, the detection of aerial vehicle UEs, and available radio resource (e.g., frequency, cell, beam, BWP, numerology) prediction. And the Near-Real-Time RIC can support deployment and execution of AI/ML models from Non-RT RIC. Based on this, the Near-Real-Time RIC can perform the radio resource allocation for on-demand coverage for UAV considering the radio channel condition, flight path information and other application information.

The architectural context of the flight path based dynamic UAV radio resource allocation use case is shown in figure 4.2.1-1.

![](images/fe386b31d675bdac6085ba544088a73f40e6b2545a91502870bc2239efa1251c.jpg)

> **Image Summary:** {"image": "image_description.png"}
  
Figure 4.2.1-1: Use case of flight path based dynamic UAV radio resource allocation

Since there is no effective functional module in current $\mathrm { e N B } / \mathrm { g N B }$ to retrieve the application information, perform machine learning and training based on both the acquired application information and radio environment information, and execute AI/ML models based on above information. And in the O-RAN architecture, the flight path based dynamic UAV radio resource allocation mechanism can be supported by the RIC function module, i.e., Non-Real-Time RIC and Near-RealTime RIC. Therefore, we provide the description of O-RAN support use case for flight path based dynamic UAV radio resource.

# 4.2.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve necessary of O-RAN support for aerial vehicles related measurement metrics from network level measurement report and SMO (can acquire data from application) for constructing/training relevant AI/ML model that will be deployed in Near-RT RIC to assist in the O-RAN support for aerial vehicles function. For example, this could be UL/DL interference from/to aerial vehicles, the detection of aerial vehicle UEs, and available radio resource (e.g. frequency, cell, beam, BWP, numerology) prediction.   
b) Training of potential ML models for O-RAN support for aerial vehicles, which can respectively autonomously control UL/DL interference from/to aerial vehicles, detect the UE of aerial vehicles, and predict available radio resource (e.g. frequency, cell, beam, BWP, numerology) for aerial vehicles.   
c) Send policies/intents to Near-RT RIC to drive the O-RAN support for aerial vehicles at RAN level in terms of expected behavior.

2) Near-RT RIC:

a) Support update of AI/ML models from Non-RT RIC.   
b) Support execution of the AI/ML models from Non-RT RIC.   
c) Support interpretation and execution of intents and policies from Non-RT RIC to derive O-RAN support for aerial vehicles at RAN level in terms of expected behavior.   
d) Support perform the radio resource allocation for on-demand coverage for UAV considering the radio channel condition, flight path information and other application information via the AI/ML models from Non-RT RIC.   
e) Sending aerial vehicles performance report to Non-RT RIC for evaluation and optimization.

3) RAN:

a) Support data collection with UE performance report over O1 interface.   
b) Support non-real-time optimization of radio resources allocation parameters over O1 interface.

4) Application server:

a) Provide application information, e.g. flight path information of aerial vehicle, climate information, flight forbidden/limitation area information and space load information.

# 4.2.3 Solutions

# 4.2.3.1 Flight path based dynamic UAV radio resource allocation

The context of the flight path based dynamic UAV radio resource allocation use case is captured in table 4.2.3.1-1.

Table 4.2.3.1-1: Flight path based dynamic UAV radio resource allocation   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">In the O-RAN architecture, the flight path based dynamic UAV radio resourceallocation mechanism can be supported, which can perform the radio resourceallocation for on-demand coverage for UAV considering the radio channelcondition, fight path information and other application information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: RAN policy control function.Near-RT RIC: RAN policy enforcement function.RAN: Implementation of updated configuration parameters.Application server: Generates RAN side UE-level policies.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/O1 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interface connectivitybeing established between them.A certificate is shared between Near-RT RIC and Non-RT RIC for modelrelated data exchange.E2 interface is established between Near-RT RIC and CU/DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Application server sends the application data to Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC deploys/updates Al/ML models in the Near-RT RIC via O1 or Non-RT RIC assigns/update the Al/ML model for the Near-RT RIC xApp via A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Non-RT RIC sends relevant policies/intents and enrichment data to the Near-RT RIC over the A1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">The Near-RT RIC receives the relevant info from the Non-RT RIC over the A1interface and from the RAN over the E2 interface, interprets the policies andupdates the AI/ML models.And the Near-RT RIC converts policy to specific configuration parametercommands.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">RAN executes the command to modify the configuration parameters RANexecutes the command to modify the configuration parameters.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC collects relevant performance data from eNB/gNB, to observe the data transmission performance improvement brought by the wireless resourceconfiguration optimization policy.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the flight path based dynamic UAV radio resource allocation use case is given in figure 4.2.3.1-1.

![](images/a031f5b280d570383b403f486e20c59869dca8807b06b9b437af43a9c525b6dd.jpg)

> **Image Summary:** {"image": "image_o_ran_arch.png"}
  
Figure 4.2.3.1-1: Use case of flight path based dynamic UAV radio resource allocation flow diagram

# 4.2.4 Required data

Multi-dimensional data are expected to be retrieved for AI/ML model training and policies generation.

1) Network level measurement report, including:

a) UE level radio channel information, mobility related metrics b) UE level location information

2) Aerial vehicles related measurement metrics collected from SMO (can acquire data from application or network, e.g., flight path information of aerial vehicle, climate information, flight forbidden/limitation area information and space load information).

# 4.3 Radio resource allocation for UAV application scenario

This use case provides the background, motivation, and requirements for the UAV control vehicle use case, allowing operators to adjust radio resource allocation policies through the O-RAN architecture, reducing latency and improving radio resource utilization.

# 4.3.1 Background and goal of the use case

As shown in figure 4.3.1-1, this scenario refers to a rotor UAV flying at low altitude and low speed, and carrying cameras, sensors and other devices mounted. The operation terminals work in the $5 . 8 \mathrm { G H z }$ to remote control the UAV for border/forest inspection, high voltage/base station inspection, field mapping, pollution sampling, and HD live broadcast. At the same time, the UAV mobile control stations and the anti-UAV weapons jointly provide the service of fighting against illegal UAVs to ensure low-altitude safety in special areas. The UAV operation terminals, the anti-UAV weapons, and the UAV mobile control stations are connected with the UAV control vehicle using 5G network.

![](images/496df7c4b3c7e88297922f9cc9a94d618d70581c0e4fde3c03e902167771bc19.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.3.1-1: UAV control vehicle application scenario

UAV control vehicle deploys network equipment, including O-CU, O-DU, the Non-RT RIC function modules and application server (in this use case it is an edge computing service platform) to provide reliable network services through 5G networks. The data transmitted over the network includes control data and application data. The control data includes navigation commands, configuration changes, flight status data reporting, etc. Control data requires low latency and low bandwidth requirements. The application data includes 4K high-definition video data, which has obvious uplink and downlink service asymmetry, and the uplink has high requirements on network bandwidth. The UAV control vehicle deploys edge computing services on the 5G gNB side to implement local processing of video and control information. At the same time, real-time data services can be provided with the third-party applications by a video server. The Near-RT RIC function module provides radio resource management functions of the gNB side.

![](images/c436ef443d5d4c4f1d626316cd1e4fcf5c8a55b0aa5a984ebfcd3418061b6041.jpg)

> **Image Summary:** {"image": "image_of_o_ran_architecture.png"}
  
Figure 4.3.1-2: Network architecture for UAV control vehicle application scenario

The 5G network supports real-time high-definition video transmission and remote low-latency control of UAV, and finally provides various industry services such as inspection, security, surveying, and mapping. In the UAV control vehicle application scenario, there are a small amount of control data interaction requirements between the terminal and the network interaction, as well as the large bandwidth requirements for uploading HD video.

The service asymmetry raises new requirements for resource allocation of the gNB. At the same time, the existing network operation and maintenance management platform (OSS system) can only optimize the parameters of a specific group of UEs, but not individual users. In the O-RAN architecture, the radio resource requirements for different terminals are sent to the gNB for execution by means of the RIC function module.

The UAV control vehicle has flexible layout features. In this use case, the application service and content are deployed on the edge computing platform instead of the core network; the RIC function module is used to schedule radio resources instead of the core network's QoS mechanism. In this way, the load and overhead of the core network can be reduced, the forwarding and processing time of data transmission can be reduced.

As shown in figure 4.3.1-2, this scenario involves two options of network architecture. Option A is that gNB and NearRT RIC are deployed on the control vehicle, Non-RT RIC and core network are deployed on the central cloud. The control vehicle is connected to the core network and Non-RT RIC via fiber optics. Option B is a private network, all the modules, including the gNB, Near-RT RIC, Non-RT RIC and the necessary core network function modules, are deployed in the control vehicle.

# 4.3.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Support sending resource allocation requirements to Near-RT RIC.   
b) Support receiving UE-level radio resource adjustment requirements from the application server.   
c) Support communication between Non-RT RIC and Near-RT RIC with UE-level policies.

2) Near-RT RIC:

a) Support for receiving resource allocation requests from Non-RT RIC.   
b) Support for the interpretation and execution of the resource allocation policies received from Non-RT RIC.   
c) Support communication with RAN of configuration parameters.

3) RAN:

a) Support resource allocation requests from the Near-RT RIC.   
b) Support sending terminal registration information to RAN application server and Near-RT RIC. c) Support non-real-time optimization of radio resources allocation parameters over O1 interface.   
d) Support for adjustment of the resource configuration parameters for a specific UE.

4) Application server:

a) Support receiving terminal registration information from E2 nodes via SMO.   
b) Support collection of user plane data uploaded from RAN.   
c) Support sending UE-level radio resource adjustment requirements to Non-RT RIC.

# 4.3.3 Solutions

# 4.3.3.1 UAV control vehicle

The context of the UAV control vehicle use case is captured in table 4.3.3.1-1.

Table 4.3.3.1-1: UAV control vehicle   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">In the UAV control vehicle scenario, the UE-level radio resource configurationoptimization is achieved through the delivery of policies and configurationparameters.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: RAN policy control function.Near-RT RIC: RAN policy enforcement function.RAN: Implementation of updated configuration parameters.Application server: Generates UE-level resource allocation requirements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/O1 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">The Non-RT RIC sends an instruction through the interface, informing the RANto allocate the default resource, and establish the cell.The RAN notifies the Near-RT RIC and application server of the accessedterminal (UE) information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Application server sends requirements of radio resource allocation adjustmentto Non-RT RIC.This request can be sent at any time, or it can be sent at regular intervals.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC converts the requirements to resource adjustment policy anddistributes the policy to the Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Near-RT RIC converts policy to specific configuration parameter commands.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">RAN executes the command to modify the configuration parameters.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">The specified UE adjusts the uplink rate.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The RAN operates using the newly deployed parameters/models.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the UAV control vehicle use case is given in figure 4.3.3.1-1.

![](images/5103e4106bcc49ae4c79f0f7829cf9bc7454b63678fc161f186ebf217bd17324.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.3.3.1-1: UAV control vehicle

# 4.3.4 Required data

Multi-dimensional data are expected to be retrieved for policy generation and performance improvements brought by the policy:

1) The number of terminals accessed, the identification information such as a UE ID that distinguishes each UAV connected with UAV the control vehicle, and the resource information assigned by default.   
2) UE-level radio resource allocation information, such as the number of PRB resources used in PDSCH/PUSCH scheduling.

# 4.4 QoE optimization

This use case provides the background and motivation for the O-RAN architecture to support real-time QoE optimization.   
Moreover, some high-level description and requirements over Non-RT RIC, A1 and E2 interfaces are introduced.

# 4.4.1 Background and goal of the use case

The highly demanding 5G native applications like cloud VR are both bandwidth consuming and latency sensitive. However, for such traffic-intensive and highly interactive applications, current semi-static QoS framework cannot efficiently satisfy diversified QoE requirements especially taking into account potentially significant fluctuation of radio transmission capability. It is expected that QoE estimation/prediction from application level can help deal with such uncertainty and improve the efficiency of radio resources, and eventually improve user experience. RAN analytics information as RAN service can be exposed to an external application or MEC. It is envisioned to be helpful for the application to improve the user experience.

The main objective is to ensure QoE optimization be supported within the O-RAN architecture and its open interfaces. Multi-dimensional data, e.g., user traffic data, QoE measurements, network measurement report, can be acquired and processed via ML algorithms to support traffic recognition, QoE prediction, QoS enforcement decisions. ML models can be trained offline and model inference will be executed in a real-time manner. Focus should be on a general solution that would support any specific QoE use case (e.g., cloud VR, video, etc.).

# 4.4.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve necessary QoE related measurement metrics from network level measurement report and SMO (can acquire data from application) for constructing/training relevant AI/ML model that will be deployed in NearRT RIC to assist in the QoE optimization function. For example, this could be application classification, QoE prediction, and available bandwidth prediction.   
b) Training of potential ML models for predictive QoE optimization, which can respectively autonomously recognize traffic types, predict quality of experience, or predict available radio bandwidth.   
c) Send policies/intents to Near-RT RIC to drive the QoE optimization at RAN level in terms of expected behavior.

2) Near-RT RIC:

a) Support update of AI/ML models from Non-RT RIC.   
b) Support execution of the AI/ML models from Non-RT RIC, e.g., application classification, QoE prediction, and available bandwidth prediction.   
c) Support interpretation and execution of intents and policies from Non-RT RIC to derive the QoE optimization at RAN level in terms of expected behavior.   
d) Sending QoE performance report to Non-RT RIC for evaluation and optimization.

3) RAN:

a) Support network state and UE performance report with required granularity to SMO over O1 interface.   
b) Support QoS enforcement based on messages from A1/E2, which are expected to influence RRM behavior.

4) Application server/MEC:

a) Request/subscribe RAN analytics information from Near-RT RIC.

# 4.4.3 Solutions

# 4.4.3.1 AI/ML model training and distribution

The context of the model training and distribution is captured in table 4.4.3.1-1.

Table 4.4.3.1-1: Model training and distribution   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Model training and distribution</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO, application server</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/01 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.A certificate is shared between Near-RT RIC and Non-RT RIC for modelrelated data exchange.Editor's note: Security related procedure is not defined in the presentdocument.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">QoE related measurement metrics from SMO (can acquire data fromapplication) and network level measurement report either for instantiatingtraining of a new ML model or modifying existing ML model.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC does the model training, obtains QoE related models, andcan deploy QoE policy model internally. An example of QoE-relatedmodels that can be used at the Near-RT RIC is provided as follows:a) Application classification model (optional and can refer to 3rdparty's existing functionality)b) QoE prediction modelc) QoE policy modeld)Available BW prediction model</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Non-RT RIC deploys/updates the AI/ML model in the Near-RT RIC via O1or Non-RT RIC assigns/update the Al/ML model for the Near-RT RICxApp via A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Near-RT RIC stores the received QoE related ML models in the MLmodel inference platform and based on requirements of ML models.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">If required, Non-RT RIC can configure specific performancemeasurement data to be collected from RAN to assess the performanceof Al/ML models and update the Al/ML model in Near-RT RIC based onthe performance evaluation and model retraining.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1">[</td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Near-RT RIC stores the received QoE related ML models in the MLmodel inference platform and execute the model for QoE optimizationfunction in Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the model training and distribution is given in figure 4.4.3.1-1.

![](images/2f023e45c032706fd94de92b882df1e09587aecd2ad2f436f140a9bb590da33e.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.4.3.1-1: Model training and distribution flow diagram

4.4.3.2 Policy generation and performance evaluation

The context of the policy generation and performance evaluation is captured in table 4.4.3.2-1.

Table 4.4.3.2-1: Policy generation and performance evaluation   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Policy generation and performance evaluation</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/O1 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">QoE related models have been deployed in Non-RT RIC and Near-RT RICrespectively.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The network operator/manager want to generate QoE policy or optimizeQoE related Al/ML models.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Non-RT RIC evaluates the collected data and generates the appropriateQoE optimization policy.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC sends the QoE optimization policy to Near-RT RIC via A1interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Near-RT RIC receives the policy from the Non-RT RIC over the A1interface and from the RAN over the E2 interface. And the Near-RT RICinferences the QoE related Al/ML models and converts policy to specificE2 control or policy commands.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Near-RT RIC sends the E2 control or policy commands towards RAN forQoE optimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">RAN enforces the received control or policy from the Near-RT RIC overthe E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (0)</td><td colspan="1" rowspan="1"> If required, Non-RT RIC can configure specific performance measurementdata to be collected from RAN to assess the performance of the QoEoptimization function in Near-RT RIC, or to assess the outcome of theapplied A1 policies. And then update A1 policy and E2 control or policy.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC monitors the performance of the QoE optimization relatedfunction in Near-RT RIC by collecting and monitoring the relevantperformance KPIs and counters from RAN.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the policy generation and performance evaluation is given in figure 4.4.3.2-1.

![](images/b7a074d1193d5b9be73ee3c547114e1f61060d4de235c49dfb7daf777c6d789a.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.4.3.2-1: Policy generation and performance evaluation flow diagram

# 4.4.3.3 RAN performance analytics

The context of the RAN performance analytics is captured in table 4.4.3.3-1.

Table 4.4.3.3-1: RAN performance analytics

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Expose RAN analytics information to external applications or MEC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Non-RT RIC, Near-RT RIC, SMO, application server/MEC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated.A1/O1 interface connectivity is established with Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>QoE related models have been deployed in Non-RT RIC and Near-RT RICrespectively.Editor&#x27;s note: Security related procedure is not defined in the presentdocument.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The application server or MEC wants to request/subscribe RAN analyticsinformation</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Application server or MEC sends RAN analytics information request toNear-RT RIC or subscribes RAN analytics information from Near-RT RICto get periodic or event triggered RAN performance.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Near-RT RIC receives the request or subscription from application serveror MEC. Upon the request, the Near-RT RIC subscribes and receives themeasurement data from O-CU/O-DU. Based on it, with QoE related AI/MLmodels, the Near-RT RIC infers the RAN analytics information, andexposes it to application server or MEC via the response or notificationcommand. Such information, e.g., performance analytics could be used forQoE optimization.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Application server gets response or sends subscription deletion toward theNear-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Application server executes logic control, e.g., TCP transmission windowadjustment, video coding rate selection to improve QoE.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the RAN performance analytics is given in figure 4.4.3.3-1.

![](images/e01563b889692bdb1481229dfc3e3d0aeb3aa1d7ed382dc854630cdcc37783f4.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.4.3.3-1: RAN performance analytics flow diagram

# 4.4.4 Required data

Multi-dimensional data are expected to be retrieved by Non-RT RIC for AI/ML model training and policies/intents generation. Network level measurement data from O-CU/O-DU are also expected to report to Near-RT RIC for RAN analytics information inference.

1) Network level measurement report, including:

a) UE level radio channel information, mobility related metrics, e.g., CQI, SINR, MCS   
b) L2 measurement report related to traffic pattern, e.g., throughput, latency, packets per-second, inter frame arrival time   
c) RAN protocol stack status: e.g., PDCP buffer status   
d) Cell level information: e.g., DL/UL PRB occupation rate

2) QoE related measurement metrics collected from SMO (can acquire data from application or network).

3) User traffic data, which can be obtained via a proprietary interface from existing data collection equipment and is currently out of the scope of A1 or E2.

# RAN analytics information:

RAN analytics information exposed by Near-RT RIC to application server includes but is not limited to:

1) UE level information, e.g.:

a) Predicted RAN performance, e.g., maximum/average traffic rate, maximum/average latency, average packet loss rate   
b) Prediction related information, e.g., confidence, validity period

2) Cell level information.

# 4.5 Traffic steering

This use case provides the motivation, description, and requirements for traffic steering use case, allowing operators to specify different objectives for traffic management such as optimizing the network/UE performance, or achieving balanced cell load.

# 4.5.1 Background and goal of the use case

5G systems will support many different combinations of access technologies namely; LTE (licensed band), NR (licensed band), NR-U (unlicensed band), Wi-Fi (unlicensed band) [i.3]. Several different multi-access deployment scenarios are possible with 5GC to support wide variety of applications and satisfy the spectrum requirements of different service providers;

Carrier aggregation between licensed band NR (primary cell) and NR-U (secondary cell) Dual connectivity between licensed band NR (primary cell) and NR-U (secondary cell) Dual connectivity between licensed band LTE (primary cell) and NR-U (secondary cell) Dual connectivity between licensed band NR (primary cell) and Wi-Fi (secondary cell)

NOTE: The scenario of dual connectivity between NR and Wi-Fi is not defined in the present document.

The rapid traffic growth and multiple frequency bands utilized in a commercial network make it challenging to steer the traffic in a balanced distribution. Further in a multi-access system there is need to switch the traffic across access technologies based on changes in radio environment and application requirements and even split the traffic across multiple access technologies to satisfy performance requirements. The different types of traffic and frequency bands in a commercial network make it challenging to handle the complex QoS aspects, bearer selection (Master Cell Group (MCG) bearer, Secondary Cell Group (SCG) bearer, split bearer), bearer type change for load balancing, achieving low latency and best in class throughput in a multi-access scenario with 5GC networks as specified in 3GPP TS 37.340 [12]. Typical controls are limited to adjusting the cell reselection and handover parameters; modifying load calculations and cell priorities; and are largely static in nature when selecting the type of bearers and QoS attributes.

Further, the RRM (Radio Resource Management) features in the existing cellular network are all cell-centric. Even in different areas of within a cell, there are variations in radio environment, such as neighboring cell coverage, signal strength, interference status, etc. However, base stations based on traditional control strategies treat all UEs in a similar way and are usually focused on average cell-centric performance, rather than UE-centric.

Such current solutions suffer from following limitations:

It is hard to adapt the RRM control to diversified scenarios including multi-access deployments and optimization objectives. • The traffic management strategy is usually passive, rarely taking advantage of capabilities to predict network and UE performance. The strategy needs to consider aspects of steering, switching, and splitting traffic across different access technologies in a multi-access scenario. Non-optimal traffic management, with slow response time, due to various factors such as inability to select the right set of UEs for control action. This further results in non-optimal system and UE performance, such as suboptimal spectrum utilization, reduced throughput and increased handover failures.

Based on the above reasons, the main objective of this use case is to allow operators to flexibly configure the desired optimization policies, utilize the right performance criteria, and leverage machine learning to enable intelligent and proactive traffic management.

# 4.5.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve necessary performance, configuration, and other data for defining and updating policies to guide the behavior of traffic management function in Near-RT RIC. For example, the policy could relate to specifying different optimization objectives to guide the carrier/band preferences at per-UE or group of UE granularity.   
b) Support communication of policies to Near-RT RIC.   
c) Support communication of measurement configuration parameters to RAN.

2) Near-RT RIC:

a) Support interpretation and enforcement of policies from Non-RT RIC.

3) E2 nodes:

a) Support data collection with required granularity to SMO over O1 interface.

# 4.5.3 Solutions

# 4.5.3.1 Policy-based traffic steering

The context of the traffic steering use case is captured in table 4.5.3.1-1.

Table 4.5.3.1-1: Traffic steering   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Drive traffic management in RAN in accordance with defined intents, policies,and configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: RAN policy control function.Near-RT RIC: RAN policy enforcement function.E2 nodes: Control plane and user plane functions.SMO/Collection &amp; Control: Termination point for O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1 interface connectivity is established with Non-RT RIC.O1 interface connectivity is established with SMO/ Collection &amp; Control.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational.SMO/ Collection &amp; Control has established the data collection and sharingprocess, and Non-RT RIC has access to this data. Non-RT RIC monitors the performance by collecting the relevant performanceevents and counters from E2 nodes via SMO/ Collection &amp; Control.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">If required, Non-RT RIC configures additional, more specific, performancemeasurement data to be collected from E2 nodes to assess the performance.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC decides an action and communicates relevant policies to Near-RTRIC over A1. The example policies can include:a) QoS targetsb) Preferences on which cells to allcate control plane and user plane</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">c) Bearer handling aspects including bearer selection, bearer typechange</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">The Near-RT RIC receives the relevant info from Non-RT RIC over A1 interface,interprets the policies and enforces them.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Non-RT RIC decides that conditions to continue the policy is no longer valid.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Non-RT RIC deletes the policy.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC monitors the performance by collecting the relevant performanceevents and counters from E2 nodes via SMO.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the traffic steering use case is given in figure 4.5.3.1-1.

![](images/e121184fc9ef7a68e9c0807e650ac3d8dd38fc7ce189fe7b93438164fefaa008.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.5.3.1-1: Traffic steering use case flow diagram

# 4.5.3.2 Enrichment information based traffic steering

In this variation, when the Near-RT detects cell congestion, it requests via A1-EI to Non-RT RIC analytics that can be used as additional information to assist in its efforts at alleviating that congestion.

The context of the enrichment information-based traffic steering use case is captured in table 4.5.3.2-1.

Table 4.5.3.2-1: Enrichment information-based traffic steering   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Drive traffic management in RAN in accordance with defined enrichmentinformation and associated decision control.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">• Non-RT RIC: RAN analytics and enrichment information framework.• "UE location" rApp: Capable of calculating the geo-location of UEs with aprediction on the granularity of seconds time scale (e.g., based on timingadvance and RRC measurements), aggregating and trending those overtime to learn mobility patterns, and using these to predict a UE's futurelocation based on its recent location history.• "Traffic steering" rApp: Determines set of UEs connected to requested celland requests UE location rApp analytics, forwarding the same to the Near-RT RIC.• Near-RT RIC: Detects breaches in expected performance and requestsenrichment information from Non-RT RIC to aid in mitigation efforts. Alsoperforms RAN decision control based on network telemetry and theenrichment information provided by Non-RT RIC.• E2 nodes: Control plane and user plane RAN functions.• SMO/ Collection &amp; Control: Termination point for O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">• All relevant functions and components are instantiated.• A1 interface connectivity is established between Near-RT RIC and Non-RTRIC.• O1 interface connectivity is established between RAN E2 nodes and SMO/Collection &amp; Control.• Near-RT RIC is capable of detecting a breach in cell performance anddetermine the usefulness of predictive data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">• Network is operational.• Network data collection pipelines have been engineered for necessary datavolumes and Non-RT RIC has access to this data.• Both rApps have registered via R1 the data types that they produce and thedata types they consume.• UE location rApp has been trained to recognize the UE mobility patterns inthe local area such that, given a UE identifier, it can quickly determinewhether that UE is or is not following a known mobility pattern.• Traffic steering rApp has subscribed to, and Non-RT RIC/SMO is collectingon its behalf, the relevant performance events and counters from E2 nodesvia SMO/ Collection &amp; Control.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">Related use</td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Near-RT RIC detects a cell performance breach (e.g., due to UE capacityconsiderations) and determines it might be useful to have additional information from the Non-RT RIC regarding UE candidates for handover.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Near-RT RIC requests of the Non-RT RIC the enrichment informationcorresponding to the UE_Traj_Pred R1 data type for the congested cell.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC leverages R1 to subscribe to UE_Traj_Pred data type from thetraffic steering rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp subscribes to relevant network data for the cell in question.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 4-8 (M)</td><td colspan="1" rowspan="1">Non-RT RIC/SMO interact with the O-RAN network to collect the requestednetwork data and deliver to the trficstering rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp determines from network data which UEs are connected tothe cells in question.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp leverages R1 to subscribe to UE location prediction datatype (UeLocPred) for those UEs connected to the cells in question and that alsomeet other criteria known to the traffic steering rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Non-RT RIC leverages R1 to have UE location rApp produce the requested datatype instances for the specified UEs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">UE location rApp subscribes to relevant network data for the UEs in question.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 13-17 (M)</td><td colspan="1" rowspan="1">Non-RT RIC/SMO interact with the O-RAN network to collect the requestednetwork data and deliver to the UE location rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (M)</td><td colspan="1" rowspan="1">UE location rApp determines from network data, trended over time, the UElocation prediction over a particular future time window (e.g., 10-30 seconds) forthe UE along with a confidence value for that prediction.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 19-20 (M)</td><td colspan="1" rowspan="1">UE location rApp leverages R1 to return the UeLocPred instances to the Non-RT RIC, which in turn delivers to the traffic steering rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 21 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp determines from UE location prediction analytics thepredicted locations of the specified UEs within the next 10-30 seconds, mapsthose locations into a historical RF measurements map overlaying cellboundaries to physical geography, and determines the subset of UEs predictedto be leaving the oversubscribed cell within the next 10-30 seconds anyway,and hence which would perhaps be candidates for expedited handover.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 22 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp leverages R1 to generate UE trajectory prediction(UE_Traj_Pred) data based on its analysis.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 23 (M)</td><td colspan="1" rowspan="1">Non-RT RIC leverages A1-EI to forward the UE trajectory prediction data to theNear-RT RIC as the corresponding A1 enrichment information type.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 24 (M)</td><td colspan="1" rowspan="1">The Near-RT RIC interprets the information content received across the A1-EI interface and determines whether and how to use that EI in its congestionmitigation activities. (As a further optimization, it can be useful for the Near-RTRIC to also understand what type of activity the UE is engaged in.)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 25 (M)</td><td colspan="1" rowspan="1">Near-RT RIC continues monitoring cell performance and decides thatcongestion has been resolved.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 26 (M)</td><td colspan="1" rowspan="1">Near-RT RIC requests the Non-RT RIC to discontinue UE_Traj_Pred dataproduction for the target cell.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 27 (M)</td><td colspan="1" rowspan="1">Non-RT RIC leverages R1 to unsubscribe to UE_Traj_Pred data type from thetraffic steering rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 28 (M)</td><td colspan="1" rowspan="1">Traffic steering rApp leverages R1 to unsubscribe to the UE location predictiondata type for the corresponding UEs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 29 (M)</td><td colspan="1" rowspan="1">Non-RT RIC leverages R1 to unsubscribe to UELocPred data type from the UElocation rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 30-32 (M)</td><td colspan="1" rowspan="1">UELocPred rApp unsubscribes to the relevant network data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">UE location prediction rApp ceases to produce the UE location prediction data for the corresponding UEs and to collect the associated network data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Near-RT RIC continues to monitor RAN performance.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the enrichment information-based traffic steering use case is given in figure 4.5.3.2-1.

![](images/09ac375e32974494c0b428220069cd4258982224f5fb70cbab21b7ae1976d9da.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.5.3.2-1: Enrichment information-based traffic steering use case flow diagram

# 4.5.4 Required data

The measurement counters and KPIs (as defined by 3GPP and will be extended for O-RAN use cases) shall be appropriately aggregated by cell, QoS type, slice, etc.

1) Measurement reports with RSRP/RSRQ/CQI information for serving and neighboring cells. In multi-access scenarios this will also include intra-RAT and inter-RAT measurement reports, cell quality thresholds, CGI reports and measurement gaps on per-UE or per-frequency.

2) UE connection and mobility/handover statistics with indication of successful and failed handovers, etc.   
3) Cell load statistics such as information in the form of number of active users or connections, number of scheduled   
active users per TTI, PRB utilization, and CCE utilization.   
4) Per user performance statistics such as PDCP throughput, RLC or MAC layer latency, etc.   
5) UE level measurements useful in calculating UE location, such as RRC and timing advance measurements.

# 4.6 Massive MIMO optimization

This use case provides the motivation, description, and requirements for Non-RT and Near-RT loop massive MIMO beamforming optimization use case. Massive MIMO system configuration can allow operators to optimize the network performance and QoS by e.g. Non-RT and Near-RT loop balancing cell loads or reducing inter-cell interference and control electromagnetic (EM) emissions.

# 4.6.1 Background and goal of the use case

# 4.6.1.1 Common aspects & background of all Massive MIMO optimization use cases

Massive MIMO (mMIMO) is among the key levers to increase performance and QoS in 5G networks. Capacity enhancement is obtained by means of beamforming of the transmitted signals, and by spatially multiplexing data streams for both single user (SU) and for multi-user (MU) MIMO. Beamforming increases the received signal power, while decreasing the interference generated on other users, hence resulting in higher SINR and user throughputs. Beamforming can be codebook based (mainly for FDD), or non-codebook based (TDD). Grid of Beams (GoB) with the corresponding beam sweeping has been introduced to allow beamforming the control channels used during initial access, mainly for high frequency (but can be used also for the sub-6 GHz band) MIMO operation. The codebook and the GoB define the span of the beams, namely the horizontal and vertical aperture in which beamforming is supported, and therefore the coverage area and the shape of the cell. Massive MIMO can be deployed in 5G macro-cells as well as in heterogeneous network, where macro-cells and 3D-MIMO small cells co-exist and complement each other for better aggregated capacity and coverage. In order to obtain an optimal beamforming and cell resources (Tx power, PRB) configuration, one will have to look at a multi-cell environment instead of a single cell. Moreover, different vendors can have different implementations in terms of the number of beams, the horizontal/vertical beam widths, azimuth and elevation range, to achieve the desired coverage. In a multi-node/multi-vendor scenario, centralized monitoring and control is required to offer optimal coverage, capacity and mobility performance as well as control over EM emissions in order to comply with regulatory requirements. Additionally, the number of such combinations of adjustable parameters is in the thousands, hence it is prohibitive for the traditional human expert system to work out the optimal configuration, and a new method is in need.

State of the art solutions suffer from the following problems:

mMIMO macro- and small-cells benefit from a flexible way of serving users in their coverage area thanks to beamforming. However, the coverage area itself is defined by (vendor specific) fixed mMIMO system parameters such as the azimuth and elevation angle range, or the GoB parameters. Hence due to user and traffic distribution and terrain topology, the mMIMO cell can suffer from e.g.

1) 2) High inter-cell interference Unbalanced traffic between neighboring cells 3) Low performance of cell edge users 4) Poor handover performance

Moreover, load balancing functions can be activated in the network nodes, e.g. gNB adapting mobility parameters in order to distribute load between the beams of the neighbor cells, relying on load information exchange over network interfaces. This approach however is partly limited by the cell footprint statically fixed at the initial configuration.

The objective of this use case is to allow the operator to flexibly configure a mMIMO system parameters by means of policies and configuration assisted by machine learning techniques, according to objectives defined by the operator.

# 4.6.1.2 NR cell shaping optimization

Traditionally network coverage in a cellular network is defined by the coverage provided by the union of all the cells in the network. The individual coverage of a cell is determined by aspects including frequency band, radio emission power, orientation and tilt of the antenna, etc. The coverage of a given radio site would include one or multiple cells or sectors, and the coverage if each of these cells/ sectors is relatively static in nature.

One of the challenges for operators in deployment their networks is maximizing the efficiency of the spectrum deployed. Because spectrum is both very scarce and expensive, enhancing this efficiency can significantly help improve the operations and business for the wireless network operator.

As the traffic profile evolves during the day and driven by special circumstances and events, it has become necessary to have the ability to dynamically modify the shapes of the cells to tune the cell coverage to the evolving traffic needs.

The shape of the cell corresponds to the shape of the coverage provided by the sector carrier.

NR cell shaping is designed for FDD or for TDD mid-band deployments. It allows the adjustment of cell footprint by adjusting by configuring the vertical and horizontal coverage width of the common beam into combinations to describe a valid supported shape as driven by O-RU capabilities and then refined through further adjustments with the tilt. The data beams, which carry user traffic, are impacted the serving cell shape changes from the cell shaping optimization. The configurable cell shape allows for coverage control, interference reduction, and better power utilization. However, with the increased optimization comes the challenge of more complexity.

NR cell shaping optimizes cell shaping via different configuration of RET and digital tilt. The optimization leverages algorithms to consider the network configuration and conditions in both the acting and the neighbour cells. The benefits from NR cell shaping include:

Dynamic, adaptation of the network changes and traffic distribution with beam width optimization. Reduction and/or improvements of interference to optimize quality and cell overlapping. Intra-frequency load balancing. • The ability to execute different policies according to operator needs.

# 4.6.2 Entities/resources involved in the use case

# 4.6.2.1 Non-RT massive MIMO GoB beam forming optimization

1) Non-RT RIC:

a) Retrieve necessary configurations, performance indicators, measurement reports, user activity information and other data from SMO and RAN directly for the purpose of constructing/training relevant AI/ML models that will be deployed in Non-RT RIC to assist in the massive MIMO optimization function.   
b) Retrieve necessary user location related information, e.g., GPS coordinates, from the application layer for the purpose of constructing/training relevant AI/ML models.   
c) Use the trained AI/ML model to infer the user distribution and traffic distribution of multiple cells and predict the optimal configuration of massive MIMO parameters for each cell/beam according to a global optimization objective designed by the operator. The massive MIMO configurable parameters includes horizontal beam width, vertical beam width, beam azimuth and downtilt, maximum and average transmitted power per beam/direction as specified in 3GPP TS 28.541 [5].   
d) Send the optimal beam pattern configuration to SMO configuration components.   
e) Retrain the AI/ML model and re-optimize the beam pattern configurations based on the monitored performance.   
f) Execute the control loop periodically or event-triggered.

2) SMO:

a) Collect the necessary configurations, performance indicators, and measurement reports data from RAN nodes triggered by Non-RT RIC if required.   
b) Configure the optimized beam parameters via O1 interface.   
c) Monitor the performance of all the cells; when the optimization objective fails, initiate fall-back procedure; meanwhile, trigger the AI/ML model re-training, data analytics and optimization in Non-RT RIC.

3) E2 nodes:

a) Collect and report to SMO and/or to Near-RT RIC KPI related to user activity, traffic load, coverage and QoS performance, per beam/area, handover, and beam failures statistics. b) Collect and report to SMO and/or to Near-RT RIC information about beam and resource utilization. c) Apply beam management strategies following SMO and Near-RT RIC configuration and constraints.

# 4.6.2.2 Near-RT beam-based mobility robustness optimization

1) SMO:

a) Trigger bMRO configuration. (O)   
b) Send bMRO configuration target to Near-RT RIC.   
c) Send GoB beam pattern related information (beam pattern configuration, beam pattern configuration list, beam pattern configuration switch timing/condition, beam pattern identifier etc.) to the Near-RT RIC.

2) Near-RT RIC:

a) Retrieve necessary configurations, performance indicators, measurement reports and other data from E2 nodes for the purpose of training of relevant AI/ML models.   
b) Use the trained AI/ML models to infer the correlation between the Grid-of-Beam configuration, handover, and beam failure statistics of multiple cells and beams, and to predict the optimal configuration of mobility parameters (e.g., beam individual offsets for beam mobility) for each cell/beam pair optionally according to a global optimization objective designed by the operator and retrieved from the SMO.   
c) Send the optimal beam mobility parameter configurations to E2 nodes as specified in 3GPP TS 28.541 [5].   
d) Monitor the performance of the AI/ML model based on configurations, performance indicators, and measurement reports received from the RAN.   
e) Retrain the AI/ML model and re-optimize the beam mobility configurations based on the monitored performance and/or based on a switch of the Grid-of-Beam configuration.   
f) Execute the control loop periodically or event triggered.   
g) Retrieve GoB beam pattern related information from the SMO.

3) E2 nodes:

a) Collect and report to Near-RT RIC KPIs related to Grid-of-Beam configuration, handover, and beam failure statistics.   
b) Apply L3 beam mobility parameter configuration following Near-RT RIC configuration as specified in 3GPP TS 28.541 [5].   
c) Send GoB beam pattern related information to the Near-RT RIC.

# 4.6.2.3 NR cell shaping optimization

1) SMO:

a. Collect the necessary configurations, performance indicators, and measurement reports data from RAN nodes triggered by Non-RT RIC as required.   
b. Configure the optimized cell shape per cell level for MIMO beam parameters and tilt via the O1 interface.   
c. Monitor the performance of all the cells to determine when to trigger for new data analytics and optimization in Non-RT RIC.

2) Non-RT RIC & rApp:

a. Retrieve necessary performance, configuration, and other data for defining and updating cel shaping policy. b. rApp provides the target optimal pattern settings and configuration to create an optimal cell shape characteristics to be applied to the SMO configuration, as to be applied by the RAN.

3) RAN:

a. Collect and report to SMO KPIs and PMs related to user activity, evolution of radio conditions, traffic load, coverage and QoS performance, per cell/beam/areas. b. Collect and report to SMO information and statistics about beam and resource utilization. c. Apply beam management strategies following SMO configuration instructions and constraints.

# 4.6.3 Solutions

# 4.6.3.1 Non-RT massive MIMO GoB beam forming optimization

The context of the massive MIMO beamforming optimization is captured in table 4.6.3.1-1.

Table 4.6.3.1-1: Massive MIMO GoB beam forming optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable flexible optimization of the multi-cell M-MiMO beamformingperformance (capacity and coverage) by means of configurationparameter change with operator-defined objectives and allow for Al/ML-based solutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC acting as massive MIMO beamforming configurationoptimization decision making function.SMO acting as the RAN data collection and parameter configurationfunction.RAN acting as configuration enforcement function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O1 interface connectivity is established between RAN and SMO.Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">SMO has processed the collected data and Non-RT RIC has access tothis data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">If required, SMO can initiate the specific measurement data collectionrequest towards RAN for Al/ML model training or to assess the outcomeof the applied configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC retrieve the data from SMO components and trains theAl/ML model with the collected data from the application, the RANnodes. Trained Al/ML models are deployed and inferenced for long-termconfiguration parameters optimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Upon trigger from Non-RT RIC with the optimized beam parameters,SMO configures the parameters towards the RAN via O1 interface. Therelevant parameters can include:a) horizontal beam width, vertical beam width, beam azimuth anddowntiltb) maximum and average transmitted power per beam/direction</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">SMO monitors the network performance. If the algorithm performance isunsatisfactory in terms of predefined objective/requirement, SMO initiates fallback mechanism to restore previous configuration.Ilt can also</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">gather necessary information and data to retrain and update the AI/MLmodel or trigger the optimization in Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1">[</td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The RAN operates using the newly deployed parameters/models.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the massive MIMO beamforming optimization is given in figure 4.6.3.1-1.

![](images/62d42e13cd2c056dc5d55bed7d995c1a82348e7947710ca063a6b8662e07fa8b.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.6.3.1-1: Massive MIMO beamforming optimization flow diagram

4.6.3.2 Near-RT massive MIMO beam-based mobility robustness optimization

The context of the massive MIMO beam-based mobility robustness optimization is captured in table 4.6.3.2-1.

Table 4.6.3.2-1: Beam-based mobility robustness optimization

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Enable flexible optimization of the beam-based mobility robustnessoptimization by means of configuration parameter change with operator-defined objectives and allow for Al/ML-based solutions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Near-RT RIC acting as bMRO function, data collection function, andAI/ML model training function.E2 nodes acting as configuration enforcement function.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>E2 connectivity is established between Near-RT RIC and E2 nodes. O1connectivity is established between Near-RT RIC and SMO. Network isoperational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>Active Grid-of-Beams beam pattern is defined.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Operator specified trigger condition is set or event is detected orperiodically.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Near-RT RIC collects necessary data from E2 nodes and related GoBbeam pattern Information and trains the Al/ML model with the collecteddata.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Trained Al/ML models are executed in Near-RT RIC and infer forconfiguration parameter optimization based on the operator target.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Continuously or upon trigger (e.g., change in the mMIMO beam patternconfiguration, manual trigger etc.), Near-RT RIC configures optimizedparameters in E2 nodes (e.g., bClO-s).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Near-RT RIC monitors the network performance. If the algorithmperformance  iscYaYnannacterywin  termsofpredefinedobjective/requirement, Near-RT RIC initiates fallback mechanism torestore previous/default configuration. It can also gather necessary information and data to retrain and update the AlI/ML model or trigger theoptimization.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Operator specified trigger condition or event is satisfied.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>The E2 Nodes operate using the newly deployed parameters.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the massive MIMO beam-based mobility robustness optimization is given in figure 4.6.3.2-1.

![](images/f71f6dd243e4096227711c2c0080e3cf0b9d2b4fdf4d058f5f6f5d159849958e.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.6.3.2-1: Massive MIMO beam-based mobility robustness optimization flow diagram

One of the necessary inputs for training and inference of the bMRO function is the (current) GoB beam pattern (or alternative beam pattern) that is determined externally (in the SMO, in the Non-RT RIC, in the E2 nodes, or in the NearRT RIC by another function). The relevant GoB beam pattern information shall be made available to the Near-RT RIC bMRO function both for training and inference. Depending on implementation, this can be achieved by transmission from the SMO (over O1), or by transmission from the E2 nodes (over E2), or by combined transmission from the SMO and the E2 nodes (or by communication between two Near-RT RIC functions). Moreover, depending how the relevant GoB beam pattern information is defined, the necessary information can be even transmitted separately and asynchronously (e.g., SMO transmits a list of GoB beam patterns for the next, longer time period, while the E2 nodes transmit the exact times of beam pattern change and indicate the ID of the beam pattern in the list).

# 4.6.3.3 NR cell shaping optimization

The context for the cell shaping optimization use case is captured in table 4.6.3.3-1.

Table 4.6.3.3-1: Cell shaping optimization   

<table><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Detect optimization opportunities for cell shape optimizations and apply newconfiguration settings to ensure the optimization cells shapes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">SMO, Non-RT RIC, O-RAN NFs, rApp</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated, and O1, R1, OFH interfaceconnectivity is in place.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational.SMO has processed the collected data, and Non-RT RIC has access to this data.O1 is established between the SMO and RAN Nodes. Non-RT RIC monitors the performance by collecting the relevant performance events and counters from O-RANnodes from SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Network is in normal operational state, providing regular PM and KPI reports.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step1 (M)</td><td colspan="1" rowspan="1">Network provides regular interval performance measurements, and in one such reportthere are criteria to optimize the shape of the cells.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">Alternate scenario 1 – Automated intervention: Triggering for new cell shape to beapplied triggered automatically based on network criteria and performancemeasurements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Alternate scenario 2 – Manual Intervention: Triggering for new cellshape to be applied is triggered by manual operator / radio planning intervention.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Once criteria have been triggered field data is provided to the rApp via the Non-RTRIC to determine what new settings to set.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Applicable field inputs are provided to rApp as inputs for the optimization logic to apply.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Based on rApp logic, new configuration settings for cellshape are provided.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">The new settings are made available to the SMO for communication to the RAN.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8-12 (M)</td><td colspan="1" rowspan="1">The SMO communicates the new O1 settings to the O-DU and O-RU as driven byhybrid or hierarchical management options - via O1 and M-plane.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified or rApp trigger changes and event are satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PostConditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr></table>

<table><tr><td>@startuml</td></tr><tr><td>skin rose</td></tr><tr><td>skinparam ParticipantPadding 5</td></tr><tr><td>skinparam BoxPadding 10</td></tr><tr><td>skinparam defaultFontsize 14</td></tr><tr><td>autonumber</td></tr><tr><td>Box &quot;operator Personnel&quot; #Lightcyan</td></tr><tr><td>Actor planner as &quot;Planner&quot;</td></tr><tr><td>End box</td></tr><tr><td>Box &quot;sMO Framework&quot; #gold</td></tr><tr><td>participant smo as &quot;smo&quot;</td></tr><tr><td>participant non_RT_RIC</td></tr><tr><td>participant rApp</td></tr><tr><td>End box</td></tr><tr><td>Box &quot;RAN&quot; #lightpink</td></tr><tr><td>participant odu as &quot;o-Du&quot;</td></tr><tr><td>participant oru as &quot;o-Ru&quot;</td></tr><tr><td>End box</td></tr><tr><td>== START - Triggering Optimization ==</td></tr><tr><td>Note over smo</td></tr></table>

Criteria triggered for cell shaper optimization. Two scenarios:   
1 - automated based on observed network conditions 2 - manual, driven by radio planning   
End note

$= = = = = = =$ Scenario 1 - Automated $= =$ odu $- >$ smo: O1 - Notify SMO criteria triggered $= = = = = = =$ Scenario 2 - Operator intervention $= =$ planner $- >$ smo: Notify SMO to apply new cell shaper settings $= = = = = = =$ Common flow $= =$ smo $- >$ non_RT_RIC: Data retrieval - pms, metrics non_RT_RIC-> rApp: R1 - Criteria triggered for rApp

$= =$ Apply rApp logic $= =$

Note over rApp   
Apply logic to   
re-configure   
to target cell shape   
End note

rApp -> non_RT_RIC: R1 - Provide new configuration settings to RAN $= =$ Setup new configuration for cell shaper $= =$ non_RT_RIC-> smo: Provide new configuration settings to apply smo $- >$ odu: O1 - Provide new configuration settings to ODU odu $- >$ oru: OFH - Provide new configuration settings to ORU

@enduml

The flow diagram of the cell shaping optimization is given in figure 4.6.3.3-1.

![](images/d9dc245e1f25a74ce182370db768a292377f4fe47ede4870c8baf2be30c927f0.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.6.3.3-1: Cell shaping optimization flow diagram

# 4.6.4 Required data

# 4.6.4.1 Non-RT massive MIMO GoB beam forming optimization

There are different types of data that are required from different parts of the network, and the following list summarizes with some examples:

1) Environment data: Cell site information (location), inter-site distance, BS system configuration, (e.g. operating frequency, bandwidth, frame structure, transmit power, default beam weight configuration); complete set of massive MIMO configurations, i.e., horizontal beamwidth adjustable range, vertical beamwidth adjustable range, azimuth angle adjustable range, elevation angle adjustable range.

2) From RAN to SMO and/or Near-RT RIC

a) Measurement reports with RSRP/RSRQ/CQI/SINR per beam information for the UEs in cells of interest; the time granularity of data collection shall be configurable and satisfy the requirement of the AI/ML model.   
b) Network KPIs: e.g., cell downlink/uplink traffic load, RRC connection attempts, average RRC connected UE, maximum RRC connected UE, average active connections (downlink/uplink), DL/UL throughput, DL/UL spectral efficiency, NI (Noise Interference); beam resource usage (transmitted power per beam/directions and associated PRB usage), beam based handover and beam failure statistics

3) From application to SMO

a) User location related information, e.g., GPS coordinates for the purpose of constructing/training relevant AI/ML models.

# 4.6.4.2 Near-RT massive MIMO beam-based mobility robustness optimization

1) Beam-specific handover related KPMs, as specified in 3GPP TS 28.552 [6] and in 3GPP TS 28.622 [8] from E2 nodes, similar to:

a) Too early handovers   
b) Too late handovers   
c) Attempted handovers   
d) Successful handovers   
e) Failed handovers   
f) The time granularity is an integer multiple of 1 second as specified in 3GPP TS 28.622 [8].

2) The beam pattern information supplied externally is not defined in the present document.

# 4.6.4.3 NR cell shaping optimization

Table 4.6.4.3-1: Cell shaping optimization data requirements

<table><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">ApplicableInterface</td><td colspan="1" rowspan="1">Reference</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.001</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Node Id: Nodelidentification</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clause 4.3.1, gnbld +gnbDUId</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.002</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Sector Id: Sectoridentification</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.003</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Cell ld: Cellidentification</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clauses 4.3.1, 4.3.5,gnbld + cellLocalld</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.004</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna Latitude</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.005</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna Longitude</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.006</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna Azimuth(direction)</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.007</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna Elevation(Height)</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">3GPP TS 28.662 [41],clause 4.3.2</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.008</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna – RemoteElectrical Tilt subunitmapping</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.009</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Antenna – RemoteElectrical Tilt subunitmapping</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">FH MP</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [28],clause 14.4.2</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.010</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Remote ElectricalTilt per antenna</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">3GPP TS 28.662 [41],clause 4.3.2,retTiltValue</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.011</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Remote ElectricalTit per antenna</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">FH MP</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [28],clause 14.4.3 andAISG specifications</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.012</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Digital tilt perantenna</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.013</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Digital tilt perantenna</td><td colspan="1" rowspan="1">O-DU/O-RU</td><td colspan="1" rowspan="1">FH MP</td><td colspan="1" rowspan="1">O-RAN.WG4.MP [28],clause 14.4.3 andAISG specifications</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.014</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Broadcast andCellular Broadcast(BCB) per cell level</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clause 4.3.1, gnbld +gnbDUId</td></tr><tr><td colspan="1" rowspan="1">Req-4.6.015</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Horizontal coveragewidth</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.016</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Horizontal coveragewidth</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">FH MP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.017</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Vertical coveragewidth</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.018</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Vertical coveragewidth</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">FH MP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.6.019</td><td colspan="1" rowspan="1">Network ConfigurationManagement</td><td colspan="1" rowspan="1">Supported coveragecombinations ofvertical / horizontaloptions (radiospecific capabilities)</td><td colspan="1" rowspan="1">O-RU</td><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1"></td></tr><tr><td rowspan="2">Req-4.6.020</td><td rowspan="2">Network Configuration Management</td><td rowspan="2">Supported coverage combinations of vertical / horizontal</td><td rowspan="2">O-RU</td><td rowspan="2">FH MP</td><td rowspan="2"></td></tr><tr><td>options (radio</td></tr></table>

# 4.7 RAN sharing

This use case provides the motivation, description, and requirements for RAN sharing use case. The goal of this use case is to enable multiple operators to share the same O-RAN infrastructure, while allowing them to remotely configure and control the shared resources via a remote O1, O2 and E2 interface.

# 4.7.1 Background and goal of the use case

RAN sharing is envisioned as an efficient and sustainable way to reduce the network deployment costs, while increasing network capacity and coverage. Among the different RAN sharing models that have been experimented so far, a special focus is put here on the evaluation of the compatibility of the “geographical split” RAN sharing model with the O-RAN architecture. In such a model, a coverage area is split between two or more operators; each operator manages the RAN in a specific area, while sharing its RAN infrastructure and computing resources with its partner operators.

Specifically, this use case analyzes the Multi-Operator RAN (MORAN) sharing scenario, wherein each operator utilizes a separate carrier in order to achieve more freedom and independency on the control of the radio resources. Accordingly, the goal of this use case is to propose a sharing-compliant O-RAN architecture that lets operators to configure the shared network resources independently from configuration and operating strategies of the other sharing operators. Specifically, it is proposed that a home operator (operator A) makes available its O-RAN infrastructure and computing resources to host the Virtual RAN Functions (VNF) of a second operator (operator B), allowing it to configure and control such remote VNFs via a remote O1, O2 and E2 interface.

![](images/ddde47a337c2eaecbf3bf60223fcb4aad08f34562766fdfaa6da3e273db0d770.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.7.1-1: MORAN use case in O-RAN

The logic architecture of the proposed MORAN use case is shown in figure 4.7.1-1. It is assumed that operator A owns the site A and shares the PHY layer (LOW) with operator B (Shared O-RU). Indeed, multiple PLMN IDs are broadcasted, while each operator operates in a different carrier. Moreover, the computing resources of the site A are shared among multiple VNFs, belonging to operator A and operator B, respectively.

Each VNF represents a logic implementation of the O-DU and O-CU functionalities and is controlled by each partner operator in an independent manner. While operator A can directly orchestrate and configure its VNFs, operator B needs to control its VNFs in a remoted manner. The challenge here is to enable operator B to configure and control resources in an infrastructure that is owned by another operator.

Accordingly, it is assumed that operator B can monitor and control the remote radio resources via the RIC node of site B, using an “E2 remote” interface. Note that in the proposed architecture, the RIC nodes are not shared and kept independent at the site A and B respectively.

However, it is assumed that operator B cannot directly orchestrate its VNFs in site A, but it is allowed to communicate the desired initial VNF configuration via an extended O1, O2 interface, hereafter referred to as “O1, $\mathrm { O } 2 + \mathrm { S L A } ^ { \prime \prime }$ interface (O1, O2 remote). Note that the O1, O2 nomenclature is used hereafter to refer to both O1 and O2 messages.

The “O1, O2 remote” interface is connected to a specific “sharing orchestration application”, referred to as “SMO-sharing App”, that is located at the Service Management & Orchestration Framework of each operator. Specifically, the “SMOsharing App” at site A acts as an SLA (Service Level Agreement) monitoring and filter entity: it checks that O1, O2 requests coming from operator B are in line with a predefined SLA and finally configures the VNF of operator B, according to the initial O1, O2 request.

# 4.7.2 Entities/resources involved in the use case

1) SMO-sharing App (site A):

a) SLA monitoring: checks that orchestration/management requests sent by operator B are in line with the SLA.   
b) Remote provisioning and initial VNF deployment: asks the IMF to instantiate the VNFs for operator B.   
c) Remote management operations via “O1, O2 remote”: configures the VNF of operator B via the Orchestrator, according to “O1, O2 remote” requests sent by operator B.   
d) Forwards RAN related data, collected from the hosted VNFs, to the SMO-sharing App (site B) over the “O1, O2 remote” interface.

2) SMO-sharing App (site B):

a) Detects the “SMO-sharing App” in site A towards which to forward “O1, O2 remote” requests.   
b) Sends “O1, O2 remote” commands for initial deployment and configuration of remote VNFs.   
c) Forwards RAN related data of operator B, collected in site A, to the Non-RT RIC.

3) IMF (site A): creates VNFs for operator B in site A on initial request of the SMO-sharing App (site A).

4) RAN (site A):

a) Supports data collection from the hosted VNFs with radio state report over “E2 remote” interface.   
b) Supports data collection from hosted VNFs with UE KPI report over “O1, O2 remote” interface.

5) Non-RT RIC (site B):

a) Configures the initial network policy template, e.g., default scheduling policy, of the remote VNFs. b) Elaborates RAN data collected by “SMO-sharing App”, e.g., scheduling performance metrics, and sends A1 policy/intentions to the remote virtual O-DU/O-CU (VNF_B) via the Near-RT RIC.

6) Near-RT RIC (site B):

a) Monitors and collects E2-related parameters from the remote VNFs.   
b) Detects the “E2 remote” interface towards the VNFs hosted in site A.

# 4.7.3 Solutions

# 4.7.3.1 RAN sharing

The context of the RAN sharing use case is captured in table 4.7.3.1-1.

Table 4.7.3.1-1: RAN sharing use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable two operators to share the same O-RAN infrastructure, while allowingthem to remotely configure and control the shared resources via a remote "O1",“O2”and “E2" interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Sharing-SMO App handles remote orchestration operations via "O1, O2 remote"interface. Non-RT RIC (operator B): updates configuration of VNFs hosted insite A. Near-RT RIC (operator B): execute remote E2 commands via “E2remote" interface. RAN (site A): collects and reports RAN statistics to the RICof operator B (RIC_B) for its VNFs hosted in site A.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1, O1, O2, E2 interface connectivity is established with local SMO, Non-RTRIC and Near-RT RIC, respectively."O1, O2 remote"and “E2 remote"end-to-end connectivity is established withremote SMO and remote Near-RT RIC, respectively. The remote interfaceshave been secured through appropriate end-to-end security mechanisms(security configuration details are out of scope of this use case).Non-RT RIC_B and Near-RT RIC_B are aware of the presence of O-DU_B andO-CU_B in the site A. Near-RT RIC_B is aware of the “E2 remote" interface, tobe used to control the remote VNFs hosted in site A.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">An SLA sharing agreement is established between the home (operator A) andhost operator (operator B). The SLA defines the amount of physical resources(CPU, memory, etc.), that can be allocated to the host operator and the type ofadmissible orchestration operations that can be remotely executed by the hostoperator. Such SLA is translated in appropriate SLA monitoring-check controlsto be executed by the SMO-sharing App.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Phase 1-2: Host operator (operator B) asks to provision and instantiate an O-DU_B and O-CU_B in the site of the home operator (operator A).Phase 3: Host operator wants to send a new instruction to the shared RAN overthe“E2 remote" interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">SMO-sharing App_B sends a request to SMO-sharing App_A for provisioningand deploying a remote virtual O-DU_B and O-CU_B in the site A.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">SMO-sharing App_A checks that the request is in line with the predefined SLAand ask the IMF (via the Orchestrator) to instantiate the VNFs for the O-CU_Band O-DU_B.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">IMF creates VNF for operator B in site A as for the request of the SMO-sharingApP_A.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">SMO-sharing App_B notifies SMO-sharing App_A the request to installa defaultnetwork policy template, e.g., RB scheduling policy, in the remote VNFs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">SMO-sharing App_A checks that operator B request is in line with the SLA andconfigures (via the Orchestrator) the O-DU_B/ O-CU_B via an O1 configurationcommand.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">RAN related data from VNF_B in site A are collected at SMO Collector andforwarded to the SMO-sharing App_A, which in turns forwards them to the Non-RT RIC_B, via the SMO-sharing App_B.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7</td><td colspan="1" rowspan="1">Non-RT RIC_B decides to update the default network policy of the remoteVNFs, e.g., scheduling policy of O-DU_B/O-CU_B and sends an A1 updatepolicy request to the Near-RT RIC_B.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8</td><td colspan="1" rowspan="1">Near-RT RIC_B configures the remote O-DU_B/O-CU_B accordingly, over the"E2 remote" interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The VNFs of operator B in site A are instantiated with success and no update-requests are sent by the host operator (operator B).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">RIC of operator B monitors relevant radio KPI from the remote O-CU_ B and O-DU_B and decides to reconfigure the scheduling policy as for Step 7.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the VNF configuration procedure for VNF_B hosted in site A is given in figure 4.7.3.1-1.

![](images/0320c918367854345707878a04d893e9535fae21697319c1430950681591eb46.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.7.3.1-1: VNF configuration procedure for VNF_B hosted in site A

# 4.7.4 Required data

Multi-dimensional data are expected to be handled by the SMO-sharing App:

1) SLA data needs to be converted in a set of condition steps to be matched for each request of the host operator (operator B). 2) SMO needs to handle O1, O2 messages sent by the host operator, converting them in local O1, O2 commands.

The RAN of the home operator needs to report to the RIC_B the network state of the served UEs that belong to the host operator.

# 4.8 QoS based resource optimization

This use case provides the background and motivation for the O-RAN architecture to support RAN QoS based resource optimization. Moreover, some high-level description and requirements over Non-RT RIC and A1 interfaces are introduced.

# 4.8.1 Background and goal of the use case

QoS based resource optimization can be used when the network has been configured to provide some kind of preferential QoS for certain users. One such scenario can be related to when the network has been configured to support e2e slices. In this case, the network has functionality that ensures resource isolation between slices as well as functionality to monitor that slice Service Level Specifications (SLS) are fulfilled.

In RAN, it is the scheduler that ensures that Physical Resource Block (PRB) resources are isolated between slices in the best possible way and also that the PRB resources are used in an optimal way to best fulfill the SLS for different slices. The desired default RAN behavior for slices is configured over O1. For example, the ratio of physical resources (PRBs) reserved for a slice is configured at slice creation (instantiation) over O1. Also, QoS can be configured to guide the RAN scheduler how to (in real-time) allocate PRB resources to different users to best fulfill the SLS of a specific slice. In the NR NRM this is described by the resource partition attribute.

Instantiation of a RAN sub-slice will be prepared by rigorous planning to understand to what extent deployed RAN resources will be able to support RAN sub-slice SLS. Part of this procedure is to configure RAN functionality according to above. With this, a default behavior of RAN is obtained that will be able to fulfill slice SLSs for most situations. However, even through rigorous planning, there will be times and places where the RAN resources are not enough to fulfill SLS given the default configuration. To understand how often (and where) this happens, the performance of a RAN slice will continuously be monitored by SMO. When SMO detects a situation when RAN SLS cannot be fulfilled, NonRT RIC can use A1 policies to improve the situation. To understand how to utilize A1 policies and how to resolve the situation, the Non-RT RIC will use additional information available in SMO.

Take an emergency service as an example of a slice tenant. For this example, it is understood (at slice instantiation) that $50 \%$ of the PRBs in an area can be enough to support the emergency traffic under normal circumstances. Therefore, the ratio of PRBs for the emergency users is configured to $50 \%$ as default behavior for the pre-defined group of users belonging to the emergency slice. Also, QoS is also configured in CN and RAN so that video cameras of emergency users get a minimum bitrate of 500 kbps.

Now, suppose a large fire is ongoing and emergency users are on duty. Some of the personnel capture the fire on video on site. The video streams are available to the emergency control command. Because of the high traffic demand in the area from several emergency users (belonging to the same slice), the resources available for the emergency slice is not enough to support all the traffic. In this situation, the operator has several possibilities to mitigate the situation. Depending on SLAs towards the emergency slice compared to SLAs for other slices, the operator could reconfigure the amount of PRB reserved to emergency slice at the expense of other slices. However, there is always a risk that emergency video quality is not good enough irrespective if all resources are used for emergency users. It might be that no video shows sufficient resolution due to resource limitations around the emergency site.

In this situation, the emergency control command decides, based on the video content, to focus on a selected video stream to improve the resolution. The emergency control system gives the information about which users to up- and downprioritized to the e2e slice assurance function (through e.g. an Edge API) of the mobile network to increase bandwidth for selected video stream(s). Given this additional information, the Non-RT RIC can influence how RAN resources are allocated to different users through a QoS target statement in an A1 policy. By good usage of the A1 policy, the emergency control command can ensure that dynamically defined group of UEs provides the video resolution that is needed.

# 4.8.2 Entities/resources involved in the use case

# 1) Non-RT RIC:

a) Monitor necessary QoS related metrics from network function and other SMO functions.

b) Send policies to Near-RT RIC to drive QoS based resource optimization at RAN level in terms of expected behavior.

2) Near-RT RIC:

a) Support interpretation and execution of A1 policies for QoS based resource optimization.

3) RAN:

a) Support network state and UE performance report with required granularity to SMO over O1 interface.   
b) Support QoS enforcement based on messages from E2, which are expected to influence RRM behavior.

# 4.8.3 Solutions

# 4.8.3.1 QoS based resource optimization

he context of the QoS based resource optimization is captured in table 4.8.3.1-1.

Table 4.8.3.1-1: QoS based resource optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Drive QoS based resource optimization in RAN in accordance with definedpolicies and configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: Creates A1 policies.Near-RT RIC: Enforces A1 policies.RAN: Policy enforcement.SMO: Termination point for O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated and configuredaccording wanted default behavior.A1 interface connectivity is established with Non-RT RIC.O1 interface connectivity is established with SMO.The default configuration will handle most situations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational with default configuration.SMO has established the data collection and sharing process, and Non-RT RIChas access to this data.Non-RT RIC analyzes the data from RAN to understand the current resourceconsumption.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Non-RT RIC observes that resources are close to congestion in a certain area.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">If needed, Non-RT RIC orders additional RAN observability, SMO configuresadditional observability over 01.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2</td><td colspan="1" rowspan="1">Non-RT RIC evaluates RAN resource utilization for all users in a slice in specificarea.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3</td><td colspan="1" rowspan="1">Non-RT RIC asks for additional information from additional SMO functionality,e.g. e2e slice assurance function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4</td><td colspan="1" rowspan="1">Non-RT RIC determines dynamic group of users for which QoS target shall bechanged.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step5</td><td colspan="1" rowspan="1">Non-RT issues A1 policy/policies with QoS target based on information fromother SMO functionality.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Non-RT RIC (through O1 observability) understands that situation of resourceconstraints within the slice is resolved, and the deployed policies are deletedover A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the QoS based resource optimization is given in figure 4.8.3.1-1.

![](images/57d421acd525d16aeecd2ef80f1a44d0d6ef9d524aa3f8471b8d7071b436afc9.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.8.3.1-1: QoS based resource optimization flow diagram

# 4.8.4 Required data

For this use case, different kind of observability need to be reported to Non-RT RIC. First Non-RT RIC shall monitor resource consumption in the area. As long as resource consumption is low, the RAN scheduler will be able to give all users in an area the needed resources. When resource consumption in an area increases above a threshold, the risk of that the default configuration of RAN will not be enough to fulfil the requirements. At this point, the Non-RT RIC need to be able to configure more detailed reporting for individual UEs that the Non-RT RIC is interested in. This detailed observability shall provide the Non-RT RIC better insight in performance for specific users and therefore includes observability of e.g., user throughput and delay. With this more detailed observability, the Non-RT RIC can understand when pre-configured priorities are not enough for the scheduler to solve the problem and when additional (non-RAN) information to solve the prioritization is needed.

# 4.9 RAN slice SLA assurance

The 3GPP standards architected a sliceable 5G infrastructure which allows creation and management of customized networks to meet specific service requirements that can be demanded by future applications, services, and business verticals. Such a flexible architecture needs different requirements to be specified in terms of functionality, performance and group of users which can greatly vary from one service to the other. The 5G standardization efforts have gone into defining specific slices and their Service Level Agreements (SLAs) based on application/service type as specified in 3GPP TS 23.501 [2]. Since network slicing is conceived to be an end-to-end feature that includes the core network, the transport network and the Radio Access Network (RAN), these requirements shall be met at any slice subnet during the life-time of a network slice as specified in 3GPP TS 28.530 [4], especially in RAN side. Exemplary slice performance requirements are specified in terms of throughput, energy efficiency, latency, and reliability at a high level in SDOs such as 3GPP TS 22.261 [1] and GSMA NG.116 [17]. These requirements are defined as a reference for SLA/contractual agreements for each slice, which individually need proper handling in NG-RAN.

Although network slicing support is started to be defined with 3GPP Release 15, slice assurance mechanisms in RAN needs to be further addressed to achieve deployable network slicing in an open RAN environment. It is necessary to assure the SLAs by dynamically controlling slice configurations based on slice specific performance information. Existing RAN performance measurements as specified in 3GPP TS 28.552 [6] and information model definitions as specified in 3GPP TS 28.541 [5] are not enough to support RAN slice SLA assurance use cases. This use case is intended to clarify necessary mechanisms and parameters for RAN slice SLA assurance.

# 4.9.1 Background and goal of the use case

In the 5G era, network slicing is a prominent feature which provides end-to-end connectivity and data processing tailored to specific business requirements. These requirements include customizable network capabilities such as the support of very high data rates, traffic densities, service availability and very low latency. According to 5G standardization efforts, the 5G system can support the needs of the business through the specification of several service needs such as data rate, traffic capacity, user density, latency, reliability, and availability. These capabilities are always provided based on a Service Level Agreement (SLA) between the mobile operator and the business customer, which brought up interest for mechanisms to ensure slice SLAs and prevent its possible violations. O-RAN’s open interfaces and AI/ML based architecture will enable such challenging mechanisms to be implemented and help pave the way for operators to realize the opportunities of network slicing in an efficient manner.

# 4.9.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve RAN slice SLA target from respective entities such as SMO, NSSMF   
b) Long term monitoring of RAN slice performance measurements   
c) Training of potential AI/ML models that will be deployed in Non-RT RIC for slow loop optimization and/or Near-RT RIC for fast loop optimization   
d) Support deployment and update of AI/ML models into Near-RT RIC   
e) Receive slice control/slice SLA assurance rApps from SMO   
f) Create A1 policies based on RAN intent A1 feedback   
g) Retrieve UE specific performance reports   
h) Send A1 policies and enrichment information to Near-RT RIC to drive slice assurance   
i) Send O1 reconfiguration requests to SMO for slow-loop slice assurance

2) Near-RT RIC:

a) Near real-time monitoring of slice specific RAN performance measurements b) Support deployment and execution of the AI/ML models from Non-RT RIC

c) Receive slice SLA assurance xApps from SMO   
d) Send UE specific performance reports to SMO/Non-RT RIC   
e) Support interpretation and execution of policies from Non-RT RIC   
f) Perform optimized RAN (E2) actions to achieve RAN slice requirements based on O1 configuration, A1 policy, and E2 reports

3) E2 nodes:

a) Support slice assurance actions such as slice-aware resource allocation, prioritization, etc. b) Support slice specific performance measurements through O1   
c) Support slice specific performance reports through E2

# 4.9.3 Solutions

# 4.9.3.1 Creation and deployment of RAN slice SLA assurance models and control apps

The context of the creation and deployment of RAN slice SLA assurance models and control apps is captured in table 4.9.3.1-1.

Table 4.9.3.1-1: Creation and deployment of RAN slice SLA assurance models and control apps   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Training and distribution of the model, or distribution of control apps.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1, O1 interface connectivity is established.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interface andconnectivity has been established between them.O1 interface has been established between SMO and Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">A RAN slice is activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Non-RT RIC retrieves a RAN slice SLA from SMO (NSSMF).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2a</td><td colspan="1" rowspan="1">Non-RT RIC starts to collect performance measurements (PMs) via O1.Examples of the PMs are CSI, PRB usage, L2 throughput, RAN latency, etc.Applicable PMs are specified in 3GPP TS 28.552 [6].</td><td colspan="1" rowspan="1">Step 2 and 3are mandatoryin case of usingthe Al/MLmodel</td></tr><tr><td colspan="1" rowspan="1">Step 2b (O)</td><td colspan="1" rowspan="1">Non-RT RIC starts to collect Enrichment Information (Els) from externalapplications. Examples of the external applications are public safetyapplication triggering slice priority during an emergency event, or location-based enrichment information, etc.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2c</td><td colspan="1" rowspan="1">Non-RT RIC analyzes collected PMs and/or Els for long term monitoring,such as during the day or over the weekend.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3</td><td colspan="1" rowspan="1">Non-RT RIC does the model training using the collected data in step 2 andobtains RAN slice SLA assurance models.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4a</td><td colspan="1" rowspan="1">In case of using the Al/ML model, Non-RT RIC deploys the trained modelinternall for slow loop optimization and/or distributes it to the Near-RT RICvia O2 for fast loop optimization.</td><td colspan="1" rowspan="1">Step 4a or 4b ismandatory</td></tr><tr><td colspan="1" rowspan="1">Step 4b</td><td colspan="1" rowspan="1">In case of using the control app, the control app is deployed by SMO to Non-RT RIC for slow loop optimization and/or Near-RT RIC via O2 for fast loopoptimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Non-RT RIC receives feedback internally or from Near-RT RIC via A1 toupdate the model or control apps based on it.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">A RAN slice is deactivated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the creation and deployment of RAN slice SLA assurance models and control apps is given in figure 4.9.3.1-1.

![](images/7b990bdb63555b8b023ae87d2b10701e8e97581c782709963be6964b6f425533.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.9.3.1-1: Creation and deployment of RAN slice SLA assurance models and control apps flow diagram

# 4.9.3.2 Slow loop RAN slice SLA optimization

The context of the slow loop RAN slice SLA optimization is captured in table 4.9.3.2-1.

Table 4.9.3.2-1: Slow loop RAN slice SLA optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Slow loop RAN slice SLA optimization</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO, RAN</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1, O1, E2 interface connectivity is established.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.O1 interfaces are established between SMO and Near-RT RIC, and SMOand RAN nodes.RAN slice SLA assurance models or control apps have been deployed inNon-RT RIC and Near-RT RIC respectively.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">A RAN slice is activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1a</td><td colspan="1" rowspan="1">Non-RT RIC decides that RAN shall be reconfigured based on long term trends collected via O1 using PMs and/or Els.Examples of the PMs are layer 2 throughput, PRB usage, CSI, RAN latency.</td><td colspan="1" rowspan="1">Config updatestep 1a or 1b ismandatory</td></tr><tr><td colspan="1" rowspan="1">Step 1b</td><td colspan="1" rowspan="1">Non-RT RIC decides to create slice specific A1 policies based on RAN sliceSLA requirements and/or operator-defined RAN intents, A1 feedback from Near-RT RIC, EI from external app server and O1 based long term trends.The policies include scope identifiers (e.g., S-NSSAl, fow ID, cel ID) and/orpolicy statements (e.g. slice specific KPl targets).</td><td colspan="1" rowspan="1">Policy update</td></tr><tr><td colspan="1" rowspan="1">Step 2a</td><td colspan="1" rowspan="1">The model or control app in Non-RT RIC requests SMO to update sliceconfiguration of Near-RT RIC and/or RAN nodes through O1.</td><td colspan="1" rowspan="1">Config request</td></tr><tr><td colspan="1" rowspan="1">Step 2b</td><td colspan="1" rowspan="1">SMO sends the updated slice configuration to Near-RT RIC and/or RANnodes via O1. Examples of the slice configuration are the number ofallocated PRBs, number of flows, slice priorities.</td><td colspan="1" rowspan="1">Config deliverystep 2b or 2c ismandatory</td></tr><tr><td colspan="1" rowspan="1">Step 2c</td><td colspan="1" rowspan="1">Non-RT RIC sends the updated A1 policies to Near-RT RIC.</td><td colspan="1" rowspan="1">Policy delivery</td></tr><tr><td colspan="1" rowspan="1">Step 3a</td><td colspan="1" rowspan="1">Near-RT RIC and RAN nodes process and execute the updated sliceconfiguration.</td><td colspan="1" rowspan="1">Configexecutionstep 3a or 3b ismandatory</td></tr><tr><td colspan="1" rowspan="1">Step 3b</td><td colspan="1" rowspan="1">Near-RT RIC receives the updated A1 policy, controls RAN nodes based onthe A1 policy and sends the feedback to Non-RT RIC via A1.</td><td colspan="1" rowspan="1">Policyexecution</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">A RAN slice is deactivated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the slow loop RAN slice SLA optimization is given in figure 4.9.3.2-1.

![](images/e328e2ce4512ddd1b680a1003c06599d97c342c7394aeb277ea4884231549d90.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.9.3.2-1: Slow loop RAN slice SLA optimization flow diagram

# 4.9.3.3 Fast loop RAN slice SLA optimization

The context of the fast loop RAN slice SLA optimization is captured in table 4.9.3.3-1.

Table 4.9.3.3-1: Fast loop RAN slice SLA optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Fast lop RAN slice SLA optimization</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO, RAN</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">A1, O1, E2 interface connectivity is established.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.O1 interfaces are established between SMO and Near-RT RIC, and SMOand RAN nodes.RAN slice SLA assurance models or control apps have been deployed inNear-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">A RAN slice is activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step1</td><td colspan="1" rowspan="1">Non-RT RIC decides to generate a policy for Near-RT RIC slice SLAassurance based on RAN slice SLA requirements and/or operator-definedRAN intents, A1 feedback from Near-RT RIC, EI from external app serverand O1 based long term trends.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step2</td><td colspan="1" rowspan="1">Near-RT RIC receives slice specific O1 configuration and A1 policies fromSMO and Non-RT RIC respectively. The former is static and default, thelatter is dynamic, optimized and converted from slice SLA. The policiesconsist of scope identifiers (e.g., S-NSSAl, flow ID, cell ID) and policystatements (e.g., slice specific KPl targets).In case of using Els, Near-RT RIC also receives the Els from Non-RT RICvia A1-El interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3</td><td colspan="1" rowspan="1">Near-RT RIC starts to collect PMs via E2. Examples of the PMs are CSI,PRB usage, L2 throughput, RAN Iatency, etc. Applicable PMs are specified in 3GPP TS 28.552 [6].</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4</td><td colspan="1" rowspan="1">The model or control app in Near-RT RIC analyzes collected PMs, A1policies from Non-RT RIC (and optionally Els from A1-El interface) to guideRAN nodes via E2 to meet the slice SLA.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5</td><td colspan="1" rowspan="1">Near-RT RIC sends A1 feedback to Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">A RAN slice is deactivated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the fast loop RAN slice SLA optimization is given in figure 4.9.3.3-1.

![](images/aa0b52583505071ec45cadbb041edbf85ae787513d004feb2834d415adfd6ba2.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.9.3.3-1: Fast loop RAN slice SLA optimization flow diagram

# 4.9.4 Required data

The data requirements for RAN slice SLA assurance use case are specified below. The required data specified in table 4.9.4-1 shall be supported by the associated interfaces specified in the table.

Table 4.9.4-1: Required data for RAN slice SLA assurance use case   

<table><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters / Measurements</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.001</td><td colspan="1" rowspan="1">CQl relatedmeasurements</td><td colspan="1" rowspan="1">Wideband CQI distribution</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]clause5.1.1.11.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.002</td><td colspan="1" rowspan="1">UE throughputrelatedmeasurements</td><td colspan="1" rowspan="1">Average DL / UL UE throughput ingNB</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5],clauses</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">5.1.1.3.1,5.1.1.3.3</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.9.003</td><td colspan="1" rowspan="1">UE throughputrelatedmeasurements</td><td colspan="1" rowspan="1">Scheduled IP throughput in DL/UL</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPPTS36.314 [6]clauses 4.1.6.1,4.1.6.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.004</td><td colspan="1" rowspan="1">RRC connectionrelatedmeasurements</td><td colspan="1" rowspan="1">Mean / max number of RRCconnections</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]，clauses5.1.1.4.1,5.1.1.4.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.005</td><td colspan="1" rowspan="1">RRC connectionrelatedmeasurements</td><td colspan="1" rowspan="1">Attempted / successful RRCconnection establishments</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]，clauses5.1.1.15.1,5.1.1.15.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.006</td><td colspan="1" rowspan="1">DRB relatedmeasurements</td><td colspan="1" rowspan="1">Number of DRBs attempted to /successfully setup</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPPTS28.552 [5]，clauses5.1.1.10.1,5.1.1.10.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.007</td><td colspan="1" rowspan="1">PDU sessionmanagementrelatedmeasurements</td><td colspan="1" rowspan="1">Number of PDU sessionsrequested to / successfully / failedto setup</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPPTS28.552[5]clauses5.1.1.5.1,5.1.1.5.2,5.1.1.5.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.008</td><td colspan="1" rowspan="1">Number of activeUEs</td><td colspan="1" rowspan="1">Mean number of active UEs in theUL / DL per cell</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]，clauses5.1.1.23.1,5.1.1.23.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.009</td><td colspan="1" rowspan="1">Radio resourceutilization relatedmeasurements</td><td colspan="1" rowspan="1">Mean DL / UL PRB used for datatraffic</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552[5]clauses5.1.1.2.5,5.1.1.2.7</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.010</td><td colspan="1" rowspan="1">PDCP datavolumemeasurements</td><td colspan="1" rowspan="1">DL / UL PDCP PDU data volume</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]，clauses5.1.3.6.1.1,5.1.3.6.1.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.011</td><td colspan="1" rowspan="1">PDCP datavolumemeasurements</td><td colspan="1" rowspan="1">Data volume in DL/UL</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPPTS36.314 [6]，clauses 4.1.8.1,4.1.8.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.012</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">UL PDCP packet average delay</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.558 [23]，clause 6.3.1.1.5</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.013</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay DL air-interface</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552[5]，clause 5.1.1.1.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.014</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay UL on over-the-airinterface</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5],clause 5.1.1.1.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.015</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay DL in gNB-DU</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552[5]clause 5.1.3.3.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.016</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay DL on F1-U</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5],clause 5.1.3.3.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.017</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay DL in CU-UP</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5],clause 5.1.3.3.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.018</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average over-the-air interfacepacket delay in the UL per DRB perUE</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS38.314 [7]，clause 4.2.1.2.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.019</td><td colspan="1" rowspan="1">Average userplane delay</td><td colspan="1" rowspan="1">Average delay DL air-interface</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.558 [23]，clause 6.3.1.1.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.020</td><td colspan="1" rowspan="1">Packet dropmeasurements</td><td colspan="1" rowspan="1">DL RLC SDU packet drop rate ingNB-DU</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPPTS28.552[5]clause 5.1.3.2.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.021</td><td colspan="1" rowspan="1">Packet loss ratemeasurements</td><td colspan="1" rowspan="1">UL / DL F1-U packet loss rate</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [5]，clauses5.1.3.1.2,5.1.3.1.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.022</td><td colspan="1" rowspan="1">Packet loss ratemeasurements</td><td colspan="1" rowspan="1">Packet Uu loss rate in the DL perDRB per UE</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS38.314 [7]，clause 4.2.1.5.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.023</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">NRCelICU</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPPTS28.541 [4]clause 4.3.4</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.024</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">NRCellDU</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.541 [4],clause 4.3.5</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.025</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">GNBDUFunction</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.541[4],clause 4.3.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.026</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">GNBCUCPFunction</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.541 [4],clause 4.3.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.027</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">GNBCUUPFunction</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.541 [4]clause 4.3.3</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.9.028</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">RRMPolicy_</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.541 [4]clause 4.3.43</td><td colspan="1" rowspan="1">01</td></tr></table>

# 4.10 Multi-vendor slices

This use case “multi-vendor slices” is a case that vO-DU and vO-CU functions composing each slice is provided from different vendor. In this sub-clause, concept, motivation and benefits of introducing “multi-vendor slices” are explained and candidate solutions are studied.

# 4.10.1 Background and goal of the use case

Proposed use case enables multiple slices with functions provided from multi-vendors, such as slice #1 is composed with DU and CU provided from vendor A and slice $\# 2$ is composed with DU and CU provided from vendor B (see figure 4.10.1-1).

![](images/44365fcbe7c864e20cc6afb7a07bba02cb82318076c7f388753af72b062d3f56.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.10.1-1: Multi-vendor slices

To support multi-vendor slicing, there are many possible configurations to realize this use case; all of which share that one O-RU is connected to one or more O-DUs. For example, one possible configuration might be one where a single cell is shared by two O-DUs, and another possible configuration is where two cells are allocated to two different O-DUs in a Shared O-RU configuration. Under those possible configurations, it is desired to keep frequency efficiency.

When providing multiple slices, it is assumed that suitable vO-DU/scheduler and vO-CU treat each slice respectively. A vendor who providing vO-DU and vO-CU function can have a strength of a customized scheduler for a certain service. With accomplishment of multi-vendor circumstances, following benefits can be expected.

1) More flexible and time to market deployment Operator can maximize options to choose suitable vO-DU/scheduler and vO-CU to offer various slice. For example, some vendor has a strength of a scheduler for eMBB service and the other has a strength of scheduler for URLLC service. Or vendor A can provide vO-DU/scheduler and vO-CU suitable for URLLC earlier than vendor B, therefore operator can choose vO-DU and vO-CU functions from vendor A to meet their service requirement.

Also, when operator will add a new service/slice, new functions from a new vendor can be introduced with less consideration for existing vendor if multi-vendor circumstance was realized. This can lead to expand vendor’s business opportunities rapidly.

2) Flexible deployment when sharing RAN equipment among operators When operators want to share RAN equipment and resources, RAN vendors and their placement of each RAN functions can be different. If multi-vendor circumstance was introduced, then it can relax restrictions among operators to share RAN equipment and resources. This can lead to expand opportunity reaching agreement of RAN sharing among operators. With expansion of RAN sharing, CAPEX and OPEX by operator will be optimized and additional investment can be done more.

3) Reducing supply chain risk

If existing vendor providing a certain pair of vO-DU and vO-CU functions would withdraw of their market due to business reason, operator can deploy new vO-DU and vO-CU functions alternatively from other vendor under this multi-vendor circumstance. This can reduce a risk for operators’ business continuity.

# 4.10.2 Entities/resources involved in the use case

1) SMO multi-vendor slice App:

a) Configures vO-DU and vO-CU.   
b) Configures O-RU to connect to vO-DU.

2) Near-RT RIC:

a) Shares MAC related data unique for UE among vO-DUs.   
b) Supports communication of configuration parameters to RAN.

3) E2 nodes (vO-CU, vO-DU, O-RU):

a) Primary vO-DU processes SRB (Signalling Radio Bearer), DRB (Data Radio Bearer) and other vO-DU related functions. Secondary vO-DU processes only DRB related functions. Note that vO-DU and vO-CU are created as part of network slice creation procedure.

# 4.10.3 Solutions

# 4.10.3.1 Data transmission call flow example for multi-vendor slices use case

he context of data transmission call flow example for multi-vendor slices use case is captured in table 4.10.3.1-1.

Table 4.10.3.1-1: Data transmission call flow example for multi-vendor slices use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">UE communicates on slice #1 and #2 respectively.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO multi-vendor slice App configures vO-DU and v-O-CU with radioresource assignment (via Orchestrator) and collects KPI data.Near-RT RIC configures vO-DU and vO-CU for resource assignment andshares MAC related information unique for UE among vO-DUs.Primary vO-DU processes SRB (Signalling Radio Bearer), DRB (DataRadio Bearer). Secondary vO-DU processes only DRB.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.</td><td colspan="1" rowspan="1"></td></tr><tr><td></td><td>Slice #1 is created over primary vO-DU and vO-CU with logical channel ID #1 and #2, and slice #2 is created over secondary vO-DU and vO-CU with logical channel ID #3.</td><td rowspan="3"></td></tr><tr><td></td><td colspan="1">O-RU is shared between primary vO-DU and secondary vO-DU with one component carrier.</td></tr><tr><td></td><td colspan="1">CU-CP is shared between primary vO-CU-UP and secondary vO-CU-UP.</td></tr><tr><td></td><td>TDD operation is assumed.</td><td rowspan="3"></td></tr><tr><td rowspan="3">Pre-conditions</td><td colspan="1">UE tries to transmit data on slice #1 and #2. Slice #1 and #2 are created and activated on primary vO-DU, vO-CU and</td></tr><tr><td colspan="1">secondary vO-DU, vO-CU respectively. Slice #1 is tied with scheduling request resource 1 and logical channel ID</td></tr><tr><td colspan="1">#1 and #2, and slice #2 is tied with scheduling request resource 2 and logical channel ID #3 Primary vO-DU and secondary vO-DU know which timing/resource block they can utilize on for slice #1 and #2 respectively by direction from SMO</td></tr><tr><td>Begins when</td><td>UE has already performed RACH procedure with primary vO-DU. UE tries to perform registration procedure with RRC Connection Request</td><td></td></tr><tr><td>Step 1 (M)</td><td>message. [UE performs registration procedure] UE sends RRC Connection Request message to primary vO-DU and vO-CU through O-RU. Primary vO-CU and vO-DU responds with RRC Connection</td><td rowspan="3"></td></tr><tr><td rowspan="2"></td><td colspan="1">Setup. UE sends RRC connection Setup Complete message. Primary vO-DU sends initial RRC message and shared information such as C-</td></tr><tr><td colspan="1">RNTI to Near RT-RIC. Near RT-RIC determines to transfer it to secondary vO- DU over E2 interface. Other registration procedure is performed. [PDU session establishment] UE starts PDU session establishment procedure with PDU session</td></tr><tr><td>Step 2 (M)</td><td>establishment request message with primary vO-DU and vO-CU. UE initiates PDU session establishment procedure with S-NSSAI 2 for slice #2 via primary vO-DU. UE context modification is made at secondary vO-DU.</td><td></td></tr><tr><td>Step 3 (M)</td><td>[U-plane data transmission between primary vO-DU and O-RU] At allocated timing/resources, primary vO-DU sends Scheduling Command message to O-RU to start transfer and receive DL and UL Data. UE sends Scheduling Request message on PUCCH with scheduling request resource 1 to primary vO-DU over open fronthaul.</td><td>O-RAN.WG4.CUS.0- v02.00 [29], "Figure 6-5: C-plane and U- plane message transfer procedure (DL &amp; UL shown)"</td></tr><tr><td>Step 4 (M)</td><td>Primary vO-DU responds with UL Grant message to the UE. [Buffer notification and transmission user data] UE notices buffer with Buffer Status Request message to primary vO-DU.</td><td></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Primary vO-DU acknowledges with UL Grant message.UE sends user data on PUSCH with logical channel ID #1 and #2.Primary vO-DU acknowledges with Ack or Nack.UE repeats step 3 unti buffer becomes empty.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">[U-plane data transmission between secondary vO-DU and O-RU]At allocated timing/resources, secondary vO-DU sends Scheduling Command message to O-RU to start transfer and receive DL and UL Data.UE sends Scheduling Request message on PUCCH with scheduling requestresource 2 to secondary vO-DU over open fronthaul. Secondary vO-DUresponds with UL Grant message to the UE.</td><td colspan="1" rowspan="1">O-RAN.WG4.CUS.0-v02.00 [29], “Figure6-5: C-plane and U-plane message transfer procedure (DL&amp; UL shown)"</td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">[Buffer notification and transmission user data]UE notices buffer with Buffer Status Request message to secondary vO-DU.Secondary vO-DU acknowledges with UL Grant message.UE sends user data on PUSCH with logical channel ID #3.Secondary vO-DU acknowledges with Ack or Nack.UE repeats step 5 until buffer becomes empty.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">[Collect data]RAN related data from RAN nodes are collected at SMO Collector via O1interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">UE finishes data transmission until buffer becomes empty.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified</td><td colspan="1" rowspan="1"></td></tr></table>

The data transmission call flow example for multi-vendor slices use case – part 1 of 2 is given in figure 4.10.3.1-1.

![](images/5eee2c562d612f9a97bb978ad6d38995fff626f58da5e53cf534ed26789a9ac7.jpg)

> **Image Summary:** {"image_transcription": "Entities: \n- O-RU \n- O-DU \n- CU-CP \n- CU-UP \n- Near-RT RIC \n- SMO \n\nRelationships: \n- O-RU → O-DU: Fronthaul (bidirectional)\n- O-DU → CU-CP: F1-C interface\n- O-DU → CU-UP: F1-U interface\n- CU-CP → Near-RT RIC: E2 interface\n- Near-RT RIC → SMO: A1 interface\n- SMO → Near-RT RIC: A1 interface\n\nHierarchy: \n- gNB = RU + DU + CU-CP + CU-UP\n\nFlows: \n- 1. O-DU → Near-RT RIC: Request\n- 2. Near-RT RIC → SMO: request\n- 3. SMO → Near-RT RIC: Response\n- 4. Near-RT RIC → O-DU: Command\n\nNotes: \n- Image caption: 'O-RAN Architecture - Near-RT RIC Interaction'\n- Label 1: 'O-RU'\n- Label 2: 'O-DU'\n- Label 3: 'CU-CP'\n- Label 3a: 'CU-UP'\n- Label 3b: 'Near-RT RIC'\n- Label 3c: 'SMO'"}
  
Figure 4.10.3.1-1: Data transmission call flow example for multi-vendor slices use case – part 1 of 2

The data transmission call flow example for multi-vendor slices use case – part 2 of 2 is given in figure 4.10.3.1-2.

![](images/1398b3a370e923e0c4fd9d9c6bcc6dcf3413c4af3fc5732227f51a08893f3dfb.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.10.3.1-2: Data transmission call flow example for multi-vendor slices use case – part 2 of 2

# 4.10.3.2 Data transmission call flow example for RAN sharing use case

The context of data transmission call flow example for RAN sharing use case is captured in table 4.10.3.2-1.

Table 4.10.3.2-1: Data transmission call flow example for RAN sharing use case   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>UE communicates on secondary vO-DU and vO-CU with PLMN #2.</td><td></td></tr><tr><td rowspan="2">Actors and Roles</td><td>SMO multi-vendor slice App configures vO-DU and v-O-CU with radio resource assignment (via Orchestrator) and collects KPI data. Near-RT RIC configures vO-DU and vO-CU for resource assignment and</td><td></td></tr><tr><td>shares MAC related information unique for UE among vO-DUs. Primary vO-DU processes SRB (Signalling Radio Bearer), DRB (Data Radio Bearer). Secondary vO-DU processes only DRB.</td><td></td></tr><tr><td rowspan="6">Assumptions</td><td>All relevant functions and components are instantiated.</td><td rowspan="6"></td></tr><tr><td>PLMN #1 is assigned to primary vO-DU and vO-CU, and PLMN #2 is assigned to secondary vO-DU and vO-CU respectively.</td></tr><tr><td>O-RU is shared between primary vO-DU and secondary vO-DU with one component carrier.</td></tr><tr><td>CU-CP is shared between primary vO-CU-UP and secondary vO-CU-UP.</td></tr><tr><td>TDD operation is assumed.</td></tr><tr><td>UE tries to transmit data with PLMN #2. PLMN #1 and #2 are assigned to primary vO-DU, vO-CU and secondary</td></tr><tr><td rowspan="4">Pre-conditions Begins when</td><td>vO-DU, vO-CU respectively Primary vO-DU and vO-CU advertise PLMN #1 and #2 over the air.</td><td></td></tr><tr><td>Primary vO-DU and secondary vO-DU know which timing/resource block they can utilize on for PLMN #1 and #2 respectively by direction from SMO</td><td></td></tr><tr><td>via O1 interface.</td><td></td></tr><tr><td>UE has already performed RACH procedure with primary vO-DU. UE tries to perform registration procedure with RRC Connection Request</td><td></td></tr><tr><td></td><td>message. [UE performs registration procedure with PLMN #2] UE sends RRC Connection Request message to primary vO-DU and vO-CU through O-RU. Primary vO-CU and vO-DU responds with RRC Connection Setup. UE sends RRC connection Setup Complete message with PLMN#2 in</td><td></td></tr><tr><td rowspan="2">Step 1 (M)</td><td>selected PLMN-identity. Primary vO-DU sends initial RRC message with PLMN-identity and shared information such as C-RNTI to Near RT-RIC. Near RT-RIC determines to</td><td></td></tr><tr><td>transfer it to secondary vO-DU over E2 interface. Other registration procedure is performed through secondary vO-DU. [PDU session establishment]</td><td></td></tr><tr><td>Step 2 (M)</td><td>UE starts PDU session establishment procedure with PDU session establishment request message through secondary vO-DU and vO-CU.</td><td></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">[U-plane data transmission between secondary vO-DU and O-RU]At allocated timing/resources, secondary vO-DU sends Scheduling Command message to O-RU to start transfer and receive DL and UL Data.UE sends Scheduling Request message on PUCCH with scheduling requestresource 2 to secondary vO-DU over open fronthaul.Secondary vO-DU responds with UL Grant message to the UE.</td><td colspan="1" rowspan="1">O-RAN.WG4.CUS.0-v02.00 [29], "Figure6-5: C-plane and U-plane messagetransfer procedure (DL&amp; UL shown)"</td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">[Buffer notification and transmission user data]UE notices buffer with Buffer Status Request message to secondary vO-DU.Secondary vO-DU acknowledges with UL Grant message.UE sends user data on PUSCH with logical channel ID #2.Secondary vO-DU acknowledges with Ack or Nack.UE repeats step 3 until buffer becomes empty.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">[Collect data]RAN related data from RAN nodes are collected at SMO Collector via O1interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">UE finishes data transmision until buffer becomes empty.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The data transmission call flow example for RAN sharing use case is given in figure 4.10.3.2-1.

![](images/07f837fd9ade26bd2604ed68e42897f091f0662700ed635af103b020070caf14.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.10.3.2-1: Data transmission call flow example for RAN sharing use case

# 4.10.4 Required data

The measurement counters and KPIs (as defined by 3GPP and will be extended for O-RAN use cases) shall be appropriately aggregated by cell, QoS type, slice, etc.

1) Per-UE CSI   
2) Per slice performance statistics such as PDCP throughput, PRB usage

# 4.11 Dynamic spectrum sharing (DSS)

This use case provides the background, motivation, and requirements to realize Dynamic Spectrum Sharing (DSS) over the O-RAN architecture. This is to enable operators to adapt radio resource allocation policies and control to dynamically share radio spectrum between 4G and 5G networks.

# 4.11.1 Background and goal of the use case

As we transition from 4G to 5G, the spectral resources used for 5G deployment is a key consideration and this situation varies from one operator to another. Though, new C-band resources between $3 { \cdot } 6 ~ \mathrm { G H z }$ and mmWave bands have been acquired by operators, these bands suffer from great propagation and penetration loss, limiting their coverage to those users close to the cell, this situation worsens in the UL as the UE device is power constrained. A cost-effective way to address this is the 5G deployment on lower bands (i.e., below 2GHz), which are also used in 4G LTE deployments today. Operating on lower bands along with non-standalone mode of 5G deployment helps to cover large geography, enables seamless mobility between 4G and 5G while being sensitive to overall cost of deployment. In addition, DSS offers the advantage of dynamically sharing the available spectrum adapting to the varying workloads of the 4G and 5G network.

DSS is compelling considering the need for operators to dynamically share already deployed spectral resources between LTE and NR devices without degrading the QoE of the current 4G subscribers while offering the same level of coverage and necessary QoS to NR devices, under the assumption that the two networks will co-exist in the near term. The objective of this use case is to propose DSS in the context of the O-RAN architecture, specifically to realize it as an application in the RIC framework.

This would particularly benefit vRAN implementations when the 4G/5G CU/DU are from different vendors and one could leverage RAN data over O-RAN’s framework for traffic prediction, DSS related resource management and conduct control functions. Towards this, the intelligent control functions are identified, which can be realized as a DSS application to augment the L3/L2/L1 control functions specified as part of LTE-NR coexistence in 3GPP TS 23.501 [2] and in 3GPP TS 37.340 [12].

The architectural context set for this discussion is shown in figure 4.11.1-1. DSS enables 4G and 5G UEs to operate over the same spectrum identified as X (typically low band), while 5G itself could operate on new bands Y (typically high band) not used by current 4G deployment. In a typical setting, Y would offer higher capacity, low latency and smaller coverage, while X would be used to offer reasonable capacity along with larger coverage. 3GPP specifications offers DSS support over X2/Xn interface to enable dynamic sharing of the spectrum resource in addition to the L2/L1 adaptation for 5G-NR to co-exist with LTE.

Considering the scenario of incremental deployment - in the 5G NSA mode, the 5G UE is required to have dual connectivity capability and be able to connect to eNBs on LTE bands for control plane requirements and user plane connectivity towards the LTE and/or 5G depending on deployment requirements. In the scenario where gNB only operates on 5G C or mmWave bands, the sharing of the LTE frequency band between 4G and 5G UEs can be solely fulfilled by eNB MAC scheduler, as the UE is expected to be dual stacked. While, if the $\mathrm { g N B }$ is required to operate on lower LTE bands as well, then spectral sharing needs to be coordinated between the LTE and 5G schedulers.

When DSS is enabled in the SA mode, 5G UE would be capable of operating on lower LTE bands (below 2GHz), C and mmWave bands and connects only to the gNBs. The sharing of the LTE bands between LTE and 5G data channels are achieved by both 4G scheduler and 5G scheduler using resource management and interference mitigation functions in the RIC between them.

The use case proposes to conduct DSS related policy, configuration, resource management and control functions using the Non-RT and Near-RT functions over open interfaces proposed by O-RAN.

An abstracted view of how DSS application can be realized using the Non-Real-Time and Near-Real-Time RIC components is shown in figure 4.11.1-2. The DSS over RIC can be realized as multiple applications considering its multiple optimization and operational objectives. One possible logical breakdown is as a traffic prediction and resource management application (DSS-App) managing the shared spectrum resource adapting to dynamic 4G and 5G specific workload requirements in various local contexts, and another application (RAT-App) to configure, control and monitor DSS related functions in the CU/DU corresponding to the LTE and 5G cells. The DSS-App engineers at the Non-RT RIC level translates the global DSS policies based on workload requirements for a region and time-of-day to spectrum sharing policies such as max/min bandwidth threshold at a local level (e.g. edge or central office). The RAT-App at the Non-RT RIC level also translates the DSS-App’s resource policies to RAT specific configuration and policies at the Near-RT RIC and the CU/DU entities. The DSS-App at the Near-RT RIC uses the data collected by the RAT-App to make dynamic resource sharing decisions that are enforced by the RAT-App using the E2 control APIs.

![](images/bf89353ea9fa222a5b556d4ba9c9798ee23e1529f4a25e825f60f0ce1b10b321.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.11.1-1: RIC-based DSS architecture

![](images/9d7e24f2a93abd22bba6c43f6001b9f927297567fa50e0d8b71c124f4a8781ff.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.11.1-2: RIC-based DSS realization

The main goal of the Non-RT DSS-App is to provide long-term scheduling policy to 4G and 5G scheduler considering business, user, spatial and temporal workload factors.

The main functionality of Non-RT RAT-App is to translate the global DSS policies from Non-RT DSS-App to RAT specific policies to the RAT-App in the Near-RT RIC over A1.

The main functionalities of the Near-RT DSS-App include policy translation between Non-RT DSS-App to RAT specific configuration to the Near-RT RAT-App. Furthermore, it is actively involved in closed loop decision using the KPIs from the RAN adapting to the needs of the 4G and 5G cells.

The main functionality of Near-RT RAT-App is to perform RAT specific configuration, control and data subscription over E2 interface with RAN (CU/DU components).

# 4.11.2 Entities/resources involved in the use case

1) Non-RT RIC: a) Receive SMO’s DSS specific service requirement for the RAN and translate them into resource sharing policies.

b) Provide long-term policies in terms of scheduling guidance to 4G and 5G scheduler over A1 to Near-RT RIC, considering business, user, spatial and temporal workload factors, policies related to expected performance and actions when it deviates based on KPIs from the 4G and 5G network.   
c) Develop and train AI/ML models with the help of SMO functions for the Near-RT RIC to predict the shortterm traffic demand for 4G and 5G network based on near-real-time metrics from RAN. Deployment of these ML model over O1 and xApps over O2 to the Near-RT RIC.   
d) Receive policy feedback from Near-RT RIC and update policy and re-train ML models whenever required.

2) Near-RT RIC:

a) Support deployment, execution, and ability to update DSS xApps from Non-RT RIC.   
b) Support interpretation of policies related to RAT specific resource allocation.   
c) Translate RAT specific SLA policy to configuration, control, and data subscription over E2 interface to E2 nodes (O-CU, O-DU).   
d) Share resource allocation performance and policy feedback report with Non-RT RIC for further evaluation and optimization over O1/A1.

3) RAN:

a) Support discovery of DSS related configuration of E2 nodes over E2 interface.   
b) Share the data collection over O1 interface.   
c) Support resource management related metrics collection over E2 interface.   
d) Support control and policy enforcement from Near-RT RIC over E2 interface.

# 4.11.3 Solutions

# 4.11.3.1 Dynamic spectrum sharing for 4G and 5G

The context of the dynamic spectrum sharing for 4G and 5G is captured in table 4.11.3.1-1.

Table 4.11.3.1-1: Dynamic spectrum sharing for 4G and 5G   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable operators to dynamically share spectrum in the existing 4G deploymentwith 5G systems, based on the dynamic loads of both networks and resourcesharing policies.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC: Spectrum resource sharing policy function.Near-RT RIC: Executes resource sharing models and algorithms, translatingRAT specific policy to configuration, control and data subscription over E2interface with RAN.RAN: Executes resource sharing enforcement rules and policies, collects andreports RAN statistics and performance over E2 and O1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated. DSS xApps aredeployed over O1 with initial configuration.A1, E2 interface connectivity is established with Non-RT RIC and RANrespectively.Data report, policy and control subscription established on E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational.SMO has established the data collection and sharing interface with Non-RT RIC.Non-RT RIC analyzes the historical data from RAN, develops, trains with helpof SMO functions and deploys the relevant Al/ML models or algorithm as xAppsto the Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is detected.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Near-RT RIC collects DSS related RAN function capabilities and configurationparameters from RAN over E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC communicates DSS relevant policies to the Near-RT RIC over theA1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Near-RT RIC communicates RAT specific DSS relevant configuration, controlpolicies to RAN over the E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">RAN deploys the configuration and control policies received from the Near-RTRIC over the E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Near-RT RIC collects relevant observability data from RAN, executes xApp andoutputs the optimal resource allocation and cell level resource schedulingdecisions to RAN over E2 and policy feedback to Non-RT RIC over A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">RAN deploys the updated control policies received from the Near-RT RIC overthe E2 interface and continues reporting data to SMO over O1 and E2 asconfigured.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Non-RT RIC adjusts the policy based on PM data from SMO and feedback fromNear-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">Non-RT RIC updates the resource sharing policy to Near-RT RIC over A1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (0)</td><td colspan="1" rowspan="1">Non-RT RIC re-trains/updates the Al/ML model with new data and performance,and deploys the new model or new model configurations to Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC monitors loads and relevant KPI performance metrics ofeNB/gNB to observe the resource sharing efficiency and sets up new policiesbased on the metrics and business needs.Near-RT RIC executes the resource sharing model or algorithm. RAN operates with the scheduling guidance from RIC and reports performance data to RIC .</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the dynamic spectrum sharing for 4G and 5G is given in figure 4.11.3.1-1.

![](images/e9042086deefadc04954500e6a0e678e7a46692a5b55b5a189d63e429b34b44e.jpg)

> **Image Summary:** {"entities": ["O-RAN Intelligent Controller (O-RIC)", "O-RAN Near-RT RIC", "O-RAN Far-RT RIC", "Non-RT RIC", "O-DU", "CU-CP", "CU-UP", "O-RU", "O-CU", "Radio Access Network (RAN) Architecture", "O-RAN Architecture", "O-RAN Interfaces", "O-RAN Functionality"], "relationships": ["O-RAN Intelligent Controller (O-RIC) → O-RAN Near-RT RIC: A3 interface, RIC Communication", "O-RAN Intelligent Controller (O-RIC) → O-RAN Far-RT RIC: A3 interface, RIC Communication", "O-RAN Near-RT RIC → O-DU: E2 interface, RIC Control", "O-RAN Near-RT RIC → CU-CP: E2 interface, RIC Control", "O-RAN Near-RT RIC → CU-UP: E2 interface, RIC Control", "O-RAN Near-RT RIC → O-RU: E2 interface, RIC Control", "O-RAN Near-RT RIC → O-CU: E2 interface, RIC Control", "O-RAN Far-RT RIC → O-DU: E2 interface, RIC Control", "O-RAN Far-RT RIC → CU-CP: E2 interface, RIC Control", "O-RAN Far-RT RIC → CU-UP: E2 interface, RIC Control", "O-RAN Far-RT RIC → O-CU: E2 interface, RIC Control", "O-RAN Far-RT RIC → O-RU: E2 interface, RIC Control", "O-DU → CU-CP: F1-C interface, Control Plane", "O-DU → CU-UP: F1-U interface, User Plane", "CU-CP → CU-UP: Interface", "CU-UP → CU-CP: Interface", "O-CU → O-RU: Fronthaul interface"], "hierarchy": ["O-RAN Architecture = O-RIC + O-RAN Near-RT RIC + O-RAN Far-RT RIC + O-DU + CU-CP + CU-UP + O-RU + O-CU", "CU = CU-CP + CU-UP", "O-CU = CU-CP + CU-UP"], "flows": [], "notes": ["Figure: O-RAN Architecture and Interfaces", "Note 1: The interfaces are presented as an example", "Figure shows O-RAN Architecture and Interfaces", "Note 2: The interfaces and functionality are presented as an example"]}
  
Figure 4.11.3.1-1: Dynamic spectrum sharing for 4G and 5G flow diagram

# 4.11.4 Required data

Multiple observability data from RAN need to be reported to SMO, Non-RT RIC and Near-RT RIC for DSS to operate.   
The required data for DSS use case is captured in table 4.11.4-1.

Table 4.11.4-1: Required data for DSS use case   

<table><tr><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters / Measurements</td><td colspan="1" rowspan="1">RAT</td><td colspan="1" rowspan="1">Source IInterface</td><td colspan="1" rowspan="1">Reference</td></tr><tr><td colspan="1" rowspan="1">4G/5G DSSconfiguration andoperation parameters</td><td colspan="1" rowspan="1">Geography location (e.g., cell site)</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">Externalserver</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">DSS modality (static, semi-static (MBSFN),dynamic (sub-frame level))</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3GPP TS38.211 [13],3GPP TS38.213 [14]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Cell configuration information (e.g., FDD/TDD,band, signaling/RS allocation bitmap)</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3GPP TS36.423 [30],3GPPTS38.211 [13],3GPP TS38.213 [14]</td></tr><tr><td colspan="1" rowspan="1">4G/5G schedulinginformation</td><td colspan="1" rowspan="1">Physical resource blockused/reserved/requested/blocked bitmapinformation</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3GPP TS36.423 [30]</td></tr><tr><td colspan="1" rowspan="1">4G/5G cell loadstatistics</td><td colspan="1" rowspan="1">Number of active UEs (total, UL/DL, per QCI)</td><td colspan="1" rowspan="1">4G</td><td colspan="1" rowspan="1">E2 and 01</td><td colspan="1" rowspan="1">3GPP TS36.314 [31]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Mean/Max number of active UEs (DL/UL, total,per DRB(mapped 5QI))</td><td colspan="1" rowspan="1">5G</td><td colspan="1" rowspan="1">E2 and 01</td><td colspan="1" rowspan="1">3GPP TS38.314 [32],3GPPTS32.425 [33]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Traffic demand/buffer size (total, per QCl/5QI)</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">PRB usage (DL, UL, total, per QCl/5QI)</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS36.314 [31],3GPPTS36.423 [30]3GPPTS28.552[6]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">PDCCH CCE usage</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS36.423 [30]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">RRC connection number</td><td colspan="1" rowspan="1">5G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS28.552[6]，3GPPTS32.425 [33]</td></tr><tr><td colspan="1" rowspan="1">4G/5G QoSconfiguration andparameters</td><td colspan="1" rowspan="1">QoS classes</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3GPP TS23.501 [2] (5G)3GPPTS36.300 [34],3GPPTS23.401 [35]3GPP TS23.203 [36](4G)</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Slice types</td><td colspan="1" rowspan="1">5G</td><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">3GPP TS23.501 [2]</td></tr><tr><td colspan="1" rowspan="1">UE performancestatistics</td><td colspan="1" rowspan="1">Scheduled IP throughput (DL, UL, per QCI)</td><td colspan="1" rowspan="1">4G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS36.314 [31]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Data volume (DL/UL per CQI)</td><td colspan="1" rowspan="1">4G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS36.314 [31]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UL/DL PDCP SDU data volume</td><td colspan="1" rowspan="1">5G</td><td colspan="1" rowspan="1">E2 and 01</td><td colspan="1" rowspan="1">3GPP TS28.552[6]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">PDCP packet delay DL/UL per CQI/QCI</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and 01</td><td colspan="1" rowspan="1">3GPP TS36.314 [31] (4G)</td></tr><tr><td colspan="1" rowspan="1">UE mobility statistics</td><td colspan="1" rowspan="1">RSRP/RSRQ/SINR/RSSI</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and 01</td><td colspan="1" rowspan="1">3GPP TS36.214 [37]，3GPPTS36.331 [38]</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UE location information</td><td colspan="1" rowspan="1">45/5G</td><td colspan="1" rowspan="1">ExternalServer</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UE capability</td><td colspan="1" rowspan="1">4G/5G</td><td colspan="1" rowspan="1">E2 and O1</td><td colspan="1" rowspan="1">3GPP TS36.331 [38]</td></tr></table>

# 4.12 NSSI resource allocation optimization

This use case provides the background, motivation, description, and requirements for the NSSI resource allocation optimization use case, allowing operators to optimize the allocation resources to NSSI(s) with wide range service requirements.

# 4.12.1 Background and goal of the use case

5G networks are becoming increasingly complex with the densification of millimeter wave small cells, and various new services, such as eMBB (enhanced Mobile Broadband), URLLC (Ultra Reliable Low Latency Communications), and mMTC (massive Machine Type Communications) that are characterized by high speed high data volume, low speed ultralow latency, and infrequent transmitting low data volume from huge number of emerging smart devices, respectively. It is a challenging task for 5G networks to allocate resources dynamically and efficiently among multiple network nodes to support the various services. However, as eMBB, URLLC, and mMTC services in 5G are typically realized as NSI (Network Slice instance). Therefore, the resources allocated to NSSI (Network Slice Subnet Instance) to support the ORAN nodes can be optimized according to the service requirements.

As the new 5G services have different characteristics, the network traffic tends to be sporadic, where there can be different usage pattern in terms of time, location, UE distribution, and types of applications. For example, most IoT sensor applications can run during off-peak hours or weekends. Special events, such as sport games, concerts, can cause traffic demand to shoot up at certain time and locations. Therefore, NSSI resource allocation optimization function trains the AI/ML model, based on the huge volume of performance data collected over days, weeks, months from O-RAN nodes. It then uses the AI/ML model to predict the traffic demand patterns of 5G networks in different times and locations for each network slice, and automatically re-allocates the network resources ahead of the network issues surfaced.

The resource quota policies associated with RAN NFs (E2 nodes) included in the respective NSSIs enable 5G network providers to optimize or prioritize the utilization of the RAN resources across slices and supports the flexibility to share resources optimally across critical service slices during resource surplus or scarcity. For example, an NSSI allocated for premium service can receive a major share of the resources compared to a slice allocated for a standard/best-effort service. Another such example is the scenario of additional resource allocation for emergency services. An important consideration here is that the NSSI resource quota policies focus on maximization of resource utilization across the NSSIs. The resource quota policies can be used as a constraint for resource allocation that defines the range of resources that can be allocated per slice. One use case for applying such a constraint is the analysis and decision based on history of resource allocation failure that can be reflected in the RAN node measurements. Here resource quota policy can be provisioned to control the minimum, maximum and dedicated resources that need to be allocated based on the historical pattern.

The NSSI resource allocation optimization on the Non-RT RIC is shown in figure 4.12.1-1, and can consist of the following steps:

1) Monitoring: monitor the radio network(s) by collecting data via the O1 interface, for example including the following performance measurements that are measured on per S-NSSAI (3GPP TS 28.552 [6] shall apply):

Mean DL PRB used for data traffic (3GPP TS 28.552 [6], clause 5.1.1.2.5 shall apply) Mean UL PRB used for data traffic (3GPP TS 28.552 [6], clause 5.1.1.2.7 shall apply) Average DL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.1 shall apply)

Average UL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.3, shall apply) Number of PDU sessions requested to setup (3GPP TS 28.552 [6], clause 5.1.1.5.1 shall apply) Number of PDU sessions successfully setup (3GPP TS 28.552 [6], clause 5.1.1.5.2 shall apply) Distribution of DL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.2 shall apply) Distribution of UL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.4 shall apply) Number of DRBs successfully setup (3GPP TS 28.552 [6], clause 5.1.1.10.2 shall apply)

NOTE 1: The above measurements are indicative and are subject to change based on the progress of this use case in O-RAN.

NOTE 2: Monitoring of the measurements related to O-Cloud (or transport network) that can be required for NSSI resource optimization is not defined in the present document.

2) Analysis & decision: consisting of the following steps:

2a. Utilize AI/ML models to analyze the measurements and predict the future traffic demand, including the RRMPolicyRatio IOC limits, for each NSSI for a given time and location.   
2b. Determine the actions needed to add or reduce the resources (e.g. capacity, VNF resources, slice subnet attributes (3GPP TS 28.541 [5] shall apply, etc.) for the RAN NFs (E2 nodes included in the respective NSSI at the given time, and location.

3) Execution: execute the actions to reallocate the NSSI resources that include:

3a. Re-configure the NSSI attributes, including RRMPolicyRatio IOC (3GPP TS 28.541 [5] shall apply) via the OAM Functions in SMO which uses O1 interface to configure the E2 nodes.

3b. Update the cloud resources via the O2 interface.

![](images/e437ae232c8c9b55297654bdab4d18f8aec68cdb90bd5ea09fd8628d45f43abc.jpg)

> **Image Summary:** {"image": "image.png"}


# Figure 4.12.1-1: The realization of NSSI resource allocatıon optimization over Non-RT RIC

For association of resource quota policies for the RAN NFs (E2 nodes) per NSSI or group of NSSIs, RRMPolicyRatio IOC (realization of abstract IoC RRMPolicy_) is currently being specified in 3GPP TS 28.541 [5] which allows definition of maximum, minimum and dedicated values for the percentage of resources to be used per RRMPolicyMemberList –

that is group of members with specific plmnID and sNSSAI (applied at NRCellDU, NRCellCU, GNBDUFunction, GNBCUCPFunction or in GNBCUUPFunction) via RRMPolicyManagedEntity.

# 4.12.2 Entities/resources involved in the use case

1) SMO:

a) Pre-provision the default NSSI resource quota policy as constraint for NSSI resource allocation optimization. This information is optionally used by the Non-RT RIC in case the resource quota that needs to be allocated per slice is not specified during the slice creation and for conflict resolution at the time of resource scarcity.

2) Non-RT RIC:

a) Collect the performance measurements related to NSSI resource usage from the O-RAN nodes via the O1 interface.   
b) Train the AI/ML model based on the analysis of historical performance measurements, to predict of the traffic demand patterns of NSSI at different times and locations.   
c) Determine the time/date and locations (i.e. which O-RAN nodes) to add or reduce the resources (e.g. capacity, VNF resources, slice subnet attributes (3GPP TS 28.541 [5] shall apply), RRMPolicyRatio IOC, etc.) for a given NSSI based on inference.   
d) Perform the following action(s) to optimize the NSSI resource allocation, at the time determined by the model. i. Re-configure the NSSI attributes via the O1 interface. ii. Update the cloud resources via the O2 interface.

3) RAN nodes (O-CU-CP, O-CU-UP, O-DU, O-RU):

a) Support the performance measurement collection with required granularity over O1 interface.   
b) Support the configuration related to the NSSI resource allocation update over O1 interface.

# 4.12.3 Solutions

# 4.12.3.1 NSSI resource allocation optimization

The context of the NSSI resource allocation optimization is captured in table 4.12.3.1-1.

Table 4.12.3.1-1: NSSI resource allocation optimization   

<table><tr><td rowspan=1 colspan=1>Use Case stage</td><td rowspan=1 colspan=1>Evolution/Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>To automatically optimize the NSSI resource allocation by leveraging the Al/MLmodel that was trained via the analysis of performance measurements collectedfrom the RAN nodes.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO: Pre-Provision the default resource quota policy as constraint for resourceallocation optimization and monitor runtime context change.Non-RT RIC: Analysis of performance measurements and Al/ML model trainingRAN nodes (O-CU-CP, O-CU-UP, O-DU, O-RU): performance measurementscollection and configuration changes execution.O-Cloud M&amp;O: The cloud resources modification via the O2 interface.OAM functions: Part of SMO which manages the O1 based OAM functionality.O-Cloud: Manages virtualization infrastructure and virtualized resources .</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>- All relevant functions and components are instantiated.- Non-RT RIC is able to receive performance measurements from RAN nodes viathe O1 interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>- RAN is operational.- OAM function is pre-provisioned with default NSSI resource quota policy - Non-RT RIC has been collecting the RAN performance measurements from RAN nodes.</td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>An Al/ML model has been trained based on the analysis of performancemeasurements predict of the traffic demand patterns of NSSI at different times andlocations, resource quora per slice.</td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Non-RT RIC collects the RAN performance measurements from RAN nodes.</td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>i. Non-RT RIC utizes the Al/ML models to analyze the measurements and predictfuture the traffic demand for each NSSI for a given time and location.li. Non-RT RIC determines the action based on model inference to update the NSSIresources that can include the following information:a) the time/dateb) locations (e.g. gNB ID)c) NSSIIDd) slice subnet attributese) VNF resources update (e.g. scaling in/out)f) NSSI resource quota policy to be enforced per slice over O1 interface</td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RIC executes the action at the time determined by the model inference byperforming the following operations:a) Re-configure the slice subnet attributes, including RRMPolicyRatio IOC(3GPP TS 28.541 [5] shall apply) via the OAM functions in SMO which uses O1interface to configure the E2 nodes.b) Request O-Cloud M&amp;O to update the O-Cloud resources via the O2interface.The execution of these steps is carried out by SMO based on the recommendationof the Non-RT RIC.</td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>All the steps identified above are successfully completed.</td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>One of the steps identified above fails.</td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Near-RT RIC continues monitoring the NSSI resource usages.</td></tr></table>

The flow diagram of the NSSI resource allocation optimization is given in figure 4.12.3.1-1.

![](images/57f7606fbc44122fc06fb8bc14a2c7ec13bc651eb9f1e747447d0e03b85f966a.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.12.3.1-1: NSSI resource allocation optimization flow diagram

# 4.12.4 Required data

The measurement counters, as specified in 3GPP TS 28.552 [6], which are measured on per S-NSSAI include:

Mean DL PRB used for data traffic (3GPP TS 28.552 [6], clause 5.1.1.2.5 shall apply) Mean UL PRB used for data traffic (3GPP TS 28.552 [6], clause 5.1.1.2.7 shall apply) Average DL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.1 shall apply) Average UL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.3 shall apply) Number of PDU sessions requested to setup (3GPP TS 28.552 [6], clause 5.1.1.5.1 shall apply) Number of PDU sessions successfully setup (3GPP TS 28.552 [6], clause 5.1.1.5.2 shall apply) Distribution of DL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.2 shall apply) Distribution of UL UE throughput in gNB (3GPP TS 28.552 [6], clause 5.1.1.3.4 shall apply)

Number of DRBs successfully setup (3GPP TS 28.552 [6], clause 5.1.1.10.2 shall apply)

NOTE: The above measurements are indicative and are subject to change based on the progress of this use case in O-RAN. The monitoring of the measurements related to O-Cloud (or transport network) that can be required for NSSI resource optimization is not defined in the present document.

# 4.13 Local indoor positioning in RAN

This use case provides the background and motivation for the O-RAN architecture to support local indoor positioning.

# 4.13.1 Background and goal of the use case

Real-time indoor positioning based on cellular network has aroused attention with the development of 5G vertical industries, individuals and operators. NR positioning is introduced by 3GPP Rel.16. The Location Management Function (LMF) resides in core network request the NG-RAN node to report positioning measurements, which is used by LMF to compute the location of UE. The messages between LMF and the NG-RAN need the AMF to route transparently. However, this long route messages between the NG-RAN node and centralized LMF can suffer network jitters and leads to un-realtime UE location results.

The main objective is to ensure local positioning be supported within the O-RAN architecture and its open interfaces. In the context of O-RAN architecture, the positioning function can be deployed as a positioning xApp in the Near-RT RIC. The positioning xApp computes the UE location and optional velocity based on the positioning measurement obtained via the E2 interface. The local indoor positioning results can be acquired via positioning xApp to support positioning applications (e.g., indoor navigation, electric security fence, etc.).

# 4.13.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Retrieve necessary positioning-related indicators (e.g., RSSI, labeled user location by manual or by minimal drive test, etc.) from positioning measurement report or network level measurement report or enrichment information from SMO (can acquire data from application). The data is for constructing/training relevant AI/ML model that will be deployed in Near-RT RIC to assist in the position computation function.   
b) Training of potential ML models for real-time positioning optimization, which can be used to compute the position, correct positioning errors, and predict motion.   
c) Send policies/intents to Near-RT RIC to drive the positioning optimization at RAN level.

2) Near-RT RIC:

a) Support selection of positioning algorithms (e.g., according to QoS requirements, etc.).   
b) Support the calculation of positioning results based on the measurements from RAN.   
c) Support update of AI/ML models from Non-RT RIC.   
d) Support execution of the AI/ML models from Non-RT RIC, e.g., positioning result calculation.   
e) Sending positioning results to Non-RT RIC for evaluation and optimization.

3) RAN:

a) Support positioning related measurement report over E2 interface.   
b) Support positioning related measurement report over O1 interface.

4) Application server:

a) Request/subscribe RAN analytics information from Near-RT RIC.   
b) Support positioning related enrichment information (e.g., labeled user location by manual or by minimal drive test, etc.) to SMO.

# 4.13.3 Solutions

# 4.13.3.1 Local indoor positioning in RAN (1)

The context of the local indoor positioning in RAN (1) is captured in table 4.13.3.1-1.

Table 4.13.3.1-1: Local indoor positioning in RAN (1)   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Expose positioning results to external applications.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Near-RT RIC, SMO, application server</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>Editor&#x27;s note: Security related procedure is not defined in the presentdocument.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The application server wants to request/subscribe RAN positioningresults of target UE.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Application server sends positioning request of target UE to Near-RT RICor subscribes positioning results from Near-RT RIC to get periodic orevent triggered position reporting.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Near-RT RIC receives the request or subscription from application serverand requests or subscribes measurements to RAN through E2 interface.The Near-RT RIC selects the positioning algorithm based on the requestor the measurement data from RAN.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>RAN reports the measurements to Near-RT RIC according to the requestor subscription.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Near-RT RIC calculates the positioning results based on themeasurement report from RAN, using the selected positoning algorithm.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>Near-RT RIC sends the response or notification command to exposeradio performance analytics towards application server.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Application server gets response or sends subscription deletion towardthe Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the local indoor positioning in RAN (1) is given in figure 4.13.3.1-1.

![](images/b327d550ad75772e60cbc987daa6e8cf805c65e5beed1dafedef18d011e32a48.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.13.3.1-1: Local indoor positioning in RAN (1) flow diagram

# 4.13.3.2 Local indoor positioning in RAN (2)

The context of the local indoor positioning in RAN (2) is captured in table 4.13.3.2-1.

Table 4.13.3.2-1: Local indoor positioning in RAN (2)   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Expose positioning results to external applications.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO, application server</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/O1 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Positioning related models have been deployed in Non-RT RIC and Near-RT RIC respectively.Editor's note: Security related procedure is not defined in the presentdocument.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The application server wants to request/subscribe RAN positioning resultsof target UE.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Application server sends positioning request of target UE to Near-RT RICor subscribes positioning results from Near-RT RIC to get periodic or eventtriggered position reporting.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Near-RT RIC receives the request or subscription from application serverand requests or subscribes measurements to RAN through E2 interface.The Near-RT RIC selects the positioning algorithm based on the requestor the measurement data from RAN and can update the positioning relatedmodels from Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">RAN reports the measurements to Near-RT RIC according to the requestor subscription.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Near-RT RIC calculates the positioning results based on the positiongreport from RAN, usingthe selected positoning algorithm.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Near-RT RIC sends the response or notification command to expose radioperformance analytics towards application server. Near-RT RIC can alsopass the positioning results to the Non-RT RIC for further analysis.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Application server gets response or sends subscription deletion toward theNear-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the local indoor positioning in RAN (2) is given in figure 4.13.3.2-1.

![](images/b4c9132206ac440ec403755156a297bcb565e2095433b21bd776e8449691dcc4.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.13.3.2-1: Local indoor positioning in RAN (2) flow diagram

# 4.13.4 Required data

Multi-dimensional data are expected to be retrieved by Non-RT RIC for AI/ML model training and policies/intents generation.

1) Network level measurement report, including UE level radio channel information, mobility related metrics, e.g., RSRP, RSSI, etc.   
2) Positioning measurement report, including UE level E-CID, OTDOA, UTDOA, TOA, RSSI, AOA, etc.   
3) Enrichment information (optional) collected from SMO (can acquire data from application), can including labeled user location by manual or by minimal drive test, etc.

Near-RT RIC required data to select the positioning algorithm and calculate the positioning results.

1) Positioning measurement report, including UE level E-CID, OTDOA, UTDOA, TOA, RSSI, AOA, etc.   
2) Performance requirements in positioning requests (optional) such as QoS.

# 4.13.4.1 RAN analytics information

Radio performance analytics data are expected to be exposed by Near-RT RIC to application server.

1) UE positioning results, including location coordinates, coordinate system, position methods used (in the case of success indication provided), failure cause (in the case of failure indication provided), achieved location QoS accuracy (optional).   
2) Velocity estimation (optional).

# 4.14 Massive SU/MU-MIMO grouping optimization

Void

# 4.15 O-RAN signalling storm protection

This use case provides the background, motivation, and requirements for the O-RAN signaling storm protection use case, allowing protecting the mobility network against signaling storms initiated by devices.

# 4.15.1 Background and goal of the use case

Society is increasingly dependent on network connectivity at any time and in any place and increasing diversity of device types ranging from complex devices such as smart phone to very simple and low-cost IoT devices are connecting to the network. The sheer number of connected devices, as well as the wide range of device types, makes the mobility network subject to accidental or intentional attacks that can disrupt the regular usage of the network. Given that life-critical applications are moving to wireless networks, such network disruptions are not only an inconvenience but can have impact on life and health of individuals. The O-RAN architecture offers an opportunity to address such security challenges in customizable and creative ways by utilizing the Near-RT RIC xApps and Non-RT RIC rApps.

Currently, the main defense mechanism standardized in 3GPP against attacks coming from the devices toward the network is based on configuration of the devices themselves and trust that the devices will indeed comply with restrictions defined by mobility standards. One such defense mechanism is the back-off timer that restricts the number of repeated device registrations, thus preventing devices from overloading the network with attaches. If this trust is breached there are no other options for defending the network rather than rejecting (denying service) randomly to both benign and malicious devices, a state which is equivalent to DDoS. Unfortunately, even today the network has few hundreds of device types that under certain conditions accidently breach this trust and allow devices to aggressively attach to the network in a rate of few thousand times per hour (the maximum allowed number by standard is less than 20 attaches per hour). An attacker that finds a way to manipulate vulnerabilities in a large set of these devices remotely can cause an attach storm that could lead to a long outage of large parts of the network. Furthermore, this attacker can continue this attack over many hours, each time picking few thousand of devices from a large pool of millions of vulnerable devices connected to the same carrier network; the network carrier will not be able to stop this attack without intelligent and fine-grained controls to act against a certain patterns of behavior.

Fortunately detecting these aggressive devices is possible as their behavior is very different from the other devices in the network. What the network really needs is to apply dynamic restriction over these devices to prevent them from overloading the control plane of the network. This restriction should be smart enough to still allow benign devices to register to the network without interruption. Having smart security control at the RAN can stop such attack and without overloading deeper parts of the network in the core.

The goal of this use case is utilizing O-RAN to detect and mitigate signaling storms DDoS quick and as close to the network edge, thus minimizing affected network nodes. The Near-RT RIC would detect these signaling storms by analyzing signaling events from RAN nodes it controls. When such a storm is detected the Near-RT RIC creates fine grained filters, which cover the aggressive UEs that cause the storm. These UEs registration requests will then be blocked/throttled while the behaving UEs will continue to get service as usual. In some cases, the attack can be spread across many locations. It could be that the volume of signaling per location has not crossed a critical threshold but the moderate increase in many locations do cause an overload of central nodes such as the network core elements. In this case a network-wide view is required; thus, the Non-RT performs the network-wide analysis and in the case of a network signaling storm, it pushes policies to the local Near-RT RIC to adjust detection parameters to reduce the moderate increase of signaling from a set of one or more E2 nodes. This combined view of both Non-RT RIC and Near-RT RIC ensures quick reaction to local signaling storms as well as response to widely distributed attacks.

While flows in this use case focus on the signaling storm scenario, they could be easily extended to include other attack scenarios both in terms of detection and mitigation. For example, the scenario where rogue devices report false CQI measurements that indicate high values while the real channel quality is poor. When exploited by attackers and applied to large set of devices this attack can cause to waste of radio resources and eventually to DoS. Detection of the attack can be achieved by analyzing anomalous CQI reports, or abnormal volume of NACK messages based on signaling messages. For mitigation actions either rejecting the rogue devices or limiting radio resources can be applied.

# 4.15.2 Entities/resources involved in the use case

1) Non-RT RIC in SMO domain:

a) Maintains overall view of network wide phenomenon of signaling storms using signaling storm detection rApp. The detection of distributed signaling storms that spread over many geographical locations and are more difficult to be observed locally. This overall view is broken down by location and corresponding policies are pushed to specific instances of Near-RT RIC to respond to abnormal signaling activity in affected geographical areas, over the A1 interface.   
b) Uses enrichment data from non-RAN source (i.e., 5G core or probing framework) to maintain global view and support more accurate detection and classification of attacks.   
c) Utilizes AI/ML models in the signaling storm detection rApp that monitor network-level signaling behavior to support signaling anomalies detection.

2) Near-RT RIC in RAN domain:

a) Monitors E2 interface for connection establishment messages and identifies abnormal levels of signaling activity using the signaling storm detection xApp.   
b) Signaling storm mitigation xApp utilizes policies over E2 to enforce appropriate mitigation action (e.g., reject, throttle, alert) over misbehaving UEs connection establishment.   
c) Signaling storm detection xApp utilizes AI/ML models that monitor cell-level signaling behavior to support signaling anomalies detection.   
d) Applies appropriate detection policy based on policies received from Non-RT RIC (e.g., false-positive levels, UE thresholds, throttling ratios).

3) E2 nodes in RAN domain:

a) Support sending connection establishment messages over the E2 interface. b) Support control and policy enforcement from Near-RT RIC over E2 interface

# 4.15.3 Solutions

# 4.15.3.1 Mode 1 – Local signaling storm protection policy

The context of the local signaling storm protection policy is captured in table 4.15.3.1-1.

Table 4.15.3.1-1: Local signaling storm protection policy   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Detect localized signaling storms based on "default parameters" and applypolicy to mitigate the attack.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Near-RT RIC: Detection of local cell-level signaling storms; execution ofmitigation policies and controls, maintenance of cell-level normal behaviormodels.E2 nodes: Execute mitigation policies, collects and reports RAN signalingevents and policy specific statistics over E2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated. Signaling stormsdetection and signaling storm mitigation xApps are deployed over E2 with initialconfiguration.E2 interface connectivity is established with Non-RT RIC and RAN respectively.Data report, policy and control subscription established on E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network is operational.SMO has established the data collection and sharing interface with Non-RTRIC.Near-RT RIC already established relevant detection mechanisms of normalsignaling behavior and adjusted detection parameters accordingly. Non-RTRIC analyzes the historical data from RAN, develops, trains with help of SMO functions and deploys the models or algorithm as part of the signaling stormdetection xApp to the Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Network is in normal state (attack is described later on).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Signaling storm detection xApp subscribes on connection establishmentsignaling messages report from the RAN over the E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">E2 node sends report to signaling storm detection xApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm detection xApp monitors reports to detectaggressive UEs that act with abnormal signaling.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 4-7 (M)</td><td colspan="1" rowspan="1">UEs send establish connection messages and E2 node accepts theserequests.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">E2 node sends a connection establishment reports.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Signaling storm detection xApp detects aggressive activity.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">Signaling storm detection xApp updates signaling storm mitigation xApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm mitigation xApp creates a filter to block/throttlesignaling messages from the aggressive UEs. Filter is applied in the E2 nodesas POLICY + REPORT to track filter activity. Near-RT RIC shall notify the Non-RT RIC to avoid conflicts.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">Aggressive UE sends connection establishment message.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">E2 node evaluate policy with respect to the connection establishmentmessage.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">E2 node rejects/throttles connection establishment request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">Near-RT RiC signaling storm mitigation xApp receives relevant signalingmessages that the POLICY filter blocked/ throttled to track changes in attack</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">status and aggressive devices list of UEs blocked, blocked signaling volume,trend).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm mitigation xApp is finds that some devices are no longer aggressive or no longer present. It decides to update filter by updatingthe E2 node POLICY.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17-19 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm detection xApp detects a new set of aggressivedevices and updates the signaling storm mitigation xApp, which updates thefilter by updating the E2 node POLICY.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 20-21 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm mitigation xApp evaluates signaling level anddecides that there is no more aggressive UE activity. The xApp removes theE2 node policy.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Attack is over and signaling messages level is back to normal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Return to normal signaling activity monitoring (step 1).</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the local signaling storm protection policy is given in figure 4.15.3.1-1.

![](images/67b9c5c0bd4cb7163ef5324ae1cf1a34e45c541f8a51117add35cd6b18fb17a6.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.15.3.1-1: Local signaling storm protection policy flow diagram

# 4.15.3.2 Mode 1 – Local signaling storm protection insert-control (optional)

The context of the local signaling storm protection insert-control is captured in table 4.15.3.2-1.

Table 4.15.3.2-1: Local signaling storm protection insert-control   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>Detect localized signaling storms based on "default parameters" and apply control to mitigate the attack.</td><td rowspan="3"></td></tr><tr><td>Actors and Roles</td><td>Near-RT RIC: Detection of local cell-level signaling storms; execution of mitigation policies and controls, maintenance of cell-level normal behavior models. E2 nodes: Execute UE level mitigation policies, collects and reports RAN</td></tr><tr><td rowspan="2">Assumptions</td><td rowspan="2">signaling events and policy specific statistics over E2. All relevant functions and components are instantiated. Signaling storms detection and signaling storm mitigation xApps are deployed over E2 with initial</td></tr><tr><td rowspan="3">configuration.</td></tr><tr><td></td><td>E2 interface connectivity is established with Non-RT RIC and RAN respectively. Data report, policy and control subscription established on E2 interface.</td></tr><tr><td rowspan="3">Pre-conditions</td><td>Network is operational. SMO has established the data collection and sharing interface with Non-RT RIC.</td></tr><tr><td>Near-RT RIC already established relevant detection mechanisms of normal signaling behavior and adjusted detection parameters accordingly. Non-RT RIC analyzes the historical data from RAN, develops, trains with help of SMO</td></tr><tr><td>functions and deploys the models or algorithm as part of the signaling storm detection xApp to the Near-RT RIC.</td></tr><tr><td>Begins when</td><td>Network is in normal state (attack is described later on).</td><td></td></tr><tr><td>Step 1 (M)</td><td>Signaling storm detection xApp subscribes on connection establishment signaling messages report from the RAN over the E2 interface.</td><td></td></tr><tr><td>Step 2 (M)</td><td>E2 node sends report to signaling storm detection xApp.</td><td></td></tr><tr><td>Step 3 (M)</td><td>Near-RT RIC signaling storm detection xApp monitors reports to detect aggressive UEs that act with abnormal signaling.</td><td></td></tr><tr><td>Steps 4-7 (M)</td><td>UEs send establish connection messages and E2 node accepts these requests.</td><td></td></tr><tr><td>Step 8 (M)</td><td>E2 node sends a report indicating aggressive devices behavior.</td><td></td></tr><tr><td>Step 9 (M)</td><td>Signaling storm detection xApp detects aggressive activity.</td><td></td></tr><tr><td>Step 10 (M)</td><td>Signaling storm detection xApp updates signaling storm mitigation xApp.</td><td></td></tr><tr><td>Step 11 (M)</td><td>Signaling storm mitigation xApp updates subscription to INSERT-CONTROL. Use control filter to block/throttle aggressive UEs by rejecting some of the</td><td></td></tr><tr><td>Step 12 (M)</td><td>messages. E2 node receives another connection establishment from an aggressive UE.</td><td></td></tr><tr><td>Step 13 (M)</td><td>E2 node forwards the message to the signaling storm mitigation xApp.</td><td></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">Signaling storm mitigation xApp determines that message is from anaggressive device.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">Signaling storm mitigation xApp sends a reject/throttle message to the E2node.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">E2 node rejects/throttles connection establishment request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">Signaling storm mitigation xApp continues to monitor its control filter.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (M)</td><td colspan="1" rowspan="1">Near-RT RIC DDoS mitigation xApp evaluates signaling level and decides thatthere is no more aggressive UE activity. The xApp updates subscription backto REPORT.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Attack is over and signaling messages level is back to normal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the local signaling storm protection insert-control is given in figure 4.15.3.2-1.

![](images/6cddbcf4ecb0601b4b2ecdbe10cd3579a903a57ecd97365dc0225e2aa6736999.jpg)

> **Image Summary:** {"image": "image_from_user.png"}
  
Figure 4.15.3.2-1: Local signaling storm protection insert-control flow diagram

# 4.15.3.3 Mode 2 – Distributed signaling storm protection

The context of the distributed signaling storm protection is captured in table 4.15.3.3-1.

Table 4.15.3.3-1: Distributed signaling storm protection

<table><tr><td colspan="3"></td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt;</td></tr><tr><td>Goal</td><td>Detect distributed signaling using Non-RT RIC and A1 policy initiates mode 2 handling in Near-RT RIC with "stricter parameters" mitigation.</td><td>Related use</td></tr><tr><td>Actors and Roles</td><td>Non-RT RIC: Detection of network-level distributed signaling storms, maintenance of cell-level, network slice level and node level normal behavior models. Near-RT RIC: Detection of local cell-level signaling storms; execution of mitigation policies and controls, maintenance of cell-level normal behavior models.</td><td></td></tr><tr><td>Assumptions</td><td>RAN: Executes UE level or network slice level mitigation policies, collects and reports RAN signaling events and policy specific statistics over E2. All relevant functions and components are instantiated. Signaling storms detection and signaling storms mitigation xApps are deployed over E2 with initial configuration. A1, E2 interface connectivity is established with Non-RT RIC and RAN respectively.</td><td></td></tr><tr><td>Pre-conditions</td><td>Data report, policy and control subscription established on E2 interface. Network is operational. SMO has established the data collection and sharing interface with Non-RT RIC. Non-RT RIC and Near-RT RIC already established relevant detection mechanisms of normal signaling behavior and adjusted detection parameters accordingly. Non-RT RIC analyzes the historical data from RAN, develops,</td><td></td></tr><tr><td>Begins when</td><td>trains with help of SMO functions and deploys the models or algorithm as xApps to the Near-RT RIC. Network is in normal state when (attack is described later on).</td><td></td></tr><tr><td>Step 1 (M)</td><td>OAM functions start to collect Enrichment Information (Els) from external sources (e.g. network core probing framework).</td><td></td></tr><tr><td>Step 2 (M)</td><td>OAM functions start to collect alarms &amp; metrics from E2 nodes. OAM functions sends signaling statistics based on collected information to</td><td></td></tr><tr><td>Step 3 (M)</td><td>Non-RT RIC.</td><td></td></tr><tr><td>Step 4 (M)</td><td>Non-RT RIC uses Al/ML model to analyze overall network signaling activity levels based on signaling statistics. Non-RT RIC applies initial configurations to all Near-RT RIC elements</td><td></td></tr><tr><td>Step 5 (M)</td><td>regarding detection and mitigation parameters, including: accepted signaling volume thresholds, throttle/block ratio, accepted false negative levels, filter pause periods, etc.</td><td></td></tr><tr><td>Step 6 (M)</td><td>Non-RT RIC detects distributed signaling storm activity originated from a list of locations.</td><td></td></tr><tr><td>Step 7 (M)</td><td>Non-RT RIC updates configuration to a stricter one in the relevant Near-RT RIC</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Step 8 (M)</td><td>3.15.3.2 with stricter configuration (e.g. lower thresholds).</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>locations over A1 interface.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>Near-RT RIC performs detection and mitigation as described in 3.15.3.1 or</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Non-RT RiC determines that distributed signaling storm attack is over basedon signaling statistics information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">Non-RT RIC updates Near-RT RICs back to initial configuration parametersover the A1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Near-RT RIC signaling storm detection xApp observed aggressive behaviorwhere temporal identifiers cannot be correlated with the underlying devices.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">Near RT RIC alarms the OAM functions over O1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">OAM functions report suspicious behavior to Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">Non-RT RIC sends enrichment information to Near-RT RIC over A1-EI tosupport detection of aggressive devices.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">Near-RT RIC performs detection and mitigation as described in 3.15.3.1 or3.15.3.2 with stricter configuration (e.g. lower thresholds).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">Non-RT RIC evaluates data and decides that there is no more distributedsignaling storm activity.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">Non-RT updates configuration of relevant Near-RT RICs over the A1 back tonormal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Attack is over and signaling messages level is back to normal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC monitors network-level signaling messages statistics.Near-RT RIC monitors cell-level signaling messages statistics.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the distributed signaling storm protection is given in figure 4.15.3.3-1.

![](images/5e6c10c00ab6bbf4cf7850d8bc45b3674f21b2e9c173cbaf7eac133817e3d1b6.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.15.3.3-1: Distributed signaling storm protection flow diagram

# 4.15.4 Required data

The measurement counters, detection within the Near-RT RIC is based upon analyzing per UE connection establishment messages events that include the following data:

1) Basic registration event parameters: timestamp, cell ID, temporary ID (e.g., C-RNTI, 5G-GUTI)

2) RAN parameters to correlate between a UE and registration events: e.g. RSRP/RSRQ, timing advance, beam ID

Tracking status of ongoing attack by monitoring statistics of active filters that include the following data:

3) Number of UEs in the filter, number of requests blocked, trend (change over last x periods of time)

Enrichment information from a non-RAN source regarding network-wide DDoS information:

4) Overloaded regions, overloaded sites, severity $\%$ above normal)

# 4.16 Congestion prediction and management

Void

# 4.17 Industrial IoT optimization

Void

# 4.18 BBU pooling to achieve RAN elasticity Void

# 4.19 Integrated SON function within the O-RAN framework

This use case provides the motivation, description, and requirements for enabling the O-RAN framework to support a minimum SON function set. This use case enables realization of SON functions in the O-RAN architectural framework to help operators address issues seen from vendor specific SON implementation in earlier generation of cellular networks.

# 4.19.1 Background and goal of the use case.

SON (Self-Organizing Network) functionalities reduces the cost of running a mobile network by providing control on aspects of network configuration and control and thus eliminating manual configuration of network elements right from initial deployment through the network operation. SON also helps better network performance and customer experience and can significantly improve OPEX-to-revenue ratio and help in realizing avoidable CAPEX.

SON is an automation technology that enables the network to set itself up and self-manage resources and configuration to achieve optimal performance. The SON functions are handled by SON algorithms either individually or in groups. SON algorithms perform functionalities like monitoring the network(s) by collecting management data including MDAS (Management Data Analytics Service) data, analysis of the data to determine issues in the network(s) and their resolution. SON intends to achieve the following:

Self-configuration: Aids in seamlessly integrating into the network through automatic configuration of key parameters (initial PCI and ANR functions).

Self-optimization: Aids in enhanced network performance through near real time optimization of radio & network configurations. It is valuable throughout the lifetime of the network and includes SON functionalities such as Mobility Load Balancing [MLB], Mobility Robustness Optimization [MRO], Random Access Channel [RACH] Optimization, etc.

Self-healing: It allows adjacent cells to maintain network quality in case a cell/sector fails, providing resiliency (reliability) in the face of unforeseen outage conditions. It is relevant throughout the lifetime of the network and includes SON functions such as cell outage detection, compensation and recovery.

The definitions for the SON functionality are specified in 3GPP TS 28.313 [20] but the realization of the SON functions is left to implementation. The SON coordination function for detecting, preventing and resolving conflicts or negative influences between multiple SON functions when there is an attempt to change some (same or associated) network configuration parameters of some (same or associated) nodes is also specified in 3GPP TS 28.313 [20]. Based on the deployment of SON algorithm, the SON solution can be termed as Centralized SON (C-SON – where the SON algorithms are executed in the 3GPP management system), Distributed SON (D-SON - where SON algorithms are executed in the network function layer) and Hybrid SON (where SON algorithm execution is spread across the network function layers and the management layers).

The objective of this use case is to enable the realization of SON functions in the O-RAN architecture framework i.e., as rApps, xApps or as management entity functions through open interfaces in a way that inter vendor interoperability issues can be addressed.

NOTE: Other deployment options other than the ones mentioned in this use case are also possible.

The scope of the integrated SON use case covers the following functions:

1. Self configuration:

PCI initial allocation and conflict resolution ANR (Automatic Neighbor Relations)

2. Self optimization:

• Mobility Load Balancing (MLB) • Mobility Robustness Optimization (MRO) • Coverage and Capacity Optimization (CCO) • RACH Optimization (RO)

Editor’s note: R1 interface needs to be shown in the UMLs.

# 4.19.2 Entities/resources involved in the use case

# 4.19.2.1 SON inventory and deployment management

1) SMO

Support SON inventory and deployment management for Non-RT RIC(s), Near-RT RIC(s) and E2 node(s).   
Support collection of SON configurations from Non-RT RIC(s), Near-RT RIC(s) and E2 node(s).   
Support decision making on setup of the SON functions in Non-RT RIC(s), Near-RT RIC(s) and E2 node(s).   
Configure Non-RT RIC(s), Near-RT RIC(s) and E2 node(s) based on the decided SON function deployment model.

2) Non-RT RIC

Support exposure of SON functionalities and configurations.   
Support configuration and setup of the SON functions from SMO.

3) Near-RT RIC

Support exposure of SON functionalities and configurations. • Support configuration and setup of the SON functions from SMO via O1 interface.

4) E2 node

Support exposure of SON functionalities and configurations.   
Support configuration and setup of the SON functions from SMO via O1 interface.

# 4.19.2.2 Self configuration (PCI conflict detection/resolution, ANR)

1) SMO

Configure self configuration SON functionality (PCI conflict detection/resolution, ANR) in Non-RT RIC, NearRT RIC or E2 node. Configure/reconfigure the respective SON related parameters and measurements in the Non-RT RIC, Near-RT RIC and E2 node. Support collection of measurements or notifications from the respective O-RAN nodes.

2) Non-RT RIC

• Retrieve necessary data from SMO. Support setup of SON function and configuration of relevant SON data inputs from SMO.   
• Support AI/ML training and inference and provide output via O1 or A1 to the relevant O-RAN nodes.

3) Near-RT RIC

Support setup of SON function and configuration of relevant SON data inputs from SMO.   
Configure and receive necessary input data for AI/ML training of SON functions.   
Support notifications to SMO related to SON functions.   
Support AI/ML training and inference and provide output to E2 node via E2 interface.   
Support inputs from Non-RT RIC for AI/ML training and conversion of policies via A1 into E2 inputs.

4) E2 node

• Support setup of SON function and configuration of relevant SON data inputs from SMO.   
• Support configuration and retrieval of necessary SON function related data for AI/ML model training via E2/O1 interfaces.   
Support policies or configuration changes or relevant inputs via E2/O1 interface to execute RRM functionalities for the respective SON functions.   
Support notifications to SMO related to SON functions.   
• Support AI/ML model inference and execute relevant RRM functionalities.

# 4.19.2.3 Self optimization (MLB, MRO, CCO, RO)

1) SMO

Configure the self optimization (MLB, MRO, CCO, RO) SON functionality in Non-RT RIC, Near-RT RIC or E2 node.

2) Non-RT RIC

• Support setup of SON function and configuration of relevant SON data inputs from SMO.   
− Configuration and collection of cell load related information, HO related reports, CCO related measurement reports (RLF (Radio Link Failure), MDT (Minimization Drive Test), RCEF (RRC Connection Establishment Failure)), RACH performance reports for constructing relevant AI/ML models to assist in the self optimization SON functionality.   
• Support AI/ML model training and inference based on the input data received.   
• Re-configure inter-site/inter-rat cell reselection parameters, HO related parameters, CCO related control parameters and RACH parameters based on AI/ML output.   
• Generate relevant A1 policies to execute any RRM function for the configured SON function.

# 3) Near-RT RIC

Support setup of SON function and configuration of relevant SON data inputs from SMO. Configuration and collection of load reports, HO related reports (HO failure and RLF), CCO related measurement reports (RLF, MDT, RCEF), RACH performance reports from E2 nodes over E2 interface. Support AI/ML model training and inference based on the input data received via O1 and E2. Re-configure HO related, cell reselection parameters, CCO related control parameters and RACH parameters based on AI/ML output. • Support initiation of RRM functions like HO initiation, trigger cell reselection at E2 node via E2 policies or controls based on AI/ML output. Support conversion of A1 policy into relevant E2 actions for executing RRM function for a specific SON function.

4) E2 node

Support setup of SON function and configuration of relevant SON data inputs from SMO.

Report Measurement Report (MR), HO related information, coverage information, RACH performance over E2/O1 interface.   
Support reconfiguration of HO related parameters, cell reselection parameters, CCO related parameters, RACH parameters based on inputs via E2 or O1 interface.   
Support initiation of RRM functions like HO initiation, cell reselection, etc. based on inputs received via E2/O1 interface.

# 4.19.3 Solutions

# 4.19.3.1 SON inventory and deployment management

The context of the SON inventory and deployment management is captured in table 4.19.3.1-1.

Table 4.19.3.1-1: SON inventory and deployment management   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Management of SON configurations of Non-RT RIC, Near-RTRIC and E2 node by the SMO.Management of deployment of SON functions in Non-RT RIC,Near-RT RIC and E2 node by the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO acting as controller for the SON inventory anddeployment management.Non-RT RIC, Near-RT RIC and E2 node acting as supportingentities by providing the required information and adhering toSON configuration by SMO.Operator providing the necessary inputs to SMO for decisionmaking on the SON function deployment.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O1 interface connectivity between the SMO and E2 node andNear-RT RIC is established.E2 interface connectivity is established between E2 node andNear-RT RIC.A1 interface connectivity is established between Near-RT RICand Non-RT RIC.Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">SMO is unaware of the SON configurations of the O-RANnodes.SMO has necessary inputs from operator to decide thedeployment of SON functions in the respective O-RAN nodes.O-RAN nodes are capable of providing their SONconfigurations to SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Network becomes operational and operator configures the SMO forSON inventory and deployment management.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1, 2, 3 (M)</td><td colspan="1" rowspan="1">Operator sets the SON targets and the SON functiondeployment model.SMO analyzes the SON targets and the SON deploymentmodel and notifies the operator on the decision.SMO inspects the SON inventory and decides on the need forretrieval of SON configuration from O-RAN nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4, 5, 6, 7, 8, 9(0)</td><td colspan="1" rowspan="1">If required, SMO initiates request to retrieve the configurationfrom O-RAN nodes in a loop until all the necessaryconfigurations are retrieved.Based on the retrieved configuration, SMO re-evaluates theSON deployment model and notifies the operator if anychanges to SON deployment model.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10, 11, 12 (O)</td><td colspan="1" rowspan="1">Alternatively, SMO can decide to configure the O-RAN nodeswith the necessary SON functions by deploying rApps or xAppsto cater to the SON deployment model.SMO can notify the operator on the rApp and xAppdeployments if needed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 - 17 (O)</td><td colspan="1" rowspan="1">Based on the revised deployment model, SMO communicates thechanges to the SON configurations and the SON function setup to theO-RAN nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (M)</td><td colspan="1" rowspan="1">The O-RAN nodes collect data, analyze, and decide if any changes areneeded to the configuration and notify operator for any modificationsdone.This is done in a loop until SON targets are met.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 19 – 27 (M)</td><td colspan="1" rowspan="1">If the SON functions need to be terminated based on inputs fromoperator, then SMO initiates deletion of SON configurations in therespective O-RAN nodes and notifies the operator when the terminationis completed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The SON functions are terminated by the operator or when the SONtargets are met.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SMO, Non-RT RIC, Near-RT RIC and E2 nodes interwork with eachother seamlessly adhering to the SON function setup input from SMO.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the SON inventory and deployment management is given in figure 4.19.3.1-1.

![](images/9e5b127e0483b55f5e69ee2284ef86188ea49a60c76a890396b3971b7f47bf0f.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.19.3.1-1: SON inventory and deployment management flow diagram

# 4.19.3.2 Self configuration (PCI conflict detection/resolution, ANR)

The context of the self configuration is captured in table 4.19.3.2-1.

Table 4.19.3.2-1: Self configuration   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable flexible deployment of the self configuration SON functions likePCI conflict detection/resolution， ANR by means of configurationparameter change, regulating RRM function actions and allowing Al/ML-based solutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO acting as parameter configuration function.Non-RT RIC/ Near-RT RIC:Configuration decision makingfunction.E2 node: Configuration enforcement function, andmeasurement reporting function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">01 interface connectivity between the SMO and E2 node,Near-RT RIC is established.E2 interface connectivity is established between E2 node andNear-RT RIC.A1 interface connectivity is established between Near-RT RICand Non-RT RIC.Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">SMO has configured the SON functions and required initial parametersin the respective O-RAN nodes via SON inventory and deploymentmanagement as shown in clause 4.19.3.1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator enables the self configuration SON functions like PCI conflictdetection/resolution, ANR and E2 node becomes operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1a, 1b, 1c (O)</td><td colspan="1" rowspan="1">Non-RT RIC initiates the specific measurement data collectionrequest towards SMO and SMO towards E2 node for AI/MLmodel training and for analysis of data for optimization.E2 node sends the configured measurement data via O1 interface to SMO and Non-RT RIC retrieves the required datafrom SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2a, 2b, 2c, 2d,2e,2f (0)</td><td colspan="1" rowspan="1">Non-RT RIC can train the Al/ML model with the collected data from O1 interface and constantly monitors the performance ofthe E2 node(s) for optimization.Based on the output of the AlI/ML processing the Non-RT RICcan trigger modification of configuration parameters throughSMO via O1 interface to E2 node.Optionally Non-RT RIC can also generate and send A1 policiesfor initiation of HO etc. to Near-RT RIC. Near-RT RIC convertsthe A1 policies to E2 actions and forwards them to E2 nodes.Non-RT RIC continues to monitor the performance of the E2nodes and re-trains the Al/ML model in a loop.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3a, 3b (O)</td><td colspan="1" rowspan="1">Near-RT RIC initiates the specific measurement data collectionrequest towards E2 node. Near-RT RIC can use the collecteddata for optionally Al/ML model training and for analysis of datafor optimization.E2 node sends the configured measurement data via E2interface to Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4a, 4b, 4c, 4d(0)</td><td colspan="1" rowspan="1">Near-RT RIC can train the Al/ML model with the collected datafrom E2 interface and constantly monitors the performance ofthe E2 node(s) for optimization.Upon trigger from the Al/ML processes, Near-RT RIC performsreconfiguration of parameters.Optionally Near-RT RIC can request initiation of certain E2node actions like HO or cell reselection, etc.Near-RT RIC continues to monitor the performance of the E2nodes and re-trains the Al/ML model in a loop.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">E2 node receives required inputs from SMO/Non-RT RIC and Near-RTRIC for execution of self configuration SON functions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6a, 6b (O)</td><td colspan="1" rowspan="1">●  Based on the inputs received and the inputs from inbuilt RRMalgorithm, E2 node reconfigures parameters related to selfconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">●   E2 node can initiate certain RRM actions like HO or cellreselection, etc.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">E2 node becomes non-operational or when the operator disables theself configuration SON functions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1">[</td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SMO/ Non-RT RIC, Near-RT RIC continues real time close loopoptimization of self configuration SON functions.The E2 node operates using the newly deployed parameters.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the self configuration is shown in figure 4.19.3.2-1.

![](images/6555a7bab23c892effac5c03e2dbb002c7344f6b3379741803ff455df97d3809.jpg)

> **Image Summary:** {"entities": ["O-RAN Architecture", "RIC", "near-RT", "far-RT", "non-RT", "O-RAN Components", "O-RU", "O-DU", "O-CU", "O-CG", "O-NF", "RAN Intelligent Controller (RIC)", "O-RAN Interfaces", "O-RAN Architectural Pattern", "O-RU Interfaces", "O-DU Interfaces", "O-CU Interfaces", "O-CG Interfaces", "O-NF Interfaces", "Open Fronthaul", "Open Mesh", "Open Core", "Reference Architectures", "Service Function Exposure"], "relationships": ["O-RAN Architecture → RIC: Service Function Exposure", "O-RAN Architecture → near-RT: provides near-RT capabilities", "O-RAN Architecture → far-RT: provides far-RT capabilities", "O-RAN Architecture → non-RT: provides non-RT capabilities", "O-RAN Components → O-RU: includes", "O-RAN Components → O-DU: includes", "O-RAN Components → O-CU: includes", "O-RAN Components → O-CG: includes", "O-RAN Components → O-NF: includes", "RAN Intelligent Controller (RIC) → near-RT: provides near-RT capabilities", "RAN Intelligent Controller (RIC) → far-RT: provides far-RT capabilities", "RAN Intelligent Controller (RIC) → non-RT: provides non-RT capabilities", "O-RAN Interfaces → Open Fronthaul: describes", "O-RAN Interfaces → Open Mesh: describes", "O-RAN Interfaces → Open Core: describes", "Reference Architectures → Service Function Exposure: describes"], "hierarchy": ["O-RAN Architecture = RIC + near-RT + far-RT + non-RT", "O-RAN Components = O-RU + O-DU + O-CU + O-CG + O-NF", "O-RAN Interfaces = Open Fronthaul + Open Mesh + Open Core"], "flows": [], "notes": ["Figure 4.2-1: O-RAN Architectural Pattern"]}
  
Figure 4.19.3.2-1: Self configuration

# 4.19.3.3 Self optimization (MLB, MRO, CCO, RO)

The context of the self optimization is captured in table 4.19.3.3-1.

Table 4.19.3.3-1: Self optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="2" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="2" rowspan="1">Enable flexible optimization of the self optimizing SON functions likeMRO, MLB, CCO and RACH by means of configuration parameterchange, regulating RRM function actions and allowing Al/ML-basedsolutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="2" rowspan="1">• SMO acting as parameter configuration function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="2" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">●  Non-RT RIC/ Near-RT RIC: Self optimization decision makingfunction.E2 node: Configuration enforcement function, andmeasurement reporting function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="2" rowspan="1">O1 interface connectivity between the SMO and E2 node,Near-RT RIC is established.E2 interface connectivity is established between E2 node andNear-RT RIC.A1 interface connectivity is established between Near-RT RICand Non-RT RIC.• Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="2" rowspan="1">SMO has configured the SON functions and required initial parameters in the respective O-RAN nodes via SON inventory and deploymentmanagement as shown in clause 4.19.3.1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="2" rowspan="1">Operator enables the optimization functions for SON functions like MRO,MLB, CCO or RACH and E2 node becomes operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1a, 1b, 1c (O)</td><td colspan="2" rowspan="1">Non-RT RIC initiates the specific measurement data collectionrequest towards SMO and SMO towards E2 node for Al/MLmodel training and for analysis of data for optimization.E2 node sends the configured measurement data via 01interface to SMO and Non-RT RIC retrieves the required datafrom SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2a, 2b, 2c, 2d,2e, 2f (O)</td><td colspan="2" rowspan="1">Non-RT RIC can train the Al/ML model with the collected datafrom O1 interface and constantly monitors the performance ofthe E2 node(s) for optimization.Based on the output of the Al/ML processing the Non-RT RICcan trigger modification of configuration parameters throughSMO via O1 interface to E2 node.Optionally Non-RT RIC can also generate and send A1 policiesfor initiation of HO etc to Near-RT RIC. Near-RT RIC convertsthe A1 policies to E2 actions and forwards them to E2 nodes.Non-RT RIC continues to monitor the performance of the E2nodes and re-trains the Al/ML model in a loop.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Use Case Stage</td><td colspan="2">Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Step 3a, 3b (0)</td><td></td><td>Near-RT RIC initiates the specific measurement data collection request towards E2 node. Near-RT RIC can use the collected data to optionally train the Al/ML model and for analysis of data for optimization. E2 node sends the configured measurement data via E2</td><td rowspan="6"></td></tr><tr><td rowspan="5">Step 4a, 4b, 4c, 4d (0)</td><td></td><td>interface to Near-RT RIC. Near-RT RIC can train the AlI/ML model with the collected data from E2 interface and constantly monitors the performance of</td></tr><tr><td>the E2 node(s) for optimization. reconfiguration of parameters related to self optimization.</td><td>Upon trigger from the AI/ML processes, Near-RT RIC performs</td></tr><tr><td></td><td>Optionally Near-RT RIC can request initiation of certain E2</td></tr><tr><td></td><td>node Actions like HO or cell reselection, etc. Near-RT RIC continues to monitor the performance of the E2</td></tr><tr><td></td><td>nodes and re-trains the Al/ML model in a loop.</td></tr><tr><td>Step 5 (0)</td><td></td><td>E2 node receives required inputs from SMO/Non-RT RIC and Near-RT RIC for execution of self optimization SON functions.</td><td></td></tr><tr><td>Step 6a, 6b (O)</td><td>●</td><td>Based on the inputs received and the inputs from inbuilt RRM algorithm E2 node reconfigures parameters related to self optimization. E2 node can initiate certain RRM Actions like HO or cell</td><td></td></tr><tr><td>Ends when</td><td></td><td>reselection, etc. E2 node becomes non-operational or when the operator disables the optimization functions for SON functions like MRO, MLB, CCO or RACH.</td><td></td></tr><tr><td>Exceptions</td><td></td><td>One of the steps identified above fails.</td><td></td></tr><tr><td>Post Conditions</td><td></td><td>SMO/Non-RT RIC, Near-RT RIC continues real time close loop optimization of self optimization SON functions. The E2 node operates using the newly deployed parameters.</td><td></td></tr></table>

The flow diagram of the self optimization is given in figure 4.19.3.3-1.

![](images/02387a07a736f21f34b21f10647b6659e6a75bca6b197b32d372944b9ee3cc53.jpg)

> **Image Summary:** {"image": "o-ran_image.png"}
  
Figure 4.19.3.3-1: Self optimization

# 4.19.4 Required data

4.19.4.1 Self configuration (PCI conflict detection/resolution, ANR)

1) SMO

Network topology, GPS coordinates of the E2 nodes, PCI allocation range as inputs from operator   
Information on PCI confusion or PCI conflict from E2 node via O1 interface   
Neighbor information (PCI, ECGI, PLMN, TANAC, TAC, frequency bands) based on network topology as input   
from operator

2) Non-RT RIC/Near-RT RIC and E2 node

• 3GPP RRC measurement reports with PCI information of the neighboring cells via E2 interface • PCI allocation range via O1 interface from SMO

• Information on PCI confusion or PCI conflict from E2 node via O1 interface • Neighbour cell relation table information of the neighboring cells via E2 interface 3GPP XN, X2 and NG mobility related messages via E2 interface from E2 node

# 4.19.4.2 Self optimization (MLB, MRO, CCO, RO)

1) Non-RT RIC/Near-RT RIC and E2 node

MLB - Load reports from Xn/X2/F1/E1 interface resource status reporting procedures and Xn, X2 and NG mobility messages defined in 3GPP via E2 interface from E2 node.   
MLB - HO trigger control parameters available as specified in 3GPP TS 28.313 [20], clause 7.1.5 to E2 node via E2 interface or O1 interface.   
MRO - Xn, X2 and NG HO reports, RLF reports, NG uplink and downlink RRC transfer messages, UE history information, coverage, and quality information and XN/NG/X2 mobility related messages defined in 3GPP via E2 interface from E2 node.   
• MRO - HO target and control parameters available as specified in 3GPP TS 28.313 [20], clause 7.1.2 to E2 node via E2 interface or O1 interface.   
• CCO – RLF, MDT, measurement reports and RCEF related reports defined in 3GPP via E2 interface from E2 node.   
• CCO related control parameters and control information available as specified in 3GPP TS 28.313 [20], clause 7.2.3 to E2 node via E2 interface or O1 interface.   
• RACH optimization – PRACH parameters available over XN/X2 interface, contention detection per RACH attempt, number of RACH preambles per SSB, information on SSB threshold per RACH attempt defined in 3GPP via E2 interface from E2 node.   
• HO target and control parameters available as specified in 3GPP TS 28.313 [20] to E2 node via E2 interface or O1 interface.

# 4.20 Shared O-RU

# 4.20.1 Background and goal of the use case

# 4.20.1.1 Common aspects & background for all Shared O-RU use cases

This use case provides the background, motivation, and requirements for the lower layer split multi node support, allowing to share an O-RU between multiple O-DU nodes, including single operator and multi-operator use cases.

Shared O-RU use cases deliver a range of different benefits depending on specific scenarios. Shared O-RU support for Single-MNO use cases delivers important resiliency and load balancing capabilities. Shared O-RU support for multipleMNO use cases delivers important network sharing capabilities to complement established MOCN, MORAN and DAS approaches.

Shared O-RU use cases cover the class 2 BBU pooling specified in clause 4.18.

Shared O-RU use cases are associated with RAN sharing use case. In particular, RAN sharing depicts a Shared O-RU configuration, specified in clause 4.7.

Shared O-RU feature also serves to support the Multi-Vendor (MV) network slicing use case, its operation, and scenarios, specified in clause 4.10. Multi-vendor network slicing has implications to the front-haul as well. The multi-vendor slicing use case will use dynamic resource allocation aspects of the Shared O-RU feature.

The following sub-clauses describe different configurations and deployment scenarios for Shared O-RU. They also describe use cases to accomplish key functionality such as a resiliency use case.

The Shared O-RU will have common solutions that span the sub-use cases. The clauses that follow describe different aspects, configurations, and deployment scenarios for Shared O-RU; however, they will likely share common solutions which are described in the solution clause.

Expected use cases that accomplish a purpose between actors comprise the sub-use cases: such as software upgrade of a Shared O-RU, start up of a Shared O-RU, recovery from failed primary O-DUs that are sharing a O-RU, rehoming of a Shared O-RU in a network.

# State management:

The Shared O-RU supports lock/unlock operations (administrative state) of a Shared O-RU administrative state management and these are used throughout the sub-use cases. State management of administrative, operation and availability state are specified in ITU-T X.731 [18] and in 3GPP TS 28.624 [9], in 3GPP TS 28.625 [10] (for all classes in the NRM), and in 3GPP TS 28.626 [11]. Some of the sub-use cases can use them, some cannot. Role-based admission control. The host can change administrative state of the O-RU while the tenant cannot. The Shared O-RU sub-use cases shall be as specified in RFC 8348 [19] which is similar to what is specified in ITU-T X.731 [18].

# 4.20.1.2 Resource portioning use case of Shared O-RU for Single-MNO

This sub-use case describes the procedures of how to decide on the partitioning of a Shared O-RU. The actors are the sharing co-ordinator, SMO, and the resource partitioning rApp (Shared O-RU). The sharing co-ordinator recovers the inventory from the SMO and decides on how to partition the resources of a Shared O-RU. The sharing co-ordinator uses the rApp to partition the resources of a Shared O-RU between multiple O-DUs. The outcome is that rApp has details on how a Shared O-RU’s resource are to be partitioned.

# 4.20.1.3 Start-up use case of a Shared O-RU for Single-MNO

This sub-use case describes the start-up of a Shared O-RU. The actors are the SMO, the O-DUs, the Shared O-RU, and their interactions that are needed for a Shared O-RU to boot up and enter into operation. The outcome is that the Shared O-RU is operating with the necessary software version and has established network connectivity with the O-DUs and, for hybrid deployments, the SMO. The start-up for a Shared O-RU is the basis of the other Shared O-RU sub-use cases.

# 4.20.1.4 Configuration use case of a Shared O-RU for Single & Multi-MNO

This sub-use case describes the configuration of a Shared O-RU. The configuration is invoked after the start-up use case has completed. Configuration can occur with different actors in hybrid vs hierarchical management mode. The common aspects of the Shared O-RU configuration are configured by the O-DU when in hierarchical management mode and by the SMO in hybrid management mode. The common aspects include the security, operational, transmission, and connectivity related parameters. The O-DUs are always responsible for configuring the partitioned carrier information on the Shared O-RU through the open front-haul interface. The use case enables the SMO to be notified of the configured carrier parameters.

This sub-use case includes the configuration of multi-operator role-based access control (configuration) for the management sessions associated with a tenant operator. The Shared O-RU uses the PLMN-Id associated with the management account and used in other aspects of the Shared O-RU’s configuration to prevent a tenant from reading configuration associated with a second tenant’s partitioned resources or subscribing to performance measurements associated with a second tenant’s partitioned resources.

This sub-use case also describes the procedures of how a sharing co-ordinator can confirm that a tenant operator is complying with the sharing agreements that cover operation of a Shared O-RU.

The outcome is that the Shared O-RU has been configured with the configuration parameters necessary for operation.

# 4.20.1.5 Supervision use case of a Shared O-RU for Single-MNO

This sub-use case applies to the running/operation of Shared O-RU.

This sub-use case describes the supervision operations of the Shared O-RU. This sub-use case is triggered after the ODUs have configured the partitioned carrier information of a Shared O-RU. It is invoked during run-time. The actors are the SMO, O-DUs, and Shared O-RU. The objective that the use case accomplishes is the establishment of watchdog supervision of the Shared O-RU by multiple O-DUs. Supervision enables the Shared O-RU to autonomously cease transmitting on a partitioned carrier if it loses supervision with the O-DU responsible for that carrier.

# 4.20.1.6 Performance management use case of a Shared O-RU for Single-MNO

This sub-use case applies to the running/operation of Shared O-RU.

This sub-use case describes the performance management operations of the Shared O-RU. This sub-use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. It is also invoked during run-time. The actors are the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for each O-DU to establish subscriptions to receive performance management notifications regarding operation of the fronthaul between the O-DUs and Shared O-RU.

The sub-use case also describes how performance management logs, data and files are passed from the Shared O-RU to the connected O-DUs and data from O-DUs to SMO. Performance measurement data should be supported in three basic ways by the O-DU:

Active push by a producer (O-DU) – A producer (O-DU) could push performance data to a consumer (SMO).

o Streaming – A persistent connection between consumer & producer exists without having to renegotiate between the data reports to send a steady flow of data. This is like 3GPP performance streaming reporting (as specified in 3GPP TS 28.532 [21], clause 11.5). Once the WebSocket is opened, the meta-data about the streams is exchanged, and the consumer can then receive the serialized data.

o Event notifications – Performance measurement information sent by event notifications will reestablish a new connection between a consumer and producer for each data reporting. This is how 5GC SBA works (as specified in 3GPP TS 23.501 [2] and in 3GPP TS 23.502 [22] services). The data is sent as a payload of a notification.

Active collection by a consumer – The consumer (SMO) could also actively collect data from a producer (O-DU).

o Configuration management read only attributes – Reuse of configuration management approach where attribute conveying the value of performance data is read by the consumer like any other configuration management attribute.

o Data scraping – Use of data scraping common to cloud native implementations where a collector reads the data from a pre-defined URI.

File-based reporting – File based reporting is used for low-priority or background collection for large amounts of performance data.

o File upload by producer – In this method, there is no artificial delay, the data is reported whenever it is available. However, it involves action by the producer.   
o File download by consumer – It removes the burden from the producer, but relies upon either periodic polling, or file ready notification from the producer about the data being ready for download. This is how 3GPP file-based reporting works as specified in 3GPP TS 28.532 [21], clause 11.6 and in ETSI GS NFV IFA008 [24] and ETSI GS NFV IFA013 [23] specifications.

For the Shared O-RU:

- Active push by Shared O-RU (producer) – The Shared O-RU pushes performance data to the O-DU.

o Event notifications – The Shared O-RU sends performance measurement information through event notifications to the O-DU by establishing a new connection for each data reporting session.

- Active collection by O-DU (consumer) – The O-DU can actively collect data from the Shared O-RU.

o Attributes - The performance data is read by the O-DU. The O-DU can invoke a Remote Procedure Call (RPC) towards O-RU giving the O-RU all information it needs to send PM file. Then, the O-RU acts as sftp client and performs file upload to pointed to location.

NOTE 1: The Shared O-RU does not support streaming-based reporting.

NOTE 2: The Shared O-RU cannot act as a sftp server but can act as a sftp client. Thus, the Shared O-RU can upload files to a designated location.

# 4.20.1.7 Antenna Line Device (ALD) control use case of a Shared O-RU for Single-MNO

This sub-use case applies to the running/operation of Shared O-RU.

This sub-use case describes the operation of antenna line devices with the Shared O-RU. This sub-use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. The actors are one of the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for the selected O-DU to operate the ALD controller and control the ALD connected to the Shared O-RU.

ALD control is an end-to-end operation from the operator using the SMO at one end issuing operations to the O-DU and realising that ALD operation through the O-RU on through to the terminating ALD device at the other end.

Because there is a single ALD controller, and the Shared O-RU can be connected to multiple O-DUs, one of them needs to be nominated as the ALD controller.

There are many types of operations for ALD control. These include but not limited to software update of ALD devices, setting of RET mechanical/electrical tilt setting, reset of ALD devices, etc.

# 4.20.1.8 Basic resiliency use case (active O-DU failure) for Single-MNO

This sub-use case describes system recovery from a failure (operational state $=$ disabled) of the active O-DU#1 or O-DU switchover may be triggered by SMO in reactions to failure or due to operator’s activity for a Shared O-RU in SingleMNO deployment. A switch of the active O-DU to standby O-DU is done. This sub-use case only applies to the hierarchical management of the O-RU.

The actors are the SMO, O-CU, O-DUs, and Shared O-RU. The actors work together to recover operation from O-DU(s) failures.

This basic resiliency sub-use case, covers failure of the active O-DU#1 that is unable to provide service. For example, when SMO detects that O-DU is out of service, the SMO assumes operational state for such O-DU as “disabled” and triggers recovery action for cells served by such O-DU. This use case covers a flow of operations that occurs in this situation.

This use case is triggered when the active O-DU fails (operational state $=$ disabled).

This use case describes the switch-over of the other O-DU to become the new active O-DU.

# 4.20.1.9 Antenna calibration sub-use case of a Shared O-RU for Single-MNO

This sub-use case applies to the running/operation of Shared O-RU.

This sub-use case describes the operation of antenna calibration using a Shared O-RU. This sub use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. The actors are the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for the Shared O-RU to be able to perform antenna calibration when connected to multiple O-DUs.

It is typically initiated from the Shared O-RU when it detects that antenna calibration is necessary, which then sends a notification to the O-DU.

If supported by the O-RU, the O-DU may also set an automatic antenna calibration setting which enables the Shared ORU to automatically perform antenna calibration.

# 4.20.1.10 Rehoming use case of a Shared O-RU for Single-MNO

This sub-use case describes how a Shared O-RU is rehomed within a network and paired with new parent O-DUs. Rehoming is the process of associating new management (parent) O-DUs with a Shared O-RU. This might be a virtual rehoming in a cloud native deployment, management-requested parent rehoming, or a physical move of the Shared O-RU whereby the Shared O-RU is connected and communicating to new parent O-DUs.

Rehoming is typically done deliberately. Resiliency flows has some similarity to the rehoming flow; however, the difference is that resiliency is a reaction to a fault in the system, whereas rehoming is typically a planned activity.

Some typical reasons why rehoming is done is as follows:

Replanning or changing a network – Altering a network resulting from physical construction work or network optimization may cause an MNO to replan their network necessitating a Shared O-RU to rehome.   
New greenfield network – When a new greenfield pocket deployment is created within a brownfield deployment rehoming might happen.   
Service management-level operations – The MNO may trigger a rehoming operation for the Shared O-RU which can happen for a variety of purposes.   
Physical move a Shared O-RU – The Shared O-RU is physically moved from one location to another. Evolving a network – The site might be changed from a non-Shared O-RU configuration to a Shared O-RU configuration which will require rehoming as at least there is a new second O-DU now connected to the O-RU. Partnership with a new MNO – Changing from a Single-MNO type configuration to a Multi-MNO configuration may require the Shared O-RU to be rehomed.   
Maintenance activities – When troubleshooting a failure, or other various maintenance activities may cause a Shared O-RU to be rehomed.   
Parent failure – The failure of a parent O-DU(s) may result in rehoming of a Shared O-RU being necessary.

To illustrate an example of rehoming, suppose there is a Shared O-RU with identity $\# 7 0 0$ that currently exists in an edge cloud with CloudID $\# 2 0$ with parents, O-DU #1 and O-DU #2. And it is physically moved to a different edge cloud CloudID $\# 9 0 0$ and then subsequently reconnected to new different parent O-DUs, O-DU $\# 1 9$ and O-DU $\# 2 4$ . Rehoming is a software-based operation, however, to physically move a Shared O-RU would also require the associated physical front-haul connections to be made.

O-CUs and O-DUs can also be rehomed to new management entities (SMO). However, this sub-use case will only focus on when a Shared O-RU is rehomed to new O-DU parents. There are two basic forms of rehoming, one that is a physical move of the Shared O-RU and other is a deliberate management level operation:

Physical rehoming – In this kind of rehoming, the Shared O-RU is physically moved from one location to another. There are two cases where after the physical move, the Shared O-RU has either new O-DU parents or stays with the original ODU parents. For a Shared O-RU this means that the front-haul connections will be separated and reconnected. This may also entail LCM operations, where a Shared O-RU is decommissioned and then subsequently recommissioned and reinstalling with new parent O-DU. These would fall into common LCM operations. Physical rehoming can also happen during maintenance operations, where a Shared O-RU might be disconnected and reconnected to new parent O-DUs for a variety of reasons.

Management initiated rehoming – Management initiated and coordinated rehoming of a Shared O-RU is when the Shared O-RU is given new O-DU parents done at the SMO. This may happen for a variety of reasons and is expected to be an intentionally planned activity. The management entity of the Shared O-RU may be the O-DU in the hierarchical case or SMO in a hybrid configuration. The new parent O-DU may have different carrier support, capabilities, and capacities of than the former parent; for example, it might be more energy efficient with less capabilities or it might an expanded more powerful O-DU.

# 4.20.1.11 Reset use case of a Shared O-RU for Single-MNO

The reset of a Shared O-RU sub-use case describes the operations related to taking a Shared O-RU out of service and resetting it.

There are some important aspects to reset of Shared O-RU. Only the Shared O-RU host would have permissions to perform the reset operation.

In a multiple MNO configuration, reset operations would need to be coordinated between operators. The Shared O-RU host operator has the permission to perform the reset of a Shared O-RU. It would expect that the Shared O-RU host operator would try to coordinate with the Shared Resource Operator (SRO). This can entail something as simple as those two operators talking to each other; it can also entail automated coordination between management entities of these operators. The reset of a Shared O-RU would impact Availability, Reliability, and Maintenance (ARM) metrics, and uptime KPIs.

The reset of a Shared O-RU operation is the basis for maintenance activities, debugging operations, the physically moving, physical rehoming, and recovery from malfunctions of the Shared O-RU.

There are situations where the Shared O-RU would autonomously reset itself. When the Shared O-RU has lost M-plane connectivity to all of its connected O-DUs the Shared O-RU would autonomously reset itself. This would be the same as if the O-RU was not in a shared configuration.

A software update will result in a reset of the Shared O-RU. The software update of a Shared O-RU is expected to be coordinated between the Shared O-RU host and the SRO.

Before removing the Shared O-RU from service, the Shared O-RU carriers and its associated cells on O-DU/O-CU shall be deactivated.

# 4.20.1.12 Advanced resiliency sub-use cases of a Shared O-RU for Single-MNO

Advanced resiliency sub-use cases provide descriptions for the resiliency operations where any of O-DUs or Shared ORU have either partially failed (for instance, when the availability status is “degraded” for any of them), completely failed (when the operational state is ”disabled”), or when there are failures detected in the interfaces (like the FH-C/U/S/M plane, F1, E2, and O1).

The key actors in this scenario are the SMO, O-CU, O-DUs, and Shared O-RU. These entities may collaborate to recover or maintain operations in the event of partial O-DU(s) failures, software issues, interface disruptions, power outages, connectivity failures, and loss of synchronization.

This use case shall be triggered when at least one of the aforementioned failures occurs in the network.

# 4.20.1.13 Load-balancing sub-use case of a Shared O-RU

Load-balancing is a use case where relevant actors can reallocate Shared O-RU resources based on triggers, metrics, or policies.

A key actor is a policy-enforcer that makes Shared O-RU resource allocation decisions based on inputs from measurements. For example, measurements can indicate the amount of traffic on each of the two O-DUs connected to the Shared O-RU. The policy-enforcer decides when a reallocation of Shared O-RU resources is needed. For example, if the policy-enforcer observes that one O-DU has a disproportionate amount of traffic (e.g., more users per MHz) than the other O-DU, the policy-enforcer makes a decision to re-allocate a component carrier from one O-DU to the other O-DUs.

The policy-enforcer role could be played by the SMO/Non-RT RIC or the Near-RT RIC, depending on the time granularity of load balancing decision-making needed. There are limitations that are governed from the air interface which will influence the mechanisms and time granularity for load balancing. Policies can reflect a variety of triggers or mechanisms to be used to balance traffic or carriers. These might include guaranteed bandwidth, O-DU computational load/capacity (processor occupancy), and time of day triggers among others. Whatever the policy rules are and how often they are evaluated, the policy-enforcer would evaluate the situation, probably periodically, and make a resource re-allocation decision.

# 4.20.1.14 Coordinated reset of a Shared O-RU sub-use case for Multi-MNO

The coordinated reset of a Shared O-RU sub-use case describes the operations related to resetting a Shared O-RU when there are multiple Shared Resource Operator (SRO) O-DUs connected to the Shared O-RU.

In a multiple MNO configuration, reset operations would need to be coordinated between operators. The active Shared O-RU Host (SOH) operator coordinates the reset of a Shared O-RU. The definition of the active SOH is a SOH that has a state $=$ active. The active SOH can perform a reset on its own volition. The active Shared O-RU Host (SOH) coordinates the reset operation; thus, the SROs can request a reset of the Shared O-RU to be performed by the active SOH. So, the active SOH approves or rejects a reset request of the Shared O-RU coming from other SROs. If the request is accepted by the active SOH, the x would inform all the other SROs x. Then the SOH would perform the reset of the Shared O-RU. If the SOH rejects the operation, then the SOH that originated the SRO that the command was rejected. The SOH can reject a command for example in the middle of a software update or other possible conditions that might prohibit a reset. The reset of a Shared O-RU would impact availability, reliability, and maintenance (ARM) metrics, and uptime KPIs.

The reset of a Shared O-RU operation is the basis for maintenance activities, debugging operations, the physically moving, physical rehoming, and recovery from malfunctions of the Shared O-RU.

Before removing the Shared O-RU from service, the Shared O-RU carriers and its associated cells on O-DU/O-CU shall be deactivated.

The reset of a Shared O-RU is a “hard reset”.

There can be other variations of coordinated reset of a Shared O-RU possibly based on a policy.

# 4.20.1.15 Management of Shared O-RU during O-DU software update sub-use case for Shared O-RU for Single & Multi-MNO

As part of WG6 Cloudification and Orchestration Use Cases and Requirements for O-RAN, a generic case of software upgrade of network function is described. In the practical implementation context, a variety of strategies are incorporated for updating the network function with a new software version, with the objective of minimizing the impact of modifications and mitigating any disruptions to the overall service delivered to end users. These strategies include wellestablished practices such as Canary update, Rolling update, Blue/Green update etc. The choice of a specific approach relies on various factors such as the extent of the changes, the associated risk potential, and the cost of incorporating the change. Moreover, such changes necessitate careful consideration of dependencies and the need to re-provision and optimize resources accordingly. Furthermore, it is crucial to incorporate contingency/mitigation plans in the event that the software update does not align with the intended plan for implementing the changes.

This sub-use case focuses on the management of Shared O-RU during the software update of O-DU. It is a critical consideration for Shared O-RU, particularly when O-RU resources are shared between the updated O-DU and existing O-DUs. To address this, well-defined procedures are necessary to identify the specific O-RU that can be shared, determine the particular O-DU with which the O-RU resources can be shared, and optimize the shared resources effectively. Prior to the software update, it can be essential to identify the candidate O-DU and associated O-RU resources that requires evacuation, thereby necessitating the provisioning of target RAN nodes. Moreover, in the event of performance degradation or negative impact on performance indicators following the completion of O-DU software update and activation, it is essential to establish efficient risk mitigation strategies and evaluate possibility of rolling back the introduced changes.

Here the consideration of the Shared O-RU arises from the need to minimize the impact of the software update of O-DU. This is achieved by validating the update with minimal traffic or allocating minimal resources, thereby effectively reducing the footprint of affected end users. Utilizing a Shared O-RU effectively fulfils this objective which otherwise can require deployment of dedicated O-RUs solely for validating the O-DU software update. An additional aspect to be considered is the prevention of Shared O-RU restart following a software update at the O-DU level. This is particularly relevant as a software update on the O-DU can entail the establishment of m-lane connections and initiation of the call home procedure, both of which typically require an O-RU restart to be initiated.

A high-level view of the software update scenario of O-DU wherein the software (SW) updated O-DU shares the O-RU resources with an existing O-DU is shown in figure 4.20.1.15-1.

![](images/ef2ddc7885054b4164424843d0ec5fb3227bf821b99710d90234b9a3ea378d77.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.1.15-1: Shared O-RU management scenario during O-DU software update

Shared O-RU management scenario during O-DU software update follows a high-level approach as given below:

1. Selection of O-DU node for software update based on inventory, FM/PM data

2. Deployment and call-home procedures of O-DU

3. O-DU registration with O-CU, Near-RT RIC

4. Common aspect provisioning on Shared O-RU (e.g., ODU-ID, User account) based on SW updated O-DU

5. Selection of the policy for load sharing (e.g., load balancing policy, or selection based on cells having low priority user sessions, S-NSSAI, anticipated traffic, etc.) with the SW updated O-DU

6. O-RU initiates m-plane connection establishment with SW updated O-DU

7. Translation of the load sharing policy to O-RU configuration

8. Inactivation and evacuation of component carriers selected for allocation to SW updated O-DU

9. Provisioning of O-RU with carrier configuration details by SW updated O-DU (e.g., end points, list entries)

10. Activation of carrier configuration associated with SW updated O-DU

11. Initiate KPI and functional log monitoring of SW updated O-DU and associated O-RU resources

12. O-DU SW update mitigation $:$ In case of degraded KPIs reverse SW update process of O-DU

It is to be noted that this sub-use case does not differentiate based on the extent of change introduced to the O-DU through the software upgrade because it primarily depends on the implementation context.

This use case does not enforce a specific policy for the SW update as this depends on the particular deployment and implementation choice. Such policies are typically incorporated to define the rules, control logic, constraints, and thresholds to be considered during the particular change being initiated. As an example, if an implementation scenario calls for such flexibility, the component carrier shifting could be omitted by utilizing appropriate SW update policy and limit only to the general health check after O-DU SW update.

This use case introduces couple of new actors such as O-DU SW change management rApp. An O-DU SW update lifecycle can be managed using these optional functions or using appropriate implementation specific extensions of SMO function.

Currently this use case considers only single operator Shared O-RU scenario. The impact of SW update on multi-operator Shared O-RU scenarios is not in scope of the current version of this sub-use case.

# 4.20.1.16 Resource partitioning sub-use case for Multi-MNO configuration

This sub-use case describes the procedures of how to decide on the partitioning of a Shared O-RU in a Multi-MNO configuration where one O-DU belongs to an owner operator (MNO) and at least one other O-DU belongs to a participating operator (MNO). The actors are the owner operator MNO sharing co-ordinator, the participating operator MNO sharing co-ordinator, the owner operator SMO, the participating operator MNO SMO, the owner operator resource partitioning rApp, and participating operator MNO resource partitioning rApp. The owner operator MNO sharing coordinator retrieves the inventory from the owner operator SMO and decides on how to partition the resources of a Shared O-RU. The owner operator MNO sharing co-ordinator uses the owner operator resource partitioning rApp to partition the resources of a Shared O-RU between multiple O-DUs. The outcome is that the owner operator resource partitioning rApp has details on how a Shared O-RU’s resource are to be partitioned.

# 4.20.1.17 Start-up sub-use case of for Multi-MNO configuration

This sub-use case describes the start-up of a Shared O-RU in a Multi-MNO configuration where one O-DU belongs to an owner operator (MNO) and at least one other belongs to a participating operator (MNO). The actors are the owner operator SMO, participating operator SMO, the connected O-DUs, the Shared O-RU, and their interactions that are needed for a Shared O-RU to boot up and enter into operation. The outcome is that the Shared O-RU is operating with the necessary software version and has established network connectivity with the O-DUs and, for hybrid deployments, the corresponding SMOs. The start-up for a Shared O-RU is a basis for some of the other Shared O-RU sub-use cases.

# 4.20.1.18 Supervision sub-use case for Multi-MNO configuration

This sub-use case applies to the running or operation of Shared O-RU in a Multi-MNO configuration where one O-DU belongs to an owner operator (MNO) and at least one O-DU belongs to a participating operator (MNO).

This sub-use case describes the supervision operations of the Shared O-RU. It is triggered after the connected O-DUs have configured the partitioned carrier information of a Shared O-RU. It is invoked during run-time. The actors are the owner operator SMO, participating operator SMO, the connected O-DUs, and Shared O-RU. The objective that the use case accomplishes is the establishment of watchdog supervision of the Shared O-RU by multiple O-DUs. Supervision enables the Shared O-RU to autonomously cease transmitting on a partitioned carrier if it loses supervision with the ODU responsible for that carrier.

# 4.20.1.19 Antenna Line Device (ALD) control sub-use case for Multi-MNO configuration

This sub-use case applies to the running or operation of Shared O-RU in a Multi-MNO configuration where one O-DU belongs to an owner operator (MNO) and at least one other belongs to a participating operator (MNO).

This sub-use case describes the operation of Antenna Line Devices (ALD) with the Shared O-RU. This sub-use case is triggered after the connected O-DUs have configured the partitioned carrier information of a Shared O-RU. The actors are one of the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for the selected O-DU to operate as the ALD controller and control the ALD connected to the Shared O-RU.

ALD control is an end-to-end operation from a technician using the owning operator or participating operator SMO at one end issuing operations to the O-DU and realising that ALD operation through the O-RU on through to the terminating ALD device at the other end.

Because there is a single ALD controller, and the Shared O-RU can be connected to multiple O-DUs, one of them needs to be nominated as the ALD controller. It is expected that an O-DU of the owning operator would be the ALD controller (but not necessarily).

There are many types of operations for ALD control. These include but not limited to software update of ALD devices, setting of RET mechanical/electrical tilt setting, TMA updates, reset of ALD devices, etc.

NOTE: Only the host O-DU (of the owner operator) can control the ALD and the participating operator O-DU would not be able to control the ALD devices.

# 4.20.1.20 Antenna calibration sub-use case for Multi-MNO configuration

This sub-use case applies to the running or operation of Shared O-RU in a Multi-MNO configuration where one O-DU belongs to an owner operator (MNO) and at least O-DU other belongs to a participating operator (MNO).

This sub-use case describes the operation of antenna calibration using a Shared O-RU. This sub-use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. The actors are the connected O-DUs, and Shared O-RU. The objective that the use case accomplishes is for the Shared O-RU to be able to perform antenna calibration when connected to multiple O-DUs.

# 4.20.1.21 Rehoming use case of a Shared O-RU for Multi-MNO

This is rehoming the Shared O-RU in a Multi-MNO configuration where different O-DU (parents of the Shared O-RU) are now under the management of different MNOs. Some considerations among others in the Multi-MNO configuration are that there might be different configuration, security concerns, role based access privileges, physical security, coordination between the two MNOs technicians when performing maintenance activities that require rehoming the Shared O-RU.

For the Multi-MNO configuration, the three basic forms of rehoming, physical rehoming where the Shared O-RU is physically moved (with original O-DU parents or new O-DU parents), and management initiated rehoming caused from management level planned activities still apply to the Multi-MNO case.

# 4.20.1.22 Performance management use case of a Shared O-RU for Multi-MNO

This sub-use case applies to the running/operation of Shared O-RU.

This sub-use case describes the performance management operations of the Shared O-RU in a Multi-MNO configuration. Here the Shared O-RU is connected to O-DUs that are owned by different MNOs. This sub-use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. It is also invoked during run-time. The actors are the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for each O-DU to establish subscriptions to receive performance management notifications regarding operation of the fronthaul between the O-DUs and Shared O-RU.

The sub-use case also describes how performance management logs, data and files are passed from the Shared O-RU to the connected O-DUs and data from O-DUs to SMO. Performance measurement data and telemetry information should be supported in three basic ways.

The same mechanisms described in performance measurement reporting for Single-MNO are also supported in a MultiMNO configuration. The O-DU supported active push through streaming and event notification methods. The O-DU supports active collection by a consumer through attribute based and data scraping. The O-DU supports file-based reporting. The Shared O-RU supports active push through event notifications and active collection from O-DU via RPC and sftp. See clause 4.20.1.6 for further details. The main difference between the Single-MNO configuration and the Multi-MNO configuration is that there are additional considerations for sending performance information to two different mobile network operators. This entails aspects of security and support for different subscription filters. As such, two MNOs may want different collected data, may have different security controls based on role-access, different subscription filters and session operation. For example, one MNO might employ NetConf and another MNO Virtual Event Streaming (VES) messaging.

# 4.20.1.23 Antenna calibration sub-use case of a Shared O-RU for Multi-MNO

This sub-use case applies to the running/operation of Shared O-RU. This sub-use case describes the operation of antenna calibration using a Shared O-RU in a Multi-MNO configuration. This sub-use case is triggered after the O-DUs have configured the partitioned carrier information of a Shared O-RU. The actors are the O-DUs, and Shared O-RU. The objective that the use case accomplishes is for the Shared O-RU to be able to perform antenna calibration when connected to multiple O-DUs in a Multi-MNO configuration.

This sub-use case is essentially the same as for the Single-MNO configuration except the O-DUs which are connected to different operators may coordinate.

# 4.20.1.24 Dynamic resource shifting

Dynamic resource shifting is a Shared O-RU sub-use case related to how resources are moved to achieve improvements in performance. In this case, the resources that are shifted are fractions of radio spectrum utilized by cells. These resources correspond to PRBs and can be dynamically addressed by bandwidth parts. See 3GPP TS 38.211 [13], clause 4.4.5.

This sub-use case describes how radio spectrum resources can be shifted between cells that use overlapping spectrum and are served by Shared O-RU. This is performed automatically and dynamically (autonomously) without the need to perform time-consuming cell reconfiguration process.

The process of dynamic resource shifting is controlled by Near-RT RIC based on traffic-related KPIs or operator-defined parameters. Exact triggers for RIC to request for dynamic resource shifting are out of scope of this specification.

Important drivers for this use case are as follows:

The use case shall deliver truly dynamic frequency resource shifting between cells.   
The use case shall preserve power consumption usage at the UE level.

The use case shall utilize existing radio link control procedures.

# 4.20.1.25 Static resource shifting use case for Single-MNO

The Shared O-RU resource shifting use case describes how cell(s)/carrier(s) and their resources are optimally reallocated between O-DUs to achieve performance improvements, and resource optimization.

Static resource shifting is initiated by the SMO based on pre-configured triggers or policies, where it describes about how cell(s)/carrier(s) are moved between O-DUs. Two or more O-DUs connected to an O-RU utilize their respective carrier frequency resources exclusively during designated time periods, with potential optimization based on various resource reallocation requirements. O-RU configured with respective carrier frequency resources associated with two O-DUs, enabling the transfer of throughput between cells/carriers. This process involves the reconfiguration of cell and carrier resources between O-DUs to optimize performance.

Important drivers for this use case are as follows:

The use case should provide mechanism for cell resource shifting between O-DUs.   
The use case shall utilize the existing cell/carrier configuration scenarios.

# 4.20.2 Entity/resources involved in the use case

# 4.20.2.1 General aspects of entity/resources for Shared O-RU

The following sub-clauses describe the entity/resources that are important and key players for each of the sub-use cases for Shared O-RU. Many of the sub-use cases will have a similar set of actors/entities/resources involved in realise the operation related to that sub-use case.

In general, the identification of entity/resources serve as the basis for understanding a service model. The actors are trying to accomplish a particular goal, and the actions between the actors are the services that are the basis of a service model. The service model is a basis for an information model.

Sometimes, the actors in the sub-use cases perform differing operations, and sometimes there is a variable number of entities depending on the function.

# 4.20.2.2 Resource partitioning use case of Shared O-RU for Single-MNO

1) Sharing co-ordinator:

a) Recovers the inventory of Shared O-RUs and O-DUs and determines how to partition the resources of a Shared O-RU between multiple different O-DUs.

2) SMO:

a) Provides inventory of Shared O-RUs and O-DUs.   
b) Configures call home identities in external transport systems.

3) Shared O-RU orchestration rApp:

a) Supports partitioning of individual carriers of a Shared O-RU between multiple different O-DUs operated by different operators.

# 4.20.2.3 Start-up use case of a Shared O-RU for Single-MNO

1) Shared O-RU:

a) Performs call home and triggers establishment of network management session.

2) SMO:

a) Recovers the software inventory of Shared O-RU and decides whether to upgrade operational software of Shared O-RU (hybrid management model).

3) O-DU: a) Recovers the software inventory of Shared O-RU and decides whether to upgrade operational software of Shared O-RU (hierarchical management model).

# 4.20.2.4 Configuration use case of a Shared O-RU for Single & Multi-MNO

1) SMO:

a) Responsible for Shared O-RU common configuration (hybrid management model). b) Responsible for receiving notifications of modifications to Shared O-RU’s configuration (Multi-MNO deployment model).

2) O-DU:

a) Responsible for Shared O-RU common configuration (hierarchical management model).   
b) Responsible for Shared O-RU carrier configuration.

3) Shared O-RU orchestration rApp:

a) Responsible for determining which O-DU performs Shared O-RU common configuration (hierarchical management model).   
b) Responsible for receiving notifications of modifications to Shared O-RU’s configuration (Multi-MNO deployment model).

4) Shared O-RU:

a) Responsible for notifying any subscriber of its modified configuration.

5) Sharing coordinator:

a) Confirms that the Shared O-RU’s configuration complies with a sharing agreement (Multi-MNO deployment model).

# 4.20.2.5 Supervision use case of a Shared O-RU for Single-MNO

1) Shared O-RU:

a) Responsible for operating supervision on a per O-DU basis.   
b) Responsible for de-activating carriers associated with O-DU if there is supervision failure by O-DU.   
c) Responsible for signalling alarm to subscribers if O-DU supervision is lost.

2) O-DU:

a) Responsible for repeatedly resetting the Shared O-RU’s supervision timer.

3) SMO:

a) Responsible for subscribing to alarm notifications (hybrid management model).   
b) Responsible for forwarding alarm notifications to Shared O-RU orchestration rApp.

# 4.20.2.6 Performance management use case of a Shared O-RU

1) Shared O-RU: a) Responsible for generating performance management notifications on a per partitioned carrier basis.   
2) O-DU: a) Responsible for subscribing to receive performance management notifications from Shared O-RU.   
3) SMO: a) The operator, or SMO, or another entity is an endpoint for the performance measurement data or reports.

# 4.20.2.7 Antenna Line Device (ALD) control use case of a Shared O-RU for Single-MNO

The following actors are involved in the ALD control use case.

1) Antenna line device control rApp (for the Shared O-RU): a) Responsible for determining which O-DU is responsible for ALD controller aspects.   
2) O-DU: a) Responsible for implementing ALD controller.   
3) Shared O-RU (hardware): a) Responsible for bridging between OFH and HDLC.   
4) ALD (one or more ALD devices): a) Responsible for terminating HDLC.

# 4.20.2.8 Basic resiliency use case (active O-DU failure) for Single-MNO

The description below outlines the actors involved:

1) Shared O-RU:

a) The Shared O-RU helps in detection of the O-DU connectivity/availability seen from O-RU perspective during a resiliency recovery operation. For example, when the active O-DU fails, the Shared O-RU informs other available and subscribed NetConf clients about the connection failure towards previously active O-DU.

2) O-DUs (host/tenant/ & other O-DUs):

a) All the O-DUs connected to the Shared O-RU are actors that are relevant in some way during a resiliency operation. The active O-DU is main O-DU that performs the basic LCM and FCAPS functionality and terminates HDLC stack for ALDs operations connected to O-RU. In the various resiliency situations, where the active O-DU fails, then the other O-DU(s) connected to the Shared O-RU get involved in restoring the services for end users.

3) O-CU: a) O-CU receives cell related configurations from SMO and available cell details from O-DU(s). Based on the available resources reported by O-DU and desired availability of cells received from SMO, the O-CU activates or deactivates the cells in the O-DU using F1 interface.

4) SMO:

a) Based on operator’s decision, the SMO assigns initial O-DU roles (active, standby).   
b) The SMO makes high-level decisions related to failures and the various resiliency situations. For example, in a case where a O-DU is taken out of service, it might be intentionally removed, or physically removed permanently, which has impact to the Shared O-RU operation.

# 4.20.2.9 Antenna calibration use case of a Shared O-RU for Single-MNO

The following are the principal actors in the antenna calibration use case for a Shared O-RU.

1) Antenna calibration rApp (Shared O-RU): a) This App is responsible for determining which O-DU is responsible for the antenna calibration operation.   
2) O-DU: a) Responsible for supporting Shared O-RU antenna calibration operation.   
3) Shared O-RU (HW): a) Responsible for implementing antenna calibration.

# 4.20.2.10 Rehoming use case of a Shared O-RU for Single-MNO

The following are the principal actors in the rehoming use case:

1) Shared O-RU: a) The Shared O-RU is the entity that is being rehomed.   
2) Original O-DUs: a) The original O-DU(s) are the O-DUs that the Shared O-RU were originally attached to.   
3) New O-DUs attached to: a) These are the new O-DU(s) that the Shared O-RU will now be attached to.   
4) SMO: a) It is also possible to rehome to a O-RU to a new management system (SMO). As such, the O-RU can be rehomed to a different SMO. For a hybrid configuration this would mean the O-RU is connected to a different SMO.

# 4.20.2.11 Reset use case of a Shared O-RU for Single-MNO

The following are the principal actors in the [shut down/reset] of a Shared O-RU use case.

1) Shared O-RU: a) The Shared O-RU is the entity that is being affected by the operation ([shutdown/reset]).   
2) The [primary/host] O-DU: a) The [primary/host] O-DU for the Shared O-RU is the managing entity that will execute the command.   
3) SMO: a) The operator using the SMO can issue the shut-down/reset command, and starts the use case for the operatio

# 4.20.2.12 Advanced resiliency sub-use cases of a Shared O-RU for Single-MNO

The following description details the actors involved in the advanced resiliency sub-use cases of a Shared O-RU:

1) Shared O-RU: The Shared O-RU acts as actor in M-plane session supervision towards O-DU. As such O-RU detects M-plane link breaks and reports them in form of alarms towards other NetConf clients who still have active M-plane links with O-RU. NOTE: If there is no client with active M-plane session available - the O-RU performs autonomous reset.

2) O-DUs (active/stand-by):

a) All the O-DUs connected to the Shared O-RU are actors during a resiliency operation. The active O-DU performs the LCM, FCAPS functionality, and ALD operations with the O-RU. In various resiliency scenarios, when the active O-DU fails, the SMO may decide to trigger the O-DU role change (active/standby) to restore service availability for end users.

3) SMO:

a) Based on operator’s decision, the SMO assigns initial O-DU roles (active, stand-by). The SMO may then decide to perform switch between O-DU’s roles for specific O-DUs initially “paired” by operator based on alarms/performance counters/operator’s decision.

NOTE: The sub-use cases assume the hierarchical deployment scenarios.

# 4.20.2.13 Load-balancing sub-use case of a Shared O-RU

The following description details the actors involved in the resiliency use case of a Shared O-RU:

1) Shared O-RU: a) The Shared O-RU is actor that has its resources adjusted by the policy enforcer.   
2) O-DUs (host/tenant/ & other O-DUs): a) All the O-DUs connected to the Shared O-RU are actors that are relevant because they perform the load balancing working with the O-RU. They can also provide measurements relevant to the load-balancing policy.   
3) Policy enforcer (SMO, RIC, etc): a) The policy enforcer is an actor that executes the load-balancing policy. The policy defines the characteristics, triggers, and timing of how and when load-balancing occurs.

# 4.20.2.14 Coordinated reset of a Shared O-RU sub-use case for Multi-MNO

The following description details the actors involved in the coordinate reset of a Shared O-RU use case:

1) Shared O-RU: a) The Shared O-RU is actor that would be reset from the host O-DU.   
2) Shared O-RU Host (SOH): a) The SOH coordinates and issues the coordinate reset of a Shared O-RU.   
3) Shared Resource Operators (non-SOH SROs):

a) All the O-DUs connected to the Shared O-RU are actors that are relevant because they can request a coordinate reset also for the Shared O-RU.

4) SMO/Operator: a) The SMO operator can initiate a coordinated reset for the Shared O-RU.   
5) Partner SMO/Partner operator a) The SMO/partner operator can initiate a coordinated reset for the Shared O-RU.

# 4.20.2.15 Management of Shared O-RU during O-DU software update sub-use case for Shared O-RU for Single & Multi-MNO

The following description details the actors involved in the management of Shared O-RU during the SW update of O-DU subusecase:

1) Shared O-RU:

• The Shared O-RU which has its resources shared with the SW updated O-DU and other O-DUs.

2) O-DU SW change management rApp:

The rApp that supports SMO and Non-RT RIC in managing the SW change of the O-DU. This is an optional   
functionality which can alternately be implemented as an extended capability in one of the existing SMO   
functions. The capabilities of the O-DU SW change management rApp includes but not limited to the following:   
a) Validation of change management plan & impact assessment.   
b) Identification of the candidate Shared O-RU resources that can be shared based on the change plan and associated policies.   
c) Identification of the candidate O-DU for SW update.   
d) Translation of change management plan to O-DU and O-RU configurations.   
e) Recommendation of the configuration for Shared O-RU provisioning for m-plane setup with updated ODU.   
f) Recommendation of configuration for traffic evacuation of Shared O-RU and O-DU before the O-DU SW update.   
g) Monitoring and management of SW update by coordinating with other SMO functions, Shared O-RU and rApps.   
h) Management of fallout scenarios and recovery.

3) Shared O-RU orchestration rApp:

Supports partitioning of individual carriers of a Shared O-RU between updated O-DU and other O-DUs. This is an optional functionality which can alternately be implemented as an extended capability in one of the existing SMO functions.

4) SMO:

• Maintains inventory of Shared O-RUs and O-DUs.   
• Configures O-DUs and O-RUs with the support of the rApps.   
• Subscribe to alarms, notifications and measurements from O-DU and O-RU.   
• Sharing of alarm, notification and measurements from O-DU and O-RU with the rApps.

5) O-DU SW planner: Personnel:

Prepares O-DU SW change management strategy and associated plan. Based on the strategy and plan O-DU SW planner identifies the right software version, prepares target O-DU identification policies (for e.g., least loaded O-DU), Shared O-RU load sharing criteria (e.g., component carrier to be allocated), identifies carrier evacuation criteria, etc.

6) Sharing coordinator: Personnel:

Confirms that the Shared O-RU’s configuration complies with a sharing policy defined as per the O-DU SW change management requirement.

7) Updated O-DU:

• Responsible for load sharing the O-RU resources such as component carriers with other active O-DUs.

8) Original O-DUs:

• The original O-DU(s) are the O-DUs that the Shared O-RU were originally attached to.

# 4.20.2.16 Resource partitioning use case of Shared O-RU for Multi-MNO configuration

1) Owning operator sharing coordinator:

a) Recovers the inventory of Shared O-RUs and O-DUs and determines how to partition the resources of a Shared O-RU between multiple different O-DUs.

2) Owning operator SMO:

a) Provides inventory of Shared O-RUs and O-DUs.   
b) Configures call home identities in external transport systems.

3) Shared O-RU owning operator orchestration rApp:

a) Supports partitioning of individual carriers of a Shared O-RU between multiple different O-DUs operated by different operators.

4) Participating operator SMO:

a) Handles management of participating operator O-DU.

# 4.20.2.17 Start-up use case of a Shared O-RU for Multi-MNO configuration

1) Shared O-RU:

a) Performs call home and triggers establishment of network management session.

2) Owning operator SMO:

a) Recovers the software inventory of Shared O-RU and decides whether to upgrade operational software of Shared O-RU (hybrid management model).

3) Participating operator SMO:

a) Handles management of participating operator O-DU.

4) Owning operator O-DU:

a) Recovers the software inventory of Shared O-RU and decides whether to upgrade operational software of Shared O-RU (hierarchical management model).

5) Participating operator O-DU:

a) Expected to be a Shared O-RU Operator (SRO). The participating operator O-DU handles configuration of its component carriers with the Shared O-RU that it is connected to and has a communication link up.

# 4.20.2.18 Supervision use case of a Shared O-RU for Multi-MNO configuration

1) Shared O-RU:

a) Responsible for operating supervision on a per O-DU basis.   
b) Responsible for de-activating carriers associated with O-DU if there is supervision failure by O-DU.   
c) Responsible for signaling alarm to subscribers if O-DU supervision is lost.

2) Owning operator O-DU:

a) Responsible for repeatedly resetting the Shared O-RU’s supervision timer.

3) Participating operator O-DU:

a) Expected to be a Shared O-RU Operator (SRO). Has a heartbeat timer with the Shared O-RU that it is connected to and has a communication link up.

4) Owning operator SMO:

a) Responsible for subscribing to alarm notifications (hybrid management model). b) Responsible for forwarding alarm notifications to Shared O-RU orchestration rApp

5) Participating operator SMO:

a) Handles management of participating operator O-DU.

# 4.20.2.19 Antenna Line Device (ALD) control use case of a Shared O-RU for Multi-MNO configuration

The following actors are involved in the ALD control use case.

1) Owning operator antenna line device control rApp (for the Shared O-RU):

a) Responsible for determining which O-DU is responsible for ALD controller aspects.   
2) Owning operator O-DU: a) Responsible for implementing ALD controller.   
3) Participating operator O-DU: a) Expected to be a Shared O-RU Operator (SRO). Does not perform any operations directly with ALD until it becomes host under failure situations.   
4) Participating operator SMO: a) Handles management of participating operator O-DU.   
5) Shared O-RU (hardware): a) Responsible for bridging between OFH and HDLC.   
6) ALD (one or more ALD devices): a) Responsible for terminating HDLC.

# 4.20.2.20 Antenna calibration use case of a Shared O-RU for Multi-MNO configuration

The following are the principal actors in the antenna calibration use case for a Shared O-RU.

1) Owning operator antenna calibration rApp (Shared O-RU): a) Responsible for determining which O-DU is responsible for configuring common aspects of antenna calibration.   
2) Owning operator O-DU: a) Responsible for supporting Shared O-RU coordinated calibration.   
3) Participating operator O-DU: a) Expected to be a Shared O-RU Operator (SRO). The participating operator O-DU and does not perform calibration operations.   
4) Shared O-RU (HW): a) Responsible for implementing coordinated calibration.

# 4.20.2.21 Rehoming use case of a Shared O-RU for Multi-MNO

The following are the principal actors in the rehoming use case for Multi-MNO:

1) Shared O-RU: a) The Shared O-RU is the entity that is being rehomed.   
2) Original O-DUs: a) The original O-DU(s) (the owning operator O-DU and participating operator O-DU) are the O-DUs that the Shared O-RU were originally attached to. These O-DUs belong to different MNOs (the owning MNO and participating MNO).   
3) New O-DUs attached to: a) These are the new O-DU(s) (the owning operator O-DU and participating operator O-DU) that the Shared ORU will now be attached to. These O-DUs belong to different MNOs. The new O-DU(s) could be different ODUs than the original O-DU(s).   
4) Owning operator SMO: a) The owning operator SMO connects the owning operator O-DU to the Shared O-RU.   
5) Participating operator SMO: a) The participating operator SMO connects the participating operator O-DU which is connected to the Shared ORU.

# 4.20.2.22 Performance management use case of a Shared O-RU for Multi-MNO

1) Shared O-RU: a) Responsible for generating performance management notifications on a per partitioned carrier basis.   
2) Managing operator O-DU: a) Responsible for subscribing to receive performance management notifications from Shared O-RU.   
3) Participating operator O-DU: a) The O-DU of the participating operator that is also connected to the Shared O-RU.   
4) Managing operator SMO: a) The managing operator SMO, or another entity is an endpoint for the performance measurement data or reports.   
5) Participating operator SMO: a) The SMO of the participating operator which is an endpoint for the performance measurement data or reports from the participating operator O-DU.

# 4.20.2.23 Antenna calibration use case of a Shared O-RU for Multi-MNO

The following are the principal actors in the antenna calibration use case for a Shared O-RU.

1) Antenna calibration rApp (Shared O-RU) of owning operator (SMO): a) The owning operator App is responsible for telling the owning operator O-DU that it is responsible for the antenna calibration operation.   
2) Owning operator O-DU, participating operator O-DU: a) The owning operator O-DU is responsible for supporting Shared O-RU antenna calibration operation.   
3) Shared O-RU (HW): a) Responsible for implementing antenna calibration.

# 4.20.2.24 Dynamic resource shifting use case of a Shared O-RU

The following are the principal actors in the dynamic resource shifting use case:

1) Shared O-RU: a) The Shared O-RU is the entity that serves cells to the air.   
2) O-DU1, O-DU2: a) Responsible for processing of user data and radio resource handling.   
3) SMO: a) Responsible for configuration of Near-RT RIC, O-DUs and O-RU (used architecture does not matter for this sub-use case).   
4) Near-RT RIC: a) Responsible for control of dynamic resource shifting between cells served by cooperating O-DUs.

# 4.20.2.25 Static resource shifting use case for Single-MNO

The following are the actors in the static resource shifting use case:

1) Shared O-RU:

a) The Shared O-RU is the entity that serves cells to the air. b) The Shared O-RU terminates open fronthaul interface towards O-DU(s) and optionally towards SMO.   
2) O-DU1, O-DU2: a) Responsible for processing of user data and handle radio resources. b) O-DU(s) terminate open fronthaul interface towards O-RU. c) O-DU(s) terminate F1 interface towards O-CU.   
3) O-CU: a) O-CU terminates F1 interface towards O-DU(s). b) O-CU is responsible for RRC protocol handling for UEs.   
a) Responsible for configuration of O-CU, O-DUs and O-RU (depending on deployment SMO configures O-RU directly or through O-DU).   
b) In hybrid deployment SMO terminates open fronthaul interface towards O-RU.

# 4.20.3 Solution

# 4.20.3.1 General aspects of solutions for all Shared O-RU use cases

The following clauses describe solutions that apply to each of the sub–use cases. They describe different solutions for key aspects of Shared O-RU operation, such as the start-up, configuration, supervision, and performance management among other things. There are a few general aspects of each of these solutions that share similar goals, assumptions, actors, and roles and are captured in table 4.20.3.1-1.

Table 4.20.3.1-1: General aspects of solutions for all Shared O-RU use cases   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Common Goals</td><td rowspan=1 colspan=1>All the following sub-use cases involve either getting the Shared O-RUoperational or keeping it operational. Each of the sub-use cases explore adifferent aspect of these two common goals. Each of the sub-use cases hasa diferent specific goal and is trying to accomplish a particular dimension ofShared O-RU operation. This sub-use case is only applicable to thehierarchical configuration. Bringing into operation – Many of the sub-use cases have the goal to getthe Shared O-RU operational and capable of supporting over the air traffic.These include the resource partitioning， start-up， configuration, andsupervision sub-use cases. They are &quot;day 0&quot; related use cases.Maintaining service – The other set of sub-use cases are related tomaintaining service. These include the supervision, performance, andresiliency sub-use cases. These use cases relate to the continued operationof the Shared O-RU, thus &quot;day 2&quot; operation.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Common Actors</td><td rowspan=1 colspan=1>The Shared O-RU and the multiple O-DUs that the Shared O-RU is connectedto are common actors that apply to al the following sub-use cases.The common configurations that apply to the sub-use cases many alsoinvolve the management system between two operators.Some actors can be controlled by different operators and / or provided bydifferent solution providers.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>CommonAssumptions</td><td rowspan=1 colspan=1>For the following sub-use cases it is assumed that all relevant functions andcomponents are instantiated.Inventory management systems identify Shared O-RU and the available O-DUs as inventory elements.For all of the sub-use cases, an O-RU resources are statically partitionedbetween O-DUs (static configuration)</td><td rowspan=1 colspan=1></td></tr></table>

All the sub-use cases also apply a set of common configurations. These sub-use cases are intended to apply to Single Operator (MNO) and Multiple Operator (MNO) configurations. The configurations will be important to service providers, wireless operators as they roll out new networks. Those configurations can then be further broken down into either hybrid or hierarchical configurations. In a hierarchical configuration the SMO performs configuration and FCAPS/LCM with the O-DU which in does that for the O-RUs. In a hybrid configuration, the SMO can perform operations with either the O-DU and/or the O-RU. The O-DUs that share the O-RU can be from either common or different vendors. It can be envisaged that many more possible configurations or variations of those basic configurations could be supported by the following sub-use cases. For example, more than just two O-DUs. Sub-use cases present solutions that are intended to apply to all these possible configurations. Exceptions can arise from the variations of the resiliency sub-use case.

The collection of the sub-use cases either bring a Shared O-RU into operation by performing vital aspects of getting a Shared O-RU initially working; or they try to keep a Shared O-RU operational. Additionally, these sub-use cases apply to some other use cases such as class 2 BBU pooling (BBU pooling to achieve RAN elasticity use case), RAN sharing, and advanced multi-vendor multi-operator network slicing operation (multi-vendor slices). Support for different configuration, resiliency operation and, supervision that apply to Shared O-RU will often be relevant to these other related use cases as well. These other related use cases can use the following sub-use cases as building blocks operations because they provide basic goals and objectives to getting a Shared O-RU operational and keeping it running. Thus, the sub-use cases are likely be applicable to many those use cases outside of just this Shared O-RU use case.

# 4.20.3.2 Resource partitioning use case of Shared O-RU for Single-MNO

The following describes the solution for the resource partitioning sub-use case for a Shared O-RU.

The context of the resource partitioning use case of Shared O-RU is captured in table 4.20.3.2-1.

For mTLS, TLS and NACM security for this Shared O-RU sub-use case see requirements SEC-CTL-SharedORU-1, SECCTL-SharedORU-3 and SEC-CTL-SharedORU-4 in the O-RAN.WG11.TS.Security-Requirements-Specification.0- R004-v11.00 [39], clause 5.1.9.2.

Table 4.20.3.2-1: Resource partitioning use case of Shared O-RU   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>rApp has details on how a Shared O-RU&#x27;s resource are to be partitioned.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO provides inventory details of Shared O-RU and O-DUs.Sharing co-ordinator recovers inventory and decides on partitioning of carriersbetween O-DUs.Sharing co-ordinator uses resource partitioning rApp to partition resourceconfiguration of a Shared O-RU between O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated.Inventory management systems identify Shared O-RU carrier capabilities andavailable O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Sharing co-ordinator decides to share an O-RU between muliple O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>Inventory system is up to date.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Sharing co-ordinator recovers O-RU and O-DU inventory and decides onresource partitioning.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Sharing co-ordinator resource partitioning rApp to partition Shared O-RUbetween multiple O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>rApp signals O-DU identity(ies) to configuration management system.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Configuration management system configures transport systems with callhome identity(ies) for O-DU(s).</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 6.2.5</td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>rApp has details on how Shared O-RU&#x27;s resource are to be partitioned.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the resource partitioning use case is given in figure 4.20.3.2-1.

![](images/b7be3fedae1b5e1ba917cc727ffd5aa30f7a6f4cfb9262507794532c1117ed3b.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.2-1: Resource partitioning use case

# 4.20.3.3 Start-up use case of Shared O-RU for Single-MNO

The following describes the solution for the start-up sub-use case for a Shared O-RU.

The context of the Shared O-RU start-up use case is captured in table 4.20.3.3-1.

Table 4.20.3.3-1: Shared O-RU start-up use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The Shared O-RU is operating with the necessary software version andhas established network connectivity with the O-DU(s) and, for hybriddeployments, the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU calls home and establishes network management session.SMO is responsible for software management for the Shared O-RU whenoperating in hybrid management mode.O-DU is responsible for software management for the Shared O-RUwhen operating in hierarchical management mode.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Shared O-RU powers on.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Transport systems (DHCP server) has been configured with call homeconfiguration information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Establish synchronization:</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Each O-DU and Shared O-RU establish synchronisation with a timingsource, for example PTP (IEEE 1588) or Sync-E. See NOTE 1, NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Synchronization State Change Notification:After the O-RU has a synchronisation source, all subscribed O-DU(s) arenotified through a Synchronisation State Change Notification. We expectthe O-RU to be in the sync state "LOCKED".The Synchronisation State Change Notification goes from Shared O-RUto all subscribed O-DU(s). It is possible that the synchronisation procedure can happen in parallel tothe other steps of the start-up sub-use case. Thus, many of the othersteps in this use case can happen as the synchronization procedureoccurs. Even though this is shown as "step 2" this can complete afterother steps.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]Shared O-RU calls home and triggers establishment of networkmanagement session with SMO.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3and/or clause6.9.2</td></tr><tr><td colspan="1" rowspan="1">Step 4 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]Shared O-RU calls home and triggers establishment of networkmanagement session with O-DU#1.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3</td></tr><tr><td colspan="1" rowspan="1">Step 5 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]Shared O-RU calls home and triggers establishment of networkmanagement session with O-DU#2.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3</td></tr><tr><td colspan="1" rowspan="1">Step 6 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]SMO recovers software inventory.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.4</td></tr><tr><td colspan="1" rowspan="1">Step 7 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode and softwareupdate required]SMO triggers download of new software.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.5</td></tr><tr><td colspan="1" rowspan="1">Step 8 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode and softwareupdate required]O-RU downloads software files.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.5</td></tr><tr><td colspan="1" rowspan="1">Step 9 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode and softwareupdate required]SMO triggers the installation and activation of the software.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clauses 8.6and 8.7</td></tr><tr><td colspan="1" rowspan="1">Step 10 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode and softwareupdate required]SMO brings active software into operation.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.7</td></tr><tr><td colspan="1" rowspan="1">Step 11 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]O-DU recovers software inventory.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.4</td></tr><tr><td colspan="1" rowspan="1">Step 12 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode and softwareupdate required]O-DU triggers download of new software.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.5</td></tr><tr><td colspan="1" rowspan="1">Step 13 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode and softwareupdate required]O-RU downloads software files.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.5</td></tr><tr><td colspan="1" rowspan="1">Step 14 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode and softwareupdate required]O-DU triggers the installation and activation of the software.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clauses 8.6and 8.7</td></tr><tr><td colspan="1" rowspan="1">Step 15 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode and softwareupdate required]O-DU brings active software into operation .</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.7</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Shared O-RU is operating with the necessary software version andhas established network connectivity with the O-DU and, for hybriddeployments, the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: It is expected the O-RU and all O-DUs connected it would share the same synchronisation sourceotherwise, the O-DUs will drift in timing.NOTE 2: For more details on O-RU sync and O-RU loss of sync, see O-RAN.WG4.MP [28], clause 15.3.3.</td></tr></table>

The flow diagram of the Shared O-RU start-up use case is given in figure 4.20.3.3-1.

![](images/9f6785605cec32872c55e80ae71916d94f856fbbb8ec211fadf5d6e5a361429b.jpg)

> **Image Summary:** {"image": "image_ocran_001.png"}
  
Figure 4.20.3.3-1: Shared O-RU start-up use case

# 4.20.3.4 Configuration use case of a Shared O-RU for Single & Multi-MNO

The following describes the solution for the configuration sub-use case for a Shared O-RU.

The context of the Shared O-RU configuration use case is captured in table 4.20.3.4-1.

Table 4.20.3.4-1: Shared O-RU configuration use case

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The Shared O-RU is configured to operate with multiple O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">SMO responsible for Shared O-RU common configuration whenoperating in hybrid management mode.SMO optionally can subscribe to receive notifications of modifications toShared O-RU's configuration.When operating in hierarchical management mode, rApp is responsiblefor determining which O-DU is responsible for common configurationaspects.Shared O-RU responsible for role-based access control based on PLMN-Id.O-DU is responsible for Shared O-RU carrier configuration and optionally,when operating in hierarchical management mode, the Shared O-RUcommon configuration.Sharing co-ordinator can check the Shared O-RU's committedconfiguration complies with any sharing agreement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Shared O-RU has started up and has been configured with correctsoftware version.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]rApp determines which O-DU is responsible for common configuration ofShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">rApp triggers the configuration of the common aspects of the Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Non-RT RIC triggers the configuration of the common aspects of theShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (ALT)</td><td colspan="1" rowspan="1">[Hybrid or neutral host management mode]SMO uses OpenFronthaul interface to configure common aspects ofShared O-RU.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 9</td></tr><tr><td colspan="1" rowspan="1">Step 5 (ALT)</td><td colspan="1" rowspan="1">[Hierarchical management mode]SMO uses O1 interface to configure Shared O-RU's common aspects viaO-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (ALT)</td><td colspan="1" rowspan="1">[Hierarchical management mode]O-DU uses OpenFronthaul interface to configure common aspects ofShared O-RU.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 9</td></tr><tr><td colspan="1" rowspan="1">Step 7 (0)</td><td colspan="1" rowspan="1">Shared O-RU calls home to tenant's O-DU (multi-operator).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (0)</td><td colspan="1" rowspan="1">Shared O-RU calls home to tenant's SMO (multi-operator).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (0)</td><td colspan="1" rowspan="1">rApp triggers the configuration of the carrier aspects of the Shared O-RU(non-neutral host).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (0)</td><td colspan="1" rowspan="1">Non-RT RIC triggers the configuration of the carrier aspects of the SharedO-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (0)</td><td colspan="1" rowspan="1">SMO configures O-DU#1 and partitioned carrier information #1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (0)</td><td colspan="1" rowspan="1">O-DU#1 configures partitioned carrier information #1 on Shared O-RUnon-neutral host).</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 9</td></tr><tr><td colspan="1" rowspan="1">Step 13 (0)</td><td colspan="1" rowspan="1">Tenant's SMO configures O-DU#2 and partitioned carrier information #2(multi-operator).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">O-DU#2 configures partitioned carrier information #2 on Shared O-RU.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 9</td></tr><tr><td colspan="1" rowspan="1">Step 15 (0)</td><td colspan="1" rowspan="1">Shared O-RU implements role-based access control based oplmn-id#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (0)</td><td colspan="1" rowspan="1">The Shared O-RU notifies SMO of its modified configuration.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 9.4</td></tr><tr><td colspan="1" rowspan="1">Step 17 (0)</td><td colspan="1" rowspan="1">SMO signals Non-RT RIC information pertaining to changedconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (0)</td><td colspan="1" rowspan="1">Non-RT RIC signals changed configuration to Shared O-RUorchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 19 (0)</td><td colspan="1" rowspan="1">Sharing co-ordinator checks that the changed configuration compliancewith the sharing agreement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 20 (0)</td><td colspan="1" rowspan="1">Host sharing co-ordinator indicates non-compliance with tenant sharingco-ordinator and remedial actions agreed (out of band exchange).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Shared O-RU is configured with common aspects and partitionedcarrier#1 for O-DU#1 and partitioned carrier #2 for O-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">See NOTE.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE: Before activation of carrers, O-RU needs to have sync state “LOCKED" with its sync source. For moredetails, see O-RAN.WG4.MP [28], clause 15.3.3.</td></tr></table>

The flow diagram of the Shared O-RU configuration use case is given in figure 4.20.3.4-1.

![](images/5468cc43fac9b9158fba78c468e6c15725ac78e222995d23f46930ba7d970a31.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.4-1: Shared O-RU configuration use case

# 4.20.3.5 Supervision use case of a Shared O-RU for Single-MNO

The following describes the solution for the supervision sub-use case for a Shared O-RU.

The context of the supervision use case of a Shared O-RU is captured in table 4.20.3.5-1.

Table 4.20.3.5-1: Supervision use case of a Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The Shared O-RU operates watchdog timers with each of its O-DUs andceases transmitting on a partitioned carrier associated with an O-DU if iswatchdog timer to that O-DU expires.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU operates watchdog timers and deactivates any carriersassociated with an expired watchdog timer.O-DU repeatedly resets the Shared O-RU's supervision timer.SMO forwards any alarms to Shared O-RU rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-DUs are operating fronthaul control and user plane for their respectivepartitioned carriers.SMO has subscribed to receive alarm notifications (hybrid managementmodel).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">An O-DU subscribes to receive supervision notifications.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (Loop)</td><td colspan="1" rowspan="1">O-DU#1 performs supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (O)</td><td colspan="1" rowspan="1">Shared O-RU detects supervision failure with O-DU#1 and ceasestransmiting on partitioned carrier associated with O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Shared O-RU sends alarm notification to Fault Management</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">Fault management sends alarm notification to Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">Non-RT RIC sends alarm notication to Shared O-RU orchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (Loop)</td><td colspan="1" rowspan="1">O-DU#2 performs supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (0)</td><td colspan="1" rowspan="1">Shared O-RU detects supervision failure with O-DU#2 and ceasestransmitting on partitioned carrier associated with O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 ( )</td><td colspan="1" rowspan="1">Shared O-RU sends alarm notification to fault management.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (0)</td><td colspan="1" rowspan="1">Fault management sends alarm notification to Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (0)</td><td colspan="1" rowspan="1">Non-RT RIC sends alarm notication to Shared O-RU orchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">O-DU terminates subscription to supervision notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the supervision use case of a Shared O-RU is given in figure 4.20.3.5-1.

![](images/8b128c68f54206120530877bef75b4be449eb615438c6a5aacf0d09f62f32cf5.jpg)

> **Image Summary:** {"image": "image_of_5g_oran_architecture.png"}
  
Figure 4.20.3.5-1: Supervision use case of a Shared O-RU

4.20.3.6 Performance management use case of a Shared O-RU for Single-MNO

The following describes the solution for the performance management sub-use case for a Shared O-RU.   
The context of the performance management use case of a Shared O-RU is captured in table 4.20.3.6-1.

# Table 4.20.3.6-1: Performance management use case of a Shared O-RU

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Each O-DU has established subscriptions to receive performancemanagement notifications regarding operation of the fronthaul betweenthe O-DUs and Shared O-RU.The O-DU and Shared O-RU are able to report performancemeasurement data towards their consumers in a Multi-MNoconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU generates performance management notifications on a perpartitioned carrier basis.O-DU subscribes to receive performance management notifications fromShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-DU has configured performance management metrics for respectivepartitioned carrier.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Fronthaul control and user plane is operational between O-DU andShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">O-DU#1 subscribes to receive PM notifications from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">O-DU#2 subscribes to receive PM notifications from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (loop)</td><td colspan="1" rowspan="1">Shared O-RU sends PM notification to O-DU#1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (loop)</td><td colspan="1" rowspan="1">Shared O-RU sends PM notification to O-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">O-DU to SMO performance operations</td></tr><tr><td colspan="1" rowspan="1">Step 1 (O)</td><td colspan="1" rowspan="1">PM event notification reportingThe O-DU (producer) sends performance data to the SMO (consumer)through an event notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">Streaming PM reportsThe O-DU establishes a persistent connection to the SMO (consumer)and sends performance data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Attribute-based or URI-based collectionPerformance data is read by the consumer (SMO) through configurationmanagement atribute. Alternatively, the O-DU can support a datascraping method where a collector (SMO) reads the data from a pre-defined URI.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (O)</td><td colspan="1" rowspan="1">Producer or PM file upload (file upload)O-DU uploads a PM file to the SMO.See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td rowspan="2">Step 5 (O)</td><td>Consumer downloads PM file (file download)</td><td rowspan="2"></td></tr><tr><td colspan="1">O-DU issues file ready notification to SMO about the data being ready for download， or SMO periodically polls the O-DU. Afterwards, the SMO (consumer) can download the PM file.</td></tr><tr><td rowspan="2">Step 1 (0)</td><td>O-RU to O-DU performance operations (in hierarchical configuration) PM event notification reporting</td><td rowspan="2"></td></tr><tr><td colspan="1">The O-RU sends performance data to the O-DU through an event</td></tr><tr><td rowspan="2"></td><td>notification. The notification is sent to a subscriber of performance data. O-DU requests for O-RU to start sending PM data</td><td rowspan="2"></td></tr><tr><td colspan="1">O-DU invokes an RPC to give PM credentials, target URI, and periodicity notification interval to the Shared O-RU. This includes all the necessary</td></tr><tr><td rowspan="2">Step 1 (M)</td><td>information for the O-RU to perform a file transfer to an endpoint periodically.</td><td rowspan="2"></td></tr><tr><td colspan="1">See NOTE 2. Shared O-RU uploads PM file</td></tr><tr><td rowspan="2">Step 2 (M)</td><td></td><td rowspan="2"></td></tr><tr><td colspan="1">The Shared O-RU periodically uploads a performance fil to the target URI using the PM credentials given by the O-DU. O-RU to SMO performance operations (in hybrid configuration)</td></tr><tr><td rowspan="4">Step 1 (0) Step 1 (0)</td><td>PM event notification reporting</td><td rowspan="4"></td></tr><tr><td colspan="1">The O-RU sends performance data to the SMO through an event</td></tr><tr><td colspan="1">notification via M-plane. SMO requests for O-RU to start sending PM data</td></tr><tr><td colspan="1">SMO invokes an RPC to give PM credentials, target URI, and periodicity</td></tr><tr><td rowspan="2">Step 2 (0)</td><td>periodically. Shared O-RU uploads PM file</td><td></td></tr><tr><td>The Shared O-RU uploads performance file to target URI using PM credentials given by the SMO.</td><td colspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">1) Subscriptions setup: O-DU terminates subscription to performancemanagement notification.2)O-DU to SMO sending PM data: Use case ends with the producer(O-DU) sending performance data to the consumer (SMO).3)O-RU sending performance data: Use case ends with the producer(O-RU) starting to send performance data to the subscriber.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The consumer has received performance data and may perform postprocessing operations on the data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: When the O-DU sends performancefiles received from a Shared O-RU, they are converted to the proper3GPP format before sending to SMO. See O-RAN WG5.O-DU-O1 [25].NOTE 2: The O-DU establishes a framework for the Shared O-RU to send PM files. This operation is performedonly once, thereafter, the Shared O-RU sends the PM files periodically.</td></tr></table>

The flow diagram of the performance management use case of a Shared O-RU is given in figure 4.20.3.6-1.

![](images/b0d562d88cd0fae1825bfb77716d53e2351ce3b1c4590b4f7712f062cb93f5e9.jpg)

> **Image Summary:** {"entities": ["O-RU", "O-DU", "near-RT RIC", "far-RT RIC", "non-RT RIC", "O-RAN Alliance", "O-RAN Architecture", "O-RAN Interfaces", "O-RAN", "O-RAN Management and Orchestration", "O-RAN Interfaces: Network Graph", "O-RAN", "O-RAN Interface specification", "O-RAN Architecture", "O-RAN", "near-RT RIC", "far-RT RIC", "non-RT RIC", "O-RU", "O-DU", "near-RT RIC", "far-RT RIC", "non-RT RIC", "O-RAN", "O-RAN Architecture", "O-RAN Interfaces", "O-RAN Management and Orchestration", "O-RAN Interfaces: Network Graph"], "relationships": ["O-RAN Alliance → O-RAN Architecture: defines", "O-RAN Architecture → O-RAN Interfaces: specifies", "O-RAN Architecture → O-RAN Management and Orchestration: enables", "O-RAN Interfaces → O-RAN: provides interfaces", "O-RAN Management and Orchestration → O-RAN: enables management", "near-RT RIC → O-DU: near-RT RIC", "far-RT RIC → O-DU: far-RT RIC", "non-RT RIC → O-DU: non-RT RIC", "O-RU → O-DU: Fronthaul interface", "near-RT RIC → O-RU: A1 interface", "far-RT RIC → O-RU: A1 interface", "non-RT RIC → O-RU: A1 interface"], "hierarchy": ["O-RAN Architecture contains: O-RU, O-DU, near-RT RIC, far-RT RIC, non-RT RIC"], "flows": [], "notes": ["Figure: O-RAN Interfaces: Network Graph", "Labels: O-RAN, O-RAN Architecture, O-RAN Interfaces, O-RAN Management and Orchestration, O-RU, O-DU, near-RT RIC, far-RT RIC, non-RT RIC, A1 interface, Fronthaul interface"]}
  
Figure 4.20.3.6-1: Performance management use case of a Shared O-RU for Single-MNO

# 4.20.3.7 Antenna Line Device (ALD) control use case of a Shared O-RU for Single-MNO

The following describes the solution for the ALD control sub-use case for a Shared O-RU.

The context of the antenna line device control use case of a Shared O-RU is captured in table 4.20.3.7-1.

Table 4.20.3.7-1: Antenna line device control use case of a Shared O-RU   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>The ALD connected to Shared O-RU is configured to operate with ALDcontroller.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors andRoles</td><td rowspan=1 colspan=1>rApp is responsible for determining which O-DU is responsible for ALDcontroller aspects.O-DU is responsible for implementing ALD controller.O-RU is responsible for bridging between OFH and HDLC.ALD is responsible for terminating HDLC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Shared O-RU has started up and has been configured with correctsoftware version.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>rApp determines which O-DU is responsible for performing ALD controllerfunctionality.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>rApp triggers the configuration of the ALD controller for Shared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RIC triggers the configuration of ALD controller for Shared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>SMO uses O1 interface to configure ALD controller in O-DU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>O-DU uses OpenFronthaul interface to configure ALD aspects of SharedO-RU.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 9</td></tr><tr><td rowspan=1 colspan=1>Step 6 (M)</td><td rowspan=1 colspan=1>O-DU uses OpenFronthaul interface to signal ALD.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>Shared O-RU provides interworking between OFH and HDLC.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>ALD connected to Shared O-RU is configured correctly.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the antenna line device use case is given in figure 4.20.3.7-1.

![](images/5621d73dc73bb18efd6c682e1929423f204f49144c3a396b01f5cae74e965908.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.7-1: Antenna line device use case

4.20.3.8 Basic resiliency use case (active O-DU failure) for Single-MNO

The following describes the solution for the basic resiliency sub-use case for a Shared O-RU.

The context of the basic resiliency use case of a Shared O-RU is captured in table 4.20.3.8-1.

Table 4.20.3.8-1: Resiliency use case of a Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The goal of this sub-use case is to handle situations related to resiliencyoperations with the Shared O-RU when the O-DU is out of service.This is a service impacting use case.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RUThe Shared O-RU handles the fronthaul and air interfaces andthe reporting of performance counters and failures.O-DUs (active/standby O-DUs)All the O-DUs connected to the Shared O-RU are actors that areinvolved in basic resiliency scenario.O-CU:O-CU receives cell related configurations from SMO andavailable cell details from O-DU(s). Based on the availableresources reported by O-DU and desired availability of cells</td><td colspan="1" rowspan="1"></td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>Related use</td></tr><tr><td>SMO:</td><td>received from SMO, the O-CU activates or deactivates the cells in the O-DU using F1 interface. The SMO configures the role of O-DUs as active or standby O-DUs</td><td></td></tr><tr><td></td><td>and informs these roles to Shared O-RU through O-DU in hierarchical deployment. It makes high-level decisions related to conditions listed in clause 4.20.1.8. It is assumed that when active O-DU fails, there is stil at least one standby O-DU having active NetConf session with the Shared O-RU.</td><td></td></tr><tr><td>Assumptions</td><td>It is assumed that the resiliency operations are intended to take over the Shared O-RU operation and recover the service to the end user.</td><td></td></tr><tr><td rowspan="5">Begins when</td><td>There are many possible scenarios that trigger the basic resiliency use</td><td></td></tr><tr><td>case as described in clause 4.20.1.8. In this basic resiliency use case, only the complete failure of a O-DU is</td><td colspan="1"></td></tr><tr><td>considered.</td><td colspan="1"></td></tr><tr><td>The purpose of the resiliency use case is to keep the Shared O-RU &amp; O- DU system operational in the case of a failure of the active O-DU.</td><td colspan="1"></td></tr><tr><td>This use case begins when the active O-DU encounters a failure (operational state = disabled). The Shared O-RU has the NetConf connectivity with two or more O-DUs.</td><td colspan="1"></td></tr><tr><td>Pre-conditions</td><td>CU plane monitoring has been properly configured which sets up a communication monitoring interval for the interface between the Shared O-RU and active O-DU.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>O-DUs have subscribed to alarm notifications successfully. Basic resiliency use case - Initial system setup</td><td></td></tr><tr><td>Step 1.1 (M)</td><td>The SMO may configure O-DU#1 to take active role in controlling the Shared O-RU. It then configures the cells and corresponding carrier</td><td></td></tr><tr><td>Step 1.2 (M)</td><td>resources (including NRCGI(s) for the cells) via the O1 interface. O-DU configures the carriers in O-RU, corresponding to the carrier</td><td></td></tr><tr><td>Step 1.3 (M)</td><td>resources outlined in step 1. The SMO may configure O-DU#2 to take standby role via O1 interface.</td><td></td></tr><tr><td>Step 1.4 (M)</td><td>SMO may provide O-CU with information via the O1 interface regarding which cell(s) (NRCGI(s)) associated with O-DU#1 need to be activated.</td><td></td></tr><tr><td></td><td>See NOTE 1, NOTE 2, NOTE 3, NOTE 4. Basic resiliency use case – O-DU#1 failure detection</td><td></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Active O-DU failsActive O-DU (the one serving as the active role) is no longer operational.The O-DU is no longer able to provide service. The O-DU has operationalstate = disabled. The Shared O-RU losses communication with the activeO-DU. See NOTE 5.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">O-RU raises alarms to subscribersThe Shared O-RU raises the loss of connectivity alarm to subscriber(s).The simple case shows that the O-DU#1 and O-DU#2 are subscribers.The Shared O-RU raises an alarm to subscribers (O-DUs) that are stillactive that is O-DU #2, connected and subscribed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Alarm forwardedThe Shared O-RU alarm is forwarded to the managing entity, such as theSMO. It is possible that the SMO will make the decision for making thestandby O-DU#2 into the active O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">SMO provides O-CU with information regarding which cell(s) (NRCGI(s))associated with O-DU#2 need to be made inactive and/or removed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Recover Shared O-RU operation</td></tr><tr><td colspan="1" rowspan="1">Step 6.1 (M)</td><td colspan="1" rowspan="1">The SMO may configure O-DU#2 to take standby role via O1 interface.See NOTE 6.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6.2 (M)</td><td colspan="1" rowspan="1">O-DU#2 becomes the active O-DU to recover Shared O-RU operation.See NOTE 7.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6.3 (M)</td><td colspan="1" rowspan="1">O-DU configures the carriers in O-RU, corresponding to the carrierresources outined in step 6.1. See NOTE 8.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6.4 (M)</td><td colspan="1" rowspan="1">SMO provides O-CU with information regarding which cell(s) (NRCGI(s))associated with O-DU#2 need to be activated. See NOTE 1, NOTE 2,NOTE 9, NOTE 10, NOTE 11.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The use case ends when the standby O-DU, O-DU#2 shown in the flowdiagram has taken over for the previously active O-DU, O-DU #1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">There are many possible exceptions. Some of these include: If the Shared O-RU fails during a switch over.If the standby O-DU#2 also becomes unavailable when it is due tobecome active. If any event messaging for the flow is lost.If configuration was not done properly.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">If the standby O-DU losses the configuration data from the configurationreplica.If the active O-DU returns to service while the standby O-DU is trying tobecome the active O-DU.If the connectivity, or functionality of the management system (SMO)becomes unavailable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Successful post condition – On a successful post-condition, the SharedO-RU is connected to the newly active O-DU, the newly active O-DU isoperational and has properly synced with the O-RU.Failure post condition – If one of the various exception cases occurs,there are a variety of failure post conditions. If no O-DUs are availableand the O-RU is orphaned no service is available and the O-RU shallshutdown operations. If misconfiguration occurs the O-RU will respondaccordingly. If there are ever two active O-DUs, the Shared O-RU willoperate accordingly.</td><td colspan="1" rowspan="1"></td></tr></table>

NOTE 1: When cells and corresponding carriers are configured and available for service, the O-DU informs O-CU about cells availability using F1 interface. O-CU requests O-DU to activate the cell(s) (NRCGI(s)), using the associated messages exchanged via the F1 interface. O-DU activates the carrier in O-RU that are associated with the specific cell(s) (NRCGI(s)) requested for activation.

NOTE 2: O-DU activates carriers related to cell(s) requested by O-CU. O-DU uses the F1 interface to inform O-CU about activation status for cells requested.

NOTE 3: Shared O-RU becomes operational with O-DU#1 with cell on air and ready to serve UEs.

NOTE 4: SMO collects alarms and performance management data from O-DU#1.

NOTE 5: The active O-DU can be no longer operational for a variety of reasons. (see the “Begins when” section).

NOTE 6: There might be multiple other O-DUs, but only one active O-DU. The management system, SMO, shall know and coordinate and ensure that there is only one active O-DU.

NOTE 7: There are preconditions that are relevant and necessary for this to happen. It is necessary that a call home between the O-RU and standby O-DU, and the replication of the configuration information has occurred, and that the

standby O-DU has the configuration of the active O-DU.

NOTE 8: The new active O-DU has control only of its carriers. The new O-DU does not handle ALDs.

NOTE 9: Shared O-RU operations are restored with O-DU#2, subsequently services to the users are reestablished, i.e., CUS-plane is up and running.

NOTE 10: SMO collects the alarms and performance management data from O-DU#2.

NOTE 11: The transition of the active role from O-DU#2 back to O-DU#1 involves the same steps as the initial transition from the O-DU#1 to O-DU#2, with the exception of which O-DU is to be activated. This activity is initiated based on a trigger from the SMO and/or the operator's decision.

The flow diagram of the basic resiliency use case is given in figure 4.20.3.8-1.

![](images/5666dffb203fe5213e29b6570162e1ace640be6f068b14bcf5fee3854e4250fb.jpg)

> **Image Summary:** {"image": "image_ocu_o_du_ran_architecture.png"}
  
Figure 4.20.3.8-1: Basic resiliency use case

# 4.20.3.9 Antenna calibration use case of a Shared O-RU for Single-MNO

The following describes the solution for the antenna calibration sub-use case for a Shared O-RU in a Single-MNO configuration.

The step-by-step details of the antenna calibration use case of a Shared O-RU are captured in table 4.20.3.9-1.

# Table 4.20.3.9-1: Antenna calibration use case of a Shared O-RU

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The host O-DU performs an antenna calibration procedure with theShared O-RU.The O-DU reports antenna calibration results to the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU performs the antenna calibration procedure.O-DU (host) can request for antenna calibration procedure with SharedO-RU.SMO can receive results from calibration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-DU has connectivity to O-RU.All actors are operational and have initialized.Fronthaul control and user plane is operational between O-DU andShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">1. The Shared O-RU has detected that antenna calibration is required.2. The O-DU initiates an antenna calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.1 (0)</td><td colspan="1" rowspan="1">Recalibration required (O-RU initiated)The Shared O-RU has detected that antenna calibration is needed andsends an antenna calibration needed notification to the host O-DU overthe open FH. In this case, the O-RU initiates the calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.2 (O)</td><td colspan="1" rowspan="1">Calibration requestThe host O-DU requests for antenna calibration procedure to start forShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Calibration request (O-DU initiated)The host O-DU requests for antenna calibration procedure to start forShared O-RU. In this case the O-DU initiates the calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Calibration operation at O-RUShared O-RU performs antenna calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Calibration responseShared O-RU responds with antenna calibration results.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Calibration resultsThe O-DU returns antenna calibration results to SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">(1) Antenna calibrated: Antenna calibration procedure has finished, andresults reported.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">The O-RU may indicate a calibration failure, which is reported to the O-DU. The O-DU logs the failure and notifies north-bound entities.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1">[</td></tr></table>

The flow diagram of the antenna calibration use case of a Shared O-RU for Single-MNO is given in figure 4.20.3.9-1.

![](images/57d570f6944e2435fa22197429c359af16154132cd1816b4293f1d305997f007.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.9-1: Antenna calibration use case of a Shared O-RU for Single-MNO

# 4.20.3.10 Rehoming use case of a Shared O-RU for Single-MNO

The following will describe the solution for the rehoming sub-use case for a Shared O-RU.

The context of the rehoming use case of a Shared O-RU for Single-MNO is captured in table 4.20.3.10-1.

Table 4.20.3.10-1: Rehoming use case of a Shared O-RU for Single-MNO   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">A Shared O-RU is rehomed and is able to pair with new O-DU or existing(previous) O-DU parents.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU is the element that is rehomed.Host O-DU (old) is the original Shared O-RU parent.SRO O-DU (old) is another original O-DU Shared O-RU is connected to.Host O-DU (new) is the new Shared O-RU parent.SRO O-DU (new) is another new O-DU Shared O-RU is connected to.SMO can receive results from calibration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">The Shared O-RU is in a deployment with the original (old) O-DUs and will be moved to the new ones or could stay with original O-DUs (asparents).(Typically) the operator wil plan a Shared O-RU rehoming activity beforethey actually perform the operations related to the move.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">This use case starts with any of these three situations:Case #1 starts when the Shared O-RU is physically moved to a newlocation (however still connected to original O-DUs).Case #2 starts when the Shared O-RU is physically moved to a newlocation but is connected to new O-DUs.Case #3 starts when the Shared O-RU stays in same physical locationbut is connected to new O-DUs (management-initiated rehoming).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Case #1 – O-RU is physically moved with same O-DU parents</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Shared O-RU is disconnected from original O-DUsThe Shared O-RU is physically disconnected (fiber disconnected) fromthe existing O-DU parents.Then, the Shared O-RU is physically moved to a new location.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Shared O-RU is reconnected to original O-DUsThe Shared O-RU is either physically reconnected (different fiber) orconnected at the transport layer (with the original fiber) to the original O-DU parents, and the following sub-use cases are triggered as a result:</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">●  Shared O-RU startup sub-use case・Configuration sub-use caseResource partitioning sub-use caseReset sub-use case supervision sub-use case</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Case #2 – O-RU is physically moved with new O-DU parents</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Shared O-RU is disconnected from original O-DUsThe Shared O-RU is physically disconnected (fiber disconnected) fromthe former O-DU parents.Then, the Shared O-RU is physically moved to a new location.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Shared O-RU is connected to new O-DUsThe Shared O-RU is either physically reconnected (different fiber) orconnected at the transport layer (with the original fiber) to new O-DUparents, and the following sub-use cases are triggered as a result:• Shared O-RU startup sub-use caseConfiguration sub-use case● Resource partitioning sub-use case•Reset sub-use case supervision sub-use case</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Case #3 – Management initiated rehoming</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Management initiated rehoming for Shared O-RUShared O-RU already has physical front-haul connections in place.SMO initiates rehoming operation with connected O-DUs to the SharedO-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Shared O-RU starts upThe Shared O-RU starts up with the new O-DU parents, and the fllowingsub-use cases are triggered as a result:・Shared O-RU startup sub-use caseConfiguration sub-use caseResource partitioning sub-use case● Reset sub-use case supervision sub-use case</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Shared O-RU has been moved and connected to the appropriate O-DUs, and is operational again.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1">[</td></tr></table>

The flow diagram of the rehoming use case of a Shared O-RU for Single-MNO is given in figure 4.20.3.10-1.

![](images/b86b4e75997d7b9be622bbe12610179c8e6892d6a87e120e4fd2d8a0dc15a315.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.10-1: Rehome by physically moving Shared O-RU with same O-DU for Single-MNO

The flow diagram of the rehoming use case of a Shared O-RU for Single-MNO is given in figure 4.20.3.10-2.

![](images/b7c79884ed3166ed70bbbaaeeeaa5ef58d32ca674044be886cb80ab2426766dd.jpg)

> **Image Summary:** {"image": "image.png"}


# 4.20.3.11 Reset use case of a Shared O-RU for Single-MNO

The following describes the solution for the reset sub-use case for a Shared O-RU.

The context of the reset use case of a Shared O-RU is captured in table 4.20.3.11-1.

Table 4.20.3.11-1: Reset use case of a Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The goal of this sub-use case is to describe the flow related to reset ofShared O-RU for a Single-MNO operator configuration.This is a service impacting use case.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU:The Shared O-RU is a key actor. It undergoes reset in this use case.The Shared O-RU can be reset by intention/request orautonomously.O-DUs (host/tenant/ &amp;other O-DUs):All the O-DUs connected to the Shared O-RU are actors areinvolved in the reset operation. O-DU#1 has the role of the SharedO-RU host, it also has a role of Shared Resource Operator (SRO).O-DU#2 is only an SRO.SMO:The SMO is informed by the O-DU that O-RU has been reset orissues a reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">It is assumed that there is always at least one O-DU still operationalwith the Shared O-RU.This use case describes the flow for a Single-MNO operatorconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The reset of a Shared O-RU use case can be invoked when there is adirect request to reset the Shared O-RU, or it can be resetautonomously.There are many possible reasons why a Shared O-RU can need to be intentionally reset. Maintenance, software upgrade, network failure,power outages, communication ink issues are just some of the manypossible situations where the active O-RU would be reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">The Shared O-RU has connectivity to one or more O-DUs (and one ofthem is serving the primary role).The Shared O-DU has been configured originally by the active O-DU,and also carriers for the standby O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">O-DUs have subscribed to alarm notifications successfully.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">[Shared O-RU reset fl low]Reset request from SMOA reset request is communicated from the SMO to the Shared O-RUhost (O-DU #1). The reset request can be originated from the SMO for avariety of reasons.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Reset request from O-DUThe reset request is communicated onward from the Shared O-RU host(O-DU #1) to the Shared O-RU through the open front-haul interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Reset replyThe Shared O-RU RPC Reply Acknowledge is sent from the Shared O-RU to the Shared O-RU host (O-DU #1).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Shared O-RU resetOnce invoked, the Shared O-RU goes through its reset sequence tocomplete the reset operation.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Reset responseThe Shared O-RU host (O-DU #1) informs the SMO with a resetresponse.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">[Autonomous reset flow]Autonomous Shared O-RU resetThe Shared O-RU is autonomously reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">O-DU initial detects loss of connection.</td><td colspan="1" rowspan="1"></td></tr><tr><td rowspan="4">Step 8 (M)</td><td>The Shared O-DU host (O-DU #1) detects loss of polling as a result of the autonomous O-RU reset. It can also detect a call home signal from a Shared O-RU that just had a valid M-plane session.</td><td rowspan="4"></td></tr><tr><td colspan="1">O-DU determines loss of connection. The O-DU can deduce that O-RU has a lost connection with broken</td></tr><tr><td colspan="1">polling with the O-DU. The O-DU does not know if the O-RU was performing a reset or if there was other reason for the lost connection, for example, a broken optical fiber. The O-DU can only report lost connection to O-RU in such a case.</td></tr><tr><td colspan="1">The O-DU redetects the Shared O-RU through a call home from the Shared O-RU. Then the Shared O-RU Start up sequence of that sub- use case happens (see the ref flow). Afterwards, the O-DU can read the reset cause from the Shared O-RU.</td></tr><tr><td>Step 9 (M)</td><td>O-DU informs SMO. When the O-DU #1 starts sensing cal home signals from O-RU, O-DU can deduce that O-RU has returns to service after a reset. Afterwards, the O-DU #1 can read the restart cause. Then, the Shared O-DU host can report to SMO that O-RU is re-detected and what was the reason why the O-RU reset. Then O-DU can fill update its aggregated model with details obtained from the O-RU and populate this information to SMO. Step 14 When O-DU redetects, the SMO can clear the alarm.</td><td></td></tr><tr><td>Ends when</td><td>The use case ends the Shared O-RU has reset whether by reset or by autonomous reset.</td><td></td></tr><tr><td rowspan="2">Exceptions</td><td>There are many possible exceptions. Some of these include: The Shared O-RU was not able to successfully reset.</td><td></td></tr><tr><td>The O-DU #1 was not able to properly detect lost connection with the Shared O-RU through loss of polling or call home signal was never sent. The O-DU #1 was not able to establish a restore connection to the Shared O-RU after reset.</td><td colspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Successful post condition – On a successful post-condition, the SharedO-RU is reset, and has restored connectivity to the Shared O-RU host(O-DU #1).Failure post condition – One of the failure exceptions has beenencountered.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the reset use case is given in figure 4.20.3.11-1.

![](images/6c193a7f2b01c29c695c8591a4eb82e8696b34aed026050ab7a7547ca5a83921.jpg)

> **Image Summary:** {"image": "o-ran_call_flow.png"}
  
Figure 4.20.3.11-1: Reset use case

# 4.20.3.12 Advanced resiliency sub-use cases of a Shared O-RU for Single-MNO

Advanced resiliency sub-use cases describe interactions between actors for resiliency operations.

4.20.3.12.1 Advanced resiliency sub-use case with 1 O-DU active $^ +$ 1 O-DU standby $( 1 + 1 )$

The context of the advanced resiliency sub-use case with 1 O-DU active $^ { + 1 }$ O-DU standby $( 1 + 1 )$ is captured in table 4.20.3.12.1-1.

Table 4.20.3.12.1-1: Advanced resiliency sub-use case with 1 O-DU active $^ +$ 1 O-DU standby $( 1 + 1 )$   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>The objective of this sub-use case is to manage resiliency operations involving the active and stand-by O-DUs with the Shared O-RU. This includes system behaviour in situations such as partial O-DU failures, interface failures, and power outages related to the O-DU. This ensures to restore the service availability to end users.</td><td rowspan="9"></td></tr><tr><td rowspan="5">Actors and O-CU: Roles</td><td>This is a service impacting use case. Shared O-RU:</td></tr><tr><td>The Shared O-RU handles the fronthaul and air interfaces and the reporting of performance counters and failures. O-DUs (active/stand-by O-DUs):</td></tr><tr><td>O-DUs may receive configurations from SMO. The O-DU may report performance counters and alarms to SMO. The O-DU is also responsible for configuring and collecting the performance data and alarms from O-RU(s) in hierarchical deployment. This use case focusses on active / stand-by role change for O-DUs to minimize service disruption.</td></tr><tr><td>O-CU receives cell related configurations from SMO and available cell details from O-DU(s). Respectively to available resources reported by O-DU and desired availability of cells received from SMO. The O-CU activates or deactivates the cells in the O-DU using F1 interface.</td></tr><tr><td>SMO: The SMO configures the role of O-DUs as active and standby O- DUs and informs these roles to Shared O-RU through O-DU in hierarchical deployment or directly in case of hybrid deployment.</td></tr><tr><td>SMO also makes high-level decisions about O-DU role change based on e.g., received alarms and degraded performance.</td></tr><tr><td>Assumptions</td><td>The assumptions are based on the premise that there will always be at least one O-DU remains operational with the Shared O-RU. This use case is triggered when the SMO detects the partial failure</td><td></td></tr><tr><td>Begins when</td><td>related to active O-DU based on alarms or service performance degradation. The use case may also be triggered due to various interfaces malfunction or service degradation. 1. The Shared O-RU is on.</td><td></td></tr><tr><td>Pre-conditions</td><td>2. Prior carrier activation (step 6) O-RU's sync-state is "locked". 3. All actors are connected to same sync source.</td><td></td></tr><tr><td>Step 1 (M)</td><td>The SMO may configure O-DU#1 to take active role in controlling the Shared O-RU. It then configures the cells and corresponding carrier resources (including NRCGI(s) for the cells) via the O1 interface.</td><td></td></tr><tr><td>Step 2 (M)</td><td>O-DU configures the [tr]x-array-carrier(s) in O-RU, corresponding to the carrier resources outlined in step 1.</td><td></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">The SMO may configure O-DU#2 to take stand-by role via O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">SMO may provide O-CU with information regarding which cell(s)(NRCGl(s) associated with O-DU#1 need to be activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">When cells and corresponding carriers are configured and available forservice, the O-DU informs O-CU about cell availability using F1interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">O-CU requests O-DU#1 to activate the cel(s) (NRCGI(s)), using theassociated messages exchanged via the F1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">O-DU#1 activates the [tr]x-array-carrier(s) in O-RU that are associatedwith the specific cell(s) (NRCGIl(s)) requested for activation in step 6.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">O-DU#1 activates the cell(s) as requested by O-CU in step 6.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">O-DU#1 uses the F1 interface to inform O-CU about activation statusfor cells requested in step 6.See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="4" rowspan="1">Advanced resiliency use case for partial failure (interface or node)/performance degrade scenarios. SMOmakes a high-level decision to make the Shared O-RU remains operational by initiating an O-DU switch</td></tr><tr><td colspan="1" rowspan="1">Step 10.1 (M)</td><td colspan="1" rowspan="1">See NOTE 2 and NOTE 3.The SMO set the administrative state of the O-DU#1 to "locked" and itsoperational state is set to "disabled".See NOTE 4.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.2 (M)</td><td colspan="1" rowspan="1">SMO removes the cell(s) configuration from O-DU#1. This results inremoval of the associated carrier resources from Shared O-RU.See NOTE 5.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.3 (M)</td><td colspan="1" rowspan="1">O-DU#1 may send the RPCs to the O-RU via fronthaul M-plane todeactivate and remove the U-plane configurations related to cell(s)mentioned in Step 9.1.See NOTE 6.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.4 (M)</td><td colspan="1" rowspan="1">O-DU#1 informs O-CU about the cell(s) removal using associatedmessages via F1 interface.See NOTE 7.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.5 (M)</td><td colspan="1" rowspan="1">The SMO configures the cells (including NRCGI) and correspondingcarrier resources to O-DU#2 via O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>Related use</td></tr><tr><td>Step 10.6 (M)</td><td>O-DU configures the [tr]x-array-carrier(s) in O-RU, corresponding to the carrier resources outlined in step 10.5.</td><td></td></tr><tr><td>Step 10.7 (M)</td><td>SMO provides O-CU with information regarding which cell(s) (NRCGI(s) associated with O-DU#2 need to be activated.</td><td></td></tr><tr><td>Step 10.8 (M)</td><td>O-DU#2 informs O-CU, about the added cell(s) (NRCGI(s) that are ready for activation via F1 interface using the associated messages.</td><td></td></tr><tr><td>Step 10.9 (M)</td><td>O-CU requests O-DU#2 to activate the cell(s) (NRCGI(s)), using the associated messages exchanged via the F1 interface.</td><td></td></tr><tr><td>Step 10.10 (M)</td><td>O-DU#2 activated [tr]x-array-carriers related to cells (NRCGI) requested by O-CU in step 10.9.</td><td></td></tr><tr><td>Step 10.11 (M)</td><td>O-DU#2 activates the cell(s) that were specified by O-CU in step 10.9. O-DU#2 informs O-CU about the cell(s) that are activated using</td><td></td></tr><tr><td>Step 10.12 (M)</td><td>associated messages via F1 interface. See NOTE 8, NOTE 9 and NOTE 10.</td><td></td></tr><tr><td>Ends when</td><td>This use case ends when roles are changed as per SMO's request (or when their process ends with non-recoverable error).</td><td></td></tr><tr><td rowspan="6">Exceptions</td><td>There are several exceptions that may occur during this process. These include:</td><td rowspan="6"></td></tr><tr><td colspan="2">1. Shared O-RU fails during a switch over. 2. If the standby O-DU #2 also becomes unavailable when it is due to</td></tr><tr><td colspan="2">become active.</td></tr><tr><td colspan="2">3. If same event messaging for the flow is lost.</td></tr><tr><td colspan="2">4. If configuration provided to O-DU or O-CU is improper.</td></tr><tr><td colspan="2">5. If the connectivity or functionality of the management system (SMO) becomes unavailable. Successful post condition – O-DU's roles are changed successfully,</td></tr><tr><td rowspan="2">Post Conditions</td><td>services for end users are available. Failure post condition- O-RU does not have active O-DU connected</td><td></td></tr><tr><td>and services for end user are not available. NOTE 1: Shared O-RU becomes operational with O-DU#1 with cell on air and ready to serve UEs.</td><td colspan="2"></td></tr><tr><td colspan="4">NOTE 2: SMO collects alarms and performance management data from O-DU#1.</td></tr><tr><td colspan="4">NOTE 3: When analysing the active alarms and performance counters, SMO may detect a partial failure of O-DU#1. Scenario continues in case of partial failure is detected.</td></tr><tr><td colspan="4">NOTE 4: The meanings of administrate and operational states are defined in ITU-T X.731 [18].</td></tr><tr><td colspan="4">NOTE 5:Ifthe above role change is due to M-plane failure between O-DU#1 and Shared O-RU, then O-DU#1 would</td></tr><tr><td colspan="4">not have access to O-RU and hence cannot remove carriers.</td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td colspan="4">NOTE 6: f M-plane failure occurs between O-DU#1 and Shared O-RU, then the O-DU#1 would not have access to O- RU and cannot deactivate and remove carriers.</td></tr><tr><td colspan="4">NOTE 7: If F1 interface failure occurs between O-CU and O-DU#1, then the O-DU#1 would not have access to O-CU and hence it cannot request for cell(s) removal.</td></tr><tr><td colspan="4">NOTE 8: Shared O-RU operations are restored with O-DU#2 and begins providing services to the users, i.e., CUS- plane is up and running.</td></tr><tr><td colspan="4">NOTE 9: SMO collects the alarms and performance management data from O-DU#1 (f it i only partil failure and not lost communication, list of available PM counters reported by O-DU#1 wil probably be reduced (when compared to</td></tr><tr><td colspan="4">the list available from fully operational O-DU)) and O-DU#2. NOTE 10: The transition of the active role from O-DU#2 back to O-DU#1 involves the same steps as the initial transition from the O-DU#1 to O-DU#2, with the exception of which O-DU is to be activated. This activity is initiated based on a</td></tr></table>

![](images/2701aecb38c9a8b0bc63663f9d28eb49c44607c13abff412b3ec67f78d4bd460.jpg)

> **Image Summary:** {"entities": ["O-RU", "O-DU", "Near-RT RIC", "O-CU", "O-RAN Controller", "gNB", "O-DU (and O-RU)", "O-RAN architecture", "Control Plane", "User Plane"], "relationships": ["O-RU → O-DU: Fronthaul Interface, bidirectional", "O-DU → O-CU: F1_C Interface, bidirectional", "O-DU → O-CU: F1_U Interface, bidirectional", "O-CU → Near-RT RIC: E2 Interface, bidirectional", "Near-RT RIC → O-RU: A1 Interface, bidirectional", "O-RU → O-RAN Controller: A1 Interface, bidirectional", "O-CU → O-RAN Controller: A1 Interface, bidirectional", "gNB → O-RAN architecture: composition", "O-RAN architecture → O-DU (and O-RU): component", "O-CU → Control Plane: contains", "O-CU → User Plane: contains"], "hierarchy": ["gNB = O-RU + O-DU + O-CU", "O-CU = Control Plane + User Plane"], "flows": [], "notes": ["The diagram illustrates an O-RAN architecture", "O-RU and O-DU are components of the gNB", "The Control Plane and User Plane reside within the O-CU", "Interfaces A1, E2, and F1 are used for communication between components"]}
  
Figure 4.20.3.12.1-1: Advanced resiliency sub-use case implementation flow for 1 active $^ { + }$ 1 standby O-DUs with various resiliency situations

# 4.20.3.13 Load-balancing sub-use cases of a Shared O-RU

The load-balancing sub-use cases describes the flow of how actors involved execute a policy to load-balance the resources of the O-DUs and Shared O-RU coordinated through a policy enforcer (actor).

# 4.20.3.14 Coordinated reset of a Shared O-RU sub-use cases for Multi-MNO

The coordinated reset of a Shared O-RU sub-use cases describes the flow of how actors coordinate to reset Shared O-RU.   
The context of the coordinated reset of a Shared O-RU sub-use cases is captured in table 4.20.3.14-1.

# Table 4.20.3.14-1: Coordinated reset of a Shared O-RU sub-use cases

<table><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Coordinated reset of a Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Host SMO – The connected host SMO to the host O-DU.Partner SMO – The partner operator SMO. It connects to the SROs.Host O-DU – Host O-DU connected to the Shared O-RU.Operator O-DU – The SRO O-DU connected to the Shared O-RU.Shared O-RU – The target Shared O-RU that will be reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">There are four basic variations of a coordinated reset of a Shared O-RU. These aredescribed in the following steps and diagrams.(1) Coordinated reset of a Shared O-RU initiated by host personnel(2) Coordinated reset of a Shared O-RU initiated by SRO personnel(3) Coordinated reset of a Shared O-RU autonomously initiated by host O-DU(4) Coordinated reset of a Shared O-RU autonomously initiated by SRO O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Coordinated reset of Shared O-RU initiated by host personnel</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Reset request from operatorThe request for the coordinated reset of a Shared O-RU is initiated from the hostoperator and is received by the host operator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Host SMO informs partner SMOsThe host operator SMO informs associated SMOs that the coordinated reset of aShared O-RU has been initiated. Associated SMOs are other SMOs which areconnected to O-DUs that are connected to the affected Shared O-RU. See NOTE 1,NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3.1 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to host O-DU (hierarchal mode)The request for the coordinated reset of the target Shared O-RU is sent from thehost operator SMO to the host O-DU over the O1 interface. See NOTE 3.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3.2 (ALT)</td><td colspan="1" rowspan="1">Reset request from host O-DU to Shared O-RU (hierarchical mode)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"> In hierarchical mode, the coordinated reset request of the target Shared O-RU issent from the host O-DU to the target Shared O-RU through the fronthaul as anRPC request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3.3 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to Shared O-RU (hybrid mode)In hybrid mode, the coordinated reset request of the target Shared O-RU is sentfrom the host SMO to target Shared O-RU as an RPC request via the M-plane. SeeNOTE 4.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies the host O-DUThe affected Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode). See NOTE 5, NOTE 6, NOTE 7.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Host O-DU notifies the SMOThe host O-DU informs the host SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifes connected host O-DUThe target Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode) with a reset response. This is an RPC reply-acknowledgement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Host O-DU notifies the SMOThe host O-DU informs the host operator SMO that the Shared O-RU has executedthe reset with a "Shared O-RU Reset Executed"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">Shared O-RU reset &amp; startupThe Shared O-RU resets; and then initiates its start-up sequence.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Coordinated reset of Shared O-RU initiated by SRO personnel</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Reset procedure initiatedThe partner operator has identified a need to reset the target Shared O-RU and initiates a reset procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Identify hostThe host for the target Shared O-RU is identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Reset coordinationCoordination between the operators can occur, so that the partner operator canindicate to the host the need for a reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Reset request from operator</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The reset request from the partner operator is sent to the partner SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Identify hostThe partner SMO identifies the proper host SMO for the target Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Reset request (coordination)The partner shared operator SMO sends a request to the host SMO to initiate acoordinate reset of the target Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Reset response (coordination)The host SMO responds to the partner shared operator SMO regarding the initiationof a coordinate reset of the target Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.1 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to host O-DU (hierarchal mode)The request for the coordinated reset of the target Shared O-RU is sent from thehost operator SMO to the host O-DU over the O1 interface. See NOTE 8.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.2 (ALT)</td><td colspan="1" rowspan="1">Reset request from host O-DU to SHARED O-RU (hierarchical mode) In hierarchical mode, the coordinated reset request of the target Shared O-RU issent from the host O-DU to the target Shared O-RU through the fronthaul as anRPC request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.3 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to Shared O-RU (hybrid mode)In hybrid mode, the coordinated reset request of the target Shared O-RU is sentfrom the host SMO to target Shared O-RU as an RPC request via the M-plane. SeeNOTE 9.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies the host O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The affected Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode). See NOTE 10, NOTE 11, NOTE 12.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">Host O-DU notifies the SMOThe host O-DU informs the host SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected host O-DUThe target Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode) with a reset response. This is an RPC reply-acknowledgement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">O-DU notifes the SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">A L L I A N C E</td></tr><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The host O-DU informs the host operator SMO that the Shared O-RU has executedthe reset with a "Shared O-RU Reset Executed"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">Shared O-RU reset &amp; startupThe Shared O-RU resets; and then initiates its start-up sequence.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="2" rowspan="1">Coordinated reset of Shared O-RU autonomously initiated by host O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Reset request from host O-DU to Shared O-RUThe reset request goes from the host O-DU to Shared O-RU through the fronthaulas an RPC request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Reset notification from host O-DU to SMOThe notification of a coordinated reset for a Shared O-RU goes from host O-DU tothe host operator SMO over the O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Host SMO informs partner SMOs (coordination)The host operator SMO informs associated SMOs that the coordinated reset of aShared O-RU has been initiated. Associated SMOs are other SMOs which areconnected to O-DUs that are connected to the affected Shared O-RU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Partner SMOs respond to host SMO (coordination)The associated SMO responds to the host operator SMO regarding the Shared O-RU reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected O-DUsThe affected Shared O-RU notifies connected O-DUs including the host O-DU, SOHand other connected O-DUs, SROs. This is a notification message originating fromthe Shared O-RU and sent to all connected O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Host O-DU notifes host SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use CaseStage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The host O-DU notifies the host SMO with a Shared O-RU Reset Initiated messagethat is triggered from the reset requested by host notification sent from the SharedO-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected O-DUsThe affected Shared O-RU notifies connected O-DUs including the host O-DU, SOHand other connected O-DUs, SROs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">O-DU (SRO) notifies the operator SMOThe O-DU (SRO) informs its associated operator SMO that the Shared O-RU hasinitiated a reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected O-DUsThe affected Shared O-RU notifies connected O-DUs including the host O-DU, SOHand other connected O-DUs, SROs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">O-DU (SRO) notifes the operator SMOThe O-DU (SRO) informs its associated operator SMO that the Shared O-RU hasinitiated a reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected host O-DUThe affected Shared O-RU notifies the host O-DUs with a Reset Response. This isan RPC reply-acknowledgement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">Host O-DU notifies the host SMO with reset executedThe host O-DU informs the host operator SMO that the Shared O-RU has executedthe reset with a "Shared O-RU Reset Executed"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">Shared O-RU reset &amp; startupThe Shared O-RU resets; and then initiates its start-up sequence.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Coordinated reset of Shared O-RU autonomously initiated by SRO O-DU</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Reset request</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The SRO O-DU has determined that the target Shared O-RU needs to be reset. TheSRO O-DU sends a reset request to its associated SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Reset request (coordination)The partner shared operator SMO sends a request to the host SMO to initiate acoordinate reset of the target Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Reset response (coordination)The host SMO responds to the partner shared operator SMO regarding the initiationof a coordinate reset of the target Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4.1 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to host O-DU (hierarchal mode)The request for the coordinated reset of the target Shared O-RU is sent from thehost operator SMO to the host O-DU over the O1 interface. See NOTE 13.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4.2 (ALT)</td><td colspan="1" rowspan="1">Reset request from host O-DU to Shared O-RU (hierarchical mode)In hierarchical mode, the coordinated reset request of the target Shared O-RU issent from the host O-DU to the target Shared O-RU through the fronthaul as anRPC request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4.3 (ALT)</td><td colspan="1" rowspan="1">Reset request from host SMO to Shared O-RU (hybrid mode)In hybrid mode, the coordinated reset request of the target Shared O-RU is sentfrom the host SMO to target Shared O-RU as an RPC request via the M-plane. SeeNOTE 14.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies the host O-DUThe affected Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode). See NOTE 15, NOTE 16, NOTE 17.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Host O-DU notifies the SMOThe host O-DU informs the host SMO with a "Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a “Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies other connected O-DUsThe target Shared O-RU notifies other connected O-DUs as SROs. This is anotification message originating from the Shared O-RU with no specific ordering.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">O-DU notifies associated SMOThe O-DU (SRO) informs its associated SMO with a "Shared O-RU reset initiated"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">Shared O-RU notifies connected host O-DUThe target Shared O-RU notifies the host O-DU (hierarchical mode) or host SMO(hybrid mode) with a reset response. This is an RPC reply-acknowledgement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">O-DU notifies the SMOThe host O-DU informs the host operator SMO that the Shared O-RU has executedthe reset with a "Shared O-RU Reset Executed"notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">Shared O-RU reset &amp; startupThe Shared O-RU resets; and then initiates its start-up sequence.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The target Shared O-RU has been reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PostConditions</td><td colspan="1" rowspan="1">Success: The target Shared O-RU has been reset.Failure: The target Shared O-RU fails to be reset.</td><td colspan="1" rowspan="1"></td></tr></table>

NOTE 1: There are other use cases exploring operator to operator coordination and in 3GPP specifications as well. These are the exposure of management services (SMO Services).

NOTE 2: There might be some coordination between SMOs such that the host SMO would not initiate a coordinated reset if the partner SMOs objected, this would be part of the SMO decomposition work. Thus, there might be other transactions happening between the SMOs before step 4.

NOTE 3: Once the coordinate reset request is issued from the host SMO, the operation will be executed and can no longer be rejected by the system. This implies that any OSS/SMO coordination has finalized before reaching this step.

NOTE 4: Step 3.3 is specifically for hybrid mode configuration where the SMO could be a host and thus initiate a coordinated reset of a Shared O-RU as an RPC request.

NOTE 5: These set of notification messages originating from the Shared O-RU and are sent to all connected O-DUs.

NOTE 6: The notification messages sent to all connected O-DUs in steps 4, 6, and 8 happen in an unspecified order.

NOTE 7: In both hybrid and hierarchal mode, the Shared O-RU will inform all the connected O-DUs of a reset requested by host notification.

NOTE 8: Once the coordinate reset request is issued from the host SMO, the operation will be executed and can no longer be rejected by the system. This implies that any OSS/SMO coordination has finalized before reaching this step.

NOTE 9: Step 8.3 is specifically for hybrid mode configuration where the SMO could be a host and thus initiate a coordinated reset of a Shared O-RU as an RPC request.

NOTE 10: These set of notification messages originating from the Shared O-RU and are sent to all connected O-DUs.

NOTE 11: The notification messages sent to all connected O-DUs in steps 9, 11, and 13 happen in an unspecified order.

NOTE 12: In both hybrid and hierarchal mode, the Shared O-RU will inform all the connected O-DUs of a reset requested by host notification.

NOTE 13: Once the coordinate reset request is issued from the host SMO, the operation will be executed and can no longer be rejected by the system. This implies that any OSS/SMO coordination has finalized before reaching this step.

NOTE 14: Step 4.3 is specifically for hybrid mode configuration where the SMO could be a host and thus initiate a coordinated reset of a Shared O-RU as an RPC request.

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td colspan="3">NOTE 15: These set of notification messages originating from the Shared O-RU and are sent to all connected O-DUs.</td></tr><tr><td colspan="3">NOTE 16: The notifiction messages sent to llconnected O-DUs in steps 5, 7, and 9 happen in an unspecified order.</td></tr><tr><td colspan="3">NOTE 17: In both hybrid and hierarchal mode, the Shared O-RU wil inform al the connected O-DUs of a reset requested by host notification.</td></tr></table>

The flow diagram of the coordinated reset sub-use case 1 (personnel triggered) is given in figure 4.20.3.14-1.

![](images/05f7c09c7783a945efbf85edf1a5903885d135be96acfeb358d75bb1b7003571.jpg)

> **Image Summary:** {"entities": ["O-RU", "O-DU", "CU-CP", "CU-UP", "gNB", "NR", "O-RAN Alliance", "gNB Architecture", "gNB Interfaces", "CU-CP Interfaces", "CU-UP Interfaces", "O-RU Interfaces", "Service Based Architecture", "gNB Cloud Native Architecture", "CU", "DU", "RU", "Functional Split", "Option 7-2", "gNB Architecture Overview", "CU-CP and CU-UP Interfaces", "CU-CP and CU-UP interfaces", "CU-CP and CU-UP Interfaces - Overview", "gNB Overall Architecture", "3GPP TS 38.300"], "relationships": ["gNB Architecture → gNB Overall Architecture: overview, unidirectional", "gNB Architecture → CU: cloud native architecture, unidirectional", "gNB Architecture → DU: cloud native architecture, unidirectional", "gNB Architecture → RU: cloud native architecture, unidirectional", "CU → CU-CP: part of, unidirectional", "CU → CU-UP: part of, unidirectional", "CU-CP → CU-CP Interfaces: defines, unidirectional", "CU-UP → CU-UP Interfaces: defines, unidirectional", "O-RU → O-RU Interfaces: defines, unidirectional", "gNB Interfaces → CU-CP and CU-UP Interfaces: shows, unidirectional", "gNB Interfaces → O-RU Interfaces: shows, unidirectional", "CU-CP and CU-UP Interfaces → CU-CP and CU-UP Interfaces - Overview: shows, unidirectional", "O-RU Interfaces → O-RU: defines, unidirectional", "gNB Cloud Native Architecture → CU: part of, unidirectional", "gNB Cloud Native Architecture → DU: part of, unidirectional", "gNB Cloud Native Architecture → RU: part of, unidirectional", "Functional Split → Option 7-2: example, unidirectional"], "hierarchy": ["gNB Architecture = CU + DU + RU", "CU = CU-CP + CU-UP"], "flows": [], "notes": ["Image depicts gNB architecture overview and interfaces according to 3GPP TS 38.300.", "Image is from O-RAN Alliance.", "Functional Split: Option 7-2 is shown as an example."]}
  
Figure 4.20.3.14-1: Coordinated reset sub-use case 1 (personnel triggered)

The flow diagram of the coordinated reset sub-use case 2 (autonomous) is given in figure 4.20.3.14-2.

![](images/6f18c2d38b82b9ac601f6d850bb0f70d1c624640b6b99d6458321fe122a25687.jpg)

> **Image Summary:** {"entities": ["O-RU", "O-DU", "CU-CP", "CU-UP", "Near-RT RIC", "Far-Edge RIC", "Near-RT RIC API", "Far-Edge RIC API", "O-CU", "gNB", "O-RAN Fronthaul Interface", "E2 Interface", "A1 Interface", "O-RAN Use Case", "Policy"], "relationships": ["O-RU → O-DU: O-RAN Fronthaul Interface", "O-DU → CU-CP: E2 Interface", "O-DU → CU-UP: E2 Interface", "Near-RT RIC → O-DU: A1 Interface", "Far-Edge RIC → O-DU: A1 Interface", "Near-RT RIC API → Near-RT RIC: service API", "Far-Edge RIC API → Far-Edge RIC: service API", "O-CU → gNB: service", "O-RAN Use Case → O-CU: service"], "hierarchy": ["gNB = O-RU + O-DU + CU-CP + CU-UP", "O-CU = CU-CP + CU-UP"], "flows": [], "notes": ["Figure 3.1-1: Overall O-RAN Architecture and RIC Interaction", "Note: The gNB includes the O-RU, O-DU and CU. The CU can be split into CU-CP and CU-UP. The RIC interfaces are used for O-RAN Use Case and Policy interactions.","O-RAN Architecture and RIC Interaction"]}
  
Figure 4.20.3.14-2: Coordinated reset sub-use case 2 (autonomous)

# 4.20.3.15 Management of Shared O-RU during O-DU software update sub-use case for Shared O-RU for Single & Multi-MNO

This sub-use case describes the Shared O-RU management scenarios associated with various stages in the O-DU software update such as planning, deployment, and monitoring. The detailed steps for each of these stages are described in the subsequent clauses.

# 4.20.3.15.1 Shared O-RU management during O-DU SW change management planning

The context of the Shared O-RU management during O-DU SW change management planning is captured in table 4.20.3.15.1-1.

Table 4.20.3.15.1-1: Shared O-RU management during O-DU SW change management planning   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Management scenarios associated with Shared O-RU during the O-DUSW change management planning.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">●   SMO: Maintains up-to-date information about the deployed RANnodes including inventory, FM and PM data that help to identifyappropriate Shared O-RU resources that can be allocated forvalidating the O-DU SW update.O-DU SW planner: Personnel who prepares deployment strategy ofO-DU SW and associated plan based on the Shared O-RUresources that need to be allocated for validation.O-DU SW change management rApp: The rApp that supports SMOand Non-RT RIC in managing the O-DU SW update based on theplan prepared by the planner.Non-RT RIC: Facilitates communication between rApps and SMOservices over R1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">SW updated O-DU shares the O-RU resources with an existing O-DU.SW updated O-DU and existing O-DUs address different set ofcomponent carriers and does not have common componentcarriers among them.•   SW updated O-DU is considered for single operator Shared O-RUscenario.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">O-DU SW planner identifies changes in O-DU software that need to bevalidated and rolled out on the RAN node deployment with limitedservice disruption.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">O-DU SW planner received the O-DU software changespecification (for example a document detailing the changes in theO-DU software with information about impact of change andpriority).O-DU SW planner collected the information about the RAN nodesfrom the SMO Topology Exposure &amp; InVentory Management(TE&amp;lV) service.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3">D-RAN</td></tr><tr><td>NC E Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td></td><td colspan="2">● O-DU SW planner collected the performance indicators and health/fault details of the RAN nodes from the SMO. O-DU SW planner identified the KPIs, PMJobs and scaling parameters of O-DU and Shared O-RU that need to be modified or redefined. This is to ensure that any temporary degradation during the software update does not result in false alarms or unintended</td></tr><tr><td></td><td>actions. O-DU SW planner designs the change management plan for SW update based on the information collected from SMO services. The plan can include but not limited to a) The version of O-DU software to be used for SW update.</td><td></td></tr><tr><td>Step 1 (0)</td><td>b) The policy to select the target O-DU (e.g., least loaded cell, particular S-NSSAl, random or specific O-DU ID). c) Evacuation policies of currently occupied component carriers associated with the Shared O-RU which need to be reallocated based on the O-DU SW update. The traffi-distribution or component carrier allocation policy d) between target O-DU and existing O-DU. e) Performance and fault indicators with threshold values, monitoring schedule for the updated O-DU. f) Mitigation policy in case of a SW update failure or any disruptions. The availability of plan can be notified to the subscribed SMO services</td><td></td></tr><tr><td>Step 2 (M)</td><td>and rApps (for example O-DU SW change management rApp). See NOTE. The O-DU SW planner initiates SW update of O-DU through the O-DU SW change management rApp with reference to the change</td><td></td></tr><tr><td>Step 3 (0)</td><td>management plan prepared and made available to the O-Du SW change management rApp. O-DU SW change management rApp collects the change management plan for O-DU software update.</td><td></td></tr><tr><td>Step 4 (0)</td><td>O-DU SW change management rApp validates the change management plan.</td><td></td></tr><tr><td>Step 5 (ALT)</td><td colspan="2">Upon successful validation, the O-DU SW change management rApp prepares the provisioning configurations for the Shared O-RU and O- DU (target and existing), along with the execution steps for the software update, for the designated RAN nodes.</td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 7 (0)</td><td colspan="1" rowspan="1">O-DU SW planner verifies and sends approval to the O-DU SW changemanagement rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (0)</td><td colspan="1" rowspan="1">Prepares detailed execution plan which can be notified to thesubscribed SMO services and rApps.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (ALT)</td><td colspan="1" rowspan="1">If the validation of the change management plan failed, a notification issent to the O-DU SW planner with the reason for failure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The change management plan for SW update is ready for execution. Theexecution can be auto triggered, or it can be manually initiated by the O-DU SW planner.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE: It is optional to store the change management plan for SW update in SMO TE&amp;iIV. The changemanagement plan can be stored in alternate SMO functions registered with and authorized by SMO datamanagement and exposure functions based on the implementation choice.</td></tr></table>

The O-DU SW update change management planning sequence diagram is given in figure 4.20.3.15.1-1.

![](images/0e7e569c322cd9590825fb0ee295f53be9a86c2f0bb47cc987cf26947d6c55e8.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.15.1-1: O-DU SW update change management planning sequence diagram

4.20.3.15.2 Shared O-RU management during O-DU SW update

The context of the Shared O-RU management during O-DU SW update is captured in table 4.20.3.15.2-1.

# Table 4.20.3.15.2-1: Shared O-RU management during O-DU SW update

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Shared O-RU management during O-DU SW update.</td><td colspan="1" rowspan="1"></td></tr><tr><td rowspan="4">Actors and Roles</td><td>SMO: Facilitates the execution of O-DU SW update and associated Shared O-RU provisioning by enabling interaction across SMO services, rApps and RAN nodes – These services include but not limited to – TE&amp;IV, OAM functions, O2 related functions.</td><td></td></tr><tr><td>O-RU sharing co-ordinator retrieves change management plan for O-DU SW update and decides on partitioning of carriers between O-DUs.</td><td colspan="1"></td></tr><tr><td>Sharing co-ordinator uses Shared O-RU orchestration rApp to partition resource configuration of a Shared O-RU between O-DUs. O-DU SW change management rApp: The rApp that supports SMO</td><td colspan="1"></td></tr><tr><td>and Non-RT RIC in managing the O-DU SW update based on the plan prepared by the O-DU SW planner. Non-RT RIC: Facilitates communication between rApps and SMO</td><td colspan="1"></td></tr><tr><td rowspan="4">Assumptions</td><td>services over R1 interface. O-DU(#n): An active O-DU in the RAN being managed by the SMO.</td><td></td></tr><tr><td>O-DU (updated): O-DU updated with new SW based on the change management plan.</td><td colspan="1"></td></tr><tr><td>SW updated O-DU shares the O-RU resources with an existing O- DU.</td><td colspan="1"></td></tr><tr><td>SW updated O-DU and existing O-DUs address different set of component carriers and does not have common component carriers among them.</td><td colspan="1"></td></tr><tr><td>Begins when Preconditions</td><td>RU scenario. O-DU SW change management rApp receives confirmation about the O-DU SW update and Shared O-RU provisioning steps.</td><td></td></tr><tr><td></td><td>by the O-DU SW planner and made available to the O-DU SW change management rApp. O-DU SW change management rApp, based on the change management plan identifies software version to be updated and</td><td></td></tr><tr><td>Step 0 (Ref)</td><td>the software version and O-DU identifier. For software update of an existing O-DU, the designated O-DU (updated) is updated using O-RAN.WG6.ORCH-USE-CASES [26], clause 3.2.4 (steps 1 to 4) Initial provisioning of O-DU (updated) as per change management plan- Refer to O-RAN.WG10.OAM-Architecture [27], clause 4.2.1</td><td></td></tr><tr><td>Step 1 (M)</td><td>See NOTE 1.</td><td></td></tr><tr><td>Step 2 (M)</td><td>O-DU SW change management rApp request (via R1 and SMO/Non-RT RIC) Shared O-RU orchestration rApp to facilitate resource sharing</td><td></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">between O-DU (updated) and existing O-DUs based on the changemanagement plan.See NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Shared O-RU orchestration r-App initiates configuration of the SharedO-RU common aspects</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4-6 (M)</td><td colspan="1" rowspan="1">Common aspect provisioning of Shared O-RU as per WG1 Use CasesDetailed Specification, clause 4.20.1.1 which include the include thesecurity, operational, transmission, and connectivity related parameters.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Based on the call home procedure, Shared O-RU establishesmanagement session with O-DU (updated).See NOTE 3.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8-10 (0)</td><td colspan="1" rowspan="1">Notification of configuration update to SMO OAM functions andsubsequently to Shared O-RU orchestration rApp.See NOTE 4.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11-13 (0)</td><td colspan="1" rowspan="1">Carrier aspect provisioning to deactivate and evacuate componentcarriers designated for the O-DU (updated) from the existing O-DU i.e.,O-DU (#1).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14-15 (0)</td><td colspan="1" rowspan="1">Carrier aspect provisioning to activate component carriers designated for the O-DU (updated).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16-18 (0)</td><td colspan="1" rowspan="1">Notification of committed carrier aspect configuration to SMO OAMfunctions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 19-20 (0)</td><td colspan="1" rowspan="1">Notification of configuration aspect to Shared O-RU orchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 21 (0)</td><td colspan="1" rowspan="1">Notification to sharing coordinator to validate the committedconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 22 (0)</td><td colspan="1" rowspan="1">Validation of committed configuration by Shared O-RU orchestrationrApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 23 (0)</td><td colspan="1" rowspan="1">Validation of committed configuration by O-DU SW changemanagement rApp based on the change management plan.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 24 (0)</td><td colspan="1" rowspan="1">O-DU SW change management rApp coordinates with OAM functionsto provision KPls, PM jobs or scaling parameters used for assessing thehealth of the RAN nodes so that any variations anticipated due to O-DUSW update does not lead to false alarms or unintended actions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Committed configuration associated with the Shared O-RU is acceptedby sharing coordinator and validation of the configuration isacknowledged by the O-DU SW change management rApp.SMO TE&amp;iV service is updated with inventory details about the O-DU(updated) and Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Post Conditions</td><td>SW updated O-DU is ready for health &amp; sanity check and is actively handling UE sessions.</td><td></td></tr><tr><td colspan="3">NOTE 1: It is assumed that based on the O-DU (updated) provisioning procedure SMO TE&amp;IV is updated with the inventory information of O-DU (updated) as per change management plan. NOTE 2: Refer to the resource partitioning use case described in WG1 Use Cases Detailed Specification, clause 4.20.3.2. NOTE 3: After O-DU (updated) deployment, before M-plane connection establishment, there is a possibility of race condition depending on when the Shared O-RU attempts call-home and the readiness of O-DU (updated) to process the call-home requests. There are two potential scenarios and associated approaches for addressing this. Scenario 1: O-DU (updated) is ready for establishing M-plane connection when call home signals are In the O-RAN operations yang model (o-ran-operations.yang) there are two parameters that</td></tr><tr><td colspan="3">still being sent by Shared O-RU o govern the call-home connection attempts – re-call-home-no-ssh-timer : A common timer used by the O-RAN equipment to trigger</td></tr><tr><td colspan="3">the repeated call-home procedure to all identified call-home servers to which the O- RAN equipment has not already an established NETCONF connection. max-call-home-attempts : counter to repeat call-home procedures. In case counter is set with value zero O-RU shall not repeat call-home procedure.</td></tr><tr><td colspan="3">In order for the deployed O-DU (updated) to be ready to receive and process call-home requests from the shared O-RU, the above parameters shall be optimized, so that adequate time is allocated for the O-DU (updated) to become operational. Scenario 2: O-DU (updated) becomes ready after a long-time duration and Shared O-RU is not performing call home procedure anymore due to expiration of the timers.</td></tr></table>

![](images/8a268a8ec090fdb3474f0635c071afd20521b2a24a78beb6c64c6e05d0cb2380.jpg)

> **Image Summary:** {"entities": ["NR-DU", "gNB-CU", "NR-CU-CP", "NR-CU-UP", "O-RAN Interface", "NR-DU Interface", "gNB-CU Interface", "NR-CU-CP Interface", "NR-CU-UP Interface", "RIC", "xApp", "O-DU Service(s)", "xApp Configuration", "CU-CP Function", "CU-UP Function", "O-DU Service Exposure"], "relationships": ["NR-DU → gNB-CU: NR-CU Interface, Fronthaul, bidirectional", "gNB-CU → NR-CU-CP: NR-CU-CP Interface, bidirectional", "gNB-CU → NR-CU-UP: NR-CU-UP Interface, bidirectional", "RIC → NR-CU-CP: O-RAN Interface, Management/Orchestration, bidirectional", "RIC → NR-CU-UP: O-RAN Interface, Management/Orchestration, bidirectional", "NR-DU → xApp: O-DU Service Exposure, bidirectional", "xApp → NR-DU: O-DU Service Exposure, bidirectional", "xApp → NR-CU-CP: xApp Configuration, bidirectional", "xApp → NR-CU-UP: xApp Configuration, bidirectional"], "hierarchy": ["gNB-CU = NR-CU-CP + NR-CU-UP", "NR-CU-CP includes CU-CP Function", "NR-CU-UP includes CU-UP Function"], "flows": [], "notes": ["The diagram title is 'O-RAN Architecture - DU Service Exposure'"]}
  
Figure 4.20.3.15.2-1: O-DU SW update sequence diagram

4.20.3.15.3 Shared O-RU management during O-DU SW update monitoring and mitigation

The context of the Shared O-RU management during O-DU SW update monitoring and mitigation is captured in table 4.20.3.15.3-1.

Table 4.20.3.15.3-1: Shared O-RU management during O-DU SW update monitoring and mitigation   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Shared O-RU management during O-DU SW update monitoring andmitigation.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>Related use</td></tr><tr><td rowspan="8">Actors and Roles</td><td>SMO: Facilitates the monitoring, and mitigation of O-DU SW update and associated Shared O-RU provisioning by enabling interaction across SMO services, rApps and RAN nodes – These services include but not limited to – TE&amp;IV, OAM functions, O2 related</td><td></td></tr><tr><td>functions. O-DU SW planner: Personnel who prepares O-DU SW change</td><td colspan="1"></td></tr><tr><td>management strategy and associated plan based on the identified change in the O-DU software. O-DU SW change management rApp: The rApp that supports SMO and Non-RT RIC in managing the O-DU SW update and associated</td><td colspan="1"></td></tr><tr><td>mitigation actions.</td><td colspan="1">Shared O-RU provisioning based on the plan prepared by the O- DU SW planner and subsequent health monitoring to decide on</td></tr><tr><td>Shared O-RU orchestration rApp is used to rebalance the Shared O-RU resources based on the health monitoring and mitigation action selection by the O-DU SW change management rApp.</td><td colspan="1"></td></tr><tr><td>services over R1 interface.</td><td colspan="1">Non-RT RIC: Facilitates communication between rApps and SMO</td></tr><tr><td></td><td colspan="1">O-DU(#n): An active O-DU in the RAN being managed by the SMO.</td></tr><tr><td>management procedure.</td><td colspan="1">O-DU (updated): A new O-DU deployed through SW change</td></tr><tr><td rowspan="4">Assumptions</td><td>Software updated O-DU shares the O-RU resources with an existing O-DU.</td><td></td></tr><tr><td>of component carriers and does not have common component carriers among them.</td><td colspan="1">Software updated O-DU and existing O-DUs address different set</td></tr><tr><td>cell IDs.</td><td colspan="1">Software updated O-DU and existing O-DUs do not have common</td></tr><tr><td>O-RU scenario.</td><td colspan="1">Software update of O-DU is considered for single operator Shared</td></tr><tr><td rowspan="4">Begins when</td><td>O-DU SW planner subscribes to the health monitoring events for the updated RAN nodes, based on access granted by SMO external</td><td></td></tr><tr><td>exposure service OR</td><td colspan="1"></td></tr><tr><td>As per the predefined plan O-DU SW change management rApp initiates health check of the SW updated O-DU</td><td colspan="1"></td></tr><tr><td>Successfully completed the SW update of target O-DU •</td><td colspan="1"></td></tr><tr><td rowspan="4">Pre-conditions</td><td></td><td>Planned Shared O-RU resources allocated to O-DU (updated) and</td></tr><tr><td>activated</td><td colspan="1"></td></tr><tr><td>O-DU (updated) sharing O-RU resources with an existing O-DU</td><td colspan="1"></td></tr><tr><td>O-DU (updated), existing O-DUs, Shared O-RU are ready for monitoring of KPls and actively handling the UE sessions</td><td colspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">O-DU SW planner subscribes to change management events from O-DU SW change management rApp via SMO/Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">O-DU SW change management rApp subscribes to PM/FM data fromO-DU (updated) and existing O-DU, i.e O-DU (#1) through R1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Non-RT RIC forwards the subscription request to OAM function.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">OAM function subscribes to the FM/PM data updates for O-DU(updated) and existing O-DU, i.e O-DU (#1) via O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">O-DU (updated) subscribes to FM/PM data updates from Shared O-RUbased on the O-DU_ID of O-DU (updated) as the filter criteria.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Notification of FM/PM data from Shared O-RU to O-DU (updated) overOFH.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Notification of FM/PM data from O-DU (updated) to OAM functions over01.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">OAM function forwards notification of FM/PM data received from O-DU(updated) to Non-RT RIC through SMO internal interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Non-RT RIC notifies O-DU SW change management rApp aboutFM/PM data received from O-DU (updated).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">O-DU SW change management rApp evaluates FM/PM data againstthe change management plan.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 ()</td><td colspan="1" rowspan="1">If the health and sanity of the O-DU (updated) and Shared O-RU are notas per plan, O-DU SW change management rApp analyses mitigationaction based on evaluation of the FM/PM data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (0)</td><td colspan="1" rowspan="1">If the health and sanity of the O-DU (updated) is not as per plan O-DUSW change management rApp sends change management reportconsisting of sanity, health details and mitigation action(s) to O-DU SWplanner.See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (0)</td><td colspan="1" rowspan="1">O-DU SW planner verifies the mitigation action and sends approval ifaction is within the scope of the plan.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (0)</td><td colspan="1" rowspan="1">If mitigation involves provisioning of Shared O-RU, O-DU SW changemanagement rApp recommends to Shared O-RU orchestration rApp re-provisioning of O-RU resources based on recommended action.See NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (O)</td><td colspan="1" rowspan="1">Shared O-RU orchestration rApp recommends re-configuration to OAMfunctions over R1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (0)</td><td colspan="1" rowspan="1">Non-RT RiC forwards configuration request to OAM functions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (0)</td><td colspan="1" rowspan="1">OAM functions initiates configuration of O-DU (updated) and partitionedcarrier information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (0)</td><td colspan="1" rowspan="1">O-DU (updated) initiates reconfiguration of partitioned carrier information on Shared O-RU. This can include required evacuationprocedures if applicable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 19 (0)</td><td colspan="1" rowspan="1">OAM functions initiates configuration of O-DU (#n) and partitionedcarrier information on the O-RU shared with O-DU (updated).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 20 (0)</td><td colspan="1" rowspan="1">O-DU (#n) initiates reconfiguration of partitioned carrier information onShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 21 (0)</td><td colspan="1" rowspan="1">O-DU (#n) sends notification about configuration update to OAMfunctions over O1 interface</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 22 (0)</td><td colspan="1" rowspan="1">O-DU (updated) sends notification about configuration update to OAMfunctions over O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 23 (0)</td><td colspan="1" rowspan="1">O-DU SW change management rApp sends revised report to O-DU SWplanner.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">to O-DU SW planner validates the change management report andcertifies the O-DU SW update.SMO TE&amp;lIV service is updated with inventory details about the O-DU(updated) and Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">NA</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">SW updated O-DU is functioning as per the change management plan.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: Sanity check and health check are assumed to be implementation specific and depends on the pre-defined change management plan for O-DU SW update. In general, the sanity check assesses whether the SWupdate satisfies the designated performance and connectivity objectives, while also ensuring compliance withthe policies established in accordance with the plan. On the other hand, the health check examines theresponsiveness and overall condition of the updated O-DU.NOTE 2: The mitigation action depends on the change management plan and specific implementation strategy.This can include but not limited to readjustment of component cariers in Shared O-RU between O-DU(updated) and other O-DUs.</td></tr></table>

The O-DU SW update monitoring and mitigation sequence diagram is given in figure 4.20.3.15.3-1.

![](images/7eb6df158c8cac531f24177df51701753fdc1fe0b3de4058d8682b53121e73c5.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.15.3-1: O-DU SW update monitoring and mitigation sequence diagram

# .20.3.16 Resource partitioning use case of Shared O-RU for Multi-MNO configuration

The following describes the solution for the resource partitioning sub-use case for a Shared O-RU in a Multi-MNO configuration.

The context of the resource partitioning use case of Shared O-RU is captured in table 4.20.3.16-1.

Table 4.20.3.16-1: Resource partitioning use case of Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">rApp has details on how a Shared O-RU's resource are to be partitioned.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Owning operator Service Management &amp; Orchestration (SMO) providesinventory details of Shared O-RU and O-DUs.Owning operator sharing coordinator recovers inventory and decides onpartitioning of carriers between O-DUs.Owning operator sharing coordinator uses resource partitioning rApp topartition resource configuration of a Shared O-RU between O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated. Inventory management systems identify Shared O-RU carrier capabilities andavailable O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Owning operator sharing coordinator decides to share an O-RU betweenmultiple O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Inventory system is up to date.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Owning operator sharing coordinator recovers O-RU and O-DU inventory anddecides on resource partitioning.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Owning operator sharing coordinator resource partitioning rApp to partitionshared O-RU between multiple O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">rApp signals O-DU identity(ies) to owning operator configuration managementsystem.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Owning operator configuration management system configures transportsystems with call home identity(ies) for O-DU(s).</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.2.5</td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Participating operator sharing coordinator recovers O-RU and O-DU inventoryand decides on resource partitioning.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Participating operator sharing coordinator resource partitioning rApp to paritionShared O-RU between multiple O-DUs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">rApp signals O-DU identity(ies) to participating operator configurationmanagement system.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">Participating operator configuration management system configures transportsystems with call home identity(ies) for O-DU(s).</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.2.5</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Owning operator rApp has details on how shared O-RU's resource are to bepartitioned.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the resource partitioning use case for Multi-MNO configuration is given in figure 4.20.3.16-1.

![](images/651f9b89f6256120ba9f70b890cbfaffbbadc90a67a82ebce5c77990f24f3a97.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.16-1: Resource partitioning use case for Multi-MNO

# 4.20.3.17 Start-up use case of Shared O-RU for Multi-MNO configuration

The following describes the solution for the start-up sub-use case for a Shared O-RU for Multi-MNO configuration.

The context of the Shared O-RU start-up use case is captured in table 4.20.3.17-1.

Table 4.20.3.17-1: Shared O-RU start-up use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The Shared O-RU is operating with the necessary software version andhas established network connectivity with the O-DU(s) and, for hybriddeployments, the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU calls home and establishes network management session.Owning operator SMO is responsible for software management for theShared O-RU when operating in hybrid management mode.O-DU is responsible for software management for the Shared O-RUwhen operating in hierarchical management mode.Participating operator SMO handles communication to its connected O-DU.RAN NF OAM SMO services – provides RAN NF OAM related servicesfor FCAPS and LCM type functions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Shared O-RU powers on.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Preconditions</td><td colspan="1" rowspan="1">Transport systems (DHCP server) has been configured with call homeconfiguration information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Establish synchronization:Each O-DU and Shared O-RU establish synchronisation with a timingsource, for example PTP (IEEE 1588) or Sync-E. See NOTE 1, NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Synchronization state change notification:After the O-RU has a synchronisation source, all subscribed O-DU(s) arenotified through a synchronisation state change notification. We expectthe O-RU to be in the sync state "LOCKED".The synchronisation state change notication goes from Shared O-RU toall subscribed O-DU(s). It is possible that the synchronisation procedure can happen in parall tothe other steps of the start-up sub-use case. Thus, many of the othersteps in this use case can happen as the synchronization procedureoccurs. Even though this is shown as “step 2" this can complete afterother steps.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]Shared O-RU establishes a network management session with owningoperator SMO.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3and/or clause6.9.2</td></tr><tr><td colspan="1" rowspan="1">Step4</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]Shared O-RU calls home and triggers establishment of networkmanagement session with owning operator O-DU#1.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3</td></tr><tr><td colspan="1" rowspan="1">Step 5 (ALT)</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]Shared O-RU establishes network management session withparticipating operator SMO.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 8.4</td></tr><tr><td colspan="1" rowspan="1">Step 6</td><td colspan="1" rowspan="1">[Shared O-RU operated in hierarchical management mode]Shared O-RU calls home and triggers establishment of networkmanagement session with participating operator O-DU#2.</td><td colspan="1" rowspan="1">O-RAN.WG4.MP[28], clause 6.3</td></tr><tr><td colspan="1" rowspan="1">Step7</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]SMO recovers software inventory request from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step8</td><td colspan="1" rowspan="1">[Shared O-RU operated in hybrid management mode]SMO recovers software inventory response from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>Related use</td></tr><tr><td>Step 9 (0)</td><td>[Shared O-RU operated in hybrid management mode and software update required]</td><td>O-RAN.WG4.MP [28], clause 8.5</td></tr><tr><td>Step 10 (0)</td><td>SMO triggers download of new software. [Shared O-RU operated in hybrid management mode and software update required]</td><td>O-RAN.WG4.MP</td></tr><tr><td></td><td>O-RU downloads software files. [Shared O-RU operated in hybrid management mode and software</td><td>[28], clause 8.5</td></tr><tr><td>Step 11 (0)</td><td>update required] SMO triggers the installation of the software.</td><td>O-RAN.WG4.MP [28], clause 8.6</td></tr><tr><td>Step 12 (0)</td><td>[Shared O-RU operated in hybrid management mode and software update required] SMO triggers the activation of the software.</td><td>O-RAN.WG4.MP [28], clause 8.7.2</td></tr><tr><td>Step 13 (0)</td><td>[Shared O-RU operated in hybrid management mode and software update required] SMO brings active software into operation.</td><td>O-RAN.WG4.MP [28], clause 8.7.3</td></tr><tr><td></td><td>A O-RU reset is required to take the activated software into operation.</td><td></td></tr><tr><td>Step 14 (ALT)</td><td>[Shared O-RU operated in hierarchical management mode] Owning operator O-DU#1 recovers software inventory request.</td><td>O-RAN.WG4.MP [28], clause 8.4</td></tr><tr><td>Step 15</td><td>[Shared O-RU operated in hierarchical management mode] Owning operator O-DU#1 recovers software inventory response.</td><td>O-RAN.WG4.MP [28], clause 8.4</td></tr><tr><td>Step 16 (0)</td><td>[Shared O-RU operated in hierarchical management mode and software update required] Owning operator O-DU#1 triggers download of new software.</td><td>O-RAN.WG4.MP [28], clause 8.5</td></tr><tr><td>Step 17 (0)</td><td>[Shared O-RU operated in hierarchical management mode and software update required]</td><td>O-RAN.WG4.MP [28], clause 8.5</td></tr><tr><td></td><td>O-RU downloads software files.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>[Shared O-RU operated in hierarchical management mode and software</td><td></td></tr><tr><td>Step 18 (0)</td><td>update required]</td><td>O-RAN.WG4.MP</td></tr><tr><td></td><td></td><td>[28], clause 8.6</td></tr><tr><td></td><td>Owning operator O-DU#1 triggers the installation of the software.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Step 18 (0)</td><td>[Shared O-RU operated in hierarchical management mode and software</td><td></td></tr><tr><td></td><td>update required]</td><td>O-RAN.WG4.MP</td></tr><tr><td></td><td></td><td>[28], clause 8.7</td></tr><tr><td></td><td>Owning operator O-DU#1 triggers activation of the software.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>[Shared O-RU operated in hierarchical management mode and software</td><td></td></tr><tr><td></td><td></td><td>O-RAN.WG4.MP</td></tr><tr><td>Step 19 (0)</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>Owning operator O-DU#1 brings active software into operation.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>update required]</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td>[28], clause 8.7</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">The Shared O-RU is operating with the necessary software version andhas established network connectivity with the O-DU and, for hybriddeployments, the owning operator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: It is expected the O-RU and all O-DUs connected it would share the same synchronisation sourceotherwise, the O-DUs will drift in timing.NOTE 2: For more details on O-RU sync and O-RU loss of sync, see O-RAN.WG4.MP [28], clause 15.3.3.</td></tr></table>

The flow diagram of the Shared O-RU start-up use case is given in figure 4.20.3.17-1 for Multi-MNO.

![](images/6880f3583bfe6fea2ce65f1f2d9167e5eb9c8538799f88ea62ff35ae8519cbd8.jpg)

> **Image Summary:** {"image": "image_of_oran_architecture.png"}
  
Figure 4.20.3.17-1: Shared O-RU start-up use case for Multi-MNO

# 4.20.3.18 Supervision sub-use case of a Shared O-RU for Multi-MNO configuration

The following describes the solution for the supervision sub-use case for a Shared O-RU for a Multi-MNO configuration.

The context of the supervision use case of a Shared O-RU is captured in table 4.20.3.18-1.

Table 4.20.3.18-1: Supervision sub-use case of a Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The Shared O-RU operates watchdog timers with each of its O-DUs andceases transmitting on a partitioned carrier associated with an O-DU if iswatchdog timer to that O-DU expires.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU operates watchdog timers and deactivates any carriersassociated with an expired watchdog timer.O-DU repeatedly resets the Shared O-RU's supervision timer.SMO forwards any alarms to Shared O-RU rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-DUs are operating fronthaul control and user plane for their respectivepartitioned carriers.SMO has subscribed to receive alarm notifications (hybrid managementmodel).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">An O-DU subscribes to receive supervision notifications.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (Loop)</td><td colspan="1" rowspan="1">O-DU#1 initiates supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (Loop)</td><td colspan="1" rowspan="1">O-RU response from supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">O-DU#1 detects that it has lost communication sessions to the SharedO-RU. It raises a communication alarm to the owning operator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">Cease transmission – Shared O-RU detects supervision failure with O-DU#1 and ceases transmiting on partitioned carrier associated with O-DU of the owning operator RAN network.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">Shared O-RU sends alarm notification to owning operator faultmanagement in SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6(0)</td><td colspan="1" rowspan="1">Owning operator fault management sends alarm notification to owningoperator Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (0)</td><td colspan="1" rowspan="1">Owning operator Non-RT RIC sends alarm notification to owning operatorShared O-RU orchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (Loop)</td><td colspan="1" rowspan="1">O-DU#2 initiates supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (Loop)</td><td colspan="1" rowspan="1">O-RU response from supervision operations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (0)</td><td colspan="1" rowspan="1">O-DU#2 detects that it has lost communication sessions to the SharedO-RU. It raises a communication alarm to the owning operator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (0)</td><td colspan="1" rowspan="1">Cease transmission – Shared O-RU detects supervision failure with O-DU#2 and ceases transmitting on partitioned carrier associated with O-DU from the participating operator RAN network.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (0)</td><td colspan="1" rowspan="1">Shared O-RU sends alarm notification to the participating operator faultmanagement.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (0)</td><td colspan="1" rowspan="1">Participating operator fault management sends alarm notification toparticipating operator Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (0)</td><td colspan="1" rowspan="1">Participatingoperator Non-RT RIC sends alarmnotification toparticipating operator Shared O-RU orchestration rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">O-DU terminates subscription to supervision notification .</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the Shared O-RU supervision use case is given in figure 4.20.3.18-1 for Multi-MNO.

![](images/73b05290202b0c56265ff5d0b1a9f0488d797fe6bef7a976bab29bdd06c08d1d.jpg)

> **Image Summary:** {"image": "image_o_ran_spec.png"}
  
Figure 4.20.3.18-1: Supervision use case of a Shared O-RU in Multi-MNO

4.20.3.19 Antenna Line device (ALD) control sub-use case of a Shared O-RU for MultiMNO configuration

The following describes the solution for the ALD control sub-use case for a Shared O-RU for Multi-MNO configuration.

he context of the antenna line device control use case of a Shared O-RU is captured in table 4.20.3.19-1.

# Table 4.20.3.19-1: Antenna line device control use case of a Shared O-RU

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>The ALD connected to Shared O-RU is configured to operate with ALDcontroller.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors andRoles</td><td rowspan=1 colspan=1>Owning operator rApp is responsible for determining which O-DU isresponsible for ALD oontroller aspects.O-DU is responsible for implementing ALD oontroller.O-RU is responsible for bridging between OFH and HDLC.ALD is responsible for terminating HDLC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Shared O-RU has started up and has been configured with correctsoftware version.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Owning operator rApp determines which O-DU is responsible forperforming ALD controller functionality.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Owning operator rApp triggers the configuration of the ALD controller forShared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Owning operator Non-RT RIC triggers the configuration of ALD controllerfor Shared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Owning operator SMO uses O1 interface to configure ALD controller inO-DU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>O-DU uses open fronthaulinterface to configure ALD aspects of SharedO-RU.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 9</td></tr><tr><td rowspan=1 colspan=1>Step 6 (M)</td><td rowspan=1 colspan=1>Participating operator rApp triggers the configuration of the ALD controllerfor Shared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>Participating operator Non-RT RIC triggers the configuration of ALDcontroller for Shared O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 8 (M)</td><td rowspan=1 colspan=1>O-DU uses open fronthaul interface to signal ALD request.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Step 9 (M)</td><td rowspan=1 colspan=1>O-DU uses open fronthaul interface to signal ALD response.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Step 10 (M)</td><td rowspan=1 colspan=1>Shared O-RU provides interworking between OFH and HDLC request.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Step 11 (M)</td><td rowspan=1 colspan=1>Shared O-RU provides interworking between OFH and HDLC response.</td><td rowspan=1 colspan=1>O-RAN.WG4.MP[28], clause 14.4</td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>ALD connected to Shared O-RU is configured correctly.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the antenna line device sub-use case is given in figure 4.20.3.19-1.

![](images/9ec980800285f1edd9824f2f4d2b04518605544c28a53313935828c12be3ce37.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.19-1: Antenna line device sub-use case for multi-MNO

4.20.3.20 Antenna calibration use case of a Shared O-RU for Multi-MNO configuration (deferred)

The following will describe the solution for the antenna calibration sub-use case for a Shared O-RU.

# 4.20.3.21 Rehoming use case of a Shared O-RU for Multi-MNO

The following describes the solution for the rehoming sub-use case for a Shared O-RU in a Multi-MNO configuration.   
The step-by-step details of the rehoming use case of a Shared O-RU is in table 4.20.3.21-1.

Table 4.20.3.21-1: Rehoming use case of a Shared O-RU in Multi-MNO   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">A Shared O-RU is rehomed and is able to pair with new O-DU or existing(previous) O-DU parents in a Multi-MNO setting.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU is the element that is rehomed.Host O-DU (old) is the original Shared O-RU parent.SRO O-DU (old) is another original O-DU Shared O-RU is connected to.This is owned by the participating operator.</td><td colspan="1" rowspan="1"></td></tr><tr><td rowspan="7">Assumptions</td><td>Host O-DU (new) is the new Shared O-RU parent. SRO O-DU (new) is another new O-DU Shared O-RU is connected to.</td><td></td></tr><tr><td>This is owned by the participating operator.</td><td colspan="1"></td></tr><tr><td>SMO can receive results from calibration.</td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td>The Shared O-RU is in a deployment with the original (old) O-DUs and</td><td colspan="1"></td></tr><tr><td>will be moved to the new ones or stays with the original O-DUs (Typically) the operator will plan a Shared O-RU move before they</td><td colspan="1"></td></tr><tr><td>actually perform the operations related to the move.</td><td colspan="1"></td></tr><tr><td rowspan="6">Begins when</td><td>This use case starts with any of these three situations:</td><td></td></tr><tr><td>Case #1 starts when the Shared O-RU is physically moved to a new</td><td colspan="1"></td></tr><tr><td>location (however still connected to original O-DUs).</td><td colspan="1"></td></tr><tr><td>Case #2 starts when the Shared O-RU is physically moved to a new location but is connected to new O-DUs.</td><td colspan="1"></td></tr><tr><td>Case #3 starts when the Shared O-RU stays in same physical location</td><td colspan="1"></td></tr><tr><td>but is connected to new O-DUs (management-initiated rehoming).</td><td colspan="1"></td></tr><tr><td rowspan="2">Step 1 (M)</td><td>Case #1 – O-RU is physically moved with same O-DU parents Shared O-RU is disconnected from original O-DUs</td><td></td></tr><tr><td>The Shared O-RU is physically disconnected (fiber disconnected) from the existing O-DU parents.</td><td colspan="1"></td></tr><tr><td>Step 2 (M)</td><td colspan="2">The Shared O-RU is either physically reconnected (different fiber) or connected at the transport layer (with the original fiber) to reconnected to the original O-DU parents, and the following sub-use cases are triggered as a result: Shared O-RU startup sub-use case for Multi-MNO configuration • Configuration sub-use case ● Resource partitioning sub-use case for Multi-MNO configuration Coordinated reset sub-use case for Multi-MNO configuration • Supervision sub-use case for Multi-MNO configuration</td></tr><tr><td>Step 1 (M)</td><td colspan="2">CASE #2 – O-RU is physically moved with new O-DU parents Shared O-RU is disconnected from original O-DUs</td></tr></table>

<table><tr><td colspan="4">NCE</td></tr><tr><td>Use Case Stage</td><td colspan="2">Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td rowspan="2"></td><td colspan="2">The Shared O-RU is physically disconnected (fiber disconnected) from the former O-DU parents.</td><td></td></tr><tr><td colspan="2">Then, the Shared O-RU is physically moved to a new location. Shared O-RU is connected to new O-DUs</td><td></td></tr><tr><td rowspan="7">Step 2 (M)</td><td colspan="2">The Shared O-RU is either physically reconnected (different fiber) or</td><td rowspan="6"></td></tr><tr><td>connected at the transport layer (with the original fiber) to new O-DU parents, and the following sub-use cases are triggered as a result:</td><td></td></tr><tr><td>Shared O-RU startup sub-use case for Multi-MNO configuration</td><td></td></tr><tr><td>Configuration sub-use case ●</td><td>Resource partitioning sub-use case for Multi-MNO configuration</td></tr><tr><td>●</td><td></td></tr><tr><td></td><td>Coordinated reset sub-use case for Multi-MNO configuration</td></tr><tr><td colspan="2">Supervision sub-use case for Multi-MNO configuration Case #3 – Management initiated rehoming</td></tr><tr><td colspan="2">Step 1 (M) Main operator SMO Initiates rehoming operation with O-DUs connected</td><td>Management initiated rehoming for Shared O-RU Shared O-RU already has physical front-haul connections in place.</td><td></td></tr><tr><td></td><td colspan="2">to the Shared O-RU. Participating operator SMO initiates rehoming operation with O-DUs connected to the Shared O-RU. Shared O-RU starts up</td><td></td></tr><tr><td rowspan="8">Step 2 (M) Ends when</td><td colspan="2">The Shared O-RU starts up with the new O-DU parents, and the following</td><td rowspan="3"></td></tr><tr><td rowspan="2"></td></tr><tr><td></td></tr><tr><td colspan="2">sub-use cases are triggered as a result: Shared O-RU startup sub-use case for Multi-MNO configuration</td></tr><tr><td>Configuration sub-use case ●</td><td></td></tr><tr><td>●</td><td>Resource partitioning sub-use case for Multi-MNO configuration Coordinated reset sub-use case for Multi-MNO configuration</td></tr><tr><td></td><td>Supervision sub-use case for Multi-MNO configuration</td></tr><tr><td>●</td><td>The Shared O-RU has been moved and connected to the appropriate O-</td></tr><tr><td>DUs, and is operational again.</td><td></td></tr><tr><td>Exceptions</td><td colspan="2">None.</td><td></td></tr><tr><td>Post Conditions None.</td><td colspan="2"></td><td></td></tr><tr><td></td><td colspan="2"></td><td></td></tr></table>

The flow diagram of the rehoming use case of a Shared O-RU for Multi-MNO is given in figure 4.20.3.21-1.

![](images/f01afcd924070fd09adca3658d8f1cc77a516fc35b629ae937d161ef8c15ab2a.jpg)

> **Image Summary:** {"entities": ["gNB", "RU", "CU", "O-RU", "O-DU", "O-CU", "RAN", "O-RAN", "CU-CP", "CU-UP", "RIC", "Non-RT RIC", "Near-RT RIC", "Far-RT RIC", "O-RU Function", "Radio Unit", "Central Unit", "Control Plane", "User Plane", "O-RAN Alliance", "xAPI", "A1 Interface", "E2 Interface", "X2 Interface", "Xn Interface", "F1 Interface", "Open Fronthaul Interface", "A1.1 Interface", "xAPI Client", "xAPI Server", "gNB Interface", "gNB Architecture", "O-RAN Architecture", "Radio Access Network"], "relationships": ["gNB → CU: Radio Access Network", "RU → CU: O-RAN Architecture", "CU → CU-CP: Central Unit", "CU → CU-UP: Central Unit", "O-RU → O-DU: Open Fronthaul Interface", "O-DU → CU: F1 Interface", "CU → Non-RT RIC: E2 Interface", "CU → Near-RT RIC: E2 Interface", "CU → Far-RT RIC: E2 Interface", "RIC → O-DU: A1 Interface", "xAPI Client → xAPI Server: xAPI", "O-RU Function → RU: Radio Unit", "O-DU → O-CU: Distributed Unit", "O-RAN → O-RU Function: O-RAN Alliance", "O-RU → gNB: O-RAN"], "hierarchy": ["gNB = RU + CU", "CU = CU-CP + CU-UP", "O-RAN = O-RU Function + O-DU + O-CU", "RIC = Non-RT RIC + Near-RT RIC + Far-RT RIC"], "flows": [], "notes": ["Figure 2.1.1: gNB and O-RAN Architecture", "Figure 2.1.1-1: O-RAN Interface", "Figure 2.1.1-2: gNB Interface", "Figure 2.1.1-3: O-RAN Interface", "Figure 2.1.1-4: gNB Interface", "Figure 2.1.1-5: O-RAN Interface", "The figure depicts the architecture of a gNB within the context of O-RAN. It illustrates the interaction between different components such as the Radio Unit (RU), Central Unit (CU), and various Radio Interface Controllers (RICs).", "The diagram outlines the interfaces between these components, including Open Fronthaul, F1, A1, and E2 interfaces. These interfaces facilitate communication and control across the network elements.", "Several RICs (Non-RT, Near-RT, and Far-RT) are shown, each with distinct capabilities and responsibilities in managing and optimizing the network performance."], "image_label": "Figure 2.1.1"}


# 4.20.3.22 Performance management use case of a Shared O-RU for Multi-MNO

The following describes the solution for the performance management sub-use case for a Shared O-RU in a Multi-MNO configuration.

The context of the performance management sub-use case of a Shared O-RU in a Multi-MNO configuration is captured in table 4.20.3.22-1.

Table 4.20.3.22-1: Performance management sub-use case of a Shared O-RU in a Multi-MNO   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Each O-DU has established subscriptions to receive performancemanagement notifications regarding operation of the fronthaul betweenthe O-DUs and shared O-RU.The O-DU and Shared O-RU are able to report performancemeasurement data towards their consumers in a Multi-MNoconfiguration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU generates performance management notifications on a perpartitioned carrier basisO-DU subscribes to receive performance management notifications fromShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-DU has configured performance management metrics for respectivepartitioned carrier.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Fronthaul control and user plane is operational between O-DU andShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">O-DU#1 subscribes to receive PM notifications from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">O-DU#2 subscribes to receive PM notifications from Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (loop)</td><td colspan="1" rowspan="1">Shared O-RU sends PM notification to O-DU#1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (loop)</td><td colspan="1" rowspan="1">Shared O-RU sends PM notification to O-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">O-DU to SMO performance operations</td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">PM event notification reportingThe O-DU (producer) sends performance data to the SMO (consumer)through an event notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">Streaming PM reportsThe O-DU establishes a persistent connection to the SMO and sendsperformance data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Attribute-based or URI-based collection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Performance data is read by the consumer (SMO) through configurationmanagement attribute. Alternatively, the O-DU can support a datascraping method where a collector (SMO) reads the data from a pre-defined URI.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">Producer or PM fil upload (file upload)O-DU uploads a PM file to the SMO.See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">Consumer downloads PM file (fil download)O-DU issues file ready notification to SMO about the data being ready fordownload, or SMO periodically polls the O-DU. Afterwards, the SMO(consumer) can download the PM file.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">O-RU to O-DU performance operations (in hierarchical configuration)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">PM event notification reportingThe O-RU sends performance data to the O-DU through an eventnotification. The notification is sent to a subscriber of performance data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">O-DU requests for O-RU to start sending PM dataO-DU invokes an RPC to give PM credentials, target URI, and periodicitynotification interval to the Shared O-RU. This includes al the necessaryinformation for the O-RU to perform a file transfer to an endpoint.See NOTE 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Shared O-RU uploads PM fileThe Shared O-RU periodically uploads a performance to the target URIusing the PM credentials given by the O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">O-RU to SMO performance operations (in hybrid configuration)</td></tr><tr><td colspan="1" rowspan="1">Step 1 (0)</td><td colspan="1" rowspan="1">PM event notification reportingThe O-RU sends performance data to the SMO through an eventnotication via M-plane. The notification is sent to a subscriber ofperformance data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">SMO requests for O-RU to start sending PM data</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">SMO invokes an RPC to give PM credentials, target URI, and periodicitynotification interval to the Shared O-RU. This includes all the necessary information for the O-RU to perform a file transfer to a endpoint.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Shared O-RU uploads PM fileThe Shared O-RU uploads performance file to target URI using PMcredentials given by the SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">(1) Subscription setup: O-DU terminates subscription to performancemanagement notification.(2) O-DU to SMO sending PM data: Use case ends with the producer (O-DU) sending performance data to the consumer (SMO).(3) O-RU sending performance data: Use case ends with the producer(O-RU) starting to send performance data to the subscriber.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The consumer has received performance data and may perform post processing operations on the data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: When the O-DU sends performance files received from a Shared O-RU, they are converted to the proper3GPP format before sending to SMO. See O-RAN WG5.O-DU-O1 [25].NOTE 2: The O-DU establishes a framework for the Shared O-RU to send PM files. This operation is performedonly once, thereafter, the Shared O-RU sends the PM files periodically.</td></tr></table>

The flow diagram of the performance management sub-use case of a Shared O-RU in a Multi-MNO is given in figure 4.20.3.22-1.

![](images/3a9f5df71ba6a78dc257ad16d1977ec1c249a92b953cb90febdfb8cb8018f3a1.jpg)

> **Image Summary:** {"entities": ["O-RAN Architecture", "RAN Intelligent Controller (RIC)", "Near-RT RIC", "Far-Edge RIC", "Non-RT RIC", "O-RU", "O-DU", "CU", "CU-CP", "CU-UP", "gNB", "O-RAN Fronthaul Interface", "O-RAN Fronthaul Interface", "E2 Interface", "A1 Interface", "Xn Interface", "F1 Interface", "O-RAN", "3GPP", "Interface Description", "RIC Use Case", "Performance Optimization", "Automated Policy Management", "Network Slicing", "O-RAN Architecture Principles", "Openness", "Intelligence", "Virtualization", "Cloudification", "Open APIs", "AI/ML", "Real-Time Data"], "relationships": ["RAN Intelligent Controller (RIC) → O-RAN Architecture: Architectural element", "Near-RT RIC → O-RAN Architecture: Architectural element", "Far-Edge RIC → O-RAN Architecture: Architectural element", "Non-RT RIC → O-RAN Architecture: Architectural element", "O-RU → O-DU: O-RAN Fronthaul Interface, bidirectional", "O-DU → CU: F1 Interface, bidirectional", "CU → CU-CP: Internal interface, bidirectional", "CU → CU-UP: Internal interface, bidirectional", "CU-CP → CU-UP: Internal interface, bidirectional", "CU → gNB: Internal interface, bidirectional", "gNB → CU: Internal interface, bidirectional", "Near-RT RIC → O-DU: A1 Interface, bidirectional", "Near-RT RIC → CU: A1 Interface, bidirectional", "O-RAN Architecture → O-RU: Contains", "O-RAN Architecture → O-DU: Contains", "O-RAN Architecture → CU: Contains", "O-RAN Architecture → CU-CP: Contains", "O-RAN Architecture → CU-UP: Contains", "O-RAN Architecture → gNB: Contains", "O-RAN Architecture → Performance Optimization: RIC Use Case, enables", "O-RAN Architecture → Automated Policy Management: RIC Use Case, enables", "O-RAN Architecture → Network Slicing: RIC Use Case, enables", "O-RAN → Openness: O-RAN Architecture Principle, enables", "O-RAN → Intelligence: O-RAN Architecture Principle, enables", "O-RAN → Virtualization: O-RAN Architecture Principle, enables", "O-RAN → Cloudification: O-RAN Architecture Principle, enables", "O-RAN → Open APIs: O-RAN Architecture Principle, enables", "O-RAN → AI/ML: O-RAN Architecture Principle, enables"], "hierarchy": ["gNB = O-RU + O-DU + CU (CU-CP + CU-UP)", "CU = CU-CP + CU-UP", "O-RAN Architecture = O-RU + O-DU + CU + RAN Intelligent Controller (RIC)"], "flows": [], "notes": ["Figure 1: O-RAN Architecture Principles", "Note 1: Interfaces and functions are allocated based on flexibility and performance requirements.", "Note 1: Interfaces and functions are allocated based on flexibility and performance requirements.", "Note 1: Interfaces and functions are allocated based on flexibility and performance requirements.", "The architecture and interfaces support open, intelligent, and virtualized networks.", "Figure 1 depicts a high-level O-RAN architecture and its key components.", "The O-RAN architecture enables new functionalities and use cases through intelligent control and automation.", "Figure 1 illustrates the integration of the RIC into the O-RAN architecture.", "Figure 1 demonstrates the role of the RIC in optimizing network performance and automating policy management.", "Figure 1 showcases the flexibility and adaptability of the O-RAN architecture.", "Figure 1 highlights the importance of open interfaces and APIs in enabling innovation and interoperability.", "3GPP interfaces are also shown in Figure 1 for context.", "O-RAN Architecture Principles: Openness, Intelligence, Virtualization, Cloudification, Open APIs, AI/ML"], "image_description": "This image presents a high-level overview of the O-RAN architecture. The core components include the O-RU, O-DU, CU (split into CU-CP and CU-UP), and the RAN Intelligent Controller (RIC), encompassing Near-RT, Far-Edge, and Non-RT RICs.  The architecture emphasizes openness, intelligence, virtualization, and cloudification, utilizing open APIs and AI/ML.  The image shows various interfaces between these components, including the O-RAN Fronthaul Interface between the O-RU and O-DU, the F1 Interface between the O-DU and CU, and the A1 Interface connecting the RIC to both the O-DU and CU. A note clarifies that the allocation of interfaces and functions is based on flexibility and performance requirements. The diagram also includes 3GPP interfaces for context.  The architecture supports several RIC use cases, such as performance optimization, automated policy management, and network slicing. This figure is labeled 'Figure 1: O-RAN Architecture Principles.'"}


# 4.20.3.23 Antenna calibration use case of a Shared O-RU for Multi-MNO

The following describes the solution for the antenna calibration sub-use case for a Shared O-RU in a Multi-MNO configuration.

The step-by-step details of the antenna calibration use case of a Shared O-RU are captured in table 4.20.3.23-1.

Table 4.20.3.23-1: Antenna calibration of a Shared O-RU in Multi-MNO   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">The host O-DU performs an antenna calibration procedure with theshared O-RU in a Multi-MNO configuration.The owning operator O-DU reports antenna calibration results to theSMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Shared O-RU performs the antenna calibration procedure.Owning operator O-DU (host) that requests for antenna calibrationprocedure with Shared O-RU.Participating operator O-DU is owned by the participating operator.Owning operator SMO can receive results from calibration.Participating operator SMO can also receive results from calibration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All O-DUs have connectivity to O-RU.All actors are operational and have initialized.Fronthaul control and user plane is operational between all O-DUs andShared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">1. The Shared O-RU has detected that antenna calibration is required.2. The Owning operator O-DU initiates an antenna calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.1 (0)</td><td colspan="1" rowspan="1">Recalibration required (O-RU initiated)The Shared O-RU has detected that antenna calibration is needed andsends an antenna calibration needed notification to the owning operatorhost O-DU over the open FH. In this case, the O-RU initiates thecalibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.2 (0)</td><td colspan="1" rowspan="1">Calibration requestThe host O-DU of the owning operator requests for antenna calibrationprocedure to start for Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.1 (M)</td><td colspan="1" rowspan="1">Host O-DU informs SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The owning operator SMO together with host O-DU (owning operator) informs that an antenna calibration operation is needed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.2 (M)</td><td colspan="1" rowspan="1">SMO to SMO negotiationThrough exposure of management services, the owning operator SMOnegotiates with the participating operator SMO that the host O-DU wouldlike to perform an antenna calibration operation. Here, the participatingoperator SMO may object to the antenna calibration operation.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.3 (0)</td><td colspan="1" rowspan="1">Host O-DU initiates antenna calibration If agreed to proceed, owning operator SMO together with host O-DU(owning operator) initiates an antenna calibration operation.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.4 (M)</td><td colspan="1" rowspan="1">SMO informs participating operator O-DUThe participating operator SMO informs its O-DU that the antennacalibration operation will be initiated by the owning operator (host) O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1.5 (M)</td><td colspan="1" rowspan="1">Calibration request (O-DU initiated)The host O-DU of the owning operator requests for antenna calibrationprocedure to start for Shared O-RU. In this case the O-DU initiates thecalibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">Calibration operation at O-RUShared O-RU performs antenna calibration procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Calibration responseThe Shared O-RU responds with antenna calibration results to theowning operator O-DU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Calibration resultsThe owning operator O-DU returns antenna calibration results to owningoperator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Calibration results to O-DU #2Shared O-RU notifies the participating operator O-DU with antennacalibration results.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Calibration results</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">The participating operator O-DU returns antenna calibration results to theparticipating operator SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">(1) Antenna calibrated: Antenna calibration procedure has finished, andresults reported.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">The O-RU may indicate a calibration failure, which is reported to theowning operator O-DU. The O-DU logs the failure and notifies north-bound entities.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the antenna calibration use case of a Shared O-RU for Multi-MNO is given in figure 4.20.3.23-1.

![](images/1aaee20ecf457f3c27e5e7f03cbcf32147c8c0cd116ce24dfd5c47baa69ede3d.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.23-1: Antenna calibration use case of a Shared O-RU for Multi-MNO

# 4.20.3.24 Dynamic resource shifting use case of a Shared O-RU

The following will describe the solution for dynamic resource shifting sub-use case for a Shared O-RU.

Table 4.20.3.24-1: Dynamic resource shifting use case of a Shared O-RU   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Cooperating O-DUs serve cells overlapping spectrum in a way, so thatfrequency resources effectively used by each O-DU can be dynamicallyshifted between O-DUs and interference is avoided at air interface. There is no impact to regular procedures performed between O-DUs and UEsand UE energy consumption is not increased.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors andRoles</td><td rowspan=1 colspan=1>Shared O-RU serves radio functions to the air.O-DU performs radio resource handling.SMO configures other actors.Near-RT RIC coordinates dynamic shifting of spectrum resourcesbetween O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O-RU is configured to serve for 2 or more O-DUs.O-DUs are configured respectively – including dedicated set of bandwidthparts in UL and DL alike. Near-RT RIC knows how bandwidth parts are configured to O-DUs.Near-RT RIC is receiving traffic-related statistics from O-DUs.Near-RT RIC is provided with traffic shaping policy for cells that useoverlapping spectrum.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Near-RT RIC decides to change bandwidth effectively used by cellsserved by O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Near-RT RIC provides O-DUs with updated lists of bandwidth parts O-DUs are allowed to utize.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>O-DUs respectively confirm reception of updated list of permitedbandwidth parts to Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (l0op)</td><td rowspan=1 colspan=1>O-DUs use actual list of permitted bandwidth parts for scheduling indownlink and uplink respectively.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Update of list of permitted bandwidth parts confirmed to Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>It is feasible that list of permitted bandwidth parts is updated to some (notall) of cooperating O-DUs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Lists of permitted bandwidth parts are successfully updated for desiredO-DUs.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the dynamic resource shifting sub-use case for Shared O-RU is given in figure 4.20.3.24-1.

![](images/fca1cebd22040f210fc4f711d548b93be748acb5b0293df0fac43de36652bcde.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.20.3.24-1: Dynamic resource shifting sub-use case for Shared O-RU

# 4.20.3.25 Static resource shifting use case for Single-MNO

The following will describe the solution for static resource shifting sub-use case for a Shared O-RU.

Table 4.20.3.25-1: Static resource shifting use case of a Shared O-RU   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Cooperating O-DUs serve cells using a designated chunk of spectrum ata time, allowing carrier frequency resources to be effectively reallocatedbetween O-DUs and ensuring interference is avoided at the air interface.This is a service impacting use case.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors andRoles</td><td colspan="1" rowspan="1">Actors:Shared O-RU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">O-DUsO-CUSMORoles:Please refer to 4.20.2.25.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Initiation</td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O-RU is configured to have connectivity with 2 or more O-DUs.O-DUs are configured respectively for connectivity with Shared O-RU.Fronthaul M-plane (Netconf session) sessions are established between Shared O-RU and O-DUs as per provided configurations.●  SMO knows the capabilities of O-DUs.SMO is receiving traffic-related statistics from O-DUs.SMO manages the entire process and ensures coordination betweenO-DUs.SMO configures the initial roles and resources for O-DUs and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Collection of counters</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">O-DUs report PM counters to SMO (Non-RT RIC). PM counters are usedby SMO as trigger to decide if static resource shifting shall be applied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Static resource shifting</td></tr><tr><td colspan="3" rowspan="1">Deactivation and removal of cell(s) and carrier(s) associated with O-DU#1</td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">SMO decides to start static resource shifting for specific cell(s) served byO-DUs through Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">SMO requests O-CU to deactivate cell(s) served by O-DU#1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">O-CU informs O-DU#1 about the cell(s) to be deactivated via F1interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">O-DU#1 maps mentioned above cell(s) with corresponding carrier(s) thatneed to be deactivated on Shared O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">For carriers determined in Step 3, O-DU#1 performs carrier deactivationwith O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Once O-DU#1 knows that relevant carriers(s) are deactivated, it repliesto O-CU's request for cell deactivation received in Step 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">O-CU replies to SMO's request for cell deactivation received in Step 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7.1 (M)</td><td colspan="1" rowspan="1">Hierarchical deployment – Cell(s) and carrier(s) removal</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">SMO requests O-DU#1 to remove specific inactive cell(s) and relatedcarrier(s) from configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7.2 (M)</td><td colspan="1" rowspan="1">O-DU#1 maps requested cells) with carrier(s) that needs to be removedfrom O-RU's configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7.3 (M)</td><td colspan="1" rowspan="1">O-DU#1 informs O-CU about cell(s) being subject of removal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7.4 (M)</td><td colspan="1" rowspan="1">O-DU#1performs config update scenario to O-RU to removeconfiguration related to carrier(s) determined in Step 7.2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7.5 (M)</td><td colspan="1" rowspan="1">O-DU#1 responds to SMO's request for cell removal received in Step 7.1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.1 (M)</td><td colspan="1" rowspan="1">Hybrid deployment – Cell(s) and carrier(s) removalSMO requests O-RU to remove specific carriers.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.2 (M)</td><td colspan="1" rowspan="1">O-RU notifies O-DU that specific carriers have been removed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.3 (M)</td><td colspan="1" rowspan="1">O-DU#1 performs carrier-to-cell mapping.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.4 (M)</td><td colspan="1" rowspan="1">O-DU#1 informs SMO about change in resource availability.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.5 (M)</td><td colspan="1" rowspan="1">For cells that have lost their related carriers completely O-DU#1 informsO-CU about cell are no longer operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.6 (M)</td><td colspan="1" rowspan="1">O-RU responds to SMO's request for carrier(s) removal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.7 (M)</td><td colspan="1" rowspan="1">SMO requests O-DU#1 to remove affected cells.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8.8 (M)</td><td colspan="1" rowspan="1">O-DU#1 responds to SMO's request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">Configuration of cell(s) and carrier(s) associated with O-DU#2</td></tr><tr><td colspan="1" rowspan="1">Step 9.1 (M)</td><td colspan="1" rowspan="1">Hierarchical deployment– Cel(s) and carrier(s) configurationSMO configures the cell(s and related carriers to O-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9.2 (M)</td><td colspan="1" rowspan="1">Based on provided configuration O-DU#2 maps the cell(s) with relatedcarrier(s) that needs to be configured to O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9.3 (M)</td><td colspan="1" rowspan="1">O-DU#2 provides O-RU with configuration for carrier(s) known from Step9.1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9.4 (M)</td><td colspan="1" rowspan="1">For cells having their related carriers configured to O-DU, the O-DU#2 informs O-CU about cell(s) being ready to be used.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9.5 (M)</td><td colspan="1" rowspan="1">For configured cell requested in Step 9.1 the O-DU#2 sends cell(s)configuration notification to SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.1 (M)</td><td colspan="1" rowspan="1">Hybrid deployment – Cell(s) and carrier(s) removalSMO requests O-RU to configure carier(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.2 (M)</td><td colspan="1" rowspan="1">O-RU sends carrier(s) configuration change notification to O-DU#2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.3 (M)</td><td colspan="1" rowspan="1">O-RU sends carrier(s) configuration change notification to SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.4 (M)</td><td colspan="1" rowspan="1">SMO requests O-DU#2 to configure cell(s) and informs O-DU#2 aboutmapping between cells and carriers.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.5 (M)</td><td colspan="1" rowspan="1">For cells with properly mapped carriers the O-DU#2 informs O-CU aboutcell(s) that are available and ready for activation.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10.6 (M)</td><td colspan="1" rowspan="1">O-DU#2 to SMO's request provided in Step 10.4.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">SMO requests O-CU to activate specific cells.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">O-CU requests O-DU#2 to activate specificl(s) mentioned in Step 11.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">O-DU#2 maps requested cell(s) with carrier(s) that needs to be activatedto O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1">O-DU#2 requests O-RU to activate cariers determined in Step 13.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">O-RU responds to O-DU#2 with carrier(s) activation notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">O-DU#2 responds to O-CU with cell(s) activation response.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">O-CU responds to SMO with cell(s) activated notification.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Shifting of cell(s) and associated carrier(s) from O-DU#1 to O-DU#2 isaccomplished.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">Error at any of isted steps.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Frequency resources are used by cells and related carriers handled byO-DU#2.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the static resource shifting sub-use case for Shared O-RU is given in figure 4.20.3.25-1.

![](images/7fa97ce73c0be53acac243c39a6f79c1c8e8963e142d5adab996d974d29693c7.jpg)

> **Image Summary:** {"entities": ["O-RAN", "O-DU", "O-RU", "RIC", "O-CU", "Non-RT RIC", "Near-RT RIC", "Far-RT RIC", "xApp", "O-DU Interface", "O-RU Interface", "O-CU Interface", "E2 Interface", "A1 Interface", "E1 Interface", "xApp Function", "O-CU Function", "O-RU Function", "O-DU Function", "API", "Management and Orchestration"], "relationships": ["O-RAN → xApp: API, management and orchestration, unidirectional", "O-CU → Non-RT RIC: E2 Interface, management and orchestration, unidirectional", "O-CU → Near-RT RIC: E2 Interface, management and orchestration, unidirectional", "O-CU → Far-RT RIC: E2 Interface, management and orchestration, unidirectional", "xApp → O-DU Interface: API, management and orchestration, unidirectional", "xApp → O-RU Interface: API, management and orchestration, unidirectional", "xApp → O-CU Interface: API, management and orchestration, unidirectional", "O-DU Interface → O-DU Function: Function, unidirectional", "O-RU Interface → O-RU Function: Function, unidirectional", "O-CU Interface → O-CU Function: Function, unidirectional", "O-DU Function → O-CU Function: E1 Interface, unidirectional", "O-RU Function → O-CU Function: E1 Interface, unidirectional", "RIC → xApp: A1 Interface, management and orchestration, unidirectional"], "hierarchy": ["O-RAN = xApp + O-DU + O-RU + O-CU", "O-CU = O-CU Function + O-CU Interface", "O-DU = O-DU Function + O-DU Interface", "O-RU = O-RU Function + O-RU Interface", "RIC = Non-RT RIC + Near-RT RIC + Far-RT RIC"], "flows": [], "notes": ["Figure 2.1 - Overall architecture", "xApp Function provides the required functionality to interface with RIC","RIC interfaces with O-CU through E2","RIC interfaces with xApp through A1"]}
  
Figure 4.20.3.25-1: Static resource shifting sub-use case for Shared O-RU

# 4.20.4 Required data

# 4.20.4.1 Required data for all Shared O-RU use cases

The following required data is relevant to the following sub-use cases: resource partitioning, start-up, configuration, supervision, performance management, ALD control, antenna calibration, rehoming, and shutdown:

Inventory system maintains inventory data for the Shared O-RUs because it needs to be able to identify Shared O-RUs.   
• The resource partitioning rApp maintains carrier resource information because it needs to be able to partition the Shared O-RU carrier resources between different O-DU nodes. In hierarchical management mode, the configuration rApp maintains the active/standby state & status for O-DUs because needs to determine which O-DU is responsible for configuring the common aspects of a Shared O-RU.   
• The supervision needs to include the O-DU identity because the Shared O-RU needs to be able to support supervision on a per O-DU basis. Alarm data needs to be kept at the Shared O-RU because the Shared O-RU needs to be able to terminate transmissions associated with an O-DU when it loses supervision with that O-DU and to continue to operate with other O-DUs. There will be a history of alarm data.   
• Shared O-RU measurement counters and KPIs (as defined by O-RAN.WG4.MP [28]) shall be available on a per O-DU basis.   
• O-DU needs to include its O-DU identity to enable supervision operation on a per O-DU basis. The ALD control rApp maintains data to keep track which O-DU is responsible for ALD controller functionality because it needs to be able to select which O-DU is responsible for ALD controller functionality.

# 4.20.4.2 Required data for Single-MNO configurations

he following data applies for single operator configurations when used by the other Shared O-RU sub-use cases:

• Non-RT RIC needs to be able to partition the Shared O-RU carriers between O-DU nodes operated by the same MNO.

# 4.20.4.3 Required data for Multi-MNO configurations

The following data applies for multi-operator configurations when used by the other Shared O-RU sub-use cases:

The resource partitioning rApp needs to be able to partition the Shared O-RU carrier resources between differen O-DU nodes of different MNOs. • Shared O-RU needs to be able to associate management accounts with an MNO. • The Shared O-RU needs to be able to implement role-based access control on a per-MNO basis. • The Shared O-RU needs to associate carrier resources with MNOs. • Measurement counters and KPIs (as defined by O-RAN WG4) need to be available on a per MNO basis. • Tenant SMO needs to be able to support common Shared O-RU configuration defined by host operator.

# 4.20.4.4 Required data for resiliency use cases

The following data is used by the resiliency use case:

The supervision needs to include the O-DU identity because the Shared O-RU needs to be able to support supervision on a per O-DU basis. Alarm data needs to be kept at the Shared O-RU because the Shared O-RU needs to be able to terminate transmissions associated with an O-DU when it loses supervision with that O-DU and to continue to operate with other O-DUs. There will be a history of alarm data. The configuration data from the active O-DU is passed to the standby O-DU. The configuration information of carriers of the standby O-DU are configured for the O-RU. • The management system has the state & status data regarding which O-DU is and shall be active. The management system has the state & status data regarding which O-DUs are and shall be standby. The management system has the alarm history and alarm information for the Shared O-RU.

NOTE: There are many different situations and variations of the resiliency sub-use cases. Some of them need not require all the above data.

# 4.20.4.5 Required data for Shared O-RU management during O-DU SW update sub-use case for Shared O-RU

The following data is used by SW update of O-DU and associated Shared O-RU provisioning:

The configuration data for provisioning the SW updated O-DU based on the change management plan for SW update. The configuration information of carriers of the SW updated O-DU configured on the Shared O-RU. The management system has state and status details of O-DUs to identify the right candidate to be used for SW update. The management system has state and status details of SW updated O-DU to verify the status and health of the SW update. The management system has the alarm history and alarm data of the Shared O-RU to verify functionality and sanity of the SW updated O-DU. Non-RT RIC needs to be able to partition the Shared O-RU carriers between SW updated O-DU and other O-DU nodes operated by the same MNO. Alarm data and performance data needs to be kept at Shared O-RU to verify the sanity of O-DU SW update O-DU SW change management rApp maintains the change management plan data for O-DU SW update to initiate & supervise the SW update process and to validate the sanity of the deployment against the plan. Historical configuration and software details of the O-DU is maintained for SW update so that the mitigation step of the SW update can bring the O-DU to the situation before SW update.

# 4.20.4.6 Required data for Shared O-RU - Dynamic resource shifting

The following data is used to perform dynamic resource shifting:

The resource partitioning xApp maintains cell resource information because it needs to be able to partition frequency resources between different O-DU nodes.   
• O-DU measurement counters and KPIs related to served traffic shall be available for Near-RT RIC on a per O-DU basis.   
• Near-RT RIC needs to be able to dynamically update list of allowed bandwidth parts per O-DU nodes in a way so that each O-DU exclusively uses subset of shared bandwidth. The configuration information of cells served by O-DUs needs to be known to Near-RT RIC.

# 4.20.4.7 Required data for Shared O-RU - Static resource shifting

The following data is used to perform static resource shifting:

The resource optimization rApp may maintain cell resource information because it needs to be able to reallocate the cell and associated carrier frequency resources between different O-DU nodes. • O-DU measurement counters shall be available for SMO (Non-RT RIC) on a per O-DU and per cell basis via O1 interface. • The configuration information of cell(s) served by O-DUs needs to be known to SMO (Non-RT RIC).

# 4.21 Network energy saving

This clause provides the motivations, descriptions, and proposed solutions for different energy efficiency and energy saving features (sub-use cases). While there are energy savings by improving base station hardware efficiency and by the evolution of radio access technologies, the EE/ES use case primarily addresses enhancements in software efficiency and optimized configuration/control of various elements and functions, which are often AI/ML based.

# 4.21.1 Background and goal of the use case

The RAN is responsible for a major part of the Energy Consumption (EC) of a mobile network, and the O-RU accounts for the largest part of the energy consumption of the RAN. The rarefication of fossil fuel-based energy resources and the urgent need to reduce $\mathrm { C O } _ { 2 }$ emissions make the EC a strategic topic for network operators, in addition of being a significant component of the operators’ OPEX.

EC can be reduced by improving the Energy Efficiency (EE) of the network, and by introducing different Energy Saving (ES) mechanisms. Several ES mechanisms are related to switching off certain components in the network and differ from one another by their scope, time scale and network area. Applicable ES methods are for instance strongly load dependent. Optimization efficiency might be further improved by AI/ML based configuration thereof.

RAN functions related to network energy saving solutions have been studied in 3GPP RAN3 in Rel.17 as part of the Study on Enhancement for Data Collection for NR and EN-DC. The outcome is documented in 3GPP TR 37.817 [i.2]. 3GPP RAN2 and RAN3 might specify enhancements for the Minimization of Drive Tests (MDT) procedures and/or signaling procedures that rely on Xn signaling in Rel.18. While 3GPP RAN WGs work on solutions with ML model inference within the gNB, O-RAN specifies solutions that benefit from ML model inference in the Near-RT or Non-RT RIC (e.g., optimizing the network in larger service areas). For EE related network management, use cases, requirements and solutions are specified in 3GPP TS 28.310 [3]. Furthermore, EC measurements and KPIs for 5G networks, network functions, NG-RAN and gNBs such as energy efficiency and energy consumption KPIs and performance measurements are specified in 3GPP TS 28.554 [7]. Centralized and distributed ES management functions are specified in 3GPP TS 28.541 [5].

EE can be considered for the whole network (i.e., end-to-end), for a sub-network or per single network element. Within a network element it could be applicable per specific radio resource management mechanism or per radio or transport network link. Network wise EE is defined as the ratio between the data volume delivered in the network and the network

EC observed during the time-period required to deliver such data, with possible adaptations to account for different deployment scenarios and load situations (ETS ES 203 228 [i.5], 3GPP TR 38.913 [i.4]). 3GPP has launched a study item within Rel-18 (RP-213554: “Study on network energy saving for NR”) that will include among others, an evaluation methodology and KPIs for EC and ES gains and their impact on network and UE performance and EE. To assess EE and ES associated to radio resource management mechanisms and links, appropriate KPIs are necessary.

In a timescale of minutes, hours and above, and when the cell load is low, ES can be achieved by switching off one or more carriers or the cell. In a timescale from seconds to minutes, ES can be achieved by switching off RF channels (including possibly antennas) of a massive MIMO system. Tx and Rx parts might be switched independently. In a very short timescale corresponding to a symbol, subframe or frame, Advanced Sleep Modes (ASM) can be considered. RF channel on/off switching can be used at medium load and ASM might be usable even at high load. Lastly, ES solutions can be applied to the O-Cloud, namely to the O-CU and O-DU, and can cover mechanisms such as scale in/out processes, workload placement or hardware processors’ sleep modes etc. AI/ML is useful for all the above mechanisms with the important role of determining the switch off/on time that maximizes ES gain.

# 4.21.2 Entities/resources involved in the use case

Editor’s note: If possible, single common description for all sub-use cases.

The following is an exhaustive list of entities across all the identified solutions for this use case. All the entities may not be applicable for every solution.

1) Energy saving rApp:

a) Collect configurations, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports, geolocation information) from Non-RT RIC/SMO framework.   
b) Utilize the collected data for EE/ES optimization (e.g., if carriers or cells need to be switched off/on), and initiate O1 configuration updates, A1 policy updates, and/or open FH M-plane configuration updates through R1 interface.

2) Non-RT RIC/SMO framework:

a) Collect configurations, performance indicators and measurement reports E2 nodes via O1 and optionally via open FH M-plane from O-RUs and provide this information to energy saving rApp.   
b) Determine and signal updated configuration or policy for network energy saving use case (provided by energy saving rApp) to E2 nodes, and/or Near-RT RIC, and optionally O-RU.

3) E2 node:

a) Report cell configuration, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports).   
b) Perform actions required for EE/ES optimization per the configuration updates or policies received from NonRT RIC/rApp and/or Near-RT RIC/xApp.

4) O-RU node:

a) Report EC and EE related information.   
b) Perform actions required to perform EE/ES optimization per the configuration updates or policies received from Non-RT RIC/rApp and/or Near-RT RIC/xApp.

5) Near-RT RIC:

a) Collect configurations, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports) from E2 nodes. b) Receive EE/ES related policies via A1 interface for consideration during optimization. c) Determine and signal updated configuration or prolicy for network energy saving use case to E2 nodes.

# 4.21.3 Solutions

Editor’s note: Sub-use case specific solutions with detailed descriptions in fully separate clauses.

# 4.21.3.1 Carrier and cell switch off/on

Mobile networks often utilize multiple frequency layers (carriers) to cover the same service area. At low load, ES can be achieved by switching off one or more carriers or entire cells without impairing the network performance. The switch off/on decision can be made by an AI/ML model, deployed in Non-RT RIC/SMO (including option for deployment in an rApp) or at Near-RT RIC. Among others, the AI/ML models' functionality can include prediction of future traffic, user mobility, and resource usage and can also predict expected energy efficiency enhancements, resource usage, and network performance for different ES optimization states. Before switching off/on carrier(s) or cell(s), the E2 node can perform some preparation actions for off switching (e.g., to enable, disable, modify carrier aggregation and/or dual connectivity, to trigger HO traffic and UEs from cells/carriers to other cells or carriers, informing neighboring nodes via $\mathrm { X } 2 / \mathrm { X n }$ interface etc.) as well as for on switching (e.g., cell probing, informing neighboring nodes via X2/Xn interface etc.).

# 4.21.3.1.1 Solution 1: rApp-based solution (O1-based)

The following entities are applicable to this solution: Energy saving rApp, Non-RT RIC/SMO framework, E2 node(s) and O-RU node(s).

A solution for carrier and cell switch off/on: use case through rApp-based solution is captured in table 4.21.3.1.1-1.

Table 4.21.3.1.1-1: Carrier and cell switch off/on: AI/ML inference via Non-RT RIC   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable carrier and cell switch off/on energy saving functions in thenetwork by means of configuration parameter change and actionscontrolled by Non-RT RIC and allow for Al/ML-based solutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">1) Energy saving rApp2)Non-RT RIC/SMO framework3) E2 node(s)4)O-RU node(s)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O1 interface connectivity is established towards E2 nodes, Non-RT RICand SMO.Open FH M-plane interface is established between E2 node and O-RUand/or SMO and O-RU directly.Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Operator has set the targets for energy saving functions in the Non-RTRIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator enables the optimization functions for carrier and cell switchoff/on energy saving functions and E2 node and O-RU becomeoperational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">SMO initiates specific measurement data collection request towards E2node and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">E2 node and O-RU send the configured measurement data to SMOperiodically or event based.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Energy saving rApp retrieves the collected measurement data forprocessing.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Energy saving rApp constantly monitors(i) performance and energy consumption of the E2 node(s)(ii） energy consumption of O-RU(s)(ii) cell utization and throughput metricsrApp determines configuration changes for carrier(s) and cell(s) switchoff/on use case. Al/ML inference may be used to make the decision.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Energy saving rApp requests Non-RT RIC/SMO framework to makeconfiguration changes to E2 node(s) and O-RU(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">SMO instructs E2 node via O1 interface to apply the received request(s)for configuration changes from the rApp. O-RU is informed about theupdated O-RU configuration via open FH M-plane interface either by E2node, or by SMO directly. E2 node / O-RU notify SMO once cellor carrierswitch off/on is completed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Energy saving rApp continuously analyzes energy saving objectives and if energy saving objectives are not achieved, it can decide to initiatefallback mechanism, for example, reverting changes over O1 interfacefor carrier and cell switch off/on optimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">E2 node becomes non-operational or when the operator disables theoptimization functions for energy saving.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Non-RT RIC continues close loop monitoring of energy saving functionat E2 node and O-RU.E2 node(s) and O-RU(s) operate using the configuration provided by theenergy saving rapp via Non-RT RIC/SMO framework.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the carrier and cell switch off/on using O1-based solution is given in figure 4.21.3.1.1-1.

![](images/8edf56ffd6fa7d0f61837299e5331f2aad06940539902a37891ff1de425f0ef6.jpg)

> **Image Summary:** {"image": "https://i.imgur.com/wzL8Q9c.png"}
  
Figure 4.21.3.1.1-1: Carrier and cell switch off/on flow diagram: AI/ML inference via Non-RT RIC

# 4.21.3.1.2 Solution 2: rApp and xApp-based solution (A1 and E2-based)

The following entites are applicable to this solution: Energy saving rApp, Non-RT RIC/SMO framework, Near-RT RIC, E2 node and O-RU node.

A solution for carrier and cell switch off/on through rApp and xApp-based solution is captured in table 4.21.3.1.2-1.

Table 4.21.3.1.2-1: Carrier and cell switch off/on: AI/ML inference via Near-RT RIC   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Enable carrier and cell switch off/on energy saving functions in thenetwork by means of configuration parameter change and actionscontrolled by Near-RT RIC and allow for AlI/ML-based solutions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">1)Energy saving rApp2)Non-RT RIC/SMO framework3)Near-RT RIC4)E2 node(s)5)O-RU node(s)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">O1 interface connecting the SMO with E2 node and Near-RT RIC isestablished.E2 interface connectivity is established between E2 node and Near-RTRIC.A1 interface is established between Non-RT RIC and Near-RT RIC.Open FH M-plane interface is established between E2 node(s) and O-RU(s).Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Operator has set the targets for energy saving function in the Non-RTRiC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator enables the optimization functions for carrier and cell switchoff/on energy saving functions and E2 node and O-RU becomeoperational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">SMO initiates specific measurement data collection request towards E2node and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">E2 node and O-RU send the configured measurement data to SMOperiodically or event based.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Energy saving rApp retrieves the collected measurement data forprocessing</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Energy saving rApp constantly monitorsi)      performance and energy consumption of the E2 node(s)in)     energy consumption of O-RU(s)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Energy saving rApp determines A1 policy for carrier(s) and cell(s) switchoff/on use case. Al/ML model inference may be used to make thedecision.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">rApp requests A1 policy function to create or update A1 policy for energysaving.A1 policy function requests Near-RT RIC to create or update A1 policyfor energy saving.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Near-RT RIC constantly monitors(i) performance and energy consumption of the E2 node(s)(ii) energy consumption of O-RU(s)Based on the optional Al/ML inference, and considering A1 policies, theNear-RT RIC can request the E2 node to prepare and execute cell orcarrier switch offon. E2 node can request O-RU node to prepare andexecute cell or carrier switch off/on. E2 node will notify Near-RT RIConce cell or carrier switch of/on is completed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Non-RT RIC/rApp and/or Near-RT RIC/xApp monitor energy savingobjectives (with possible actions, e.9g., update of A1 policy, fallback).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">E2 node becomes non-operational or when the operator disables theoptimization functions for energy saving.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">E2 node and O-RU operate using configuration provided by the Near-RT RIC over E2 interface.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the carrier and cell switch off/on using A1 and E2-based solution is given in figure 4.21.3.1.2-1.

![](images/aeb732b8a8f9a7bf79874451d1d76b1e2ebb6385bb2a32706584ea95746ba117.jpg)

> **Image Summary:** {"image": "image.png"}


![](images/61a3a40461e72335238dae2aeb49829891d5739777ec7dbf7d943e8b271dc436.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.21.3.1.2-1: Carrier and cell switch off/on flow diagram: AI/ML inference via Near-RT RIC

# 4.21.4 Required data

# 4.21.4.1 Carrier and cell switch off/on

# 4.21.4.1.1 Solution 1: rApp-based solution

The data requirements for this solution are specified below. The input data specified in table 4.21.4.1.1-1 shall be supported by the associated interfaces specified in the table.

Table 4.21.4.1.1-1: Required input data for energy saving use case   

<table><tr><td>Requirement</td><td>Category</td><td>Parameters / Measurements</td><td>Source</td><td>Reference</td><td>Interface</td></tr><tr><td>Req-4.21.001</td><td>Network load and data performance</td><td>DL PDCP SDU data volume per interface (data volume in DL delivered from O-CU-UP to O-DU, per PLMN, per QoS level, per slice, per interface (F1-U, Xn-U, X2-U))</td><td>O-CU</td><td>3GPP TS 28.552 [6], clause 5.1.3.6.2.3</td><td>01</td></tr><tr><td>Req-4.21.002</td><td>Network load and data performance</td><td>UL PDCP SDU data volume per interface (data volume in UL delivered to O-CU-UP from O-DU, per PLMN, per QoS level, per slice, per interface (F1-U, Xn-U, X2-U)</td><td>O-CU</td><td>3GPP TS 28.552 [6], clause 5.1.3.6.2.4</td><td>01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.003</td><td colspan="1" rowspan="1">Network loadand dataperformance</td><td colspan="1" rowspan="1">DL Total PRB Usage</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]，clause 5.1.1.2.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.004</td><td colspan="1" rowspan="1">Network loadand dataperformance</td><td colspan="1" rowspan="1">UL Total PRB Usage</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]，clause 5.1.1.2.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.005</td><td colspan="1" rowspan="1">Network loadand dataperformance</td><td colspan="1" rowspan="1">Mean number of Active UEs, per cell(and optionally per PLMN, per slice)</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]clause5.1.1.23.5</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.006</td><td colspan="1" rowspan="1">Network loadand dataperformance</td><td colspan="1" rowspan="1">Average DL UE throughput in gNBper cell (and optionally per PLMN, perQoS level, per slice)</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552[6]clause 5.1.1.3.1</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.007</td><td colspan="1" rowspan="1">Network loadand dataperformance</td><td colspan="1" rowspan="1">Average UL UE throughput in gNBper cell (and optionally per PLMN, perQoS level, per slice)</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]，clause 5.1.1.3.2</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.008</td><td colspan="1" rowspan="1">UEmeasurement</td><td colspan="1" rowspan="1">RSRQ measurement per SSB per cell</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]，clause 5.1.1.31</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.009</td><td colspan="1" rowspan="1">UEmeasurement</td><td colspan="1" rowspan="1">RSRP measurement per SSB per cell</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552[6]clause 5.1.1.22</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.010</td><td colspan="1" rowspan="1">UEmeasurement</td><td colspan="1" rowspan="1">SINR measurement per SSB per cell</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]，clause 5.1.1.32</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.011</td><td colspan="1" rowspan="1">Energyconsumption</td><td colspan="1" rowspan="1">Energy consumption</td><td colspan="1" rowspan="1">O-DU,O-RU</td><td colspan="1" rowspan="1">3GPP TS28.552 [6]clause5.1.1.19.3</td><td colspan="1" rowspan="1">01,Open FHM-plane</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.012</td><td colspan="1" rowspan="1">Energyconsumption</td><td colspan="1" rowspan="1">Power consumed by physical networkfunction &amp; its components</td><td colspan="1" rowspan="1">O-DU,O-RU</td><td colspan="1" rowspan="1">3GPP TS28.552[6]clause5.1.1.19.2 andinO-RAN.WG4.MP[28], clausesB.1,B.5</td><td colspan="1" rowspan="1">01,Open FHM-plane</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.013</td><td colspan="1" rowspan="1">Energyconsumption</td><td colspan="1" rowspan="1">Transmit power</td><td colspan="1" rowspan="1">O-RU</td><td colspan="1" rowspan="1">0-RAN.WG4.MP[28], clausesB.1, B.2.1</td><td colspan="1" rowspan="1">01,Open FHM-plane</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.014</td><td colspan="1" rowspan="1">Topology</td><td colspan="1" rowspan="1">Site location and orientation per cellsiteLatitude, siteLongitude, Azimuth /orientation</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3GPP TS28.623 [40]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.21.015</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">Carrier frequency per cellarfcnDL</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.541 [5]，clause 4.3.6</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.016</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">Carrier bandwidth per cell</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.541 [5]，clause 4.3.6</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.21.017</td><td colspan="1" rowspan="1">Configuration</td><td colspan="1" rowspan="1">cellState</td><td colspan="1" rowspan="1">O-DU</td><td colspan="1" rowspan="1">3GPP TS28.541 [5]，clause 4.4.1</td><td colspan="1" rowspan="1">01</td></tr></table>

The output data specified in table 4.21.4.1.1-2 shall be supported by the associated interfaces specified in the table.

Table 4.21.4.1.1-2: Required output data for O1-based solution   

<table><tr><td rowspan=1 colspan=1>Requirement</td><td rowspan=1 colspan=1>Category</td><td rowspan=1 colspan=1>Parameters / Measurements</td><td rowspan=1 colspan=1>Target</td><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>Interface</td></tr><tr><td rowspan=1 colspan=1>Req-4.21.018</td><td rowspan=1 colspan=1>Carrier(s) orcell(s) indicatedfor energy savingaction</td><td rowspan=1 colspan=1>CESManagementFunction</td><td rowspan=1 colspan=1>O-CU</td><td rowspan=1 colspan=1>3GPP TS28.541 [5],clause 4.3.63</td><td rowspan=1 colspan=1>01</td></tr></table>

# 4.22 MU-MIMO optimization

This use case provides motivation, description, and requirements for a near-real-time MU-MIMO optimization control loop deployment. Deploying MU-MIMO application in the Near-RT RIC enables new solutions that can optimize UE and cell level performance in certain deployments by e.g. deriving channel estimation/prediction and UEs selections with their associated precoding coefficients, resulting in increased per UE and overall cell throughput.

# 4.22.1 Background and goal of the use case

MU-MIMO is one of the key technologies available for increasing UE and cell capacities using existing time/frequency resources. The use of multiple antennas enables the pointing of beams to multiple UEs with each beam spatially filtering the interference from the other beams. This has the potential to provide higher total cell capacity when there are multiple $\mathrm { e N B } / \mathrm { g N B }$ antennas.

In a commercial deployment, some subscribers can be stationary, some can be pedestrian moving slowly, and some can be moving at high speed. Traditional MU-MIMO solutions are very sensitive to subscriber’s mobility and as a result the capacity gains achieved with multiple antennas is limited.

New beamforming solutions are emerging that support MU-MIMO with less time sensitivity allowing them to be implemented in the Near-RT RIC. These solutions are applicable to both downlink and uplink data channels and to TDD as well as FDD and can provide high user and cell performance for subscribers moving within a wide range of speeds.

The objective of this use case is to allow the operator to improve user throughput and overall cell capacity by deploying an application in the Near-RT RIC that can use information collected from the E2 nodes to calculate and send to the E2 nodes user selections and applicable precoding coefficients in a near real time loop. This use case will also open the door for future expansion of the MU-MIMO to supporting CoMP covering both ICIC and joint multi sites MU-MIMO.

# 4.22.2 Entities/resources involved in the use case

1) Near-RT RIC

a) Retrieve cell configuration and UE states from E2 nodes   
b) Send configurations for DL channel estimation reporting and UL SRS and DMRS to the E2 nodes   
c) Retrieve DL/UL traffic, and DL/UL channel quality information from E2 nodes   
d) Use the retrieved information to select the UEs to be spatially multiplexed per frequency and time resources and for each selection calculate the relevant MCS and precoder coefficients for optimal UE and cell throughput   
e) Send the recommended UE selections with their resource assignments, MCS, and precoding coefficients to the E2 nodes.

2) E2 nodes

a) Collect and report to Near-RT RIC information related to cell configuration, UE states, DL/UL traffic, and DL/UL channel quality.   
b) Apply the configurations received from the Near-RT RIC for DL channel estimation reporting and UL SRS transmissions   
c) Apply MU-MIMO parameters following Near-RT RIC recommendations (while handling time critical events separately).

# 4.22.3 Solutions

# 4.22.3.1 MU-MIMO optimization

The context of MU-MIMO optimization is captured in table 4.22.3.1-1.

Table 4.22.3.1-1: MU-MIMO optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">MU-MiMO optimization using Near-RT RIC control loop.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Near-RT RIC: Configures E2 nodes' measurements, collects data fromE2 nodes, performs MU-MIMO optimization function, and sends MIMOrecommendations to E2 nodes.E2 nodes: Report measurements to Near-RT RIC and execute MU-MIMO recommendations.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">E2 connectivity is established between Near-RT RIC and E2 nodes.Network is operational.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated. MU-MIMOoptimization xApp is deployed with initial configurationAll relevant subscriptions established on E2 interface .</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Pre-conditions are met.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Near-RT RIC initiates data collection from E2 nodes (cell configuration,UE states, RRC connection, UL/DL traffic and channel information).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">E2 nodes send cell configuration, UE states, and RRC connectioninformation to Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">E2 nodes send UL/DL traffic and channel information to Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">Near-RT RIC sends DL channel estimation reporting and UL SRS andDMRS configuration to E2 nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">E2 nodes continuously send UL/DL trafic and channel information toNear-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">E2 nodes send updated UE states and RRC connections information toNear-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Near-RT RIC uses the collected information to estimate channels andselect UE groupings per ranges of frequency and time resources</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">Near-RT RIC calculates MCS and precoding coefficients for eachselection of UEs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Near-RT RIC sends optimized MU-MIMO parameters (UE selectionswith their resource assignments, MCS, and precoding coefficients) to E2nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">E2 nodes schedule MU-MIMO transmissions using the parametersreceived from the Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (0)</td><td colspan="1" rowspan="1">Near-RT RIC sends updated DL channel estimation reporting and ULSRS and DMRS configuration to E2 nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator disables or uninstall MU-MiMO optimization xApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The E2 nodes operate using the newly received parameters.</td><td colspan="1" rowspan="1">[</td></tr></table>

The flow diagram of MU-MIMO optimization is given in figure 4.22.3.1-1.

![](images/33abef19cc8ef8cc666ee925faa06d01d5f60d3e6c55aa793cfe9ad95b3ff96c.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.22.3.1-1: MU-MIMO optimization flow diagram

# 4.22.4 Required data

The Near-RT RIC requires different types of data from the E2 nodes as summarized below with examples:

1) Cell configuration information (e.g., frequency and BW, FDD/TDD, SCS, UL-DL configuration)   
2) List of connected UEs   
3) UE connection updates (setup, release, handover)   
4) UE RRC state changes (connected, inactive, idle)   
5) UL channel information (e.g., SRS, ACK/NACK counts)   
6) DL channel information (e.g., CQI, RI, PMI, ACK/NACK counts)   
7) DL PDCP and RLC buffer status and UL BSR

# 4.23 Sharing Non-RT RIC data with the core Void

# 4.24 Industrial vision SLA assurance

This use case provides the background and motivation for the O-RAN architecture to support industrial vision ServiceLevel Agreement (SLA) assurance. Moreover, some high-level description and requirements over Non-RT RIC, A1 and E2 interfaces are introduced.

# 4.24.1 Background and goal of the use case

Industrial vision is an image recognition technology used for work piece inspecting, processing and assembling automation, as well as the monitoring and controlling of production process by replacing human eyes with cameras for various measurements and judgments. The main feature of industrial vision system is that it needs to collect the images of the products to be tested or processed in the area with dense production lines, and then transmit the images to the vision server for detection and feed back the results.

Because the industrial vision system shall accommodate to the production speed of the production line, there are strict delay and reliability requirements for visual acquisition, transmission, judgment and execution. For example, a production line which processes 8000 work pieces per hour has an operation interval of 450ms for each product in the production line. Considering the image recognition, results execution time and the mechanical execution time, the two-way data transmission delay left for the transmission network is even less. When 5G is applied in the industrial vision business scenario, the main challenge is the assurance of image data transmission delay and reliability of 5G wireless network in an ultra-dense networking environment.

5G pre-scheduling technology is introduced to reduce the transmission delay and improve the transmission reliability. However, the traditional static pre-scheduling mechanism could not adapts to changing production environments. It always allocates fixed air interface resource according to the static configuration, regardless of the actual data arrival, resulting mis-alignment of resource allocation and uplink transmission needs, causing increased and unstable delay, waste of PRB resources and significant decline in the actual bearable traffic of the cell.

Therefore, dynamic pre-scheduling, which allocates uplink resources according to actual work piece arrival time, is deemed to be a more efficient way to enable industrial vision deployment in production line. In O-RAN, RIC can be used to dynamically optimize the pre-scheduling parameters, so that accurate matching between uplink data arrival and uplink transmission resource allocation could be achieved. This helps to reduce uplink transmission delay and improve the resource efficiency.

With enrichment information from application server/Manufacturing Execution System (MES), e.g., production-line and industrial camera configuration and image transmission delay related data, Near-RT RIC can calculate and iteratively update pre-scheduling parameter (e.g., pre-scheduling data size, pre-scheduling period and pre-scheduling start time), and send those parameters to E2 nodes vis E2 interface. Note that the configured parameters mentioned above only serve as scheduling recommendations to E2 nodes. Actual PRB scheduling depends on many other factors not captured by this use case. E2 node might for instance supersede Near-RT RIC’s recommendation in case high priority delay critical data needs to be scheduled.

One example method to transmit Non-RAN application server/MES data into Non-RT RIC is through SMO external interface. Application server/MES is registered as SMO external system, which serves as a data source outside the ORAN domain that provides data to the SMO. By leveraging SMO external interface (the interface between the SMO and an SMO external system), production-line and industrial camera configuration and image transmission delay related data is transmitted to SMO as enrichment information, which is consumed by Non-RT RIC and bypassed to Near-RT RIC through A1.

# 4.24.2 Entities/resources involved in the use case

1) Non-RT RIC:

a) Support communication of non-RAN data to enrich control functions in Near-RT RIC (enrichment information).

2) Near-RT RIC:

a) Support communication of pre-scheduling configuration parameters to E2 node.

3) E2 node:

a) Support pre-scheduling parameters configuration over E2 interface.   
b) Report necessary performance, configuration, and other data for performing pre-scheduling parameter configuration in the Near-RT RIC over E2 interface.

4) Application server/ MES:

a) Support communication of non-RAN data about production line information and data transmission information to Non-RT RIC as enrichment information.

# 4.24.3 Solutions

The context of industrial vision assurance is captured in table 4.24.3-1.

Table 4.24.3-1: Industrial vision assurance

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Meeting industrial vision service SLA requirement via dynamic pre-scheduling parameter configuration.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, E2 node, application server/ MES</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1, E2 interface connectivity is established.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.E2 interface is established between Near-RT RIC and E2 node.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Production line is started. Periodical industrial vision service is started.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">MES sends the production-line and industrial camera configuration relateddata to the Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">The Non-RT RIC sends the enrichment information to the Near-RT RICover the A1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Based on the received production-line and industrial camera configurationrelated enrichment information from the Non-RT RIC over the A1 interface,the Near-RT RIC sends initial time-domain pre-scheduling parameters,which includes pre-scheduling data size, pre-scheduling period and pre-scheduling start time, to the E2 node.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Industrial vision application server sends the image data transmissiondelay related enrichment data to the Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">The E2 node and the Non-RT RIC sends service data transmission information, which includes relevant measurement (e.g., pre-schedulingtime-domain resource utization which is the ratio of the time-domainresource of the data to be scheduled to the total pre-scheduled time-domain resource, and the image data transmission delay relatedenrichment information) to the Near-RT RIC.Near-RT RIC receives the service data transmission information and thenbased on those information, evaluates the performance of the pre-scheduling and iteratively updates pre-scheduling start time. Then theNear-RT RIC sends the updated pre-scheduling start time to the E2 nodeover E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Based on the pre-scheduling data size, pre-scheduling period and pre-scheduling start time received from the Near-RT RiC, E2 node pre-schedules the time-domain resource for the terminal device. Repeat step4, 5, 6 until the situation in step "Ends when" is met.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">When the industrial vision service data transmission information (includingpre-scheduling time-domain resource utization fed back from E2 nodeand the image data transmission delay related enrichment informationfrom the Non-RT RIC) becomes stable within reasonable range, the Near-RT RIC stops updating the pre-scheduling start time.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td>Post Conditions</td><td>The Non-RT RIC monitors the service performance by collecting and monitoring the relevant performance KPIs and counters from the RAN and the application server.</td><td></td></tr></table>

The flow diagram of industrial vision assurance use case is given in figure 4.24.3-1.

![](images/de5e53221079aa30d076dfc4336f5c070a7dcf17f10e9649ea287bec19b27298.jpg)

> **Image Summary:** {"image": "image_of_5g_oran_specification.png"}
  
Figure 4.24.3-1: Industrial vision assurance use case flow diagram

# 4.24.4 Required data

Enrichment information are expected to be retrieved by Non-RT RIC for industrial vision SLA assurance. Service data transmission information from E2 node are also expected to be collected by Near-RT RIC for industrial vision assurance.

1) Enrichment information:

a. Production-line and industrial vision camera configuration related data, e.g. production line speed, image color, pixel. (collected from application server/MES)   
b. Service-related performance measurement metrics collected from application server, e.g., image data transmission delay. (collected from application server/MES)

2) Service data transmission information: e.g., pre-schedule time-domain resource utilization, which is the ratio of the time-domain resource of the data to be scheduled to the total pre-scheduled time-domain resource. (new E2 measurements)

# 4.25 Void

# 4.26 Interference detection, prediction and optimization

This use case provides the background and motivation for the O-RAN architecture to support real-time interference detection and optimization. Moreover, some high-level description and requirements over Non-RT RIC, A1, Near-RT RIC and E2 interfaces are introduced.

# 4.26.1 Background and goal of the use case

LTE and 5G network are deployed based on co-frequency networking due to limited radio resources, which leads to cofrequency interference becoming the bottleneck of network performance. Heterogeneous networks as well as ultra-dense networks make inter-cell interference more complex. As a result, how to detect and/or predict, and then optimize interference is of great importance for wireless networks. Current research mainly focuses on a class of interference optimization solutions called Inter-Cell Interference Coordination (ICIC), which includes static ICIC and dynamic ICIC, assuming that inter-cell interference is available via detection and/or prediction. The principle of ICIC is to restrict the use of radio resources in individual cells in an inter-cell coordination manner, including restricting which time-frequency resources are available, or limiting their transmitting power on certain time-frequency resources. The principle of ICIC is to divide all cells in the network in several categories, then divides the UE to Cell Edge User (CEU) as well as Cell Center User (CCU), and schedule CEU to edge radio resources.

Such ICIC solutions suffer from the following limitations:

The radio resources are allocated statically or in non-real-time, and do not support dynamic adjustment, which causes low radio resource utilization. ICIC depends on specific ideal cell networking structure, and the performance of interference optimization algorithm is poor for complex networking structure. • The radio resource allocation is based on cell level, and do not support UE level or UE group level. The measurement data is used for post-interference analysis and optimization, with low real-time.

Besides, current research may mainly focus on interference optimization, based on the assumption that inter-cell interference is available via detection and/or prediction. In fact, interference detection and prediction is not less important than interference optimization. On the one hand, interference detection and/or prediction with high accuracy contributes to accurate and efficient interference optimization. On the other hand, interference detection and/or prediction can be utilized to optimize other transmission configurations, e.g., Modulation and Coding Scheme (MCS), not limited to radio resources allocation.

Thanks to the open interface and intelligent functionalities provided by the O-RAN architecture, multi-cell-based collaborative real-time interference detection, prediction and interference optimization schemes can be realized. Multidimensional data, e.g., network level measurement data, can be acquired and used for interference detection, interference prediction, interference relationships construction, and interference optimization in real time. Interference relationship construction can further take QoS related metrics into analysis, to facilitate UE service assurance through interference management. Based on the A1 policy as well as interference relationships, Near-RT RIC ensures optimal radio resource allocation for UE or UE group or RAN slice or PRBs or mMIMO beams through E2 interface towards RAN for interference optimization. In addition, based on the history interference detection, Near-RT RIC can predict interference for future data transmissions and thus facilitates MCS optimization for UE to adapt to fluctuating interference.

# 4.26.2 Entities/resources involved in the use case

1) SMO/Non-RT RIC:

a) Generate and send interference detection, prediction and optimization policies to Near-RT RIC.   
b) Retrieve QoS related metrics and send to Near-RT RIC.   
c) Receive interference detection, prediction and optimization performance evaluation updates from Near-RT RIC.   
d) Receive interference related network level measurement data from gNBs.   
e) Generate and send radio resources configuration based on the interference optimization policy to E2 nodes.

2) Near-RT RIC:

a) Retrieve necessary interference related measurement metrics from network level (cell level) measurement report through E2 interface.

b) Receive interference detection, prediction and optimization polices from Non-RT RIC, and support interpretation and execution of Non-RT RIC policies to derive the interference detection, prediction and optimization control or policy.   
c) Send the controls or policies to E2 nodes through E2 interface for interference detection, prediction and optimization.   
d) Send interference performance report to Non-RT RIC for evaluation and optimization

3) E2 node:

a) Support network state and UE measurements with required granularity to Near-RT RIC over E2 interface.   
b) Support interference configurations and enhancements based on messages from E2, which are expected to influence RRM behavior.   
c) Receive interference detection, prediction results from UE and network, and report to Near-RT RIC.   
d) Update RAN parameters based on radio resources configuration from the SMO/Non-RT RIC over the O1 interface.

# 4.26.3 Solutions

# 4.26.3.1 Fast loop optimization

# 4.26.3.1.1 Interference detection

The context of the interference detection is captured in table 4.26.3.1.1-1.

Table 4.26.3.1.1-1: Interference detection   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Interference detection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.A1/01 interface connectivity is established with Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Near-RT RIC triggers interference detection.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1-2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC generates interference detection policy and sends the policyto Near-RT RIC via A1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Near-RT RIC receives A1 policy, converts and generates E2 control orpolicy. E2 control or policy includes: 1) allocated resource(s) of thereference signal for the gNB(S); 2) Information transmission strategyconfigured for the intra-frequency cells adjacent to the cells correspondingto the gNB(S); 3) information for UL PRBs to be monitored; 4) for example,for mMIMO deployment scenario, information for mMIMO beams to bemonitored.The reference signal can be NZP CSI-RS and ZP CSl-IM, which is usedby UE(S) accessed in the gNB(S) for channel measurement, channelestimation and interference measurement respectively:a) For channel measurement and channel estimation referencesignal: based on the Information transmission strategy, intra-frequency cell adjacent to the cells corresponding to the gNB(S),</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">such as the cells corresponding to gNB(N), keep silent at theallocated resource(s) of the reference signal.b) For interference measurement reference signal: based on theInformation transmission strategy, intra-frequency cells adjacentto the cells corresponding to the gNB(S), such as the cellscorresponding to gNB(N), can send data at the allocatedresource(s) of the reference signal.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4, 6 (M)</td><td colspan="1" rowspan="1">Near-RT RIC sends E2 control or policy to the target gNBs via E2 interface,such as sending allocated resource(s) of the reference signal for thegNB(S), sending information transmission strategy to the intra-frequencycells adjacent to the cells corresponding to the gNB(S), for example thecells corresponding to gNB(N), and sending information for UL PRBs andfor mMIMO deployment scenario mMIMO beams to be monitored.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5,7 (M)</td><td colspan="1" rowspan="1">gNB(S) allcates resources for reference signal based on the E2 controlor policy. gNB(N) allocates resources for DL data transmission to UE(N).gNB(N) allocates resources for UL data transmission.gNB(S) allocates resources for UL PRBs and for mMiMO deploymentscenario mMIMO beams to be monitored.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8-10 (M)</td><td colspan="1" rowspan="1">gNB(S) sends reference signal at allocated resources to UE(S). UEdetects interference based on the reference signal configured by gNB(S)and sends the interference detection results to the Near-RT RIC throughRAN.gNB(S) detects uplink interference based on interference levels andpatterns of UL PRBs among intra-frequency cells and sends theinterference detection results to the Near-RT RIC.gNB(S) detects interference levels of mMIMO beams among intra- frequency cells and sends the interference detection results to the Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11-20 (O)</td><td colspan="1" rowspan="1">Ifrequired, Near-RT RIC can configure specific performancemeasurement data to be collected from RAN to monitor the performanceof E2 control or policy and sends the result to Non-RT RIC for updating theA1 and E2 policies based on the performance evaluation results.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator triggers to stop interference detection.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the interference detection is given in figure 4.26.3.1.1-1.

![](images/324fc7ec204f324542474903850fb6bd928f5e8b83b9ceedc065a10efe73073e.jpg)

> **Image Summary:** {"image": "image_3.png"}
  
Figure 4.26.3.1.1-1: Interference detection flow diagram

# 4.26.3.1.2 Interference relationships construction

The context of the interference relationships construction is captured in table 4.26.3.1.2-1.

Table 4.26.3.1.2-1: Interference relationships construction   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Interference relationships construction</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Near-RT RIC, gNB</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.E2 interface connectivity is established with Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Interference detection results have been sent to Near-RTRIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Near-RT RIC triggers interference relationship construction.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1-4 (M)</td><td colspan="1" rowspan="1">QoS related metrics from SMO and network levelmeasurements reported by RAN through E2 interface arereported to Near-RT RIC for instantiating or modifyinginterference relationships.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Near-RT RIC constructs interference relationships (e.g.,interference graph) based on the received QoS relatedmetrics from SMO and network level measurement fromRAN.Near-RT RIC constructs uplink interference relationshipsamong intra-frequency cells based on the interference levelsand patterns of UL PRBs.Near-RT RIC constructs interference relationships amongmMIMO beams located at different intra-frequency cellsbased on interference levels of mMIMO beams.Near-RT RIC uses interference relationships for furtherinterference optimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6-8 (0)</td><td colspan="1" rowspan="1">If required, Near-RT RIC can configure specific performancemeasurement data to be collected from RAN to assess theperformance of the interference relationships and update theinterference relationships in Near-RT RIC based on theperformance evaluation and model retraining.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">Near-RT RIC stores the interference relationships forinterference optimization function in Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the interference relationships construction is given in figure 4.26.3.1.2-1.

![](images/9fc22fec4c5491d9cdd09c17261f704aa1663d4254222729f4e4426906cf91b6.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.26.3.1.2-1: Interference relationships construction flow diagram

# 4.26.3.1.3 Interference optimization

The context of the interference optimization is captured in table 4.26.3.1.3-1.

Table 4.26.3.1.3-1: Interference optimization   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Interference optimization policy generation and performanceevaluation</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Non-RT RIC, Near-RT RIC, SMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated.A1/01 interface connectivity is established with Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>Interference relationships required by interference optimizationhave been constructed by Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The network operator/manager want to generate interferenceoptimization policy based on user QoS.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>Non-RT RIC generates the appropriateinterferenceoptimization policy based on the configured QoS parameters.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>Non-RT RIC sends the interference optimization policy to Near-RT RIC via A1 interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Network level measurements reported by RAN through E2 interface are reported to Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Near-RT RIC receives the policy from the Non-RT RIC over theA1 interface and measurement data from the RAN over the E2anaerface.Near-RT RIC generates radio resourcesconfiguration based on the interference relationships (e.g. interference graph) as well as A1 policy.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>Near-RT RIC sends the radio resources configuration throughE2 interface towards RAN for interference optimization. RANenforces the received control or policy from the Near-RT RICover the E2 interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6-12 (O)</td><td rowspan=1 colspan=1>If required, Non-RT RIC can configure specific performancemeasurement data to be collected from RAN to assess theperformance of the QoE optimization function in Near-RT RIC,or to assess the outcome of the applied A1 policies. And thenupdate A1 policy and E2 control or policy.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Operator specified trigger condition or event is satisfied.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>If required, Near-RT RIC can configure specific performancemeasurement data to be collected from RAN to monitor theperformance of E2 control or policy and sends the result to Non-RT RIC for updating the A1 and E2 policies based on theperformance evaluation results.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the interference optimization is given in figure 4.26.3.1.3-1.

![](images/81af1048d4c7ffa76f05be27bb7e7936e27171b3c35a2cb970bd688e1b414c78.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.26.3.1.3-1: Interference optimization flow diagram

# 4.26.3.2 Slow loop optimization

# 4.26.3.2.1 Interference detection and relationships construction

The context of the interference detection and relationships construction is captured in table 4.26.3.2.1-1.

Table 4.26.3.2.1-1: Interference detection and relationships construction   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Interference detection and relationships construction</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO/Non-RT RIC, gNB</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated.01 interface connectivity is established with SMO/Non-RTRIC.SMO/Non-RT RIC has RAN topology including therelationship of geographical location among cells.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>Network level measurement data generated at gNBs through01 interface are reported to SMO/Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>SMO/Non-RT RIC triggers interference detection andrelationship construction.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>SMO/Non-RT RIC collects the interference data and RBusage rate as network level measurement data from gNBs.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>SMO/Non-RT RIC analyzes the interference relationshipamong cells based on the network level measurement dataand the RAN topology. SMO/Non-RT RIC constructsinterference relationships (e.g., interference graph) based onnetwork level measurement data from gNBs. The interference relationships indicate a table for each cell, istingthe neighboring cells that have a significant interferenceimpact.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3-5 (0)</td><td rowspan=1 colspan=1>If required, SMO/Non-RT RIC can update the interferencerelationships based on the network level measurement dataand the RAN topology.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Operator specified trigger condition or event is satisfied.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>SMO/Non-RT RIC stores the interference relationships.</td><td rowspan=1 colspan=1></td></tr></table>

The flow diagram of the interference detection and relationships construction is given in figure 4.26.3.2.1-1.

![](images/fefee8768919fe588bcfd65953483ad024088810df5f709eefa4d414818b9018.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.26.3.2.1-1: Interference detection and relationships construction flow diagram

# 4.26.3.2.2 Interference optimization

The context of the interference optimization is captured in table 4.26.3.2.2-1.

Table 4.26.3.2.2-1: Interference optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Interference optimization policy generation and performanceevaluation</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO/Non-RT RIC, gNB</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated. 01interface connectivity is established with SMO/Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Interference relationships required by interference optimizationhave been constructed by SMO/Non-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The network operator/manager want to generate interferenceoptimization policy based on the interference relationship.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1-2 (M)</td><td colspan="1" rowspan="1">SMO/Non-RT RIC can monitor the pefirmance and creates cellgroups for interference optimization based on the interferencerelationship and network level measurement data</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">SMO/Non-RT RIC generates the appropriate interferenceoptimization policy based on the network level measurementdata. Non-RT RIC creates the radio resources configurationbased on the interference optimization policy for each cellgroup.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">SMO/Non-RT RIC sends the radio resources configurationthrough O1 interface to the cell group. gNBs update the RANparameters based on radio resources configuration from theSMO/Non-RT RIC over the O1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5-7 (0)</td><td colspan="1" rowspan="1">If required, SMO/Non-RT RIC can update the optimizationpolicy based on the network level measurement data and theRAN topology. SMO/Non-RT RIC updates the radio resourcesconfiguration and sends the radio resources configurationthrough O1 interface to the cell group.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator specified trigger condition or event is satisfied.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the interference optimization is given in figure 4.26.3.2.2-1.

![](images/8c7d5995d1298617b08155a3fcb80abc1611c51b67a563c0d5cf2b5cde7f1940.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.26.3.2.2-1: Interference optimization flow diagram

# 4.26.3.3 Intereference prediction for MCS optimization

The context of the interference prediction for MCS optimization is captured in table 4.26.3.3-1.

Table 4.26.3.3-1: Interference prediction for MCS optimization   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Interference prediction and MCS optimization</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">Non-RT RIC, Near-RT RIC, E2 nodes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Near-RT RIC and Non-RT RIC are instantiated with A1 interfaceconnectivity being established between them.E2 nodes and Non-RT RIC are instantiated with E2 interface connectivitybeing established between them.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Non-RT RIC triggers interference prediction.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1-2 (M)</td><td colspan="1" rowspan="1">Non-RT RIC generates interference prediction policy and sends the policyto Near-RT RIC via A1 interface. The policy including neighborhood list ofserving cell prediction granularities and prediction steps, etc.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">I A N C E</td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">Data collection from E2 node(S) for serving cell!:1) Near-RT RIC initiates data collection request to E2 node(S) via E2interface,to request uplink interference reported periodically;2) E2 node(S) collects the uplink interference on each RB in thebandwidth of the serving cell and reports the uplink interference toNear-RT RIC periodically as request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Data collection from E2 node(N) for neighbouring cell!:Neighbouring cell corresponding to E2 node(N) is a intra-frequency celladjacent to the serving cell corresponding to the E2 node(S).1) Data collection to construct uplink interference users set.a. Near-RT RIC initiates data collection request to E2 node(N) via E2interface, to request DL RSRP for the serving cell corresponding to E2node(S) reported periodically.b. E2 node(N) collects the DL RSRP and reports the DL RSRP to Near-RT RIC periodically as request.c. Near-RT RIC constructs the uplink interference users set based onthe DL RSRP. The users with high DL RSRP, whose uplink service maycause more uplink interference to the serving cell corresponding to E2node(S) are included in the set.2) Data collection of uplink interference users in the set.a. Near-RT RIC initiates data collection request to E2 node(N) torequest uplink interference related information (e.g., UL PRB usagerate, PHR, BSR, location and velocity) of users in the set reported.b. E2 node(N) collects the information of users in the set and reportsuplink interference related information to Near-RT RIC as request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">Over multiple historical time periods, the collected uplink interference fromthe serving cell and/or uplink interference related data from theneighbouring cell, could be processed as a training data set for the Al/MLmodel training and/or processed as input data for the Al/ML modelinference.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">Assuming the Al/ML model training using the training data set is on Non-RT RIC or on Near-RT RIC, the trained Al/ML model will be deployed inthe Near-RT RIC used for the AI/ML model inference.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">Near-RT RIC performs Al/ML model inference and outputs the predicteduplink interference value based on the latest input data.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">Near-RT RIC sends the RIC control or policy with the predicted uplinkinterference value to E2 node(S) via E2 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">E2 node(S) could use the predicted uplink interference value for UE(s) tobe scheduled to estimate the uplink channel quality (e.g., SINR) at thefuture PUSCH transmission slot. E2 node(S) could realize this byreplacing the uplink interference collected when the last uplink referencesignal of the scheduled UE(s) is received by E2 node(S).The E2 node(S) then uses the uplink channel quality (e.g., SINR) todecide the MCS in DCI sent to the scheduled UE.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator triggers to stop interference prediction.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

The flow diagram of the interference prediction is given in figure 4.26.3.3-1

![](images/ba9d6cb3241f636616647ff8953c56b766e16e96fee3171f13585b8df6a41133.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.26.3.3-1: Interference prediction flow diagram

# 4.26.4 Required data

Multi-dimensional data are expected to be retrieved by Near-RT RIC for interference prediction, interference relationship generation, and interference optimization, including network level measurement data from O-CU/O-DU, which indicates network status, as well as QoS related metrics from SMO which indicates service requirements.

1) Network level measurement report, including a) UE level information, e.g., CQI, SINR, MCS, UL/DL RSRP, DL/UL PRB usage rate, throughput, DU/UL PRB usage, mMIMO beams, BSR, PHR, location and velocity b) Cell level information: e.g., DL/UL PRB usage rate, throughput, uplink interference

2) QoS related metrics collected from SMO, e.g., 5QI, throughput, latency, packet loss rate, BLER requirement etc.

# 4.27 Communication and computing integrated networks

4.27.1 Background and goal of the use case

# 4.27.1.1 Common aspects & background for communication and computing integrated networks use cases

With the development of 5G and future networks, the integration of communication and computing has become a critical trend in network architecture. Traditional communication networks have focused primarily on data transmission and connectivity, while modern network applications increasingly require substantial computational resources. Examples of these applications include Artificial Intelligence (AI), Augmented Reality (AR), Virtual Reality (VR), autonomous driving, and Industrial Internet of Things (IIoT). These applications not only require high-speed, low-latency communication but also significant computing capabilities for real-time data processing and inference.

The past decades witnessed the convergence of communication and computing trends in mobile network. Great efforts were made and good momentum were achieved. C-RAN featured by centralization, cooperative, clean and cloud were first proposed in 2009, which depicts the vision of software based virtualized RAN [i.1]. The concept of Network Function Virtualization (NFV) was initiated from 2012. It introduced the Information Technology (IT) to enable the network transformation from the traditional physical hardware network into a new software based virtualized network [i.6]. This further steers up the pace for the convergence of communication and computing in RAN. Multiple-access Edge Computing (MEC), which enables compute-intensive applications for mobile devices and access to cloud computing service at the edge of communication networks, had attracted great attention [i.7]. The virtualized/cloudification RAN infrastructure can server as perfect edge computing platform. Thanks to the well-developed IT tools/frameworks, such as the containers, kubernets, the general-purpose hardware infrastructure could be easily and dynamically shared by the RAN functionality and the edge applications, providing the converged capabilities of mobile communication and computing. Edge computing was also incorporated into 5G system in 3GPP since Release 15. However, the communication and computing services offered by the existing design, such as NFV and MEC, were designed separately and developed independently. To fulfill the gap, the coordination of computing and networking is proposed in the context of IMT-2020 and beyond, and provides network enhancements based on the functional architecture of IMT-2020, to achieve the computing and network joint optimization based on the awareness, control and management over computing resources [i.8], [i.9]. Besides the above, IETF initiated a new working group on computing aware traffic steering to study how the network edge can steer traffic between clients of a service and sites offering the services, considering the integrated network and compute resource status [i.10].

The O-RAN ALLIANCE focuses on promoting the openness and intelligence of RAN. Its architecture provides a solid foundation for the integration of communication and computing. O-RAN’s cloud-based architecture (O-Cloud) supports the virtualization of multiple network functions, including RAN functions and edge computing applications. Additionally, O-RAN’s intelligent capabilities—enabled by the Non-RT RIC and Near-RT RIC—allow for the dynamic optimization and management of both communication and computing resources. This flexibility enables O-RAN to meet the requirements of various application scenarios and network conditions.

# 4.27.1.2 Sub-use case 1: Multi-aspect handover optimization

CCIN enables the collaboration of communication network and computing. It is an approach of softening the boundaries between the cloud computing and networking, such that their resources can be utilized in the most efficient way. This allows the applications to leverage on such convergence of compute and network resources. Cloud based RAN solutions can play an important role in the CCIN with its potential to share some of its vacant computing resources as the edge computing platform. New age applications based on XR (see 3GPP TR 26.928 [i.13], clause 4.1.1), V2X (see 3GPP TR 38.885 [i.14]) can benefit from CCIN but they require application mobility in addition to posing stringent requirements on both communication and computing. New network architecture for CCIN needs to address these application requirements.

The types of computing resources required for different applications can be diverse based on the nature of the applications. However, the computing resources available in different entities might be of different computing resource type than what is required for specific applications. It is also possible that capabilities of a computing resource type required for specific applications is different even if an entity supports required computing resource type. Computing resource types referred here could be but not limited to the support for graphical processing unit, neural processing unit, deep processing unit, etc. An example illustration of the cloud based joint RAN $^ +$ computing node used in CCIN is given below in figure 4.27.1.2-1.

![](images/d13d8abdba6cbf99d0d94a26e49f88309a2567c4324b522883db1f9522a0b6a9.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.27.1.2-1: Example illustration of cloud based joint RAN $^ { + }$ computing node

In CCIN, the idea is to use the vacant computing resources from the cloud-based RAN (e.g., if the network load is low), to perform some edge computing related tasks so that cloud resources are used efficiently. In particular, leveraging the proximity of the cloud-based RAN nodes to the end users/devices is a key factor to address low latency requirements of the tasks/applications. But in order to take advantage of this opportunity the following needs to be considered:

If the vacant resources match the task requirements in terms of the type of the computing resource and related capabilities.   
If the amount of vacant resources of required type/capability suffices the task requirements   
If the nodes are within the proximity required to support the continuity of the service and service latency requirements of the applications.

In the use case of UE handover especially in the scenario where the UE needs to run applications with high computing and low latency requirements such as XR based applications the above stated challenges are more prominent. Thus, in such use case it is desirable that system considers the aspects of computing capability and availability of cloud-based RAN nodes while supporting the mobility of UE and applications in it.

In particular, it is important to create the awareness in a cloud-based RAN nodes of the information regarding the computing capability and availability of other cloud-based RAN nodes in the proximity and use these multiple aspects as part of the UE handover decisions. Proximity here means that coverage area of the cells served by source cloud-based RAN node has some overlap with the coverage area of the cells served by target cloud-based RAN node.

In order to address aforementioned use case and related challenges it is proposed to extend the CCIN framework. Such extensions focus on obtaining information about the computing capabilities of cloud-based RAN nodes and utilizing this information in UE handover decisions. This helps the handover of the UE to a target cloud-based RAN node in the proximity with computing resource types of relevant capabilities and availability required for the applications in that UE.

![](images/92f8936d3efe93ee8b786ea4fec00ecabaf98c426f674e99806853f07cfdebc8.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.27.1.2-2: Example illustration of multi-aspect handover

4.27.1.3 Sub-use case 2: RAN edge computing resource information exposure

AI/ML processing for network intelligence and automation evolution, as well as new 5G edge applications supporting e.g., immersive Virtual Reality (VR), autonomous driving, and intelligent Internet of Things (IoT), etc., put an unprecedented demand on the edge computing resources. The O-Cloud architecture of O-RAN and the spatial and temporal tidal effects of RAN communication services offer great opportunities for sharing underutilized computing resources in the RAN infrastructure. This helps to improve resource utilization efficiency and reduce operators’ investment on the edge computing infrastructure.

The main objective is to provide RAN edge computing information exposure service based on O-RAN architecture and its open interface. In O-RAN, SMO is a great candidate to provide RAN edge computing information exposure service to the service consumers for using RAN edge computing capability. This helps service consumer perceive RAN edge computing resources in the O-Cloud infrastructure, such as total, allocated, reserved or available computing capacity. The service consumers might be other orchestrators, e.g., central cloud orchestrator, edge cloud orchestrator, RAN edge cloud orchestrator, device edge cloud orchestrator etc. The orchestrators could request computing information for multi-cloud collaboration, such as task migration between multiple clouds or edge intelligence. The service consumers could also be application servers, e.g., RAN service computing center serving vertical customers, VR consumers, etc., which could request computing information for application deployment using shared computing resources in a secured way.

# 4.27.1.4 Sub-use case 3: O-RAN and mobile devices collaborative AI/ML inference Void

# 4.27.1.5 Sub-use case 4: XR rendering collaboration

Void

# 4.27.1.6 Sub-use case 5: Joint communication and computing optimization for V2X communications

It is expected that there will be approximately 8 million autonomous or semi-autonomous vehicles on the road by 2025 [i.11]. As an enabling technology, Vehicle-to-Everything (V2X) communication is pivotal in paving the way for the intelligent traffic system and autonomous vehicles by facilitating the exchange of crucial information among vehicles, infrastructure, and pedestrians. This exchange encompasses critical data, including real-time updates on traffic conditions, impending road hazards, and precise speed limits, to improve decision-making and prevent accidents.

Within the realm of V2X communications, the intersection is one of the most challenging scenarios. The various ways of transportation (e.g., vehicles, pedestrians) coupled with densely constructed buildings contributes to the complexity of traffic conditions, resulting in a large amount of data gathered from diverse sources for comprehensive sensing and collision avoidance. As shown in figure 4.27.1.6-1, Vehicle 1 travels straight through the intersection, while Vehicle 2 maintains a safe distance behind Vehicle 1, intending to turn left. During the drive, there are several risks.

⚫ Vehicle 1 risks colliding with Vehicle 3.   
Vehicle 1 or Vehicle 3 risks colliding with the pedestrian 2 (if he suddenly rushes from behind Building 2 and turns left). However, either Vehicle 1 or Vehicle 3 cannot sense the pedestrian timely due to the blocking by Building 2.   
Vehicle 2 risks colliding with other vehicles and pedestrians (e.g., Vehicle 3 and pedestrian 1). Due to the blocking by Vehicle 1 and Building 1, Vehicle 2 is unable to accurately sense traffic conditions ahead and to the left in realtime and has to obtain information by exchanging information with other vehicles or infrastructures, which may result in high latency and high risk of collision.

![](images/cee871ce0cd60f9c203cfe6b836079402f03981a725a88f20e71161c49bae3a2.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.27.1.6-1: An illustration of the potential collisions at intersections

In collision warning scenarios, the latency requirement for data collection and computing are in a few milliseconds (e.g., the maximum end-to-end latency for cooperative collision avoidance in the advanced driving scenario is $1 0 \mathrm { m s } .$ .) [i.12], so that the results and warns can be fed back to vehicles and pedestrians in a timely manner. To fulfill the strict latency demand, it is essential to process these tasks in one or several optimal computing nodes, e.g., the central cloud, edge cloud, radio edge cloud, device edge cloud, etc. Since the end-to-end latency is limited by the computing latency and network latency, the optimal offloading choice cannot be found by either optimizing the network or computing resource. Hence, joint optimization of network and computing resources is needed. For example, the road status sensing data from Vehicle 1, Vehicle 3 and Pedestrian 2 must be communicated and processed and the result fed back within milliseconds to avoid the collision between them.

To reduce network latency, it is desirable to process the data locally in vehicles. However, the computing resources of vehicles may be limited, which may not satisfy the task requirements in terms of computing resources and capabilities and could also lead to high computing latency. Therefore, it may be desired to offload all or part of the data processing to the best edge server (e.g., the server completes data processing with the lowest latency, lowest energy consumption.) through joint optimization of network and computing resources. However, since the task requirements on computing resources (e.g., the required type of computing resources) are diverse and the availability of computing resources is dynamic, it is of great importance to enable joint communication and computing resources optimization. What is worse, there are other data to be processed, such as navigation requests from other vehicles, requests for entertainment-related services from passengers, etc., which also consume limited computing and communication resources and increase the difficulties.

The main objective of the use case is to enable joint communication and computing resources optimization for V2X communications. In O-RAN, the global information on communication and computing resources is available over O1 and O2 interface, thus facilitating joint communication and computing resources optimization. With the above global information, resource scheduling policies for both communication and computing can be developed in Non-RT RIC (e.g., policies in terms of CPU frequency, bandwidth and power, etc.), and communication optimization policies can be enforced by Near-RT RIC based on the near-real-time UE level information (e.g., real-time link quality). In addition, the vacant computing resources in O-Cloud can provide edge computing services in case of low network load, which further facilitates the low-latency computing in V2X communications.

# 4.27.1.7 Sub-use case 6: Exposure of performance information to assist computing resource scheduling

Void

# 4.27.2 Entities/resources involved in the use case

# 4.27.2.1 General aspects of entities/resources for communication and computing integrated networks use cases

The following clauses describe the entities/resources that are important and key players for each of the CCIN sub-use cases.

4.27.2.2 Sub-use case 1: Multi-aspect handover optimization

1) SMO/Non-RT RIC framework:

a) Collects necessary CM/PM data from different cloud-based RAN nodes such as O-CU over O1 interface. Collects supported types of computing resources, capabilities of computing resource types, and load/availability of computing resources in different cloud-based RAN nodes such as O-CU over O2 interface.   
b) Provides CM data, PM data, supported types of computing resources, capabilities of computing resource types, and load/availability of computing resources of different cloud-based RAN nodes such as O-CU to rApp over R1 interface.   
c) Provides O1 configurations to Near-RT RIC via O1 interface or A1 policies to Near-RT RIC via A1 interface based on the request from rApp.

2) rApp:

a) Retrieves necessary CM/PM data related to different cloud-based RAN nodes such as O-CU from SMO/Non-RT RIC framework.   
b) Retrieves supported types of computing resources, capabilities of computing resource types, and load/availability of computing resources in different cloud-based RAN nodes such as O-CU from SMO/Non-RT RIC framework.   
c) Derives the proximal computing capabilities and availability information (e.g., represented in tabular formats) for each cloud-based RAN node, use this information to create related O1 configurations or A1 policies to support multi-aspect handover optimization in Near-RT RIC.

3) Near-RT RIC:

a) Performs multi-aspect handover optimization based on the O1 configurations or A1 policies received.   
b) Sends E2 control or E2 policy messages to E2 nodes (O-CU) related to multi-aspect handover optimization.

4) E2 nodes:

a) Support CM data read requests from SMO over O1 interface. Collect and report PM data to SMO over O1 interface.

b) Support UE handover related control and/or policy enforcement from Near-RT RIC over E2 interface.

5) O-Cloud:

a) Support data requests related to supported types of computing resources, capabilities of computing resource types, and load/availability of computing resources of different cloud-based RAN nodes such as O-CU to SMO over O2 interface.

# 4.27.2.3 Sub-use case 2: RAN edge computing resource information exposure

1) SMO:

a) Support collection and analysis of computing related resources from O-Cloud. b) Support RAN edge computing information service, send the RAN computing information for managed O-Cloud related computing resources to the service consumer, e.g., orchestrator/application server.

2) O-Cloud:

a) Support computing related inventory and updated resources report with required granularity to SMO over O2 interface.

3) RAN edge computing information exposure service consumer:

a) Request/subscribe RAN edge computing information from SMO.   
b) The service consumer might be orchestrator/application server.

4.27.2.4 Sub-use case 3: O-RAN and mobile devices collaborative AI/ML inference Void

4.27.2.5 Sub-use case 4: XR rendering collaboration

Void

# 4.27.2.6 Sub-use case 5: Joint communication and computing optimization for V2X communications

1) SMO:

a) Receive available communication and computing resources information from E2 nodes and O-Cloud.   
b) Expose integrated communication and computing service and/or computing service.   
c) Receive integrated communication and computing service requests from external entities.   
d) Generate and send joint communication and computing resource optimization policies.

2) Near-RT RIC:

a) Receive communication resource optimization policies from SMO through A1 interface, and send the policies to E2 nodes over E2 interface. b) Send communication performance report to SMO for evaluation and optimization. c) Retrieve available communication resource information from E2 nodes over E2 interface.

3) E2 nodes:

a) Report available communication resource information with required granularity to SMO over O1 interface.

b) Update RAN parameters based on communication optimization policies from the Near-RT RIC. 4) O-Cloud:

a) Report available computing resource information with required granularity to SMO over O2 interface. b) Receive workload deployment policies and/or computing resource optimization policies from SMO over O2 interface.

# 4.27.2.7 Sub-use case 6: Exposure of performance information to assist computing resource scheduling

Void

# 4.27.3 Solutions

# 4.27.3.1 General aspects of solutions for communication and computing integrated networks use cases

The following clauses describe solutions that apply to each of the CCIN sub–use cases.

# 4.27.3.2 Sub-use case 1: Multi-aspect handover optimization

The context of the multi-aspect handover optimization use case is captured in table 4.27.3.2-1.

Table 4.27.3.2-1: Multi-aspect handover optimization use case   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>Configure and update the proximal computing information for multi-aspect handover optimization.</td><td></td></tr><tr><td rowspan="4">Actors and Roles</td><td>SMO/Non-RT RIC framework: Provide relevant R1 services to enable the rApp to read relevant OAM data, O2 related data and write configuration changes.</td><td rowspan="4"></td></tr><tr><td>rApp: Create related O1 configurations or A1 policies to support multi-aspect handover optimization.</td></tr><tr><td>Near-RT RIC: Performs multi-aspect handover optimization.</td></tr><tr><td>E2 node: Support UE handover related control and/or policy enforcement from Near-RT RIC over E2 interface.</td></tr><tr><td>Assumptions</td><td>O-Cloud: Support data requests related to computing information. Operator has set the targets for multi-aspect handover optimization in the rApp.</td><td></td></tr><tr><td colspan="1" rowspan="1">Pre conditions</td><td colspan="1" rowspan="1">A1/O1 interface connectivity is established with Non-RT RIC.01/02 interface connectivity is established with SMO.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Operator triggers the rApp for multi-aspect handover optimization.rApp is set to periodically monitor network status and computing information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Steps 1-4 (M)</td><td colspan="1" rowspan="1">rApp collects O1 related data using R1 services provided by SMO/Non-RTRIC framework.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5-8 (M)</td><td colspan="1" rowspan="1">rApp collects O2 related data using R1 services provided by SMO/Non-RTRIC framework.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">Create O1 configurations which contain proximal computing capability andavailability information for each O-Cloud based RAN nodes for multi-aspecthandover optimization. Alternatively, create A1 policies which contain proximalcomputing capability and availability information for each O-Cloud based RANnodes for multi-aspect handover optimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">rApp sends O1 configurations or A1 polices for multi-aspect handoveroptimization via R1 interface.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11(M)</td><td colspan="1" rowspan="1">SMO/Non-RT RIC framework sends O1 configurations via O1 interface or A1polices via A1 interface to Near-RT RIC.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12(M)</td><td colspan="1" rowspan="1">Near-RT RIC sends E2 control or E2 policies for multi-aspect handoveroptimization.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Operator stops the rApp.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">E2 node(s) operate using the new configurations/policies.</td><td colspan="1" rowspan="1"></td></tr></table>

<table><tr><td>@startuml</td></tr><tr><td>skin rose</td></tr><tr><td>skinparam ParticipantPadding 5</td></tr><tr><td>skinparam BoxPadding 10</td></tr><tr><td>skinparam defaultFontsize 12</td></tr><tr><td>skinparam lifelineStrategy solid</td></tr><tr><td></td></tr><tr><td>skinparam wrapwidth 300</td></tr><tr><td>autonumber</td></tr><tr><td>box #lightseagreen</td></tr><tr><td></td></tr><tr><td>participant &quot;o-Cloud(s)&quot; as OcLouDs</td></tr><tr><td>endbox</td></tr></table>

box #gold

participant "rApp" as rApp

<table><tr><td></td><td>Participant &quot;sMO / Non-RT RIC Framework&quot; as nonRTRICFramework</td></tr><tr><td colspan="2">endbox</td></tr><tr><td colspan="2">box &quot;O-RAN Nodes&quot; #lightpink</td></tr><tr><td colspan="2">Participant &quot;Near-RT RIc&quot; as NearRTRIC Participant &quot;E2-Node(s)&quot; as RANNodes</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">endbox</td></tr><tr><td colspan="2">group 01 Data Collection</td></tr><tr><td colspan="2">rApp -&gt; nonRTRICFramework : &lt;&lt;Rl&gt;&gt; Data collection request</td></tr><tr><td colspan="2">nonRTRICFramework -&gt; RANNodes : &lt;&lt;O1&gt;&gt; Data collection request</td></tr><tr><td colspan="2">RANNodes -&gt; nonRTRICFramework : &lt;&lt;O1&gt;&gt; Data Collection</td></tr><tr><td colspan="2">nonRTRICFramework -&gt; rApp :&lt;&lt;Rl&gt;&gt; Data Collection end</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">group 02 Data Collection</td></tr><tr><td colspan="2">rApp -&gt; nonRTRICFramework : &lt;&lt;Rl&gt;&gt; Data collection request</td></tr><tr><td colspan="2">nonRTRICFramework -&gt; OcLouDs : &lt;&lt;o2&gt;&gt; Data collection request OCLOUDs -&gt; nonRTRICFramework</td></tr><tr><td colspan="2">nonRTRICFramework -&gt; rApp : &lt;&lt;R1&gt;&gt; Data Collection</td></tr><tr><td colspan="2">end</td></tr><tr><td colspan="2">group Data Analysis and Inference</td></tr><tr><td colspan="2">rApp -&gt; rApp : Creates O1 configurations or Al polices which contains proximal computing capability information \nand availability information for each o-cloud based RAN nodes for multi-aspect handover optimization</td></tr><tr><td colspan="2">end</td></tr><tr><td colspan="2">group Policy Creation rApp -&gt; nonRTRICFramework : &lt;&lt;Rl&gt;&gt; O1 configurations or Al polices for multi-aspect</td></tr><tr><td colspan="2">handover optimization via Rl interface</td></tr><tr><td colspan="2">nonRTRICFramework -&gt; NearRTRIC : &lt;&lt;01 or Al&gt;&gt; 01 configurations via O1 interface \nor A1 polices via Al interface</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">NearRTRIC -&gt; RANNodes : &lt;&lt;E2&gt;&gt; E2 control or E2 policies \nfor multi-aspect handover</td></tr><tr><td colspan="2">optimization</td></tr><tr><td colspan="2">end</td></tr></table>

The flow diagram of the multi-aspect handover optimization is given in figure 4.27.3.2-1.

![](images/e48970d80d27259dcf2b68d0e72bb91e4513af62fa53b835bbb1008d62c9a9fb.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.27.3.2-1: Multi-aspect handover optimization flow diagram

4.27.3.3 Sub-use case 2: RAN edge computing resource information exposure

The context of the RAN edge computing information exposure is captured in table 4.27.3.3-1.

Table 4.27.3.3-1: RAN edge computing information exposure   

<table><tr><td colspan="1" rowspan="1">Use Case Step</td><td colspan="1" rowspan="1">Description of the step</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">RAN edge computing information exposure</td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO, O-Cloud, orchestrator/application server</td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.O2 interface connectivity is established with SMO.</td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">SMO and O-Cloud are instantiated with O2 interface connectivity being established betweenthem.Editor's note: Security related procedure is not defined in the present document.</td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">Orchestrators or application servers want to request/subscribe RAN edge computinginformation.</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">Service consumer (i.e., orchestrator or application server) sends RAN edge computing information request to SMO for updated RAN edge computing resource information, orreserving RAN edge computing resources to be used.</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">SMO requests or subscribes the measurement data from O-Cloud and receives computingrelated resource data from O-Cloud through response or periodic notifications.</td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">Alternatively, SMO could use Al/ML or other methods to perform computing related resourcedata statistics and analysis.</td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">Based on the received request from service consumer, SMO sends RAN edge computinginformation response indicating the RAN side computing related information managed bySMO, which includes updated or reserved RAN edge computing resource information.</td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">Orchestrators or application servers get the response.</td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td></td></tr></table>

@startuml   
Skin rose   
skinparam ParticipantPadding 5   
skinparam BoxPadding 10   
skinparam defaultFontSize 12   
Box “Service Consumer” #lightcyan Participant “Orchestrator/Application Server” as app   
End box   
Box “Service Management and Orchestration” #gold Participant “SMO” as smo   
End box   
Box “O-Cloud Platform” #lightseagreen Participant ims as “IMS/DMS”   
End box app $- >$ smo : 1 RAN Edge Computing Information Request smo $- >$ ims: 2.1 <<O2>> Data Collection Request/Subscribe ims $- >$ smo: 2.2 $< < 0 2 > >$ Data Collection Response/Notify smo $- >$ smo: 3 Data analysis smo $- >$ app: 4 RAN Edge Computing Information Response   
@enduml

The flow diagram of the RAN edge computing information exposure is given in figure 4.27.3.3-1.

![](images/31a8f8935cc450e24c9f571dbe2db6e36955c55ddf50ed21e2a7dcff23fc5c3c.jpg)

> **Image Summary:** {"image": "image_20240503_143642_0.png"}
  
Figure 4.27.3.3-1: RAN edge computing information exposure

4.27.3.4 Sub-use case 3: O-RAN and mobile devices collaborative AI/ML inference Void

4.27.3.5 Sub-use case 4: XR rendering collaboration

# 4.27.3.6 Sub-use case 5: Joint communication and computing optimization for V2X communications

The context of the joint communication and computing optimization for V2X communications is captured in table 4.27.3.6-1.

Table 4.27.3.6-1: Joint communication and computing optimization for V2X communications   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Joint communication and computing optimization for V2X communications</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">SMO, Near-RT RIC, O-Cloud, E2 nodes, service consumer</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">All relevant functions and components are instantiated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre conditions</td><td colspan="1" rowspan="1">AIll relevant functions and components are instantiated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1-2 (M)</td><td colspan="1" rowspan="1">SMO retrieves data from E2 nodes and O-Cloud via O1 and O2 interfacesto obtain available communication resource (e.g., network load,bandwidth) and computing resource information (e.g., resource type,available CPU/GPU frequency, storage), respectively.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3-4 (M)</td><td colspan="1" rowspan="1">SMO exposes integrated communication and computing services orcomputing services to service consumers (e.g., vehicles or other third-party consumers).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">SMO retrieves service requests from service consumers, which indicatethe V2X service requirements. The service request includes but not limitedto following information:Service profile IDService type (e.g., ID indicates service type in V2X scenarios,such as safety, advanced driving assistance)Computing data volumeLocation of UEService end-to-end latency requirementsUE mobility level, UE trajectoryUplink/downlink throughput requirementsComputing resource requirements, including resource type,resource description, etc.Storage resource requirement If the service consumer is a third-party service provider, followinginformation should also be included in the service request:Maximum number of UEsCoverage for communication part of communication andcomputing services provided by RANOverall uplink/downlink throughput requirements</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6-9 (M)</td><td colspan="1" rowspan="1">SMO performs joint communication and computing resource optimizationvia Al/ML inference based on service requests and generates policies. Thepolicies include but not limited to workload deployment (e.g., offload theworkload to which endpoint) and/or computing resource schedulingpolicies.SMO sends the workload deployment policies including servicerequirements, and/or computing resource allocation policies to O-Cloudvia O2 interface.SMO sends communication optimization policies to Near-RT RIC via A1interface to facilitate that Near-RT RIC optimized communicationresources of E2 nodes.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">SMO sends notifications (e.g., service availability) to the consumer. Theconsumer establishes connection with the assigned endpoint and sendsservice load to the endpoint.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">SMO evaluates the performance (e.g., network performance, QoS ofservice), updates Al/ML model and /or policy accordingly.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">None identified</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

<table><tr><td>skin rose</td></tr><tr><td>skinparam ParticipantPadding 5</td></tr><tr><td>skinparam BoxPadding 10</td></tr><tr><td>skinparam defaultFontsize 12</td></tr><tr><td>Autonumber</td></tr><tr><td>box #lightcyan</td></tr><tr><td>Participant &quot;service consumer&quot; as consumer</td></tr><tr><td>endbox</td></tr><tr><td></td></tr><tr><td>box #lightseagreen Participant &quot;o-cloud&quot; as cloud</td></tr><tr><td>endbox</td></tr><tr><td></td></tr><tr><td>box #gold Participant &quot;sMo/Non-RT RIc&quot; as SMO</td></tr><tr><td>endbox</td></tr><tr><td>box &quot;O-RAN Nodes&quot; #lightpink</td></tr><tr><td>Participant &quot;Near RT-RIc&quot; as RIC</td></tr><tr><td>Participant &quot;E2 nodes&quot; as e2</td></tr><tr><td>Endbox</td></tr><tr><td></td></tr><tr><td>SMo&lt;-cloud： &lt;o2&gt; Computing resource information SMo&lt;-e2： &lt;ol&gt; Communication resource information</td></tr><tr><td></td></tr><tr><td>group service exposure</td></tr><tr><td>consumer-&gt;smo: service discovery request consumer&lt;-smo: service discovery response</td></tr><tr><td>end</td></tr><tr><td>consumer-&gt;smo: service request</td></tr><tr><td></td></tr><tr><td>group Joint communication and computing resource optimization</td></tr><tr><td>SMO-&gt;sMO:AI/ML inference</td></tr></table>

SMO->cloud: <O2> Workload offload policy and/or computing resource optimization policy   
SMO->RIC:<A1> Communication resource optimization policy   
RIC->e2:<E2> Communication resource optimization policy   
end   
consumer<-SMO:Notifications (e.g., service availbility)   
group Performance monitoring   
ref over SMO,RIC,cloud, e2   
Performance monitoring and evaluation   
end ref   
SMO->SMO: AI/ML model or policy update   
end   
@enduml

The flow diagram of the joint communication and computing optimization for V2X communications is given in figure 4.27.3.6-1.

![](images/b67ce09277ac522585230362f4578eed99d847431d7a37dcf735c7aa43da5792.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4.27.3.6-1: Joint communication and computing optimization for V2X communications flow diagram

4.27.3.7 Sub-use case 6: Exposure of performance information to assist computing resource scheduling

Void

# 4.27.4 Required data

4.27.4.1 Required data for communication and computing integrated networks use cases The following clauses describe the required data that is relevant to each of the CCIN sub–use cases.

4.27.4.2 Sub-use case 1: Multi-aspect handover optimization

Table 4.27.4.2-1: Required data for multi-aspect handover optimization   

<table><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters /Measurements</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(Available/Required)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.001</td><td colspan="1" rowspan="1">Networkconfigurationmanagement</td><td colspan="1" rowspan="1">Base stationidentifier</td><td colspan="1" rowspan="1">Uniquely identifythe base station,including PLMNidentifier andother identifiersof both theserving basestation and thetarget basestation in theproximity.</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS28.541 [5]，clause 4.3.1,gnbld</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.002</td><td colspan="1" rowspan="1">Proximalcomputingcapabilityinformation</td><td colspan="1" rowspan="1">Computingresource type</td><td colspan="1" rowspan="1">Identifies the typeof resource, suchas CPU, GPU,FPGA, NPU,DPU, AIaccelerator, etc.</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">0-RAN.WG6.TS.O-CLOUD-IM[42], clause4.2.1.4.1.2,resourceTypes</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.003</td><td colspan="1" rowspan="1">Proximalcomputingcapabilityinformation</td><td colspan="1" rowspan="1">Computing tasktype</td><td colspan="1" rowspan="1">ldentifies the typeof computationaltask, such asA/CU/DU,FFT/IFFT/DFT/LDPC/POLAR/PDCPencryption/decryption, or useraccess-relatedprocessing, etc.</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Required</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.004</td><td colspan="1" rowspan="1">Networkconfigurationmanagement</td><td colspan="1" rowspan="1">Location</td><td colspan="1" rowspan="1">The geographicallocation of boththe serving basestation and thetarget basestation in theproximity.</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS28.541 [5]，clause 5.4.1,ntnGeoArea</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters IMeasurements</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(Available/Required)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.005</td><td colspan="1" rowspan="1">Proximalcomputingavailabilityinformation</td><td colspan="1" rowspan="1">Computingavailability</td><td colspan="1" rowspan="1">The total capacityand availablecapacity ofcomputingresource typesfor both theserving basestation and thetarget basestation in theproximity.</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM[42], clause4.2.1.4.5.2,capacity</td><td colspan="1" rowspan="1">02</td></tr></table>

4.27.4.3 Sub-use case 2: RAN edge computing resource information exposure

Table 4.27.4.3-1: Required data for RAN edge computing information exposure   

<table><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters IMeasurements</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(Available/Required)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.006</td><td colspan="1" rowspan="1">Computingrelatedresource data</td><td colspan="1" rowspan="1">CPU number for O-Cloud, cluster, ornode</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Required</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.007</td><td colspan="1" rowspan="1">Computingrelatedresource data</td><td colspan="1" rowspan="1">vCPU number for O-Cloud, cluster, ornode</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Required</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.008</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Total capacity ofcomputing or numberof computingresources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.5.2, capacity</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.009</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Allocated capacity ofcomputing or numberof computingresources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.5.2, capacity</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.010</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Reserved capacity ofcomputing or numberof computingresources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.5.2, capacity</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.011</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Available capacity ofcomputing or numberof computingresources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.5.2, capacity</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters /Measurements</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(Available/Required)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.012</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Cloud identifier</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.1.2, oCloudld</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.013</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Resource identifier</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.3.2, resourceld</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.014</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Resource poolidentifier</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.4.2, resourcePoolld</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.015</td><td colspan="1" rowspan="1">RAN edgecomputinginformation</td><td colspan="1" rowspan="1">Computing location</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.31.2, locationsld</td><td colspan="1" rowspan="1">02</td></tr></table>

4.27.4.4 Sub-use case 3: O-RAN and mobile devices collaborative AI/ML inference Void

4.27.4.5 Sub-use case 4: XR rendering collaboration

4.27.4.6 Sub-use case 5: Joint communication and computing optimization for V2X communications

Table 4.27.4.6-1: Required data for joint communication and computing optimization for V2X communications   

<table><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters /Measurements</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(Available/Required)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.016</td><td colspan="1" rowspan="1">Computingresourcerelated data</td><td colspan="1" rowspan="1">Resource type ofcomputing resources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Requirement</td><td colspan="1" rowspan="1">Category</td><td colspan="1" rowspan="1">Parameters IMeasurements</td><td colspan="1" rowspan="1">Source</td><td colspan="1" rowspan="1">Availability(AvailablelRequired)</td><td colspan="1" rowspan="1">Reference</td><td colspan="1" rowspan="1">Interface</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">in O-Cloud, e.g.,CPU/GPU/NPU</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4.2.1.4.1.2,resourceTypes</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Req-4.27.017</td><td colspan="1" rowspan="1">Computingresourcerelated data</td><td colspan="1" rowspan="1">Available capacity ofcomputing or numberof computingresources</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42], clause4.2.1.4.5.2, capacity</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.018</td><td colspan="1" rowspan="1">Computingresourcerelated data</td><td colspan="1" rowspan="1">Available storage</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Required</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.019</td><td colspan="1" rowspan="1">Computingresourcerelated data</td><td colspan="1" rowspan="1">Cloud identifier</td><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">O-RAN.WG6.TS.O-CLOUD-IM [42],clause 4.2.1.4.1.2,oCloudld</td><td colspan="1" rowspan="1">02</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.020</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">PRB Usage</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.552 [6],clause 5.1.1.2.3,Distribution of DL TotalPRB Usage</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.021</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">Maximum uplinkbandwidth</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clause 5.4.1, maxbrUI</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.022</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">Maximum downlinkbandwidth</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5]，clause 5.4.1, maxbrDI</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.023</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">Guaranteed uplinkbandwidth</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clause 5.4.1, gbrUI</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.024</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">Guaranteed downlinkbandwidth</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5],clause 5.4.1, gbrDI</td><td colspan="1" rowspan="1">01</td></tr><tr><td colspan="1" rowspan="1">Req-4.27.025</td><td colspan="1" rowspan="1">Communicationresourcerelated data</td><td colspan="1" rowspan="1">Link quality</td><td colspan="1" rowspan="1">O-CU</td><td colspan="1" rowspan="1">Available</td><td colspan="1" rowspan="1">3GPP TS 28.541 [5]，clause 4.4.1, qQualMin</td><td colspan="1" rowspan="1">01</td></tr></table>

# 4.27.4.7 Sub-use case 6: Exposure of performance information to assist computing resource scheduling

Void

# Annex A (informative): Additional information

# A.1 Traffic steering use case A1 interface usage example

NOTE: Please refer to WG2 Use Cases and Requirements Specification for more details and up to date definitions of this use case A1 interface usage examples.

An example scenario is here used to describe the use of A1 for traffic steering, implying the Non-RT RIC sending policies for allocation of the control plane (RRC) and the user plane for different services, identified by their 5QI.

In the scenario a UE with UEid $\Longrightarrow 1$ , belonging to a subnet slice identified by S-NSSA $[ = 1$ , having a voice $( 5 0 \mathrm { I } { = } 1 )$ ) and an MBB (5Q $[ = 9$ ) connection established, enters an area covered by four frequency bands. The Non-RT RIC understands the requirements and characteristics of the services and decides to let the voice and RRC connection reside on the low band (here covered by a macro cell B becoming the PCell), while the MBB connection should preferably use the higher band (here provided by a smaller cell C and D becoming the SCells) and avoid the low band if possible. Cell A is used for MBB if required for coverage reasons.

Policies are sent to any cell of concern, e.g. where the UE resides and can move.

The desired use of the cells is shown in figure A.1-1.

![](images/68269a63630dbb9a5d78ffbfd30ac3a87542abe5935ba1836dfdc05d3dc42bda.jpg)

> **Image Summary:** {"image": "image_8q2q87092p.png"}
  
Figure A.1-1: Desired use of the cells

Two policies over A1 are needed to accomplish the desired behavior, described in JSON format below. Note that as part of the scope, the cell_id is optional, and if omitted it is up to the Near-RT RIC to locate the UE and there enforce the policy.

![](images/c637fb985b213a421c6c025d7084388690694073626481977df22bcd0ce2f956.jpg)

> **Image Summary:** {"image": "image.png"}


“cell_id”: ”X” // Policy for Cell X, where X is one of A, B, C or D }, "statement": { "cell_id_list": "B", "preference": "Shall", "primary": true // Control plane on Cell B (becoming PCell) }, "statement": { "cell_id_list ": "B", "preference": "Shall", "primary": false // Voice on Cell B }

"policy_id": "2",   
"scope": { "ue_id": "1", "slice_id": "1", "qos_id": "9", “cell_id”: ”X” // Policy for Cell X, where X is one of A, B, C or D   
},   
"statement": { "cell_id_list ": {"B", “A”}, "preference": "Avoid", "primary": false // Avoid MBB on Cell A and Cell B   
},   
"statement": { "cell_id_list": {“C”, “D”}, "preference": "Prefer", "primary": false // Prefer MBB on Cell C and Cell D   
}

# Annex (informative): Change history/Change request (history)

<table><tr><td colspan="1" rowspan="1">Date</td><td colspan="1" rowspan="1">Revision</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">2019.07.07</td><td colspan="1" rowspan="1">01.00.00</td><td colspan="1" rowspan="1">Draft template</td></tr><tr><td colspan="1" rowspan="1">2019.09.18</td><td colspan="1" rowspan="1">01.00.01</td><td colspan="1" rowspan="1">Addition of CR:ORAN-WG1.UseCasesDetailedSpecification_CR_NOK_DHO_20190909</td></tr><tr><td colspan="1" rowspan="1">2019.09.19</td><td colspan="1" rowspan="1">01.00.02</td><td colspan="1" rowspan="1">Addition of QoE optimization use case from WG2 UCR specification</td></tr><tr><td colspan="1" rowspan="1">2019.09.20</td><td colspan="1" rowspan="1">01.00.03</td><td colspan="1" rowspan="1">Addition of Traffic Steering use case from WG2 UCR specification</td></tr><tr><td colspan="1" rowspan="1">2019.09.23</td><td colspan="1" rowspan="1">01.00.04</td><td colspan="1" rowspan="1">Addition of CR:ORAN-WG1.UAV Control Vehicle Use Case -INSPUR-20190911Editorial changes</td></tr><tr><td colspan="1" rowspan="1">2019.09.27</td><td colspan="1" rowspan="1">01.00.05</td><td colspan="1" rowspan="1">Addition of CR:ORAN-WG1.UAV_Use Case for dynamic UAV Radio Resource Allocation_CMCC_CREditorial changes for improved sections, consistency, typo fixes</td></tr><tr><td colspan="1" rowspan="1">2019.09.28</td><td colspan="1" rowspan="1">01.00.06</td><td colspan="1" rowspan="1">Updates to Radio Resource Allocation for UAV Application Scenario from UC AnalysisdocAddition of CR:ORAN-WG1.UAV_Use Case for dynamic UAV Radio Resource Allocation_CMCC_CR_v2</td></tr><tr><td colspan="1" rowspan="1">2019.10.11</td><td colspan="1" rowspan="1">01.00.07</td><td colspan="1" rowspan="1">Updates to the follwing use cases based on use case review meeting:Fight Path Based Dynamic UAV Radio Resource Allocation (CMCC)Radio Resource Allocation for UAV Application (Inspur)</td></tr><tr><td colspan="1" rowspan="1">2019.10.17</td><td colspan="1" rowspan="1">01.00.08</td><td colspan="1" rowspan="1">Add plantuml code and diagram for OoE use case to add E2 interaction between Near-RT RIC and RANModified UAV Control Vehicle use case required data to remove IMSI and replace withuser identification clarificationCorrected UAV Resource Allocation plantuml code and diagram with ML modeldeployment over O1 (rather than A1)Corrected QoE use case plantuml code and diagram for ML model deployment over O1(rather than A1)Merged updates from ORAN-WG1.Correction onUAV_UseCasesDetailedSpecification_CMCC_CR v1</td></tr><tr><td colspan="1" rowspan="1">2019.10.17</td><td colspan="1" rowspan="1">01.00</td><td colspan="1" rowspan="1">Final version 01.00</td></tr><tr><td colspan="1" rowspan="1">2019.11.16</td><td colspan="1" rowspan="1">02.00.01</td><td colspan="1" rowspan="1">Initial version of v2.0Document version number update to v02.00.01</td></tr><tr><td colspan="1" rowspan="1">2019.11.25</td><td colspan="1" rowspan="1">02.00.02</td><td colspan="1" rowspan="1">Addition of CR (new use case):ORAN-WG1.UseCasesDetailedSpecification_CR_ORANGE_20191120.docx</td></tr><tr><td colspan="1" rowspan="1">2019.12.06</td><td colspan="1" rowspan="1">02.00.03</td><td colspan="1" rowspan="1">Addition of CRs:UAV Control Vehicle-CR-INSPUR-20191204.docxORAN-WG1.UseCasesDetailedSpecification_CR_ORANGE_20191125-update-uml.docx</td></tr><tr><td colspan="1" rowspan="1">2019.12.08</td><td colspan="1" rowspan="1">02.00.04</td><td colspan="1" rowspan="1">Addition of CRs:ORAN-WG1.UseCasesDetailedSpecification_CR_CMCC_20191204.docx</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-  ORAN-WG1.UseCasesDetailedSpecification_CR_NOK_DHO_20191203.docx</td></tr><tr><td colspan="1" rowspan="1">2020.01.10</td><td colspan="1" rowspan="1">02.00.05</td><td colspan="1" rowspan="1">Addition of CRs:ORAN-WG1.UseCasesAnalysisReport_CR_Traffic_Steering_Ericsson_2020.01.08.docxORAN-WG1.Usecase_QoS_based_resource_optimization_1_6-2020.docx</td></tr><tr><td colspan="1" rowspan="1">2020.01.22</td><td colspan="1" rowspan="1">02.00.06</td><td colspan="1" rowspan="1">Editorial updates and terminology corrections</td></tr><tr><td colspan="1" rowspan="1">2020.02.12</td><td colspan="1" rowspan="1">02.00.07</td><td colspan="1" rowspan="1">Addition of CR:ORAN-WG1.UCTG_CMCC_QoE Optimization Use CaseEditorial updates to plantUML diagrams to add interface names, and rearrangingcomponents per O-RAN plantUML guidelines</td></tr><tr><td colspan="1" rowspan="1">2020.02.13</td><td colspan="1" rowspan="1">02.00.08</td><td colspan="1" rowspan="1">Addition of CR:ORAN-WG1.UseCasesDetailedSpecification_CR_ (UC_M-MIMO)_TIM-ORANGE-CMCC_20200114-v2</td></tr><tr><td colspan="1" rowspan="1">2020.02.23</td><td colspan="1" rowspan="1">02.00.09</td><td colspan="1" rowspan="1">Editorial updates, O-RAN license agreement additions, update RAN Sharing diagramwith latest version,</td></tr><tr><td colspan="1" rowspan="1">2020.03.01</td><td colspan="1" rowspan="1">02.00.10</td><td colspan="1" rowspan="1">Editorial updates, fixing table of contents issues, spec naming corrections</td></tr><tr><td colspan="1" rowspan="1">2020.03.11</td><td colspan="1" rowspan="1">02.00.11</td><td colspan="1" rowspan="1">Updates to definitions and RAN Sharing use case (update O1* to O2) based on WG1review/approval feedback</td></tr><tr><td colspan="1" rowspan="1">2020.03.11</td><td colspan="1" rowspan="1">02.00</td><td colspan="1" rowspan="1">Final version 02.00</td></tr><tr><td colspan="1" rowspan="1">2020.06.19</td><td colspan="1" rowspan="1">03.00.01</td><td colspan="1" rowspan="1">Initial version of v3.0Document version number update to v03.00.01</td></tr><tr><td colspan="1" rowspan="1">2020.06.20</td><td colspan="1" rowspan="1">03.00.02</td><td colspan="1" rowspan="1">Addition of CR:O-RAN_WG1_2020.03.11-Netsia_KDDI_ATT_TEF_UCTG_CR_UCDS_SliceAssurance .docx</td></tr><tr><td colspan="1" rowspan="1">2020.06.20</td><td colspan="1" rowspan="1">03.00.03</td><td colspan="1" rowspan="1">Addition of CR:INT-2020.05.21-WG1-D-CR-UCDR_MultiAccess_UC_v1.docx</td></tr><tr><td colspan="1" rowspan="1">2020.07.15</td><td colspan="1" rowspan="1">03.00.04</td><td colspan="1" rowspan="1">Updates based on WG1 review comments (very minor editorial corrections to section3.9)</td></tr><tr><td colspan="1" rowspan="1">2020.07.16</td><td colspan="1" rowspan="1">03.00.05</td><td colspan="1" rowspan="1">Getting the version ready to be published externally (removal of trackchanges/comments)</td></tr><tr><td colspan="1" rowspan="1">2020.07.16</td><td colspan="1" rowspan="1">03.00</td><td colspan="1" rowspan="1">Final version 03.00</td></tr><tr><td colspan="1" rowspan="1">2020.10.17</td><td colspan="1" rowspan="1">04.00.01</td><td colspan="1" rowspan="1">Initial version of v4.0Document version number update to v04.00.01</td></tr><tr><td colspan="1" rowspan="1">2020.11.01</td><td colspan="1" rowspan="1">04.00.02</td><td colspan="1" rowspan="1">Addition of CR:-  STL.AO-10.14.2020-WG1(UCTG)-CR-0001-DSS-V1.2</td></tr><tr><td colspan="1" rowspan="1">2020.11.02</td><td colspan="1" rowspan="1">04.00.03</td><td colspan="1" rowspan="1">Addition of CR:INT-2020.11.02-WG1(UCTG)-CR-0001-NSSI-Rsrc-Opt-D-UC-V1.3Editorial updates/corrections</td></tr><tr><td colspan="1" rowspan="1">2020.11.05</td><td colspan="1" rowspan="1">04.00.04</td><td colspan="1" rowspan="1">Addition of CR:KDDI.AO-2020.11.05-WG1-CR-0001-Multi-vendor Slices Use Case-v01</td></tr><tr><td colspan="1" rowspan="1">2020.11.13</td><td colspan="1" rowspan="1">04.00.05</td><td colspan="1" rowspan="1">Correction of plantuml source and diagram for Multi-vendor Slices use case and othereditorial updates</td></tr><tr><td colspan="1" rowspan="1">2020.11.13</td><td colspan="1" rowspan="1">04.00</td><td colspan="1" rowspan="1">Final version 04.00</td></tr><tr><td colspan="1" rowspan="1">2021.02.28</td><td colspan="1" rowspan="1">05.00.01</td><td colspan="1" rowspan="1">Initial version of v5.0Document version number update to v05.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.03.04</td><td colspan="1" rowspan="1">05.00.02</td><td colspan="1" rowspan="1">To keep the same use case numbering as Use Case Analysis Report, addition ofUse case 13 “Local Indoor Positioning in RAN"Use case 16 “"Congestion Prediction and Management"Use case 17 "Industrial loT Optimization"Use case 18 “BBU Pooling to achieve RAN Elasticity"as FFS items. Use case 14 and 15 will be defined in further sub versions of this v5specification.Addition of CR:ATT.AO-2020.12.01-WG1-CR-0001-UseCaseDetailedSpecification_SSP-v04</td></tr><tr><td colspan="1" rowspan="1">2021.03.08</td><td colspan="1" rowspan="1">05.00.03</td><td colspan="1" rowspan="1">Updating use case 14 name to "Massive SU/MU-MIMO Grouping Optimization"</td></tr><tr><td colspan="1" rowspan="1">2021.03.08</td><td colspan="1" rowspan="1">05.00.04</td><td colspan="1" rowspan="1">Addition of CR:NOK-2021.02.10-ORAN-CR-0001-UseCaseDetailedSpecification_mMIMO_BF_Optimization-v01Editorial updates</td></tr><tr><td colspan="1" rowspan="1">2021.03.13</td><td colspan="1" rowspan="1">05.00</td><td colspan="1" rowspan="1">Final version 05.00</td></tr><tr><td colspan="1" rowspan="1">2021.07.10</td><td colspan="1" rowspan="1">06.00.01</td><td colspan="1" rowspan="1">Initial version of v6.0Document version number update to v06.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.07.11</td><td colspan="1" rowspan="1">06.00.02</td><td colspan="1" rowspan="1">Addition of CR:NOK-2021.05.03-ORAN-CR-0001-UseCaseDetailedSpecification_mMIMO_BF_Optimization</td></tr><tr><td colspan="1" rowspan="1">2021.07.19</td><td colspan="1" rowspan="1">06.00</td><td colspan="1" rowspan="1">Final version 06.00</td></tr><tr><td colspan="1" rowspan="1">2021.11.11</td><td colspan="1" rowspan="1">07.00.01</td><td colspan="1" rowspan="1">Initial version of v7.0Document version number update to v07.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.11.13</td><td colspan="1" rowspan="1">07.00.02</td><td colspan="1" rowspan="1">Addition of CR:NC.AO-2021.07.20-WG1-CR-0001-NSSIResourceAllocationWithQuota-v04</td></tr><tr><td colspan="1" rowspan="1">2021.11.13</td><td colspan="1" rowspan="1">07.00.03</td><td colspan="1" rowspan="1">Correction of terminology used in NSSI optimization use case</td></tr><tr><td colspan="1" rowspan="1">2021.11.14</td><td colspan="1" rowspan="1">07.00.04</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2021.11.23</td><td colspan="1" rowspan="1">07.00.05</td><td colspan="1" rowspan="1">Updates to address WG1 review comments</td></tr><tr><td colspan="1" rowspan="1">2021.11.23</td><td colspan="1" rowspan="1">07.00</td><td colspan="1" rowspan="1">Final version 07.00</td></tr><tr><td colspan="1" rowspan="1">2022.03.27</td><td colspan="1" rowspan="1">07.00.06</td><td colspan="1" rowspan="1">Adopted new spec revision numbering per O-RAN Work ProceduresInitial version towards v08.00, starting with v07.00.06 per new revision numbering</td></tr><tr><td colspan="1" rowspan="1">2022.03.27</td><td colspan="1" rowspan="1">07.00.07</td><td colspan="1" rowspan="1">Addition of CR:CMCC-2022.1.13-WG1-CR-0001-UseCasesDetailedSpecification-QOE-Optimization-v3.0</td></tr><tr><td colspan="1" rowspan="1">2022.03.27</td><td colspan="1" rowspan="1">07.00.08</td><td colspan="1" rowspan="1">Addition of CR:CMCC-2022.03.10-WG1-CR-0001-UseCasesDetailedSpecification-Local-Indoor-Positioning-in-RAN-v1</td></tr><tr><td colspan="1" rowspan="1">2022.03.27</td><td colspan="1" rowspan="1">07.00.09</td><td colspan="1" rowspan="1">Addition of placeholders for new use cases added to Use Case Analysis RreportUse Case 20: Lower Layer Split Multi Node Support (Shared O-RU)Use Case 21: Energy Saving</td></tr><tr><td colspan="1" rowspan="1">2022.03.27</td><td colspan="1" rowspan="1">07.00.10</td><td colspan="1" rowspan="1">Changes accepted from v07.00.09Baseline for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.04.04</td><td colspan="1" rowspan="1">08.00</td><td colspan="1" rowspan="1">Final version 08.00</td></tr><tr><td colspan="1" rowspan="1">2022.07.24</td><td colspan="1" rowspan="1">08.00.01</td><td colspan="1" rowspan="1">Initial version towards v09.00, starting with v08.00.01 per O-RAN specification revisionnumbering process</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">08.00.02</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO-2022.04.25-ORAN-CR-0001-RevisedUseCaseDetailedSpecification_EE-ES_V10Editorial updates and corrections</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">08.00.03</td><td colspan="1" rowspan="1">Addition of CR:COT.AO-2022.06.29-WG1-CR-0002-UseCaseDetailedSpecification-MU-MIMO-Optimization-v05Per UCTG Shared O-RU subgroup discussions, updating use case #20 from "LowerLayer Multi Node Support"” to “Shared O-RU" for consistency with the O-RAN Shared O-RU feature</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">08.00.04</td><td colspan="1" rowspan="1">Update of the document to comply with the new O-RAN Technical Spec template</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">08.00.05</td><td colspan="1" rowspan="1">All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.07.27</td><td colspan="1" rowspan="1">08.00.06</td><td colspan="1" rowspan="1">Addition of CR:CIS.AO-2022.07.21-WG1-CR-0001-UseCaseDetailedSpecification-shared-ORU-v04Editorial corrections and updates</td></tr><tr><td colspan="1" rowspan="1">2022.07.27</td><td colspan="1" rowspan="1">08.00.07</td><td colspan="1" rowspan="1">Updated version for WG1/TSC approval</td></tr><tr><td colspan="1" rowspan="1">2022.08.01</td><td colspan="1" rowspan="1">09.00</td><td colspan="1" rowspan="1">Final version 09.00</td></tr><tr><td colspan="1" rowspan="1">2022.11.09</td><td colspan="1" rowspan="1">09.00.01</td><td colspan="1" rowspan="1">Initial version towards v10.00, starting with v09.00.01 per O-RAN specification revisionnumbering processAddition of CR:ATT.AO-2022.04.12-ORAN-CR-0001-UseCaseDetailedSpecification_TrafficSteeringEI - Rev 2</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">09.00.02</td><td colspan="1" rowspan="1">Addition of CR:FJT-2022.08.25-ORAN-CR-0001-UseCaseDetailedSpecification_RANSliceSlaAssurance_ReliabilityAssurance-Rev1</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">09.00.03</td><td colspan="1" rowspan="1">Addition of CR:QCM.AO-2022.06.14-ORAN-CR-0001-UseCaseDetailedSpecification_ISRM-v14-clean</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">09.00.04</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO-2022.10.27-WG1-CR-0001-UseCaseDetailedSpecification-shared-ORU-v01Editorial updatesAddition of Section 3.23 as placeholder to align with new use case addition to O-RANUse Cases Analysis Technical Report</td></tr><tr><td colspan="1" rowspan="1">2022.11.13</td><td colspan="1" rowspan="1">09.00.05</td><td colspan="1" rowspan="1">Added O-RAN Release "R003" to document name, updated copyright to 2023 as thedocument will be published externally in 2023.All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.11.18</td><td colspan="1" rowspan="1">10.00</td><td colspan="1" rowspan="1">Final version 10.00</td></tr><tr><td colspan="1" rowspan="1">2023.03.16</td><td colspan="1" rowspan="1">10.00.01</td><td colspan="1" rowspan="1">Initial version towards v11.00, starting with v10.00.01 per O-RAN specification revisionnumbering processUpdate of the spec to latest O-RAN TS template except for spliting the references toformative and informative. This split is planned to be made in next release of thedocument.</td></tr><tr><td colspan="1" rowspan="1">2023.03.16</td><td colspan="1" rowspan="1">10.00.02</td><td colspan="1" rowspan="1">Addition of CR:</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">NOK.AO-2023.02.09-WG1-CR-0001-SharedORU_CoordinatedReset-v02.00</td></tr><tr><td colspan="1" rowspan="1">2023.03.16</td><td colspan="1" rowspan="1">10.00.03</td><td colspan="1" rowspan="1">Addition of CR:KDDI.AO-2023.03.07-WG1-CR-0000-UseCaseDetailedSpecification-MultiVendorSlicesAddRequirement-v02Addition of placeholder for "use case #24: Industrial vision SLA Assurance" as this usecase is approved and merged to Use Case Analysis Report</td></tr><tr><td colspan="1" rowspan="1">2023.03.16</td><td colspan="1" rowspan="1">10.00.04</td><td colspan="1" rowspan="1">All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.03.24</td><td colspan="1" rowspan="1">10.00.05</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed. Ready for TSCapproval and publication.</td></tr><tr><td colspan="1" rowspan="1">2023.03.24</td><td colspan="1" rowspan="1">11.00</td><td colspan="1" rowspan="1">Final version 11.00</td></tr><tr><td colspan="1" rowspan="1">2023.05.04</td><td colspan="1" rowspan="1">11.00.01</td><td colspan="1" rowspan="1">Initial version towards v12.00, starting with v11.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2023.05.02-WG1-CR-0012-O-RAN-Use-Cases-Detailed-Specification-ODR-References-Section-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.04</td><td colspan="1" rowspan="1">11.00.02</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.02-WG1-CR-0013-O-RAN-Use-Cases-Detailed-Specification-ODR-References-Section-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.16</td><td colspan="1" rowspan="1">11.00.03</td><td colspan="1" rowspan="1">Addition of CRs:JNPR-2023.05.16-WG1-CR-0021-O-RAN-Use-Cases-Detailed-Specification-References-Update-v01JNPR-2023.05.16-WG1-CR-0022-O-RAN-Use-Cases-Detailed-Specification-References-Correction-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.29</td><td colspan="1" rowspan="1">11.00.04</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.17-WG1-CR-0023-O-RAN-Use-Cases-Detailed-Specification-References-Wording-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.06</td><td colspan="1" rowspan="1">11.00.05</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.29-WG1-CR-0025-O-RAN-Use-Cases-Detailed-Specification-ODR-Figures-References_Wording_Corrections-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.13</td><td colspan="1" rowspan="1">11.00.06</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.13-WG1-CR-0032-O-RAN-Use-Cases-Detailed-Specification-ODR-Tables-References-Headings-Corrections-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.13</td><td colspan="1" rowspan="1">11.00.07</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.13-WG1-CR-0033-O-RAN-Use-Cases-Detailed-Specification-ODR-Notes-v02</td></tr><tr><td colspan="1" rowspan="1">2023.06.27</td><td colspan="1" rowspan="1">11.00.08</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.27-WG1-CR-0036-O-RAN-Use-Cases-Detailed-Specification-ODR-Modal-Verbs_Shall_Shall_not_Should_Should_not_Must_Must_not-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.28</td><td colspan="1" rowspan="1">11.00.09</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.28-WG1-CR-0038-O-RAN-Use-Cases-Detailed-Specification-ODR-Modal-Verbs_Can_Cannot_May_Need_not-v01</td></tr><tr><td colspan="1" rowspan="1">2023.07.19</td><td colspan="1" rowspan="1">11.00.10</td><td colspan="1" rowspan="1">Addition of CR:</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">KDDI.AO-2023.03.08-WG1-CR-0002-UseCaseDetailedSpecification-update-SLA-Assurance-v01</td></tr><tr><td colspan="1" rowspan="1">2023.07.19</td><td colspan="1" rowspan="1">11.00.11</td><td colspan="1" rowspan="1">Addition of CR:CMCC-2023.2.6-WG1-CR-0001-UseCasesDetailedSpecification-Industrialvision-guarantee-v3Addition of section 4.25 as placeholder for Use Case 25: Non-Public Network(NPN) RAN-Sharing via Midhaul for Multi-Operator Coverage</td></tr><tr><td colspan="1" rowspan="1">2023.07.19</td><td colspan="1" rowspan="1">11.00.12</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO-2023.06.30-WG1-CR-0002-ResiliencyUseCase-SharedORU-v02.01</td></tr><tr><td colspan="1" rowspan="1">2023.07.19</td><td colspan="1" rowspan="1">11.00.13</td><td colspan="1" rowspan="1">Addition of CR:NEC-2022.12.12-WG1-CR-0008-ODU_SW_Update-shared-ORU-v08.00</td></tr><tr><td colspan="1" rowspan="1">2023.07.20</td><td colspan="1" rowspan="1">11.00.14</td><td colspan="1" rowspan="1">Update of the spec to latest O-RAN TS templateCorrection of font types and spacing across the spec per ODR requirementsEditorial corrections</td></tr><tr><td colspan="1" rowspan="1">2023.07.20</td><td colspan="1" rowspan="1">11.00.15</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">11.00.16</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">11.00.17</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">12.00</td><td colspan="1" rowspan="1">Final version 12.00</td></tr><tr><td colspan="1" rowspan="1">2023.11.06</td><td colspan="1" rowspan="1">12.00.01</td><td colspan="1" rowspan="1">Initial version towards v13.00, starting with v12.00.01 per O-RAN specification revisionnumbering process.Addition of CR:NOK.AO-2023.10.17-WG1-CR0004-MultiMNO-SharedORU_SubUseCase-v01.01Addition of section 4.26 as placeholder for Use Case 26: Interference Detection andOptimizationEditorial Modifications</td></tr><tr><td colspan="1" rowspan="1">2023.11.06</td><td colspan="1" rowspan="1">12.00.02</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">12.00.03</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">12.00.04</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">13.00</td><td colspan="1" rowspan="1">Final version 13.00</td></tr><tr><td colspan="1" rowspan="1">2023.11.22</td><td colspan="1" rowspan="1">13.00.01</td><td colspan="1" rowspan="1">Initial version towards v14.00, starting with v13.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2023.11.22-WG1-CR-0047-O-RAN-Use-Cases-Detailed-Specification-ODR-FFS-Concepts-v01</td></tr><tr><td colspan="1" rowspan="1">2024.02.26</td><td colspan="1" rowspan="1">13.00.02</td><td colspan="1" rowspan="1">Addition of CRs:JNPR-2024.01.16-WG1-CR-0051-O-RAN-Use-Cases-Detailed-Specification-ODR-Clauses-v01JNPR-2024.01.16-WG1-CR-0053-O-RAN-Use-Cases-Detailed-Specification-ODR-Figures-Numbering_Capital_Letters_Editorial_Changes-v01JNPR-2024.01.16-WG1-CR-0054-O-RAN-Use-Cases-Detailed-Specification-ODR-Tables-Numbering_Capital_Letters_Editorial_Changes-vV01 copy</td></tr><tr><td colspan="1" rowspan="1">2024.03.07</td><td colspan="1" rowspan="1">13.00.03</td><td colspan="1" rowspan="1">Addition of CRs:CMCC-2023.09.12-WG1-CR-0004-UseCasesDetailedSpecification-Interference-Detection-and-Optimization-v05KDDI.AO-2023.11.14-WG1-CR-0004-UseCaseDetailedSpecification-update-SLA-Assurance-v01</td></tr><tr><td colspan="1" rowspan="1">2024.03.08</td><td colspan="1" rowspan="1">13.00.04</td><td colspan="1" rowspan="1">Addition of CR:KDDI.AO-2023.12.11-WG1-CR-0005-UseCasesDetailedSpecification-Interference-Detection-and-Optimization-v03</td></tr><tr><td colspan="1" rowspan="1">2024.03.20</td><td colspan="1" rowspan="1">13.00.05</td><td colspan="1" rowspan="1">Addition of CRs:NOK-2024.01.25-WG1UCTG-CR0009-SharedORU_SubUseCaseTitleUpdates-v01.00RMI.AO-2023.08.30-WG1-UCTG-CR-0002-Shared-ORU-Advanced-Resiliency-sub-use-case#1(1+1)-v01.00NOK.AO-2024.01.25-WG1UCTG-CR0008-SharedORU_PerformanceMgmt_SubUseCase-v01.04NOK.AO-2024.02.15-WG1UCTG-CR0010-SharedORU_AntennaCalibration_SubUseCase-v01.00</td></tr><tr><td colspan="1" rowspan="1">2024.03.22</td><td colspan="1" rowspan="1">13.00.06</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">13.00.07</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">13.00.08</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">14.00</td><td colspan="1" rowspan="1">Final version 14.00</td></tr><tr><td colspan="1" rowspan="1">2024.06.25</td><td colspan="1" rowspan="1">14.00.01</td><td colspan="1" rowspan="1">Initial version towards v15.00, starting with v14.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2024.05.10-WG1-CR-0056-O-RAN-Use-Cases-Detailed-Specification-ODR-Capital_Letters-Editorial_Changes-Fixes-v01</td></tr><tr><td colspan="1" rowspan="1">2024.06.28</td><td colspan="1" rowspan="1">14.00.02</td><td colspan="1" rowspan="1">Addition of CRs:JNPR-2024.06.03-WG1-CR-0059-O-RAN-Use-Cases-Detailed-Specification-ODR-References-v01NOK-2024.04.10-WG1-CR-0066-Shared_O-RU_Dynamic_Resource_Shifting-v02NOK.AO-2024.06.11-WG1UCTG-CR0065-SharedORU_Rehoming_SubUseCase-v03RMI-2023.05.17-WG1-CR-0001-Shared-ORU-Basic-Resiliency-use-case-v01</td></tr><tr><td colspan="1" rowspan="1">2024.07.05</td><td colspan="1" rowspan="1">14.00.03</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">14.00.04</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">14.00.05</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">Final version 15.00</td></tr><tr><td colspan="1" rowspan="1">2024.09.10</td><td colspan="1" rowspan="1">15.00.01</td><td colspan="1" rowspan="1">Initial version towards v16.00, starting with v15.00.01 per O-RAN specification revisionnumbering process.Addition of CRs:CMCC-2024.06.03-WG1-UCTG-CR-0027-UseCasesDetailedSpecification-Use Case 26-Interference-Prediction_v2</td></tr><tr><td></td><td></td><td>JNPR-2024.08.05-WG1-CR-0061-O-RAN-Use-Cases-Detailed-Specification-ODR- References-Editorial_Change-v01</td></tr><tr><td></td><td></td><td>MTR.AO-2024.06.02-WG1UCTG-CR0002-Detailed-Specification-Use Case 26- Interference Detection and Optimizatio-r4</td></tr><tr><td>2024.11.04</td><td>15.00.02 Addition of CRs:</td><td></td></tr><tr><td></td><td></td><td>JNPR-2024.10.22-WG1-CR-0070-O-RAN-Use-Cases-Detailed-Specification- ETSI_PAS_Comments-v01</td></tr><tr><td></td><td></td><td>DTAG-2024.09.24-WG1-CR-0003-Use case numbering-v03</td></tr><tr><td></td><td></td><td>RMI.AO-2024.09.05-WG1-CR-0003-Shared-ORU-Resource-Shifting-use-case-v02</td></tr><tr><td>2024.11.15</td><td>15.00.03</td><td>Updated copyright statement on the cover page and footer to 2025</td></tr><tr><td></td><td></td><td>Editorial changes to align to O-RAN TS template v02.01</td></tr><tr><td></td><td></td><td>Added 3GPP Release 18 related text to Normative and Informative References clauses</td></tr><tr><td>2024.11.21</td><td></td><td>Editorial updates</td></tr><tr><td>2024.12.06</td><td>15.00.04</td><td>Clean version for WG1 approval WG1 review comments are addressed, and approval is completed.</td></tr><tr><td>2024.12.06</td><td>15.00.05</td><td>All changes accepted, clean version.</td></tr><tr><td>2024.12.06</td><td>15.00.06</td><td>Final version 16.00</td></tr><tr><td>2025.01.13</td><td>16.00 16.00.01</td><td>Initial version towards v17.00, starting with v16.00.01 per O-RAN specification revision</td></tr><tr><td></td><td></td><td>numbering process.</td></tr><tr><td></td><td></td><td>Addition of CR:</td></tr><tr><td></td><td></td><td>JNPR-2024.12.10-WG1-CR-0089-O-RAN-Use-Cases-Detailed-Specification- ETSI_PAS_Comments-v01</td></tr><tr><td>2025.01.29</td><td>16.00.02</td><td>Addition of CRs: JNPR.AO-2025.01.13-WG1-CR-0090-O-RAN-Use-Cases-Detailed-Specification-</td></tr><tr><td></td><td></td><td>Reference_Correction-v01 JNPR-2025.01.13-WG1-CR-0091-O-RAN-Use-Cases-Detailed-Specification- Removal_of_TBDs-v01</td></tr><tr><td>2025.03.05</td><td>16.00.03</td><td>Addition of CRs:</td></tr><tr><td></td><td></td><td>JNPR-2025.02.13-WG1-CR-0098-O-RAN-Use-Cases-Detailed-Specification-Rel- 18-Upgrade-Normative-References-v01</td></tr><tr><td></td><td></td><td>JNPR-2025.02.13-WG1-CR-0099-O-RAN-Use-Cases-Detailed-Specification-Rel- 18-Upgrade-28.552-v01</td></tr><tr><td></td><td></td><td>JNPR-2025.02.13-WG1-CR-0100-O-RAN-Use-Cases-Detailed-Specification-Rel-</td></tr><tr><td></td><td></td><td>18-Upgrade-28.313-v01 JNPR-2025.02.13-WG1-CR-0101-O-RAN-Use-Cases-Detailed-Specification-Rel-</td></tr><tr><td></td><td></td><td>18-Upgrade-37.817-v01 JNPR-2025.02.13-WG1-CR-0102-O-RAN-Use-Cases-Detailed-Specification-Rel-</td></tr><tr><td></td><td></td><td>18-Upgrade-Informative-References-v01</td></tr><tr><td></td><td></td><td>JNPR-2025.02.13-WG1-CR-0103-O-RAN-Use-Cases-Detailed-Specification-Rel- 18-Upgrade-28.624-v01</td></tr><tr><td></td><td></td><td>JNPR-2025.02.13-WG1-CR-0104-O-RAN-Use-Cases-Detailed-Specification-Rel- 18-Upgrade-38.213-v01</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">JNPR-2025.02.13-WG1-CR-0105-O-RAN-Use-Cases-Detalled-Speclficatloh-References-Corrections-v01JNPR-2025.02.13-WG1-CR-0106-O-RAN-Use-Cases-Detailed-Specification-Reference-Fix-v01</td></tr><tr><td colspan="1" rowspan="1">2025.03.20</td><td colspan="1" rowspan="1">16.00.04</td><td colspan="1" rowspan="1">Addition of CR:NOK-2025.02.24- O-RAN.WG1.TS.UCDS-CR0267-ShdORU_UC_SecurityReqmtReference-v03Editorial updates to align to O-RAN TS template v03.00</td></tr><tr><td colspan="1" rowspan="1">2025.03.20</td><td colspan="1" rowspan="1">16.00.05</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2025.03.28</td><td colspan="1" rowspan="1">17.00</td><td colspan="1" rowspan="1">Final version 17.00</td></tr><tr><td colspan="1" rowspan="1">2025.06.19</td><td colspan="1" rowspan="1">17.00.01</td><td colspan="1" rowspan="1">Initial version towards v18.00, starting with v17.00.01 per O-RAN specification revisionnumbering process.Addition of CRs:QCM.AO-2025.05.14-WG1-CR-0001-NES_Carrier_Cell_Switch_Off_On_update_entities-v01QCM.AO-2025.05.14-WG1-CR-0002-NES_Carrier_Cel_Switch_Off_On_update_solutions-v01QCM.AO-2025.05.14-WG1-CR-0003-NES_Carrier_Cell_Switch_Off_On_required_data_update-v01JNPR.AO-2025.05.15-WG1-CR-0107-O-RAN-Use-Cases-Detailed-Specification-RAN_Slice_SLA_Assurance_Use_Case_Improvement-v01ERI.AO-2025.05.01-WG1-UCTG-CR-01- Cell Shaping Optimization-v03</td></tr><tr><td colspan="1" rowspan="1">2025.07.08</td><td colspan="1" rowspan="1">17.00.02</td><td colspan="1" rowspan="1">Addition of CRs:CMCC-2025.02.12-WG1-CR-0029-O-RAN-Use-Cases-Detailed-Specification-RANEdge Computing Resource Information Exposure-v06CMCC-2025.02.11-WG1-CR-0030-O-RAN-Use-Cases-Detailed-Specification-JointCommunication and Computing Optimization for V2X Communications for CCIN-v06CMCC.AO-2025.02.11-WG1-CR-0031-O-RAN-Use-Cases-Detailed-Specification-Multiaspect handover optimization for CCIN-v06Editorial updatesEditorial updates to align to O-RAN TS template v05</td></tr><tr><td colspan="1" rowspan="1">2025.07.10</td><td colspan="1" rowspan="1">17.00.03</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2025.07.18</td><td colspan="1" rowspan="1">17.00.04</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2025.07.18</td><td colspan="1" rowspan="1">17.00.05</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2025.07.18</td><td colspan="1" rowspan="1">18.00</td><td colspan="1" rowspan="1">Final version 18.00</td></tr></table>