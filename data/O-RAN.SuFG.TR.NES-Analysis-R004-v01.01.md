<table><tr><td colspan="2">O-RAN O-RAN.SuFG.TR.NES-Analysis-R004-v01. NCE</td></tr><tr><td colspan="2">Technical Report</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">O-RAN Sustainability Focus Group</td></tr></table>

<table><tr><td></td></tr><tr><td>Copyright © 2025 by the O-RAN ALLIANCE e.V. The copying or incorporation into any other work of part or al of the material available in this document in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material of this document for your personal use, or copy the material of [this document for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them. O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, Germany</td></tr></table>

# Contents

List of figures... 3   
List of tables... 3   
Foreword... 4   
Modal verbs terminology.. . 4   
Introduction.... 4   
1 Scope.... 5   
2 References...... ... 5   
2.1 Informative references.. ... 5   
3 Definition of terms, symbols and abbreviations.. .. 6   
3.1 Terms..... 6   
3.2 Symbols.... 6   
3.3 Abbreviations.... 6   
4 Objectives and analysis approach. .. 8   
4.1 Objectives.... 8   
4.2 Approach followed.. ... 8   
5 O-Cloud Energy Measurements. ...9   
5.1 Foundational Requirements for O-Cloud... ... 9   
5.1.1 Energy consumption KPIs at hardware level.. ...9   
5.1.2 Energy consumption KPIs at Workload level.. ... 12   
5.1.3 Granular Energy Measurement Reporting and Control.. .... 15   
6 O-RU Energy Measurements... ... 18   
6.1 Foundational Requirement for O-RU.. ... 18   
6.1.1 O-RU Energy measurements reporting.. .... 18   
7 O-CU & O-DU Energy related Measurements..... ..... 25   
7.1 Foundational requirements for O-CU / O-DU.. ..25   
7.1.1 O-DU & O-CU Energy measurements reporting.. ..25   
8 SMO Automations..... .... 27   
8.1 Foundational requirements on SMO Automations... ... 27   
8.1.1 SMO Capabilities related to Energy Measurements.. ... 27   
Annex:... 28   
Change history/Change request (history)... ..28

# List of figures

Figure 1 – O-Cloud Resource Infrastructure Power Consumption Metrics [i.3].... . 8   
Figure 2 – O-Cloud Resource Infrastructure Power Consumption Metrics [i.3].. . 9   
Figure 3 – Energy Consumption of Containers [i.5].. 12   
Figure 4 – CPU Time usage counter [i.5].. 12   
Figure 5 – NF Deployment Energy Metrics [i.5].. 12   
Figure 6 – Cloudified NF Energy Efficiency [i.5].. 13   
Figure 7 – O-RU Architecture Example Implementation 1 (see Figure 2.3.2-1 [i.11]).. 18

# List of tables

Table 5.1.1.2.2-1: PEE Measurements... 14   
Table 6.1.1.2.1-1: Counters definition (see Table B.1-1 [i.10]).. 18   
Table 6.1.1.2.1-2: Energy, Power and Environmental Measurements (see Table B.5-1 [i.10]).. 19   
Table 6.1.1.2.1-3: O-RU Hardware components and purpose (see [i.11]).. 19   
Table 6.1.1.2.1-4: Energy Saving Features and O-RU Roles (see Table 3 [i.3]).. .21   
Table 6.1.1.2.2-1: PEE measurements 3GPP TS 28.552 [i.6].. . 22

# Foreword

This Technical Report (TR) has been produced by O-RAN ALLIANCE . The content of the present document is subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN ALLIANCE modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\tt x x { = } 0 1$ ). Always 2 digits with leading zero if needed.

yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.

zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# Introduction

Open RAN energy management is a key sustainability objective shared by mobile operators worldwide, aiming to scale Open RAN technology for commercial deployments and expedite its development. As part of broader industry goals, leading operators have highlighted energy efficiency as critical to Open RAN’s success, underscoring their commitment to advancing sustainable telecommunications infrastructure. To achieve meaningful energy savings, while ensuring reliable performance, the telecom industry requires a standardized approach not only to save energy but also to evaluate, test, measure, and monitor energy consumption in Open RAN deployments. This Technical Report (TR) analyzes operator requirements related to energy consumption measurements and energy efficiency KPIs and identifies gaps within O-RAN ALLIANCE specifications to align with these industry-wide priorities

# 1 Scope

The present document provides a technical analysis report aimed at identifying gaps and inconsistencies in the definitions of energy consumption measurements and energy efficiency KPIs across O-RAN ALLIANCE specifications, current MoU Release Operator Requirements, and relevant Standard Development Organizations (SDOs), primarily 3GPP and ETSI. Its objective is to harmonize the reporting of energy consumption KPIs and to enable the calculation of consistent and comparable energy efficiency KPIs.

# 2 References

# 2.1 Normative references

Not applicable.

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or nonspecific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

1. 3GPP TR 21.905: “Vocabulary for 3GPP Specifications”.   
2. Open RAN Technical Priorities “Release $3 ^ { \mathfrak { s } }$ Document: Open RAN MoU Group at Telecom Infra Project   
(TIP)   
3. O-RAN.WG1.NESUC-R003-v02.00: Network Energy Saving Use Cases Technical Report   
4. O-RAN.WG6.O2-GA&P-R003-v06.00: O2 Interface General Aspects and Principles   
5. O-RAN.WG6.O-Cloud Energy Savings.v00.00.07: Study on O-Cloud Energy Savings   
6. 3GPP TS 28.552 v18.5.0: Management and orchestration; 5G performance measurements   
7. ETSI GR NFV-EVE 021 V5.1.1 (2023-09): Report on energy efficiency aspects for NFV   
8. ETSI ES 202 336-12 v1.2.1v1.2.1: Monitoring and control interface for infrastructure equipment   
9. 3GPP TS 28.554 V18.4.0 (2023-12): Management and orchestration; 5G end to end Key Performance   
Indicators (KPI)   
10. O-RAN.WG4.MP.0-R004-v15.00 Management Plane Specifications   
11. O-RAN.WG7.OMAC-HRD.0-R003-v03.00: Outdoor Macrocell Hardware Architecture and Requirements   
12. O-RAN-WG6.ORCH-USE-CASES-R003-v09.00: Cloudification and Orchestration Use Cases and   
Requirements for O-RAN Virtualized RAN   
13. O-RAN.WG7.NES.0-v1.00: Network Energy Savings Procedures and Performance Metrics   
14. 3GPP TS 28.550 V18.3.0 (2023-12): Management and orchestration; Performance assurance   
15. 3GPP TS 28.532 V18.1.0 (2023-12): Management and orchestration; Generic management services   
16. O-RAN.TIFG.E2E-Test.0-R003-v05.00: End-to-end Test Specification

17. ETSI ES 202 706-1 V1.6.1 (2021-01): Environmental Engineering (EE); Metrics and measurement method for energy efficiency of wireless access network equipment; Part 1: Power consumption - static measurement method

18. ETSI ES 203 228 V1.4.1 (2022-04): Environmental Engineering (EE); Assessment of mobile network energy efficiency

19. O-RAN.WG1.O1-Interface.0-v04.00: O-RAN Operations and Maintenance Interface Specification

20. O-RAN.WG10.OAM-Architecture-R003-v12.00: O-RAN Operations and Maintenance Architecture

21. O-RAN WG6 Orch-Use-Cases-R003: Cloudification and Orchestration Use Cases and Requirements for O-RAN Virtualized RAN

22. O-RAN-WG1. Decoupled-SMO-Architecture-R003-v02.00

23. O-RAN.WG2.Use-Case-Requirements-R003-v09.00

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [i.1]and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [i.1]

Energy Efficiency: Relation between the useful output and energy/power consumption as defined in ETSI ES 203 228 [i. 18]   
Energy Consumption: Integral of power consumption over time as defined in ETSI ES 202 706-1 [i.17]   
3GPP TR 21.905 [i.1]: “Vocabulary for 3GPP Specifications”

# 3.2 Symbols

For the purposes of the present document, the following symbols apply:

PNF Deployment, estimatedEstimated power consumption of a NF deployment running in the O-Cloud   
ECNF Deployment, estimated Estimated energy consumption of a NF deployment running in the O-Cloud   
PcloudifiedNF, estimated Estimated power consumption of a Cloudified NF   
ECcloudifiedNF, estimatedEstimated energy consumption of a Cloudified NF   
EEcloudifiedNF Energy efficiency of a Cloudified NF

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in [i.1] and the following apply:

