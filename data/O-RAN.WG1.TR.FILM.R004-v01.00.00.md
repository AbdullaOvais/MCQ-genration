# O-RAN Work Group 1 (Use Cases and Overall Architecture) Filtered Measurements

# Contents

List of figures ... .4

List of tables .................................................................................................................................................4   
Foreword ...... .............................................................................................................................................5   
Modal verbs terminology..... ............................................................................................................ ......5   
Executive summary ....... ............................................................................................................ .......5   
1 Scope....... ........................................................................................................................ ........6   
2 References ..........................................................................................................................................6   
2.1 Normative references................................................................................................................................... 6   
2.2 Informative references ........... ...................................................................................................................... 6   
3 Definition of terms, symbols and abbreviations ...................................................................................7   
3.1 Terms...... ........................................................................................................... 7   
3.2 Symbols ...... ................................................................................................................... 7   
3.3 Abbreviations...... ................................................................................... 7   
4 Measurement data filtering in O-RAN.................................................................................................8   
4.1 Usages of measurement data filtering ........................................................................................................... 8   
4.1.1 xApp and rApp performance evaluation....... .... 8   
4.1.2 xApp and rApp operation ....................................................................................................................... 9   
4.2 Current approaches to measurement data filtering in O-RAN............................................................... ...... 9   
4.2.1 O1 performance measurements with sub-counters................................................................................... 9   
4.2.2 O1 trace data and its filtering........................ ............................................................................... 9   
4.2.3 E2SM-KPM condition-based measurement.. ................................................................ ...... 9   
5 Filtered Measurements for O-RAN . ... 10   
5.1 Definition...... ..................................................... ..... 10   
5.2 Key requirements for Filtered Measurements .. .... 11   
5.3 5.3.1 5.3.2 Potential solutions for Filtered Measurements ...................................Solution 1: Enhanced PM job via O1 interface for O-CU/O-DU...Solution 2: Enhanced trace job via O1 interface for O-CU/O-DU . ............................................ ....... 13....... 13....... 14   
5.3.3 Solution 3: Enhanced PM job via O1 interface for Near-RT RIC exploiting E2SM-KPM . ..... 14   
6 Key use cases and benefits analysis......... ............ .......... ..... 15   
6.1 Use case #1: Massive MIMO optimization..... .................................................. ....... 15   
6.1.1 Background information........ ............................................................................... ..... 15   
6.1.2 Motivation ..................... .................................................................................................... 16   
6.1.3 6.1.4 Potential solution ................................................................................................................................. 17Benefits of Filtered Measurements........................................................................................................ 18   
6.2 Use case #2: Interference detection and optimization............................................................................. .... 19   
6.2.1 Background information....................................................................................................................... 19   
6.2.2 6.2.3 Motivation ..............Potential solution .... ........................................................................................ ..... 19..... 20   
6.2.3.1 Slow loop solution ............. .................................................................................................................. 20   
6.2.3.1.1 6.2.3.1.2 Interference detection and optimization .Interference suppression evaluation ....... ..................................................................................... .... 20.... 20   
6.2.3.2 Fast loop solution... .......................................................................... .. 20   
6.2.3.2.1 Interference detection and optimization . ....................................................................................... ...... 20   
6.2.4 Benefits of Filtered Measurements... .. 21   
6.3 Use case #3: QoE optimization ..... ..................................................................................... ...... 21   
6.3.1 Background information..... .................................................................................................. ..... 21   
6.3.2 Motivation .............. .................................................................................................................. 21   
6.3.3 6.3.4 Potential solution ................................................................................................................................. 22Benefits of Filtered Measurements........................................................................................................ 22   
6.4 Use case #4: MU-MIMO optimization ................................................................................................. . 23   
6.4.1 Background information....... ........................................................................................................ . 23   
6.4.2 Motivation ........ ................................ 23   
6.4.3 Potential solution ..... .............................................................................. ..... 23   
6.4.4 6.5 Benefits of Filtered Measurements........................................................................................................ 23Use case #5: UE capability based measurements ....................................................................................... 24   
6.5.1 Background information.... .............................................................................................................. 24   
6.5.2 Motivation .... ................................................................................................ .... 24   
6.5.3 Potential solution ......   
6.5.4 Benefits of Filtered Measurements........................................................................................................ 26

7 Conclusion and recommendations..... .. 26

Annex: Change history/Change request (history).. .27

# List of figures

Figure 5.1-1: Filtered Measurements on a graph considering a single filter data .... .. 11   
Figure 5.2-1: Aggregated data and per-UE data . . 12   
Figure 5.3.1-1: Enhanced PM job via O1 interface for O-CU/O-DU . . 13   
Figure 5.3.2-1: Enhanced trace job via O1 interface for O-CU/O-DU ... .... 14   
Figure 5.3.3-1: Enhanced PM job via O1 interface for Near-RT RIC exploiting E2SM-KPM.. .. 15   
Figure 6.1.1-1: The list of requested input data for AI/ML model training (quoted from Table 5.2.2.1-4 in [i.6]) . . 16   
Figure 6.1.3-1: Expected DL throughput histograms (bin distribution) with and without filtering . .17   
Figure 6.1.3-2: A proposed counter for DL PDCP throughput updated in a filtered event-triggered manner...... .. 17   
Figure 6.1.4-1: Histogram of DL PDCP UE throughput without ‘small or short traffic filtering’. . 18   
Figure 6.1.4-2: Histogram of DL PDCP UE throughput with ‘small traffic filtering’ .........   
Figure 6.3.3-1: Grouping of UEs with the same application based on RSRP and velocity. . 22   
Figure 6.5.1-1: Layer management for CA vs. non-CA capable UEs... .................................. .. 24   
Figure 6.5.2-1: Treatment of CA and non-CA UEs with and without Filtered Measurements..... . 25   
Figure 6.5.3-1: Potential solution for UE capability-based layer management . . 25

# List of tables

Table 4.2.3-1: Condition IEs corresponding to Label Information and Test Information [i.8]... . 10   
Table 5.2-1: Target data and filter data per use case identified in clause 6 .. . 12   
Table 6.3.3-1: Example of UE grouping based on RSRP and velocity...... .22

# Foreword

This Technical Report (TR) has been produced by WG1 of the O-RAN ALLIANCE.

The content of the present document is subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN ALLIANCE modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\mathbf { X } \mathbf { X } { = } 0 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# Executive summary

As the O-RAN ecosystem continues to expand, the App market for the RAN Intelligent Controllers (RICs), which are responsible for key cornerstones of O-RAN, will also grow significantly. In anticipation of this trend, it is necessary to accurately evaluate the performance of rApps and xApps to enhance network performance as well as to establish well-defined inputs for their operations. In this context, the role of measurements of network quality is important in O-RAN architecture.

Traditional performance measurements make it difficult to clearly identify performance changes due to averaging errors, as they provide ambiguous results that reflect not only the targeted UEs but all UEs. On the other hand, using the MDT/UE tracing methods requires tracing many UEs per cell simultaneously, which places a significant processing burden on the O-DU/O-CU and also strains interface bandwidth due to the large volume of data. Because of that, in live networks, the traditional performance measurements are utilized only for overall network monitoring purpose and the MDT/UE tracing method is utilized in a limited way. For example, if we monitor the traditional KPI when the cells are on the energy saving mode, the exact level of UE performance degradation is hard to be captured since the KPI incorporates low traffic volume UEs, using the web or SNS, which are not significantly affected by energy saving.

Therefore, “Filtered Measurements” which include the performance measurement of the certain UEs of interest that are directly or indirectly related with the target behavior that the rApps or xApps are seeking to enhance or control, should be considered. By employing Filtered Measurements, network operators can conduct targeted analyses. This will enable easy and quick rApp and xApp validation. Also, in the context of rApp and xApp operation, Filtered Measurements serves a pivotal role by establishing quality data inputs especially when it comes to AI/ML-based rApps and xApps.

# 1

# Scope

The present document provides a Technical Report (TR) for Filtered Measurements in O-RAN. This TR captures the outcome of the WG1 UCTG Filtered Measurements pre-normative phase. The scope and objectives of the pre-normative phase are as follows:

• Examine the current state of measurement data filtering in O-RAN, including its usages and current supported approaches with their inherent limitations, as covered in clause 4.   
• Based on the limitations identified in clause 4, introduce Filtered Measurements and its requirements. Subsequently, investigate the possible enhancements to O-RAN, as covered in clause 5.   
• Investigate the use cases of Filtered Measurements, as covered in clause 6.   
• Provide the conclusion of the present document and recommendations for the further works, as covered in clause 7.

