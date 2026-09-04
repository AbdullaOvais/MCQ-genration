Technical Report

# O-RAN Working Group 1 Study on O-RAN Slicing

# This is a re-published version of the attached final specification.

For this re-published version, the prior versions of the IPR Policy will apply, except that the previous requirement for Adopters (as defined in the earlier IPR Policy) to agree to an O-RAN Adopter License Agreement to access and use Final Specifications shall no longer apply or be required for these Final Specifications after 1st July 2022.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material on this site for your personal use, or copy the material on this site for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

# O-RAN Working Group 1 Study on O-RAN Slicing

Revision History   

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Author</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2019.12.16</td><td rowspan=1 colspan=1>02.00.01</td><td rowspan=1 colspan=1>Arda Akman (Netsia)</td><td rowspan=1 colspan=1> Initial version of v2.0 (and deletion of v1.0 revision history)</td></tr><tr><td rowspan=1 colspan=1>2019.12.26</td><td rowspan=1 colspan=1>02.00.02</td><td rowspan=1 colspan=1>Arda Akman (Netsia),Tugba Aric1 (Netsia)</td><td rowspan=1 colspan=1>Update to SDO Mapping table to addFault Management-Security Aspects</td></tr><tr><td rowspan=1 colspan=1>2019.12.29</td><td rowspan=1 colspan=1>02.00.03</td><td rowspan=1 colspan=1>Arda Akman (Netsia),Tugba Arici (Netsia)</td><td rowspan=1 colspan=1>Updates to GSMA section to reflect the latest GSMA specs</td></tr><tr><td rowspan=1 colspan=1>2020.01.20</td><td rowspan=1 colspan=1>02.00.04</td><td rowspan=1 colspan=1>Arda Akman (Netsia),Burcu YargiçoğluSahin (Netsia)</td><td rowspan=1 colspan=1>Addition of O1, A1, E2, O2 impact and Deployment Optionssections through CR:-  ORAN-WG1.Netsia_CR_StudyO-RAN-Slicing_20012020</td></tr><tr><td rowspan=1 colspan=1>2020.03.01</td><td rowspan=1 colspan=1>02.00.05</td><td rowspan=1 colspan=1>Arda Akman (Netsia)</td><td rowspan=1 colspan=1>Updated references, abbreviations, deployment options andother editorial updates</td></tr><tr><td rowspan=1 colspan=1>2020.03.09</td><td rowspan=1 colspan=1>02.00.06</td><td rowspan=1 colspan=1>Arda Akman (Netsia)</td><td rowspan=1 colspan=1>Updates to various sections based on review feedback duringWG1 approval process</td></tr></table>

2

# Contents

# Revision History..... 2 ..2

Chapter 1 Introduction. ...4   
1.1 Scope ...... ...... 4   
1.2 References... ..... 4   
1.3 Definitions and Abbreviations ......................... ....... 5   
1.3.1 Definitions...... ..... 5   
1.3.2 Abbreviations ..... ...................................... ...................................................................................... ....... 6   
Chapter 2 Objective... ................................................................. ......7   
Chapter 3 Common Terminology... ................................................................... .....8   
Chapter 4 Slicing in SDOs .   
4.1 Slicing in 3GPP.....   
4.2 Slicing in ONAP .. ........................................................................... 11   
4.3 Slicing Orchestration in 3GPP SA5 and ETSI NFV MANO. .................................................................... 12   
4.4 Slicing in ETSI ZSM .. ................................................................ .... 14   
4.5 Slicing in GSMA .. .. 16   
Chapter 5 O-RAN Slicing Framework . ............................................................................................... ....18   
5.1 O-RAN Slicing Architecture..... ................................................................................................................... 18   
5.1.1 Non-RT RIC.. ............................................................................................................... . 18   
5.1.2 Near-RT RIC.. ........................................................................................................ 18   
5.1.3 O-RAN Central Unit (O-CU) .... ................................................................................................................. 18   
5.1.4 O-RAN Distributed Unit (O-DU).... ........................................................................................................ 18   
5.1.5 A1 Impact...... ............................................................................................................... 19   
5.1.6 E2 Impact ... ....................................................................................................... .. 19   
5.1.7 O1 Impact.... ... 19   
5.1.8 O2 Impact... .. 19   
Chapter 6 Deployment Options . ..20   
Annex A (informative): Additional Information . ..23   
A.1 Slicing SDO Mapping Table.. . 23

Annex ZZZ O-RAN Adopter License Agreement ... ..24

#

# Chapter 1 Introduction

# 1.1 Scope

This Technical Report has been produced by O-RAN Alliance.

The contents of the present document are subject to continuing work within O-RAN WG1 Slicing Task Group and may change following formal O-RAN approval. In the event that O-RAN Alliance decides to modify the contents of the present document, it will be re-released by O-RAN Alliance with an identifying change of release date and an increase in version number as follows:

Release x.y.z where:

x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } = 0 1$ ).   
y the second digit is incremented when editorial only changes have been incorporated in the document.   
z the third digit included only in working versions of the document indicating incremental changes during the editing process.

This document provides common terminology for slicing, an overview of slicing activities in different SDOs (3GPP, ETSI, ONAP, GSMA, etc.) and provides the high level view of O-RAN slicing framework and architecture along with different deployment options.

# 1.2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific. For a specific reference, subsequent revisions do not apply. For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in Release 16. [1] 3GPP TR 21.905: “Vocabulary for 3GPP Specifications” [2] 3GPP TS 23.501: “System Architecture for the 5G System”, Release 16, December 2019 [3] 3GPP TR 28.801: “Study on management and orchestration of network slicing for next generation network”, Release 15, January 2018. [4] 3GPP TS 28.530: “Aspects; Management and orchestration; Concepts, use cases and requirements”, Release 16, January 2020. [5] 3GPP TS 28.541: “Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage $3 ^ { \circ }$ , Release 16, January 2020. [6] 3GPP TS 38.300: “NR and NG-RAN Overall Description”, Release 16, January 2020.