3GPP 3rd Generation Partnership Project CNF Cloud-Native Network Function DL Down Link DME Data Management and Exposure EPE Energy Power Environmental EE Energy Efficiency EC Energy Consumption FPGA Field Programmable Gate Array gNB Next Generation Node B KPI Key Performance Indicators

LS Liaison Statement   
MnS NF-related Management Services   
MoU Memorandum of Understanding   
NBI North Bound Interface   
NF Network Function   
NFPM NF Performance Assurance Management   
Non-RT RIC Non-real-time RAN Intelligent Controller   
NIC Network Interface Card   
O-DU O-RAN Distributed Unit   
O-RU O-RAN Radio Unit   
PDCP Packet Data Convergence Protocol   
PEE Power Energy & Environmental   
PM Performance Management   
PNF Physical Network Function   
RAT Radio Access Technology   
SDO Standards Defining Organization   
SDU Service Data Unit   
SME Service Management and Exposure   
SMO Service Management and Orchestration   
TG Task Group   
UC Use Case   
UL Up Link

# 4 Objectives and analysis approach

# 4.1 Objectives

This Technical Report presents the outcomes of the SuFG TG2 Energy Measurement analysis phase, with objectives in the pre-normative phase outlined as follows:

This report evaluates O-RAN ALLIANCE specifications and energy consumption measurement standards to align with industry KPIs, ensuring consistency with operator-specific KPIs that address real-world expectations and requirements from 3GPP and ETSI standards.

The report identifies key gaps and areas for improvement in current O-RAN ALLIANCE specifications, focusing on the need for actionable and practical energy measurement and KPI enhancements. These improvements aim to provide a robust foundation for standardized reporting, ensuring compatibility with industry-wide frameworks and operational needs.

The goal is to propose new measurement approaches and configuration parameters where necessary, addressing identified gaps while maintaining alignment with industry best practices and priorities.

# 4.2 Approach followed

O-RAN SuFG conducted an analysis of the Open RAN Technical Priority Documents, which were published by the Open RAN MoU Group at TIP in March 2023 [i.2]. These documents, developed as part of the memorandum signed by Deutsche Telekom, Orange, Telefónica, TIM, and Vodafone, outline key operator expectations for O-RAN technology. SuFG focused its analysis on energy consumption measurements and energy efficiency KPIs, identifying gaps in the existing O-RAN specifications and providing recommendations for future enhancements within the O-RAN ALLIANCE.

The methodology of this Technical Report includes:

Current Standard Analysis: Examines foundational requirements against O-RAN, 3GPP, and ETSI specifications.

Gap Analysis: Identifies and documents gaps between these requirements and the specifications.

Recommendations: Provides informed recommendations aimed at improving future NES work items in O-RAN, based on the analysis.

# 5

# O-Cloud Energy Measurements

# 5.1

# Foundational Requirements for O-Cloud

5.1.1 Energy consumption KPIs at hardware level

5.1.1.1 Description

The O-Cloud platform to provide power, energy, and environmental (PEE) metrics for all hardware components, including CPU, NIC, and Accelerator card, reporting energy consumption via the O2 interface to the SMO, or through a proprietary NBI interface to external tools until O2 specifications are available.

Reference MOU “rel2_CaaS_123”

5.1.1.2 Current Standard Analysis

5.1.1.2.1 O-RAN ALLIANCE references

WG1 has identified a similar requirement in their Network Energy Saving Use Cases Technical Report but does not provide any further analysis in that report, see clause 4.2 of O-RAN.WG1.NESUC-R003- v02.00 [i.3].

WG6 has specified a generic Performance Management framework in the Technical Specification for O2 Interface General Aspects and Principles that supports PM reporting of O-Cloud resources to SMO, see clause 3.9 of O-Cloud Performance Basic Concepts of O-RAN.WG6.O2-GA&P-R003-v06.00 [i.4]. The ongoing Study on O-Cloud Energy Savings, now in version O-RAN.WG6.O-Cloud ES-v02.00 [i.5], provides a comprehensive analysis of power and energy consumption metrics at the infrastructure level in clause 6.

The ES technical report [i.3] have identified several KPIs and measurement methodologies for power/ energy consumption, and efficiency at various levels within the O-Cloud infrastructure.

O-Cloud Resource Power Consumption Metrics: These metrics include PowerCapacity, PowerConsumed, AveragePowerConsumed, MaxPowerConsumed, and MinPowerConsumed. These measurements apply to relevant O-Cloud resources, capturing the power dynamics over a specified interval.   
O-Cloud Node Energy Consumption Metrics: New metrics such as ECnode,core (total energy consumption of CPU cores), ECnode,uncore (uncore components like caches and memory controllers), ECnode,dram (DRAM energy), and others are introduced to monitor energy consumption across different components of the O-Cloud nodes.   
Container Energy Consumption: WG6 introduces metrics at the container level, such as ECcontainer, total (total energy consumption within a container), ECcontainer,core (energy used by CPU cores within a container), and other relevant metrics to track energy usage at the container level.

Table 6.2-1: O-Cloud Resource Infrastructure Power Consumption Metrics   

<table><tr><td rowspan=1 colspan=3>Measurement Data</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>PowerCapacity</td><td rowspan=1 colspan=1>The total amount of power that can be allocated to the O-Cloud Resource(Instantaneous),</td><td rowspan=1 colspan=1>w</td></tr><tr><td rowspan=1 colspan=1>PowerConsumed</td><td rowspan=1 colspan=1>The actual power the O-Cloud Resource consumes (Instantaneous)</td><td rowspan=1 colspan=1>w</td></tr><tr><td rowspan=1 colspan=1>AveragePowerConsumed</td><td rowspan=1 colspan=1>The average power consumed by the O-Cloud Resource over a measurementwindow.</td><td rowspan=1 colspan=1>w</td></tr><tr><td rowspan=1 colspan=1>MaxPowerConsumed</td><td rowspan=1 colspan=1>Maximum power consumed by the O-Cloud Resource over a measurementwindow.</td><td rowspan=1 colspan=1>w</td></tr><tr><td rowspan=1 colspan=1>MinPowerConsumed</td><td rowspan=1 colspan=1>Minimum power consumed by the O-Cloud Resource over a measurementwindow.</td><td rowspan=1 colspan=1>w</td></tr></table>

# Figure 5.1.1.2-1 – Excerpt from O-Cloud Resource Infrastructure Power Consumption Metrics [i.3]

Table 6.2-2: O-Cloud Node Resource Energy Consumption   

<table><tr><td rowspan=1 colspan=3>Measurement Data</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>ECnode,core</td><td rowspan=1 colspan=1>Represents the total energy consumption of all CPU cores on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnode,uncore</td><td rowspan=1 colspan=1>Represents the total energy consumption of uncore components (e.g., caches,memory controllers) on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnodc,dram</td><td rowspan=1 colspan=1>Represents the total energy consumption of DRAM on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnode,package</td><td rowspan=1 colspan=1>Represents the total energy consumption of the CPU package on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnode,other</td><td rowspan=1 colspan=1>Represents the total energy consumption of other host components (e.g., network interfaces, storage devices) on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnode,acc</td><td rowspan=1 colspan=1>Represents the total energy consumption of hardware accelerators on the node.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECnode,plaform</td><td rowspan=1 colspan=1>Represents the overall energy consumption of the entire host.</td><td rowspan=1 colspan=1>J</td></tr></table>

# Figure 5.1.1.2-2 – Excerpt from O-Cloud Node Power Consumption Metrics [i.3]

# 5.1.1.2.2

3GPP and ETSI references

3GPP TS 28.552 v18.5.0 [i.6] clause 5.1.1.19 specifies following PEE (Power Energy & Environmental) related measurements for a 5G Physical Network Function (PNF):

Table 5.1.1.2.2-1: PEE Measurements [i.6]   