# 2 References

# 2.1 Normative references

Not applicable.

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

<table><tr><td>[i.1]</td><td>3GPP TR 21.905: "Vocabulary for 3GPP Specifications".</td></tr><tr><td>[i.2]</td><td>O-RAN.WG1.TR.Use-Cases-Analysis-Report-R004-v15.00: "O-RAN Working Group 1 (Use Cases and Overall Architecture) Use Cases Analysis Report'".</td></tr><tr><td>[i.3]</td><td>O-RAN.WG1.TS.Use-Cases-Detailed-Specification-R004-v15.00: "O-RAN Working Group 1 (Use Cases and Overall Architecture) Use Cases Detailed Specification".</td></tr><tr><td>[i.4]</td><td>3GPP TS 28.552: "Management and orchestration; 5G performance measurements", Release 18, September 2024.</td></tr><tr><td>[i.5]</td><td>3GPP TS 32.423: "Telecommunication management; Subscriber and equipment trace; Trace data definition and management", Release 18, September 2024.</td></tr><tr><td>[i.6]</td><td>O-RAN.WG1.MMIMO-USE-CASES-TR-v01.00: "O-RAN Working Group 1 Massive MIMO Use Cases Technical Report".</td></tr><tr><td>[i.7]</td><td>O-RAN.WG10.TS.O1PMeas-R004-v02.00: "O-RAN Working Group 10 (OAM for O-RAN) O-RAN 01 Performance Measurements Specification".</td></tr><tr><td>[i.8]</td><td>O-RAN. WG3.TS.E2SM-KPM-R004-v06.00: "O-RAN Work Group 3 Near-Real-time RAN Intelligent Controller E2 Service Model (E2SM) KPM".</td></tr><tr><td>[i.9]</td><td>O-RAN.WG4.TS.MP.0-R004-v17.01: "O-RAN Working Group 4 (Open Fronthaul Interfaces WG) Management Plane Specification'".</td></tr><tr><td>[i.10]</td><td>3GPP TS 28.622: "Telecommunication management; Generic Network Resource Model (NRM); Integration Reference Point (IRP); Information Service (IS)", Release 18, September 2024.</td></tr><tr><td>[i.11]</td><td>3GPP TS 32.422: "Telecommunication management; Subscriber and equipment trace; Trace control and configuration management"', Release 18, September 2024.</td></tr><tr><td>[i.12]</td><td>3GPP TS 37.320: "Radio measurement collection for Minimization of Drive Tests (MDT); Overall description; Stage 2", Release 18, September 2024.</td></tr><tr><td>[i.13]</td><td>3GPP TS 28.558: "Management and orchestration; UE level measurements for 5G system", Release 18, September 2024.</td></tr><tr><td>[i.14]</td><td>O-RAN.WG10.TS.O1-Interface.0-R004-v15.00: "O-RAN Work Group 10 (OAM for O-RAN) O-RAN O1 Interface Specification'".</td></tr><tr><td>[i.15]</td><td>O-RAN.WG3.TS.UCR-R004-v07.00: "O-RAN Work Group 3 (Near-Real-time RAN Intelligent Controller) Use Cases and Requirements".</td></tr><tr><td>[i.16]</td><td>3GPP TS 32.425: "Telecommunication management; Performance Management (PM); Performance measurements Evolved Universal Terrestrial Radio Access Network (E-UTRAN)", Release 18, April 2024.</td></tr><tr><td>[i.17]</td><td>3GPP TS 38.331 "NR; Radio Resource Control (RRC) protocol specification".</td></tr></table>

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms given in [i.1] and the following apply:

Filtered Measurements: Measurement data selectively obtained by NFs from performance observations associated with UEs that meet specific, pre-defined filtering conditions.

Target data: A configuration parameter for Filtered Measurements, referring to the measurement data to be retrieved (e.g., 3GPP or O-RAN defined performance measurements).

Filter data: A configuration parameter for Filtered Measurements, referring to the measurement variables used to define the filtering conditions.

# 3.2 Symbols

Void

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in [i.1] and the following apply:

3GPP Third Generation Partnership Project   
5QI 5G QoS Identifier   
AI/ML Artificial Intelligence and Machine Learning   
BSR Buffer Status Report   
CQI Channel Quality Indicator   
DL Downlink   
eNB evolved Node B   
FILM Filtered Measurements   
gNB next generation Node B   
GoB Grid of Beams   
HARQ Hybrid Automatic Repeat Request   
iBLER Initial Block Error Rate   
ICIC Inter-Cell Interference Coordination   
IMEI International Mobile Equipment Identity   
IMSI International Mobile Subscriber Identity   
IOC Information Object Class   
KPI Key Performance Indicator   
LTE Long Term Evolution   
MCS Modulation and Coding Scheme   
MDT Minimization of Drive Tests   
MIMO Multiple Input Multiple Output   
mMIMO Massive MIMO   
MnS Management Service   
MU-MIMO Multi-User MIMO   
NG-RAN Next Generation Radio Access Network   
NR NSA New Radio Non-Standalone   
NR SA New Radio Standalone   
O-CU O-RAN Central Unit   
O-CU-CP O-RAN Central Unit - Control Plane   
O-CU-UP O-RAN Central Unit - User Plane   
O-DU O-RAN Distributed Unit   
O-RU O-RAN Radio Unit   
PDCP Packet Data Convergence Protocol   
PHR Power Headroom Report   
PLMN Public Land Mobile Network   
PM Performance Measurements / Performance Management   
PMI Precoding Matrix Indicator   
PRB Physical Resource Block   
QoE Quality of Experience   
RLF Radio Link Failure   
RNOAMF RAN NF OAM SMO Function   
RSRQ Reference Signal Received Quality   
RSSI Received Signal Strength Indicator   
S-NSSAI Single Network Slice Selection Assistance Information   
S-TMSI 5G Temporary Mobile Subscriber Identity   
SRS Sounding Reference Signal   
SS-RSRP Synchronization Signal Reference Signal Received Power   
SU-MIMO Single-User MIMO   
SUPI Subscription Permanent Identifier   
UE User Equipment   
UL Uplink   
VR Virtual Reality

# 4 Measurement data filtering in O-RAN

In this document, the measurement data filtering refers to the process of selectively extracting performance data based on predefined criteria, offering a balance between the granularity of per-UE data and aggregated data. This intermediate approach is critical in providing actionable insights while managing data volume effectively, ensuring that only relevant data is analysed for network optimization. Clause 4.1 highlights the key usages of measurement data filtering in O-RAN, particularly in enabling performance evaluation and operational enhancements for xApps and rApps. Clause 4.2 explores the current approaches to measurement data filtering, analysing their methodologies and inherent limitations to identify areas for improvement.

# 4.1 Usages of measurement data filtering

# 4.1.1 xApp and rApp performance evaluation

Measurement data filtering enables network engineers to conduct targeted performance evaluations by focusing on the impact of configuration changes applied by xApps and rApps. Consequently, engineers can isolate and analyse the metrics that reflect

performance variations of their interest, ensuring an accurate assessment of the network's response to these configurations. This facilitates continuous improvement in network functionality and operational efficiency.

Data collected from the O-DU or O-CU is delivered to the RNOAMF within the SMO framework via the O1 interface or other interfaces. The engineers then can utilize this filtered data from RNOAMF to monitor and evaluate the performance of xApps and rApps, either through file-based reports or real-time data streams, depending on the monitoring requirements.

# 4.1.2 xApp and rApp operation

Measurement data filtering enables xApps and rApps to use filtered measurement data as an essential input for their operations and to rely on it again to monitor the outcomes of these operations. This feedback loop ensures that the applications can adapt to dynamic network conditions and achieve their intended objectives. In the case of AI/ML-based xApps and rApps, high-quality and relevant measurement data is critical for both training and inference phases, supporting accurate decision-making and operational optimization.

rApps consume measurement data through RNOAMF within the SMO framework. On the other hand, xApps collect and consume measurement data directly from the O-DU or O-CU through E2 interface. This direct integration allows xApps to both act on the data in real-time and evaluate the effects of their operations, creating a closed loop of data utilization.

# 4.2 Current approaches to measurement data filtering in O-RAN

# 4.2.1 O1 performance measurements with sub-counters