[7] ETSI GR NFV-EVE 012: “Report on Network Slicing Support with ETSI NFV Architecture Framework”, Release 3, December 2017.

[8] ETSI GS NFV-IFA 008: “Ve-Vnfm reference point - Interface and Information Model Specification”, Release 2, February 2018.

] ETSI GS NFV-IFA 013: “Os-Ma-Nfvo reference point - Interface and Information Model Specification”, Release 2, February 2018.

[10] GSMA: “An Introduction to 5G Network Slicing”, 2017.

[11] GSMA: “From Vertical Industry Requirements to Network Slice Characteristics”, August 2018.

GSMA: “Network Slicing, Use Case Requirements”, April 2018.

[13] GSMA: ”Generic Network Slice Template”, Release 2, October 2019

14] ETSI GS ZSM 003: “Zero-touch Network and Service Management (ZSM); End to end management and orchestration of network slicing”.

# 1.3 Definitions and Abbreviations

# 1.3.1 Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

A1: Interface between non-RT RIC and Near-RT RIC to enable policy-driven guidance of Near-RT RIC applications/functions, and support AI/ML workflow.

E2: Interface connecting the Near-RT RIC and one or more O-CU-CPs, one or more O-CU-UPs, and one or more ODUs.

FCAPS: Fault, Configuration, Accounting, Performance, Security.

Intents: A declarative policy to steer or guide the behaviour of RAN functions, allowing the RAN function to calculate the optimal result to achieve stated objective.

near-RT RIC: O-RAN near-real-time RAN Intelligent Controller: a logical function that enables near-real-time control and optimization of RAN elements and resources via fine-grained data collection and actions over E2 interface.

non-RT RIC: O-RAN non-real-time RAN Intelligent Controller: a logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policybased guidance of applications/features in near-RT RIC.

NMS: A Network Management System.

O-CU: O-RAN Central Unit

O-CU-CP: O-RAN Central Unit – Control Plane: a logical node hosting the RRC and the control plane part of the PDCP protocol.

O-CU-UP: O-RAN Central Unit – User Plane: a logical node hosting the user plane part of the PDCP protocol and the SDAP protocol.

O-DU: O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

O-RU: O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

O1: Interface between management entities (NMS/EMS/MANO) and O-RAN managed elements, for operation and management, by which FCAPS management, Software management, File management shall be achieved.

RAN: Generally referred as Radio Access Network. In terms of this document, any component below near-RT RIC per O-RAN architecture, including O-CU/O-DU/O-RU.

# 1.3.2 Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

<table><tr><td>13</td><td>eNB</td><td>eNodeB (applies to LTE)</td></tr><tr><td>14</td><td>gNB</td><td>gNodeB (applies to NR)</td></tr><tr><td>15</td><td>KPI</td><td>Key Performance Indicator</td></tr><tr><td>16</td><td>KQI</td><td>Key Quality Indicator</td></tr><tr><td>17</td><td>Near-RT RIC</td><td>Near-RT RIC</td></tr><tr><td>18</td><td>Non-RT RIC</td><td>Non-Real-Time RIC</td></tr><tr><td>19</td><td>NS</td><td>Network Service</td></tr><tr><td>20</td><td>O-CU</td><td>O-RAN Central Unit</td></tr><tr><td>21</td><td>O-DU</td><td>O-RAN Distributed Unit</td></tr><tr><td>22</td><td>O-RU</td><td>O-RAN Radio Unit</td></tr><tr><td>23</td><td>PNF</td><td>Physical Network Function</td></tr><tr><td>24</td><td>PRB</td><td>Physical Resource Block</td></tr><tr><td>25</td><td>RIC</td><td>O-RAN RAN Intelligent Controller</td></tr><tr><td>26</td><td>RRM</td><td>Radio Resource Management</td></tr><tr><td>27</td><td>SDO</td><td>Standards Developing Organizations (For ex: 3GPP, ETSI, ONAP, O-RAN)</td></tr><tr><td>28</td><td>SMO</td><td>Service and Management Orchestration</td></tr><tr><td>29</td><td>VNF</td><td>Virtual Network Function</td></tr><tr><td>30</td><td>NSD</td><td>NFV Network Service Descriptors</td></tr><tr><td>31</td><td>NST</td><td>Network Slice Templates</td></tr></table>

# Chapter 2 Objective

The current document aims to define the common terminology for slicing, captures slicing activities in different SDOs (3GPP, ETSI, ONAP, GSMA, etc.) and provides the high level view of O-RAN slicing framework and architecture, with the purpose of helping identify requirements for O-RAN defined interfaces and functions, eventually leading to formal drafting of interface specifications.

# Chapter 3 Common Terminology

In this chapter, it is aimed to list slice specific definitions to agree on a common terminology.

Network slice instance: a set of network functions and the resources for these network functions which are arranged and configured, forming a complete logical network to meet certain network characteristics. [3]

Network slice subnet instance: a set of network functions and the resources for these network functions which are arranged and configured to form a logical network. [3]

Network slice subnet template: description of the structure (and contained components) and configuration of the network slice subnet. [3]

Network slice template: description of the structure (and contained components) and configuration of a network slice. [3]

Physical resource isolation: regime of resource management when a physical resource used by one network slice instance cannot be shared with another network slice instance. [3]

# Chapter 4 Slicing in SDOs

# 4.1 Slicing in 3GPP

Architecture Including Network Slicing

Network slicing concept is considered as one of the key feature of 5G networks. Service-based 5G architecture including network slicing is defined in 3GPP TS 23.501 [2]. Figure 4.1-1 represents the non-roaming reference architecture and interfaces utilised in control plane.