<table><tr><td rowspan=1 colspan=1>Attribute</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>PEE.AvgPower</td><td rowspan=1 colspan=1>This measurement provides the average power consumed over the measurement period in watts(W)</td></tr><tr><td rowspan=1 colspan=1>PEE.MinPower</td><td rowspan=1 colspan=1>This measurement provides the minimum power consumed during the measurement period inwatts (W)</td></tr><tr><td rowspan=1 colspan=1>PEE.MaxPower</td><td rowspan=1 colspan=1>This measurement provides the maximum power consumed during the measurement period inwatts (W)</td></tr><tr><td rowspan=1 colspan=1>PEE.Energy</td><td rowspan=1 colspan=1>[This measurement provides the energy consumed in kilowatt-hours (kwh).</td></tr><tr><td rowspan=1 colspan=1>PEE.AvgTemperature</td><td rowspan=1 colspan=1>IThis measurement provides the average temperature over the measurement period in degreesCelsius (°C).</td></tr><tr><td rowspan=1 colspan=1>PEE.MinTemperature</td><td rowspan=1 colspan=1>fThis measurement provides the minimum temperature during the measurement period in degreesCelsius (°C).</td></tr><tr><td rowspan=1 colspan=1>PEE.MaxTemperature</td><td rowspan=1 colspan=1>maximum This measurement provides the temperature during the measurement period in degreesCelsius (ºC).</td></tr><tr><td rowspan=1 colspan=1>PEE.Voltage</td><td rowspan=1 colspan=1>This measurement provides the voltage in volts (V)</td></tr><tr><td rowspan=1 colspan=1>PEE.Current</td><td rowspan=1 colspan=1>[This measurement provides the current in ampere (A)</td></tr><tr><td rowspan=1 colspan=1>PEE.Humidity</td><td rowspan=1 colspan=1>This measurement provides the percentage of humidity during the measurement period (asinteger value between 0-100)</td></tr></table>

For the measurement methods of each of the above measurements, the 3GPP TS references the respective clause in ETSI ES 202 336-12 v1.2.1 [i.8]. The equipment in scope of ETSI ES 202 336-12 v1.2.1 [i.8]is not limited to 3GPP 5G PNFs, but has a broader scope, i.e., all types of ICT equipment that is used in telecommunications networks, see Table 1 in clause 4.4.1 of ETSI ES 202 336-12 v1.2.1 [i.8].

# 5.1.1.3 Gap Analysis

Looking at the MoU requirement and the standards references above, SuFG TG2 interprets “rel2_CaaS_123” as requirement for providing power, energy and environmental (PEE) parameters and measurement data for O-RAN resources to SMO in a similar way as specified by 3GPP TS 28.552 [i.6] for PNFs. As O-CU and O-DU are not necessarily PNFs but can be implemented as virtualized NFs (VNFs/CNFs) running in O-Cloud, the O-Cloud will need the capability to collect PEE measurements of all relevant physical components of O-Cloud, and to provide these as PM data to SMO, similar to the PEE measurements provided by O-RU (as already specified by relevant WGs).

WG6 has already specified a generic framework for PM reporting and is currently working on stage 3 specifications for O2 PM. In the ongoing study on O-Cloud Energy Savings WG6 has provided an initial analysis for power and energy consumption metrics of infrastructure

WG6 has not defined a data model for O2 PM measurements. Currently, only a framework exists for transporting supplier-proprietary data elements, which are specified within supplier-specific dictionaries. Discussions within WG6 have revealed differing opinions regarding the exposure of hardware and component-level measurements to the SMO, resulting in a lack of consensus on this issue. The O-RAN ALLIANCE has not yet established a clear definition or framework for measuring hardware energy efficiency, such as computing performance per watt (Compute/Watt).

It is important to note that all current work in WG6 is still at the study level, and there have been no normative discussions on power or energy measurements thus far.

# 5.1.1.4 Proposed Recommendations

Table 5.1.1.4-1 O-Cloud Energy Measurement recommendations   

<table><tr><td colspan="1" rowspan="1">Recommendation ID</td><td colspan="1" rowspan="1">Title</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Motivation</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG6-REC-001</td><td colspan="1" rowspan="1">StandardizedData Model for02PMMeasurements</td><td colspan="1" rowspan="1">Define a standardized dataImodel for Power and Energy(PE) measurements within the02 interface, including metricslike PowerCapacity,PowerConsumed, etc.</td><td colspan="1" rowspan="1">Improves consistency andcross-vendor interoperabilitylin energy management.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG6-REC-002</td><td colspan="1" rowspan="1">Exposure ofHardwareMeasurementsto SMO</td><td colspan="1" rowspan="1">Establish guidelines forsecurely exposing hardwareand component-level powerand energy measurements tothe SMO, with specific metricsand reporting conditions.</td><td colspan="1" rowspan="1">Enhances transparency andenables effective energymanagement in SMO.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG6-</td><td colspan="1" rowspan="1">HardwareEnergy</td><td colspan="1" rowspan="1">Define a standardized datamodel for reporting workload-</td><td colspan="1" rowspan="1">Enables consistent hardwareenergy efficiency metrics for</td></tr><tr><td>REC-003</td><td>Efficiency</td><td>level energy metrics (e.g., container, pod, CNF) over the 02 interface, including metrics like ECcontainer,total, ECNF Deployment, estimated, etc.</td><td>optimization.</td></tr></table>

# 5.1.2 Energy consumption KPIs at Workload level

# 5.1.2.1 Description

The O-Cloud platform to provide power, energy and environmental (PEE) parameters and measurement data at the workload level e.g. container, pod, CNF, etc. as well as for the OCloud software components themselves. O-Cloud platform be able to report energy efficiency through O2 interface to SMO or NBI inteface to external tooling. Reference MOU “rel2_CaaS_124”

5.1.2.2 Current Standard Analysis

5.1.2.2.1 O-RAN ALLIANCE references

WG1 has identified a similar requirement in their Network Energy Saving Use Cases Technical Report but does not provide any further analysis in that report, see clause 4.2 of O-RAN.WG1.NESUC-R003- v02.00 [i.3].

WG6 has specified a generic Performance Management framework in the Technical Specification for O2 Interface General Aspects and Principles that supports PM reporting of O-Cloud resources to SMO.

WG6 defined power and energy consumption metrics at the workload level within the O-Cloud in Energy Savings Technical Report (O-RAN.WG6.O-Cloud ES-v02.00 [i.5]). Specifically, clauses 6.3 and 6.4 outline metrics for containers, NF deployments, and Cloudified NFs. These include energy consumption metrics such as ECcontainer,total, ECcontainer,core, and ECNF Deployment, estimated, which allow for detailed monitoring and analysis of energy consumption at various levels of the O-Cloud infrastructure. WG6 has also highlighted the importance of these metrics in assessing the performance of energy efficiency strategies and making necessary policy adjustments. power and energy consumption metrics [i. 5] (Table 5.1.2.2.1-1):

<table><tr><td colspan="3">Measurement Data</td></tr><tr><td>Name</td><td>Description</td><td>Unit</td></tr><tr><td>ECcontince,total</td><td>Represents the total energy consumption across hardware components within a specified container.</td><td>J</td></tr><tr><td>ECcontaincr, core</td><td>Tracks the total energy used by a container&#x27;s CPU cores, it can be measured or estimated.</td><td>J</td></tr><tr><td>ECcontainer, dram</td><td>Indicates the cumulative energy draw of a container in DRAM, providing insight into its memory-related energy footprint.</td><td>J</td></tr><tr><td>ECcontainer, uncore</td><td>Provides the accumulated energy consumption of specific uncore elements including the last- level cache, integrated hardware accelerator(s), and memory controller.</td><td>J</td></tr></table>

<table><tr><td rowspan=1 colspan=1>ECoontainer, package</td><td rowspan=1 colspan=1>Provides a cumulative measurement of the energy consumed by the entire CPU socket,encompassing all cores and uncore components including the last-level cache, integratedhardware accelerator, and memory controller. It is generally expected that Package Energy isequivalent to the sum of CPU cores and hardware accelerator energy counters.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECcontaincr, other</td><td rowspan=1 colspan=1>Represents energy consumption for non-CPU and non-DRAM componcnts. To calculate individual component usage, this total is typically reduced by measured CPU and DRAMpower.</td><td rowspan=1 colspan=1>J</td></tr><tr><td rowspan=1 colspan=1>ECcontainer, acc</td><td rowspan=1 colspan=1>Measures the total hardware accelerator power consumption allocated to a particularcontainer.</td><td rowspan=1 colspan=1>J</td></tr></table>

# Figure 5.1.2.2-1 - Excerpt from O-Cloud Energy Consumption of Containers [i.5]

Table 6.3-2: Container Resource Utilization   
Figure 5.1.2.2-2 - Excerpt from O-Cloud CPU Time usage counter [i.5]   

<table><tr><td rowspan=1 colspan=3>Measurement Data</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>CPU Time</td><td rowspan=1 colspan=1>This metric captures the container&#x27;s total CPU usage, measured through CPU time, that isreported by the tracing technology. It is used as an input for power estimation models.</td><td rowspan=1 colspan=1>us</td></tr></table>

<table><tr><td rowspan=1 colspan=3>KPI</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>PNFDeployment,estimted</td><td rowspan=1 colspan=1>A KPI that gives an estimation of the power consumption of a NF deployment running in the O-Cloud. This KPI is derived from the power consumption of O-Cloud Resources allocated to that NF Deployment based on the mcan usage of the resource (c.g. vCPU mean usage).</td><td rowspan=1 colspan=1>w</td></tr></table>

Figure 5.1.1.2-3 - Excerpt from O-Cloud NF Deployment Energy Metrics [i.5]   

<table><tr><td rowspan=1 colspan=3>KPI</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>ECNFDeploymcnt,estimated</td><td rowspan=1 colspan=1>A KPI that gives an estimation of the energy consumption of a NF deployment running in the O-Cloud. This KPI is derived from the energy consumption of O-Cloud resources allocated to thatNF Deployment based on the mean usage of the resource (e.g. vCPU mean usage).</td><td rowspan=1 colspan=1>J</td></tr></table>

Figure 5.1.1.2-4 - Excerpt from O-Cloud Cloudified NF Energy Efficiency [i.5]   

<table><tr><td rowspan=1 colspan=3>KPI</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>PeloudifiedNF,estimated</td><td rowspan=1 colspan=1>A KPI that gives an estimation of the power consumption of a Cloudified NF. This KPI is obtained by summing up the estimated power consumption of ts constituent NF deployment(s).</td><td rowspan=1 colspan=1>w</td></tr><tr><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=3>KPI</td></tr><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>ECcloudifiedNF,estimated</td><td rowspan=1 colspan=1>A KPI that gives an estimation of the energy consumption of a Cloudified NF. This KPI isobtained by summing up the estimated energy consumption of its constituent NF deployment(s).</td><td rowspan=1 colspan=1>J</td></tr></table>

# 5.1.2.2.2

# 3GPP and ETSI references

Relevant 3GPP and ETSI references are covered by the WG6 TR, these are ETSI GR NFV-EVE 021 [i.7] and clause 6.7.3.1.4 of 3GPP TS 28.554 [i.9].

ETSI NFV EVE (authoring WG of ETSI GR NFV-EVE 021 [i.7] and 3GPP SA5 (responsible WG for 3GPP TS 28.554 [i.9]) had an LS exchange about "5G network energy efficiency and energy saving", that highlight results of ETSI NFV EVE informative work in ETSI GR NFV-EVE 021 [i.7].

Based on the LS from ETSI NFV EVE to 3GPP SA5, SuFG TG2 expects that ETSI NFV will provide normative specifications to derive actual VNF/CNF power consumption by collecting relevant metrics about power consumption of underlying virtualized resources without having to rely on estimated values based on other metrics. Their intention is to make extensible the functionality to collect power

consumption for any kind of NFVI resources, if feasible. 3GPP SA5 can then take this normative work as basis to update their TS 28.554 [i.9].

# 5.1.2.3 Gap Analysis

Observations related to WG6:

■ As mentioned in 5.1.1.3 WG has yet to establish a mechanism for reporting of PM data in a standardized, Interoperable manner.   
Furthermore, WG6 will need to work out a detailed flow about how power and energy consumption metrics of NF deployment and cloudified NFs is derived and made available for SMO; respective specifications updates will need to be made.

The following SMO requirement is also connected to this topic:

MoU Requirement rel_2_SMO_116 [i.2]: “Dashboards for power consumption of clusters should be available in SMO (power consumption by worker, by switch, by FAN, by HW acceleration, by site, by data center, by CaaS, PaaS, tools). Operator should be able to export all dashboard manually or automatically”

MoU Requirement rel_2_SMO_118 [i.2]: “Power consumption metrics/KPI/counters/logs of CNFs should be available on SMO per NF type and per NF instance to allow automated load consolidation.”

# 5.1.2.4 Proposed Recommendations

Table 5.1.2.4-1 – Workload Energy consumption measument recommendations   

<table><tr><td rowspan=1 colspan=1>Recommendation ID</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Motivation</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG6-REC-004</td><td rowspan=1 colspan=1>Standardized DataModel for NFDeployment LevelEnergyMeasurements</td><td rowspan=1 colspan=1>Define a standardized data model forreporting NF deployment energy metrics(e.g., container, pod, CNF) over the 02interface, including metrics likeECcontainer,total, ECNF Deployment,estimated, etc.</td><td rowspan=1 colspan=1>Ensures consistent and vendor-agnosticreporting of energy metrics to sMO.</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG6-REC-005</td><td rowspan=1 colspan=1>Net EnergyConsumptionReporting</td><td rowspan=1 colspan=1>Implement mechanisms for capturing andreporting energy consumption metrics atthe container level (e.g., ECcontainer,total,ECcontainer,core) via the O2 interface.</td><td rowspan=1 colspan=1>Facilitates detailed monitoring andoptimization of energy usage at thecontainer level.</td></tr></table>

# 5.1.3 Granular Energy Measurement Reporting and Control

# 5.1.3.1 Description

O-CU/O-DU hardware (e.g. CPU, Accelerators, NIC cards, Fans(s), PSU, etc.) to have the capability to measure and report power consumption values to the O-Cloud (via O2 interface). Reference [i.2] MOU “rel3_CaaS_125”

5.1.3.2 Current Standard Analysis

5.1.3.2.1 O-RAN ALLIANCE references

In the ongoing Study [i.5] , WG6 has identified the relevant energy efficiency KPIs in clause 6.4, also including the relevant 3GPP and ETSI references:

“The approach for assessing energy efficiency of Cloudified NF strongly depends on the functionality and purpose of the Cloudified NF. In general, the energy efficiency of a Cloudified NF can be

determined by assessing its delivered performance versus its energy consumption over a defined time interval following formula:

Wherein corresponds to the service $p$

Table 5.1.3.2.1-1: Types of Energy Efficiency Measures (see Table 6.4.2-1 [i.5])   

<table><tr><td rowspan=1 colspan=1>Measurement Approach</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency assessment based onPDCP SDU data volume</td><td rowspan=1 colspan=1>[i.9] clause 6.7.1 and [i.18], clause 5.3</td><td rowspan=1 colspan=1>bit/J</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency assessment based oncoverage</td><td rowspan=1 colspan=1>[i.18], clause 5.3</td><td rowspan=1 colspan=1>m2/J</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency assessment based onlatency (used for URLLC slice)</td><td rowspan=1 colspan=1>[i.9], clause 6.7.2.3.2 and [i.18], clause 5.3</td><td rowspan=1 colspan=1>(0.1ms * J)-1</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency assessment based on bothlatency and data volume(used for URLLC slice)</td><td rowspan=1 colspan=1>[i.9], clause 6.7.2.2 and 6.7.2.2a</td><td rowspan=1 colspan=1>bit/(0.1ms*J)</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency of registered subscribers(used for MIoT slice)</td><td rowspan=1 colspan=1>[i.9], clause 6.7.2.4.1</td><td rowspan=1 colspan=1>user/J</td></tr><tr><td rowspan=1 colspan=1>Energy efficiency of number of active UEs(used for MIoT slice)</td><td rowspan=1 colspan=1>[i.9], clause 6.7.2.4.2</td><td rowspan=1 colspan=1>user/J</td></tr></table>

NOTE: “Further information on how these KPIs is calculated are available in the relevant 3GPP and ETSI specifications. Selection of a particular way of measuring the energy efficiency depends on the requirements, type of deployments and use-cases. It is expected that the SMO can compute the Energy consumption and efficiency of a Cloudified NF based on measurements from the O-Cloud. Energy efficiency calculations may involve collaboration with other working groups, such as WG10.”

WG6 specifications for O2 general aspects and principles (see clause 3.9 of O-RAN.WG6.O2-GA&PR003-v06.00 [i.4] and use-cases and requirements (see clasue 3.8 of O-RAN-WG6.ORCH-USE-CASESR003-v09.00 [i.12]) for PM are available. These enable SMO to interact with PM services to receive measurement reports and to perform PM jobs related interations, e.g. request for, subsribe to, update, PM jobs

Stage 3 for O-Cloud PM for O2 interface is expected to be covered in the future releases.

WG1studied decoupling of SMO Services (SMOS) offered by different SMO Functions in O-RAN-WG1. Decoupled-SMO-Architecture-R003-v02.00 [i.22]. In clause 5.1.1 the RAN NF Performance Assurance Management SMO Service (NFPM) is discussed. It describes the NFPM SMOS that provides a mechanism for the NFPM SMOS consumers to create and terminate the PM job as well as querying the related PM information by consuming PM MnS via O1 interface and Open Fronthaul M-Plane interface. This enables a NFPM SMOS consumers to collect PM measurements as defined in 3GPP TS 28.552 [i. 6], like DL PDCP SDU Data Volume per interface in clause 5.1.3.6.2.3, UL PDCP SDU Data Volume per interface in clause 5.1.3.6.2.4, PNF Energy consumption in clause 5.1.1.19.3 or Power consumed by Physical Network Function & its components in clause 5.1.1.19.2. Generic mechanisms for O1 PM are already standardized, see O-RAN.WG1.O1-Interface.0- v04.00 [i.19] clause 2.3 Performance Assurance Management Services and ORAN.WG10.OAM-Architecture-R003-v11.00 [i.20] clause4.2.2 O-RAN Measurement Data Collection Use Case.

# 5.1.3.2.2 3GPP and ETSI references

In addition to the 3GPP and ETSI references above, it is relevant to look at the 3GPP specifications for the OA&M collection method, which are 3GPP TS 28.550 [i.14] and 3GPP TS 28.532 [i.15]. 3GPP defines one set of generic procedures for all types of PM measurements and KPIs that are specified in 3GPP TS 28.552 [i.6] and TS 28.554 [i.9].

Looking at the MoU requirement and the standards references above, SuFG TG2 interprets “rel2_CaaS_123” as requirement towards O2 PM services, i.e. to enable a management service within SMO to control requests and collection of sufficient energy/power measurements in a way that allows it to synchronise these PM measurements with relevant performance PM measurements from E2 Nodes over the respective interfaces so that management service within SMO can calculate meaningful EC and EE KPIs.

The following SMO requirement is also connected to this topic:

MoU Requirement rel_1_SMO_62: “SMO shall be capable to receive energy metrics / create KPIs to optimize the management devices”

# 5.1.3.4 Proposed Recommendations

Table 5.1.3.4-1 – Granular Energy measument reporting and control recommendations   

<table><tr><td rowspan=1 colspan=1>RequirementID</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Motivation</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG6-REC-006</td><td rowspan=1 colspan=1>Granular EnergyMeasurementReporting andControl</td><td rowspan=1 colspan=1>O-Cloud platform to providedetailed power, energy, andenvironmental (PEE) data,including whether the data isinstantaneous or averaged,and allow control overparameters like rollingwindow size for averages.</td><td rowspan=1 colspan=1>Enables precise KPIcomputation and flexibilityin measurement reporting.</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG6-REC-007</td><td rowspan=1 colspan=1>Power Meteringfor O-CloudHardware</td><td rowspan=1 colspan=1>The O-Cloud should becapable of measuring theenergy consumption ofhardware componentsassociated with O-RAN CNFs,such as O-CU and O-DU (e.g.,CPU, accelerators, NIC cards,fans, and PSUs). It shouldalso support themeasurement and reportingof power consumptionvalues to the O-Cloud via the02 interface</td><td rowspan=1 colspan=1>Facilitates comprehensiveenergy monitoring acrossall hardware components.</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG1-REC-001</td><td rowspan=1 colspan=1>Energy Efficiency KPIAssessment forCloudified NF</td><td rowspan=1 colspan=1>The SMO be computing energyefficiency KPIs for Cloudified NFs basedon various measures (e.g., PDCP SDUdata volume, coverage, latency,registered subscribers) to assess theenergy performance over definedintervals.</td><td rowspan=1 colspan=1>Supports optimal energymanagement and policyadjustments for Cloudified NFs.</td></tr></table>

# 6.1 Foundational Requirement for O-RU

# 6.1.1 O-RU Energy measurements reporting

# 6.1.1.1 Description

Availability of counters/KPIs to be able to monitor in any time the power consumption per RAT, frequency band in multi-band RUs. Reporting capability towards Management systems or external tooling.

Reference (MoU Requirement “rel2_O-RU_43”, rel3_RAN_features_48 & MOU Requirement rel_2_SMO_124)

6.1.1.2 Current Standard Analysis

# 6.1.1.2.1

# O-RAN ALLIANCE references

The requirement specifies the measurements to be reported from the O-RU. The counters associated with epe-stats are the only ones that deal with energy measurements. Transceiver-stat, rx-window-stats and txmeasurement-objects are not relevant for energy measurements. This requirement is already specified in existing O-RAN.WG4.MP.0-R004-v15.00 [i.10] technical specification.

According to Table 6.1.1.2.1-1, energy, power and environmental statistics (EPE-STATS) are the following:

Table 6.1.1.2.1-1: Counters definition (see Table B.1-1 [i.10])   

<table><tr><td rowspan=1 colspan=1>measurement-group</td><td rowspan=1 colspan=1>measurement-object</td><td rowspan=1 colspan=1>report-info</td><td rowspan=1 colspan=1>object-unit</td><td rowspan=1 colspan=1>Note</td></tr><tr><td rowspan=1 colspan=1>epe-statistics</td><td rowspan=1 colspan=1>POWERTEMPERATUREVOLTAGECURRENT</td><td rowspan=1 colspan=1>MAXIMUMMINIMUMAVERAGE</td><td rowspan=1 colspan=1>Hardwarecomponent type,e.g., O-RAN-RADIO, O-RU-POWER-AMPLIFIER, O-RU-FPGA,power- supply,fan, cpu</td><td rowspan=1 colspan=1>Type decimal 64 including 4 fraction-digitsfor max, min, average.Power measured using method specified inclause 5.1.1.19 of 3GPP TS 28.552Unit of power: watts (W)Temperature measured using methodspecified in clause 5.1.1.19 of 3GPP TS28.552Unit of temperature: CelsiusVoltage measured using method asspecified in clause 5.1.1.19 of 3GPP TS28.552Unit of voltage: VoltsCurrent measured using method specified inclause 5.1.1.19 of 3GPP TS 28.552Unit of current: Amperes</td></tr></table>

For further details, see annex B.5 [i.10]:   
The epe-stats include the performance measurement for energy, power and environmental parameters, as shown in the following table. An O-RU shall report its supported measurement objects per hardware component class.

Table 6.1.1.2.1-2: Energy, Power and Environmental Measurements (see Table B.5-1 [i.10])   

<table><tr><td rowspan=1 colspan=1>measurement-object</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>POWER</td><td rowspan=1 colspan=1>Value of measured power consumed by identified hardwarecomponent</td></tr><tr><td rowspan=1 colspan=1>TEMPERATURE</td><td rowspan=1 colspan=1>Value of measured temperature of identified hardware component</td></tr><tr><td rowspan=1 colspan=1>VOLTAGE</td><td rowspan=1 colspan=1>Value of measured voltage of identified hardware component</td></tr><tr><td rowspan=1 colspan=1>CURRENT</td><td rowspan=1 colspan=1>Value of measured current of identified hardware component</td></tr></table>

Measurement objects measure the power, temperature, voltage and current of hardware components of the O-RU. The specification O-RAN.WG4.MP.0-R004-v15.00 [i.10] mentions hardware types such as ORAN-RADIO, O-RU-POWER-AMPLIFIER, O-RU-FPGA, power supply, fan, and CPU. Based on Technical Specification O-RAN.WG7.OMAC-HRD.0-R003-v03.00 [i.11] the following O-RU hardware components are identified:

Table 6.1.1.2.1-3: O-RU Hardware components and purpose (see [i.11])   

<table><tr><td rowspan=1 colspan=1>Hardware Component</td><td rowspan=1 colspan=1>Purpose</td></tr><tr><td rowspan=1 colspan=1>O-RAN Fronthaul Unit</td><td rowspan=1 colspan=1>Communicates with O-DU through the O-RAN Fronthaul interface andprocesses control/data packets using the CUS and M plane processing block.</td></tr><tr><td rowspan=1 colspan=1>Low-PHY Processing</td><td rowspan=1 colspan=1>Responsible for physical layer processing tasks like encoding, scrambling,modulation, layer mapping, precoding, beamforming, and resource elementmapping.</td></tr><tr><td rowspan=1 colspan=1>Digital Processing Unit</td><td rowspan=1 colspan=1>Handles digital frequency conversion and implements DPD and CFRalgorithms to enhance power amplifier efficiency by reducing PAPR/ACLR.</td></tr><tr><td rowspan=1 colspan=1>RF Processing Unit</td><td rowspan=1 colspan=1>Processes RF signals, interfacing between digital signals in the digitalprocessing unit and the analog domain in the transceiver unit.</td></tr><tr><td rowspan=1 colspan=1>Transceiver Unit</td><td rowspan=1 colspan=1>Converts digital signals to analog in DL (using DAC) and analog to digital inUL (using ADC), facilitating signal transmission and reception.</td></tr><tr><td rowspan=1 colspan=1>Power Amplifier</td><td rowspan=1 colspan=1>Amplifies signals. PA boosts power of outgoing signals in DL, and LNAenhances strength of incoming signals in UL.</td></tr><tr><td rowspan=1 colspan=1>Cavity Filter</td><td rowspan=1 colspan=1>Suppresses unwanted signals. Used after amplification in DL and beforeamplification in UL.</td></tr><tr><td rowspan=1 colspan=1>TDD Switch</td><td rowspan=1 colspan=1>Switches operation between DL and UL, allowing the system to alternatebetween transmit and receive operations.</td></tr><tr><td rowspan=1 colspan=1>Antenna Unit</td><td rowspan=1 colspan=1>[Transmits processed signals over the air in DL and receives signals from the airin UL.</td></tr><tr><td rowspan=1 colspan=1>Power Unit</td><td rowspan=1 colspan=1>Supplies power to the processing units (FH, Digital, and RF).</td></tr><tr><td rowspan=1 colspan=1>Timing/SynchronizationBlock</td><td rowspan=1 colspan=1>Ensures that the processing units are synchronized, crucial for signal integrityand timing accuracy.</td></tr><tr><td rowspan=1 colspan=1>Antenna CalibrationProcessing Block</td><td rowspan=1 colspan=1>Compensates for amplitude and phase ofsets in each RF chain, ensuringaccurate beamforming.</td></tr></table>

![](images/d13fa9f111747bd4183c5c8e090d6662beda15f48d8eb11f100e55bc0a309fc0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1.1.2.1-1 - O-RU Architecture Example Implementation (see Figure 2.3.2-1 [i.11])

Energy Saving features

To improve energy efficiency, it's crucial to examine how measurements from the O-RU can be used and what types are needed for various energy-saving features. The current O-RAN specifications don't define the necessary energy measurements for these features in the O-RU. The following details are from the WG1 O-RAN.WG1.NESUC-R003-v02.00 technical report on O-RU rules for different energy-saving features:

Specific KPIs: Energy Efficiency and power consumption KPIs provided by real-time metering

Table 6.1.1.2.1-4: Energy Saving Features and O-RU Roles (see Table 3 [i.3])   
WG1.NESUC-R003-v02.00 TR [i.3] is referencing the 3GPP TS 28.552 [i.6], clause.5.1.1.19.2 and ORAN.WG4.MP [i.10] (Clause B.1 and B.5) in relation to the energy measurements.   

<table><tr><td rowspan=1 colspan=1>Energy Saving Feature</td><td rowspan=1 colspan=1>O-RU Roles</td></tr><tr><td rowspan=1 colspan=1>Carrier and Cell Switch Off/OnO-RAN.WG1.NESUC-R003-v02.00 [i.3] Clause 5.2.2.2 and5.2.2.3.1</td><td rowspan=1 colspan=1>a) Report EC and EE related information via Open FH M-Planeinterface to O-DU or alternatively to SMO directly.b) Support actions required to perform EE/ES optimization. updatedcarrier configuration (i.e. activation, deactivation or sleep)c) Input data: Power consumption metrics: Mean total/per carrierpower consumption, mean total/per carrier transmit power</td></tr><tr><td rowspan=1 colspan=1>RF Channel ReconfigurationO-RAN.WG1.NESUC-R003-v02.00 [i.3] Clause 6.2.1.2 and6.2.1.3.1</td><td rowspan=1 colspan=1>a) Report EC and EE related information over Open FH M-Plane toO-DU or alternatively to SMO directly.b) Perform actions required to be performed due to RF ChannelReconfiguration (i.e., O-RU Tx/Rx Array selection, modification ofthe number of SSB beams, modification of the O-RU AntennaTransmit power, modification of the number of SU/MU MIMOspatial streams or data layers) as part of EE/ES optimization.c) Input: Power consumption metrics: Mean total/per carrier powerconsumption, mean total/per carrier transmit power.Information on supported Tx/Rx Array selections along with powerconsumption (site/O-RU input power needed for certain EE KPIs)</td></tr><tr><td rowspan=1 colspan=1>Advanced Sleep Mode SelectionO-RAN.WG1.NESUC-R003-v02.00 [i.3] Clause 7.2.1.2</td><td rowspan=1 colspan=1>a) Support reporting the O-RU SMs capabilities and additionaloperational parameters to O-DU via O-FH.b) Internally apply SM selection or alternatively receive over O-FHand apply O-DUs request for updated SM configuration (e.g., switchoff a certain O-RU functionality).c) Input: missing from the TR</td></tr></table>