In 3GPP TS 28.552 [i.4], 5G performance measurements (PMs) are specified. O-RAN defines additional PMs by extending 3GPP-defined PMs and introducing O-RAN-specific PMs in the O1 Performance Measurements Specification [i.7]. These PMs are calculated per O-CU-CP, O-CU-UP, O-DU, or cell. For these PMs, the 3GPP filtering mechanism can be applied, allowing the PMs to be refined by creating sub-counters with single or multiple filters combined. In the current specifications, the applicable filters include 5QI, SNSSAI, and PLMN.

However, the current sub-counters have limitations due to the limited range of applicable filters, which prevents the generation of PMs focused on specific targets. This means sub-counters filtered in broad ranges, such as 5QI, SNSSAI, and PLMN, lack the ability to capture finer details. For example, in the interference detection and optimization use case, the control target is not users with a specific 5QI or slice, but rather UEs with high interference, such as cell-edge UEs. By using PMs focused on this group of UEs for control and evaluation, performance in interference suppression can be maximized. In the massive MIMO optimization use case, using PMs focused on the group of UEs with high traffic volume, which have significant gain from the use of massive MIMO, can further enhance performance. However, sub-counters focused on these aspects are not available in the current specifications. This leads to distorted analysis using PMs calculated with irrelevant data, resulting in lower performance.

# 4.2.2 O1 trace data and its filtering

This clause describes O1 trace data, which offers much higher granularity by operating at the UE or call level. This enables grouping based on specific characteristics such as CQI, rank, or traffic volume, providing highly detailed insights, only after applying the trace to a number of UEs. However, the sheer volume of trace data imposes significant processing burdens on ODU or O-CU, making this approach impractical for efficient system operation. Therefore, such data should be able to be filtered by additional functions located in the Network Function such as the O-DU and O-CU.

The size of collected data would be huge if it includes all UEs or is collected with high periodicity. To address this, a strict file size limit is sometimes imposed, with excess data discarded for that period. Alternatively, a sampling approach may be employed — for example, recording traces from only $20 \%$ of devices. However, typically, only a small fraction of such reports proves useful for any specific analysis, making this process inefficient in terms of bandwidth and storage utilization. Furthermore, trace data is considered low priority and is the first to be dropped in the event of processing or transport issues. These limitation methods risk discarding critical information, potentially impacting the analysis.

# 4.2.3 E2SM-KPM condition-based measurement

In [i.8], it is specified that the E2 Node hosts the RAN Function “KPM Monitor”, which provides several key functionalities, including the exposure of available measurements from the O-DU, O-CU-CP, and/or O-CU-UP via the RAN Function Definition

IE, and the periodic reporting of measurements subscribed by the Near-RT RIC. Notably, the “KPM Monitor” RAN Function also supports condition-based measurement through certain RIC REPORT Service Styles. This condition-based approach offers greater granularity compared to traditional PM data and incorporates some of the benefits of trace data, such as finer insights at the UE or call level. As a result, E2SM-KPM is an effective tool for addressing data needs in use cases requiring high levels of responsiveness and precision.

More specifically, measurement data filtering is enabled by the Matching Condition IE included in E2SM-KPM Action Definition Formats 3 and 4, corresponding to RIC Service Styles 3 and 4, respectively. The Matching Condition is further divided into two categories: Label Information and Test Information. Label Information functions similarly to a subcounter, grouping data into predefined categories, while Test Information identifies UEs that meet specific conditions. Table 4.2.3-1 lists the available conditions IEs in [i.8] for Label Information and Test Information. It is notable that the conditions are added according to the identified use cases across O-RAN working groups.

Table 4.2.3-1: Condition IEs corresponding to Label Information and Test Information [i.8]   

<table><tr><td>Label Information</td><td>Test Information</td></tr><tr><td>PLMN ID</td><td>GBR</td></tr><tr><td>Slice ID</td><td>AMBR</td></tr><tr><td>5QI</td><td>IsStat</td></tr><tr><td>QFI</td><td>IsCatM</td></tr><tr><td>QCI</td><td>DL RSRP</td></tr><tr><td>Layer at MU-MIMO</td><td>DL RSRQ</td></tr><tr><td>SSB Index</td><td>UL RSRP</td></tr><tr><td>Non-GoB Beamforming Mode Index</td><td>CQI</td></tr><tr><td>MIMO Mode Index</td><td>5QI</td></tr><tr><td>CGI</td><td>QCI</td></tr><tr><td>Beam ID</td><td>S-NSSAI</td></tr></table>

Despite its advantages, E2SM-KPM data is accessible only to the Near-RT RIC (xApps) due to its reliance on the E2 interface. This restricts other entities, such as SMO or Non-RT RIC (rApps), from directly consuming this filtered data. This architectural limitation reduces the broader usability of E2SM-KPM across O-RAN architecture.

In addition, the predefined conditions in the current E2SM-KPM specification may not fully support more complex or dynamic use cases. For instance, the ability to filter measurement data based on UE’s traffic volume is either limited or undefined. This lack of sophistication in condition definitions hinders the adoption of E2SM-KPM for advanced scenarios requiring real-time adaptability and granularity, necessitating future enhancements to the specification.

# 5 Filtered Measurements for O-RAN

Based on the limitations identified in clause 4, this clause introduces Filtered Measurements and its key requirements. Subsequently, in accordance with the defined key requirements, it investigates possible enhancements to O-RAN

# 5.1 Definition

Filtered Measurements in the O-RAN architecture is a targeted approach to measurement data collection aimed at optimizing and evaluating the functionality of rApps and xApps. This method selectively gathers measurement data of UEs that meet specific, predefined criteria. At the core of Filtered Measurements is the idea that the intervention of rApps or xApps is not meant to uniformly impact all UEs in the cell. Instead, these interventions are hypothesized to have a more pronounced effect on specific UEs that may behave differently from the overall population. Therefore, measurement data needs to be filtered to focus on those UEs whose performance is expected to be most affected by the rApp or xApp intervention. The intervention, in this context, refers to changes in the network functions’ configuration set by the rApp or xApp.

The O-DU or O-CU regularly collects performance data, where data points corresponding to each UE consist of multiple performance metrics. Among these, a specific variable of interest, referred to as target data, is monitored to evaluate performance changes. Filtered Measurements can apply one or more filtering criteria based on filter data. These filtering criteria help select a subgroup of UEs that are most relevant for performance analysis. When multiple filter data variables are used, a combination of these variables can define more complex filtering conditions, allowing for greater precision in identifying UEs likely to be most affected by the rApp or xApp intervention.