![](images/d56908ba78584a36bc3005a98f42d108b3347c730a6a6c7ef34763b0a3ae04ad.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-1: Reference architecture

Network Slice Identification and Service Types

A network slice is always defined with RAN part and CN part in a PLMN (see Clause 5.15.1 in [2]). The network slicing support is based on the principle that flows of the different slices handled by different PDU sessions. Granularity of slice awareness is in PDU session level (see Clause 16.3.1 in [6]).

S-NSSAI is a unique identifier for each network slice. NSSAI (Network Slice Selection Assistance Information) includes one or a list of s-NSSAIs which is a combination of mandatary SST (Slice/Service Type) and an optional SD (Slice Differentiator). The operator may choose to serve same Slice/Service Type but using different s-NSSAIs in case of serving same features to different group of users.

To support roaming use cases more efficiently, some SST values are standardised for the most common service types as shown in the Table 4.1-2 defined as in 3GPP TS 23.501 [2].

Table 4.1-2: Standardized SST values   

<table><tr><td rowspan=1 colspan=1>Slice/Service type</td><td rowspan=1 colspan=1>SST value</td><td rowspan=1 colspan=1>Characteristics</td></tr><tr><td rowspan=1 colspan=1>eMBB</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Slice suitable for the handling of 5G enhanced Mobile Broadband.</td></tr><tr><td rowspan=1 colspan=1>URLLC</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1> Slice suitable for the handling of ultra- reliable low latency communications.</td></tr><tr><td rowspan=1 colspan=1>MIoT</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Slice suitable for the handling of massive IoT.</td></tr><tr><td rowspan=1 colspan=1>V2X</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Slice suitable for the handling of V2X services.</td></tr></table>

A single UE can connect one or more Network Slice instances simultaneously. The maximum number of simultaneous connection is 8 per UE. If UE has multiple simultaneous connections to the different slices, only one signalling connection is used.

5G QoS model is based on QoS Flows. GBR QoS flows require guaranteed flow bit rate. Non-GBR QoS flows, by contrast, do not require guaranteed flow bit rate. QoS differentiation is supported within a network slice.

NG-RAN should support resource management between slices. SLA is provided between slices. Multiple slices could be supported on a single RAN and resource isolation is maintained between slices. Shared resources should be managed by RRM policies or other mechanisms to prevent SLA violations for other slices.

Slice availability depends on the deployment scenario. Some slices might be offered globally while some others might be only in a local area.

# Selection of a Network Slice

AMF selection procedure is made based on NSSAI or Temp ID. NSSAI is used when UE does not have Temp ID. Otherwise, RAN uses the NSSAI reported by UE during initial access procedure to select appropriate AMF. If both of them is not available, RAN routes UE to a default AMF.

After RRC connection and AMF Selection are completed successfully, selected AMF sends Initial Context Setup Request message to RAN to complete UE context. This message includes allowed NSSAI, s-NSSAI for each PDU session. When required resources and policies for the selected slice(s) are ready, RAN side sends an Initial Context Setup Response message to AMF 3GPP TS 38.300 [6].

# Management and Orchestration of Network Slicing

Network slice is a logical network that provides specific network capabilities and network characteristics. There are some aspects that a network slice includes. A deployed network slice forms a Network Slice Instance (NSI). An NSI has all the physical and logical resources and the functionalities to serve a business use case. The NSI contains Core Part and Access Part. To create an NSI, configurations and policies are required for each instance. The NSI lifecycle includes commissioning, operation and decommissioning phases as shown in Fig 4.1-2.

![](images/929892d6819bafe9f44e1b7f8d9fb5ff848e2e6a57333f0c8e45f8bb39862646.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-2: NSI lifecycle

In the preparation phase NSI does not exist and necessary preparations are handled, such as network slice design, capacity planning and on-boarding. Commissioning phase includes the creation of the NSI where all needed resources are allocated and configured per slice requirements. Operation phase is the state that NSI is operating and supporting services to the specified types. In the activation step, any action required to make NSI active is included. Supervision, reporting and modification steps are involved in operation phase. To illustrate, KPI reporting, reconfiguration of NSI or scaling are used in these phases. Decommissioning phase involves termination of the NSI and releasing of the resources assigned to it (see Clause 4.3.1 in [4]).

# Network Resource Model and RRM Slice Policies

3GPP TS 28.541 [5] has introduced the Information Model in the Network Resource Model (NRM) to fulfill management and orchestration of 5G networks. Regarding the network slicing feature modeling at the NRCellCU level, the model basically lists the s-NSSAI(s) supported in the cell and RRM policy to share resources among listed slices. RRMPolicyType attribute is used to describe RRM policy to be applied.

# 4.2 Slicing in ONAP

ONAP 5G slicing activity is ongoing in Frankfurt R6 release. ONAP R5 includes the feature of Network Slicing modeling as a prerequisite for Slicing orchestration that is work in progress in R6. The Network Slice model leverages the shared service/resource approach that is essential for modeling the network slice where VNF’s/PNF’s may be shared by several slices.

The shared service approach is similar to ETSI NFV nested services approach, so its TOSCA implementation may be easily translated into Network Service descriptors defined by the ETSI NFV-SOL001 specification for TOSCA based NFV descriptors.

The graphical representation of the example of modelling the eMBB Network Slice having 3 slice segments (RAN, transport and core) is shown below in Figure 4.2-1.

![](images/58896cbcadacb2ad71264e2098c7d8996ec3051c1cf50aa7d861db27d095ca04.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.2-1: Example model of eMBB Network Slice

Nested Network Service is the approach for shared resources (VNF/NS)

 Nested network service TOSCA implementation in ETSI NFV-SOL001 C PNFD may be part of Nested Service

Sharing of Network Slice resources (PNF’s and VNF’s) for ONAP release 6 is proposed using Nested services approach (based on work done for Release 5) including wrapping PNFs/VNF’s within Network Services and defining operations and properties on Service level. The Network slicing orchestration in ONAP R6 will include assigning workflows to the operations.

![](images/f85c5cc2589607d315de23e3c628f5e2b9f08f86198d5326293e194e2674dd2d.jpg)

> **Image Summary:** (Summary not available)
  
Following this approach, the topology model for O-RAN segment would be as shown below in Figure 4.2-2:   
Figure 4.2-2: High level O-RAN topology model

# 4.3 Slicing Orchestration in 3GPP SA5 and ETSI NFV MANO

According to ETSI NFV Network Slicing Report [7], network slicing has been defined by different SDOs, there is no common definition for network slicing. Therefore, understanding of network slicing is different from each other. Nonetheless, the report does not introduce use cases or features but analyses network slicing in external SDOs. In this report, how these external use cases should be mapped to NFV and the ETSI NFV architecture is explained.

As stated in 3GPP TR 28.801 [3], a network slice may contain one or more network slice subnets and each of them includes one or more network functions. VNFs and PNFs are managed as these network functions in the ETSI NFV architecture. Related to network slicing management, there are three different management functions identified in 3GPP TR 28.801 [3]:

 Communication Service Management Function (CSMF): translates the communication service related requirement to network slice related requirements.   
 Network Slice Management Function (NSMF): responsible for management and orchestration of NSI. Provides communication with the Network Slice Subnet Management Function (NSSMF) and Communication Service Management Function.   
 Network Slice Subnet Management Function (NSSMF): responsible for management and orchestration of NSSI.

As shown in the Figure 4.3-1, Os-Ma-nfvo reference point is used for interaction between 3GPP slice management functions and NFVO. Similarly, Ve-Vnfm-em reference point is used for exchanges between NFMF and VNF Manager. Further analysis is required on these reference points to apply deployment scenarios including 3GPP network slicing related management functions and NFV-MANO. Further details are available in ETSI GS NFV-IFA 008 [8] and ETSI GS NFV-IFA 013 [9].

![](images/a95a9a51c8922fbf5cc4196c915665902bdbdadcda2a5c4bda3cba20a13b20f8.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.3-1: Network slice management in an NFV framework

Figure 4.3-2 shows an example of a 5G network realized by an end-to-end network slice, consisting of network slice subnet #1 for 5G core networks and network slice subnet $\# 2$ for 5G radio networks (see Clause 4.1.3 in TS 28.530 [4]).

![](images/07f4b42f759df0a85bc0efa59abea696febf8e60ce5fd51f3e9a93a95e5ef651.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.3-2: 5G network with network slicing

The following diagram (Figure 4.3-3) shows the interaction between 3GPP and ETSI NFV to create a network slice subnet instance for RAN network functions.

![](images/cbf43df8b2b4cb276bbf8200483df2aaa83b33243bcf4e00e4be3aa538cdc78a.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.3-3: High level view of network slice subnet instance creation

1. NSMF sends request to allocate a network slice subnet instance for RAN network functions, e.g. O-CU, O-DU, and O-RU.

2. NSSMF decides to instantiate a Network Service (NS) instance for a new network slice subnet instance.

3. NFVO sends request to instantiate the VNFs for O-CU, O-DU.

4. VNFM instantiates VNFs and notifies NFMF that VNFs have been instantiated

5. VNFM responds to NFVO informing that VNFs have ben instantiated.

6. NFVO notify NSSMF that NS has been instantiated.

7. NSSMF responds to NSMF with status equals to successful for the operation of network slice subnet instance creation.

# 4.4 Slicing in ETSI ZSM

The management services (MnSs) for end-to-end network slicing are provided by a set of management domains (MDs). Including that for network slicing defined by 3GPP SA5 and that for NFV defined by ETSI NFV, provides various MnSs as shown in Figure 4.4-1 [14].

![](images/9dfb6f0713175ba5842aad9c9f1ee1bbdef730d1a1b7a5362f88c52e35ca9cc6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.4-1: Example of MDs to support network slicing using NFV

In this operator deployment example:

 E2E Service MD provides MnSs for E2E network slices/network slice subnets, e.g. Service Orchestration service (Serv-Orch), which orchestrates the individual network slice subnets (NSSs) provided by Radio Access Network (RAN), Transport Network (TN) and Core Network (CN), and stitches them into a E2E network slice subnet being exposed as a network slice. The MnSs in this MD may also manage NSSs of Data Network (aka. SGi Network) using MD for NFV. It is expected that parts of specifications developed by 3GPP SA5 are re-used for the MnSs in this MD. This MD exposes e.g. management capabilities of E2E network slices (provisioning, performance assurance, fault supervision, etc.).

MD for NSS in TN provides MnSs for NSSs of TN, e.g. Dom-Orch service. This MD may consume TN resources outside of ZSM supported by e.g. Configuration Management service(s) (Conf-Mgmt). It is expected that parts of specifications developed by e.g. BBF, MEF, IETF and/or ETSI NFV are re-used for the MnSs in this MD. This MD exposes e.g. management capabilities of NSS of TN (provisioning, performance assurance, fault supervision, etc.).

MD for NSS in RAN provides MnSs for NSSs of RAN, e.g. Dom-Orch service. This MD may consume application level RAN resources (i.e. application part of RAN Network Functions) outside of ZSM supported by e.g. ConfMgmt, and it may also consume MnSs for Network Services which include virtualized resources from MD for NFV. It is expected that parts of specifications developed by 3GPP SA5 are re-used for the MnSs in this MD. This MD exposes e.g. management capabilities of NSS of RAN (provisioning, performance assurance, fault supervision, etc.).

MD for NSS in CN provides MnSs for NSSs of CN, e.g. Dom-Orch service. This MD may consume application level CN resources outside of ZSM (i.e. application part of CN Network Functions) supported by e.g. Conf-Mgmt, and it may also consume MnSs for Network Services which include virtualized resources from MD for NFV. It is expected that parts of specifications developed by 3GPP SA5 are re-used for the MnSs in this MD. This MD exposes e.g. management capabilities of NSS of CN (provisioning, performance assurance, fault supervision, etc.).

 MD for NFV provides MnSs for NFV Network Service(s) (at resource level), e.g. Dom-Orch service (NFV Orchestrator). This MD may also have Conf-Mgmt (VNF Manager) and MnSs for managing compute/network/storage resources (Virtualized Infrastructure Manager). It is expected that parts of specifications developed by ETSI NFV are re-used for the MnSs in this MD. This MD exposes e.g. management capabilities related to NFV Network Services (Create/Read/Update/Delete of the Network Services, on-boarding of catalogues for those, etc.).

Using the operator deployment scenario in Figure 4.4-1, a service over an E2E network slice instance comprising of RAN access $^ +$ virtualized application can be deployed. Figure 4.4-2 describes the particular instance of service consumption across the domains.

![](images/c91f3f76408c8ce16626761ff36936a5401f885baa018f0b447f8ca4f43d4e48.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.4-2: Example management services’ consumption to show E2E slice deployment.

The steps of deployment are:

1) The E2E service breaks up the E2E network slicing deployment requests into a) Part of the E2E network slice (for fixed users and Transport) $^ +$ 3GPP Core Part of the E2E network slice (for Mobile users) $^ +$ 3GPP RAN part of the E2E network slice $^ +$ application service (Virtualized)

2) A part of the E2E network slice is handed over to the TN management domain using the appropriate management services exposed by the transport management domain.

3) The 3GPP core part (CP: AMF/SMF, UPF, N1,N6) goes to the core management system a) The core management domain requests the connectivity (N1, N6) to the transport management domain b) The Core management domain hands over the VNFs (AMF/SMF, UPF…) to the virtualization management domain

4) The access part goes to radio access service management domain a) The radio access management domain uses the management services of the virtualization management domain to deploy the virtualized RAN part