Shared O-RU Scenario

The O-RU energy efficiency could also be beneficial in a Multi-Operator Operation scenario. Based on the technical specification O-RAN.WG4.MP.0-R004-v15.00 [i.10], clause 19, O-FH shall support the multi-operator scenario:

“Shared O-RU performance management   
The NETCONF client of a Shared Resource Operator is identified by using a user list entry in o-ranusermgmt YANG model that contains a configured sro-id. Such a NETCONF client shall have restricted access privileges to the o-ran-performance-management YANG model as described in sub-clause ORAN.WG4.MP.0-R004-v15.00 [i.10], 19.3.3. An O-RU supporting the SHARED-ORU-MULTIOPERATOR feature should support the GRANULARITY-TRANSPORT-MEASUREMENT and/or the GRANULARITY-EAXC-ID-MEASUREMENT features. These allow the O-RU to report rx-windowmeasurement-objects on a per ru-element and/or eaxcid basis, meaning window measurements pertain to the transport flows and/or eaxcids associated with a particular Shared Resource Operator. A Shared O-RU Host can configure multiple remote-file-uploads list entries corresponding to the individual file servers of different Shared Resource Operators. However, there is currently no role-based access control applied to file management-based performance management reporting, as specified in clause [i.10] 10.3.2. If access to configured measurement results needs to be controlled on a per Shared Resource Operator basis, file management-based performance management should not be used.”