![](images/de7fdaecc036d062c798ab4aae27280985b8514fc0844ec3a0b5d811b9eb59be.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.1-1: Filtered Measurements on a graph considering a single filter data

In summary, while no meaningful change in the average of the target data may be observed across all UEs, a significant difference can emerge when analysing only those UEs that meet the conditions defined by the filter data. This selective measurement approach allows for more targeted and effective performance evaluation, ensuring that rApps and xApps can be fine-tuned based on relevant data rather than noise from the entire dataset.

# 5.2 Key requirements for Filtered Measurements

This clause defines the key requirements for Filtered Measurements in the O-RAN architecture. These requirements are derived from the use cases identified in clause 6. The primary goal of Filtered Measurements is to enable rApps (and SMO) and xApps (and Near-RT RIC) to retrieve relevant performance data — either in aggregated or per-UE level (figure 5.2-1) — for a subset of UEs that satisfy specific, predefined conditions.

REQ-FILM-01: The Filtered Measurements functionality should be applicable to NR SA, NR NSA, and LTE.   
• REQ-FILM-02: Filtered Measurements should support the capability to retrieve target data for UEs that meet specific filtering conditions, which are defined based on given filter data.   
• REQ-FILM-03: Filtered Measurements should support the capability to filter out data that is not required for a specific purpose before it is retrieved, in order to reduce the volume of data that is carried over an interface.   
• REQ-FILM-04: Filtered Measurements should support the capability to retrieve target data in real-time streaming.   
• REQ-FILM-05: Filtered Measurements should support the capability to retrieve target data in file-based bulk transfer.   
• REQ-FILM-06: The target data should consist of performance measurements defined by 3GPP or the O-RAN Alliance, such as 3GPP TS 28.552 [i.4], 3GPP TS 32.425 [i.16], 3GPP TS 28.558 [i.13], 3GPP TS 32.423 [i.5], or O-RAN TS WG10.PMeas [i.7]. REQ-FILM-07: The filter data used to define a subset of UEs should be configurable and may involve single or multiple parameters in combination.   
• REQ-FILM-08: The time window used to evaluate whether UEs belong to a given group based on filter data should be configurable independently of the measurement granularity.   
• REQ-FILM-09: The SMO should be able to retrieve aggregated target data (e.g., sum, average, distribution) for UEs that meet specific filtering conditions, which can be used as input for rApps or for evaluation of rApps.   
• REQ-FILM-10: The SMO should be able to retrieve per-UE target data for UEs that meet specific filtering conditions, which can be used as input for rApps or for evaluation of rApps.

REQ-FILM-11: Near-RT RIC should be able to retrieve aggregated target data (e.g., sum, average, distribution) for UEs that meet specific filtering conditions, which can be used as input for xApps.

REQ-FILM-12: Near-RT RIC should be able to retrieve per-UE target data for UEs that meet specific filtering conditions, which can be used as input for xApps.

# Aggregated data

# Per-UE data

Aggregated data collected from UEs that meet the fitering conditions within a measurementobject (e.g., NRCellDU, NRCellCU), and calculating totals, averages, distributions, etc.

Per-UE data collected from UEs that meet thefiltering conditions.

![](images/5e2c09be0bf7176a1ee0e05ef0d027399ce2efd3ca4ee5baf48739a52371a710.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2-21: Aggregated data and per-UE data

Table 5.2-21: Target data and filter data per use case identified in clause 6   

<table><tr><td rowspan=1 colspan=1>Use Case</td><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source d)target</td><td rowspan=1 colspan=1>Target data</td><td rowspan=1 colspan=1>Filter data</td><td rowspan=1 colspan=1>Aggregatedor Per-UE</td><td rowspan=1 colspan=1>New orexisting</td></tr><tr><td rowspan=1 colspan=1>Massive MIMOOptimization</td><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU d)SMO</td><td rowspan=1 colspan=1>- DL/UL UEthroughput- DL PDCPthroughput</td><td rowspan=1 colspan=1>- Traffic volume- MIMO mode index</td><td rowspan=1 colspan=1>Aggregated</td><td rowspan=1 colspan=1>Partially new</td></tr><tr><td rowspan=1 colspan=1>InterferenceDetection andOptimization</td><td rowspan=1 colspan=1>O1/E2</td><td rowspan=1 colspan=1>O-DU →SMO/Near-RT RIC</td><td rowspan=1 colspan=1>- DL SS-SINR perUE- UL CQI per UE- UL MCS per UE- Throughput perUE- Uplinkinterference perUE</td><td rowspan=1 colspan=1>- UE ID- Slice ID- PRB usage per cell - DL SS-RSRP per UE,UL SRS-RSRP per UE</td><td rowspan=1 colspan=1>Aggregated/Per-UE</td><td rowspan=1 colspan=1>Partially new</td></tr><tr><td rowspan=1 colspan=1>QoE Optimization</td><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU →SMO</td><td rowspan=1 colspan=1>- Latency- Throughput- RLF ratio- iBLER- PRB allocation</td><td rowspan=1 colspan=1>- Slice ID-5QI- RSRP- Traffic volume- Velocity</td><td rowspan=1 colspan=1>Aggregated</td><td rowspan=1 colspan=1>Partially new</td></tr><tr><td rowspan=1 colspan=1>MU-MIMOOptimization</td><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU d)SMO</td><td rowspan=1 colspan=1>- DL/ULthroughput- iBLER- MU-MIMO PRButilization- Spectralefficiency- CQI, RI</td><td rowspan=1 colspan=1>- MIMO mode (SU/MU-MIMO)- Slice ID- Scheduled MU-MIMOUE list</td><td rowspan=1 colspan=1>Aggregated</td><td rowspan=1 colspan=1>Partially new</td></tr><tr><td rowspan=1 colspan=1>UE capabilitybasedmeasurements</td><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU dSMO</td><td rowspan=1 colspan=1>- RSRP- Throughput- Call quality</td><td rowspan=1 colspan=1>- UE capability- RSRP threshold- Throughput threshold</td><td rowspan=1 colspan=1>Per-UE</td><td rowspan=1 colspan=1>Partially new</td></tr></table>

# 5.3 Potential solutions for Filtered Measurements

In this clause, three potential solutions for Filtered Measurements is studied for future normative work, in which interface specifications will be enhanced to support this feature.

As stated in Clause 5.1, Filtered Measurements is aimed at selectively gathering performance data from UEs that meet specific predefined criteria, for purposes such as operation or evaluation of rApps or xApps.

From the perspective of rApps, to achieve this, each solution needs to enable the MnS consumer in the SMO to configure filter data and target data for the producer, and to collect the intended Filtered Measurements. On the other hand, xApps can collect Filtered Measurements by utilizing E2SM-KPM condition-based measurement [i.8]. Naturally, with the current specifications, there may be limitations in fully supporting more complex or dynamic use cases. Nevertheless, since E2SM-KPM can support Filtered Measurements by adding or modifying Label Information or Test Information, Clause 5.3 focuses on rApps.

# 5.3.1 Solution 1: Enhanced PM job via O1 interface for O-CU/O-DU

This solution aims to enhance the existing PM job to support Filtered Measurements. This will be enabled by incorporating the mechanism used for E2SM-KPM [i.8] into O1 interface for O-CU/O-DU, as described below.

Regarding filter data, the existing PMs already support filtering by sub-counters such as 5QI, SNSSAI, and PLMN [i.4]. However, the current method of appending sub-counters after the measurement name, in the format of "family.measurementName.subcounter" [i.10], is overly complex and lacks scalability when supporting various types of filter data. Therefore, it is preferable to add new attributes for configuring the filter data to NRMs for the existing PM job. Specifically, a new IOC for Filtered Measurements will be defined, which will inherit PerfMetricJob IOC (Clause 4.3.31 in [i.10]), and it will include attributes for filter data and threshold values.

Regarding target data, data supported in Filtered Measurements should include both aggregated data (e.g., cell-level) and UElevel data as shown in Figure 5.3.1-2.

For aggregated data, various PMs have been specified in TS 28.552 [i.4] and O1 PMeas [i.7]. This data is generated by aggregating data for all UEs within a measurement object, such as a cell (NRCellDU, NRCellCU), and calculating totals, averages, distributions, etc. In Filtered Measurements, data is aggregated only across UEs in the cell that meet the filter conditions.   
For UE-level data, the conversion mechanism employed in E2SM-KPM (Clause 7.9 in [i.8]) can be utilized for Filtered Measurements, allowing PMs defined per cell or per CU to be converted to UE-level data. For example, average DL UE throughput in gNB (Clause 5.1.1.3.1 in [i.4]) is calculated by dividing total transmitted data volume across all UEs in the cell by the total transmission time. To obtain UE-level data, this calculation is performed by focusing on the data volume and transmission time for a single UE. In addition, UE-level data is collected only from UEs that meet the filter conditions. This allows for the collection of a wide variety of UE-level data only from UEs of interest to support various use cases. For this purpose, the new IOC for Filtered Measurements mentioned above will also include attributes for selecting whether data is cell-level or UE-level.