5) The virtualized application AS is handed over to be deployed by the virtualization management system.

# 4.5 Slicing in GSMA

GSMA published a document [10] which aims to provide an introduction to network slicing functionality. It shows how network slicing can be used by business customers. Business customers are referred as users of the 5G services which could be enterprises, specialized industries or individuals. Network slicing is analyzed from the business customers’ point of view in addition to set of use cases.

It is highlighted that different business customers has various requirements like ultra-reliable services, ultra-highbandwidth communication or extremely low latency. Running multiple logical networks on a common physical infrastructure is enabled by network slicing. Network slice contained 5G networks allow business customers to have connectivity having different business requirements which are governed by SLAs.

Network slicing provides ability to customize capabilities and functionality of the mobile network offered to business customers. Customized services are classified as Network Connection Service and Network Resource Service. The first one indicates the connectivity functionalities of the customer e.g. near real-time latency, guaranteed SLA, seamless mobility and energy efficiency. The second one describes the case that customers are granted access to the operator network resources to run their proprietary applications. In addition to network resource services, the network is able to provide additional services i.e. big data analytics, cloud computing, edge computing and positioning.

GSMA lists some use cases for the business customers to underline potential of network slicing. Industry sectors including automotive, logistic, healthcare, government are indicated as potential application of the network slicing.