# 6.1.1.2.2

# 3GPP and ETSI references

The table below collects the PEE (Power, Energy and Environmental) measurements from 3GPP TS 28.552 [i.6], Clause 5.1.1.19, which specifies the performance measurements for 5G networks, including network slicing.

Table 6.1.1.2.2-1: PEE measurements 3GPP TS 28.552 [i.6]   

<table><tr><td rowspan=1 colspan=1>PEEMeasurementType</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Unit</td><td rowspan=1 colspan=1>MeasurementName</td><td rowspan=1 colspan=1>Obtained According to</td></tr><tr><td rowspan=1 colspan=1>PNF PowerConsumption</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Average Power</td><td rowspan=1 colspan=1>Average power consumedover the measurementperiod.</td><td rowspan=1 colspan=1>Watts (W)</td><td rowspan=1 colspan=1>PEE.AvgPower</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clauses 4.4.3.1, 4.4.3.4,AnnexA</td></tr><tr><td rowspan=1 colspan=1>MinimumPower</td><td rowspan=1 colspan=1>Minimum powerconsumed during themeasurement period.</td><td rowspan=1 colspan=1>Watts (W)</td><td rowspan=1 colspan=1>PEE.MinPower</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clauses 4.4.3.1, 4.4.3.4,Annex A</td></tr><tr><td rowspan=1 colspan=1>MaximumPower</td><td rowspan=1 colspan=1>Maximum powerconsumed during themeasurement period.</td><td rowspan=1 colspan=1>Watts (W)</td><td rowspan=1 colspan=1>PEE.MaxPower</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8]clauses 4.4.3.1, 4.4.3.4,Annex A</td></tr><tr><td rowspan=1 colspan=1>PNF EnergyConsumption</td><td rowspan=1 colspan=1>Energy consumed.</td><td rowspan=1 colspan=1>Kilowatt-hours(kWh)</td><td rowspan=1 colspan=1>PEE.Energy</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clauses 4.4.3.1, 4.4.3.4,AnnexA</td></tr><tr><td rowspan=1 colspan=1>AverageTemperature</td><td rowspan=1 colspan=1>Average temperature overthe measurement period.</td><td rowspan=1 colspan=1>DegreesCelsius (C)</td><td rowspan=1 colspan=1>PEE.AvgTemperature</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clause 4.4.3.4, Annex A</td></tr><tr><td rowspan=1 colspan=1>MinimumTemperature</td><td rowspan=1 colspan=1>Minimum temperatureduring the measurementperiod.</td><td rowspan=1 colspan=1>DegreesCelsius (°C)</td><td rowspan=1 colspan=1>PEE.MinTemperature</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clause 4.4.3.4, Annex A</td></tr><tr><td rowspan=1 colspan=1>MaximumTemperature</td><td rowspan=1 colspan=1>Maximum temperatureduring the measurementperiod.</td><td rowspan=1 colspan=1>DegreesCelsius (C)</td><td rowspan=1 colspan=1>PEE.MaxTemperature</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clause 4.4.3.4, Annex A</td></tr><tr><td rowspan=1 colspan=1>PNF Voltage</td><td rowspan=1 colspan=1>Voltage.</td><td rowspan=1 colspan=1>Volts (V)</td><td rowspan=1 colspan=1>PEE.Voltage</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] Clauses 4.4.3.3, 4.4.3.4,Annex B</td></tr><tr><td rowspan=1 colspan=1>PNF Current</td><td rowspan=1 colspan=1>Current.</td><td rowspan=1 colspan=1>Amperes(A)</td><td rowspan=1 colspan=1>PEE.Current</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] Clauses 4.4.3.3, 4.4.3.4,Annex B</td></tr><tr><td rowspan=1 colspan=1>PNF Humidity</td><td rowspan=1 colspan=1>Percentage of humidityduring the measurementperiod.</td><td rowspan=1 colspan=1>Percentage(0-100)</td><td rowspan=1 colspan=1>PEE.Humidity</td><td rowspan=1 colspan=1>ETSI ES 202 336-12 v1.2.1[i.8] clause 4.4.3.3, Annex B</td></tr></table>