![](images/2f3bfa2b88091cebebaf1148eda2eb9ac344b434f5972a1663fdca251acd36d0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.1-31: Enhanced PM job via O1 interface for O-CU/O-DU

# 5.3.2 Solution 2: Enhanced trace job via O1 interface for O-CU/O-DU

This solution aims to enhance the existing trace job to support Filtered Measurements by enabling the Trace MnS consumer in the SMO to configure filter data for TraceJob instances via the O1 interface. The goal is to allow O-CU and O-DU to apply trace jobs selectively to UEs that meet predefined conditions, with minimal impact on existing trace job structures.

TraceJob IOC, defined in TS 28.622 [i.10], supports multiple types of trace operations through attributes such as traceConfig, mdtConfig, and ueCoreMeasConfig. These job types include trace [i.11], Minimization of Drive Tests (MDT) [i.12], and UElevel performance measurements [i.13]. Each job type can be configured individually or in combination using the jobType attribute, as defined in TS 32.422 [i.11].

However, current target UE selection mechanisms under targetTrace are limited to static identifiers or location-based criteria. The selection is typically based on NG-RAN cells, area information, or subscriber/device identifiers such as IMSI, IMEI, SUPI, or S-TMSI. There is no mechanism to select UEs based on per-UE information that resides within the RAN, such as signal strength or data volume. As a result, it is not possible to restrict trace activation to a meaningful subset of UEs, which may lead to excessive trace data collection from all UEs or require vendor-specific random sampling implementations.

To address this, enhancements to the TraceJob IOC are required. This includes the introduction of new attributes that allow configuration of filter data with condition-based selection criteria. For example, thresholds on RAN-internal metrics may be specified to enable the MnS producer to autonomously select a subset of UEs for trace reporting. These enhancements would enable trace-based Filtered Measurements, while preserving compatibility with existing O-RAN O1 Trace Management Services as defined in O-RAN.WG10.TS.O1-Interface [i.14].

![](images/1515eb8cc28b1fb6b78430497a00cca739f0a53eac3c73bf785ba57e6c58095f.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2-1: Enhanced trace job via O1 interface for O-CU/O-DU

# 5.3.3 Solution 3: Enhanced PM job via O1 interface for Near-RT RIC exploiting E2SM-KPM

This solution aims to enhance the existing PM job to support Filtered Measurements by leveraging E2SM-KPM with the NearRT RIC. First, the MnS consumer in the SMO requests the MnS producer in the Near-RT RIC to generate performance metrics, i.e., Filtered Measurements. This process is equivalent to the one described in Solution 1; that is, the existing PM job is enhanced by adding new attributes to the NRMs for configuring filter data and target data. Second, upon receiving the request from the consumer, the producer in the Near-RT RIC communicates with one or more xApps via Near-RT RIC APIs to request the collection of measurement data. Upon receiving the request from the MnS producer, the xApps acquire condition-based measurements via the E2 interface using E2SM-KPM Style 3 and(or) Style 4. Using these data, the xApps generate the performance metrics, which are then transferred to the producer. Finally, the requested performance metrics are transferred from the producer to the consumer.

![](images/161d21dcda9b6d4588f1553d0437d6ed88afebf1a68bf1f771437b83ca39feab.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.3-1: Enhanced PM job via O1 interface for Near-RT RIC exploiting E2SM-KPM

# 6 Key use cases and benefits analysis

To analyse performance and enhance quality using Filtered Measurements, it is essential to select the appropriate use case, define suitable filtering criteria, and analyse the benefits of Filtered Measurements. Therefore, this clause aims to provide key use cases suitable for the application of Filtered Measurements, as well as the benefits derived from its application. In O-RAN WG1, numerous multi-WG use cases are defined and discussed. Use cases suitable for the application of Filtered Measurements will be selected from among those identified, and the expected benefits from applying the appropriate filtering criteria will be analysed. It is notable that the use cases for Filtered Measurements are not limited to those described in this clause.

# 6.1 Use case #1: Massive MIMO optimization

# 6.1.1 Background information

In the WG1 Massive MIMO use case TR [i.6], AI/ML-assisted non-GoB optimization is introduced along with its required input data for training. Specifically, it is assumed that the SMO/Non-RT RIC is responsible for obtaining beamforming configuration information from the gNB/O-DU, as well as for model training and the deployment of the xApp to the Near-RT RIC. The NonRT RIC first requests a report of supported beamforming configurations from the O-DU. Subsequently, the process enters the data collection phase, during which the Non-RT RIC requests data collection from the O-DU via O1 through the “Collection and Control” function. The O-DU responds with measurements over O1, such as SINR, with these measurements being associated with each of the N beamforming modes (referred to as the “associated non-GoB mMIMO mode”). Specific measurements defined in [i.4] may be reused, such as: average DL UE throughput in the gNB, wideband CQI distribution, RSRQ measurements, RSRP measurements, and SINR measurements. Additionally, information related to 3GPP configurations, such as SRS periodicity, is also reported. Using this data, the Non-RT RIC trains AI/ML model(s) that predict the relative performance between the N modes (or simply identify the best mode) and deploys the trained models in the xApp to the Near-RT RIC.

It is noteworthy that one of the requested input data items, "Average DL UE throughput [i.4] in gNB with associated non-GoB mMIMO mode," requires the introduction of a new per-UE reporting mechanism that incorporates the associated non-GoB mMIMO mode index.

![](images/98becff06dc96231fb019b5d31651e09076af7f04b3fdeeb9d344d11294f35ae.jpg)

> **Image Summary:** (Summary not available)


# 6.1.2 Motivation

The current methodologies employed by the Non-RT RIC for collecting, consuming and utilizing 'average DL/UL UE throughput with associated non-GoB mMIMO mode' encounter several challenges when utilized for non-GoB mMIMO optimization. These include:

Noise from small traffic UEs:

Small traffic UEs, characterized by low data volumes, introduce noise into throughput statistics. These low-traffic UEs, whose behavior is not related to beamforming modes, often dominate the dataset, skewing the distribution toward low-throughput values and obscuring meaningful distinctions between beamforming modes. This noise reduces the sensitivity of comparisons, as it fails to reflect the true performance capabilities of different configurations. High-traffic UEs, by contrast, provide data that better represents the network's ability to handle substantial traffic loads over extended periods, offering a more accurate assessment of beamforming performance.

Filtering with non-GoB mMIMO Mode Index:

E2SM-KPM defines condition-based measurements reports via E2 interface. In particular, its REPORT Service Style 3 (or Style 4), (common) condition-based UE-level measurements, employs Label Information IE as a condition to include the UEs with certain non-GoB mMIMO mode index. However, the measurements collected at the Near-RT RIC are not made accessible to the Non-RT RIC. Moreover, while the O1 Performance Assurance MnS is capable of selectively collecting measurements based on subcounters, it currently lacks subcounters related to MIMO modes.

# 6.1.3 Potential solution

It is proposed that the Non-RT RIC trains its model based on the "average DL/UL UE throughput in gNB with associated nonGoB mMIMO mode," considering only traffic that is large enough. The new measurements, so called Filtered Measurements in this document, filter out small traffic UEs, which act as noise. As shown in Figure 6.1.3-1, it is expected that throughput variations between two different beamforming modes will be captured more sensitively when only UEs with large and sustained traffic are considered. For example, the variants of red lines which refer to average of the throughput distribution are expected to be more significant with filtering rather than without filtering.

![](images/2894cc5031fef0a958cc7a03eb79d7280986b86c591745285e3476004ce3cfa2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1.3-1: Expected DL throughput histograms (bin distribution) with and without filtering

One possible solution involves pegging the counters in a filtered event-triggered manner within the O-DU or O-CU. These counters, referred to as the filtered counters, are updated whenever the traffic buffer for a DRB is emptied during the measurement interval. If filtering is applied, traffic bursts that are small in volume can be excluded, preventing them from triggering counter updates. Filtering can be implemented at either the traffic burst level or the DRB/UE level. Figure 6.1.3-2 illustrates how the counters are updated in a burst-level, filtered, event-triggered manner for DL PDCP UE throughput. The filtered counters are expected to be collected and consumed by the Non-RT RIC via the O1 interface through Performance Assurance MnS, similarly to how other traditional PMs are collected. This approach of generating Filtered Measurements based on the filtered counters enables a clearer and more accurate comparison of different beamforming modes, while the O1-based consumption of Filtered Measurements allows the Non-RT RIC to access the measurements without relying on E2SM-KPM.

![](images/5f3c41cd7b72d7a59e68a21f099b5733c56da11d03bf5d038b65ae325b0c25bf.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1.3-2: A proposed counter for DL PDCP throughput updated in a filtered event-triggered manner

# 6.1.4 Benefits of Filtered Measurements

To verify the benefits of Filtered Measurements, the changes in DL PDCP throughput statistics were analysed when applying SRS-based beamforming and PMI-based beamforming to a cluster in Gwangju, South Korea. Non-standard, vendor-specific statistics with filtering capabilities were utilized. When filtering was applied, only traffic bursts exceeding 8 Mbit in volume were included in the statistics. Additionally, the DL throughput statistics were extracted in the form of a bin distribution, with the bin size set to 150 Mbps.

Figures 6.1.4-1 and 6.1.4-2 below illustrate the effect of filtering on DL PDCP throughput distribution for SRS-based and PMIbased beamforming modes. The first histogram (without filtering) demonstrates a high concentration of low-throughput samples (0–150 Mbps), with negligible differentiation between the two beamforming modes. Conversely, the second histogram (with filtering) highlights a more distinct throughput distribution, where small traffic bursts are excluded, resulting in clearer distinctions between SRS-based and PMI-based beamforming in the higher throughput ranges. These results underline the importance of applying filtering to eliminate noise from low-volume traffic and enable meaningful performance comparisons between beamforming modes.

![](images/b591961c23027f03fc923493a2cb521a2ed26560929376f489e2ad39fd2cb806.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1.4-1: Histogram of DL PDCP UE throughput without ‘small or short traffic filtering’

![](images/8ab860c39b1dde02f3ba52564521f1c762a04bf2ca93cd1a0b1340cfa5c0b012.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1.4-2: Histogram of DL PDCP UE throughput with ‘small traffic filtering’

# 6.2 Use case #2: Interference detection and optimization

# 6.2.1 Background information

LTE and 5G networks face challenges with co-frequency interference due to limited radio resources, hindering network performance. Traditional Inter-Cell Interference Coordination (ICIC) solutions aim to manage radio resources across cells by restricting their use or adjusting transmitting power. However, these solutions face several limitations:

• They allocate resources statically or in non-real-time, resulting in low utilization.   
• They depend on ideal cell networking structures, performing poorly in complex networks.   
• They only support cell-level allocation, not user or user group levels.   
• They use measurement data for post-interference analysis rather than real-time adjustments.

The interference detection and optimization use case [i.2][i.3] addresses these limitations by dynamically managing radio resources for a specific UE, UE group, or slice, thus further improving the efficiency of radio resource utilization.

In addition to LTE and 5G interference, other non-3GPP types of interference experienced in a 5G network, including internal and external RF interference, need to be detected and optimized. To support effective interference optimization, there is a need to identify the source of the interference in terms of interference type and geographical location.

# 6.2.2 Motivation

The operation and performance evaluation for interference detection, classification, locating, and optimization should be performed based on interference-related data focusing on a specific UE group, e.g., a cell-edge UE group or a slice, which is the primary target of improvement. Especially in detection, classification, and locating, a greater variety of filtering criteria can be applied to achieve the objectives with more effectiveness. Otherwise, irrelevant data could cause inappropriate optimization or evaluation errors.

In case of the slow-loop optimization performed in the SMO/Non-RT RIC, the following data available in the SMO/Non-RT RIC pose the following challenges:

• Performance measurements such as SINR are defined per cell [i.4] and are not appropriate for optimizing interference and evaluating its effectiveness for the specific UE group. UE trace (MDT) data are defined per UE [i.5], but it is difficult to trace all the UEs belonging to the specific UE group because of the random selection of the traced UEs. This can lead to insufficient data for interference optimization and evaluation, and the influence on UEs which are not traced cannot be analysed. Moreover, data unnecessary for optimization and evaluation can be collected. For example, data can be collected from cell-center UEs which are not the target of the interference suppression due to the random selection of traced UEs, or data may be collected when the cell load is low and there is little interference. In addition, the data supported in MDT is limited and not enough for optimization and evaluation, e.g., UL RSRP is not available.   
• UE log data captured through driving tests can be used only for evaluation, but this approach requires time and effort. Moreover, the number of data samples that can be obtained in one drive is small, making it difficult to statistically evaluate the performance.

In case of the fast-loop optimization performed in Near-RT RIC, the predefined conditions in the current E2SM-KPM [i.8] specification may not fully support classification and locating use cases. For instance, the ability to filter measurement data based on UE’s direction or range is undefined. This lack of sophistication in condition definitions limits the accuracy and effectiveness in classification and locating.

The main objective of this use case is to address the above challenges and allow the SMO/Non-RT RIC or Near-RT RIC to collect necessary and sufficient data for the operation and evaluation for interference detection, classification, locating and optimization.

# 6.2.3 Potential solution

# 6.2.3.1 Slow loop solution

# 6.2.3.1.1 Interference detection and optimization

The proposed solution for interference detection and optimization aims to address the above challenges by allowing the SMO/Non-RT RIC to collect interference-related data from a specific UE group only when the cell load is high. Regarding the target data, interference-related data (e.g., DL SS-SINR, UL CQI, UL MCS), along with throughput, should be available to detect high interference situations and their impact on throughput, and to optimize the interference for the specific UE group. To allow the SMO/Non-RT RIC to collect data only from target UEs, filter data should include identifiers such as a list of UE IDs and Slice IDs. Additionally, filter data should include PRB usage of a cell to filter out data in cases where the cell load is low, and interference optimization is not necessary. A more variety of filter data should be supported to optimize interference according to the situation. For example, reception power (e.g., DL SS-RSRP, UL SRS-RSRP) can be supported to focus on the interference of the cell-edge UEs with low reception power. Data volume can also be supported to focus on the performance of UEs that cause primary interference and suffer from it. This prevents unnecessary data collection in the SMO/Non-RT RIC, thereby reducing wasteful use of the bandwidth of the interface.

# 6.2.3.1.2 Interference suppression evaluation

The target data and filter data used for interference suppression evaluation are almost the same as those required for detection and optimization. One difference is that, in evaluation, real-time data is not always necessary. In other words, there is a potential option for accumulating data in O-CU/O-DU and transferring it in bulk to the SMO/Non-RT RIC.

# 6.2.3.2 Fast loop solution

# 6.2.3.2.1 Interference detection and optimization

The potential solution is to address the above challenges in interference detection, classification and locating performed in NearRT RIC by using filtering criteria on target data. The filtering criteria for target data generated from E2 nodes can be based on a combination of:

• per cell (e.g., UL/DL loading per cell, UL interference per cell, UL interference per PRB per cell)   
• per sector   
• per beam (e.g., UL interference per PRB per antenna branch per cell)   
• per direction (e.g., target data is from the direction of multiple beams or target data with location information)   
• per UE or per group of UEs   
• per range (e.g., target data is from those UEs within a certain range of a cell)   
• per pattern (e.g., uplink RSSIs pattern or uplink PRB interference pattern)   
• per threshold level

where per cell, per sector, per UE or per group of UEs have been supported in E2SM-KPM [i.8].

xApps use processed target data from E2 nodes by applying filtering criteria. The target data generated from E2 nodes includes the following:

1) Network-level measurement reports, including

a) UE-level information, e.g., CQI, SINR, MCS, UL/DL RSRP, SS-RSRP, throughput, DU/UL PRB usage, mMIMO beams, BSR, PHR, location, velocity and timing advance

b) Cell-level information: e.g., DL/UL PRB usage, throughput, uplink interference including UL interference per cell, UL interference per PRB per cell, and UL interference per PRB per antenna branch per cell as specified in WG3 UCR use case 6

2) Received power measurements (i.e., received signal strength indicators [RSSIs]) from O-RU as specified in clause 21 in [i.9].

The xApps with the support of AI/ML analyse the target data that matches the filtering criteria to achieve the objectives. The objectives include:

Detect cells, sectors, beams, UEs, or resources of cells that are under interference when their interference levels exceed certain thresholds   
• Classify types of interference source, e.g., the uplink interference types can be classified when the uplink interference levels experienced on certain cell resources (e.g., received uplink RSSIs or uplink PRB) exceed certain thresholds and the uplink interference patterns match certain profiles   
• Identify geographical location of interference source, e.g., the source of uplink interference can be located by leveraging triangulation on the beams when the interference levels experienced on those beams exceed certain thresholds

# 6.2.4 Benefits of Filtered Measurements

The proposed solution for operation and evaluation for interference detection and optimization requires the SMO/Non-RT RIC to collect measurement data only from UEs that meet specific filtering conditions (e.g., identifiers, reception power) when another filtering condition (e.g., PRB usage of a cell) is met. This feature is assumed to be offered by Filtered Measurements, allowing SMO/Non-RT RIC to collect target data exclusively for specific entities and cases that satisfy the conditions defined by filter data. This enables optimization and evaluation focused on specific targets, using sufficient and necessary data while avoiding the collection of irrelevant data.

Similarly, with Filtered Measurements, that offer more granular data suitable for the process of conducting interference detection, classification and locating in Near-RT RIC, the effectiveness for the process can be improved. In turn, the effectiveness of conducting interference optimization is improved.

# 6.3 Use case #3: QoE optimization

# 6.3.1 Background information

Highly demanding 5G native applications like cloud VR and connected vehicles are both bandwidth consuming and latency sensitive; however, they are today often handled in a best effort way with low or no application specific optimization. These traffic-intensive and highly interactive applications are not well served by current semi-static QoS framework which does not efficiently satisfy diversified QoE requirements. These requirements can vary during an application lifetime, especially taking into account potentially significant fluctuation in radio transmission capability and applications with dynamic performance requirements. Furthermore, an increased set of mobile applications with varying QoE demands will increasingly become unmanageable if semi-static profiles are “preloaded” into the relevant RAN nodes without a more automated closed-loop approach. It is expected that QoE estimation/prediction from application level can help deal with such uncertainty and improve the efficiency of radio resources, and eventually improve user experience and yield a more efficient use of RAN resources.

Also, multi-dimensional data, e.g., user traffic data, QoE measurements, network measurement report, can be acquired and processed via ML algorithms to support traffic recognition, QoE prediction, QoS enforcement decisions.

# 6.3.2 Motivation

The main objective of QoE optimization use case [i.2] is to support QoE optimization within the O-RAN architecture and its open interfaces by enabling per-user, slice, or 5QI-based modification of RAN behavior, features, scheduling, and other configurations according to application requirements or other inputs. To achieve this, a QoE optimization approach utilizing the SMO, Non-RT RIC, and Near-RT RIC has been proposed.

The SMO/Non-RT RIC collects O1 PM data to build and train relevant AI/ML models, while the Near-RT RIC optimizes QoE operations by leveraging policy inputs and E2SM-KPM data. However, unlike the Near-RT RIC, which gathers extensive perUE information through the E2 interface, the SMO/Non-RT RIC has limited access to detailed data via O1 PM. This limitation could lead to biased evaluations, making it difficult to generate optimized policies.

For example, when monitoring a group of UEs using a specific service within a cell, different QoE optimization actions may be required based on varying radio conditions and velocity, even among UEs running the same application. To achieve effective QoE optimization, it is essential to classify and monitor UEs based on these contextual differences. However, the available O1 PM data is insufficient to enable such granular classification.

One possible solution is to utilize O1 trace data to collect more detailed information. However, capturing trace data for all UEs within the network would impose a significant processing burden, making it an impractical solution. Therefore, an alternative approach must be considered to enhance evaluation accuracy and effective policy decisions while optimizing network overhead.

The objective of this use case is to enable the SMO/Non-RT RIC to collect sufficient data for accurate evaluation and policy generation while avoiding unnecessary data collection that may impose excessive processing overhead on the network by using Filtered Measurements.

# 6.3.3 Potential solution

The proposed QoE optimization solution aims to enhance evaluation accuracy by enabling the SMO/Non-RT RIC to utilize Filtered Measurements to collect QoE optimization-related data from a specific UE group. In the case of the Near-RT RIC, which is responsible for optimizing traffic steering operations, it is possible to collect finely segmented statistics using the predefined E2SM-KPM, so no further discussion is needed here.

The measurements should be collected and aggregated using filter data such as cell, Slice ID, 5QI, etc., for the purpose of classifying patterns. The filter data may include RSRP, traffic volume, and velocity, and various conditions can be combined for more refined filtering. filter data can be added or modified according to the operator's objectives.

For example, when managing QoE for UEs using the same VR service, it is not feasible to evaluate QoE by monitoring statistics solely based on a specific Slice ID or 5QI, since not all UEs experience the same radio conditions or mobility patterns. QoE can vary significantly depending on factors such as velocity and RSRP, and thus, operators must be able to distinguish and monitor different UE groups accordingly. Otherwise, statistical averaging may obscure the poor QoE experienced by UEs under specific conditions, such as low RSRP.

To address this, operators can define RSRP and velocity as filter data to collect and monitor statistics per UE group. As shown in Table 6.3.3-1, UE groups can be segmented based on RSRP and velocity, and their QoE can be monitored by tracking target data such as latency, throughput, RLF ratio, iBLER, and PRB allocation. Additionally, if necessary, operators can reconfigure policies tailored to a specific UE group to enable QoE optimization.

<table><tr><td rowspan=1 colspan=1>RSRP\Velocity</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=1>Low</td></tr><tr><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=1>UE Group A</td><td rowspan=1 colspan=1>UE Group B</td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=1>UE Group C</td><td rowspan=1 colspan=1>UE Group D</td></tr></table>

![](images/ecb72bf1b4d2cad85c535d20621b48749d5e13d001438c17b59a380483dc3a42.jpg)

> **Image Summary:** (Summary not available)
  
Table 6.3.3-31: Example of UE grouping based on RSRP and velocity   
Figure 6.3.3-1: Grouping of UEs with the same application based on RSRP and velocity

# 6.3.4 Benefits of Filtered Measurements

By using Filtered Measurements, the operator can apply situation-specific filter data to collect appropriate statistics and perform QoE optimization, optimizing network/UE performance. Additionally, by collecting only data that meets specific conditions instead of gathering data from all UEs, unnecessary data collection in SMO/Non-RT RIC can be prevented, and wasteful use of interface bandwidth can be minimized.

# 6.4 Use case #4: MU-MIMO optimization

# 6.4.1 Background information

MU-MIMO is one of the key technologies available for increasing UE and cell capacities using existing time/frequency resources. The use of multiple antennas enables the pointing of beams to multiple UEs with each beam spatially avoiding the interference from the other beams. However, in commercial deployments, some subscribers can be stationary, some can be moving at pedestrian speeds, and others at high speeds. Due to the high sensitivity of traditional MU-MIMO solutions to subscriber mobility, the capacity gains achieved with multiple antennas are limited.

To address this limitation, new beamforming solutions are emerging that support MU-MIMO with less time sensitivity allowing them to be implemented in the Near-RT RIC. These solutions are applicable to both downlink and uplink data channels and to TDD as well as FDD and can provide high user and cell performance for subscribers moving within a wide range of speeds.

Also, to verify the effectiveness of MU-MIMO, the Non-RT/Near-RT RIC could collect and monitor statistics such as RSRP, SINR, DL/UL throughput, and HARQ information from the O-DU via the O1/E2 interface, while training AI/ML models for optimization.

In particular, the required data for MU-MIMO optimization operations is defined in [i.15]. It is also noteworthy that data such as “average DL UE throughput in gNB with associated non-GoB mMIMO mode” requires the introduction of new per-UE reporting mechanism that incorporates the associated non-GoB mMIMO mode index.

# 6.4.2 Motivation

The MU-MIMO optimization use case aims to enable new spatial multiplexing and precoding solutions that have the potential to increase both user and overall cell capacity in a massive MIMO deployment area. This is achieved by selecting appropriate users over time and frequency resources, and for each selection, recommending the applicable precoding coefficients and Modulation and Coding Schemes (MCS) for the most efficient resource usage.

To monitor performance and optimize MU-MIMO, an operator could check cell throughput or UE throughput before and after MU-MIMO is applied. However, since these statistics are averaged across all UEs in the cell, it is difficult to clearly identify the gain attributable to MU-MIMO within the same cell.

To address this, the Near-RT RIC could collect per-UE information related to MU-MIMO from E2 nodes. However, the measurements collected at the Near-RT RIC are not made accessible to the Non-RT RIC. Moreover, while the O1 Performance Assurance MnS is capable of selectively collecting measurements based on subcounters, it currently lacks sub-counters related to MU-MIMO.

The main objective of this use case is to address the above challenges and allow the SMO/Non-RT RIC to collect the necessary and sufficient data for the evaluation and optimization of MU-MIMO.

# 6.4.3 Potential solution

The proposed solution for MU-MIMO optimization aims to address the above challenges by allowing SMO/Non-RT RIC to collect MU-MIMO-related data only from a MU-MIMO UE group. The measurements should be collected and aggregated using filter data, such as MIMO mode (SU/MU-MIMO) and scheduled MU-MIMO UEs, in order to classify MU-MIMO UE Group. To allow SMO/Non-RT RIC to collect data only from target UE groups, filter data could also include identifiers such as a list of Slice IDs.

Target data could include cell performance or UE performance measurements such as PDCP DL/UL throughput, iBLER for the MU-MIMO UEs, MU-MIMO PRB utilization, and MU-MIMO spectral efficiency. Additionally, to monitor channel conditions, it is possible to collect target data such as CQI, RI, and uplink SINR of MU-MIMO UEs. The target data should be collected and consumed by the SMO/Non-RT RIC from the O-DU via the O1 interface through Performance Assurance MnS, similarly to how other traditional PMs are collected from the O-DU.

# 6.4.4 Benefits of Filtered Measurements

By using Filtered Measurements, the operator can apply situation-specific filter data to collect appropriate target data for monitoring and optimizing MU-MIMO schemes. Additionally, by collecting only data that meets specific conditions instead of

gathering data from all UEs, unnecessary data collection in SMO/Non-RT RIC can be prevented, and wasteful use of interface bandwidth can be minimized. As a result, operators can benefit from being able to monitor and optimize the operation of MUMIMO without distortion, while avoiding the collection of unnecessary data.

# 6.5 Use case #5: UE capability based measurements

# 6.5.1 Background information

In a network, there are different types of the UEs which have different UE capabilities.

• Some UEs are CA capable (FDD $+$ TDD CA, TDD $^ +$ TDD CA), while other low-end UEs do not support CA. Similarly, different UE capabilities are possible such as high Tx power UEs, DL/UL MIMO, UL CA, UL 256 QAM, 1T2R vs. 2T4R, etc.

These UEs should be treated differently in scheduling, mobility, layer management, etc. to optimize their performance according to their RAN capabilities. Consider as an example: Layer management for CA vs. non-CA capable UEs (similarly for other UE capabilities like high Tx power as well)

![](images/5a8028f788d18d1f42e4350aea025d136ecec69f0ff74e370e6243bca99f9431.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.5.1-41: Layer management for CA vs. non-CA capable UEs   
Figure 6.5.1-1 shows layer management for CA vs. non-CA capable UEs.

In this example, CA $\mathrm { ( F D D + T D D }$ ) UEs are moved to low-band FDD from mid-band earlier than non-CA UEs, to fully benefit from CA-enabled coverage extension (UL on FDD and DL on TDD). This helps the CA UEs to maintain their performance near the cell edge. Specifically, CA UEs are handed over from TDD band $( 3 . 5 \ : \mathrm { G H z } )$ to low-band FDD band $( 7 0 0 ~ \mathrm { M H z } )$ at higher RSRP values (not waiting till cell-edge), whereas non-CA UEs would continue further being on TDD until the cell edge. This can be achieved by setting the mobility RSRP thresholds (from TDD to FDD) differently for CA and non-CA UEs.

# 6.5.2 Motivation

Currently, the RSRP values in mobility thresholds (A1, A2, A3, A5, etc.) [i.17] are optimized by the network based on field trials of all the UEs. As a result, these thresholds also tend to be set to common values across all UEs. However, ideally, the gNB should have ability to set these mobility thresholds differently depending on UE capabilities and based on the user experiences measured by these UEs at different RSRP levels.

![](images/b6a0b75c1abd333695e78bd91cd806a2b7e1728285fe82b9620e02b8a1fa7f23.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.5.2-51: Treatment of CA and non-CA UEs with and without Filtered Measurements

Figure 6.5.2-1 shows that the network sets the same handover threshold for all the UEs, which is usually biased based on the non-CA UEs because they are greater in numbers. This causes CA capable UEs to hand over too late at the cell edge, even though there is another layer in which carrier aggregation can happen. This results in poor user experience for CA capable UEs. This use case tries to improve CA capable user experience at the cell edge by setting a different HO threshold so that CA capable UEs are handed over sooner compared to non-CA capable UEs. This use case also helps non-CA capable UEs to keep in the cell as far as possible.

This use case can further enhance for other RRM related decisions based on the UE capability.

# 6.5.3 Potential solution

![](images/3b39c34a8f8e2b743b00a3f36ae5890666a7923ac7e07705395cd15dea84c7f7.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.5.3-61: Potential solution for UE capability-based layer management

Figure 6.5.3-1 shows the flow diagram of a potential solution for UE capability-based layer management through setting different handover thresholds based on the UE capability.

First, Non-RT RIC configures RAN NF with the following information:

• Target data: RSRP of serving cell, RSRP of neighboring cells, call drop, DL/UL throughput, etc. • Filter data: UE capability (CA vs. non-CA UEs)

RAN NF periodically collects the RSRP values across different bands along with the corresponding user experience metrics (throughput, call quality, etc.) from only the filtered UEs that meets the target criteria, and feeds target data back to the Non-RT RIC for only those UEs which meet the filtering criteria set beforehand, in this case UE capability.

Non-RT RIC calculates mobility thresholds of the UEs based on these received Filtered Measurements. The mobility thresholds are decided differently per UE capability (e.g., different thresholds for CA and non-CA UEs). Non-RT RIC indicates the corresponding mobility thresholds to RAN NF via policy provisions over O1 interface.

Lastly, as per [i.17], the RAN NF may set different RSRP ranges for different MeasIDs, which consist of MeasObjectNR for setting the band configuration and ReportConfigNR for setting reporting conditions such as thresholds. Since the RSRP ranges

for a2-Threshold, etc., are set to the corresponding UEs via RRC procedure, it is possible to set different RSRP ranges based on UE capabilities by applying different MeasIDs according to the bandCombinationList.

# 6.5.4 Benefits of Filtered Measurements

The proposed solution for setting different thresholds for layer and mobility management based on the UE capabilities will enhance user experience and manage different layers’ resources efficiently across all different UE capabilities. This is enabled by utilizing Filtered Measurements, i.e., measurement data filtered by UE capability. This use case can further be enhanced to set different mobility thresholds based on other UE capabilities, e.g., high-power UEs vs. low-power UEs. This use case enhances UE experience as well as uses the RAN resources efficiently.

# 7 Conclusion and recommendations

This technical report first examines the current state of measurement data filtering in O-RAN, identifies the limitations of the measurement data filtering, and then investigates the following potential enhancements to the O-RAN interface to support Filtered Measurements based on the identified requirements:

• Enhanced PM job via the O1 interface for O-CU/O-DU   
• Enhanced trace job via the O1 interface for O-CU/O-DU   
• Enhanced PM job via the O1 interface for Near-RT RIC exploiting E2SM-KPM

The use cases for Filtered Measurements are also analysed to validate the effectiveness of this feature and to identify requirements.

It is recommended to continue the study in the impacted WGs prior to the normative work. In the subsequent study, solutions for the Filtered Measurements to meet the requirements captured in this TR should be analysed in more detail for the normative work.

# Annex: Change history/Change request (history)

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2024.09.05</td><td rowspan=1 colspan=1>00.00.04</td><td rowspan=1 colspan=1>Initial TR Skeleton Submitted for Approval</td></tr><tr><td rowspan=1 colspan=1>2025.01.07</td><td rowspan=1 colspan=1>00.01</td><td rowspan=1 colspan=1>Definition (clause 5.1), Key Considerations (clause 5.2) and Use Case (clause 6.2.1) areadded. The following CRs are implemented.1) SKT.AO CR-0001 - Filtered-Measurements-Definition2) SKT.AO CR-0002 – Filtered-Measurements-KeyConsiderations3) SKT.AO CR-0003 – Filtered-Measurements-UseCaseMmimo</td></tr><tr><td rowspan=1 colspan=1>2025.02.21</td><td rowspan=1 colspan=1>00.01.01</td><td rowspan=1 colspan=1>Added additional approved CRs (Table of Contents modification, clause 2.2, clause 4,clause 6.1 and clause 6.2). The following CRs are implemented.1) SKT.AO CR-0004 – Filtered-Measurements-Section42) KDDI.AO CR-0006 – Fitered-Measurements-UseCase</td></tr><tr><td rowspan=1 colspan=1>2025.06.05</td><td rowspan=1 colspan=1>00.01.02</td><td rowspan=1 colspan=1>Added additional approved CRs (clause 2.2, clause 5.2, clause 5.3, clause 5.4, clause6.3, clause 6.4 and clause 7). The following CRs are implemented.1) SKT.AO CR-0005 – Filtered-Measurements-UseCase2) SKT.AO CR-0006 – Filtered-Measurements-Requirements2) KDDI.AO CR-0007 – Filtered-Measurements-PotentialSolutions4) KDDI.AO CR-0008 - Filtered-Measurements-PotentialSolution35) KDDI.AO CR-0009 – Filtered-Measurements-Conclusion&amp;Recommendations</td></tr><tr><td rowspan=1 colspan=1>2025.06.06</td><td rowspan=1 colspan=1>00.01.03</td><td rowspan=1 colspan=1>Editorial changes</td></tr><tr><td rowspan=1 colspan=1>2025.06.16</td><td rowspan=1 colspan=1>00.01.04</td><td rowspan=1 colspan=1>Added additional approved CRs (clause 1, clause 3, clause 4, clause 5) and editorialchanges. The following CR is implemented.1) SKT.AO CR-0007 – Filtered-Measurements-Minor text refinements</td></tr><tr><td rowspan=1 colspan=1>2025.06.26</td><td rowspan=1 colspan=1>00.01.05</td><td rowspan=1 colspan=1>Added an additional approved CR (clause 6.5) and editorial changes. The following CR isimplemented.1) JIO.AO CR-0001 – UE-Capability-Based-Measurements-Usecase</td></tr><tr><td rowspan=1 colspan=1>2025.07.21</td><td rowspan=1 colspan=1>00.01.06</td><td rowspan=1 colspan=1>Minor editorial corrections: space missing between words, different level of indentationbetween bullet, etc</td></tr><tr><td rowspan=1 colspan=1>2025.07.22</td><td rowspan=1 colspan=1>01.00.00</td><td rowspan=1 colspan=1>Published as Final version 01.00</td></tr></table>