As the successor of the previous document, GSMA conducted a study on the service requirements expressed by various business customers. In addition to detailed analysis of the service requirements, recommendations for the industry has been provided. Finally, a generic slice template has been introduced and all the attributes a network slice could have, has been discussed [12]. Generic Slice Template (GST) lists set of attributes with names and units that characterise a network slice (e.g. throughput, supported functionalities). GST categorises the attributes into character attributes and scalability attributes. Former defines generic slice attributes independent from the NSC and NSP (e.g. latency, throughput), while latter provides information about scalability of the slice e.g. number of terminals, area of the service.

Another concept defined to represent network slices with a common language is Network Slice Type (NEST). The NEST is a GST filled with proper values based on a specific business use case. Moreover, NEST is the input for the network slice preparation phase which leads to service profile definition in 3GPP.

GSMA Network Slicing Taskforce (GSMA-NEST) has two main objectives which are defining the GST [13] and identifying set of slices whose characteristics are accepted by the industry. GSMA-NEST aims to deliver NESTs with industry approved slice characteristics which could be used by the operators [11].

# Chapter 5 O-RAN Slicing Framework

# 5.1 O-RAN Slicing Architecture

# 5.1.1 Non-RT RIC

The fundamental role of the Non-RT RIC in O-RAN architecture is to apply AI/ML based algorithms to provide innovative RAN use cases. Hence, Non-RT RIC is a key component to allow advanced RAN slicing technology to be applied in O-RAN framework. For this purpose, Non-RT RIC should be aware of RAN slices and related slice properties/configurations as well as slice performance metrics to actively assist slice assurance through optimization methods, including AI/ML models.

To generate AI/ML models to be deployed in the Near-RT RIC, Non-RT RIC retrieves slice specific PMs and configuration parameters of the slices and optionally external enrichment information from external servers. Complex problems for Near-RT RIC e.g. applying RRM policies can be tackled by learning capabilities of AI/ML. Training models enable non-real-time optimization of the slice specific parameters over O1 interface. Moreover, these performance, configuration and other data are used to assist Near-RT RIC to provide dynamic slice optimization. Appling dynamic slice optimization in the Near-RT RIC is used to prevent SLA violations between the slices.

# 5.1.2 Near-RT RIC

Near-RT RIC enables xApps to control RAN elements and their resources through the E2 interface in near real-time (sub second). Similar to Non-RT RIC, Near-RT RIC xApps should be aware of RAN slices and can utilize slice aware algorithms for slice SLA assurance purposes. Once the slices are up and running, slice specific PMs from E2 nodes will be gathered and sent to Near-RT RIC and Near-RT RIC will use these PMs and the slice configuration data to apply dynamic slice optimization to assure slice SLAs, through E2 interface (to be discussed).

These dynamic slice optimization algorithms can be built into the Near-RT RIC, can be guided from Non-RT RIC through A1 policies, or can be sent down as AI/ML models from Non-RT RIC.

# 5.1.3 O-RAN Central Unit (O-CU)

In order to apply RAN slicing in O-RAN framework, both O-CU and O-DU needs to support slicing features as defined by 3GPP. Furthermore slicing can be enhanced with the assistance of O-RAN specific Near-RT RIC dynamic slice optimization through E2 interface.

O-CU is the O-RAN entity which runs the upper layer protocols of the RAN stack, such as Radio Resource Management. Since RRM is responsible for managing resources, and in case of slicing – the allocation of resources between slices, OCU needs to execute slice specific resource allocation strategies and drive O-DU(s) similarly. O-CU will interact with Near-RT RIC to provide slice specific PMs as well as getting dynamic guidance through E2 interface.