# 6.1.1.3 Gap Analysis

■ The requirement is met by referencing the O-RAN.WG4.MP.0-R003-v15.00 [i.10] ■ In further analysis, the table below compares EPE-STATS and PEE from the TS 28.552 [i.6] specification. The last column checks if the EPE stat matches the PEE stats.

Table 6.1.1.3-1: EPE-STATS and PEE comparison   

<table><tr><td colspan="1" rowspan="1">PEEMeasurementType</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Unit</td><td colspan="1" rowspan="1">MeasurementName</td><td colspan="1" rowspan="1">Obtained Accordingto</td><td colspan="1" rowspan="1">Checklist(Similar inEPE-STATS)</td></tr><tr><td colspan="1" rowspan="1">PNF PowerConsumption</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">AveragePower</td><td colspan="1" rowspan="1">Average powerconsumed over themeasurement period.</td><td colspan="1" rowspan="1">Watts (W)</td><td colspan="1" rowspan="1">PEE.AvgPower</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clauses4.4.3.1, 4.4.3.4,Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">MinimumPower</td><td colspan="1" rowspan="1">Minimum powerconsumed during themeasurement period.</td><td colspan="1" rowspan="1">Watts (W)</td><td colspan="1" rowspan="1">PEE.MinPower</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clauses4.4.3.1, 4.4.3.4,Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">MaximumPower</td><td colspan="1" rowspan="1">Maximum powerconsumed during themeasurement period.</td><td colspan="1" rowspan="1">Watts (W)</td><td colspan="1" rowspan="1">PEE.MaxPower</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clauses4.4.3.1, 4.4.3.4,Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">PNF EnergyConsumption</td><td colspan="1" rowspan="1">Energy consumed.</td><td colspan="1" rowspan="1">Kilowatt-hours(kWh)</td><td colspan="1" rowspan="1">PEE.Energy</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clauses4.4.3.1, 4.4.3.4,Annex A</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">PNFTemperature</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">AverageTemperature</td><td colspan="1" rowspan="1">Average temperatureover the measurementperiod.</td><td colspan="1" rowspan="1">DegreesCelsius(℃)</td><td colspan="1" rowspan="1">PEE.AvgTemperature</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clause4.4.3.4, Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">MinimumTemperature</td><td colspan="1" rowspan="1">Minimumtemperature duringthe measurementperiod.</td><td colspan="1" rowspan="1">DegreesCelsius(℃C)</td><td colspan="1" rowspan="1">PEE.MinTemperature</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clause4.4.3.4, Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">MaximumTemperature</td><td colspan="1" rowspan="1">Maximumtemperature duringthe measurementperiod.</td><td colspan="1" rowspan="1">DegreesCelsius(C)</td><td colspan="1" rowspan="1">PEE.MaxTemperature</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clause4.4.3.4, Annex A</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">PNF Voltage</td><td colspan="1" rowspan="1">Voltage.</td><td colspan="1" rowspan="1">Volts (V)</td><td colspan="1" rowspan="1">PEE.Voltage</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] Clauses4.4.3.3, 4.4.3.4,Annex B</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">PNF Current</td><td colspan="1" rowspan="1">Current.</td><td colspan="1" rowspan="1">Amperes(A)d:</td><td colspan="1" rowspan="1">PEE.Current</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] Clauses4.4.3.3, 4.4.3.4,Annex B</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">PNFHumidity</td><td colspan="1" rowspan="1">Percentage ofhumidity during themeasurement period.</td><td colspan="1" rowspan="1">Percentage(0-100)</td><td colspan="1" rowspan="1">PEE.Humidity</td><td colspan="1" rowspan="1">ETSI ES 202 336-12v1.2.1 [i.8] clause4.4.3.3, Annex B</td><td colspan="1" rowspan="1">No</td></tr></table>

Based on the comparison above in EPE-STATS, the energy consumption (kWh) and humidity counter are missing.

■ In defining EPE-STAT, it was not clearly specified which hardware components need to transmit these data. Based on the O-RAN.WG7.OMAC-HRD.0-R003-v03.00 [i.11] specification, multiple O-RU hardware components were identified.

■ The O-RAN.WG1.NESUC-R003-v02.00 [i.3] technical report describes the energy-saving features for O-RAN, along with the equipment roles and requirements of the equipment involved. The features such as Carrier and Cell Switch Off/On and RF Channel Reconfiguration energysaving require power consumption metrics, including mean total power consumption/per carrier, as well as the mean total transmit power/per carrier. Measuring power consumption per carrier may require multiple sensors or additional calculations; refer to the following requirement for more details.

The technical report also discusses the Advanced Sleep Mode Selection energy-saving feature, which does not rely on any input counters or metrics from the O-RU. In this scenario, it is unclear which counters are required or how power consumption could be measured across different sleep mode types.

# • Advanced sleep mode with M-PLANE OFF

Advanced sleep mode with M-PLANE OFF, also known as Deep-Hibernate sleep mode, please refer to clause 20.5 of O-RAN.WG4.MP.0-R004-v15.00 [i.10]

In a multi-operator scenario, it would be beneficial to measure or calculate the energy consumption for each operator. The current specification only requires the rx-windowmeasurement-objects.

# 6.1.1.4 Proposed Recommendations

Table 6.1.1.4-1 – O-RU Energy measurements related recommendations   