# 5.1.4 O-RAN Distributed Unit (O-DU)

O-DU is the O-RAN entity which runs the lower layer protocols of the RAN stack, including MAC layer which is the layer that schedules Physical Resource Blocks to UEs. As part of slicing, MAC layer needs to allocate PRBs according to the RRM strategies provided by the Operator and slice management entities. O-DU will receive the slice configuration

parameters from O1 interface, and dynamic slice optimization guidance from RIC through E2 interface and will provide slice specific PMs through O1 interface to SMO and E2 interface to Near-RT RIC.

# 5.1.5 A1 Impact

A1 interface will be used to support policy based guidance for slicing use cases, such as SLA assurance. In addition to policy guidance towards Near-RT RIC, Non-RT RIC should be able to receive feedback related to deployed policies over A1 interface. In case of external data enrichment, Non-RT RIC should be able to transfer slice specific enrichment data to Near-RT RIC over A1 interface as well.

# 5.1.6 E2 Impact

E2 interface will be used to drive E2 nodes’ slice configuration and behaviour, such as slice based radio resource allocations, scheduling policies, and configuration policies that may affect performance characteristics of the corresponding network slice. Near-RT RIC should be able to configure and receive slice specific performance data from the E2 nodes over the E2 interface for near real-time optimization (as compared to PMs collected over the O1 interface, which is a slower loop). Slice specific PMs can include PRB utilization, average delay and DRB related measurements that are already defined in 3GPP. However, E2SM(s) can be extended to support non-3GPP slice specific PM collection so that policy control algorithms running on the Near-RT RIC are improved to meet the slice SLA requirements.

# 5.1.7 O1 Impact

The primary role of O1 interface is to enable slice specific configuration of O-RAN nodes based on the service requirements. 3GPP 28.541 [5] has defined the Information Models to list attributes of the slice profiles with the slice specific requirements, including RRM policy attributes to provide ratio of radio resources to split among the supported slices. In addition to slice specific configuration capabilities, O1 interface is used to gather slice specific performance metrics and fault information from O-RAN Nodes. As extensions to O-RAN specific slicing configuration and performance measurement attributes are defined, these information will be sent over O1 interface as well.

# 5.1.8 O2 Impact

O2 is the interface used for life cycle management of virtual O-RAN network functions. In case of network slicing, after the preparation phase, SMO might instantiate necessary O-RAN network functions (such as Near-RT RIC, O-CU-CP, OCU-UP, O-DU) through instantiation procedures as part of the RAN NSSI creation and provisioning, NSSI modification and NSSI deletion. It is expected that Non-RT RIC is instantiated as part of SMO and does not require any lifecycle management activities.

# Chapter 6 Deployment Options

This section provides possible deployment options with respect to network slice management topology and their possible effects on O-RAN slicing architecture. Based on 3GPP specifications Network Slice Management Function (NSMF) and Network Slice Subnet Management Function (NSSMF) are responsible for end-to-end slice management and slice subnet management respectively. Within the scope of O-RAN, RAN slice subnet management function is the primary focus including but not limited to its interactions with the Service Management and Orchestration Framework. Possible architectural impacts of different deployment options are planned to be investigated and captured in O-RAN Slicing Architecture Specification document.

In the following sub sections, four possible deployment options are presented. Please note that while ETSI based NFVO/VNFM interface types are depicted as examples, depending on SMO type these interfaces and NFVO/VNFM components can be different. As other SMOs (such as ONAP) make progress with RAN slicing, the relevant interfaces can be captured in the next iterations of this document.

# Option 1

In this option, both NSMF and NSSMF are deployed within the SMO.