<table><tr><td colspan="1" rowspan="1">Recommendation ID</td><td colspan="1" rowspan="1">Title</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Motivation</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG4-REC-001</td><td colspan="1" rowspan="1">O-RU PerCarrier Powerconsumption</td><td colspan="1" rowspan="1">O-RU Power Efficiency in Multi-Band Operations Powerefficiency metrics should beavailable for each frequencyband in multi-band O-RUs,reporting the efficiency of eachband's energy consumption.</td><td colspan="1" rowspan="1">Facilitates fine-tuned energyoptimization by assessing andadjusting power usage for eachactive frequency band.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG4-REC-002</td><td colspan="1" rowspan="1">O-RU energyconsumption.PEE.Energy(kWh)</td><td colspan="1" rowspan="1">Total energy consumed by theO-RU during specificmeasurement period</td><td colspan="1" rowspan="1">Its part of ETSI ES 202 336-12v1.2.1 [i.8], however notincluded in O-RAN WG4 EPE-STAT.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG4-REC-003</td><td colspan="1" rowspan="1">O-RU Energyconsumptionduring M-Planeoff (DeepHibernate)</td><td colspan="1" rowspan="1">The O-RU should report itsenergy consumption for theperiod when it was in deephibernate mode after the M-Plane connection is re-established.</td><td colspan="1" rowspan="1">When the M-Plane is off, theO-RU cannot report real-timeenergy consumption data,making it difficult for operatorsto monitor energy usageduring hibernation. Byproviding energy consumptiondata after re-establishing theM-Plane, operators canaccurately assess energy</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">savings and manageconsumption during deephibernate periods.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG4-REC-004</td><td colspan="1" rowspan="1">O-RU Real-TimePowerMonitoring</td><td colspan="1" rowspan="1">Real-time power consumptionmetrics should be accessiblefrom the O-RU to monitortransient power changesdynamically</td><td colspan="1" rowspan="1">Enables continuous tracking ofpower fluctuations, supportingimmediate adjustments inenergy managementstrategies, especially valuablein high-demand or multi-tenant deployments.</td></tr><tr><td colspan="1" rowspan="1">SuFG-to-WG4-REC-005</td><td colspan="1" rowspan="1">O-RU PowerConsumptionper AntennaArray</td><td colspan="1" rowspan="1">Detailed power consumptionmetrics for each antenna arrayin MIMO configurations withinthe O-RU.</td><td colspan="1" rowspan="1">Supports energy optimizationin MIMO setups by enablingpower adjustments forindividual antenna arraysbased on demand and usagepatterns</td></tr></table>

7

# O-CU & O-DU Energy related Measurements

# Foundational requirements for O-CU / O-DU

7.1.1 O-DU & O-CU Energy measurements reporting

7.1.1.1 Description

O-CU and O-DU to provide CNF level energy efficiency counters / KPIs (e.g. Traffic load / data volume / throughput), which is to be reported through O1 interface to the SMO or through NBI to external tooling.

Reference (MoU Requirement “rel_2_O-CU_O-DU_66”)

7.1.1.2 Current Standard Analysis

7.1.1.2.1 O-RAN ALLIANCE references

WG1 has identified a similar requirement in their Network Energy Saving Use Cases Technical Report O-RAN.WG1.NESUC-R003-v02.00 [i.3].

WG2 is using O-CU/O-DU EC measurements in Non-RT RIC & A1/R1 interface: Use Cases and Requirements, see clause 4.8 in O-RAN.WG2.Use-Case-Requirements-R003-v09.00 [i.23] but only for O-CU/O-DU deployed as PNF.

In the ongoing Study on O-Cloud Energy Savings (current draft version O-RAN.WG6.O-Cloud Energy Savings.v00.00.07[i.5], WG6 has stated the following in clause 6.4:

“It is expected that the SMO can compute the Energy consumption and efficiency of a Cloudified NF based on measurements from the O-Cloud”

# 7.1.1.2.2

# 3GPP and ETSI reference

Refer to Clause 5.2.2 in the document.

7.1.1.3 Gap Analysis

The O-CU and O-DU can exist as Cloudified NFs, or Physical NFs and energy consumption metrics should be available in SMO for both deployment options.

■ When the O-CU and O-DU are deployed as PNFs, the reporting of energy consumption by both will be via the O1 interface to the SMO.

When the O-CU and O-DU are deployed as VNFs/CNFs, the reporting of energy consumption of O-Cloud resources should be via the O2 interface and a management function in SMO would need to determine energy consumption for the O-CU and O-DU NF deployment. The issue has not yet been addressed.

# 7.1.1.4 Proposed Requirements or Recommendations

Table 7.1.1.4-1 – PNF O-CU & O-DU Energy measument recommendations   

<table><tr><td>Recommendatio n ID</td><td>Title</td><td>Description</td><td>Motivation</td></tr><tr><td>SuFG-to-WG10- REC-001</td><td>O-CU/O-DU Energy Reporting for PNFs</td><td>O-CU and O-DU to report energy efficiency metrics as Physical Network Functions (PNFs) via the O1 interface, including energy usage KPIs such as power consumption per data volume and per traffic load.</td><td>Provides a standardized energy reporting method for PNFs, allowing the SMO to analyze and manage energy efficiency across both cloudified and non-cloudified O-CU and O-DU deployments.</td></tr></table>

8

# SMO Automations

Foundational requirements on SMO Automations

8.1.1 SMO Capabilities related to Energy Measurements

8.1.1.1 Description

SMO is capable to receive energy metrics / create KPIs to optimize the management devices Reference [i.2] (MoU Requirement rel_1_SMO_62)

8.1.1.2 Current Standard Analysis

8.1.1.2.1 O-RAN ALLIANCE references

The same references apply as described in clause 5.1.3.2.1.

8.1.1.2.2 3GPP and ETSI references

EE KPIs are defined in 3GPP TS 28.554 [i.9]. clause 6.7.1 NG-RAN data Energy Efficiency (EE) for PNFs.

Additionally, the same references apply as described in clause 5.1.3.2.2.

# 8.1.1.3 Gap Analysis

Looking at the MoU requirement and the standards references above, SuFG TG2 identified following gaps:

Missing specification of SMOS for collecting relevant PM measurements (as defined in 3GPP TS 28.552 [i.6])

■ Missing specification of SMOS for calculating EE KPIs as defined in 3GPP TS 28.554 [i.9]. clause 6.7.1 NG-RAN data Energy Efficiency (EE) for PNFs

■ Missing specification of SMOS for

collecting relevant PM measurements of O-Cloud resources via the O2 interface • determining energy consumption for the O-CU and O-DU VNF/CNF deployment • for calculating EE KPIs as listed in Table 5.1.3.2.1-1

The following SMO requirement is closely related to this topic:

[i.2] MoU Requirement rel3_CaaS_125: “O-Cloud platform shall provide sufficient power, energy and environmental (PEE) parameter and measurement data details in order to compute meaningful KPIs (e.g., state if the data is an instantaneous value or an average, declare the rolling window size in case of average, etc.) and, if appropriate, it should provide control over some parameters (e.g. change size of rolling window for average).”,

# 8.1.1.5 Proposed Recommendation

Table 8.1.1.5-1 – SMO related Energy measument recommendations   

<table><tr><td rowspan=1 colspan=1>Recommendation ID</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Motivation</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG10-REC-002</td><td rowspan=1 colspan=1>Calculation ofEnergy EfficiencyKPIs</td><td rowspan=1 colspan=1>SMO to calculate energy efficiency KPIsusing 3GPP-based performance data (e.g.energy per data volume, energy per user)for O-RAN components, including O-CUand O-DU, deployed as both PNFs andVNFs/CNFs.</td><td rowspan=1 colspan=1>Supports standardized KPI calculationsacross diverse deployments, enablingconsistent energy performance monitoringand benchmarking.</td></tr><tr><td rowspan=1 colspan=1>SuFG-to-WG10-REC-003</td><td rowspan=1 colspan=1>Granular Controlover MeasurementParameters</td><td rowspan=1 colspan=1>SMO to allow control over specificmeasurement parameters, such as settingthe size of rolling windows for averages ordefining intervals for energy datacollection, to enhance data accuracy andrelevance.</td><td rowspan=1 colspan=1>Provides flexibility in managing energy datagranularity, enabling more precise energyusage analysis and customized reportingbased on operational needs.</td></tr></table>

# Annex:

# Change history/Change request (history)

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2024.03.28</td><td rowspan=1 colspan=1>00.00.01</td><td rowspan=1 colspan=1>First draft version</td></tr><tr><td rowspan=1 colspan=1>2024.05.02</td><td rowspan=1 colspan=1>00.00.02</td><td rowspan=1 colspan=1>Updates according to review comments,Completion of previously empty sections</td></tr><tr><td rowspan=1 colspan=1>2024.10.31</td><td rowspan=1 colspan=1>00.00.04</td><td rowspan=1 colspan=1>Updates on format requirements, remove shall statements and major updates to align withO-RAN related recommendations.</td></tr><tr><td rowspan=1 colspan=1>2024.11.13</td><td rowspan=1 colspan=1>00.00.05</td><td rowspan=1 colspan=1>Requirements changed to recommendations, added recommendations for O-RU, O-CU/O-DU and SMO.</td></tr><tr><td rowspan=1 colspan=1>2024.11.27</td><td rowspan=1 colspan=1>00.00.06</td><td rowspan=1 colspan=1>Several editorial corrections.</td></tr></table>