![](images/5ce02cc5b805eef836fff314fffb65334dd6c727cbb38d622abe876b48ce8595.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3: NSMF and NSSMF are deployed within the SMO

# Option 2

In this case, both NSMF and NSSMF are deployed outside the SMO.

![](images/a43107d08df8c4193818b54a437cc9dec56027860b3bdf967e7c82b61497ef12.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4: External deployment of NSMF and NSSMF

# Option 3

In this option, NSMF is placed within SMO. However, NSSMF is deployed outside the SMO.

![](images/39606a36ee698d4e8175e11802d3ad1b9072ae5720674977ead57341fab686ef.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5: External NSSMF deployment

# Option 4

In this case, NSMF is in the outside of SMO while NSSMF is deployed within SMO.

![](images/fba1fc31b4ea60c8e6eece54de6804f6524ffb62b0f3029502d6521866aee14b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6: NSSMF within the SMO

2

# Annex A (informative): Additional Information

# A.1 Slicing SDO Mapping Table

<table><tr><td rowspan=1 colspan=1>Areas</td><td rowspan=1 colspan=1>3GPP</td><td rowspan=1 colspan=1>ONAP</td><td rowspan=1 colspan=1>ETSI OSM</td><td rowspan=1 colspan=1>GSMA</td><td rowspan=1 colspan=1>ETSI ZSM</td></tr><tr><td rowspan=1 colspan=1>Use cases and highlevel requirements</td><td rowspan=1 colspan=1>3GPP TS 22.261</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Network SlicingUse CaseRequirementsGSMA-NEST(NetworkSlicing TaskForce)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Architecturalrequirements</td><td rowspan=1 colspan=1>3GPP TS 23.5013GPP TS 23.502(Procedures involving slicing)3GPP TR 28.801</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Management andorchestration</td><td rowspan=1 colspan=1>3GPP TS 28.5313GPP TS 28.5303GPP TS 28.5413GPP TR 28.801</td><td rowspan=1 colspan=1>R4 (Dublin) forNetwork SliceModel,R5 (El Alto) forOrchestration ofNetwork SlicingModel</td><td rowspan=1 colspan=1>ETSI GSNFV-IFA 014ETSI GSNFV-IFA 013(Os-Ma-nfvo)ETSI GSNFV-IFA 008(Ve-Vnfm)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ETSI GSZSM 002(ReferenceArchitecture)</td></tr><tr><td rowspan=1 colspan=1>Slice Configuration</td><td rowspan=1 colspan=1>3GPP TS 28.5313GPP TS 28.541</td><td rowspan=1 colspan=1>TOSCA basedservice andnetwork slicemodelling</td><td rowspan=1 colspan=1>ETSI GSNFV-IFA 014(NetworkServiceTemplatesSpecification)</td><td rowspan=1 colspan=1>NG.116 -GenericNetwork SliceTemplate(attributes arelisted)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Security aspects ofnetwork slicing</td><td rowspan=1 colspan=1>3GPP TR 33.811</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Slice specificPerformanceManagement (PM),KPIs</td><td rowspan=1 colspan=1>3GPP TS 28.5523GPP TS 28.554</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Fault Management</td><td rowspan=1 colspan=1>3GPP TS 28.8013GPP TS 28.5303GPP TS 28.515-5173GPP TS 32.1113GPP TS 28.545(Fault Supervision)3GPP TS 28.545</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# Annex ZZZ O-RAN Adopter License Agreement

BY DOWNLOADING, USING OR OTHERWISE ACCESSING ANY O-RAN SPECIFICATION, ADOPTER AGREES TO THE TERMS OF THIS AGREEMENT.

This O-RAN Adopter License Agreement (the “Agreement”) is made by and between the O-RAN Alliance and the entity that downloads, uses or otherwise accesses any O-RAN Specification, including its Affiliates (the “Adopter”).

This is a license agreement for entities who wish to adopt any O-RAN Specification.

# SECTION 1: DEFINITIONS

1.1 “Affiliate” means an entity that directly or indirectly controls, is controlled by, or is under common control with another entity, so long as such control exists. For the purpose of this Section, “Control” means beneficial ownership of fifty $( 5 0 \% )$ percent or more of the voting stock or equity in an entity.

1.2 “Compliant Portion” means only those specific portions of products (hardware, software or combinations thereof) that implement any O-RAN Specification.

1.3 “Adopter(s)” means all entities, who are not Members, Contributors or Academic Contributors, including their Affiliates, who wish to download, use or otherwise access O-RAN Specifications.

1.4 “Minor Update” means an update or revision to an O-RAN Specification published by O-RAN Alliance that does not add any significant new features or functionality and remains interoperable with the prior version of an O-RAN Specification. The term “O-RAN Specifications” includes Minor Updates.

1.5 “Necessary Claims” means those claims of all present and future patents and patent applications, other than design patents and design registrations, throughout the world, which (i) are owned or otherwise licensable by a Member, Contributor or Academic Contributor during the term of its Member, Contributor or Academic Contributorship; (ii) such Member, Contributor or Academic Contributor has the right to grant a license without the payment of consideration to a third party; and (iii) are necessarily infringed by implementation of a Final Specification (without considering any Contributions not included in the Final Specification). A claim is necessarily infringed only when it is not possible on technical (but not commercial) grounds, taking into account normal technical practice and the state of the art generally available at the date any Final Specification was published by the O-RAN Alliance or the date the patent claim first came into existence, whichever last occurred, to make, sell, lease, otherwise dispose of, repair, use or operate an implementation which complies with a Final Specification without infringing that claim. For the avoidance of doubt in exceptional cases where a Final Specification can only be implemented by technical solutions, all of which infringe patent claims, all such patent claims shall be considered Necessary Claims.

1.6 “Defensive Suspension” means for the purposes of any license grant pursuant to Section 3, Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates, may have the discretion to include in their license a term allowing the licensor to suspend the license against a licensee who brings a patent infringement suit against the licensing Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates.

# SECTION 2: COPYRIGHT LICENSE

2.1 Subject to the terms and conditions of this Agreement, O-RAN Alliance hereby grants to Adopter a nonexclusive, nontransferable, irrevocable, non-sublicensable, worldwide copyright license to obtain, use and modify O-RAN Specifications, but not to further distribute such O-RAN Specification in any modified or unmodified way, solely in furtherance of implementations of an O-RAN Specification.

2.2 Adopter shall not use O-RAN Specifications except as expressly set forth in this Agreement or in a separate written agreement with O-RAN Alliance.

# SECTION 3: FRAND LICENSE

3.1 Members, Contributors and Academic Contributors and their Affiliates are prepared to grant based on a separate Patent License Agreement to each Adopter under Fair, Reasonable And Non-Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Portions; provided, however, that such license shall not extend: (a) to any part or function of a product in which a Compliant Portion is incorporated that is not itself part of the Compliant Portion; or (b) to any Adopter if that Adopter is not making a reciprocal grant to Members, Contributors and Academic Contributors, as set forth in Section 3.3. For the avoidance of doubt, the foregoing license includes the distribution by the Adopter’s distributors and the use by the Adopter’s customers of such licensed Compliant Portions.

3.2 Notwithstanding the above, if any Member, Contributor or Academic Contributor, Adopter or their Affiliates has reserved the right to charge a FRAND royalty or other fee for its license of Necessary Claims to Adopter, then Adopter is entitled to charge a FRAND royalty or other fee to such Member, Contributor or Academic Contributor, Adopter and its Affiliates for its license of Necessary Claims to its licensees.

3.3 Adopter, on behalf of itself and its Affiliates, shall be prepared to grant based on a separate Patent License Agreement to each Members, Contributors, Academic Contributors, Adopters and their Affiliates under FRAND terms and conditions with or without compensation (royalties) a nonexclusive, nontransferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Portions; provided, however, that such license will not extend: (a) to any part or function of a product in which a Compliant Portion is incorporated that is not itself part of the Compliant Portion; or (b) to any Members, Contributors, Academic Contributors, Adopters and their Affiliates that is not making a reciprocal grant to Adopter, as set forth in Section 3.1. For the avoidance of doubt, the foregoing license includes the distribution by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ distributors and the use by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ customers of such licensed Compliant Portions.

# SECTION 4: TERM AND TERMINATION

4.1 This Agreement shall remain in force, unless early terminated according to this Section 4.

4.2 O-RAN Alliance on behalf of its Members, Contributors and Academic Contributors may terminate this Agreement if Adopter materially breaches this Agreement and does not cure or is not capable of curing such breach within thirty (30) days after being given notice specifying the breach.

4.3 Sections 1, 3, 5 - 11 of this Agreement shall survive any termination of this Agreement. Under surviving Section 3, after termination of this Agreement, Adopter will continue to grant licenses (a) to entities who become Adopters after the date of termination; and (b) for future versions of O-RAN Specifications that are backwards compatible with the version that was current as of the date of termination.

# SECTION 5: CONFIDENTIALITY

Adopter will use the same care and discretion to avoid disclosure, publication, and dissemination of ORAN Specifications to third parties, as Adopter employs with its own confidential information, but no less than reasonable care. Any disclosure by Adopter to its Affiliates, contractors and consultants should be subject to an obligation of confidentiality at least as restrictive as those contained in this Section. The foregoing obligation shall not apply to any information which is: (1) rightfully known by Adopter without any limitation on use or disclosure prior to disclosure; (2) publicly available through no fault of Adopter; (3) rightfully received without a duty of confidentiality; (4) disclosed by O-RAN Alliance or a Member, Contributor or Academic Contributor to a third party without a duty of confidentiality on such third party; (5) independently developed by Adopter; (6) disclosed pursuant to the order of a court or other authorized governmental body, or as required by law, provided that Adopter provides reasonable prior written notice to O-RAN Alliance, and cooperates with O-RAN Alliance and/or the applicable Member, Contributor or Academic Contributor to have the opportunity to oppose any such order; or (7) disclosed by Adopter with O-RAN Alliance’s prior written approval.

# SECTION 6: INDEMNIFICATION

Adopter shall indemnify, defend, and hold harmless the O-RAN Alliance, its Members, Contributors or Academic Contributors, and their employees, and agents and their respective successors, heirs and assigns (the “Indemnitees”), against any liability, damage, loss, or expense (including reasonable attorneys’ fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, investigations, actions, demands or judgments arising out of Adopter’s use of the licensed O-RAN Specifications or Adopter’s commercialization of products that comply with O-RAN Specifications.

# SECTION 7: LIMITATIONS ON LIABILITY; NO WARRANTY

EXCEPT FOR BREACH OF CONFIDENTIALITY, ADOPTER’S BREACH OF SECTION 3, AND ADOPTER’S INDEMNIFICATION OBLIGATIONS, IN NO EVENT SHALL ANY PARTY BE LIABLE TO ANY OTHER PARTY OR THIRD PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES RESULTING FROM ITS PERFORMANCE OR NON-PERFORMANCE UNDER THIS AGREEMENT, IN EACH CASE WHETHER UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, AND WHETHER OR NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES.

O-RAN SPECIFICATIONS ARE PROVIDED “AS IS” WITH NO WARRANTIES OR CONDITIONS WHATSOEVER, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE. THE O-RAN ALLIANCE AND THE MEMBERS, CONTRIBUTORS OR ACADEMIC CONTRIBUTORS EXPRESSLY DISCLAIM ANY WARRANTY OR CONDITION OF MERCHANTABILITY, SECURITY, SATISFACTORY QUALITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, ERROR-FREE OPERATION, OR ANY WARRANTY OR CONDITION FOR O-RAN SPECIFICATIONS.

# SECTION 8: ASSIGNMENT

Adopter may not assign the Agreement or any of its rights or obligations under this Agreement or make any grants or other sublicenses to this Agreement, except as expressly authorized hereunder, without having first received the prior, written consent of the O-RAN Alliance, which consent may be withheld in O-RAN Alliance’s sole discretion. O-RAN Alliance may freely assign this Agreement.

# SECTION 9: THIRD-PARTY BENEFICIARY RIGHTS

Adopter acknowledges and agrees that Members, Contributors and Academic Contributors (including future Members, Contributors and Academic Contributors) are entitled to rights as a third-party beneficiary under this Agreement, including as licensees under Section 3.

# SECTION 10: BINDING ON AFFILIATES

Execution of this Agreement by Adopter in its capacity as a legal entity or association constitutes that legal entity’s or association’s agreement that its Affiliates are likewise bound to the obligations that are applicable to Adopter hereunder and are also entitled to the benefits of the rights of Adopter hereunder.

# SECTION 11: GENERAL

This Agreement is governed by the laws of Germany without regard to its conflict or choice of law provisions.

This Agreement constitutes the entire agreement between the parties as to its express subject matter and expressly supersedes and replaces any prior or contemporaneous agreements between the parties, whether written or oral, relating to the subject matter of this Agreement.

Adopter, on behalf of itself and its Affiliates, agrees to comply at all times with all applicable laws, rules and regulations with respect to its and its Affiliates’ performance under this Agreement, including without limitation, export control and antitrust laws. Without limiting the generality of the foregoing, Adopter acknowledges that this Agreement prohibits any communication that would violate the antitrust laws.

By execution hereof, no form of any partnership, joint venture or other special relationship is created between Adopter, or O-RAN Alliance or its Members, Contributors or Academic Contributors. Except as expressly set forth in this Agreement, no party is authorized to make any commitment on behalf of Adopter, or O-RAN Alliance or its Members, Contributors or Academic Contributors.

In the event that any provision of this Agreement conflicts with governing law or if any provision is held to be null, void or otherwise ineffective or invalid by a court of competent jurisdiction, (i) such provisions will be deemed stricken from the contract, and (ii) the remaining terms, provisions, covenants and restrictions of this Agreement will remain in full force and effect.

Any failure by a party or third party beneficiary to insist upon or enforce performance by another party of any of the provisions of this Agreement or to exercise any rights or remedies under this Agreement or otherwise by law shall not be construed as a waiver or relinquishment to any extent of the other parties’ or third party beneficiary’s right to assert or rely upon any such provision, right or remedy in that or any other instance; rather the same shall be and remain in full force and effect.