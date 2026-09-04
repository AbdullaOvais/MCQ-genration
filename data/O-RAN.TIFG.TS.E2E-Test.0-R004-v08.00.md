<table><tr><td rowspan=1 colspan=1>O-RANＮCE</td><td rowspan=1 colspan=1>O-RANＮCE E2E-Test.0-R004-v08.00</td></tr><tr><td rowspan=1 colspan=2>Technical Specification</td></tr><tr><td rowspan=1 colspan=2>O-RAN Test and Integration Focus GroupEnd-to-end Test Specification</td></tr></table>

<table><tr><td rowspan=3 colspan=5>Copyright © 2025 by the O-RAN ALLIANCE e.V.The copying or incorporation into any other work of part or al of the material available in this specificationin any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that youmay print or download extracts of the material of this specification for your personal use, or copy thematerial of this specification for the purpose of sending to individual third parties for their informationprovided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the[third party that these conditions apply to them and that they must comply with them.O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, GermanyRegister of Associations, Bonn VR 11238, VAT ID DE321720189</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>eriala</td></tr></table>

# Contents

Foreword.......... ............................................................................................................... 4   
Modal verbs terminology..... ...... 4   
1 Scope................. ................................................................................................................................... 5   
2 References................................................................................................................................................. 5   
2.1 Normative references......   
2.2 Informative references......................................................................................................................................... 6   
3 Definition of terms, symbols and abbreviations ....................................................................................... 7   
3.1 Terms..... 7   
3.2 Symbols.......... ............................................................................................. 8   
3.3 Abbreviations..................................................................................................................................................... 8   
4 Testing methodology and configuration................................................................................................... 9   
4.0 Testing methodology introduction.......................................................................................................................9   
4.1 System under test........ ....................................................................................... .......10   
4.2 Test and measurement equipment and tools........ .............................................................................................. 11   
4.3 Test report......................... ..................................................................................................... 13   
4.4 Data traffic..................................................................................................................................................... 14   
4.5 Mobility classes................................................................................................................................................. 16   
4.6 Radio conditions................................................................................................................................................ 16   
4.7 Inter-cell interference........ ............................................................................................................... ......17   
4.8 Spectral efficiency............ ................................................................................................................................. 18   
5 Functional tests... ............................................................................. ... 18   
5.0 Functional tests introduction....... .................................................................................................... 18   
5.1 LTE/5G NSA attach and detach of single UE....................................................................................................19   
5.2 LTE/5G NSA attach and detach of multiple UEs.............................................................................................. 21   
5.3 5G SA registration and deregistration of single UE..... ............................................................. ...... 24   
5.4 Intra-O-DU mobility.......... ............................................................................................. 25   
5.5 Inter-O-DU mobility............. ......................................................................................................................... 28   
5.6 Inter-O-CU mobility......... ................................................... 30   
5.7 Registration and deregistration to a single network slice.................................................................................. 33   
5.8 Registration and deregistration to multiple network slices............................................................................... 35   
5.9 Idle Mode Intra-O-DU mobility...... ......................................................................................... 38   
5.10 Idle mode Inter-O-DU mobility..... ............................................................... ......40   
5.11 Idle mode Inter-O-CU mobility.......... ................................................................................ 43   
5.12 5G/4G Inter-System Mobility - 5GS to EPS handover..................................................................................... 45   
5.13 5G/4G Inter-System Mobility - EPS to 5GS handover..................................................................................... 47   
6 Performance tests................... ......................................................................................................... 48   
6.0 Performance tests introduction.......................................................................................................................... 48   
6.1 Expected throughput calculation... ......................................................................................... ...... 49   
6.2 Downlink peak throughput.... ................................................................................................ 52   
6.3 Uplink peak throughput........... ......................................................................................................... 55   
6.4 Downlink throughput in different radio conditions........................................................................................... 57   
6.5 Uplink throughput in different radio conditions................................................................................................ 59   
6.6 Bidirectional throughput in different radio conditions...................................................................................... 61   
6.7 Downlink coverage throughput (link budget)..... ................. ..... 64   
6.8 Uplink coverage throughput (link budget)........................................................................................................ 66   
6.9 Downlink aggregated cell throughput (cell capacity)........................................................................................68   
6.10 Uplink aggregated cell throughput (cell capacity)...... .......................................................... ......72   
6.11 Impact of fronthaul latency on downlink peak throughput............................................................................... 74   
6.12 Impact of fronthaul latency on uplink peak throughput...... ......... 78   
6.13 Impact of midhaul latency on downlink peak throughput... ... 80   
6.14 Impact of midhaul latency on uplink peak throughput...................................................................................... 83   
7 Services tests.... ............................................................. ..... 85   
7.0 Services tests introduction.... ................................................................................................................. ..... 85   
7.1 Data services tests..............................................................................................................................................85   
7.2 Video streaming tests..... ........................................................................................... ......92   
7.3 Voice Services – Voice over LTE (VoLTE) tests....................................................................................... .......106   
7.4 Voice Service – EPS Fallback tests... ....112   
7.5 Voice Service – Voice over NR (VoNR) tests.................................................................................................. 117   
7.6 Video Service – Video over LTE (ViLTE) tests...............................................................................................128   
7.7 Video Service – EPS Fallback.... ................................................................................... .... 135   
7.8 Video Service – Video over NR... ............................................................................................................139   
7.9 URLLC.... ................................................................................................................... 150   
7.10 mMTC...... ........................................................................................................................................... 155   
8 Load and stress tests...... ............................................................................................ 157   
8.0 Load and stress tests introduction....................................................................................................................157   
8.1 Simultaneous RRC_CONNECTED UEs... .................................................................... ..... 158   
8.2 UE State Transition Rate Testing.............................................................................................................. .......160   
8.3 Traffic Load Testing .......... ....................................................................................................................... 162   
8.4 Traffic Model Testing....... ....................................................................................................................... 164   
8.5 Long hours stability Testing....... ..................................................................................................................... 168   
8.6 Multi-cell Testing..... .................................................................................. .........169   
8.7 Emergency call... ................................................................................. .... 171   
8.8 ETWS (Earthquake and Tsunami Warning System)........................................................................................172   
8.9 MPS call.... .............................................................................. 173   
9 RIC-enabled end-to-end use case test.. ..... 175   
9.0 RIC-enabled end-to-end use case test introduction......................................................................................... 175   
9.1 Test Setup and Methodology...... ........................................................................ 176   
9.2 Traffic steering with connected mode mobility control... ......................................................176   
9.3 Network Energy Saving with Carrier and Cell switch off/on using Non-RT RIC.......................................... 185   
10 Profile-based Performance Tests... ...191   
10.1 Introduction..... .................................................................................................................. 191   
10.2 Test Configuration Profile.. ......................................................................................................... ...... 192   
10.3 Measurements, KPIs and Logs........................................................................................................................ 196   
10.4 Test Cases........ ........................................................................................................ 198   
Annex A (normative): Template of test report.. ............................................... .... 201   
Annex (informative): Change history/Change request (history)... ... 204

# Foreword

This Technical Specification (TS) has been produced by TIFG of the O-RAN Alliance. The content of the present document is subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } \mathbf { X } = 0 \displaystyle 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# 1 Scope

The present document specifies the methodology, procedures, configurations, and pass/fail criteria (when applicable) for end-to-end testing of an O-RAN system. It is focused on validating the end-to-end system functionality, performance, and key features of the O-RAN system as a black box. It is based on the principles outlined in the end-to-end system test framework document [11].

# 2 References

# 2.1 Normative references

References are either specific (identified by date of publication and/or edition number or version number) or nonspecific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are necessary for the application of the present document.

1. Void

2. 3GPP TR 36.104, “Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) radio transmission and reception”

3. NGMN Alliance, “Definition of the testing framework for the NGMN 5G pre-commercial networks trials”, White paper July 2019, version 3.0. Available: http://www.ngmn.org

4. NGM Alliance, “NGMN 5G pre-commercial networks trials - major conclusions”, White paper, December 2019, version 1.0. Available: http://www.ngmn.org

5. 3GPP TR 38.913: “Study on new radio access technology Radio interface protocol aspects”, March 2017.

6. IETF RFC7323, “TCP Extensions for High Performance”, September 2014

7. 3GPP TS 38.215, “Physical layer measurements”, September 2020

8. 3GPP TS 36.133, “Requirements for support of radio resource management”

9. 3GPP TS 38.133, “Requirements for support of radio resource management”

10. O-RAN ALLIANCE, “O-RAN Architecture Description v11.0”, February 2024

11. O-RAN ALLIANCE, “O-RAN End-to-End System Testing Framework Specification 1.0”, July 2020

12. O-RAN ALLIANCE, “O-RAN Fronthaul Interoperability Test Specification (IOT) 2.0”, April 2020

13. ITU-R M.2410-0, “Minimum requirements related to technical performance for IMT-2020 radio interface(s)”, November 2017.

14. 3GPP TR 36.814, “Further advancements for E-UTRA physical layer aspects”, March 2017

15. 3GPP TS 38.306, "User Equipment (UE) radio access capabilities", December 2020

16. O-RAN ALLIANCE, “O-RAN Fronthaul Control, User and Synchronization Plane Specification v5.0”, November 2020

17. 3GPP TS 38.300, “NR and NG-RAN Overall Description; Stage $2 ^ { \mathfrak { s } }$ , December 2020

18. 3GPP TS 38.101-1, “User Equipment (UE) radio transmission and reception; Part 1: Range 1 Standalone”, December 2020

19. 3GPP TS 38.101-2, “User Equipment (UE) radio transmission and reception; Part 2: Range 2 Standalone”, December 2020

20. 3GPP TS 38.211, “Physical channels and modulation”, December 2020

21. 3GPP TS 38.213, “Physical layer procedures for control”, December 2020

22. 3GPP TS 38.214, “Physical layer procedures for data”, December 2020

23. 3GPP TR 38.308, “Physical Layer Aspects”, September 2017

24. 3GPP TSG RAN WG1 Meeting #92 R1-1801352, “Discussion on NR UE peak data rate”, March 2018

25. 3GPP TS 36.211, “Physical channels and modulation”, September 2020

26. 3GPP TR 38.801, “Radio access architecture and interfaces”, March 2017

27. 3GPP TS 33.511: “Security Assurance Specification (SCAS) for the next generation Node B (gNodeB) network product class” (Release 16), September 2020

28. 3GPP TS 23.502, “Procedures for the 5G System; Stage- $\cdot 2 ^ { \mathbf { \gamma } \mathbf { \mathrm { , } } \mathbf { \gamma } }$ , December 2020

29. 3GPP TS 23.401 “General Packet Radio Service (GPRS)enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access”

30. 3GPP TS 37.340 “Overall description; Stage-2”

31. 3GPP TS 38.401 “5G; NG-RAN; Architecture description

32. 3GPP TS 38.473 “5G; NG-RAN; F1 Application Protocol (F1AP)

33. 3GPP TS 37.470 “W1 interface General aspects and principles”, July 2020

34. NGM Alliance, “Vertical URLLC Use Cases and Requirements”, February 2020, version 2.5.4. Available: http://www.ngmn.org

35. 3GPP TS 28.552: “Management and orchestration; 5G performance measurements”, December 2020

36. O-RAN ALLIANCE, “O-RAN Working Group 1 Use Cases Detailed Specification v13.00,” February 2024

37. O-RAN ALLIANCE, “O-RAN Working Group 2 Non-RT RIC & A1 Interface: Use Cases and Requirements v05.00,” November 2021

38. O-RAN ALLIANCE, “O-RAN Working Group 3 Use Cases and Requirements v01.00”, July 2021

39. 3GPP TS 23.501: “System architecture for the 5G System (5GS)”, December 2020

40. 3GPP TS 38.306: “User Equipment (UE) radio access capabilities”, December 2021

41. 3GPP TS 23.502: “Procedures for the 5G System (5GS)”, December 2023

43. Void

44. 3GPP TS 28.554, “Management and orchestration; 5G end to end Key Performance Indicators (KPI)”, June 2023

45. ETSI TS 103 786, “Environmental Engineering (EE); Measurement method for energy efficiency of wireless access network equipment; Dynamic energy performance measurement method of 5G Base Station (BS)“

46. O-RAN ALLIANCE, “O-RAN Working Group 1 Network Energy Saving Use Cases”, Technical Report v02.00, June 2023

47. 3GPP TS 38.300: “NR; NR and NG-RAN Overall Description; Stage $2 ^ { \mathfrak { s } }$ , December 2023

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or nonspecific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

3GPP TR 21.905: “Vocabulary for 3GPP Specifications”.

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms [given in [i.1] and the following] apply:

ne Control Plane: refers specifically to real-time control between O-DU and O-RU, and should not be confused with the UE’s control plane

Near-RT RIC Near-Real-Time RAN Intelligent Controller: an O-RAN Network Function (NF) comprised of the Near-RT RIC platform and Near-RT RIC Applications (xApps) [10].

Non-RT RIC Non-Real-Time RAN Intelligent Controller: a functionality within SMO comprised of the Non-RT RIC Framework and the Non-RT RIC Applications (rApps) that manages the content carried across the A1 interface [10].

Non-Stand-Alone network mode that supports operation of SgNB attached to MeNB

O-CU-CP O-RAN Central Unit – Control Plane: a logical node hosting the RRC and the control plane part of the PDCP protocol [10].

O-CU-UP O-RAN Central Unit – Control Plane: a logical node hosting the user plane part of the PDCP protocol and the SDAP protocol.

O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split [10]..

O-RU

O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction) [10].

PTP

Precision Time Protocol (PTP) is a protocol for distributing precise time and frequency over packet networks. PTP is defined in the IEEE Standard 1588.

Physical Broadcast Channel applies for LTE and NR air interface

Physical Downlink Control Channel applies for LTE and NR air interface

Stand-Alone network mode that supports operation of SUT attached to a 5G Core Network

SCS

# S-Plane

SSB

Synchronization Plane: Data flow for synchronization and timing information between   
nodes   
Synchronization Signal Block, in 5G PBCH and synchronization signal are packaged as   
a single block   
User Plane: refers to IQ sample data transferred between O-DU and O-RU

# U-Plane

# 3.2 Symbols

Void

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations [given in [i.1] and the following] apply:

<table><tr><td>5GS</td><td>5G System</td></tr><tr><td>CFI</td><td>Control format indicator</td></tr><tr><td>DL</td><td>Downlink: data flows from the core network towards the UE</td></tr><tr><td>DoS</td><td>Denial of service</td></tr><tr><td>DUT</td><td>Device under Test</td></tr><tr><td>E2E</td><td>End-to-End</td></tr><tr><td>eNB</td><td>3GPP Evolved Node B (LTE base station)</td></tr><tr><td>EPS</td><td>Evolved Packet System</td></tr><tr><td>FFS</td><td>For further study</td></tr><tr><td>gNB</td><td>3GPP Next-generation Node B (5G NR base station)</td></tr><tr><td>IMS</td><td>IP Multimedia Subsystem</td></tr><tr><td>IOT</td><td>Interoperability Testing</td></tr><tr><td>IUT</td><td>Interface under Test</td></tr><tr><td>KPI</td><td>Key performance indicator</td></tr><tr><td>MCS</td><td>Modulation and coding scheme</td></tr><tr><td>OTA</td><td>Over the air</td></tr><tr><td>PDSCH</td><td>Physical downlink shared channel</td></tr><tr><td>PRB</td><td>Physical resource block (12 x Resource Elements per PRB)</td></tr><tr><td>PUSCH</td><td>Physical uplink shared channel</td></tr><tr><td>QUIC</td><td>Quick UDP Internet Connections</td></tr><tr><td>SUT</td><td>System under test</td></tr><tr><td>TCP</td><td>Transmission Control Protocol: connection-oriented IP protc</td></tr></table>

TIFG O-RAN Test and Integration Focus Group   
UDP User Datagram Protocol: connectionless IP protocol   
UE User Equipment: terminology for a mobile device/terminal in LTE and NR   
UL Uplink: data flows from the UE towards the core network   
VoLTE Voice over LTE   
VoNR Voice over NR   
ViLTE Video over LTE

# 4. Testing methodology and configuration

# 4.0. Testing methodology introduction

This clause describes the common testing methods and configurations which shall be used in the subsequent clauses. To ensure fair and comparable test results among various test campaigns, consistent test setups should be utilized. The test conditions should reflect the realistic operational environment as much as possible to ensure meaningful and as close to real-world results as possible. The present document harmonizes the test conditions, methodologies, and procedures; but the test configuration (parameters) of DUT/SUT is not specified in this document. However, it is required to record the complete test configuration used in the test report to enable the test to be reproduced if needed, and for the test results to potentially be used for other purposes, e.g. benchmarking or comparison.

There are several design areas in RAN, where the vendors can differentiate such as RF performance (e.g. receiver sensitivity, PA design), radio link adaptation algorithms (e.g. radio channel estimation, MCS selection, MIMO mode selection, transmission mode selection, UL power control), scheduling and overhead management (e.g. number of control channels). These different approaches result in competitive advantages leading to differences in end-to-end performance which can be assessed with the tests defined in this document. Hence, it is not possible to set pass/fail criteria for all the tests, but the pass/fail criteria are set whenever possible, e.g. in the functional tests in Clause 5. The expected performance values are also indicated for reference network configurations.

Unless otherwise stated in this document, the tests are suitable for both laboratory as well as field environments. All laboratory tests should be conducted over a cable, or in case of OTA tests, inside a shielded box/room, to ensure repeatability. In the laboratory, radio signal strength (i.e. attenuation) on the 5G NR path and/or 4G LTE path can be modified by using variable attenuators. The end-user device, if used, should be placed inside a shielded box to avoid interference from external signals. The laboratory environment should allow for stable and repeatable testing conditions, and it is more suitable for benchmarking. On the other hand, the field environment allows for the evaluation of complex scenarios with realistic radio channel variations and behavior of the network (e.g. inter-cell interference and handovers). Field tests should be performed over the air (OTA). In the field, radio signal strength should be modified by placing the UE in different positions inside the cell.

Unless otherwise stated in this document, the same operating system (e.g. Windows 10) with default settings and configuration should be utilized for both ends (i.e. the host applications at end-user device (test UE) and application (traffic) server) in order to ensure a consistent test environment.

nless otherwise stated in this document, the tests are applicable to both TDD and FDD.

nless otherwise stated in this document, the following network architectures [26] depicted in Figure 41 elow should be addressed and supported:

• �G LTE ‒ Option �   
• �G NR standalone (�G SA) - Option �   
• �G NR non-standalone (�G NSA) - Option � / Option �a / Option �x

![](images/7f1b1a17f2cd186bd3e8b101581ff8900c02ffaf323e027c6b01cd8b4ce2ba53.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4 SEQ Figure \\* ARABIC \s 1 1 : The network architectures supported in this document - red dashed lines indicate control plane while blue solid lines indicate user plane.

# 4.1. System under test

# 4.1.0 System under test overview

The whole O-RAN system is the System under Test (SUT) and can be viewed as an integrated black box in the context of E2E testing [11], i.e. the internal functionality and architecture of SUT is out of scope. All involved O-RAN functions and interfaces shall properly interoperate together, and an end-to-end communication link shall be established between the end-user device and the application server or another end-user device. The testing of interoperability and conformance of the internal functions of the SUT is out of scope for this document. The SUT shall be in service mode and run in their normal operation state. The E2E KPIs are defined across the whole end-to-end communication link between the end-user device and the application (traffic) server or another end-user device – see Figure 42.

# Figure 4 SEQ Figure \\* ARABIC \s 1 2: The O-RAN system as System under Test (SUT) and E2E KPIs

The end-to-end communication link includes O-RAN as well as non-O-RAN (e.g. core, end-user device) components which could negatively affect the end-to-end performance, e.g. limited capability of the test UEs and/or the application servers to generate/receive enough data traffic, or a bottleneck in the transport network. All these unwanted contributions should be avoided or at least minimized in order to measure unbiased KPIs. In addition, there may be a performance difference between different vendors and chipsets depending on their level of maturity. Commercial (production grade) devices (e.g. test UE) should be used whenever possible, ensuring the tests are sufficiently documented, stable and repeatable.

Furthermore, the 4G/5G core or core emulator may influence the test results, particularly throughput, registration and deregistration latency, and service scale. Therefore, the choice of an 4G/5G Core (real or emulated) should be taken consciously. For this reason, the 4G/5G core shall be documented in the test setup. Ideally, this core should be reference tested prior to executing any E2E tests, to ensure that the test results represent RAN performance instead of exposing core performance limitations.

All O-RAN components [10] (such as O-CU-CP and O-CU-UP, O-DU, O-RU) and interfaces [10] (such as Open Fronthaul, X2) included in the System under Test should have been tested against their respective conformance and interoperability O-RAN specifications if they are available. For multi-cell and handover scenarios, the SUT can contain more O-RUs, O-DUs, O-CU-CPs and O-CU-UPs.

# 4.1. Load and Stress Interfaces to SUT

A key priority of load and stress testing is to exercise the performance of the SUT near or exceeding full capacity. The capacity of the O-DU and O-CU within the SUT may be such that applying all traffic necessary to reach full capacity may require many O-RUs which may not always be feasible. Figure 43 defines additional traffic insertion points where traffic may be applied directly at the Open Fronthaul or F1 Interfaces to the SUT in order to provide additional background UE stack traffic along with application of test traffic at the Uu interface to O-RU(s) in the SUT. This should allow for adequate stress on the complete SUT for execution of the E2E test scenarios.

Figure 4 SEQ Figure $\backslash ^ { * }$ ARABIC \s 1 3: Interfaces for applying incremental traffic to System Under Test for Load and Stress scenarios

4.2. Test and measurement equipment and tools

All the tests shall be performed in a non-intrusive manner; that is, in a manner in which the SUT is not required to support any functionality or mode of operation beyond that required for normal operation in a production network. The SUT is not expected to be used as test tools when deployed in a production network, and therefore it should not be used as test tools during end-to-end testing.

All the measurement equipment and tools used in the tests shall be properly calibrated and configured in advance in order to minimize the influence of the test equipment on the measurements results. The parameters (e.g. attenuation) of cables, attenuators, splitters, combiners, etc. shall be also measured in advance and compensated for in the final measurement results.

Table 4 SEQ Table $\backslash \ast$ ARABIC \s 1 1 Test and measurement equipment and tools   

<table><tr><td colspan="1" rowspan="1">Test tool</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">Real UE and/orUE emulator</td><td colspan="1" rowspan="1">The UE (Real UE or UE emulator) is used to establish stateful end-to-endconnection and to generate or receive data traffic.The real UE used in this context as a test tool is typically a UE which is designedfor commercial or testing applications with certain test and diagnostic functionsenabled for test and measurement purposes. Such test and diagnostic functionsshould not affect the performance.The real UE requires a SIM card (real or emulated) which is pre-provisioned withsubscriber profiles. A UE emulator or multiple real UEs can be used in multi-UEtest scenarios requiring multiple UEs sessions. The UE is connected with the SUTeither via RF cables or via an over the air (OTA) connection. In a lab environment,the UE should be placed inside an RF shielded box/room in order to avoidinterference from external signals.The logging tool connected to the UE is used to capture measurements and KPIlogs for test validation and reporting.</td></tr><tr><td colspan="1" rowspan="1">UE + O-RUemulator</td><td colspan="1" rowspan="1">The UE + O-RU emulator is used to establish stateful connections and to generateor receive data traffic directly at the Open fronthaul connection to an O-DU withinthe O-RAN SUT.The UE + O-RU emulator is typically designed for testing applications withcertain test and diagnostic functions enabled for test and measurement purposesThe UE + O-RU emulator is used to create background trafic driven by multiplestateful UE stacks for purposes of increasing the load on the O-DU in addition tothe E2E traffic applied at the Uu interface to the SUT</td></tr><tr><td colspan="1" rowspan="1">UE + O-DUemulator</td><td colspan="1" rowspan="1">The UE + O-DU emulator is used to establish stateful connections with, and togenerate or receive data and signaling traffic directly at the F1 connection to theO-CU within the O-RAN SUT.The UE + O-DU emulator is typically designed for testing applications withcertain test and diagnostic functions enabled for test and measurement purposes.The UE + O-DU emulator is used to create background traffic driven by multipleUE connections for purposes of increasing the load on the O-CU in addition to theE2E traffic applied at the Uu interface to the SUT</td></tr><tr><td colspan="1" rowspan="1">4G/5G Core orCore emulator</td><td colspan="1" rowspan="1">The 4G/5G core or core emulator is used to terminate 4G/5G NAS sessions, andto support core network procedures required for RAN (SUT) testing: 4G/5G coreor core emulator must support end-to-end connection and data transfer betweenApplication server and Real UE/UE emulator.</td></tr><tr><td colspan="1" rowspan="1">IMS Core orIMS Coreemulator</td><td colspan="1" rowspan="1">The IMs Core or IMS core emulator is used to support voice and video callingservices like VoLTE, ViLTE, VoNR, Video over NR and EPS Fallback usingprotocols like SIP and RTP. IMS core or IMS core emulator should interface with[the 4G/5G core to setup dedicated bearers/QoS Flows to support voice and videocalling services.</td></tr><tr><td colspan="1" rowspan="1">Application(traffic) server</td><td colspan="1" rowspan="1">The application (trafic) server is used as an endpoint for generation and/ortermination of various data traffic streams to/from Real UE(s)/UE emulator. Theapplication server should be capable to generate data traffic for the services undertest.The application server should be placed as close as possible to the core/coreemulator, and connected to the core/core emulator via a transport link with</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">sufficient capacity.</td></tr><tr><td colspan="1" rowspan="1">Protocolanalyzer</td><td colspan="1" rowspan="1">The protocol analyzer is used for test results verification, and for troubleshootingand root cause analysis of failed tests. Note that if IPsec encryption is applied atthe network interface, then it would not be possible to use the protocol analyzerwithout decryption of IPsec.</td></tr><tr><td colspan="1" rowspan="1">Networkimpairmentemulator</td><td colspan="1" rowspan="1">The network impairment emulator is used for tests which require insertion ofimpairment (packet delay and/or jitter) at the network interface (e.g. Openfronthaul).</td></tr><tr><td colspan="1" rowspan="1">RF attenuatorsand/or Fadinggenerator</td><td colspan="1" rowspan="1">RF attenuators are used for tests which require radio signal attenuation. Fadinggenerators can be used to simulate specific radio channel conditions (e.g. Urban,Rural, High Speed Train).</td></tr><tr><td colspan="1" rowspan="1">RF shieldedbox/room</td><td colspan="1" rowspan="1">The RF shielded box/room is used for over the air (OTA) connectivity between theUE and SUT in the lab environment. The RF shielded box/room should supportreliable MIMO testing, if MIMO is required.</td></tr><tr><td colspan="1" rowspan="1">Packetgeneration tool /DoS emulator</td><td colspan="1" rowspan="1">The packet generation tool / Denial of Service (DoS) emulator is used for DoStraffic generation of security tests. The tool must support crafting network trafficon network layers from 2 to 7, which conform to network protocols such as:Ethernet, IP, UDP, TCP, PTP, eCPRI, TLS, HTTP/HTTPS. The tool is intended tobe deployable in various network segments (communication planes) according tothe testing needs.</td></tr><tr><td colspan="1" rowspan="1">Packet capturetool</td><td colspan="1" rowspan="1">The packet capture tool is used to capture samples of data traffic for validation,analysis, and troubleshooting. In the case of security test cases it can be used tocapture samples of legitimate traffic, which then can be used as templates forfuzzing attacks. The tool must support capturing network traffic on network layersfrom 2 to 7, which conform to network protocols such as: Ethernet, IP, UDP, TCP,PTP, eCPRI, TLS, QUIC, HTTP/HTTPS. The tool is intended to be deployable invarious network segments (communication planes) according to the testing needs.</td></tr><tr><td colspan="1" rowspan="1">Network tap</td><td colspan="1" rowspan="1">A network tap is a hardware or software device which provides access andvisibility to the data flowing across a computer network.</td></tr><tr><td colspan="1" rowspan="1">Fuzzing tool</td><td colspan="1" rowspan="1">The protocol fuzzing tool is used for unexpected protocol input generation ofsecurity tests. The tool must support mutating and replaying of captured networktraffic on network layers from 2 to 7, which conform to network protocols such as:Ethernet, IP, UDP, TCP, PTP, eCPRI, TLS, HTTP/HTTPS. The tool is intended tobe deployable in various network segments (communication planes) according tothe testing needs.</td></tr><tr><td colspan="1" rowspan="1">Vulnerabilityscanning tool</td><td colspan="1" rowspan="1">The vulnerability scanning tool is used for blind exploitation of well-knownyulnerabilities during security tests. The tool should rely on cyclically updateddatabase of known vulnerabilities based on Common Vulnerabilities andExposures (CVE) and should support scanning network services running on TCP/IP stack of protocols. The tool is intended to be deployable in various networksegments (communication planes) according to the testing needs.</td></tr><tr><td colspan="1" rowspan="1">NFVbenchmarkingand resourceexhaustion tool</td><td colspan="1" rowspan="1">The Network Function Virtualization (NFV) tool is used for O-Cloud systemperformance measurement and resource exhaustion type of DoS attack generation.This tool should be able to be deployed on any types of O-Cloud environment(public or private) with testing VNF(s) and/or CNF(s) support.</td></tr><tr><td colspan="1" rowspan="1">Energy meter</td><td colspan="1" rowspan="1">The energy meter measures the cumulative energy consumption over a period oftime. The unit of measurement is Watt-hours or Joules.</td></tr></table>

# 4.3. Test report

Tests should be described in the test report with sufficient detail to allow the tests to be reproducible by different parties and to enable benchmarking and comparison. The unified reporting of test results is important for benchmarking and comparison of results. The following common minimum set of configuration parameters and information about the test environment shall be reported in each test report [3]:

NOTE: 3GPP specifications for 4G LTE are part of the 36.xxx series, while 3GPP specifications for 5G NR are part of the 38.xxx series.

Deployment scenario:

Deployment architecture (e.g. indoor hotspot, macro/micro, dense urban, urban, rural)   
Number of cells and their layout (incl. a mapping between O-CUs, O-DUs, O-RUs and cells)

Cell configuration parameters of each cell (if the parameters are not common to all cells):

• Downlink/Uplink Carrier frequency (MHz)

• Downlink/Uplink EARFCN [��, Clause �.�.�] or NR-ARFCN [��, Clause �.�.�.�] (Aggregated) Channel bandwidth (MHz) and transmission bandwidth configuration (i.e.number of Physical Resource Blocks (PRBs)) [��, Clause �.�] [��, Clause �.�]

• Duplex mode (e.g. FDD, TDD)

• TDD configuration parameters for �G LTE, if applied • Uplink-downlink configuration [��, Table �.�-�] • Special subframe configuration [��, Table �.�-�] • TDD configuration parameters for �G [��, Clause ��.�], if applied

• Pattern � and Pattern �

■ slot configuration period (parameter dl-UL-TransmissionPeriodicity) (msec)   
number of consecutive slots with only dowlink symbols at the start of the period (parameter nrofDownlinkSlots) number of consecutive downlink symbols within the slot which follows the downlink slots (parameter nrofDownlinkSymbols)   
■ number of consecutive slots with only uplink symbols at the end of the period (parameter nrofUplinkSlots)   
■ number of consecutive uplink symbols within the slot which preceds the uplink slots (parameter nrofUplinkSymbols)

• Subcarrier spacing (SCS) (��, ��, ��, ��� or ��� kHz) [��, Table �.�-�] • Cyclic prefix (CP) (normal or extended) [��, Table �.�-�] • SSB periodicity (ms) [��, Clause �.�]

SU/DUT and UE configuration parameters:

• Number of supported MIMO layers at both SUT and UE sides   
• Antenna configuration (number of Tx/Rx antenna elements, e.g. �T�R) at both SUT and UE sides   
• Transmit power at antenna connectors at SUT (dBm)   
• Antenna gains at SUT (dBi)

Information about test environment:

List of utilized test and measurement equipment and tools (incl. logging tools, test UE(s)) including the type and version. The Operating Systems (incl. the version) used at end-user device and application server should be noted as well. If TCP   
performance has been measured, the setting of TCP configuration parameters should be also noted.   
Information about the SUTs (e.g. O-RU, O-DU, O-CU-CP, O-CU-UP) including the type, parameters, configuration, SW and HW versions, Interface profiles (e.g. Open   
fronthaul IOT profile [��]).

The template for the test report for general use in reporting E2E test results can be found in Annex A. Any E2E testing for the purpose of seeking an O-RAN E2E Badge must comply with the processes, procedures and report templates defined in [42]. Photos and figures should also be taken as part of the test report in order to illustrate the test environment. Additional parameters and counters are specified in the description of each test in the subsequent clauses.

# 4.4. Data traffic

This clause describes the full buffer and finite buffer traffic models that are utilized in some of the tests in this document.

The full buffer traffic model is characterized by a constant number of users in the cell during the test, wherein the buffers of the users' data flows always have unlimited amount of data to transmit. The model is preferred due to its simplicity.

In the finite buffer traffic model, a user is assigned a finite payload to transmit or receive when it arrives. The user arrival process of this model captures the fact that the users in the network are not simultaneously active at the same time, but they rather become active when they start a data session that require the download/upload of data. Examples of models are FTP traffic model 1/2/3 [14] largely used in 3GPP simulations.

Data throughput can be measured at different protocol layers. Each network protocol layer adds extra overhead (header information), thereby reducing the data throughput available to the layer above. The highest throughput is provided at the physical layer including user data and the overhead from higher protocol layers. The data throughput at the RLC (Radio Link Control) layer is independent from radiospecific overhead and therefore well-suited for comparison with other access technologies. The application layer throughput is the net throughput seen by user applications operating on top of either UDP, TCP or QUIC – for example, the typical FTP overhead is around $3 \mathrm { - } 5 \%$ , typical HTTP overhead is around $3 0 \%$ compared to RLC throughput. Unless otherwise stated in this document, the reported throughput (user data rate) shall consider all the overhead (control channels, reference signals).

UDP (User Datagram Protocol), TCP (Transmission Control Protocol) and QUIC (Quick UDP Internet Connections) are typical transport layer protocols utilized in the tests.

UDP is a simple, connection-less transport layer protocol which does not guarantee error-checking and recovery. UDP throughput is more suitable for benchmarking as it is not affected by the system configuration parameters. UDP is also faster, lighter (less overhead) and more efficient than TCP.

TCP is reliable, connection-oriented transport layer protocol which includes error-checking and recovery, and guarantees data delivery with preserved order of data packets. The performance of a TCP connection can be impacted by various factors such as end-to-end latency, number of retransmissions, packet loss, and TCP configuration parameters such as window size, window scale, timestamps, etc. [6]. The default values of TCP configuration parameters can also vary in different Operation Systems (incl. different versions of the same OS) which are used at the end-user device (test UE) and application (traffic) server. It is recommended to use the same OS (incl. the version) with default setting at the end-user device (test UE) and application server. Since the settings and behavior of TCP connections cannot be easily unified and normalized, the measurement of TCP performance is recommended only as an illustrative indicator, and UDP performance should be used for the benchmarking and assessment of system performance.

QUIC (Quick UDP Internet Connections) is a general-purpose transport layer protocol built on top of UDP to support the next generation of application layer protocols. QUIC provides features like connection establishment, congestion control, stream multiplexing and forward error correction to provide a secure and reliable connection-oriented protocol over UDP. QUIC is being used as the standard transport mechanism for HTTP/3.

In addition, the following application layer protocols are utilized in the tests.

Hypertext Transfer Protocol (HTTP) is the application layer protocol used in the internet. HTTP is a stateless protocol which follows the request-response model between client and the server. The client places a request for a resource to the server, and the server responds back to the client with requested resource and/or the appropriate response code. HTTP’s support for headers between the client-server makes this protocol simple, extensible, and powerful.

Session Initiation Protocol (SIP) is an application layer signalling protocol for real-time sessions like IP telephony. This is a text-based protocol which allows negotiation between two end points to initiate a session, maintain the session and terminate the session. SIP is the default signalling protocol used in the telecom network for VoLTE, ViLTE, VoNR and Video over NR.

Real-time Transport Protocol (RTP) is an application layer protocol used to transmit real-time data such as audio and video over IP network. RTP is the default data plane protocol used in the telecom network for services like VoLTE, ViLTE, VoNR and Video over NR. RTP does not guarantee Quality of Service but works in conjunction with Real Time Control Protocol (RTCP) to detect and convey packet loss and jitter information.

File Transfer Protocol (FTP) is an application layer protocol to transfer files on a computer network. FTP follows a client-server model where the client can upload the file to the server, or download he file from the server. FTP protocol uses two separate connections between the client and the server – one for control and the other one for data or transfer of file. FTP along with multiple variants of the protocol have become the de-facto standards to transfer file on the internet.

# 4.5. Mobility classes

The following classes of mobility shall be used for the applicable tests [13]:

• Stationary: � kph • Pedestrian: � kph to �� kph (typical value � kph) Vehicular: �� kph to ��� kph (typical value �� kph) • High speed vehicular: ��� kph to ��� kph (typical value ��� kph)

High speed vehicular speeds close to ��� kph are mainly used for high speed trains.

# 4.6. Radio conditions

The radio signal quality is described by the radio parameters such as RSRP and SINR. These radio parameters are defined differently in LTE and 5G NR.

LTE RSRP (Reference Signal Received Power) [�] is defined as the linear average over the power contributions (in [W]) of the resource elements that carry cell-specific reference signals (CRS) within the considered measurement frequency bandwidth. The RSRP is reported from UE back to SUT. The reporting range of RSRP is defined from -���dBm to -��dBm [�].

LTE SINR (Signal to Noise and Interference Ratio) has not been formerly defined in the �GPP specification. The UE does not send the results back to SUT. The SINR is measured and used only in UE. Specific implementations may vary, and it is up to the manufacturer to decide, how to implement this measurement. This is making difficult to compare results of different devices. In [�], SINR is defined as the linear average over the power contribution (in [W]) of the resource elements carrying cellspecific reference signals divided by the linear average of the noise and interference power contribution (in [W]) over the resource elements carrying cell-specific reference signals within the same frequency bandwidth.

�G SS-RSRP (Synchronization Signal based Reference Signal Received Power) [�] is defined as the linear average over the power contributions (in [W]) of the resource elements that carry secondary synchronization (SS) signals. SS-RSRP is the equivalent of the RSRP parameter used in LTE systems. The reporting range of SSRSRP is defined from -���dBm to -��dBm [�].

�G SS-SINR [�] is defined as the linear average over the power contribution (in [W]) of the resource elements carrying secondary synchronisation signals divided by the linear average of the noise and interference power contribution (in [W]) over the resource elements carrying secondary synchronisation signals within the same frequency bandwidth. The SS-SINR is reported from UE back to SUT. The reporting range of SS-SINR is defined from -��dB to ��dB.

It is worth to note that in 5G, the Channel State Information Reference Signal (CSI-RS) can also be used for RSRP and SINR measurements. Due to different transmit powers of CSI-RS and SS, CSI-RS-based SINR and RSRP measurement values are usually greater than SS-based SINR and RSRP. The minimum coupling loss (MCL) [2] between O-RU (antenna) and UE shall be ensured:

Macro cell deployment scenario (wide area BS): ${ \mathsf { M C L } } = 7 0 \mathsf { d B }$ corresponding to minimal O-RU (antenna) to UE distance along the ground equal to around $3 5 { \mathsf { m } }$ Small cell (micro cell) deployment scenario (medium range BS): $M C L = 5 3 d B$ corresponding to minimal O-RU (antenna) to UE distance along the ground equal to around � m Pico cell deployment scenario (local area BS): $M C L = 4 5 d B$ corresponding to minimal O-RU (antenna) to UE distance along the ground equal to around $2 \mathsf { m }$

The radio parameters (RSRP, SINR) should be measured across the entire range covering scenarios from cell centre to cell edge. Based on the test results, the RSRP and SINR distribution statistics can be calculated and described as a cumulative distribution function (CDF) curve. According to the CDF curve, the four types of radio conditions can be defined as: excellent $( 9 5 \% - 1 0 0 \%$ ), good $( 8 0 \% - 9 0 \%$ ), fair

$( 4 0 \% - 6 0 \% )$ ) and poor $( 5 \% - 1 5 \% )$ [3]. Table 42 shows the RSRP and SINR thresholds for various radio conditions.Table 42 RSRP and SINR thresholds for various radio conditions Note that the RSRP values should primarily be used for UL assessments, and the SINR values for DL assessment.

Table 4 SEQ Table \\* ARABIC \s 1 2 RSRP and SINR thresholds for various radio conditions   

<table><tr><td rowspan=1 colspan=1>Radioconditions</td><td rowspan=1 colspan=1>RSRP (dBm)SS-RSRP (dBm)</td><td rowspan=1 colspan=1>DL SINR (dB)DL SS-SINR (dB)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Excellent(cell cente)</td><td rowspan=1 colspan=1>&gt; -75</td><td rowspan=1 colspan=1>&gt; 25</td><td rowspan=1 colspan=1>Utilization of the highestpossible MCS, transport blocksize and MIMO rankPeak performancemeasurements Negligible interference fromneighbor cells</td></tr><tr><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>-75 to -90(typical value = -85)</td><td rowspan=1 colspan=1>15 to 20(typical value = 17)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>-90 to -105(typical value = -95)</td><td rowspan=1 colspan=1>5 to 10(typical value = 7)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Poorll ede)</td><td rowspan=1 colspan=1>&lt;-105(typical value =-110)</td><td rowspan=1 colspan=1>&lt;5(typical value = 3)</td><td rowspan=1 colspan=1>Minimum performancemeasurementsStrong interference fromneighbor cells</td></tr></table>

There are many different factors that influence signal strength and quality during the field testing; these factors include, but are not limited, to the following:

• Proximity to the cellular tower (antenna)   
• Load in neighbor cells   
Surrounding physical barriers (mountains, buildings, etc.)   
• Weather conditions

# 4.7. Inter-cell interference

Some tests in this document are conducted either in a single cell scenario without any inter-cell interference, or in a multi-cell scenario where the serving cell is surrounded by neighboring cells generating traffic load (interference on the serving cell) in the downlink or uplink directions. Generating a realistic traffic load is important for meaningful results. As the number of real UEs are always a limiting factor, artificial (dummy) traffic load and interference generation may be used. In the single cell scenario, the serving cell is isolated, and all the surrounding neighbor cells are turned off (neither control nor data channels are used).

In the multi-cell scenario, all the neighbor cells are turned on. The following load setups shall be used:

Load $0 \%$ - all the surrounding neighbor cells are turned on without any data traffic and end-user device attached. Inter-cell interference is generated only on control channels (broadcasting, synchronization channels) without any inter-cell interference on data channels.

Load $3 0 \%$ - all the surrounding neighbor cells are turned on with data traffic. Intercell interference is generated both on control and data channels. The level of interference on data channel is controlled by the amount of data traffic. The interference level of $30 \%$ in downlink means that $3 0 \%$ of downlink PRBs are randomly occupied with a dummy traffic. In uplink, this interference level corresponds to �dB rise of IoT (Interference over Thermal) noise at the receiver side (i.e. SUT’s antenna(s)). The received interference noise from the UEs of neighbor cells uplink transmission should lead to �dB rise of receiver’s noise power [�].

Load $5 0 \%$ - all the surrounding neighbor cells are turned on with data traffic. Intercell interference is generated both on control and data channels. The level of interference on data channel is controlled by the amount of data traffic. The interference level of $5 0 \%$ in downlink means that $5 0 \%$ of downlink PRBs are randomly occupied with a dummy traffic. In uplink, this interference level corresponds to �dB rise of IoT (Interference over Thermal) noise at the receiver side (i.e. SUT’s antenna(s)).

Load $70 \%$ - all the surrounding neighbor cells are turned on with data traffic. Intercell interference is generated both on control and data channels. The level of interference on data channel is controlled by the amount of data traffic. The interference level of $70 \%$ in downlink means that $70 \%$ of downlink PRBs are randomly occupied with a dummy traffic. In uplink, this interference level corresponds to �dB rise of IoT (Interference over Thermal) noise at the receiver side (i.e. SUT’s antenna(s)).

Load $100 \%$ - fully loaded multi-cell scenario generating the highest possible inter-cell interference. All the surrounding neighbor cells are turned on with data traffic. Intercell interference is generated both on control and data channels. The level of interference on data channel is controlled by the amount of data traffic. The interference level of $100 \%$ in downlink means that $100 \%$ of downlink PRBs are occupied with a dummy traffic. In uplink, this interference level corresponds to �dB rise of IoT (Interference over Thermal) noise at the receiver side (i.e. SUT’s antenna(s)).

# 4.8. Spectral efficiency

The spectral (or spectrum) efficiency (SE) is an important criterion for fair performance assessment and benchmarking of different systems when various transmission bandwidths, duplex modes (FDD/TDD) and TDD DL/UL configurations are normalized.

The spectral efficiency is calculated by dividing the data throughput by the aggregated channel bandwidth (incl. guard bands) in DL or UL assuming single user and FDD duplex mode. The corresponding link frame structure is fully $( 1 0 0 \% )$ utilized in frequency and time domains.

In case of TDD where the same spectrum is used at different times for the uplink and downlink, the spectral efficiency is in addition multiplied by the fraction of resources (slots and symbols, not including switching gap) allocated to the particular link direction within $1 0 \mathrm { m s }$ radio frame.

# 5. Functional tests

# 4.9. Functional tests introduction

This clause describes the tests evaluating and assessing the functionality of the radio access network from a network end-to-end perspective. The focus of the testing is on the end-user functionality based on 3GPP and O-RAN specifications. Pass-fail criteria are defined for the tests wherever possible.

he general test methodologies and configurations are mentioned in Clause 4.

Unless otherwise stated in the clause, the tests are suitable and can be conducted in both laboratory as well as field environments, with pros and cons of both environments as described in Clause 4.

The following end-to-end functional tests are defined in this clause as an extension of the NGMN testing framework [3]:

Table 5 SEQ Table \\* ARABIC \s 1 1: E2E Functionality Test Case Summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functional group</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>TestID</td><td rowspan=1 colspan=1>E2E Functionality Assessment</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5.1</td><td rowspan=1 colspan=1>LTE/5G NSA Attach and detach of single UE</td><td rowspan=1 colspan=1>Accessibility</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>5.2</td><td rowspan=1 colspan=1>LTE/5G NSA Attach and detach of multiple UEs</td><td rowspan=1 colspan=1>Accessibility</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>5.3</td><td rowspan=1 colspan=1>5G SA Registration and deregistration of single UE</td><td rowspan=1 colspan=1>Accessibility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.4</td><td rowspan=1 colspan=1>Intra O-DU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>Inter O-DU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.6</td><td rowspan=1 colspan=1>Inter O-CU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.7</td><td rowspan=1 colspan=1>5G SA registration and deregistration to Singlenetwork slices</td><td rowspan=1 colspan=1>Accessibility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.8</td><td rowspan=1 colspan=1>5G SA registration and deregistration to multiplenetwork slices</td><td rowspan=1 colspan=1>Accessibility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.9</td><td rowspan=1 colspan=1>Idle Mode Intra- O-DU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.10</td><td rowspan=1 colspan=1>Idle Mode Inter- O-DU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.11</td><td rowspan=1 colspan=1>Idle Mode Inter- O-CU mobility</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.12</td><td rowspan=1 colspan=1>5G/4G Inter-System mobility - 5GS to EPS handover</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>5.13</td><td rowspan=1 colspan=1>5G/4G Inter-System mobility - EPS to 5GS handover</td><td rowspan=1 colspan=1>Mobility</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

The test description, setup and procedures are detailed in the following clauses for each test case.

# 4.10. LTE/5G NSA attach and detach of single UE

4.2. Test description and applicability

The purpose of this test is to validate E2E O-RAN C-plane functionality with a single UE. These tests are valid for either LTE or 5G NSA. In this test scenario, the successful attach and detach procedure shall be validated by the “Power ON” and “Power OFF” of a single UE, as described in the following specifications:

1. LTE Attach as per �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach 2. LTE Detach as per �GPP TS ��.��� [��], Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN

3. �G NSA Attach as per �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach and �GPP TS ��.��� [��] Clause ��.�.� EN-DC (Secondary Node Addition)

4. �G NSA Detach as per �GPP ��.���, Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN and �GPP TS ��.��� [��] Clause ��.�.� EN-DC (Secondary Node Release) [29]

The test procedure shall be performed in excellent radio conditions for 10 iterations. Attach success rate, detach success rate, and attach latency shall be measured and captured.

# 4.3. Test setup and configuration

The test setup is a single cell scenario (i.e. isolated cell without any inter-cell interference – see Clause 4.7) with a stationary UE (real or emulated) placed under excellent radio conditions as defined in Clause 4.6, using LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA) as the metric. Within the cell there shall be only one active UE. The test is suitable for lab as well as field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment should be setup to achieve excellent radio conditions (LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA) as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside an RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of the cell close to the radiated SUT’s antenna(s), where excellent radio conditions (LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA) as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.6) should not be exceeded.

Please refer to Figure 61 for the E2E test setups for LTE and 5G NSA.

# 4.4. Test procedure

The test steps below are applicable for either LTE or 5G NSA:

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. The UE (real or emulated UE) is placed under excellent radio conditions (Cell centre close to radiated SUT’s Antenna) as defined by LTE RSRP (for LTE) or �G SS-RSRP (for �G NSA) in Clause �.�.   
3. The End-to-end setup shall be operational for LTE or �G NSA as applicable for the test scenario, and there should not be any connectivity issues.   
4. Start the logs to capture the call flow and signalling messages   
5. “Power ON” the UE to attach to the LTE or �G NSA cell. Wait for a successful attach.   
6. “Power OFF” the connected UE to detach from the network. Wait for a successful detach.   
7. Stop and save the test logs. The logs shall be captured and kept for test result reference and measurements   
8. Repeat steps � to �, for �� times and record the KPIs mentioned in Clause �.�.�.

# 4.5. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for performance assessment.

Radio parameters such as RSRP, RSRQ KPIs mentioned in Table �� and Table 53

Validate the successful procedures from the collected logs. Expected success rate for Attach/Detach and Secondary Node Addition/Release KPI is $1 0 0 \%$ . The attach-detach procedure shall pass 10 consecutive times to mark the test case as passing. The gap analysis shall be provided for the measured and the expected target KPIs.

• LTE Attach-Detach test case validation and KPI measurements • Validate successful attach �� times with LTE cell (Refer to �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach). In the UE logs or applications installed on UE, check that UE is attached to correct cell (example PCI, Global eNB ID, ARFCN as per test configuration) • Measure the attach success rate by validating attach request and attach complete for each iteration. Record the attach success rate in Table �� • Measure the attach latency by calculating the time between attach request to attach complete. Capture the latency for each iteration and sort the latency value observed for each iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are �� in this case) and Maximum latency value observed in Table 53 • Validate successful detach/attach with LTE cell (Refer to �GPP TS ��.��� [��], Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN). Signalling connection release shall be validated from message flow (UE context release and RRC connection release messages). Measure the detach success rate by validating detach request and detach accept for each iteration. Record the detach success rate in Table ��

• �G NSA Attach-Detach test case validations and KPI measurements

• Validate successful multiple attaches with �G NSA cell (�GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach and �GPP TS ��.��� [��] Clause ��.�.� EN-DC for Secondary Node Addition)). In the UE logs or applications installed on UE, check that UE is attached to correct cell (example PCI, Global eNB ID/Global gNB, ARFCN/NR-ARFCN as per test configuration for LTE /�G cells )   
• Measure the attach success rate by validating attach request and attach complete for each iteration. Also measure the secondary node addition success rate by validating the SgNB addition request and SgNB reconfiguration complete as per flow �GPP TS ��.��� [��] Clause ��.�.� EN-DC for each iteration. Record the attach success rate and secondary   
node addition success rate in Table ��   
• Validate successful detach attach (LTE Detach and �G Secondary Node release) with �G NSA cell (Refer to �GPP TS ��.��� [��], Clause �.�.�.�.�   
UE-initiated Detach procedure for E-UTRAN and �GPP TS ��.��� [��] Clause ��.�.� EN-DC for Secondary Node Release)). Signalling connection release shall be validated the from message flow (UE context release and RRC connection release messages). �G secondary node shall also get released successfully. Measure the detach success rate by

validating detach request and detach accept for each iteration. Record the detach success rate in Table ��

Table 5 SEQ Table \\* ARABIC \s 1 2 KPI to be captured for single UE attach-detach test case   

<table><tr><td rowspan=1 colspan=2>LTE KPI</td><td rowspan=1 colspan=3>5G NSA KPI</td></tr><tr><td rowspan=1 colspan=1>AttachSuccess Rate</td><td rowspan=1 colspan=1>DetachSuccess Rate</td><td rowspan=1 colspan=1>AttachSuccessRate</td><td rowspan=1 colspan=1>DetachSuccessRate</td><td rowspan=1 colspan=1>SgNBadditionSuccess rate</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# Table 5 SEQ Table \\* ARABIC \s 1 3 Latency KPI for attach

<table><tr><td rowspan=1 colspan=3>LTE Attach Time (millisecond)</td></tr><tr><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>Average</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.11. LTE/5G NSA attach and detach of multiple UEs

4.6. Test description and applicability

The purpose of this test is to validate E2E O-RAN C-plane functionality with multiple UEs. These tests are valid for either LTE or 5G NSA. In this test scenario, the successful attach and detach procedure shall be validated by the “Power ON” and “Power OFF” of multiple (at least 2) UEs, as described in the following specifications:

1. LTE Attach as per �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach   
2. LTE Detach as per �GPP TS ��.��� [��], Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN   
3. �G NSA Attach as per �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach and �GPP TS ��.��� [��] Clause ��.�.� EN-DC (Secondary Node Addition)   
4. �G NSA Detach as per �GPP ��.���, Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN and �GPP TS ��.��� [��] Clause ��.�.� EN-DC (Secondary Node Release) [29]

The test procedure shall be performed in excellent radio conditions for 10 iterations. Attach success rate, detach success rate, and attach latency shall be measured and captured.

# 4.7. Test setup and configuration

The network setup is a single cell scenario (i.e. isolated cell without any inter-cell interference – see Clause 4.7) with multiple stationary UEs (real or emulated) placed under excellent radio conditions as defined in Clause 4.6, using LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA) as the metric. The test is suitable for lab as well as field environments. The minimum number of UEs which are used shall be two (2).

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report, including the chosen number of UEs.

Laboratory setup: The radio conditions experienced by the UEs can be modified using variable attenuators/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment should be setup to achieve excellent radio conditions (LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA) as defined in Clause 4.6) for the UEs, but the minimum coupling loss (see Clause 4.6) should not be exceeded. The UEs should be placed inside an RF shielded box or RF shielded room if the UEs are not connected via cable.

Field setup: The multiple UEs are placed in the centre of the cell close to the radiated SUT’s antenna(s), where excellent radio conditions (LTE RSRP and 5G SS-RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.6) should not be exceeded.

Please refer to Figure 61 for the E2E test setups for LTE and 5G NSA.

4.8. Test procedure

The test steps below are applicable for either LTE or 5G NSA:

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. The multiple UEs (real or emulated) are placed under excellent radio conditions (Cell centre close to radiated SUT’s Antenna) as defined by LTE RSRP (for LTE) or �G SSRSRP (for �G NSA) in Clause �.�.   
3. The End-to-end setup shall be operational for LTE or �G NSA as applicable for the test scenario, and there shall not be any connectivity issues.   
4. Start the logs to capture the call flow and signalling messages.   
5. “Power ON” the multiple connected UEs to attach to the LTE or �G NSA cell. Wait for the successful attach of all UEs.   
6. “Power OFF” the multiple UEs to detach from the network. Wait for the successful detach of all UEs   
7. Stop and save the test logs. The logs shall be captured and kept for test result reference and measurements   
8. Repeat steps � to �, for a total of �� times and record the KPIs mentioned in Clause 5.2.4

# 4.9. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for performance assessment.

Radio parameters such as RSRP, RSRQ KPIs mentioned in Table 54 and Table ��

Validate the successful procedures for each UE from the collected logs. Expected success rate for Attach/ Detach and Secondary Node Addition/Release KPI is $1 0 0 \%$ . The attach-detach procedure shall pass 10 consecutive times for all UEs to mark the test case as passing. The gap analysis shall be provided for the measured and the expected target KPIs.

LTE Attach-Detach test case validations and KPI measurements • Validate successful attach of each UE �� times with LTE cell (Refer to �GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach). In the UE logs or applications installed on UE, check that UE is attached to correct cell (example PCI, Global eNB ID, ARFCN as per test configuration) • Measure the attach success rate by validating attach request and attach complete for each iteration. Record the attach success rate in Table 54 for each UE. • Measure the attach latency by calculating the time between Attach Request to attach complete. Capture the latency for each iteration and sort the latency value observed for each iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are �� in this case) and Maximum latency value observed in Table 55 for each UE • Validate successful detach attach with LTE cell (Refer to �GPP TS ��.��� [��], Clause �.�.�.�.� UE-initiated Detach procedure for E-UTRAN).

Signalling connection release shall be validated from message flow (UE context release and RRC connection release messages). Measure the detach success rate by validating detach request and detach accept for each iteration. Record the detach success rate in Table 54

• �G NSA Attach-Detach test cases validations and KPI measurements • Validate successful multiple UE attach with �G NSA cell (�GPP TS ��.��� [��], Clause �.�.�.� E-UTRAN Initial Attach and �GPP TS ��.��� [��] Clause ��.�.� EN-DC for Secondary Node Addition)). In the UE logs or applications installed on UE, check that UE is attached to correct cell (example PCI, Global eNB ID/Global gNB, ARFCN/NR-ARFCN as per test configuration for LTE /�G cells )

• Measure the attach success rate by validating attach request and attach complete for each iteration. Also measure the secondary node addition success rate by validating the SgNB addition request and SgNB reconfiguration complete as per flow �GPP ��.��� Clause ��.�.� EN-DC for each iteration. Record the attach success rate and secondary node addition success rate in Table 54 for each UE

• Validate successful detach attach (LTE Detach and �G Secondary Node release) with �G NSA cell (Refer to �GPP TS ��.��� [��] Clause, �.�.�.�.� UE-initiated Detach procedure for E-UTRAN and �GPP TS ��.��� [��] Clause ��.�.� EN-DC for Secondary Node Release)). Signalling connection release shall be validated from the message flow (UE context release and RRC connection release messages). �G secondary node shall also get released successfully. Measure the detach success rate by validating detach request and detach accept for each iteration. Record the detach success rate in Table 54 for each UE

Table 5 SEQ Table \\* ARABIC \s 1 4 KPI to be captured for multi-UE attach-detach test case   

<table><tr><td rowspan=1 colspan=2>LTE KPI</td><td rowspan=1 colspan=3>5G NSA KPI</td></tr><tr><td rowspan=1 colspan=1>AttachSuccess Rate</td><td rowspan=1 colspan=1>DetachSuccess Rate</td><td rowspan=1 colspan=1>AttachSuccessRate</td><td rowspan=1 colspan=1>DetachSuccessRate</td><td rowspan=1 colspan=1>SgNBadditionSuccess rate</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Table 5 SEQ Table \\* ARABIC \s 1 5 Latency KPI for multi-UE attach

<table><tr><td rowspan=1 colspan=3>LTE Attach Time (millisecond)</td></tr><tr><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>Average</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

4.12. 5G SA registration and deregistration of single UE

4.10. Test description and applicability

The purpose of the test is to verify the full registration and deregistration procedure with a single UE. The test also verifies the PDU session establishment and release procedures.

The test focuses on the procedure of ‘Initial registration’ as defined in 3GPP TS 23.502 [28] Clause 4.2.2.2.2.

The test focuses on the procedure of ‘UE-initiated deregistration’ as defined in 3GPP TS 23.502 [28] Clause 4.2.2.3.2.

This test also validates PDU session establishment and release procedures.

The test validates the 3GPP standard registration/deregistration procedure and the latency of the procedure. Bi-directional data transmission shall be observed before the deregistration procedure to verify the stability of the network slice.

# 4.11. Test setup and configuration

The test setup is a single cell scenario (i.e. isolated cell without any inter-cell interference – see Clause 4.7) with a stationary UE (real or emulated) placed under excellent radio conditions as defined in Clause 4.6, using SS-RSRP as the metric. Within the cell there shall be only one active UE. The application server should be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with enough capacity so as not to limit the expected data throughput. The UE, RAN, and 5G Core shall support the network slicing, at least for one Single Network Slice Selection Assistance Information (S-NSSAI). The test is suitable for lab as well as field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment should be setup to achieve excellent radio conditions (using SS-RSRP as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside an RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (SS-RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.6) should not be exceeded.

Please refer to Figure 61 for E2E test setup for 5G SA.

# 4.12. Test procedure

Below are the test procedure steps

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. Power on the UE and the UE shall send REGISTRATION REQUEST message. UE shall successfully register to the �G SA network.   
3. Full-buffer UDP bi-directional data transmission (see Clause �.�) between the application server and UE is initiated.   
4. The registration procedure messages shall be captured, and the latency of the registration procedure shall be measured and recorded in Table ��. The duration of the test shall be at least � minutes when the throughput is stable. The PDU session establishment procedure messages shall also be captured and verified.   
5. Power off the UE and UE shall send DEREGISTRATION REQUEST message. UE shall successfully deregister from the �G SA network.   
6. The deregistration procedure messages shall be captured, and the latency of deregistration procedure shall be measured and recorded in Table ��. The PDU session release procedure messages shall also be captured and verified.   
7. Repeat steps � to �, for a total of �� times and record the KPIs mentioned in Table ��.

# 4.13. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment.

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second)   
Latency KPI mentioned in Table ��

Validate from collected logs registration (as per 3GPP TS 23.502 [28] Clause 4.2.2.2.2) and deregistration (as per 3GPP TS 23.502 [28] Clause 4.2.2.3.2) procedures and also validate ‘UE Requested PDU Session Establishment for Non-roaming and Roaming with Local Breakout case’ as defined in 3GPP TS 23.502 [28] Clause 4.3.2.2.1, and the procedure of ‘PDU Session Release for UE or network requested PDU Session Release for Non-Roaming and Roaming with Local Breakout case’ as defined in 3GPP TS 23.502 [28] Clause 4.3.4.2. The procedure shall pass 10 consecutive times to mark the test case as passing. The gap analysis shall be provided for the measured and the expected target KPIs.

The Registration Time latency is measured by calculating the time between Registration Request to Registration Complete; The Deregistration Time latency is measured by calculating the time between Deregistration Request to Signaling Connection Release. Capture the latency for each iteration and sort the latency value observed for each iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are 10 in this case) and Maximum latency value observed in Table 56.

Table � SEQ Table \\* ARABIC \s � � �G SA registration/deregistration latency KPI record table of single UE   

<table><tr><td rowspan=2 colspan=1>KPI</td><td rowspan=1 colspan=10>Repeat Times</td><td rowspan=1 colspan=3>Calculation</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>Average</td></tr><tr><td rowspan=1 colspan=1>RegistrationTime (singleslice)(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Deregistration Time(single slice)(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.13. Intra-O-DU mobility

# 4.14. Test description and applicability

The purpose of the test is to verify intra O-CU, intra O-DU handover of a UE. The test validates the OCU, O-DU, and O-RU functionality in handling inter-cell mobility when two O-RUs are connected to an O-DU. The test measures the DL / UL throughput variations, handover latency, handover interruption and packet loss during the mobility. Test scenarios are classified into two groups as Standalone (SA) and Non-Standalone (NSA).

Intra O-DU mobility with SA shall follow 3GPP TS 38.401 [29], Clause 8.2.1 and 3GPP TS 38.473 [32], Clause 8.3.4 for the call flow. Intra O-DU mobility with NSA shall follow 3GPP TS 38.401 [29], Clause 8.2.1, 3GPP TS 38.473 [32], Clause 8.3.4 and 3GPP TS 37.340 [30] for the call flow.

# 4.15. Test setup and configuration

In NSA mode, the test setup consists of one 4G cell (MeNB) and two 5G cells (SgNB). Each 5G cell is associated with a single O-DU, connected to a single O-CU, refer to Figure 51 for the test setup topology. The test environment shall have a single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/17d6b3f2cc239ad70ae663778e87c6d5d8722939d17b939ad708d6e581ea394a.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure $\backslash \ast$ ARABIC \s 1 1 Intra O-DU mobility test bed for NSA mode of operation. In SA, the test setup consists of two 5G cells, each one associated with the same O-DU and O-CU connected to a 5G core network (see Figure 52 for the test setup topology). The test environment shall have a single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/eacb81c39b757bcbc9ff692dc09294040cd40dbbd80a490669154e1ba56b4bf3.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 2 Intra O-DU mobility test bed for SA mode of operation. Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of the UE are initially set to excellent using RSRP as the metric. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside and RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing the radio signal strength of the source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (using RSRP as the metric as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.16. Test procedure

Below are the NSA mode steps

1. The �G and �G cell setups are configured following Clause �.�.�.   
2. All the three cells are configured according to the test configuration. The cells are activated and unloaded.   
3. Both �G cells are configured as neighbors to each other, so that the UE can trigger measurement events for handover.   
4. The source (cell �) and target (cell �) �G cells for intra O-DU mobility shall be depicted as in Figure 51.   
5. The test UE is under source �G cell coverage.   
6. Power on the UE and UE shall successfully complete the LTE attach followed by successful SgNB addition to source �G cell.   
7. The full-buffer UDP bi-directional data transmission (see Clause �.�) from the application server is initiated.   
8. The UE shall move from the source �G cell to the target �G cell to trigger a handover. elow are the SA Mode steps   
1. The �G cell setup is configured following Clause �.�.�.   
2. Configure two �G cells within an O-DU according to the test configuration. The cells are activated and unloaded.   
3. Both �G cells are configured as neighbors to each other, so that the UE can trigger measurement events for handover.   
4. The source and target �G cells for intra O-DU mobility shall be depicted as in Figure 52.   
5. The test UE is under source cell coverage.   
6. Power on the UE and UE shall successfully register to source �G cell.   
7. The full-buffer UDP bi-directional data transmission (see Clause �.�) from the application server is initiated.   
8. The UE shall move from source cell to target cell to perform handover.

# 4.17. Test requirements (expected results)

The intra O-DU handover call flow shall be verified for both NSA and SA use cases. Following functionalities shall also be validated:

PDU Session is established when full-buffer bi-directional data transmission is initiated. (Only in SA Mode)   
Handover is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT/Application server side:

• Transmit downlink throughput measured at application server in time (average per second) Received uplink throughput measured at application server in time (average per second) Uplink packet loss percentage during handover. Uplink BLER, MCS, MIMO rank (RI) on PUSCH in time (average per second)

UE side:

Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) Downlink BLER, MCS, MIMO rank (RI) on PDSCH in time (average per second). Received Downlink throughput (L� and L� PDCP layers) in time (average per second). Downlink packet loss percentage during handover Uplink throughput (L� and L� PDCP layers) in time (average per second) Channel utilization, i.e. Number allocated/occupied downlink and uplink RBs in time (per TTI/average per second) and Number of allocated/occupied slots in time.

• KPIs related to Handover failure, Call drop, Handover latency, Handover interruption time.

# 4.14. Inter-O-DU mobility

# 4.18. Test description and applicability

The purpose of the test is to verify intra O-CU, inter O-DU handover of a UE. The test validates the OCU, O-DU functionality in handling Inter O-DU handover. The test measures the DL / UL throughput variations, handover latency, handover interruption and packet loss during the handover procedure. Test scenarios are classified into two groups as SA (Standalone) and NSA (Non-Standalone).

Inter O-DU mobility with SA shall follow 3GPP TS 38.401 [31], Clause 8.2.1 and Inter O-DU mobility with NSA shall follow 3GPP TS 38.401[31], Clause 8.2.2 for the call flow.

3GPP 38.401 v15.7.0 has introduced a new CR 0104, which has modified the initial part of call flow for Clause 8.2.2. The ORAN system supporting 3GPP specification later than v15.7.0 shall follow Clause 8.2.2 of 3GPP TS 38.401 v15.7.0 or later to verify the inter O-DU handover.

# 4.19. Test setup and configuration

In Non-Standalone Mode, the test setup consists of one 4G Cell (MeNB) and two 5G cells (SgNB). Each 5G Cell is associated with different O-DUs, connected to the same O-CU. The test environment shall have a single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/3744ebda82feae216a0f40f07f81772ad56e7e43d4c4d03715337781ca498d1f.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 3 Inter O-DU mobility test bed for NSA mode of operation.

In standalone Mode, the test setup consists of two 5G cells, each one associated with a different O-DU, connected to the same O-CU. The test environment shall have a single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/6b27caef0c7834ebe635f1ee9458093abb8e3dabd9f1807b0248a00c41b29a20.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 4 Inter O-DU mobility test bed for SA mode of operation

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing radio signal strength of source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.20. Test procedure

In Non-Standalone Mode

1. The 4G and 5G cell setups are configured following Clause 5.5.2.   
2. All the three cells are configured according to the test configuration. The cells are activated and unloaded.   
3. Both 5G cells are configured neighbors to each other, so that UE can trigger measurement events for handover.   
4. The test UE is under source O-DU cell coverage.   
5. Power on the UE and the UE shall successfully complete the LTE attach followed by successful SgNB addition to source O-DU.   
6. The full-buffer UDP data transmission (see Clause 4.4) from the application server is initiated.   
7. The UE shall move from source O-DU to target O-DU to perform handover.

In Standalone Mode

1. The 5G cell setup is configured following Clause 5.5.2.   
2. All the 5G cells are configured according to the test configuration. The cells are activated and unloaded.   
3. Both 5G cells are configured neighbors to each other, so that UE can trigger measurement events for handover.   
4. The test UE is under source O-DU cell coverage.   
5. Power on the UE and the UE shall successfully register to source O-DU cell.

6. The full-buffer UDP data transmission (see Clause 4.4) from the application server is initiated.   
7. The UE shall move from source O-DU to target O-DU to perform handover.

# 4.21. Test requirements (expected results)

The inter O-DU handover call flow shall be verified for both NSA and SA use cases. Following functionalities shall also be validated:

PDU Session is established when full-buffer bi-directional data transmission is initiated. (Only in SA Mode)   
Handover is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT/Application server side:

• Transmit downlink throughput measured at application server in time (average per second) Received uplink throughput measured at application server in time (average per second) Uplink packet loss percentage during handover. Uplink BLER, MCS, MIMO rank (RI) on PUSCH in time (average per second)

UE side:

Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) Downlink BLER, MCS, MIMO rank (RI) on PDSCH in time (average per second). Received Downlink throughput (L� and L� PDCP layers) in time (average per second). Downlink packet loss percentage during handover   
Uplink throughput (L� and L� PDCP layers) in time (average per second)   
Channel utilization, i.e. Number allocated/occupied downlink and uplink RBs in time (per TTI/average per second) and Number of allocated/occupied slots in time. KPIs related to Handover failure, Call drop, Handover latency, Handover interruption time.

# 4.15. Inter-O-CU mobility

# 4.22. Test description and applicability

The purpose of the test is to verify inter O-CU handover of the UE. The test validates the O-CU, O-DU functionality in handling inter O-CU mobility connected to same 5G Core Network (in SA) or Master eNB (in NSA). The test measures the DL / UL throughput variations, handover latency, handover interruption and packet loss during the mobility. Test scenarios are classified into two groups as Standalone (SA) and Non-Standalone (NSA).

Inter O-CU mobility with SA- Xn based Handover call flow shall follow 3GPP TS 38.401 [31], Clause 8.9.4 and Clause 8.9.5. Inter O-CU mobility with NSA shall follow 3GPP TS 37.340 [30], Clause 10.5.1 for the call flow.

# 4.23. Test setup and configuration

In non-standalone mode, the test setup consists of a 4G cell (MeNB) and two 5G cells (SgNB), each 5G cell is associated with a different O-DU and O-CU connected to the same 4G core network, refer to Figure 55 for the test setup topology. The test environment shall have single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/be3ac10417daf8e474b7d1e22f1ceadfdcc605e4de84e87bdd8465f3e800f8cd.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure $\backslash ^ { * }$ ARABIC $\backprime \mathbf { s } \mathbf { 1 } \mathbf { 5 }$ Inter O-CU mobility test bed for NSA mode of operation

In standalone mode, the test setup consists of two 5G cells, each one associated with a different O-DU and O-CU connected to same 5G Core network (see Figure 56 for the test setup topology). The test environment shall have a single UE with active data traffic. The application server should be placed as close as possible to the core and connected to the core via a transport link with enough capacity.

![](images/9561ca0010ad22a11e96c7df3b1acd308c2037d1cdeb201e246ba5de4a768d64.jpg)

> **Image Summary:** {"image": "image_data"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 6 Inter O-CU mobility test bed for SA mode of operation.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing radio signal strength of source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.24. Test procedure

In Non-Standalone Mode

1. The 4G and 5G cell setups are configured following Clause 5.6.2.   
2. Configure two 5G cells connected to different O-DU and O-CU according to the test configuration. The cells are activated and unloaded.   
3. 5G cells are configured as neighbors to 4G cell, so that UE can trigger measurement events for mobility.   
4. The source cell (source O-DU and source O-CU) is the cell where UE is initially placed as depicted in Figure 55.   
5. Power on the UE and the UE shall successfully complete the LTE attach followed by successful SgNB addition to source 5G cell.   
6. The full-buffer UDP bi-directional data transmission (see Clause 4.4) from the application server is initiated.   
7. The UE shall move from source 5G cell to target 5G cell.

In Standalone Mode

1. The 5G cell setup is configured following Clause 5.6.2.   
2. Configure two 5G cells connected to different O-DU and O-CU according to the test configuration. The cells are activated and unloaded.   
3. Both 5G cells are configured neighbors to each other, so that UE can trigger measurement events for handover.   
4. The source cell (source O-DU and source O-CU) is the cell where UE is initially placed as depicted in Figure 56.   
5. Power on the UE and UE shall successfully register to source 5G cell.   
6. The full-buffer UDP bi-directional data transmission (see Clause 4.4) from the application server is initiated.   
7. The UE shall move from source cell to target cell to perform handover.

# 4.25. Test requirements (expected results)

The inter O-CU handover call flow shall be verified for NSA use case. Following functionalities shall also be validated:

PDU Session is established when full-buffer bi-directional data transmission is initiated. (Only in SA Mode)   
Handover is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment

UE side:

Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) Downlink BLER, MCS, MIMO rank (RI) on PDSCH in time (average per second). Received Downlink throughput (L� and L� PDCP layers) in time (average per second). Downlink packet loss percentage during handover   
Uplink throughput (L� and L� PDCP layers) in time (average per second)   
Channel utilization, i.e. Number allocated/occupied downlink and uplink RBs in time (per TTI/average per second) and Number of allocated/occupied slots in time. KPIs related to Handover failure, Call drop, Handover latency, Handover interruption time.

SUT/Application server side:

• Transmit downlink throughput measured at application server in time (average per second) Received uplink throughput measured at application server in time (average per second) Uplink packet loss percentage during handover. Uplink BLER, MCS, MIMO rank (RI) on PUSCH in time (average per second)

4.16. Registration and deregistration to a single network slice

4.26. Test description and applicability

The purpose of the test is to verify the full procedure of the registration and deregistration to the single eMBB network slice in the 5G SA network.

The test focuses on the procedure of ‘Initial registration’ as defined in 3GPP 23.502 Clause 4.2.2.2.2, with a single eMBB network slice. The network slice information (i.e., Network Slice Selection Assistance Information, NSSAI) defined in Table 57 shall be verified within the 3GPP standard registration procedure.

The test focuses on the procedure of ‘UE-initiated deregistration’ as defined in 3GPP 23.502 Clause 4.2.2.3.2, with a single eMBB network slice. Even though the network slice information is not included in the deregistration procedure, the mandatory IEs defined in Table 57 shall be verified within the 3GPP standard deregistration procedure.

The granularity of slice awareness is in PDU session level, so this test also verifies the PDU session establishment and release procedures.

The test measures not only the 3GPP standard registration/deregistration procedure but also the latency of the procedure. The bi-directional data transmission shall be involved before the deregistration procedure to verify the stability of the network slice.

# 4.27. Test setup and configuration

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal should be set to achieve the excellent radio conditions (RSRQ as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRQ as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.6) should not be exceeded.

Please refer to Figure 5-2 for E2E test setup for 5G SA.

4.28. Test procedure

Below are the test procedure steps

1. The NR cells shall be configured in the initial conditions defined in Session �.�.�.   
2. Only one eMBB S-NSSAI (i.e., Slice/Service Type $( { \mathsf { S S T } } ) = 0 { \times } 0 1 _ { \ r { \ r { \ r { \ r { \ r { \theta } } } } } }$ ) under the NSSAI shall be configured in UE, RAN, and �G Core.   
3. Power on the UE and UE shall send REGISTRATION REQUEST message. The only one requested S-NSSAI shall be included in the message with the configured value in step �. And UE shall successfully register to the �G SA network.   
4. The full-buffer UDP bi-directional data transmission (see Clause �.�) between UE and the application server is initiated.   
5. The registration procedure messages shall be captured to verify the mandatory IEs defined in Table 57, and the latency of registration procedure shall be measured and recorded in Table ��. The duration of the test should be at least � minutes when the throughput is stable. The PDU session establishment procedure messages shall also be captured and verified.   
6. Power off the UE and UE shall send DEREGISTRATION REQUEST message. And UE shall successfully de-register from the �G SA network.   
7. The deregistration procedure messages shall be captured to verify the mandatory IEs defined in Table 58, and the latency of deregistration procedure shall be measured and recorded in Table ��. The PDU session release procedure messages shall also be captured and verified.

8. Repeat steps � to �, �� times and record the KPI mentioned in Table ��.

# 4.29. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment.

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
Mandatory IEs mentioned in Table 57, and Table 58   
Latency KPI mentioned in Table ��

Validate from collected logs registration (as per 3GPP 23.502 Clause 4.2.2.2.2) and deregistration (as per 3GPP 23.502 Clause 4.2.2.3.2) procedure and also validate ‘UE Requested PDU Session Establishment for Non-roaming and Roaming with Local Breakout case’ as defined in 3GPP 23.502 Clause 4.3.2.2.1, and the procedure of ‘PDU Session Release for UE or network requested PDU Session Release for NonRoaming and Roaming with Local Breakout case’ as defined in 3GPP 23.502 Clause 4.3.4.2. Table 57 defines the verification steps along with validation of mandatory IEs for 5G SA registration procedure in single eMBB network slice.

Table 5 SEQ Table $\backslash ^ { * }$ ARABIC \s 1 7 5G SA Registration verification with mandatory IEs in single eMBB network slice   

<table><tr><td rowspan=1 colspan=1>St.</td><td rowspan=1 colspan=1>Procedure</td><td rowspan=1 colspan=1>MsgFlow</td><td rowspan=1 colspan=1>Expected Output</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>RRCSetupComplete</td><td rowspan=1 colspan=1>UE →SUT</td><td rowspan=1 colspan=1>Verify that UE sends only one S-NSSAI in IE s-nssai-List and SST =&#x27;0x01&#x27; in the S-NSSAI to SUT.</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Registration Request [</td><td rowspan=1 colspan=1>tUE →AMF</td><td rowspan=1 colspan=1>Verify that UE sends only one S-NSSAI in IE Requested NSSAI to 5GAMF, and IE 5GS registration type = &#x27;initial registration&#x27;, SST =&#x27;0x01&#x27; in the S-NSSAI.</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Initial Context SetupRequest</td><td rowspan=1 colspan=1>AMF→SUT</td><td rowspan=1 colspan=1>Verify that 5G AMF sends only one S-NSSAI in IE Allowed NSSAI andS-NSSAI (under parent IE PDU Session Resource Setup Request Item)to SUT, and SST = &#x27;0x01&#x27; in the S-NSSAI.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Registration Accept</td><td rowspan=1 colspan=1>AMF→UE</td><td rowspan=1 colspan=1>Verify that 5G AMF sends only one S-NSSAI in IE Allowed NSSAIand Configured NSSAI to UE, SST = &#x27;Ox01&#x27; in the S-NSSAI and IERejected NSSAI shall not exist.</td></tr></table>

Table 58 defines the verification steps along with validation of mandatory IEs for 5G SA deregistration procedure in single eMBB network slice.

Table 5 SEQ Table $\backslash \ast$ ARABIC \s 1 8 5G SA Deregistration verification with mandatory IEs in single eMBB network slice   

<table><tr><td>St.</td><td>Procedure</td><td>Msg Flow</td><td>Expected Output</td></tr><tr><td>1</td><td>Deregistration Request</td><td>UE →AMF</td><td>Verify that UE sends IE Deregistration type = 'Switch Off ' to 5G AMF.</td></tr></table>

Table 59 defines the KPI record table of registration/ registration testing in single eMBB network slice.

Table � SEQ Table \\* ARABIC \s � � Single eMBB Network Slice KPI record table

<table><tr><td rowspan=2 colspan=1>KPI</td><td rowspan=1 colspan=10>Repeat Times</td><td rowspan=1 colspan=3>Calculation</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>Average</td></tr><tr><td rowspan=1 colspan=1>RegistrationTime (singleslice)(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Deregistration Time(single slice)(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

4.17. Registration and deregistration to multiple network slices

4.30. Test description and applicability

The purpose of the test is to verify the full procedure of the registration and deregistration to multiple network slices (i.e., eMBB, URRLC, MIoT, V2X) in the 5G SA network.

The test focuses on the procedure of ‘Initial registration’ as defined in 3GPP 23.502 Clause 4.2.2.2.2, with multiple network slices. The network slice information (i.e., Network Slice Selection Assistance Information, NSSAI) defined in Table 510 shall be verified within the 3GPP standard registration procedure.

The test focuses on the procedure of ‘UE-initiated deregistration’ as defined in 3GPP 23.502 Clause 4.2.2.3.2, with multiple network slices. Even though the network slice information is not included in the deregistration procedure, and also the mandatory IEs defined in Table 511 shall be verified within the 3GPP standard deregistration procedure.

The granularity of slice awareness is in PDU session level, so this test also verifies the PDU session establishment and release procedures.

The test measures not only the 3GPP standard registration/deregistration procedure but also the latency of the procedure. The bi-directional data transmission shall be involved before the deregistration procedure to verify the stability of the network slice.

# 4.31. Test setup and configuration

The network setup is single cell scenario (i.e. isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in the excellent radio conditions as defined in Clause 4.6 – RSRQ should be considered in case of downlink. Within the cell there should be only one active UE. The application server(s) should be placed as close as possible to the core/core emulator and connected to the core/core emulator via transport link with enough capacity not limiting the expected data throughput. The test is suitable for lab as well as field environment. The UE, RAN, and 5G Core shall support the multiple Network Slice Selection Assistance Information (S-NSSAI). At least two network slices of eMBB, URRLC, MIoT, V2X shall be covered for this test. The test is suitable for lab as well as field environment.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal should be set to achieve the excellent radio conditions (RSRQ as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRQ as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.6) should not be exceeded.

Please refer to Figure 5-2 in section 5.4.2, for E2E test setup for 5G SA.

# 4.32. Test procedure

Below are the test procedure steps

1. The NR cells shall be configured in the initial conditions defined in Session �.�.�.   
2. Multiple S-NSSAI (i.e., Slice/Service Type $( \mathsf { S S T } ) = 0 { \times } 0 1 / 0 { \times } 0 2 / 0 { \times } 0 3 / 0 { \times } 0 4 )$ under the NSSAI shall be configured in UE, RAN, and �G Core.   
3. Power on the UE and UE shall send REGISTRATION REQUEST message. The multiple requested S-NSSAI shall be included in the message with the configured value in step �. And UE shall successfully register to the �G SA network.   
4. The full-buffer UDP bi-directional data transmission (see Clause �.�) between UE and the application server is initiated in eMBB network slice if eMBB network slice is covered.   
5. The full-buffer UDP bi-directional data transmission (see Clause �.�) between UE and the application server is initiated in URRLC network slice if URRLC network slice is covered.   
6. The full-buffer UDP bi-directional data transmission (see Clause �.�) between UE and the application server is initiated in mIoT network slice if MIoT network slice is covered.   
7. The full-buffer UDP bi-directional data transmission (see Clause �.�) between UE and the application server is initiated in V�X network slice if V�X network slice is covered.   
8. The registration procedure messages shall be captured to verify the mandatory IEs defined in Table �-��, and the latency of registration procedure shall be measured and recorded in Table ���. The duration of the test should be at least � minutes when the throughput is stable. The PDU session establishment procedure messages shall also be captured and verified for the network slices of eMBB/URRLC/MIoT/ V�X.   
9. Power off the UE and UE shall send DEREGISTRATION REQUEST message. And UE shall successfully de-register from the �G SA network.   
10. The deregistration procedure messages shall be captured to verify the mandatory IEs defined in Table �-��, and the latency of deregistration procedure shall be measured and recorded in Table ���. The PDU session release procedure messages shall also be captured and verified for the network slices of eMBB/URRLC/MIoT/ V�X.   
11. Repeat steps � to ��, �� times and record the KPI mentioned in Table �-��.

# 4.33. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment.

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
Mandatory IEs mentioned in Table 510, and Table 511   
Latency KPI mentioned in Table ���

Validate from collected logs registration (as per 3GPP 23.502 Clause 4.2.2.2.2) and deregistration (as per 3GPP 23.502 Clause 4.2.2.3.2) procedure and also validate ‘UE Requested PDU Session Establishment for Non-roaming and Roaming with Local Breakout case’ as defined in 3GPP 23.502 Clause 4.3.2.2.1 for multiple network slices of eMBB/URRLC/MIoT/ V2X, and the procedure of ‘PDU Session Release for UE or network requested PDU Session Release for Non-Roaming and Roaming with Local Breakout case’ as defined in 3GPP 23.502 Clause 4.3.4.2 for multiple network slices of eMBB/URRLC/MIoT/ V2X.

Table 510 defines the verification steps along with validation of mandatory IEs for 5G SA registration procedure in multiple network slices.

Table 5 SEQ Table $\backslash \ast$ ARABIC \s 1 10: 5G SA Registration verification with mandatory IEs in multiple network slices   

<table><tr><td rowspan=1 colspan=1>St.</td><td rowspan=1 colspan=1>Procedure</td><td rowspan=1 colspan=1>MsgFlow</td><td rowspan=1 colspan=1>Expected Output</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>RRCSetupComplete</td><td rowspan=1 colspan=1>UE →SUT</td><td rowspan=1 colspan=1>Verify that UE sends multiple S-NSSAI in IE s-nssai-List and SST =&#x27;0x01/0x02/0x03/0x04&#x27; in the S-NSSAI to SUT.</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>RegistrationRequest</td><td rowspan=1 colspan=1>UE →AMF</td><td rowspan=1 colspan=1>Verify that UE sends multiple S-NSSAI in IE Requested NSSAI to 5GAMF, and IE 5GS registration type = &#x27;initial registration&#x27;, SST =&quot;0x01/0x02/0x03/0x04&#x27; in the S-NSSAI.</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Initial ContextSetup Request</td><td rowspan=1 colspan=1>AMF→ SUT</td><td rowspan=1 colspan=1>Verify that 5G AMF sends multiple S-NSSAI in IE Allowed NSSAI andS-NSSAI (under parent IE PDU Session Resource Setup Request Item)to SUT, and SST = &#x27;0x01/0x02/0x03/0x04&#x27; in the S-NSSAI.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Registration Accept</td><td rowspan=1 colspan=1>AMF→UE</td><td rowspan=1 colspan=1>Verify that 5G AMF sends multiple S-NSSAI in IE Allowed NSSAI andConfigured NSSAI to UE, SST = 0x01/0x02/0x03/0x04&#x27; in the S-NSSAIand IE Rejected NSSAI shall not exist.</td></tr></table>

Table 511 defines the verification steps along with validation of mandatory IEs for 5G SA deregistration procedure in multiple network slices.

Table 5 SEQ Table $\backslash \ast$ ARABIC \s 1 11: 5G SA Deregistration verification with mandatory IEs in multiple network slices   

<table><tr><td rowspan=1 colspan=1>St.</td><td rowspan=1 colspan=1>Procedure</td><td rowspan=1 colspan=1>Msg Flow</td><td rowspan=1 colspan=1>Expected Output</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>DeregistrationRequest</td><td rowspan=1 colspan=1>UE →AMF</td><td rowspan=1 colspan=1>Verify that UE sends IE Deregistration type = &#x27;Switch Off to5G AMF.</td></tr></table>

Table ��� defines the KPI record table of registration/ registration testing in multiple network slices.

Table � SEQ Table \\* ARABIC \s � �� Multiple Network Slices KPI record table   

<table><tr><td rowspan=2 colspan=1>KPI</td><td rowspan=1 colspan=10>Repeat Times</td><td rowspan=1 colspan=3>Calculation</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>Maximum</td><td rowspan=1 colspan=1>Average</td></tr><tr><td rowspan=1 colspan=1>RegistrationTime(multipleslices))(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Deregistration Time(multipleslices)d)(millisecond)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.18. Idle Mode Intra-O-DU mobility

4.34. Test description and applicability

The purpose of the test is to verify O-CU, idle mode intra O-DU mobility of a UE. The test validates the O-CU, O-DU, O-RU functionality in handling inter cell mobility when two O-RU connected to an ODU. Test scenarios are classified into two groups as Standalone (SA) Intra frequency cell reselection and as Standalone (SA) Inter frequency cell reselection.

Idle mode Intra O-DU mobility shall follow 3GPP 38.133, Clause 4.2.2.3 and Clause 4.2.2.4 for intra frequency and inter frequency cell selection measurement, respectively. And 3GPP 38.304, Clause 5.2.2 for the state transition.

# 4.35. Test setup and configuration

In SA, the test setup consists of two 5G cells, each one associated with same O-DU and O-CU connected to 5G Core network, refer Figure 5-7 for the test setup topology. The test environment shall have single UE in Idle mode.

![](images/ebe50764450e7e18c057612f02d6a7af9825db967bae4fcae89ef8b2f115a994.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 7 Idle Mode Intra O-DU mobility test bed for SA mode of operation.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable. The UE mobility between the cells can be achieved by changing radio signal strength of source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.36. Test procedure

Below are the SA Mode Intra frequency steps

1. The �G cell setup is configured following Clause �.�.�.   
2. Configure two �G cells (cell � and cell �) of same frequency within an O-DU according to the test configuration. The cells are activated and unloaded.   
3. Both �G Cells are configured neighbours to each other, so that UE can use it for cell re-selection.   
4. The source and target �G cells for intra O-DU mobility shall be depicted as in Figure 5-7.   
5. The test UE is under source cell coverage.   
6. Power on the UE and UE shall successfully register to source �G cell.   
7. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell.

8. Once UE moves to new cell, make an MO data call.

9. Repeat the above test steps for �� iterations.

Below is the SA Mode Inter frequency steps

1. The �G cell setup is configured following Clause �.�.�.   
2. Configure two �G cells (cell � and cell �) on different frequencies within an O-DU according to the test configuration. The cells are activated and unloaded.   
3. Both �G Cells are configured neighbours to each other, so that UE can use it for cell re-selection.   
4. The source and target �G cells for intra O-DU mobility shall be depicted as in Figure 5-7.   
5. The test UE is under source cell coverage.   
6. Power on the UE and UE shall successfully register to source �G cell.   
7. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell, move the UE from source cell to target cell.   
8. Once UE moves to new cell, make an MO data call.   
9. Repeat the above test steps for �� iterations.

# 4.37. Test requirements (expected results)

The Idle mode intra O-DU cell reselection shall be verified for both intra-frequency and inter-frequency. Also verify call setup latency on a target cell with reference to RRC connection call flow defined in 3GPP 38.133, Clause 5.3.3.1. Following functionalities are also validated to declare the verdict.

• Cell re-selection is successful on target cell.   
• RRC connection establishment is successful on a target cell.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT side:

• Idle mode mobility time from UE, in idle mode at source to UE in idle mode to target.

UE side:

• Radio parameters such as RSRP, RSRQ. KPI’s related to Cell re-selection failure, idle mode mobility time from UE in idle mode at source to UE in idle mode to target.

The cell re-selection failure can be found out by checking if the cell re-selection is successful or not. The Idle to Connected on a target cell Time latency is measured by calculating the time between RRC_Idle mode to RRC_Connected state when UE moves to new cell after initiating an MO call. Capture the cell re-selection success/failure and latency for each iteration and sort the latency value observed for each iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are 10 in this case) and Maximum latency value observed in below tables:

Table 5 SEQ Table \\* ARABIC \s 1 13 5G Cell Re-selection Success and Failure KPI   

<table><tr><td colspan="1" rowspan="2">KPI</td><td colspan="10" rowspan="1">Repeat Times</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">10</td></tr><tr><td colspan="1" rowspan="1">Cell Re-selectionSuccess</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td>Cell Re-selection</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Failure</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 4.19. Idle mode Inter-O-DU mobility

# 4.38. Test description and applicability

The purpose of the test is to verify intra O-CU, idle mode inter O-DU mobility of a UE. The test validates the O-CU, O-DU, O-RU functionality in handling inter cell mobility. Test scenarios are classified into two groups as Standalone (SA) Intra frequency cell reselection and as Standalone (SA) Inter frequency cell reselection.

Idle mode Inter O-DU mobility shall follow 3GPP 38.133, Clause 4.2.2.3 and Clause 4.2.2.4 for intra frequency and inter frequency cell selection measurement, respectively. And 3GPP 38.304, Clause 5.2.2 for the state transition.

# 4.39. Test setup and configuration

In standalone Mode, the test setup consists of two 5G cells, each one associated with different O-DU, connected to same O-CU. The test environment shall have single UE in Idle mode.

![](images/9d2075670b3472d6453c4ca1dcf2b7fea4f8d7a652b2baa8bd10c2ac641222ca.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5 SEQ Figure \\* ARABIC \s 1 8 Inter O-DU mobility test bed for SA mode of operation Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable. The UE mobility between the cells can be achieved by changing radio signal strength of source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.40. Test procedure

Below are the SA Mode Intra frequency steps

1. The �G cell setup is configured following Clause �.��.�.   
2. All the �G cells are configured according to the test configuration. The cells are activated and unloaded   
3. Both �G Cells are configured neighbours to each other, so that UE can use it for cell re-selection.   
4. The source and target �G cells for inter O-DU mobility shall be depicted as in Figure 5-8.   
5. The test UE is under source cell coverage.   
6. Power on the UE and UE shall successfully register to source �G cell.   
7. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell.   
8. Once UE moves to new cell, make an MO data call.   
9. Repeat the above test steps for �� iterations.

Below is the SA Mode Inter frequency steps

1. The �G cell setup is configured following Clause �.��.�.   
2. All the �G cells are configured according to the test configuration. The cells are activated and unloaded.   
3. Both �G Cells are configured neighbours to each other, so that UE can use it for cell re-selection.   
4. The source and target �G cells for inter O-DU mobility shall be depicted as in Figure 5-8.   
5. The test UE is under source cell coverage.   
6. Power on the UE and UE shall successfully register to source �G cell.   
7. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell.   
8. Once UE moves to new cell, make an MO data call.   
9. Repeat the above test steps for �� iterations.

# 4.41. Test requirements (expected results)

The Idle mode inter O-DU cell reselection shall be verified for both intra-frequency and inter-frequency. Also verify call setup latency on a target cell with reference to RRC connection call flow mentioned in 3GPP 38.133, Clause 5.3.3.1. Following functionalities are also validated to declare the verdict.

RRC connection establishment is complete. Cell re-selection is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT side:

• Idle mode mobility time from UE, in idle mode at source to UE in idle mode to target.

UE side:

• Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) KPI’s related to Cell re-selection failure, Idle mode mobility time from UE, in idle mode at source to UE in idle mode to target

The cell re-selection failure can be found out by checking if the cell re-selection is successful or not. The Idle to Connected on a target cell Time latency is measured by calculating the time between RRC_Idle mode to RRC_Connected state when UE moves to new cell after initiating an MO call. Capture the cell re-selection success/failure and latency for each iteration and sort the latency value observed for each

iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are 10 in this case) and Maximum latency value observed in below tables:   
Table 5 SEQ Table \\* ARABIC \s 1 14 5G Cell Re-selection Success and Failure KPI   

<table><tr><td rowspan=2 colspan=1>KPI</td><td rowspan=1 colspan=10>Repeat Times</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>Cell Re-selectionSuccess</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Cell Re-selectionFailure</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.20. Idle mode Inter-O-CU mobility

# 4.42. Test description and applicability

The purpose of the test is to verify inter O-CU mobility of the UE. The test validates the O-CU, O-DU functionality in handling inter O-CU mobility connected to same 5G Core Network (in SA). The test validates the O-CU, O-DU, O-RU functionality in handling inter cell mobility. Test scenarios are classified into two groups as Standalone (SA) Intra frequency cell reselection and as Standalone (SA) Inter frequency cell reselection.

Idle mode Inter O-CU mobility shall follow 3GPP 38.133, Clause 4.2.2.3 and Clause 4.2.2.4 for intra frequency and inter frequency cell selection measurement, respectively. And 3GPP 38.304, Clause 5.2.2 for the state transition.

# 4.43. Test setup and configuration

In Standalone mode, the test setup consists of two 5G cells, each one associated with a different O-DU and O-CU connected to same 5G Core network, refer Figure 5-9 for the test setup topology. The test environment shall have single UE.

![](images/4112b492d277d5e4c26e32027efb30cab9f6c90f5348d556c529aaffbb6fb86d.jpg)

> **Image Summary:** {"image": "image_of_5G_O_RAN_architecture.png"}
  
Figure 5 SEQ Figure $\backslash \ast$ ARABIC \s 1 9 Inter O-CU mobility test bed for SA mode of operation Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing radio signal strength of source and target cells using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source cell to target cell.

# 4.44. Test procedure

# Below are the SA Mode Intra frequency steps

1. The 5G cell setup is configured following Clause 5.11.2.   
2. Configure two 5G cells (cell 1 and cell 2) connected to different O-DU and O-CU according to the test configuration. The cells are activated and unloaded.   
3. Both 5G Cells are configured neighbors to each other, so that UE can use it for cell re-selection.   
4. The source cell (source O-DU and source O-CU) is the cell where UE is initially placed as depicted in Figure 5-9.   
5. Power on the UE and UE shall successfully register to source �G cell.   
6. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell.   
7. Once UE moves to new cell, make an MO data call.   
8. Repeat the above test steps for �� iterations.

Below are the SA Mode Inter frequency steps

1. The 5G cell setup is configured following Clause 5.11.2.   
2. Configure two 5G cells (cell 1 and cell 2) connected to different O-DU and O-CU according to the test configuration. The cells are activated and unloaded.   
3. Both 5G Cells are configured neighbors to each other, so that UE can use it for cell re-selection.   
4. The source cell (source O-DU and source O-CU) is the cell where UE is initially placed as depicted in Figure 5-9.   
5. Power on the UE and UE shall successfully register to source �G cell.   
6. Wait till the UE goes in idle mode as per UE inactivity timer and then move the UE from source cell to target cell.   
7. Once UE moves to new cell, make an MO data call.   
8. Repeat the above test steps for �� iterations.

# 4.45. Test requirements (expected results)

The Idle mode inter O-CU cell reselection shall be verified for both intra-frequency and inter-frequency. Also verify call setup latency on a target cell with reference to RRC connection call flow mentioned in 3GPP 38.133, Clause 5.3.3.1. Following functionalities are also validated to declare the verdict.

RRC connection establishment is complete. Cell re-selection is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT side:

• Idle mode mobility time from UE, in idle mode at source to UE in idle mode to target.

UE side:

• Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) KPI’s related to Cell re-selection failure, Idle mode mobility time from UE, in idle mode at source to UE in idle mode to target

The cell re-selection failure can be found out by checking if the cell re-selection is successful or not. The Idle to Connected on a target cell Time latency is measured by calculating the time between RRC_Idle mode to RRC_Connected state when UE moves to new cell after initiating an MO call. Capture the cell re-selection success/failure and latency for each iteration and sort the latency value observed for each iteration in ascending order. Record the Minimum, Average (Sum of all latency value/ Total Iterations, Total Iterations are 10 in this case) and Maximum latency value observed in below tables:

Table 5 SEQ Table $\backslash \ast$ ARABIC \s 1 15 5G Cell Re-selection Success and Failure KPI   

<table><tr><td rowspan=2 colspan=1>KPI</td><td rowspan=1 colspan=10>Repeat Times</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>Cell Re-selectionSuccess</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Cell Re-selectionFailure</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.21. 5G/4G Inter-System Mobility - 5GS to EPS handover

# 4.46. Test description and applicability

The purpose of this test is to validate inter system handovers between 5G and LTE systems as defined in 3GPP TS 38.300 [47]. In this test scenario, inter system handover from 5G Standalone (i.e. connected with 5GC) to LTE Standalone (i.e. connected with EPC) is validated. The test validates the O-CU-CP/OCU-UP, O-DU, and O-RU functionality in handling Inter RAT mobility from 5G to LTE. This scenario covers handover of UE from 5G to LTE when UE is registered in 5G and moves from 5G coverage area to LTE coverage area. This scenario is applicable for LTE and 5G SA.

The test focuses on the procedure of ‘5GS to EPS handover using N26 interface’ as defined in 3GPP TS 23.502 [41] Clause 4.11.1.2.1.

# 4.47. Test setup and configuration

The test setup shall include 5G End to End system (5G SUT and 5G Core (5GC)) and LTE E2E system (4G SUT and 4G Core (EPC)). 5G and 4G core shall be interconnected for Inter System mobility (N26 interface between the MME and AMF) and shall supports a combined anchor point for 4G and 5G, i.e. SMF+PGW-C and UPF $^ +$ PGW-U. The LTE SUT connects to a 4G-5G interconnected core over the 4G interfaces, i.e. S1 to provide 4G LTE service to make E2E LTE system and the O-CU-CP/O-CU-UP, ODU and O-RUconnect to a 4G-5G interconnected core over the 5G interfaces, i.e. N2 and N3 to make E2E 5G SA system. The 4G and 5G SUTs and the components shall comply to the O-RAN specifications. This test needs a real or emulated UE. The test setup (UE, 4G SUT, 5G SUT, 5G and 4G Core) should include tools which have the ability to collect traces on the elements and/or packet captures of communication between the elements. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for. The 4G SUT, 5G SUT and their components (O-RU, O-DU and O-CU-CP/O-CU-UP) should have the right configuration and software load.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of the UE are initially set to excellent using RSRP as the metric. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside and RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing the radio signal strength of the source 5G cell and target 4G cell using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (using RSRP as the metric as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source 5G cell and target 4G cell.

# 4.48. Test procedure

Below are the 5G to LTE Inter System handover steps

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. �G and LTE cells are configured as neighbours to each other, so that the UE can trigger measurement events for Inter System handover.   
3. The test UE is under source �G cell coverage.   
4. Power on the UE and UE shall successfully register to source �G cell.   
5. The full-buffer UDP bi-directional data transmission (see Clause �.�) from the application server is initiated.   
6. The UE shall move from source �G cell and target �G cell to perform handover.

4.49. Test requirements (expected results)

The Inter System handover call flow shall be verified between 5G and LTE systems. Following functionalities shall also be validated:

PDU Session is established when full-buffer bi-directional data transmission is initiated with �G source cell   
Handover is successful.

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT/Application server side:

• Transmit downlink throughput measured at application server in time (average per second) Received uplink throughput measured at application server in time (average per second) Uplink packet loss percentage during handover. Uplink BLER, MCS, MIMO rank (RI) on PUSCH in time (average per second)

UE side:

Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) Downlink BLER, MCS, MIMO rank (RI) on PDSCH in time (average per second). Received Downlink throughput (L� and L� PDCP layers) in time (average per second). Downlink packet loss percentage during handover Uplink throughput (L� and L� PDCP layers) in time (average per second) Channel utilization, i.e. Number allocated/occupied downlink and uplink RBs in time (per TTI/average per second) and Number of allocated/occupied slots in time.

• KPIs related to Handover failure, Call drop, Handover latency, Handover interruption time.

# 4.22. 5G/4G Inter-System Mobility - EPS to 5GS handover

# 4.50. Test description and applicability

The purpose of this test is to validate inter system handovers between 5G and LTE systems as defined in 3GPP TS 38.300 [47]. In this test scenario, inter system handover from LTE Standalone (i.e. connected with EPC) to 5G Standalone (i.e. connected with 5GC) is validated. The test validates the O-CU-CP/OCU-UP, O-DU, and O-RU functionality in handling Inter RAT mobility from LTE to 5G. This scenario covers handover of UE from 5G to LTE when UE is registered in LTE and moves from LTE coverage area to 5G coverage area. This scenario is applicable for LTE and 5G SA.

The test focuses on the procedure of ‘EPS to 5GS handover using N26 interface’ as defined in 3GPP TS 23.502 [41] Clause 4.11.1.2.2.

# 4.51. Test setup and configuration

The test setup shall include 5G End to End system (5G SUT and 5G Core (5GC)) and LTE E2E system (4G SUT and 4G core (EPC)). 5G and 4G core shall be interconnected for Inter System mobility (N26 interface between the MME and AMF) and shall support a combined anchor point for 4G and 5G, i.e. SMF $^ +$ PGW-C and UPF $^ +$ PGW-U. The 4G SUT connects to a 4G-5G interconnected core over the 4G interfaces, i.e. S1 to provide 4G LTE service to make E2E LTE system and the O-CU-CP/O-CU-UP, ODU and O-RU connect to a 4G-5G interconnected core over the 5G interfaces, i.e. N2 and N3 to make E2E 5G SA system. The 4G and 5G SUTs and the components shall comply to the O-RAN specifications. This test needs Real or emulated UE. The test setup (UE, 4G SUT, 5G SUT, 5G and 4G Core) should include tools which have the ability to collect traces on the elements and/or packet captures of communication between the elements. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for. The 4G SUT, 5G SUT and their components (O-RU, O-DU and O-CU-CP/O-CU-UP) need to have the right configuration and software load.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of the UE are initially set to excellent using RSRP as the metric. The minimum coupling loss (see Clause 4.6) should not be exceeded. The UE should be placed inside and RF shielded box or RF shielded room if the UE is not connected via cable. The UE handover between the cells can be achieved by changing the radio signal strength of the source 4G cell and target 5G cell using variable attenuators.

Field setup: The drive route with source and target cells should be defined. The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (using RSRP as the metric as defined in Clause 4.6) should be observed. The minimum coupling loss (see Clause 4.5) should not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route from source 4G cell and target 5G cell.

# 4.52. Test procedure

Below are the LTE to 5G Inter System handover steps

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. LTE and �G cells are configured as neighbours to each other, so that the UE can trigger measurement events for Inter System handover.

3. The test UE is under source �G cell coverage.   
4. Power on the UE and UE shall successfully register to source �G cell.   
5. The full-buffer UDP bi-directional data transmission (see Clause �.�) from the   
application server is initiated.   
6. The UE shall move from source �G cell and target �G cell to perform handover.

# 4.53. Test requirements (expected results)

The Inter System handover call flow shall be verified between LTE and 5G systems. Following functionalities shall also be validated:

PDU Session is established when full-buffer bi-directional data transmission is   
initiated with LTE source cell   
Handover is successful

In addition to the common minimum set of configuration parameters defined (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

SUT/Application server side:

• Transmit downlink throughput measured at application server in time (average per second) Received uplink throughput measured at application server in time (average per second) Uplink packet loss percentage during handover. Uplink BLER, MCS, MIMO rank (RI) on PUSCH in time (average per second)

UE side:

Radio parameters such as RSRP, RSRQ, SINR on PDSCH in time (average per second) Downlink BLER, MCS, MIMO rank (RI) on PDSCH in time (average per second). Received Downlink throughput (L� and L� PDCP layers) in time (average per second). Downlink packet loss percentage during handover Uplink throughput (L� and L� PDCP layers) in time (average per second) Channel utilization, i.e. Number allocated/occupied downlink and uplink RBs in time (per TTI/average per second) and Number of allocated/occupied slots in time.

KPIs related to Handover failure, Call drop, Handover latency, Handover interruption time.

# 6. Performance tests

# 4.23. Performance tests introduction

This clause describes the tests evaluating and assessing the performance of radio access network from network end-to-end perspective (see Clause 4.1). The focus of the testing is on the end-user performance which is compared against the target and expected performance values. The pass and fail thresholds are defined for the test wherever possible.

The general test methodologies and configurations are mentioned in Clause 4.

Unless otherwise stated in the clause, the tests are suitable and can be performed in both laboratory as well as field testing environments, with pros and cons for each environment. The specific lab and field test setups are mentioned in each test.

The following end-to-end performance tests are defined in this clause as an extension of NGMN testing framework [3]:

Table 6 SEQ Table \\* ARABIC \s 1 1: E2E Performance Test Case summary   

<table><tr><td></td><td>Applicable technology</td></tr></table>

<table><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>TestID</td><td rowspan=1 colspan=1>E2E Performance Assessment</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6.2</td><td rowspan=1 colspan=1>Downlink peak throughput</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.3.</td><td rowspan=1 colspan=1>Uplink peak throughput</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.4</td><td rowspan=1 colspan=1>Downlink throughput in different radio conditions</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.5</td><td rowspan=1 colspan=1>Uplink throughput in different radio conditions</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.6</td><td rowspan=1 colspan=1>Bidirectional throughput in different radio conditions</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.7</td><td rowspan=1 colspan=1>Downlink coverage throughput (link budget)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.8</td><td rowspan=1 colspan=1>Uplink coverage throughput (link budget)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.9</td><td rowspan=1 colspan=1>Downlink aggregated cell throughput (cell capacity)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.10</td><td rowspan=1 colspan=1>Uplink aggregated cell throughput (cell capacity)</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.11</td><td rowspan=1 colspan=1>Impact of fronthaul latency on downlink peak throughput</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.12</td><td rowspan=1 colspan=1>Impact of fronthaul latency on uplink peak throughput</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.13</td><td rowspan=1 colspan=1>Impact of midhaul latency on downlink peak throughput</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>6.14</td><td rowspan=1 colspan=1>Impact of midhaul latency on uplink peak throughput</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr></table>

Future versions of this specification may add additional end-to-end performance tests not currently addressed in this version, for example:

• Downlink throughput with inter-cell interferences (multi-cell, single UE scenario)   
Uplink throughput with inter-cell interferences (multi-cell, single UE scenario) Downlink drive throughput (multi-cell, single UE scenario) Uplink drive throughput (multi-cell, single UE scenario) End-to-end latency (single cell scenario, single UE scenario) Impact of fronthaul compression scheme on downlink peak throughput (single cell, single UE scenario) Impact of fronthaul compression scheme on uplink peak throughput (single cell, single UE scenario)   
• Resource scheduling (single cell, multi-UE scenario)

# 4.24. Expected throughput calculation

# 4.54. 4G LTE

The 4G LTE expected theoretical downlink or uplink throughput at the physical layer can be calculated using the following formula:

• J is the number of aggregated LTE component carriers. is the coding rate corresponding to channel quality (CQI and SINR). The maximum coding rate is �.����.

For the j-th component carrier:

is the number of MIMO layers. The maximum is � (� in LTE-Advanced) in downlink and � (� in LTE -Advanced) in uplink.

is the modulation order, which is equal to � for QPSK, � for ��QAM, � for ��QAM, � for ��QAM, � for ���QAM.

• is the number of PRBs allocated in bandwidth BW ‒ see Table 62.

# Table 6 SEQ Table $\backslash ^ { * }$ ARABIC \s 1 2 The number of PRBs allocated in bandwidth

<table><tr><td rowspan=1 colspan=1>Bandwidth [MHz]</td><td rowspan=1 colspan=1>1.4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Number of PRBs</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>100</td></tr></table>

OH is overhead for control channels and signalling (i.e., Reference Signal, PSS, SSS, PBCH, PDCCH, etc. in downlink or SRS, PUCCH, PRACH in uplink) within a period of � sec ‒ see Table 63 for downlink.

Table 6 SEQ Table \\* ARABIC \s 1 3 Overhead as a function of bandwidth, no. of antenna ports and CFI   

<table><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=2>1.4 MHz</td><td rowspan=1 colspan=2>3MHz</td><td rowspan=1 colspan=2>5 MHz</td><td rowspan=1 colspan=2>10 MHz</td><td rowspan=1 colspan=2>15 MHz</td><td rowspan=1 colspan=2>20 MHz</td></tr><tr><td rowspan=1 colspan=1>CFI</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>1TX(ant.. ports)</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>0.14</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>0.12</td><td rowspan=1 colspan=1>0.17</td><td rowspan=1 colspan=1>0.12</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>0.16</td></tr><tr><td rowspan=1 colspan=1>2TX(ant.ports)</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.24</td><td rowspan=1 colspan=1>0.17</td><td rowspan=1 colspan=1>0.22</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.20</td></tr><tr><td rowspan=1 colspan=1>4TX(ant.ports)</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.29</td><td rowspan=1 colspan=1>0.22</td><td rowspan=1 colspan=1>0.26</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.24</td></tr></table>

is the average OFDM symbol duration in a subframe, and it is equal to for normal Cyclic Prefix (�� OFDM symbols per slot) or for extended CP (�� OFDM symbols per slot).

is a ratio of the symbols allocated for DL or UL data to total number of symbols in a frame (��ms) ‒ predefined patters (uplink-downlink configuration, special subframe configuration) for DL/UL allocation in [��]. In case of FDD mode, the $D L U L _ { r a t i o }$ is equal to �.

Example of calculation of expected downlink throughput for the following system configuration:

MIMO $2 \times 2 $ ${ \mathsf { B W } } = 2 0 { \mathsf { M H z } } \ \mathrm { ~ \to ~ } { \mathsf { = } } 1 0 0$   
• Normal CP   
• $\mathsf { C F } | = 1 \to \mathsf { O H } = 0 . 1 5$ no carrier aggregation $ \mathsf { J } = \mathsf { 1 }$ ${ \mathsf { M C S } } = 2 8$ and modulation ��QAM and TDD with uplink-downlink configuration $\ c = 1$ (i.e., DSUUD) and special subframe configuration $= 7$ (i.e., ��:�:�) →

# 4.55. 5G NR

The 5G NR expected theoretical downlink or uplink throughput at physical layer (UE category is not   
assumed) can be calculated using the following formula [15]:   
where

• J is the total number of component carriers (CC) in a band or band combination. The maximum number is �� [��].

is the coding rate corresponding to channel quality (CQI, SINR), and it is calculated as Target_code_rate [22]/1024. For LDPC code the maximum coding rate is ���/����.

For the j-th component carrier:

• is the number of MIMO layers. The maximum is � in downlink and � in uplink [��].

is the modulation order, which is equal to � for QPSK, � for ��QAM, � for ��QAM, � for ��QAM, � for ���QAM.

is the scaling factor [��] which can take the values �.�, �.��, �.� or �. The scaling factor is signalled per band and per band combination as per UE capability signalling.

• is the overhead of control channels and signalling within a period of � sec, and it is equal to:

• �.�� for frequency range � (FR�) for DL • �.�� for frequency range � (FR�) for DL • �.�� for frequency range � (FR�) for UL • �.�� for frequency range � (FR�) for UL

is �G NR numerology (sub-carrier spacing) which can take the values from � to � [��]. The number of slots per frame and sub-carrier spacing vary with numerology ‒ see Table 64.

Table 6 SEQ Table $\backslash ^ { * }$ ARABIC \s 1 4 5G NR numerology   

<table><tr><td rowspan=1 colspan=1>5G NRnumerology μ</td><td rowspan=1 colspan=1>Sub-carrierspacing (SCS)</td><td rowspan=1 colspan=1>Number of slots perframe</td><td rowspan=1 colspan=1>Number ofsymbols per slot</td><td rowspan=1 colspan=1>Total number ofsymbols per frame</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>15 kHz</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>14 (normal CP)</td><td rowspan=1 colspan=1>140</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>30 kHz</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>14 (normal CP)</td><td rowspan=1 colspan=1>280</td></tr><tr><td rowspan=2 colspan=1>2</td><td rowspan=1 colspan=1>60 kHz</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>14 (normal CP)</td><td rowspan=1 colspan=1>560</td></tr><tr><td rowspan=1 colspan=1>60kHz</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>12 (extended CP)</td><td rowspan=1 colspan=1>480</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>120kHz</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>14 (normal CP)</td><td rowspan=1 colspan=1>1120</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>240kHz</td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>14 (normal CP)</td><td rowspan=1 colspan=1>2240</td></tr></table>

is the average OFDM symbol duration in a subframe for numerology µ, and it is equal to for normal Cyclic Prefix (�� OFDM symbols per slot) or for extended CP (�� OFDM symbols per slot).

• is the number of PRBs allocated in bandwidth BW with numerology µ - see Table 65.

Table 6 SEQ Table \\* ARABIC \s 1 5 The max. number of PRBs for each supported bandwidth and 5G NR numerology µ [18], [19]   

<table><tr><td colspan="1" rowspan="1"></td><td colspan="14" rowspan="1">Channel bandwidth BW[MHz]</td></tr><tr><td colspan="1" rowspan="1">μ</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">40</td><td colspan="1" rowspan="1">50</td><td colspan="1" rowspan="1">60</td><td colspan="1" rowspan="1">80</td><td colspan="1" rowspan="1">90</td><td colspan="1" rowspan="1">100</td><td colspan="1" rowspan="1">200</td><td colspan="1" rowspan="1">400</td></tr><tr><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">52</td><td colspan="1" rowspan="1">79</td><td colspan="1" rowspan="1">106</td><td colspan="1" rowspan="1">133</td><td colspan="1" rowspan="1">160</td><td colspan="1" rowspan="1">216</td><td colspan="1" rowspan="1">270</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">51</td><td colspan="1" rowspan="1">65</td><td colspan="1" rowspan="1">78</td><td colspan="1" rowspan="1">106</td><td colspan="1" rowspan="1">133</td><td colspan="1" rowspan="1">162</td><td colspan="1" rowspan="1">217</td><td colspan="1" rowspan="1">245</td><td colspan="1" rowspan="1">273</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">31</td><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">51</td><td colspan="1" rowspan="1">65</td><td colspan="1" rowspan="1">79</td><td colspan="1" rowspan="1">107</td><td colspan="1" rowspan="1">121</td><td colspan="1" rowspan="1">135</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">66</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">132</td><td colspan="1" rowspan="1">264</td><td colspan="1" rowspan="1">N/A</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">66</td><td colspan="1" rowspan="1">132</td><td colspan="1" rowspan="1">264</td></tr></table>

is a ratio of the symbols allocated for DL or UL data to total number of symbols in a time period (periodicity) in TDD mode ‒ predefined slot formats in [��]. In case of FDD mode, the $D L U L _ { r a t i o }$ is equal to �.

Example of calculation of expected downlink throughput for the following system configuration:

$$
 S C S = 1 5 k H z  \mu = 0
$$

• MIMO $2 \times 2 $

$$
\mathsf { B W } = 2 0 \mathsf { M H z } \to = 1 0 6
$$

• Normal CP

• no carrier aggregation $ \mathsf { J } = \mathsf { 1 }$ • ${ \mathsf { M C S } } = 2 8$ and modulation ��QAM and Target code rate $= 9 4 8$

• scaling factor $f = 1$

• downlink throughput and $\mathsf { F R 1 } \to \mathsf { O H } = 0 . 1 4$ • TDD configuration �:� (DDDDSU), i.e., four DL slots (slot format � [21]), one Special slot (slot format �� [21]) and one UL slot (slot format � [21]) where slot format � means allocation of all �� symbols for DL, slot format � means allocation of all �� symbols for UL, slot format �� means allocation of �� symbols for DL, � symbols for Guard Period, � symbols for UL

# 4.25. Downlink peak throughput

# 4.56. Test description and applicability

The purpose of the test is to measure the peak (i.e., maximum achievable) user data throughput in the downlink direction (i.e., data transmitted from application (traffic) server to UE). A stationary UE is placed under excellent radio conditions inside an isolated cell.

# 4.57. Test setup and configuration

The test setup is a single cell scenario (i.e., an isolated cell without any inter-cell interference – see Clause 4.7) with a stationary UE (real or emulated UE) placed under excellent radio conditions as defined in Clause 4.6 – using SINR as the metric since this is a downlink test. Note that in this case of a single cell scenario, SINR is in fact SNR as inter-cell interference is not present. Within the cell there shall be only one active UE downloading data from the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment shall be setup to achieve excellent radio conditions (SINR as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside an RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (SINR as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

Figure 6 SEQ Figure \\* ARABIC \s 1 1 The test setups of 4G, 5G NSA and 5G SA   
![](images/e22e6083751002499e2c9152d84a7015ceb334f846036d07356565da9402ccfc.jpg)

> **Image Summary:** {"task_description": "Convert the image into a detailed, high-fidelity text description using the specified template."}


4.58. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated UE) is placed under excellent radio conditions (cell centre close to radiated SUT’s antenna) using SINR thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.

3. The downlink full-buffer UDP and TCP data transmission (see Clause �.�) from the application server shall be verified by adjusting the connection settings (cabled environment) or UE position (OTA environment). The UE under excellent radio conditions that is achieving peak user throughput shall see stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank (number of layers). These KPIs shall also be verified.

4. The UE shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmission from the application server to the UE is started. The UE shall receive the data from the application server.

5. All the required performance data (incl. the signalling and control data) as specified in the “Test requirements” clause below is measured and captured at the UE and Application server sides using logging/measurement tools. The duration of the test shall be at least � minutes when the throughput is stable. The location and position of the UE shall remain unchanged during the entire measurement duration (capture of log data).

6. The capture of log data is stopped. The downlink full-buffer UDP data transmission from the application server is stopped.

7. [Optional] Steps � to � are repeated for downlink full-buffer TCP data transmission.

# 4.59. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second)

• PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L� and Application layers) (average sample per second) Downlink transmission mode Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

When the UE is under excellent radio conditions (cell centre), the stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank shall be observed. The UE shall also receive the data with minimum downlink BLER.

Table 66 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison purposes to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 6 Example record of test results (median and standard deviation from the captured samples)

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>UDP</td><td rowspan=1 colspan=1>TCP</td></tr><tr><td rowspan=1 colspan=1>Received L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL PRB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• Received UDP downlink throughput (L� and Application layer) vs Time duration   
• PDSCH SINR vs Time duration   
• Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs Time duration

The gap analysis shall be provided for the measured and the expected target downlink throughputs which can be calculated based on the procedures from Clause 6.1.

# 4.26. Uplink peak throughput

4.60. Test description and applicability

The purpose of the test is to measure the peak (i.e., maximum achievable) user data throughput in uplink direction (i.e., data transmitted from UE to application (traffic) server). The stationary UE is placed under excellent radio conditions inside the isolated cell.

# 4.61. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed under excellent radio conditions as defined in Clause 4.6 – using RSRP as the metric since this is an uplink test. Within the cell there shall be only one active UE uploading data to the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment shall be setup to achieve excellent radio conditions (RSRP as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside an RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.5) shall not be exceeded.

The test setups of 4G, 5G NSA and 5G SA are mentioned in Figure 61.

# 4.62. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated UE) is placed under excellent radio condition (cell centre close to radiated SUT’s antenna) using RSRP thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmission (see Clause �.�) from UE to the application server shall be verified by adjusting the connection settings (cabled environment) or UE position (OTA environment). The UE under excellent radio conditions that is achieving peak user throughput shall see stable utilization of the highest possible uplink MCS and uplink transport block size. These KPIs shall also be verified.

4. The UE shall be turned off or set to airplane mode, if possible, to empty the buffers. The uplink full-buffer UDP data transmission from UE to the application server is started. The application server shall receive the sent data.

5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE, SUT and Application server sides using logging/measurement tools. The duration of test shall be at least � minutes when the throughput is stable. The location and position of the UE shall remain unchanged during the entire measurement duration (capture of log data).

6. The capture of log data is stopped. The uplink full-buffer UDP data transmission from UE to the application server is stopped.   
7. The UE shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer TCP data transmission from UE to the application server is started, and Step � is repeated.

# 4.63. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
PUSCH BLER, PUSCH MCS (average sample per second)   
Transmit power on PUSCH   
Transmitted uplink throughput (Application layer) (average sample per second)   
Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of   
allocated/occupied slots (average sample per second)

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average sample per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

When the UE is in excellent radio condition (cell centre), the stable utilization of the highest possible uplink MCS and uplink transport block size shall be observed and evaluated. The SUT shall also receive the data with the minimum uplink BLER.

Table 67 gives an example of the test results record (median and standard deviation from the measured samples shall be provided for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 7 Example record of test results (median and standard deviation from the measured samples)   

<table><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UDP</td><td colspan="1" rowspan="1">TCP</td></tr><tr><td colspan="1" rowspan="1">Received L1 UL throughput [Mbps]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">L1 UL Spectral efficiency [bps/Hz]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Received Application UL throughput[Mbps]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSRP [dBm]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PDSCH SINR [dB]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PUSCH transmit power [dBm]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PUSCH MCS</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td>UL RB number</td><td></td><td></td></tr><tr><td>PUSCH BLER [%]</td><td></td><td></td></tr></table>

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• Received UDP uplink throughput (L� and Application layers) vs Time duration   
• UE RSRP vs Time duration   
Number of allocated/occupied uplink PRBs and Number of allocated/occupied slots vs Time duration

The gap analysis shall be provided for the measured and the expected target uplink throughputs which can be calculated based on the procedures from Clause 6.1.

# 4.27. Downlink throughput in different radio conditions

# 4.64. Test description and applicability

The purpose of the test is to measure the user experienced data throughput in the downlink direction while varying received radio signal quality (strength). The UE is placed in different stationary points inside the isolated cell.

# 4.65. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in different radio conditions as defined in Clause 4.6 - SINR shall be considered in case of downlink. Note that in this case of single cell scenario, SINR is in fact SNR as inter-cell interferences are not present. The UE is sequentially placed in different radio conditions ranging from good to poor. Note that the testing of peak downlink throughput in excellent radio conditions is already covered in Clause 6.2 and so is skipped in this clause. Within the cell there shall be only one active UE in time downloading data from the application (traffic) server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/ core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for lab as well as field environment.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to good. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The change in radio conditions of UE, from excellent through fair and good to poor, is achieved by increasing the attenuation of radio signal. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The test points with good, fair, and poor radio conditions (as defined in Clause 4.6) shall be defined inside the serving cell. The minimum coupling loss (see Clause 4.5) shall not be exceeded. The UE is initially placed where good radio conditions (SINR as defined in Clause 4.6) shall be observed. The change in radio conditions is achieved by moving the UE inside the serving cell from close to cell centre (with good radio conditions) to cell edge (with poor radio conditions).

The test setups of 4G, 5G NSA and 5G SA are mentioned in Figure 61.

# 4.66. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated UE) is placed under good radio conditions (close to cell centre) using SINR thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.   
3. The downlink full-buffer UDP and TCP data transmission (see Clause �.�) from the application server shall be verified by adjusting the connection settings (cabled environment) or UE position (OTA environment) to achieve good radio conditions.   
4. The UE shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmission from the application server to the UE is started. The UE shall receive the data from the application server.   
5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE and Application server sides using logging/measurement tools. The duration of test shall be at least � minutes when the throughput is stable. The location and position of the UE shall remain unchanged during the entire measurement duration (capture of log data).   
6. The capture of log data is stopped. The downlink full-buffer UDP data transmission from the application server is stopped.   
7. The radio conditions of UE are changed to fair using SINR thresholds as indicated in Clause �.�. The steps � to � are repeated.   
8. The radio conditions of UE are changed to poor (cell edge) radio condition using SINR thresholds as indicated in Clause �.�. Steps � to � are repeated.   
9. [Optional] Steps � to � are repeated for downlink full-buffer TCP data transmission.

# 4.67. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per   
second)   
Received downlink throughput (L�, and Application layers) (average sample per   
second)   
Downlink transmission mode   
Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number   
of allocated/occupied slots (average sample per second)

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

As the UE moves from good (close to cell centre), to fair, and to poor (cell edge) radio conditions, the changing radio conditions shall cause the UE to report lower CQI and MIMO rank which results in assignment of lower MCS and lower data throughput in the downlink.

Table 68 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 8 Example record of test results (median and standard deviation from the captured samples)   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>UDP /TCP</td><td rowspan=1 colspan=1>UDP /TCP</td><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Received L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• Received UDP downlink throughput (L� and Application layer) vs Time duration   
• PDSCH SINR vs Time duration   
• Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs Time duration

The gap analysis shall be provided for the measured and the expected target downlink throughputs which can be calculated based on the procedures from Clause �.�.

# 4.28. Uplink throughput in different radio conditions

# 4.68. Test description and applicability

The purpose of the test is to measure the user experienced data throughput in uplink while varying received radio signal quality (strength). The UE is placed in different stationary points inside the isolated cell.

# 4.69. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in different radio conditions as defined in Clause 4.6 - RSRP shall be considered in case of uplink. The UE is gradually placed in different radio conditions from good (close to cell centre) to poor (cell edge – coverage limited cell edge in case of single cell scenario). Note that the testing of peak uplink throughput in excellent radio conditions is already covered in Clause 6.3 and so is skipped in this clause. Within the cell there shall be only one active UE in time uploading data to the application (traffic) server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to good. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The change in radio conditions of UE, from good to fair to poor, is achieved by increasing the attenuation of radio signal. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The test points with good, fair, and poor radio conditions (as defined in Clause 4.6) shall be identified inside the serving cell. The minimum coupling loss (see Clause 4.5) shall not be exceeded. The UE is initially placed where good radio conditions (RSRP as defined in Clause 4.6) shall be observed. The change in radio conditions is achieved by moving the UE inside the serving cell from close to cell centre (with good radio conditions) to cell edge (with poor radio conditions).

The test setups of 4G, 5G NSA and 5G SA are illustrated in Figure 61.

# 4.70. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated UE) is placed under good radio condition (close to cell centre) using RSRP thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmission (see Clause �.�) from UE to the application server shall be verified by adjusting the connection settings (cabled environment) or UE position (OTA environment) to achieve good radio conditions.

4. The UE shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer UDP data transmission from UE to the application server is started. The application server shall receive the data from UE.

5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE, SUT and application server side using logging/measurement tools. The duration of test shall be at least � minutes when the throughput is stable. The location and position of the UE shall remain unchanged during the entire measurement duration (capture of log data).

6. The capture of log data is stopped. The uplink full-buffer UDP data transmission from UE to the application server is stopped.

7. The radio conditions of UE are changed to fair using RSRP thresholds as indicated in Clause �.�. The steps � to � are repeated.

8. The radio conditions of UE are changed to poor (cell edge) radio condition using RSRP thresholds as indicated in Clause �.�. Steps � to � are repeated.

9. [Optional] Steps � to � are repeated for uplink full-buffer TCP data transmission.

# 4.71. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
PUSCH BLER, PUSCH MCS (average sample per second)   
Transmit power on PUSCH   
Transmitted uplink throughput (Application layer) (average sample per second)   
Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of   
allocated/occupied slots (average sample per second)

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

Table 69 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 9 Example record of test results (median and standard deviation from the measured samples)   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>UDP /TCP</td><td rowspan=1 colspan=1>UDP / TCP</td><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Received L1 UL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 UL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application UL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH transmit power [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• Received UDP uplink throughput (L� and Application layers) vs Time duration • UE RSRP vs Time duration

• Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs Time duration

The gap analysis shall be provided for the measured and the expected target uplink throughputs which can be calculated based on the procedures from Clause �.�.

# 4.29. Bidirectional throughput in different radio conditions

# 4.72. Test description and applicability

The purpose of the test is to measure the user experienced data throughput in both downlink and uplink in parallel while varying received radio signal quality (strength). The UE is placed in different stationary points inside the isolated cell. The test also includes the measurement of peak (maximum achievable) data throughput of UE located in the excellent radio conditions, and cell edge coverage data throughput of UE located at the cell edge in the poor radio conditions.

# 4.73. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated) placed in different radio conditions as defined in Clause $4 . 6 -$ RSRP shall be considered in this case. The UE is gradually placed in different radio conditions from excellent (cell centre) to poor (cell edge – coverage limited cell edge in case of single cell scenario). Within the cell there shall be only one active UE in time simultaneously downloading data from and uploading data to the application (traffic) server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The change in radio conditions of UE, from excellent through fair and good to poor, is achieved by increasing the attenuation of radio signal. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The test points with excellent, good, fair, and poor radio conditions (as defined in Clause 4.6) shall be identified inside the serving cell. The minimum coupling loss (see Clause 4.5) shall not be exceeded. The UE is initially placed in the cell center close to the SUT’s antenna(s), where excellent radio conditions (using RSRP as the metric as defined in Clause 4.6) shall be observed. The change in radio conditions is achieved by moving the UE inside the serving cell from cell centre (with excellent radio conditions) to cell edge (with poor radio conditions).

The test setups of 4G, 5G NSA and 5G SA are illustrated in Figure 61.

# 4.74. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed under excellent radio conditions as using RSRP thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.

3. The simultaneous downlink and uplink full-buffer UDP and TCP data transmission (see Clause �.�) shall be verified by adjusting the connection settings (cabled environment) or UE position (OTA environment). The UE under excellent radio conditions that is achieving peak uplink and downlink user throughput shall see stable utilization of the highest possible MCS, downlink block size and MIMO rank (number of layers). These KPIs shall also be verified.

4. The UE shall be turned off or set to airplane mode, to empty the buffers. The simultaneous downlink and uplink full-buffer UDP data transmissions are started. Both the UE and application server shall receive the data.   
5. All the required performance data (incl. the signalling and control data) as specified in the “Test requirements” clause below are measured and captured at UE, SUT and application server side using logging/measurement tools. The duration of test shall be at least � minutes when the throughput is stable. The location and position of the UE shall remain unchanged during the entire measurement duration (capture of log data).   
6. The capture of log data is stopped. The simultaneous downlink and uplink full-buffer UDP data transmissions are stopped.   
7. The radio conditions of UE are changed to good as defined by both SINR and RSRP in Clause �.�, if possible. The steps � to � are repeated.   
8. The radio conditions of UE are changed to fair as defined by both SINR and RSRP in Clause �.�, if possible. The steps � to � are repeated.   
9. The radio conditions of UE are changed to poor (cell edge) radio condition as defined by both SINR and RSRP in Clause �.�, if possible. The steps � to � are repeated.   
10. [Optional] Steps � to � are repeated for simultaneous downlink and uplink full-buffer TCP data transmission.

# 4.75. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample pe second) PDSCH BLER, PDSCH MCS, PUSCH BLER, PUSCH MCS (average sample per second)   
DL MIMO rank (number of layers) (average sample per second) Downlink transmission mode Transmit power on PUSCH   
Received downlink throughput (L�, and Application layers) (average sample pe second)   
• Transmitted uplink throughput (Application layer) (average sample per second)

• Channel utilization, i.e., Number allocated/occupied PRBs and Number of allocated/ occupied slots in both downlink and uplink directions (average sample per second)

SUT side (if capture of logs is possible):

• Radio parameters such as PUSH SINR (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second) • Transmitted downlink throughput (Application layer) (average sample per second)

When the UE is under excellent radio conditions (cell centre), the stable utilization of the highest possible MCS and transport block size in both uplink and downlink direction shall be observed and evaluated. The UE and SUT shall also receive the data with the minimum downlink and uplink BLER, respectively.

Table 610 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 10 Example record of test results (median and standard deviation from the captured samples)   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>UDP/TCP</td><td rowspan=1 colspan=1>UDP /TCP</td><td rowspan=1 colspan=1>UDP /TCP</td><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Received L1 UL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 UL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application UL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH transmit power [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL PUSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• Received UDP uplink throughput (L� and Application layer) vs Time duration • Received UDP downlink throughput (L� and Application layer) vs Time duration • UE RSRP vs Time duration

• UE PDSCH SINR vs Time duration   
• Number of allocated/occupied downlink PRBs and Number of allocated/occupied downlink slots vs Time duration   
• Number of allocated/occupied uplink PRBs and Number of allocated/occupied uplink slots vs Time duration

The bidirectional DL and UL throughputs shall be compared with unidirectional downlink (Clause �.�) and uplink (Clause �.�) throughputs. Assuming the same test conditions (radio conditions), the bidirectional and unidirectional throughputs are expected to be equal.

The gap analysis shall be provided for the measured and the expected target downlink and uplink throughputs which can be calculated based on the procedures from Clause �.�.

# 4.30. Downlink coverage throughput (link budget)

# 4.76. Test description and applicability

The purpose of the test is to measure the downlink user data throughput (i.e., data transmitted from application (traffic) server to UE) when radio conditions of UE change gradually. Test is verified by moving UE from center to edge of the isolated cell on the main lobe of SUT’s antenna until UE loses the coverage (call drop). Test assesses link adaptation and effect on scheduling, CQI, MCS, Number of layers (MIMO Rank) assignment etc. during the movement of UE from excellent radio conditions to poor radio conditions.

# 4.77. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with UE (real or emulated) slowly moving in the main lobe of SUT’s antenna out from cell centre to cell edge until UE loses the coverage (call drop). The drive route inside the cell shall be defined to cover the whole range of SINR values from excellent (cell center) to poor (cell edge) radio conditions as defined in Clause 4.6. Note that in case of single cell scenario SINR is in fact SNR as inter-cell interferences are not present. Within the cell there shall be only one active UE downloading UDP/TCP data from the application server. The application server shall be placed as close as possible to the core/ core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The movement of UE out from cell centre to cell edge can be achieved by gradually increasing the attenuation of radio signal to cover the whole range of SINR from excellent through good and fair to poor (as defined in Clause 4.6) until UE loses the coverage (call drop). The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The drive route inside the isolated cell shall be defined to cover the whole range of SINR values from excellent (cell center) through good and fair to poor (cell edge) (as defined in Clause 4.6) until UE loses the coverage (call drop). The UE is placed in the centre of cell close to the radiated SUT’s antenna(s). The minimum coupling loss (see Clause 4.5) shall not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route out from cell centre to cell edge until UE loses the coverage (call drop) – see Figure 62.

Figure 6 SEQ Figure \\* ARABIC \s 1 2 Testing of link budget in the field setup

4.78. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.   
2. The UE (real or emulated) is placed under excellent radio condition (cell centre) using SINR thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.   
3. The downlink full-buffer UDP and TCP data transmission (see Clause �.�) from the application server shall be verified. The excellent radio conditions experiencing peak user throughput is identified with stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank (number of layers). These KPIs shall also be verified.   
4. The UE shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmission from the application server to the UE is started. The UE shall receive the data from the application server.   
5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE and Application server sides using logging/measurement tools.   
6. In the field setup, the UE is moved along the defined drive route out from cell centre (excellent radio conditions) to cell edge (poor radio conditions) on the main lobe of SUT’s antenna and with constant speed of around ��kph until UE loses the coverage (call drop).   
7. In the lab setup, the attenuation between the antenna connectors of O-RU and UE is gradually increased until UE losses the coverage (call drop).   
8. The capture of log data is stopped. The downlink full-buffer UDP data transmission from the application server to UE is stopped.   
9. [Optional] Steps � to � are repeated for downlink full-buffer TCP data transmission. Test requirements (expected results)

# 4.79.

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L� and Application layers) (average sample per second)

• Downlink transmission mode (average sample per second) Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)   
• GPS coordinates (latitude, longitude) in the field setup

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

Initially when the UE is in the excellent radio conditions (cell centre), the stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank shall be observed and evaluated. The UE shall also receive the data with the minimum downlink BLER. As the UE moves out from excellent radio conditions (cell centre), the radio conditions of the UE change gradually from excellent through good and fair to poor (see Clause 4.6). The changing radio conditions may cause UE reporting lower CQI and MIMO rank which results in assignment of lower MCS and lower data throughput in downlink. Such a behavior shall be observed and evaluated.

Note that the test results can be affected by the various coverage enhancing features (e.g., transmit/receive diversity) at SUT and/or at UE sides. The used coverage enhancement features shall be also listed in the test report.

The following figures shall be included in the test report, and the behavior shall be evaluated. In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Received UDP downlink throughput (L� and Application layer) vs PDSCH SINR (all the samples as well as average curve with median values)   
Received UDP L� downlink spectral efficiency vs PDSCH SINR (all the samples as well as average curve with median values)   
Cumulative distribution function of PDSCH SINR   
Cumulative distribution function of PDSCH MCS   
Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs PDSCH SINR (all the samples as well as average curve with median values)

In the field environment, the cell coverage distance in meters (i.e., a straight line from the cell site) that corresponds to the cell-edge downlink application throughput of � Mbps for LTE and �� Mbps for �G NR shall be recorded.

# 4.31. Uplink coverage throughput (link budget)

# 4.80. Test description and applicability

The purpose of the test is to measure the uplink user data throughput (i.e., data transmitted from UE to application (traffic) server) when radio conditions of UE change gradually. Test is verified by moving UE from center to edge of the isolated cell on the main lobe of SUT’s antenna until UE loses the coverage (call drop). Test assesses link adaptation and effect on scheduling, uplink transmit power (power control), CQI, MCS, etc. during the movement of UE from excellent radio conditions to poor radio conditions.

# 4.81. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with UE (real or emulated) slowly moving in the main lobe of SUT’s antenna out from cell centre to cell edge until UE loses the coverage (call drop). The drive route inside the cell shall be defined to cover the whole range of RSRP values from excellent (cell center) to poor (cell edge) radio conditions as defined in Clause 4.6. Within the cell there shall be only one active UE uploading UDP/TCP data to application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The radio conditions of UE are initially set to excellent. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The movement of UE out from cell centre to cell edge can be achieved by gradually increasing the attenuation of radio signal to cover the whole range of RSRP from excellent through good and fair to poor (as defined in Clause 4.6) until UE loses the coverage (call drop). The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The drive route inside the isolated cell shall be defined to cover the whole range of RSRP values from excellent (cell center) through good and fair to poor (cell edge) (as defined in Clause 4.6) until UE loses the coverage (call drop). The UE is placed in the centre of cell close to the radiated SUT’s antenna(s). The minimum coupling loss (see Clause 4.5) shall not be exceeded. The change in radio conditions is achieved by moving the UE along the drive route out from cell centre to cell edge until UE loses the coverage (call drop) – see Figure 62.

# 4.82. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed under excellent radio condition (cell centre) using RSRP thresholds as indicated in Clause �.�. The UE is powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmission (see Clause �.�) from UE to the application server shall be verified. The UE under excellent radio conditions that is achieving peak user throughput should see stable utilization of the highest possible uplink MCS and uplink transport block size. These KPIs shall also be verified.

4. The UE shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer UDP data transmission from the application server to the UE is started. The application server shall receive data from the UE.

5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE, SUT and Application server sides using logging/measurement tools.

6. In the field setup, the UE is moved along the defined drive route out from cell centre (excellent radio conditions) to cell edge (poor radio conditions) on the main lobe of SUT’s antenna and with constant speed of around ��kph until UE loses the coverage (call drop).

7. In the lab setup, the attenuation between the antenna connectors of O-RU and UE is gradually increased until UE losses the coverage (call drop).

8. The capture of log data is stopped. The uplink full-buffer UDP data transmission from UE to the application server is stopped.

9. [Optional] Steps � to � are repeated for uplink full-buffer TCP data transmission.

4.83. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PUSCH BLER, PUSCH MCS (average sample per second) Transmit power on PUSCH (average sample per second) Transmitted uplink throughput (Application layer) (average sample per second) Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of allocated/occupied slots (average sample per second) • GPS coordinates (latitude, longitude) in the field setup

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

Initially when the UE is in the excellent radio conditions (cell centre), the stable utilization of the highest possible uplink MCS and uplink transport block size shall be observed and evaluated. The SUT shall also receive the data with the minimum uplink BLER. As the UE moves out from excellent radio conditions (cell centre), the radio conditions of the UE change gradually from excellent through good and fair to poor (see Clause 4.6). With deteriorating channel conditions and increasing path loss, SUT shall start experiencing worse PUSCH/PUCCH BLER. To compensate the path loss and limit PUSCH/PUCCH BLER, SUT shall command the UE to increate PUSCH/PUCCH transmit power through closed loop Transmit Power Control (TPC) feature. The number of HARQ retransmissions may be also increased. If the power control does not reduce PUSCH/PUCCH BLER bellow a threshold, SUT shall schedule UE with lower MCS and lower MIMO rank in uplink which results in lower uplink data throughput. The UE moving further away from SUT can cause radio link failure and call drop (due to UL Max RLC retransmissions, failure in CQI decoding, low uplink SINR, etc.) which results in triggering of RRC connection re-establishment procedure. Such a behavior shall be observed and evaluated.

Note that the test results can be affected by the various coverage enhancing features (e.g., transmit/receive diversity) at SUT and/or at UE sides. The used coverage enhancement features shall be also listed in the test report.

The following figures shall be included in the test report, and the behavior shall be evaluated. In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

• Received UDP uplink throughput (L� and Application layer) vs RSRP (all the samples as well as average curve with median values)

• Received UDP L� uplink spectral efficiency vs RSRP (all the samples as well as average curve with median values) PUSCH transmit power vs RSRP   
Cumulative distribution function of RSRP Cumulative distribution function of PUSCH MCS   
• Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs RSRP (all the samples as well as average curve with median values)

In the field environment, the cell coverage distance in meters (i.e., a straight line from the cell site) that corresponds to the cell-edge uplink application throughput of �.� Mbps for LTE and � Mbps for �G NR shall be recorded.

# 4.32. Downlink aggregated cell throughput (cell capacity)

# 4.84. Test description and applicability

The purpose of the test is to validate the downlink aggregated cell throughput (downlink cell capacity) when the UEs are distributed in a uniform or non-uniform way inside a cell. This test also captures the influence of MU-MIMO feature on aggregated cell throughput. However, the test does not require support of MU-MIMO or massive MIMO. The aggregated cell throughput depends on the multiple factors like spatial distribution of UEs inside a cell, radio conditions of UEs, test configuration supported by both UE and SUT, etc. The test covers two spatial distribution scenarios of test UEs, i.e., uniform distribution and non-uniform distribution.

# 4.85. Test setup and configuration

The test setup is a single cell scenario (i.e., an isolated cell without any inter-cell interference – see Clause 4.7) with 10 stationary UEs (real or emulated UEs) in total where 1 UE shall be placed in excellent radio conditions, 2 UEs in good radio conditions, 4 UEs in fair radio conditions and 3 UEs in poor radio conditions. The radio conditions are defined in Clause 4.6 – SINR (range of values) shall be considered in case of downlink. Note that in this case of single cell scenario, SINR is in fact SNR as inter-cell interferences are not present.

The UEs can be distributed in the following spatial distribution scenarios (see Figure 63):

a. uniform distribution: ten UEs are placed uniformly with a spatial separation in both horizontal and vertical directions. Uniform distribution maximizes the potential of MU-MIMO, because the spatially separated UEs can be served by different beams at the same time. The channel experienced by each UE is spatially uncorrelated which reduces the inter-beam interference. In addition, selecting orthogonal precoders will further reduce the inter-beam interference.

b. non-uniform distribution: the UEs are grouped in clusters. The UEs in the cluster experience very similar radio conditions. In addition, the UEs in the cluster cannot be spatially separated and served by different beams at the same time. This distribution scenario restricts the scheduling options of SUT resulting in lower aggregated cell throughput.

Figure 63 also shows impact of different types of beamforming (namely horizontal beamforming, vertical beamforming, and 3D beamforming) on aggregated cell throughput. The number of vertical beams is usually lower compared to horizontal beams, i.e., the number of UEs which can be spatially separated and served by different vertical beams at the same time is also lower resulting in lower aggregated cell throughput compared to horizontal beamforming. The typical scenario for vertical beamforming is a highrise building where each floor can be covered by different vertical beams. For example, in Figure 63 a), UEs 2 and 4 are located in the coverage of the same horizontal beam thus cannot be served at the same time, while in Figure 63 b), the same UEs 2 and 4 are located in the coverage of two different vertical beams thus can be served at the same time.

<table><tr><td>a) uniform distribution with horizontal beamforming</td><td>b) uniform distribution with vertical beamforming</td></tr><tr><td>c) uniform distribution with 3D beamforming</td><td>d) non-uniform distribution with horizontal</td></tr></table>

# Figure 6 SEQ Figure \\* ARABIC \s 1 3 The distribution scenarios of UEs inside the cell using horizontal, vertical or 3D beamforming

Within the cell there shall be 10 active UEs in total downloading data from the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/ core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UEs can be modified using a variable attenuator/fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. It is recommended to use a UE emulator to properly distribute the UEs inside a cell according to the selected distribution scenario. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The UEs shall be placed inside an RF shielded box or RF shielded room if the UEs are not connected via cables.

Field setup: The UEs shall be distributed inside a cell according to selected distribution scenario. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

# 4.86. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. Ten UEs (real or emulated) are placed inside a serving cell according to uniform distribution scenario, and in radio conditions using SINR thresholds as indicated in Clause �.� ‒ � UE shall be placed in excellent radio conditions, � UEs in good radio conditions, � UEs in fair radio conditions and � UEs in poor radio conditions. The UEs are powered on and attached to the network.

3. The downlink full-buffer UDP and TCP data transmissions (see Clause �.�) from the application server to all UEs shall be verified.

4. The UEs shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmissions from the application server to all UEs are started. All UEs shall receive the data from application server.

5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at all UEs and Application server using logging/measurement tools. The duration of the test shall be at least � minutes when the throughput is stable. The location and position of the

UEs shall remain unchanged during the entire measurement duration (capture of log data).

6. The capture of log data is stopped. The downlink full-buffer UDP data transmission from the application server to UEs is stopped.

7. [Optional] Steps � to � are repeated for downlink full-buffer TCP data transmissions.

8. [Optional] Non-uniform spatial distribution scenario of UEs is setup. Steps � to � are repeated.

# 4.87. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L� and Application layers) (average sample per second) Downlink transmission mode Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)   
• GPS coordinates (latitude, longitude) in the field setup

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

Table 611 gives an example of the test results record. The median and standard deviation shall be calculated from the captured samples for each metric). In case of 5G SA and NSA, SS-RSRP and SSSINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 11 Example record of test results (median and standard deviation is calculated from the captured samples)   

<table><tr><td colspan="1" rowspan="1">Spatial distribution scenario [uniform/non-uniform]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="2" rowspan="1">For each UE (UE 1 to UE 10) -</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UDP / [optional] TCP</td></tr><tr><td colspan="1" rowspan="1">Received L1 DL throughput [Mbps]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">L1 DL Spectral efficiency [bps/Hz]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">Received Application layer DL throughput[Mbps]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">UE RSRP [dBm]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">UE PDSCH SINR [dB]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">MIMO rank</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">PDSCH MCS</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">DL RB number</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="1" rowspan="1">PDSCH BLER [%]</td><td colspan="1" rowspan="1">median and standard deviation</td></tr><tr><td colspan="2" rowspan="1">For entire cell</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">UDP / [optional] TCP</td></tr><tr><td colspan="1" rowspan="1">Aggregated cell L1 DL throughput [Mbps]</td><td colspan="1" rowspan="1">sum of Received L1 DL throughputs – sum ofmedians (UE 1 to UE 10)</td></tr><tr><td colspan="1" rowspan="1">Aggregated cell Application layer DLthroughput [Mbps]</td><td colspan="1" rowspan="1">sum of Received Application layer DLthroughputs – sum of medians (UE 1 to UE 10)</td></tr><tr><td colspan="1" rowspan="1">Aggregated DL RB number</td><td colspan="1" rowspan="1">sum of DL RB numbers – sum of medians (UE1 to UE 10)</td></tr></table>

n addition, the used spatial distribution scenario(s) shall be properly described and depicted.

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• received aggregated UDP/TCP downlink throughput at UE side (L� and Application layers) vs Time duration [sec]

For each UE (UE� to UE��):

• UE PDSCH SINR vs Time duration [sec]   
• Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots vs Time duration [sec]

4.33. Uplink aggregated cell throughput (cell capacity)

# 4.88. Test description and applicability

The purpose of the test is to validate the uplink aggregated cell throughput (uplink cell capacity) when the UEs are distributed in a uniform or non-uniform way inside a cell. This test also captures the influence of MU-MIMO feature on aggregated cell throughput. The aggregated cell throughput depends on the multiple factors like spatial distribution of UEs inside a cell, radio conditions of UEs, test configuration supported by both UE and SUT, etc. The test covers two spatial distribution scenarios of test UEs, i.e., uniform distribution and non-uniform distribution.

# 4.89. Test setup and configuration

The test setup is a single cell scenario (i.e., an isolated cell without any inter-cell interference – see Clause 4.7) with 10 stationary UEs (real or emulated UEs) in total where 1 UE shall be placed in excellent radio conditions, 2 UEs in good radio conditions, 4 UEs in fair radio conditions and 3 UEs in poor radio conditions. The radio conditions are defined in Clause 4.6 – RSRP (range of values) shall be considered in case of uplink.

The UEs can be distributed in the following spatial distribution scenarios (see Figure 63):

a. uniform distribution: ten UEs are placed uniformly with a spatial separation in both horizontal and vertical directions. Uniform distribution maximizes the potential of MU-MIMO, because the spatially separated UEs can be served by different beams at the same time. The channel experienced by each UE is spatially un-correlated which reduces the inter-beam interference.

b. non-uniform distribution: the UEs are grouped in clusters. The UEs in the cluster experience very similar radio conditions. In addition, the UEs in the cluster cannot be spatially separated and served by different beams at the same time. This distribution scenario restricts the scheduling options of SUT resulting in lower aggregated cell throughput.

Within the cell there shall be 10 active UEs in total uploading data to the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/ core emulator via a transport link with sufficient capacity so as not to limit the expected data throughput. The test is suitable for both lab and field environments.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a fading generator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. It is recommended to use a UE emulator to properly distribute the UEs inside a cell according to selected distribution scenario. The minimum coupling loss (see Clause 4.6) shall not be exceeded. The UEs shall be placed inside an RF shielded box or RF shielded room if the UEs are not connected via cables.

Field setup: The UEs shall be distributed inside a cell according to selected distribution scenario. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

# 4.90. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. Ten UEs (real or emulated) in total are placed inside a serving cell according to uniform distribution scenario, and in radio conditions using RSRP thresholds as indicated in Clause �.� - � UE shall be placed in excellent radio conditions, � UEs in good radio conditions, � UEs in fair radio conditions and � UEs in poor radio conditions. The UEs are powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmissions (see Clause �.�) from all UEs to application server shall be verified.

4. The UEs shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer UDP data transmissions from all UEs to the application server are started. The application server shall receive data from all UEs.

5. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at all UEs, SUT and Application server using logging/measurement tools.

6. The capture of log data is stopped. The uplink full-buffer UDP data transmissions from the UEs to application server are stopped.

7. [Optional] Steps � to � are repeated for uplink full-buffer TCP data transmissions.

8. [Optional] Non-uniform spatial distribution scenario of UEs is setup. Steps � to � are repeated.

# 4.91. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for the performance assessment. UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per   
second)   
PUSCH BLER, PUSCH MCS (average sample per second)   
Transmit power on PUSCH (average sample per second)   
Transmitted uplink throughput (Application layer) (average sample per second)   
Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of allocated/occupied slots (average sample per second)   
GPS coordinates (latitude, longitude) in the field setup

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

Table 612 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G paths. The spectral efficiency (see Clause 4.8) shall be calculated for benchmarking and comparison to minimize the influence of different configured parameters such as bandwidth and TDD DL/UL ratio.

Table 6 SEQ Table \\* ARABIC \s 1 12 Example record of test results (median and standard deviation from the captured samples)   

<table><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="1">For each UE (UE 1 to UE 10)</td></tr><tr><td colspan="1" rowspan="1">UDP/TCP</td></tr><tr><td colspan="1" rowspan="1">Spatial distribution scenario [uniform/non-uniform]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Received L1 UL throughput [Mbps]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Aggregated cell L1 UL throughput [Mbps]S</td><td colspan="1" rowspan="1">sum of Received L1 UL throughput (UE 1 to UE10)</td></tr><tr><td colspan="1" rowspan="1">L1 UL Spectral efficiency [bps/Hz]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Received Application UL throughput [Mbps]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Aggregated cel App. UL throughput [Mbps]</td><td colspan="1" rowspan="1">sum of Received App. UL throughput (UE 1 toUE 10)</td></tr><tr><td colspan="1" rowspan="1">UE RSRP [dBm]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PDSCH SINR [dB]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PUSCH transmit power [dBm]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PUSCH MCS</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UL RB number</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Aggregated UL RB number</td><td colspan="1" rowspan="1">sum of UL RB number (UE 1 to UE 10)</td></tr><tr><td>PUSCH BLER [%]</td><td></td></tr></table>

In addition, the used spatial distribution scenario(s) shall be properly described and depicted.

The following figures shall be also included in the test report, and the stable behavior shall be observed and evaluated.

• received total UDP/TCP uplink throughput at Application server (L� and Application layers) vs Time duration

For each UE:

UE RSRP vs Time duration   
number of allocated/occupied uplink PRBs and Number of allocated/occupied slots   
vs Time duration

4.34. Impact of fronthaul latency on downlink peak throughput

# 4.92. Test description and applicability

The purpose of the test is to evaluate the user peak downlink throughput as a function of the fronthaul transport latency (i.e., one-way transmission delay between O-RU and O-DU at OpenFH (CUSM-plane interface), and to identify the maximum applicable fronthaul transport latency. Since the fronthaul transport latency corresponds with the distance (fiber length) between O-RU and O-DU, the results of test can be also used to identify the maximum distance (fiber length) with an acceptable degradation of user peak downlink throughput.

# 4.93. Test setup and configuration

The network setup is single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in the excellent radio condition as defined in Clause 4.6 - SINR shall be considered in case of downlink. Within the cell there shall be only one active UE downloading data from the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via transport link with sufficient capacity not limiting the expected data throughput. The test is suitable for lab as well as field environment.

The reference measurement points of the fronthaul latency (R1/R4 – Transmit/Receive interface at O-DU (CU-plane); R2/R3 – Receive/Transmit interfaces at O-RU (CU-plane)) [16] are shown in Figure 64. Transmission delay between O-RU and ODU are specified as T12 (downlink direction) and T34 (uplink direction). Transmission delay shall be symmetrical and equal in both directions. The transmission delay encompasses only the time from when a bit leaves the sender (R1/ R3) until it is received at the receiver (R2/ R4).

# Figure 6 SEQ Figure $^ { \backslash * }$ ARABIC $\bf \delta \ u$ 1 4 Definition of reference measurement points for fronthaul latency [16]

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal shall be set to achieve the excellent radio conditions (SINR as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (SINR as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

In this test, a method to vary the fronhaul latency shall be used. In both laboratory and field setups, Figure 65, the fronthaul latency may be modified by using of various lengths of fibre (assuming typical delay of fibre around 5 us per kilometre) or by using of a network impairment emulator inserted between O-RU and O-DU. It is necessary to know/measure the transmission delays produced by all fronthaul transport components between O-RU and O-DU to properly calculate the total fronthaul latency (T12/T34).

# Figure 6 SEQ Figure \\* ARABIC \s 1 5 The fronthaul transport latency test setups of 4G, 5G NSA and 5G SA

4.94. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed in the excellent radio condition (cell centre) as defined by SINR in Clause �.�. The UE is powered on and attached to the network.

3. The downlink full-buffer UDP and TCP data transmission (see Clause �.�) from the application server shall be verified. The excellent radio conditions experiencing peak user throughput is identified with stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank (number of layers). The utilization of these KPIs shall be also verified.

4. The fronthaul latency (one-way transmission delay between O-DU and O-RU) shall be set to its minimum value.

5. The UEs shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmission from the application server to the UE is started. The UE shall receive the data from application server.

6. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE and Application server using logging/measurement tools.

7. The capture of log data is stopped. The downlink full-buffer UDP data transmission from the UE to application server is stopped.

8. The fronthaul latency is increased by �� us if no degradation of user peak downlink throughput was observer in the previous measurement. As soon as a degradation of user peak downlink throughput will be observed, the fronthaul latency is increased only by � us to capture fine-grained log data.

9. Steps � to � are repeated until the total degradation of user peak downlink throughput is less than $3 0 \%$ . The KPIs measured with the minim fronthaul latency are used as a baseline $( 1 0 0 \% )$ for calculation of the degradation.

10.[Optional] Steps � to � are repeated for downlink full-buffer TCP data transmission.

# 4.95. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second)

• PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L�, and Application layers) (average sample per second)   
Downlink transmission mode Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second) GPS coordinates (latitude, longitude) in the field setup

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

When the UE is in the excellent radio conditions (cell centre), the stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank shall be observed and evaluated. The UE shall also receive the data with the minimum downlink BLER.

Table 613 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G.

# Table 6 SEQ Table \\* ARABIC \s 1 13 The example of record of test results (median and standard deviation from the captured samples)

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>For each measured fronthaul latency value</td></tr><tr><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Total fronthaul transport latency (T12/T34) [us]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Degradation of Received L1 DL throughput[%]#</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application DL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL PRB number</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td></tr></table>

# The “Received L1 DL throughput” measured with the minim fronthaul latency is used as a baseline $( 1 0 0 \% )$ for calculation of the degradation The following figures shall be also included in the test report.

• Received UDP/TCP downlink throughput (L� and Application layers) vs Total fronthaul latency (T��/T��)

# 4.35. Impact of fronthaul latency on uplink peak throughput

# 4.96. Test description and applicability

The purpose of the test is to evaluate the user peak uplink throughput as a function of the fronthaul transport latency (i.e., one-way transmission delay between O-RU and O-DU at OpenFH (CUSM-plane interface), and to identify the maximum applicable fronthaul transport latency. Since the fronthaul transport latency corresponds with the distance (fiber length) between O-RU and O-DU, the results of test can be also used to identify the maximum distance (fiber length) with an acceptable degradation of user peak uplink throughput.

# 4.97. Test setup and configuration

The network setup is single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in the excellent radio condition as defined in Clause 4.6 – RSRP shall be considered in case of uplink. Within the cell there shall be only one active UE uploading data to the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via transport link with sufficient capacity not limiting the expected data throughput. The test is suitable for lab as well as field environment.

The reference measurement points of the fronthaul latency (R1/R4 – Transmit/Receive interface at O-DU (CU-plane); R2/R3 – Receive/Transmit interfaces at O-RU (CU-plane)) [16] are shown in Figure 64. Transmission delay between O-RU and ODU are specified as T12 (downlink direction) and T34 (uplink direction). Transmission delay shall be symmetrical and equal in both directions. The transmission delay encompasses only the time from when a bit leaves the sender (R1/ R3) until it is received at the receiver (R2/ R4).

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal shall be set to achieve the excellent radio conditions (RSRR as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

In this test, a method to vary the fronhaul latency shall be used. In both laboratory and field setups, Figure 65, the fronthaul latency may be modified by using of various lengths of fibre (assuming typical delay of fibre around 5 us per kilometre) or by using of a network impairment emulator inserted between O-RU and O-DU. It is necessary to know/measure the transmission delays produced by all fronthaul transport components between O-RU and O-DU to properly calculate the total fronthaul latency (T12/T34).

# 4.98. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed in the excellent radio condition (cell centre) as defined by RSRP in Clause �.�. The UE is powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmission (see Clause �.�) from UE to the application server shall be verified. The excellent radio conditions experiencing peak user throughput is identified with stable utilization of the highest possible uplink MCS and uplink transport block size. The utilization of these KPIs shall be also verified.

4. The fronthaul latency (one-way transmission delay between O-DU and O-RU) shall be set to its minimum value.

5. The UEs shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer UDP data transmission from UE to the application server is started. The application server shall receive data from UE.

6. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE, SUT and Application server using logging/measurement tools.

7. The capture of log data is stopped. The uplink full-buffer UDP data transmission from application server to UE is stopped.

8. The fronthaul latency is increased by �� us if no degradation of user peak uplink throughput was observer in the previous measurement. As soon as a degradation of user peak uplink throughput will be observed, the fronthaul latency is increased only by � us to capture fine-grained log data.

9. Steps � to � are repeated until the total degradation of user peak uplink throughput is less than $30 \%$ . The KPIs measured with the minim fronthaul latency are used as a baseline $( 1 0 0 \% )$ for calculation of the degradation.

10. [Optional] Steps � to � are repeated for uplink full-buffer TCP data transmission.

# 4.99. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PUSCH BLER, PUSCH MCS (average sample per second)   
• Transmit power on PUSCH (average sample per second)   
• Transmitted uplink throughput (Application layer) (average sample per second) Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of allocated/occupied slots (average sample per second)   
• GPS coordinates (latitude, longitude) in the field setup

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

When the UE is in excellent radio condition (cell centre), the stable utilization of the highest possible uplink MCS and uplink transport block size shall be observed and evaluated. The SUT shall also receive the data with the minimum uplink BLER.

Table 614 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G.

Table 6 SEQ Table \\* ARABIC \s 1 14 The example of record of test results (median and standard deviation from the captured samples)   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>For each measured fronthaul latency value</td></tr><tr><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Total fronthaul transport latency (T12/T34) [us]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received L1 UL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Degradation of Received L1 UL throughput[%]#</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application UL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH transmit power [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH MCS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL PRB number</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH BLER [%]</td><td rowspan=1 colspan=1></td></tr></table>

# The “Received L1 UL throughput” measured with the minim fronthaul latency is used as a baseline $( 1 0 0 \% )$ for calculation of the degradation The following figures shall be also included in the test report.

• Received UDP/TCP uplink throughput (L� and Application layers) vs Total fronthaul latency (T��/T��)

# 4.36. Impact of midhaul latency on downlink peak throughput

# 4.100. Test description and applicability

The purpose of the test is to evaluate the user peak downlink throughput as a function of the midhaul transport latency (i.e., one-way transmission delay between O-DU and O-CU at F1 interface). Since the midhaul transport latency corresponds with the distance (fiber length) between O-DU and O-CU, the results of test can be also used to identify the maximum distance (fiber length) with an acceptable degradation of user peak downlink throughput. Note that the midhaul transport exists only if O-DU and O-CU are not a combined entity, and the interface F1 between O-DU and O-CU is exposed. The test does not support LTE network architecture because an interface providing means for interconnecting LTE ODU/DU and LTE CU has not been specified yet neither in 3GPP nor in O-RAN ALLIANCE. Note that W1 interface [33] has been specified only for 5G NSA Options 4 and 7 network architectures. The test is suitable only for 5G NSA (Option $3 / 3 \mathrm { a } / 3 \mathrm { x } )$ ) and 5G SA network architectures as defined in 4.

# 4.101. Test setup and configuration

The network setup is single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in the excellent radio condition as defined in Clause 4.6 - SINR shall be considered in case of downlink. Within the cell there shall be only one active UE downloading data from the application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via transport link with sufficient capacity not limiting the expected data throughput. The test is suitable for lab as well as field environment. The midhaul latency encompasses only the time from when a bit leaves O-CU until it is received at O-DU.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal shall be set to achieve the excellent radio conditions (SINR as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (SINR as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

In this test, a method to vary the midhaul transport latency shall be used. In both laboratory and field setups, Figure 66, the midhaul transport latency may be modified by using of a network impairment emulator or fiber spool or etc., inserted between O-DU and O-CU. It is necessary to know/measure the transmission delays produced by all midhaul transport components between O-DU and O-CU to properly calculate the total midhaul latency.

# Figure 6 SEQ Figure \\* ARABIC \s 1 6 The midhaul transport latency test setups of 5G NSA and 5G SA

# 4.102. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed in the excellent radio condition (cell centre) as defined by SINR in Clause �.�. The UE is powered on and attached to the network.

3. The downlink full-buffer UDP and TCP data transmission (see Clause �.�) from the application server shall be verified. The excellent radio conditions experiencing peak user throughput is identified with stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank (number of layers). The utilization of these KPIs shall be also verified.

4. The midhaul latency (one-way transmission delay between O-DU and O-CU) shall be set to its minimum value.

5. The UEs shall be turned off or set to airplane mode, to empty the buffers. The downlink full-buffer UDP data transmission from the application server to UE is started. The UE shall receive the data from application server.

6. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE and Application server using logging/measurement tools.

7. The capture of log data is stopped. The downlink full-buffer UDP data transmission from application server is stopped.

8. The midhaull latency is increased by ���� us if no degradation of user peak downlink throughput was observer in the previous measurement. As soon as a degradation of user peak downlink throughput will be observed, the midhaul latency is increased only by ��� us to capture fine-grained log data.

9. Steps � to � are repeated until the total degradation of user peak downlink throughput is less than $3 0 \%$ . The KPIs measured with the minim fronthaul latency are used as a baseline $( 1 0 0 \% )$ for calculation of the degradation.

10. [Optional] Steps � to � are repeated for downlink full-buffer TCP data transmission.

# 4.103. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L�, and Application layers) (average sample per second) Downlink transmission mode Channel utilization, i.e., Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)   
• GPS coordinates (latitude, longitude) in the field setup

Application server side:

• Transmitted downlink throughput (Application layer) (average sample per second)

When the UE is in the excellent radio conditions (cell centre), the stable utilization of the highest possible downlink MCS, downlink transport block size and downlink MIMO rank shall be observed and evaluated. The UE shall also receive the data with the minimum downlink BLER.

Table 615 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G.

# Table 6 SEQ Table \\* ARABIC \s 1 15 The example of record of test results (median and standard deviation from the captured samples)

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>For each measured midhaul latency value</td></tr><tr><td rowspan=1 colspan=1>UDP/TCP</td></tr><tr><td rowspan=1 colspan=1>Total midhaul transport latency [us]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Degradation of Received L1 DL throughput[%]#</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application DL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL PRB number</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td></tr></table>

# The “Received L1 DL throughput” measured with the minim fronthaul latency is used as a baseline $( 1 0 0 \% )$ for calculation of the degradation The following figures shall be also included in the test report.

• Received UDP/TCP downlink throughput (L� and Application layers) vs Total midhaul latency.

# 4.37. Impact of midhaul latency on uplink peak throughput

# 4.104. Test description and applicability

The purpose of the test is to evaluate the user peak uplink throughput as a function of the midhaul transport latency (i.e., one-way transmission delay between O-DU and O-CU at F1 interface). Since the midhaul transport latency corresponds with the distance (fiber length) between O-DU and O-CU, the results of test can be also used to identify the maximum distance (fiber length) with an acceptable degradation of user peak uplink throughput. Note that the midhaul transport exists only if O-DU and OCU are not a combined entity, and the interfaces between O-DU and O-CU are exposed. The test does not support LTE network architecture because an interface providing means for interconnecting LTE O-DU/ DU and LTE CU has not been specified yet neither in 3GPP nor in O-RAN ALLIANCE. Note that W1 interface [33] has been specified only for 5G NSA Options 4 and 7 network architectures. The test is suitable only for 5G NSA (Option $3 / 3 \mathrm { a } / 3 \mathrm { x } $ ) and 5G SA network architectures as defined in 4.

# 4.105. Test setup and configuration

The network setup is single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with stationary UE (real or emulated UE) placed in the excellent radio condition as defined in Clause 4.6 - RSRP shall be considered in case of uplink. Within the cell there shall be only one active UE uploading data to application server. The application server shall be placed as close as possible to the core/core emulator and connected to the core/core emulator via transport link with sufficient capacity not limiting the expected data throughput. The test is suitable for lab as well as field environment. The midhaul latency encompasses only the time from when a bit leaves O-DU until it is received at O-CU.

Test configuration: The test configuration is not specified. The utilized test configuration (parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions of UE can be modified by a variable attenuator/fading generator inserted between the antenna connectors of O-RU and UE. The minimum attenuation of radio signal shall be set to achieve the excellent radio conditions (RSRP as defined in Clause 4.6), but the minimum coupling loss (see Clause 4.6) shall not be exceeded. The UE shall be placed inside RF shielded box or RF shielded room if the UE is not connected via cable.

Field setup: The UE is placed in the centre of cell close to the radiated SUT’s antenna(s), where excellent radio conditions (RSRP as defined in Clause 4.6) shall be observed. The minimum coupling loss (see Clause 4.6) shall not be exceeded.

In this test, a method to vary the midhaul transport latency shall be used. In both laboratory and field setups, Figure 66, the midhaul transport latency may be modified by using of a network impairment emulator or fiber spool or etc., inserted between O-DU and O-CU. It is necessary to know/measure the transmission delays produced by all midhaul transport components between O-DU and O-CU to properly calculate the total midhaul latency.

# 4.106. Test procedure

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are turned off.

2. The UE (real or emulated) is placed in the excellent radio condition (cell centre) as defined by RSRP in Clause �.�. The UE is powered on and attached to the network.

3. The uplink full-buffer UDP and TCP data transmission (see Clause �.�) from UE to the application server shall be verified. The excellent radio conditions experiencing peak user throughput is identified with stable utilization of the highest possible uplink MCS and uplink transport block size. The utilization of these KPIs shall be also verified.

4. The midhaul latency (one-way transmission delay between O-DU and O-CU) shall be set to its minimum value.

5. The UEs shall be turned off or set to airplane mode, to empty the buffers. The uplink full-buffer UDP data transmission from UE to application server is started. The application server shall receive the data from UE.

6. All the required performance data (incl. the signalling and control data) as specified in the following “Test requirements” clause is measured and captured at UE, SUT and Application server using logging/measurement tools.

7. The capture of log data is stopped. The uplink full-buffer UDP data transmission from the UE to application server is stopped.

8. The midhaull latency is increased by ���� us if no degradation of user peak uplink throughput was observer in the previous measurement. As soon as a degradation of user peak uplink throughput will be observed, the midhaul latency is increased only by ��� us to capture fine-grained log data.

9. Steps � to � are repeated until the total degradation of user peak uplink throughput is less than $30 \%$ . The KPIs measured with the minim fronthaul latency are used as a baseline $( 1 0 0 \% )$ for calculation of the degradation.

10. [Optional] Steps � to � are repeated for uplink full-buffer TCP data transmission.

# 4.107. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be recorded and reported for the performance assessment.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, CQI, PDSCH SINR (average sample per second) PUSCH BLER, PUSCH MCS (average sample per second)   
• Transmit power on PUSCH (average sample per second)   
• Transmitted uplink throughput (Application layer) (average sample per second) Channel utilization, i.e., Number allocated/occupied uplink PRBs and Number of allocated/occupied slots (average sample per second)   
• GPS coordinates (latitude, longitude) in the field setup

SUT side (if capture of logs is possible):

• Radio parameters such as PUSCH SINR (average per second) • PUSCH BLER (average per second)

Application server side:

• Received uplink throughput (L� and Application layers) (average sample per second)

When the UE is in excellent radio condition (cell centre), the stable utilization of the highest possible uplink MCS and uplink transport block size shall be observed and evaluated. The SUT shall also receive the data with the minimum uplink BLER.

Table 616 gives an example of the test results record (median and standard deviation from the captured samples shall be calculated for each metric). In case of 5G SA and NSA, SS-RSRP and SS-SINR shall be reported. In case of 5G NSA and dual connectivity (EN-DC), the values shall be provided separately for both LTE and 5G.

# Table 6 SEQ Table \\* ARABIC \s 1 16 The example of record of test results (median and standard deviation from the captured samples)

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>For each measured midhaul latency value</td></tr><tr><td rowspan=1 colspan=1>UDP /TCP</td></tr><tr><td rowspan=1 colspan=1>Total midhaul transport latency [us]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received L1 UL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Degradation of Received L1 UL throughput[%]#</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Received Application UL throughput [Mbps]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH transmit power [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UL PRB number</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PUSCH BLER [%]</td><td rowspan=1 colspan=1></td></tr></table>

# The “Received L1 UL throughput” measured with the minim fronthaul latency is used as a baseline $( 1 0 0 \% )$ for calculation of the degradation The following figures shall be also included in the test report.

• Received UDP/TCP uplink throughput (L� and Application layers) vs Total midhaul latency.

# 7. Services tests

# 4.38. Services tests introduction

As a part of O-RAN testing, the present document is aimed at ensuring the O-RAN system can work in a telecom network, by inter-working with the other sub-systems to provide End-to-End services. This clause of the document outlines the services which should be tested to validate that the O-RAN system can be deployed and optimized to deliver great end user service experience in a telecom network.

The services which need to be tested are broadly classified as data service(s), video streaming service(s), voice service(s), video calling service(s) in the eMBB slice a\`nd services supported using other slices like URLLC and mMTC. This clause of the document also tests different scenarios, such as handover, and different radio conditions, to assess the impact of these scenarios on the end user service(s) experience.

# 4.39. Data services tests

# 7.1.0 Data services test introduction

Data services form one of the basic services supported as of today on a telecom network. This usage includes everything from web browsing, uploading/downloading content, to traffic generated by all the different applications on the end user device. These services form an integral part of data traffic on a telecom network. This clause is comprised of two test scenarios, which include web browsing and file upload/download.

Along with the monitoring and validation of these services through user experience KPIs, the O-RAN systems should also be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been listed below. As a part of the data services testing, details of these features shall be included in the test report to provide a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user experience, those shall be included in the test report as well.

• Control Channel Beamforming   
Connected Mode DRX Massive MIMO Coordinated Multi Point (DL and UL) ���QAM Support (DL and UL) SSB Power Boost Beam Management DL Common Channel Beamforming Single-User MIMO Beamforming (DL and UL) Multi-User MIMO Beamforming (DL and UL) Single-User MIMO, TM Switching Multi-User MIMO, TM Switching TDD configuration support RAN Slicing Framework (NR Low/Mid/High) RACH Enhancements (PRACH Format �) PF (Proportional Fairness) Scheduling QoS Scheduling Minimal Bit Rate Scheduling Link Adaptation (DL and UL) Uplink Data Compression UDC   
PUSCH Frequency Hopping

Refer to the summary table below for a list of test cases and applicable technology.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 11: Data Service Test Case summary

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>TestID</td><td rowspan=1 colspan=1>Data service</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.1.1</td><td rowspan=1 colspan=1>Web Browsing</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.1.2</td><td rowspan=1 colspan=1>File upload/download</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.108. Web Browsing

# 7.1. Test Description

Web browsing forms an integral part of the 4G and 5G data network traffic, and this test case is applicable to both NSA and SA deployments. The testing shall be performed for each applicable technology supported by the system under test, according to table 7-34. HTTP is the protocol used for web browsing and this protocol can be transported over TCP/TLS or UDP/QUIC. These tests will include scenarios which will include both these protocols. Testing may be performed using HTTP/TLS/TCP or HTTP/ QUIC/UDP or both these protocols as applicable.

Web browsing KPI

DNS Resolution time – Time measured from when the client sends a DNS query to when the DNS responds with an IP address in milliseconds/seconds. This KPI should be recorded if DNS is used.   
Time To First Byte (TTFB) – Time measured from when the client makes the HTTP request to when the first byte of the page is received in milliseconds/seconds. Page Load Time – Time measured from when the client places the request to when the page is completely loaded in seconds.

# 7.2. Test Setup

The SUT in this test case shall be O-eNB along with O-RU, O-DU and O-CU-CP/O-CU-UP for NSA deployments or the O-RU, O-DU and O-CU-CP/O-CU-UP for SA deployments. The O-RAN setup should support the ability to perform this testing in different radio conditions as defined in Clause 4.6. The 4G/5G core will be required to support the basic functionality to authenticate and register an end user device and to setup a PDN connection/PDU session. The 4G core will be used for O-RAN NSA testing, whereas 5G core will be used for O-RAN SA testing. The 4G/5G core may be a completely emulated, partially emulated or a real non-emulated core. The application server should support web browsing and be accessible from the 4G/5G core. This application server(s) should support protocols, such as HTTP/ TCP or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This could be a built-in capability of the emulated/nonemulated network elements and end user device(s) or external tool(s). If some of the network elements or application servers arelocated remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP shall have the correct configuration and software load. Tools which emulate latency shall be used and configured on the O-RAN system (between O-RU, O-DU and O-CU-CP/O-CU-UP) to emulate real-world deployment conditions as applicable. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 4G/5G core. The end user device also shall be provisioned with the correct application, such as the web browser to perform the tests. The 4G/5G core network shall be configured to support the end user device used for testing. This includes supporting registration, authentication and PDN connection/PDU session establishment for this end user device. The application server should be configured to support web browsing, along with support for HTTP/TCP and/or HTTP/QUIC protocols as applicable. Web browsing has several variables which can impact the KPIs and in order to reduce the impact of these variables and make the test outcomes consistent, it is recommended to set up a static web page of ${ \sim } 1 . 8 { \cdot } 2 \mathrm { M B }$ size. The size of the web page is comparable to the average size of web pages on the public Internet. A static web page shall not change the content on repeated requests, thus making the test results consistent and repeatable. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network, including the O-RAN system, 4G/5G core, and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the web browsing KPIs.

Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system, which shall be connected to the 4G/5G core which in turn shall have connectivity to the application server.

# 7.3.

# Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G/5G core and the application server have all been configured as outlined in Clause 7.1.1.2. All traces and packet captures need to be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device in excellent radio condition and ensure it registers with the �G/�G core for data services.   
2. Once the registration is complete, the end user device shall establish a PDU session with the �G core (SA) or PDN connection with the �G core (NSA).   
3. Open the browser or application on the end user device and start a web browsing session to a web content using HTTP/TCP and/or HTTP/QUIC protocol. If the intent is to execute this test case for both protocols, then this step shall be performed twice, once for web content using HTTP/TCP followed by web content using HTTP/QUIC protocol.   
4. Validate the end user can get the content from the application server and view it on the end device. For every test collect the KPIs included in Clause �.�.�.�.   
5. Clear the browser cache on the end user device between tests.   
6. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.   
7. Repeat the above steps � through � for the good, fair and poor radio conditions.

# 7.4.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection/PDU session setup by the end user device without any errors. This is a prerequisite before these tests can be validated. The end user device may be able to view the web browsing content for the web browsing test, with the content being viewable and readable. Use the packet captures to validate there is no packet drop or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

Calculate the web browsing KPIs included in Clause 7.1.1.1 and include it in the test report. In a lab setup, the use of DNS may be bypassed by using IP Addresses instead of domain names. However, the DNS resolution time KPI shall be recorded if a DNS is used for testing. The average range of values for these KPIs are included below for guidance, taking into consideration the size of the web page $( \sim 2 \mathrm { M B } )$ . These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add additional latency and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

DNS Resolution time (conditional mandatory) – < 1 second • Time To First Byte $( \mathsf { T } \mathsf { T } \mathsf { F } \mathsf { B } ) \mathrm { ~ - ~ } ^ { \angle } 3$ seconds Page Load Time – $< 1 2$ seconds

As a part of gathering test data and reporting, ensure the minimum configuration parameters (see Clause 4.3) are included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

End user device side (real or emulated):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second)

• Received downlink throughput for the duration of the page download (L1 and L3 PDCP layers) (average sample per second)

• Downlink transmission mode

Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash \ast$ ARABIC \s 12 Example of Test Report for Web Browsing Testing   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>HTTP overTCP/QUIC</td><td rowspan=1 colspan=1>HTTP overTCP/QUIC</td><td rowspan=1 colspan=1>HTTP overTCP/QUIC</td><td rowspan=1 colspan=1>HTTP overTCP/QUIC</td></tr><tr><td rowspan=1 colspan=1>DNS Resolution Time(Conditional mandatory)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Time To First Byte (TTFB)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page Load Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L3 DL PDCP throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Application DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The web browsing experience can also be impacted by some of the features available (see Clause 7.1) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which could impact the end user’s web browsing experience should be included in the test report to provide a comprehensive view of the testing.

# 4.109. File upload/download

7.5. Test Description

File Transfer Protocol (FTP) is a simple application layer protocol used to transfer file between remote locations. FTP, along with different flavours of the protocols, form one of the fundamental methods to upload/download a file on the internet. This test case is applicable to both NSA and SA deployments and shall be performed twice, once for NSA deployment and once for SA deployment as applicable. This

scenario tests the end user experience to upload/download files to/from an FTP server over an O-RAN system. The KPIs used to measure the user experience have been included below

7.1. Download throughput ‒ This is the average application layer throughput to download the file in kbps   
7.2. Upload throughput ‒ This is the average application layer throughput to upload the file in kbps.   
7.3. Time taken to Download file ‒ This is the time required to download the file in seconds.   
7.4. Time taken to Upload file ‒ This is the time required to upload the file in seconds.

# 7.6. Test Setup

The SUT in this test case would be O-eNB along with O-RU, O-DU and O-CU-CP/O-CU-UP for NSA deployments or the O-RU, O-DU and O-CU-CP/O-CU-UP for SA deployments. The O-RAN setup should support the ability to perform this testing in different radio conditions as defined in Clause 4.6. A 4G/5G core will be required with the basic functionality to authenticate and register an end user device and to setup a PDN connection/PDU session. The 4G core will be used for O-RAN NSA testing, whereas 5G core will be used for O-RAN SA testing. The 4G/5G core may be a completely emulated, partially emulated or a real non-emulated core. An FTP server acts as an application server for this test case. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This could be a built-in capability of the emulated/non-emulated network element(s) or external tool(s). Optionally, if some of the network elements are located remotely, either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP shall have the correct configuration and software load. Tools which emulate latency shall be used and configured on the O-RAN system (between O-RU, O-DU and O-CU-CP/O-CU-UP) to emulate real-world deployment conditions. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 4G/5G core. The end user device also shall be provisioned with the correct application, such as an FTP client, to upload and download files. The 4G/5G core network shall be configured to support the end user device used for testing. This includes supporting registration, authentication and PDN connection/PDU session establishment for this end user device. The FTP server should host large files $( > 1$ GB) which can be used for the download/upload testing. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network, such as the O-RAN system, 4G/5G core and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the file upload/download KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system, which shall be connected to the 4G/5G core which in turn shall have connectivity to the application server.

# 7.7.

# Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G/5G core and the FTP server have all been configured as outlined in Clause 7.1.2.2. All traces and packet captures need to be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device in excellent radio condition and ensure it registers with the �G/�G core for data services.   
2. Once the registration is complete, the end user device shall establish a PDU session with the �G core (SA) or PDN connection with the �G core (NSA).   
3. Open the application on the end user device and upload the test file to the FTP server. Make a note of the time taken to upload the file and the average upload throughput.   
4. Next use the same application on the end user device to download a different test file from the FTP server. Make a note of the time taken to download the file and the average download throughput.   
5. Clear all the buffers and caches on the client and the server. Delete the test files ‒ downloaded file on the client and the uploaded file on the FTP server.   
6. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.   
7. Repeat the above steps � through � for the good, fair and poor radio conditions.

# 7.8.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection/PDU session setup by the end user device without any errors. This is a prerequisite before these tests can be validated. Validate the end user device can upload/download the complete file to/from the FTP server without interruption. Validate there isn’t a drop in throughput while uploading/downloading the file to/from the FTP server. Use the packet captures to validate there is no packet drop or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system. Calculate the file upload/download KPIs included in Clause 7.1.1.1 and include them in the test report. There are no target values for these KPIs as they are dependent on multiple factors used in the test configuration. Some comments on each of the KPIs are included below.

Download throughput ‒ This value should be comparable to the results of the downlink throughput test performed in Clause �.� and Clause �.�.   
Upload throughput ‒ This value should be comparable to the results of the uplink throughput test performed in Clause �.� and Clause �.�.   
Time taken to Download file ‒ This value should be comparable to the value calculated using the formula included below   
Time taken to Upload file ‒ This value should be comparable to the value calculated using the formula included below.

These KPI values included in Clause 7.1.2.1 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
• Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table \\* ARABIC \s 13 Example Test Report for File Upload/Download Testing

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>FileUpload/Download</td><td rowspan=1 colspan=1>FileUpload/Download</td><td rowspan=1 colspan=1>FileUpload/Download</td><td rowspan=1 colspan=1>FileUpload/Download</td></tr><tr><td rowspan=1 colspan=1>Upload/Download Throughput(kbps)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Time taken to Upload/DownloadFile</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L3 DL PDCP throughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Application DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>]</td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>]</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>]</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>]</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The file upload/download experience can also be impacted by some of the features available (see Clause 7.1) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which could impact the end user’s web browsing experience should be included in the test report to provide a comprehensive view of the testing.

# 4.40. Video streaming tests

# 7.2.0 Video streaming tests introduction

Video makes up a major part of the internet traffic today and there is a similar trend even on the mobile data traffic. Mobile video accounts for close to two-thirds of the total mobile data traffic and is expected to increase in the coming years. Video streaming has evolved over time with newer and better audio and video codecs. The protocols used to stream the video packets has also been evolving over time, with Adaptive Bit Rate (ABR) being the most common protocol used for streaming video on the internet today. There are multiple flavours of ABR, but at the crux they all use HTTP protocol over TCP/TLS or UPD/ QUIC to transfer audio-video packets to a client. A video streaming server which supports ABR hosts multiple versions of the same video content with each version of the video being encoded at different resolution and quality, hence different bit rates. The client uses the ABR protocol to get the list of all available versions of the requested video content and picks the best video content based on the available bandwidth on the client side. The ABR client continuously monitors the network condition and dynamically adjusts the quality and resolution of the video stream to match the available bandwidth. The ABR protocol provides the user with the best video streaming experience based on the available bandwidth between the client and the content server. This however adds a lot of variables to the streaming session

An ABR client may start with a lower resolution video and progressively switch to higher resolution video as it better estimates the bandwidth available at the client. An ABR client might notice an improvement in the bandwidth and request a higher resolution/quality video content, thus improving the video quality mid-stream. An ABR client might notice a degradation in the bandwidth and request a lower resolution/quality video content, thus deteriorating the video quality mid-stream.

These variables make it challenging to quantify the video streaming experience of an end user. There have been many tools and organizations which have defined different methods and algorithms to quantify the end user experience including QoE (Quality of Experience), SVQ (Streaming Video Quality), Video Multimethod Assessment Fusion (VMAF) etc. In this document we recommend using the Mean Opinion Score (MOS) as defined by ITU P.1203.3 to quantify the quality of experience of the end user. This mechanism however limits the testing to H.264 video encoder with a resolution of HD quality (1080p resolution – $1 9 2 0 \mathrm { ~ x ~ } 1 0 8 0$ pixels) or below.

Video Streaming KPIs

Video start time or Time to load first video frame – Time from when the video was selected to play to when the video starts playing in seconds.   
Number of video stalls/buffering (Optional) – Number of times the video stalled or started buffering during the course of video streaming. This KPI has already been considered by ITU P.1203.3 to provide a cumulative MOS score.   
Duration of stalls in the video (Optional) – The cumulative duration of all the stalls during the course of video streaming in seconds. This KPI has already been considered by ITU P.1203.3 to provide a cumulative MOS score.   
Video MOS score – MOS score for the video streaming session as defined by ITU P.1203.3.

Along with the monitoring and validation of these services using user experience KPIs, the O-RAN systems also shall be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been included in the list below. As a part of the video streaming testing, details of these features shall be included in the test report to provide a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user experience, those shall be included in the test report as well.

• NR to LTE PS Redirection/Cell Reselection/Handover Intra-frequency / Inter-Frequency Cell Reselection/Handover NR Coverage-Triggered NR Session Continuity   
• LTE-NR & NR-NR Dual Connectivity and NR Carrier Aggregation Direct data forwarding between NG-RAN and E-UTRAN nodes for inter-system mobility Standard QCI Bearers Support   
• Control Channel Beamforming Massive MIMO   
���QAM Support (DL and UL)   
• Beam Management

• TDD configuration support • PF (Proportional Fairness) Scheduling • Link Adaptation (DL and UL) • Application Aware QoS

lease see below summary table of test cases and applicable technology.

Table 7SEQ Table \\* ARABIC \s 14: Video Streaming Service Test Case Selection summary

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Video Streaming</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.2.1</td><td rowspan=1 colspan=1>Video Streaming – Stationary Test</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.2.2</td><td rowspan=1 colspan=1>Video Streaming – Handover between sameMaster eNB but different O-RUs – Intra O-DU</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.2.3</td><td rowspan=1 colspan=1>Video Streaming – Handover between same MeNBbut different O-DUs – Inter O-DU Intra O-CU</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.2.4</td><td rowspan=1 colspan=1>Video Streaming – Handover between same MeNBbut different O-CUs – Inter O-CU</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.2.5</td><td rowspan=1 colspan=1>Video Streaming – Handover between differentMeNB while staying connected to same SgNB</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td></tr></table>

# 4.110. Video Streaming – Stationary Test

# 7.2.1.0

# Test Overview

This scenario tests the video experience of a user streaming video over 4G and 5G network when the end user device is stationary.

# 7.9.

Test Description

Majority of the video streaming on the internet today uses ABR (Adaptive Bit Rate) streaming using HTTP protocol over TCP/TLS or UDP/QUIC. Within this test, the user’s video streaming experience when connected to a telecom network over O-RAN system. This test case is applicable to both NSA and SA deployment, and will shall be performed twice, once for NSA deployment and once for SA deployment as applicable.

7.10. Test Setup

The SUT in this test case would be 4G O-eNB along with 5G E2E system (O-RU, O-DU and O-CU-CP/ O-CU-UP) for NSA deployments or the 5G E2E system (O-RU, O-DU and O-CU-CP/O-CU-UP) for SA deployments. The O-RAN setup should support the ability to perform this testing in different radio conditions as defined in Clause 4.6. A 4G/5G core will be required to support the basic functionality to authenticate and register an end user device in order to setup a PDN connection/PDU session. The 4G core will be used for O-RAN NSA testing, whereas 5G core will be used for O-RAN SA testing. The 4G/ 5G core may be a completely emulated, partially emulated or a real non-emulated core. The application server(s) for this testing should support video streaming using ABR protocol over HTTP/TCP and/or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This could be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements or the application server are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-eNB and (O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the correct configuration and software load. Tools which emulate latency shall be used and configured on the O-RAN system (between O-RU, O-DU and O-CU-CP/O-CU-UP) to emulate real-world deployment conditions. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 4G/5G core. The end user device also shall be provisioned with the correct application, such as a video streaming client, to perform the tests. The 4G/5G core network shall be configured to support the end user device used for testing. This includes supporting registration, authentication, and PDN connection/PDU session establishment for this end user device. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell. All the elements in the network, including the O-RAN system, 4G/5G core, and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the video streaming KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system, O-RAN system shall be connected to the 4G/5G core which in turn shall have connectivity to the application server.

# 7.11.

# Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G/5G core and the application server have all been configured as outlined in Clause 7.2.1.2. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device in excellent radio condition and ensure it registers with the �G/�G core for data services.   
2. Once the registration is complete, the end user device shall establish a PDN Session with the �G core or PDU session with the �G core.   
3. Open the video streaming client on the end user device and start a video streaming session over HTTP/TCP protocol and let the video stream for at least ��� seconds.   
4. Optionally, repeat the test by streaming a video session over the HTTP/QUIC protocol and stream the video content for at least ��� seconds.   
5. Repeat the test multiple times $( > 1 0$ times) and gather results.   
6. Repeat the above steps � through � for the good, fair and poor radio conditions.

# 7.12.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection/PDU session setup by the end user device without any errors. This is a prerequisite before these tests can be validated. Validate the end user device can start streaming the video without delays and watch the video content. Ensure the video can stream without stalls or intermittent buffering. Use the packet captures to validate there is no packet drop or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

• Video Start time or Time to load first video frame – \~1.5 seconds   
• Number of video stalls/buffering – $< 1$   
• Duration of stalls in the video – $< 5$ seconds Video MOS Score $\underline { { \mathbf { \Pi } } } > 3 . 5$

The values for the end user video streaming KPIs defined in Clause 7.2 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed in different radio conditions to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of al test results that have been captured.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 15 Example Test Report for Video Streaming – Stationary Test   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>VideoStreaming overTCP/QUIC</td><td rowspan=1 colspan=1>VideoStreaming overTCP/QUIC</td><td rowspan=1 colspan=1>VideoStreaming overTCP/QUIC</td><td rowspan=1 colspan=1>VideoStreaming overTCP/QUIC</td></tr><tr><td rowspan=1 colspan=1>Video Start Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Number of Video Stalls/buffering</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Duration of stalls in the video</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Video MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user video streaming experience can also be impacted by some of the features available (see Clause 7.2) on the 4G O-eNB and 5G system (O-RU, O-DU and O-CU-CP/O-CU-UP). The details of these features, along with any other features/functionality which could impact the end user’s video streaming experience should be included in the test report to provide a comprehensive view of the testing

4.111. Video Streaming – Handover between same Master eNB but different O-RUs – Intra O-DU

This test scenario validates the user’s video streaming experience when the end user device (UE) is connected over NSA to a 4G core and is in the process of a handover between two O-RAN subcomponents (two O-RUs) on the Secondary $\mathsf { g N B }$ while remaining connected to the same Master eNB. The VoLTE or VoNR services cannot be used to test handover of secondary gNB, video streaming is used for this testing. This test scenario is only applicable in an NSA deployment.

# 7.13. Test Description

The 5G O-RAN system has multiple sub-components, including the O-RU, O-DU and the O-CU-CP/OCU-UP. This setup leads to multiple handover scenarios when the O-RAN system is connected as a Secondary gNB in an NSA deployment. This scenario tests the end user’s video streaming experience when the end user device is connected over NSA to the 4G core and performs a handover between O-RUs which are connected to the same O-DU (and O-CU-CP/O-CU-UP) on the Secondary gNB – Intra-O-DU handover. The end user device remains connected to the same Master eNB through the entire handover process. This handover is agnostic to the 4G core as the handover occurs on the O-RAN system. This test assesses the impact of the video streaming service on the end user device in this handover scenario by monitoring the end user video streaming KPIs included in Clause 7.2. This test case streams video using ABR protocol over HTTP/TCP and/or HTTP/QUIC.

# 7.14. Test Setup

The SUT in this test case are the Master eNB and a Secondary gNBs. The Master eNB will be an O-eNB and the Secondary gNB will constitute of a pair of O-RUs – O-RU1 and O-RU2, which will connect to the same O-DU and O-CU-CP/O-CU-UP. The O-eNB, O-RUs, O-DU and O-CU-CP/O-CU-UP shall comply with the O-RAN specifications. A 4G core will be required to support the basic functionality to authenticate and register an end user device, to set up a PDN connection. The 4G core may be a completely emulated, partially emulated or a real non-emulated core. The application server(s) for this testing should support video streaming using ABR protocol over HTTP/TCP and/or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This could be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements or application server(s) are located remotely, either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-eNB shall have the correct configuration and software load. The pair of O-RUs (O-RU1 and ORU2) shall be connected to the O-DU and O-CU-CP/O-CU-UP and all the components shall have the correct configuration and software load. Tools which emulate latency shall be used and configured on the O-RAN system (between O-RU, O-DU and O-CU-CP/O-CU-UP) to emulate real-world deployment conditions. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 4G core. The end user device also shall be provisioned with the correct application, such as a video streaming client to perform the tests. The 4G core network shall be configured to support the end user device used for testing. This includes supporting registration, authentication and PDN connection establishment for this end user device.

All the elements in the network, including the O-RAN system, 4G core, and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the video streaming KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNB, O-RUs, O-DU and OCU-CP/O-CU-UP), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the application server.

# 7.15. Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G core, and the application server have all been configured as outlined in Clause 7.2.2.2. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device and ensure it registers with the �G core for data services over NSA by connecting over the O-eNB as Master eNB and O-RU� of the O-RAN system as secondary gNB.   
2. Once the registration is complete, the end user device shall establish a PDN connection with the �G core.   
3. Open the video streaming client on the end user device and start a streaming session over HTTP/TCP protocol.   
4. Once the video streaming session has started, move the device so it can handover from O-RU� to O-RU� on the Secondary gNB while it continues to use the O-eNB as the Master eNB.   
5. Allow the end user device to stream video through the entire handover process. Measure the KPIs included in Clause �.� for this video streaming session.   
6. Optionally, repeat steps � through � for a video streaming session which uses HTTP/ QUIC protocol for streaming.   
7. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.16. Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user device without any errors using the Master eNB and O-RU1, O-DU and O-CU-CP/O-CU-UP as the Secondary gNB. This is a prerequisite before these tests can be validated.

Validate the end user device can start streaming the video without delays and watch the video content through the entire handover process. Ensure there are no stalls, downgrading of video quality or intermittent buffering of the video content, especially during the handover process. Use the packet captures to validate there are no packet drops or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

• Video Start time or Time to load first video frame – \~1.5 seconds   
• Number of video stalls/buffering – $< 1$   
• Duration of stalls in the video – $< 5$ seconds Video MOS Score $\underline { { \mathbf { \Pi } } } > 3 . 5$

The values for the end user video streaming KPIs defined in Clause 7.2 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup. End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second)   
• PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second)   
• Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
• Downlink transmission mode

Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\bf \delta \ u$ 16 Example Test Report for Video Streaming – Handover between same Master eNB but different O-RUs – Intra DU handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video Streaming over HTTP/TCP</td><td rowspan=1 colspan=1> Video Streaming over HTTP/QUIC</td></tr><tr><td rowspan=1 colspan=1>Video Start Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Number of Video Stalls/buffering</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Duration of stalls in the video</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Video MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user video streaming experience can also be impacted by some of the features available (see Clause 6.2) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which could impact the end user’s video streaming experience should be included in the test report to provide a comprehensive view of the testing.

4.112. Video Streaming – Handover between same MeNB with different O-DUs – Inter O-DU Intra O-CU

# 7.2.3.0

# Test Overview

This test scenario validates the user’s video streaming experience when the UE is connected over NSA to a 4G core and the UE is in the process of a handover between two O-RAN subcomponents (two O-RUs and O-DUs) on the Secondary gNB while remaining connected to the same Master eNB. The VoLTE or VoNR services cannot be used to test handover of secondary gNB, video streaming is used for this testing. This test scenario is only applicable in an NSA deployment.

7.17. Test Description

The 5G O-RAN system has multiple sub-components, including the O-RU, O-DU and the O-CU-CP/OCU-UP. This setup leads to multiple handover scenarios when the O-RAN system is connected as a Secondary gNB in an NSA deployment. This scenario tests the end user’s video streaming experience when the end user device is connected over NSA to the 4G core and performs a handover between O-RUs which are connected to different O-DUs, which in turn are connected to the same O-CU-CP/O-CU-UP on the Secondary gNB – Inter-O-DU Intra-O-CU handover. The end user device remains connected to the

same Master eNB through the entire handover process. This handover is agnostic to the 4G core as the handover occurs on the O-RAN system. This test assesses the impact of the video streaming service on the end user device in this handover scenario by monitoring the KPIs included in Clause 7.2 This test case streams video using ABR protocol over HTTP/TCP and/or HTTP/QUIC.

# 7.18. Test Setup

The SUT in this test case shall be the Master eNB and a Secondary gNBs. The Master eNB will be an OeNB and the Secondary gNB will constitute of a pair of O-RUs – O-RU1 and O-RU2, which are connected to a pair of O-DUs -DU1 and O-DU2, which are connected to the same O-CU-CP/O-CU-UP. The O-eNB, O-RUs, O-DUs and O-CU-CP/O-CU-UP shall comply with the O-RAN specifications. The 4G core will be required to support the basic functionality to authenticate and register an end user device, to set up a PDN connection. The 4G/5G core may be a completely emulated, partially emulated or a real non-emulated core. The application server(s) for this testing should support video streaming using ABR protocol over HTTP/TCP and/or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This may be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements or application server(s) are located remotely either in a cloud or on the Internet, the additional latency should be calculated and accounted for.

The O-eNB shall have the correct configuration and software load. The pair of O-RUs (O-RU1 and ORU2) shall be connected to the pair of O-DUs (O-DU1 and O-DU2), where O-RU1 is connected to ODU1 and O-RU2 is connected to O-DU2. Both the O-DUs, O-DU1 and O-DU2 shall be connected to the same O-CU-CP/O-CU-UP. All the O-RAN components (O-RUs, O-DUs and O-CU-CP/O-CU-UP) shall have the correct configuration and software load. The end user device shall be configured with the correct user credentials to register and authenticate with the Master eNB and the 4G core. The end user device also shall be provisioned with the correct application, such as a video streaming client, to perform the tests. The 4G core network shall be configured to support end user device used for testing. This includes supporting registration, authentication and PDN connection establishment for this end user device. All the elements in the network like O-RAN system, 4G core and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the video streaming KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system (O-eNB, O-RUs, O-DUs and OCU-CP/O-CU-UP), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the application server.

# 7.19. Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G core and the application server have all been configured as outlined in Clause 7.2.3.2. All traces and packet captures need to be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device and ensure it registers with the �G core for data services over NSA by connecting over the O-eNB as Master eNB and O-RU� of the O-RAN system as secondary gNB.   
2. Once the registration is complete, the end user device shall establish a PDN connection with the �G core.   
3. Open the video streaming client on the end user device and start a streaming session over HTTP/TCP protocol.   
4. Once the video streaming session has started, move the device so it can handover from O-RU� to O-RU� (and in turn O-DU� to O-DU�) on the Secondary gNB, while it continues to use the O-eNB as the Master eNB.   
5. Allow the end user device to stream video through the entire handover process. Measure the KPIs included in Clause �.� for this video streaming session.

6. Optionally, repeat steps � through � for a video streaming session which uses HTTP/ QUIC protocol for streaming.

7. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.20.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user device without any errors using the O-eNB as Master eNB and O-RU1, O-DU1 and O-CU-CP/ O-CU-UP as the Secondary gNB. This is a prerequisite before these tests can be validated.

Validate the end user device can start streaming the video without delays and watch the video content through the entire handover process. Ensure there are no stalls, downgrading of video quality, or intermittent buffering of the video content, especially during the handover process. Use the packet captures to validate there are no packet drops or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

• Video Start time or Time to load first video frame – \~1.5 seconds Number of video stalls/buffering – $< 1$   
• Duration of stalls in the video – $< 5$ seconds Video MOS Score $\underline { { \mathbf { \Pi } } } > 3 . 5$

The values for the end user video streaming KPIs defined in Clause 7.2 need to be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup. End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\bf \delta \ u$ 17 Example Test Report for Video Streaming – Handover between same Master eNB but different O-RUs and O-DUs – Inter-O-DU Intra-O-CU handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video Streaming overHTTP/TCP</td><td rowspan=1 colspan=1>Video Streaming over HTTP/QUIC</td></tr><tr><td rowspan=1 colspan=1>Video Start Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Number of Video Stalls/buffering</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Duration of stalls in the video</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Video MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td></tr></table>

The end user video streaming experience can also be impacted by some of the features available (see Clause 7.2) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which could impact the end user’s video streaming experience should be included in the test report to provide a comprehensive view of the testing.

4.113. Video Streaming – Handover between same MeNB with different O-CUs – Inter O-CU

# 7.2.4.0

# Test Overview

This test scenario validates the user’s video streaming experience when the end user device (UE) is connected over NSA to a 4G core and is in the process of a handover between two Secondary gNB (ORUs, O-DUs and O-CU-CP/O-CU-UPs) while remaining connected to the same Master eNB. The VoLTE or VoNR services cannot be used to test handover of secondary gNB, video streaming is used for this testing. This test scenario is only applicable in an NSA deployment.

7.21. Test Description

This scenario tests the impact of a handover on the video streaming service. The end user device is connected over NSA to the 4G core and streaming video, while it performs a handover of the Secondary gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) to a new Secondary gNB (O-RU, O-DU and O-CU-CP/OCU-UP), i.e. an inter-O-CU handover, while still being connected to the same Master eNB. This test assesses the impact of the video streaming service on the end user device in this handover scenario by monitoring the end user video streaming KPIs included in Clause 7.2. This test case streams video using ABR protocol over HTTP/TCP and/or HTTP/QUIC.

# 7.22. Test Setup

The SUT in this test case shall be the O-eNB which are the Master eNB and a pair of Secondary gNBs – O-RU1, O-DU1, O-CU-CP/O-CU-UP1 and O-RU2, O-DU2, O-CU-CP/O-CU-UP2. The O-eNB, ORUs, O-DUs and O-CU-CP/O-CU-UPs shall comply with the O-RAN specifications. A 4G core will be required to support the basic functionality to authenticate and register an end user device to set up a PDN connection. The 4G/5G core may be a completely emulated, partially emulated or a real nonemulated core. The application server(s) for this testing should support video streaming using ABR protocol over HTTP/TCP and/or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This may be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the Internet, the additional latency should be calculated and accounted for.

The O-eNB, pair of gNBs (O-RUs, O-DUs and O-CU-CP/O-CU-UPs) shall have the correct configuration and software load. The pair of gNBs shall be connected as follows – O-RU1 will be connected to O-DU1, which in turn will be connected to O-CU-CP/O-CU-UP1 and similarly O-RU2 will be connected to O-DU2, which in turn will be connected to O-CU-CP/O-CU-UP2. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the Master eNB and the 4G core. The end user device also shall be provisioned with the correct application, such as a video streaming client, to perform the tests. The 4G core network shall be configured to support end user device used for testing. This includes supporting registration, authentication and PDN connection establishment for this end user device.

All the elements in the network,including the O-RAN (O-eNB and gNBs), 4G core, and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the video streaming KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system (O-eNB and gNBs), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the application server.

# 7.23.

# Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G core and the application server have all been configured as outlined in Clause 7.2.4.2. All traces and packet captures need to be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device and ensure it registers with the �G core for data services over NSA by connecting over the O-eNB as Master eNB and O-RU�, O-DU�, O-CU-CP/OCU-UP� as secondary gNB.   
2. Once the registration is complete, the end user device shall establish a PDN connection with the �G core.   
3. Open the video streaming client on the end user device and start a streaming session over HTTP/TCP protocol.   
4. Once the video streaming session has started, move the device so the secondary gNB is handed over from O-RU� to O-RU� (i.e. from O-RU�, O-DU� and O-CU-CP/O-CU-UP�, to O-RU�, O-DU� and O-CU-CP/O-CU-UP�), while it continues to use the O-eNB as the Master eNB.   
5. Allow the end user device to stream video through the entire handover process. Measure the KPIs included in Clause �.� for this video streaming session.   
6. Optionally, repeat steps � through � for a video streaming session which uses HTTP/ QUIC protocol for streaming.   
7. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.24.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user device without any errors using the Master eNB and the O-RU1, O-DU1 and O-CU-CP/O-CUUP1 as secondary gNB. This is a prerequisite before these tests can be validated.

Validate the end user device can start streaming the video without delays and watch the video content through the entire handover process. Ensure there are no stalls, downgrading of video quality, or intermittent buffering of the video content, especially during the handover process. Use the packet captures to validate there are no packet drops or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add latency, jitter and packet loss issues to the connection, thus impacting the

KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

• Video Start time or Time to load first video frame – \~1.5 seconds Number of video stalls/buffering – $< 1$   
• Duration of stalls in the video – $< 5$ seconds Video MOS Score $\underline { { \mathbf { \Pi } } } > 3 . 5$

The values for the end user video streaming KPIs defined in Clause 7.2 need to be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup. End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\bf \delta \ u$ 18 Example Test Report for Video Streaming – Handover between same Master eNB but different O-RUs – Inter CU handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video Streaming over HTTP/TCP</td><td rowspan=1 colspan=1>Video Streaming over HT&#x27;TP/QUIC</td></tr><tr><td rowspan=1 colspan=1>Video Start Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Number of Video Stalls/buffering</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Duration of stalls in the video</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Video MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user video streaming experience can also be impacted by some of the features available (see Clause 7.2) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along

with any other features/functionality which could impact the end user’s video streaming experience should be included in the test report to provide a comprehensive view of the testing.

# 4.114. Video Streaming – Handover between different MeNB while staying connected to same SgNB

# 7.2.5.0

# Test Overview

This test scenario validates the user’s video streaming experience when the end user device (UE) is connected over NSA to a 4G core and the UE is in the process of a handover between two Master eNBs (two O-eNB) while staying connected to the same Secondary gNB (O-RU, O-DU and O-CU-CP/O-CUUP). The VoLTE or VoNR services cannot be used to test handover of secondary gNB, video streaming is used for this testing. This test scenario is only applicable in an NSA deployment.

# 7.25.

Test Description

This scenario tests the impact of a handover on the video streaming service. The end user device is connected over NSA to the 4G core and streaming video while it performs handover of the Master eNB to a new Master eNB, i.e. O-eNB1 to O-eNB2, while staying connected to the same Secondary gNB (O-RU, O-DU and O-CU-CP/O-CU-UP). This test assesses the impact of the video streaming service on the end user device in this handover scenario by monitoring the end user video streaming KPIs included in Clause 7.2. This test case streams video using ABR protocol over HTTP/TCP and/or HTTP/QUIC.

# 7.26. Test Setup

The SUT in this test case shall be a pair of O-eNBs (O-eNB1 and O-eNB2) which act as Master eNBs and a Secondary gNBs – (O-RU, O-DU and O-CU-CP/O-CU-UP). The pair of O-eNBs, O-RU, O-DU and O-CU-CP/O-CU-UP shall comply with the O-RAN specifications. A 4G core will be required to support the basic functionality to authenticate and register an end user device to set up a PDN connection. The 4G/5G core may be a completely emulated, partially emulated or a real non-emulated core. The application server(s) for this testing should support video streaming using ABR protocol over HTTP/TCP and/or HTTP/QUIC as applicable. The end user device (UE) used for testing may be a real UE or an emulated one. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This may be a built-in capability of the emulated/nonemulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the Internet, the additional latency should be calculated and accounted for.

The pair of O-eNBs (O-eNB1 and O-eNB2) and the gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the correct configuration and software load. Tools which emulate latency shall be used and configured on the O-RAN system (between O-RU, O-DU and O-CU-CP/O-CU-UP) to emulate realworld deployment conditions. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN (O-eNBs and gNB) and the 4G core. The end user device also shall be provisioned with the correct application, such as a video streaming client, to perform the tests. The 4G core network shall be configured to support end user device used for testing. This includes supporting registration, authentication and PDN session establishment for this end user device. All the elements in the network like O-RAN system, 4G core and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user device should have the capability to capture traces/packets to calculate the video streaming KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system (O-eNBs and gNB), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the application server.

# 7.27.

Test Methodology/Procedure

Ensure the end user device, O-RAN system, 4G core and the application server have all been configured as outlined in Clause 7.2.5.2. All traces and packet captures need to be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device and ensure it registers with the �G core for data services over NSA by connecting over the O-eNB� as Master eNB and O-RU, O-DU and O-CU-CP/ O-CU-UP as Secondary gNB.   
2. Once the registration is complete, the end user device shall establish a PDN connection with the �G core.   
3. Open the video streaming client on the end user device and start a streaming session over HTTP/TCP protocol.   
4. Once the video streaming session has started, move the end user device so it performs a handover of the Master eNB from O-eNB� to O-eNB�, while staying connected to the same Secondary gNB i.e. O-RU, O-DU and O-CU-CP/O-CU-UP.   
5. Allow the end user device to stream video through the entire handover process. Measure the KPIs included in Clause �.� for this video streaming session.   
6. Optionally, repeat steps � through � for a video streaming session which uses HTTP/ QUIC protocol for streaming.   
7. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.28.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user device without any errors using O-eNB1 as the Master eNB and the O-RU, O-DU and O-CUCP/O-CU-UP as secondary gNB. This is a prerequisite before these tests can be validated.

Validate the end user device can start streaming the video without delays and watch the video content through the entire handover process. Ensure there are no stalls, downgrading of video quality, or intermittent buffering of the video content, especially during the handover process. Use the packet captures to validate there are no packet drops or out of sequence packets which could impact customer experience and point to a misconfigured or flawed system.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which could impact the KPIs, example: use of the Internet to connect to remote servers/hosts could add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

• Video Start time or Time to load first video frame – \~1.5 seconds   
• Number of video stalls/buffering – $< 1$   
• Duration of stalls in the video – $< 5$ seconds Video MOS Score $\underline { { \mathbf { \Pi } } } > 3 . 5$

The values for the end user video streaming KPIs defined in Clause 7.2 need to be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup. End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second)   
• Downlink transmission mode

• Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

The table below gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\bf \delta \ u$ 19 Example Test Report for Video Streaming – Handover between Master eNB while staying connected to the same Secondary gNB   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video Streaming over TCP/QUIC</td><td rowspan=1 colspan=1>Video Streaming over TCP/QUIC</td></tr><tr><td rowspan=1 colspan=1>Video Start Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Number of Video Stalls/buffering</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Duration of stalls in the video</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Video MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr></table>

The end user video streaming experience can also be impacted by some of the features available (see Clause 7.2) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which could impact the end user’s video streaming experience should be included in the test report to provide a comprehensive view of the testing.

# 4.41. Voice Services – Voice over LTE (VoLTE) tests

# 7.3.0 VoLTE tests introduction

Voice service forms another basic service which is provided to a customer on a telecom network. Even though the earlier 2G/3G networks provide voice service through a circuit-switched network, the present document focuses on voice service provided using a packet switched network and specifies test cases to validate the Voice over LTE service in different scenarios. The KPIs which shall be monitored to assess the voice service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage.   
CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds.   
MOS Score ‒ Mean Opinion Score for the voice call and shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.

Mute Rate ‒ Percentage of calls which were muted in both directions (calls with RTP loss of $= 3 - 4 s$ in both directions are considered muted call). This KPI shall be measured on both ends of the voice call ‒ mobile originated & mobile terminated and counted only once per call. • One Way Calls ‒ Percentage of calls which were muted in any one direction (calls with RTP loss of $\geq 3 \cdot 4 s$ in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the voice call ‒ mobile originated & mobile terminated and counted only once per call. RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the voice call ‒ mobile originated and mobile terminated.

Along with the monitoring and validation of these services utilizing user experience KPIs, the O-RAN systems also shall be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been included below. As a part of the voice services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user voice experience, these shall be included in the test report as well.

• RLC in Unacknowledged Mode Robust Header Compression   
• DRX Dynamic GBR Admission Control   
• TTI Bundling VoLTE Inactivity Timer Frequency Hopping   
Multi-Target RRC Connection Re-Establishment   
VoLTE HARQ   
Coordinated Multi Point (DL and UL)   
• VoLTE Quality Enhancement Packet Loss Detection   
• Voice Codec Aware scheduler NR to LTE PS Redirection/Cell Reselection/Handove LTE to NR PS Redirection/Cell Reselection/Handove

Table 710 provides a summary of test cases and applicable technology.

Table 7SEQ Table $\backslash \ast$ ARABIC $\mathbf { \ s u }$ 110: VoLTE Test Case Selection summary

<table><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=1>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Voice service (VoLTE)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.3.1</td><td rowspan=1 colspan=1>VoLTE Stationary Test</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.3.2</td><td rowspan=1 colspan=1>VoLTE handover Test (intra)</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.3.3</td><td rowspan=1 colspan=1>Voice Service – LTE to NR / NR to LTE handovertest</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.115. VoLTE Stationary Test

# 7.3.1.0

# Test Overview

This scenario tests the voice service experience on an LTE network – Voice over LTE (VoLTE) when the end user device is stationary.

7.29. Test Description

With penetration of LTE, VoLTE has become the primary method of providing voice service. VoLTE uses IP packets to send and receive voice packets, with the IP packets being transferred over LTE. IMS forms an important part of VoLTE as it is used to setup control and data plane needed for VoLTE communication. As voice service is latency sensitive, the 4G core interacts with the IMS core to setup different bearers for Voice traffic – QCI-5 for VoLTE control plane and QCI-1 for VoLTE data plane. This test case is applicable when UE is connected over an O-RAN system to a 4G core in an NSA deployment.

Test Setup

The SUT in this test case is an O-eNB which includes the Master eNB and may include a Secondary gNB. As most of the current NSA deployment use the 4G eNB to provide voice services, the use of a secondary gNB is optional. The Secondary gNB is included in this test scenario, but it is only applicable if the gNB plays a role in establishing the control plane or data plane for a voice call. The O-eNB, gNB and the components within these shall comply with the O-RAN specifications. The O-RAN setup should support the ability to perform this testing in different radio conditions as defined in Clause 4.6. A 4G core shall be used to support the basic functionality to authenticate and register an end user device in order to setup a PDN connection. An IMS core is used to register the end user device to support voice services on a 4G network. The 4G and IMS cores can be a completely emulated, partially emulated or real nonemulated core. At least two end user devices (UE) shall be used, which may be real UEs or emulated, and both shall support voice service using VoLTE. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user devices to represent the role they plan in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The Master eNB, Secondary gNB and their components (O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the right configuration and software load. The end user device shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G core. The end user devices shall be provisioned with the user credentials to attach to the 4G core and register with the IMS core to perform a voice call using VoLTE. The 4G core network and IMS core shall be configured to support end user devices used for testing including supporting registration, authentication and PDN connection establishment for these end user devices. This also includes provisioning the IMS core to support registration of the end user devices to make voice calls over VoLTE, and dynamically setting up dedicated bearers for voice calls. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network like O-RAN system, 4G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoLTE KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNBs and gNBs), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the IMS Core.

Ensure the end user devices, O-RAN system, 4G core and the IMS Core have all been configured as outlined in Clause 7.3.1.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN (i.e. same O-eNB), 4G and IMS core to perform the end-to-end voice call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices in excellent radio condition and ensure both end user devices connect to the �G core over the Master O-eNB and optionally secondary gNB.   
2. Ensure both the MO and MT end user devices can establish a PDN connection with the �G core. Once the PDN connection has been setup, both the end user devices shall register with the IMS core to support voice services.   
3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.   
4. Continue to have two-way voice communication on the voice call for at least � minutes before terminating it.   
5. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.   
6. Repeat the above steps � through � for the MO and MT end user devices in good, fair, and poor radio conditions.

# 7.32. Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful PDN connection setup by the end user devices without any errors using the Master eNB and optionally the secondary gNB. Verify both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a voice call between each other by dynamically setting up a QCI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties are clear and audible without one-way or intermittent muting. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$ MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

These end user voice KPI values included in Clause 7.3 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed in different radio conditions to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 711 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table \\* ARABIC \s 111 Example Test Report for Voice over LTE Testing – Stationary Test   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>VoLTE MO/MT</td><td rowspan=1 colspan=1>VoLTE MO/MT</td><td rowspan=1 colspan=1>VoLTE MO/MT</td><td rowspan=1 colspan=1>VoLTE MO/MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user VoLTE experience can also be impacted by some of the features available (see Clause 7.3) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.116. VoLTE Handover Test

This test clause is FFS

4.117. Voice Service - LTE and NR handover tests   
7.3.3.0 Test Overview

This test scenario validates the user’s voice experience when the UE is in a voice call and performs a handover from LTE network to a 5G network and vice versa. This test scenario is applicable for a 5G SA deployment.

# 7.33. Test Description

Voice service is one of the basic services provided on the telecommunication network. Voice service on the 4G network is provided using VoLTE. Similarly, voice service on the 5G network is provided using packet switch technology called Voice over New Radio (VoNR). As 5G network is being deployed by a telecommunication service provider, the service provider can need to support 4G and 5G network, and thus support VoLTE, VoNR and the handover between the two voice services. This scenario tests the end user’s voice experience when the end user device performs a handover from VoLTE to VoNR and vice versa.

# 7.34. Test Setup

The SUT in this test case is an O-eNB along with a gNB (O-RU, O-DU and O-CU-CP/O-CU-UP). An interworking 4G-5G core (referred to as 4G-5G core going forward) which supports a combined anchor point for 4G and 5G, i.e. SMF $^ +$ PGW-C and UPF $^ +$ PGW-U is required. The eNB connects to a 4G-5G core over the 4G interfaces like S1 to provide 4G LTE service and the O-CU-CP/O-CU-UP, O-DU and O-RU will connect to a 4G-5G core over the 5G interfaces like N2 and N3 to provide 5G SA service. The OeNB, and the components within these shall comply with the O-RAN specifications. The 4G-5G core shall support the basic functionality to authenticate and register an end user device in order to setup a PDN connection/PDU session. An IMS core is required to register the end user device to support voice services on a 4G and 5G network. The 4G and 5G core will interwork using the N26 interface between the MME and AMF to support seamless handover. Use of the N26 interface is recommended to ensure better customer experience when the end user device performs a handover between 4G and 5G. The 4G-5G and IMS cores can be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support voice service using VoLTE, VoNR and the capability to handover from VoLTE to VoNR and vice versa. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user devices to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely, either in a cloud or on the internet, the additional latency should be calculated and accounted for. The O-eNB, gNB and their components (O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the right configuration and software load. The end user devices shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G-5G core. The end user devices shall be provisioned with the user credentials to support attach procedure to the 4G-5G core, registering to the IMS core and performing a voice call using VoLTE and VoNR. This includes supporting registration, authentication and PDN connection/PDU Session establishment for these end user devices. This also includes provisioning the IMS core to support registration of the end user devices to make voice calls over VoLTE and VoNR, and dynamically setting up dedicated bearers/QoS Flows for voice calls. All the elements in the network like O-RAN system, 4G-5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoLTE and VoNR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(eNBs and gNBs), O-RAN system shall be connected to the 4G-5G core, which in turn shall have connectivity to the IMS Core.

# 7.35. Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 4G-5G core and the IMS Core have all been configured as outlined in clause 7.3.3.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the eNB and gNB to connect to the same 4G-5G and IMS core to perform the end-to-end voice call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

The below items 1 to 8 define the steps to perform a VoLTE to VoNR handover, followed by VoNR to VoLTE handover

1. Power on the two end user devices and ensure both of the end user devices can connect to the �G-�G core over the O-eNB.   
2. Ensure both the MO and MT end user devices can establish a PDN connection with the �G-�G core. Once the PDN connection has been setup, both the end user devices shall register with the IMS core to support voice services.   
3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.   
4. Once the two-way call has been setup and communication is going back and forth between the two end user devices, move the MO device to the O-RU coverage of the gNB, thus forcing a handover from �G to �G, forcing a VoLTE to VoNR handover. Continue two-way voice communication through the handover process and terminate the call once the handover process is complete. Measure the voice KPIs included in Clause �.�.   
5. At this point in time, the MO end user device is in �G coverage and registered to the �G-�G core. The MT end user device is in �G coverage and registered to the �G-�G core. Both end user devices should still be registered to the IMS core.   
6. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.   
7. Once the two-way call has been setup and communication is going back and forth between the two end user devices, move the MO device to the O-eNB coverage, thus forcing a handover from �G to �G, forcing a VoNR to VoLTE handover. Continue two-way voice communication through the handover process and terminate the call once the handover process is complete. Measure the voice KPIs included in Clause �.�.   
8. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.36.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user devices without any errors using the O-eNB when in 4G coverage. Similarly, use traces to validate successful registration and PDU session setup by the end user device without any errors using O-RU, O-DU and O-CU-CP/O-CU-UP when in 5G coverage. Also verify both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed. Validate the end user devices can make a voice call between each other by dynamically setting up a QCI-1/5QI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties is clear and audible without one-way or intermittent muting. Ensure the voice quality is not impacted during the handover process – VoLTE to VoNR and VoNR to VoLTE. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues, especially during the handover process. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. Example: use of internet to connect to remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

• CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .

• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$ • MOS Score $_ - > 3 . 5$ • Mute Rate $\% -- < 1 \%$ • One Way Call $\% - < 1 \%$ • RTP Packet Loss $\% - < 1 \%$

The end user voice KPI values included in Clause 7.3 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed in different radio conditions to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
• Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 712 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash \ast$ ARABIC \s 112 Example Test Report for Voice service handover testing – LTE and NR   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VoLTE to VoNR handover</td><td rowspan=1 colspan=1>VoNR to VoLTE handover</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user VoLTE/VoNR experience can also be impacted by some of the features available (see Clause 7.3) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.42. Voice Service – EPS Fallback tests

# 7.4.0 Voice service - EPS fall back tests introduction

Voice service is one of the basic services which must be supported on every telecom network. Upgrade of telecom network occurs in phases, and this is no different for 5G. The telecom network may not be able to support voice service on 5G during this phase for multiple reasons – the 5G network may not be deployed nationwide, or 5G network may not be tuned to support voice service or the devices may not be able to support voice service on 5G. However, there can be no interruption to voice service during this transition phase. EPS fallback is the method used to support voice services during this phase, where voice services are continued to be supported on the legacy LTE network using VoLTE by forcing the device to fallback to LTE to make or receive a call. The KPIs which shall be monitored to assess the voice service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage. CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds. MOS Score ‒ Mean Opinion Score for the voice call. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated. Mute Rate $\%$ ‒ Percentage of calls which were muted in both directions (calls with RTP loss of $> 3 \ – 4 s$ in both directions are considered muted call). This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated and counted only once per call. - One Way Calls $\%$ ‒ Percentage of calls which were muted in any one direction (calls with RTP loss of $\geq 3 \cdot 4 s$ in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the Voice call ‒ mobile originated and mobile terminated and counted only once per call. RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.

Along with the monitoring and validation of these services utilizing user experience KPIs, the O-RAN systems also shall be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been included below. As a part of the voice services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user voice experience, these shall be included in the test report as well.

• EPS Fallback for IMS Voice • NR to EPS Mobility • RLC in Unacknowledged Mode • Robust Header Compression • DRX

• Dynamic GBR Admission Control   
• TTI Bundling   
• VoLTE Inactivity Timer   
• Frequency Hopping   
• Multi-Target RRC Connection Re-Establishment   
• VoLTE HARQ Coordinated Multi Point (DL and UL) VoLTE Quality Enhancement Packet Loss Detection Voice Codec Aware scheduler

Please see Table 713 for a summary of test cases and applicable technology.

Table 7SEQ Table \\* ARABIC \s 113: EPS Fallback Test Case Selection summary

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Voice service - EPS Fallback</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.4.1</td><td rowspan=1 colspan=1>EPS Fallback (N26 and without N26)</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.118. EPS Fallback Test

# 7.4.1.0

# Test Overview

This scenario tests the voice service when an end user device (UE) is in 5G SA coverage and performs an EPS fallback to 4G to make or receive a voice call.

# 7.37.

Test Description

This clause tests the voice service on a 5G SA network when it uses EPS fallback mechanism to fallback to the LTE network and use VoLTE to support voice service. This testing only applies to 5G SA deployment and in this scenario the UE is connected to the 5G SA Core and registered with the IMS core for voice service. When the end user device (UE) wants to make a voice call or receive a voice call, the network informs the device to fallback to the LTE network to make/receive the voice call. The EPS fallback does increase the Call Setup Time due to the time needed to fallback before making/receiving the voice call.

There are two mechanisms in which EPS fallback is supported on the 5G core, and the methodology used impacts the time taken to perform the fallback to LTE, and hence impacts the Call Setup Time. The two mechanisms that may be used to perform EPS fallback are included below. These two mechanisms do change the test setup, but do not change the testing procedure.

With N�� interface ‒ The AMF in the �G core communicates with the MME in the �G over the N�� interface. In this scenario the UE performs a handover from the �G network to the �G network.

Without N�� interface ‒ The AMF in the �G core does not communicate directly with the �G core, instead uses the UDM/HSS to store and transfer relevant session information to the �G core. In this scenario the UE performs a Release with Redirect from the �G network to the �G network.

# 7.38. Test Setup

The SUT in this test case is an O-eNB along with a gNB (O-RU, O-DU and O-CU-CP/O-CU-UP). An interworking 4G-5G core (referred to as 4G-5G core going forward) which supports a combined anchor point, i.e. SMF $+$ PGW-C and UPF $^ { \prime } +$ PGW-U is required. The O-eNB connects to a 4G-5G core over the 4G interfaces like S1 to provide 4G LTE service and the gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) will connect to the 4G-5G core over the 5G interfaces like N2 and N3 to provide 5G SA service. The O-eNB, gNB and the components within these shall comply with the O-RAN specifications and support EPS fallback. The 4G-5G core will support the basic functionality to authenticate and register an end user device in order to setup a PDN connection/PDU session. The IMS core will support registration of the end user device and will be integrated with the 4G-5G core to support voice services over VoLTE and EPS fallback. The 4G-5G core will interwork either using the N26 interface or without using N26 interface depending on the desired core network configuration. The existence of the N26 interface does reduce the EPS fallback time, reducing Call Setup Time and provides better end user experience. The 4G-5G and IMS cores may be a completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used. which either can be real UEs or emulated, and both shall support voice service using VoLTE and EPS fallback procedure. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. For the sake of clarity, these end user devices will be addressed as UE-1 and UE-2 in this clause. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-eNB, gNB and their components (O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the right configuration and software load. The end user device shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G-5G core. The end user devices shall be provisioned with the user credentials to attach to the 4G-5G core and register with the IMS core to perform voice call using VoLTE and EPS fallback. The 4G-5G core network and IMS core shall be configured to support voice service on the end user devices used for testing, which includes dynamically setting up dedicated bearers for voice calls.

All the elements in the network like O-RAN system, 4G-5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoLTE KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNBs and gNBs), O-RAN system shall be connected to the 4G-5G core which in turn shall have connectivity to the IMS Core.

# 7.39.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 4G-5G core and the IMS Core have all been configured as outlined in Clause 7.4.1.2. In this test scenario, one of the end user device will be connected over the 4G O-eNB to the 4G-5G core, while the other end user device will be connected over 5G gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) to the 4G-5G core. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure UE-� is in LTE coverage, and UE-� is in the �G coverage. Validate both end user devices register to the �G-�G core.

2. Once the registration is complete, UE-� and UE-� shall establish a PDN connection and PDU session respectively with the �G-�G core. Once the PDN connection and PDU

session have been setup, both the end user devices shall register with the IMS core to support voice services.

3. Use UE-� as the MO end user device to call UE-�. Validate the UE-� performs EPS fallback to LTE to receive the call.

4. Answer the call on UE-� and continue to have two-way communication for at least � minutes and terminate the call. Measure the voice KPIs included in Clause �.�.

5. At this point UE-� should have completed the call and moved back to connect to the �G-�G Core over �G gNB.

6. Use UE-� as the MO end user device to call UE-�. Validate the UE-� performs EPS fallback to LTE before making the call.

7. Answer the call on UE-� and continue to have two-way communication for at least � minutes and terminate the call. Measure the voice KPIs included in Clause �.�.

8. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.

# 7.40.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate end user device UE-1 can perform a successful registration and PDN connection setup while using the O-eNB in LTE coverage. Similarly, use the traces to validate end user device UE-2 can perform a successful registration and PDU session setup while using $\mathsf { g N B }$ in 5G coverage. Verify both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a voice call between each other by dynamically setting up a QCI-1 bearer to transfer voice packets over RTP. Validate the device which is in the 5G coverage falls back to 4G before receiving or making a voice call, in other words the EPS fallback procedure was executed successfully. The Call Setup Time will be higher than VoLTE due to the delay associated with executing the EPS fallback procedure. Even though this test case does not directly impact the quality of the voice call, for the sake of consistency, ensure the voice quality from both parties are clear and audible without one-way or intermittent muting. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included in Table 714 for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

Table 7SEQ Table $\backslash \ast$ ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 114 Typical Voice KPI values in controlled environments with good radio conditions   

<table><tr><td rowspan=1 colspan=1>KPI</td><td rowspan=1 colspan=1>With N26 Interface</td><td rowspan=1 colspan=1>Without N26 Interface</td></tr><tr><td rowspan=1 colspan=1>CSSR – Call Setup SuccessRate %</td><td rowspan=1 colspan=1>&gt;99%</td><td rowspan=1 colspan=1>&gt;99%</td></tr><tr><td rowspan=1 colspan=1>CST − Call Setup Time</td><td rowspan=1 colspan=1>3.5s</td><td rowspan=1 colspan=1>4s</td></tr><tr><td rowspan=1 colspan=1>MOs Score</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1>3.5</td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr><tr><td rowspan=1 colspan=1>One Way Call%</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr></table>

These end user voice KPI values included in Clause 7.3 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report to provide a comprehensive view of the test setup.

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 715 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table $\backslash \ast$ ARABIC \s 115 Example Test Report for Voice Service Testing – EPS Fallback   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VoLTE MO</td><td rowspan=1 colspan=1>VoLTE MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user VoLTE experience can also be impacted by some of the features available (see Clause 7.3) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.43. Voice Service – Voice over NR (VoNR) tests

# 7.5.0 VoNR test introduction

Voice services on 5G are called Voice over New Radio (VoNR). VoNR also packetizes voice and uses IP packets for voice communication. On the Core and IMS side, VoNR is very similar to VoLTE. VoNR also uses the IMS system for voice service, and the IMS interacts with the 5G core to set up a separate bearer for voice service. This clause tests the voice service over VoNR in different scenarios. The KPIs which shall be monitored to assess the voice service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage.   
CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds.   
MOS Score ‒ Mean Opinion Score for the voice call. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.   
Mute Rate $\%$ ‒ Percentage of calls which were muted in both directions (calls with RTP loss of $= 3 - 4 s$ in both directions are considered muted call). This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile   
terminated and counted only once per call.   
One Way Calls $\%$ ‒ Percentage of calls which were muted in any one direction (calls with RTP loss of $\geq 3 \cdot 4 s$ in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the Voice call ‒ mobile originated and mobile terminated and counted only once per call.   
RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.

End user voice service experience can also be impacted by some of the features available on the O-RU, O-DU and O-CU-CP/O-CU-UP. Some of these features have been included below. As a part of the voice services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user voice experience, these shall be included in the test report as well.

Basic Voice over NR • RLC in Unacknowledged Mode (id Robust Header Compression • DRX - Dynamic GBR Admission Control TTI Bundling • Automated Neighbor Relations ANR Connected mode mobility (Handover) idle mode reselection Intra-frequency Cell Reselection/Handover • Inter-frequency Redirection/Cell Reselection/Handover • NR Coverage-Triggered NR Session Continuity

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Voice service - Voice over NR (VoNR)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.5.1</td><td rowspan=1 colspan=1>Voice over NR Test – stationary</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.5.2</td><td rowspan=1 colspan=1>VONR – Intra-Distributed Unit (DU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.5.3</td><td rowspan=1 colspan=1>VONR – Intra-Central Unit (CU) Inter- DistributedUnit (DU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.5.4</td><td rowspan=1 colspan=1>VONR – Inter-Central Unit (CU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.119. Voice over NR Test

# 7.5.1.0

# Test Overview

This test scenario validates the user’s voice experience when the end user device is in 5G coverage and the user makes a voice call over NR – VoNR.

# 7.41. Test Description

This clause tests VoNR user experience on an O-RAN system. VoNR is similar to VoLTE where it uses IP packets to send and receive voice packets, with the IP packets being transferred over NR or 5G radio. Just like VoLTE, IMS is used to set up the control and data plane for the voice communication. As voice service is latency sensitive, the 5G core interacts with the IMS core to set up different QoS flows for voice traffic – 5QI-5 for VoNR control plane and 5QI-1 for VoNR data plane. This test case is applicable when end user device (UE) is connected over a 5G SA network.

# 7.42. Test Setup

The SUT in this test case is a gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) which is used to test the voice service. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support voice services on a 5G network. The 5G and IMS cores may be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support voice service using VoNR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user device to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The O-RU, O-DU and O-CU-CP/O-CU-UP shall have the right configuration and software load. The SUT shall be set up to run this testing in different radio conditions as outlined in Clause 4.6. The end user device shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform voice call using VoNR. The 5G core network and IMS core shall be configured to support voice service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for voice calls. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network like O-RAN system, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoNR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-RU, O-DU and O-CU-CP/O-CU-UP), O-RAN system shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.43. Test Methodology/Procedure

Ensure the end user device, O-RAN system, 5G core and the IMS core have all been configured as outlined in Clause 7.5.1.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN system, 5G and IMS core to perform the end-to-end voice call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices in excellent radio condition and ensure both devices register with the �G core for voice services over SA by connecting over the O-RAN (O-RU, O-DU and O-CU-CP/O-CU-UP).   
2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support voice services.   
3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.   
4. Continue to have two-way voice communication on the voice call for at least � minutes before terminating it.   
5. Repeat the test multiple times $( > 1 0$ times) and gather results.   
6. Repeat the above steps � through � for good, fair, and poor radio conditions.

# 7.44.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over O-RU, O-DU and O-CU-CP/O-CU-UP. Also validate both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a voice call between each other by dynamically setting up a 5QI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties are clear and audible without one-way or intermittent muting. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

As a part of gathering data, ensure the minimum configuration parameters included in Clause 4.3 are included in the test report. The information in Table 717 should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second)   
PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per   
second)   
Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
Downlink transmission mode   
Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number   
of allocated/occupied slots (average sample per second)

Table 7SEQ Table \\* ARABIC \s 117 Example Test Report for VoNR – Stationary Testing   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>VoNR MO/MT</td><td rowspan=1 colspan=1>VoNR MO/MT</td><td rowspan=1 colspan=1>VoNR MO/MT</td><td rowspan=1 colspan=1>VoNR MO/MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[]</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user voice service experience can also be impacted by some of the features available (see Clause 7.5) on the O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.120. VoNR – Intra-Distributed Unit (O-DU) handover

This test scenario validates the user’s voice experience when the end user device (UE) is on a VoNR call and performs a handover between two O-RUs which connect to the same O-DU (Intra-O-DU handover)

# 7.45. Test Description

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU-CP/O-CU-UP. This setup leads to multiple handover scenarios between the O-RAN components. This scenario tests the end user’s voice experience during the handover between two O-RUs which are connected to the same

O-DU (and O-CU-CP/O-CU-UP), hence an Intra-O-DU handover. This handover will be agnostic to the 5G core as the handover occurs on the O-RAN system. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.5.

# 7.46. Test Setup

The SUT in this test case is a pair of O-RUs which connect to the same O-DU and O-CU-CP/O-CU-UP (refer Clause 5.4). This O-RAN setup is used to test the voice service during a handover. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support voice services on a 5G network. The 5G and IMS cores may be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support voice service using 5G – Voice over NR(VoNR). The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user device to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The pair of O-RUs (O-RU1 and O-RU2) shall be connected to the O-DU and O-CU-CP/O-CU-UP and all the components shall have the right configuration and software load. The end user devices shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform voice call using VoNR. The 5G core network and IMS core shall be configured to support voice service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for voice calls.

All the elements in the network-like O-RAN system, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoNR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-RUs connected to O-DU and O-CUCP/O-CU-UP), O-RAN system shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.47.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 5G core and the IMS Core have all been configured as outlined in Clause 7.5.2.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN system, 5G and IMS core to perform the end-to-end voice call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for voice services over SA by connecting over the O-RAN (O-RU, O-DU and O-CU-CP/O-CUUP). Ensure both the MO & MT end user devices are in the coverage area of the same ORU ‒ O-RU�.

2. Once the registration is complete, the MO and MT end user devices shall establish PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support voice services.

3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.

4. Once the call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, triggering a handover from O-RU� to O-RU�.

5. Continue the two-way voice communication between MO and MT end user devices until the handover procedure is complete before terminating the voice call.

6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and collect results.

# 7.48.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over O-RU, O-DU and O-CU-CP/O-CU-UP. Also validate both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a voice call between each other by dynamically setting up a 5QI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties is clear and audible without one-way or intermittent muting for the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. Example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score $\mathrm { \Omega } _ { - } > 3 . 5$   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

As a part of gathering data, the minimum configuration parameters in Clause 4.3) shall be included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second)   
Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
• Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

# Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 118 Example Test Report for VoNR – Intra-O-DU Handover

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VoNR MO</td><td rowspan=1 colspan=1>VoNR MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>One Way Call %</td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td></tr><tr><td rowspan=1 colspan=1>UE PMI</td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td></tr></table>

The end user voice service experience can also be impacted by some of the features available (see Clause 7.5) on the O-RUs, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.121. VoNR – Intra-Central Unit (O-CU) Inter-Distributed Unit (O-DU) handover

This test scenario validates the user’s voice experience when the end user device (UE) is on a VoNR call and performs a handover between O-RUs which connect to different O-DUs, which in turn are connected to the same O-CU-CP/O-CU-UP (Intra-O-CU Inter-O-DU handover)

7.49.

Test Description

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU-CP/O-CU-UP. This setup leads to multiple handover scenarios between the O-RAN components. This particular scenario tests the end user’s voice experience during the handover between two O-RUs, where the O-RUs are connected to different O-DUs which in turn are connected to the same O-CU-CP/O-CU-UP, hence an Intra-O-CU Inter-O-DU handover. This handover will be agnostic to the 5G core as the handover occurs on the O-RAN system. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.5.

7.50. Test Setup

The SUT in this test case is a pair of O-RUs which connect to a different pair of O-DUs which in turn connect to the same O-CU (refer Clause 4.5). This O-RAN setup is used to test the voice service during a handover. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support voice services on a 5G network. The 5G and IMS cores can be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support voice service using VoNR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user device to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely, either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The pair of O-RUs (O-RU1 and O-RU2) shall be connected to a pair of O-DUs (O-DU1 and O-DU2) and O-CU-CP/O-CU-UP. As for the O-RU to O-DU connection, O-RU1 shall connect to O-DU1, and O-RU2 shall connect to O-DU2, and both O-DUs shall connect to the same O-CU-CP/O-CU-UP. All the O-RAN components shall have the correct configuration and software load. The end user devices shall be provisioned with the user credentials to register and setup a PDU session with the 5G core and register with the IMS core to perform voice calls using VoNR. The 5G core network and IMS core shall be configured to support voice service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for voice calls.

All the elements in the network like O-RAN system, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoNR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-RUs connected to O-DU and O-CU), O-RAN system shall be connected to the 5G core, which in turn shall have connectivity to the IMS Core.

# 7.51.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 5G core and the IMS core have all been configured as outlined in Clause 7.5.3.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN system, 5G and IMS core to perform the end-to-end voice call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for voice services over SA by connecting over the O-RAN (O-RU, O-DU and O-CU). Both the MO & MT end user devices shall be in the coverage area of the same O-RU ‒ O-RU�.

2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support voice services.

3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.

4. Once the call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, thus causing a handover from O-RU� to O-RU�, and O-DU� to O-DU�.

5. Continue the two-way voice communication between the end user devices until the handover procedure is complete before terminating the voice call.

6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and gather results.

# 7.52.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over O-RU, O-DU and O-CU. Also validate both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed. Validate the end user devices can make a voice call between each other by dynamically setting up a 5QI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties is clear and audible without one-way or intermittent muting through the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. Example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$   
• CST ‒ Call Setup Time ‒ $\cdot < 2 . 5 s$   
• MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

As a part of gathering data, ensure the minimum configuration parameters in see Clause 4.3 are included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table $\backslash \ast$ ARABIC \s 119 Example Test Report for VoNR – Inter-O-DU Intra-O-CU Handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VoNR MO</td><td rowspan=1 colspan=1>VoNR MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user voice service experience can also be impacted by some of the features available (see Clause 7.5) on the O-RUs, O-DU and O-CU. The details of these features, along with any other features/

functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.122. VoNR – Inter-Central Unit (O-CU) handover

This test scenario validates the user’s voice experience when the end user device (UE) is on a VoNR call and performs a handover between O-RUs which connect to different O-DUs and different O-CUs (InterO-CU Inter-O-DU handover)

7.53. Test Description

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU. This setup leads to multiple handover scenarios between the O-RAN components. This particular scenario tests the end user’s voice experience during the handover between two O-RUs, where the O-RUs are connected to different O-DUs which in turn are connected to different O-CUs, hence an Inter-O-CU Inter-O-DU handover. This handover occurs on the O-RAN system and the 5G core is aware of the handover as it needs to send data to a new O-CU as a part of the handover process. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.5.

# 7.54. Test Setup

The SUT in this test case is a pair of O-RAN subsystems, a set of O-RU, O-DU and O-CU which interconnects with another set of O-RU, O-DU and O-CU (refer Clause 5.6). This O-RAN setup is used to test the voice service during a handover. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support voice services on a 5G network. The 5G and IMS cores can be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support voice service using VoNR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the voice call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user device to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The pair of O-RAN (O-RAN1 and O-RAN2) subsystems shall be connected – O-RU1 shall be connected to O-DU1, which in turn shall be connected to O-CU1 and similarly O-RU2 shall be connected to ODU2, which in turn shall be connected to O-CU2. The O-CU1 and O-CU2 nodes shall be connected to each other and the 5G core. All the O-RAN components shall have the correct configuration and software load. The end user devices shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user devices also shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform voice call using VoNR. The 5G core network and IMS core shall be configured to support voice service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for voice calls.

All the elements in the network like O-RAN system, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoNR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-RUs connected to O-DUs which are connected to the O-CUs), O-RAN system shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.55.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 5G core and the IMS Core have all been configured as outlined in Clause 7.5.4.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN system, 5G and IMS core to perform the end-to-end voice call. All

traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for voice services over SA by connecting over the O-RAN� system (O-RU�, O-DU� and OCU�). Both the MO & MT end user devices shall be in the coverage area of the same O-RU ‒ O-RU�.

2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support voice services.

3. Use the MO end user device to call the MT end user device. Validate the MT end user device can receive and answer the call.

4. Once the call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, thus causing a handover from O-RAN� to O-RAN� subsystem - O-RU� to O-RU�, O-DU� to O-DU� and O-CU� to O-CU�.

5. Continue the two-way voice communication between MO and MT end user devices until the handover procedure is complete before terminating the voice call.

6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and gather results.

# 7.56.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over O-RU, O-DU and O-CU. Also validate both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed. Validate the end user devices can make a voice call between each other by dynamically setting up a 5QI-1 bearer to transfer voice packets over RTP. Ensure the Call Setup Time is reasonable, the voice quality from both parties is clear and audible without one-way or intermittent muting through the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. Example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$   
• CST ‒ Call Setup Time $\cdot < 2 . 5 s$   
• MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet L $) 5 5 \% \mathrm { ~ -- ~ } 1 \%$ As a part of gathering data, ensure the minimum configuration parameters in Clause 4.3) are included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.   
UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second)

• PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L1 and L3 PDCP layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table $\backslash \ast$ ARABIC $\mathbf { et { } { ' } } $ 120 Example Test Report for VoNR – Inter-O-CU Handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VoNR MO</td><td rowspan=1 colspan=1>VoNR MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user voice service experience can also be impacted by some of the features available (see Clause 7.5) on the O-RUs, O-DUs and O-CU. The details of these features, along with any other features/ functionality which can impact the end user’s voice service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.44. Video Service – Video over LTE (ViLTE) tests

# 7.6.0 ViLTE test introduction

Voice service has been one of the basic services provided on the mobile device since launch. With increasing LTE penetration and the availability of higher speeds, video calls are slowly replacing voice calls. With the launch of 5G which promises much higher throughput, the shift towards using video calls is only going to get faster. This clause of the present document validates the user’s video calling experience in different conditions on the LTE network. This clause of the present document only applies to the video calling service provided by the telecom service provider, which uses the telecom operator’s IMS core to establish dedicated bearer to provide superior video calling experience. The KPIs which shall be monitored to assess the video service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage. CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds. MOS Score ‒ Mean Opinion Score for the video call. This shall be measured on both ends of the video call ‒ mobile originated and mobile terminated. Mute Rate $\%$ ‒ Percentage of video calls which were muted or video freezes in both directions (calls with RTP loss of $= 3 - 4 5$ in both directions are considered muted call). This KPI shall be measured on both ends of the video call ‒ mobile originated and mobile terminated and counted only once per call. • One Way Calls $\%$ ‒ Percentage of video calls which were muted, or video is not transmitted in any one direction only (video calls with RTP loss of $> .$ �-�s in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the Video call ‒ mobile originated and mobile terminated and counted only once per call. RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the Video call ‒ mobile originated and mobile terminated.

Along with the monitoring and validation of these services utilizing user experience KPIs, the O-RAN systems also shall be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been included below. As a part of the video calling services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user voice experience, those need be included in the test report as well.

• RLC in Unacknowledged Mode   
• Robust Header Compression   
• DRX Dynamic GBR Admission Control TTI Bundling   
VoLTE Inactivity Timer   
Frequency Hopping   
• Multi-Target RRC Connection Re-Establishment   
VoLTE HARQ Coordinated Multi Point (DL and UL)   
VoLTE Quality Enhancement Packet Loss Detection   
• Voice Codec Aware scheduler   
- NR to LTE PS Redirection/Cell Reselection/Handove

# • LTE to NR PS Redirection/Cell Reselection/Handover

Table 721 provides a summary of test cases and applicable technology.

Table 7SEQ Table $\backslash \ast$ ARABIC $\mathbf { \ s u }$ 121: ViLTE Test Case summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Video service- Video over LTE (ViLTE)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.6.1</td><td rowspan=1 colspan=1>ViLTE Stationary Test</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.6.2</td><td rowspan=1 colspan=1>ViLTE handover Test (intra)</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>7.6.3</td><td rowspan=1 colspan=1>Video Service – LTE to NR / NR to LTE handovertest</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.123. ViLTE Stationary Test

This test scenario validates the user’s video calling experience when the end user device (UE) is in LTE coverage and performs a video call.

# 7.57.

Test Description

Telecom service providers are providing video calling service to their customers and it has been gaining popularity replacing voice calls. Video over LTE (ViLTE) uses the same mechanism as VoLTE, i.e. IP packets to send and receive video & audio packets, with the IP packets being transferred over LTE. Just like VoLTE, IMS is used to setup control and data plane needed for ViLTE communication. As two-way video service is latency sensitive, the EPC core interacts with the IMS core to setup different bearers for Video traffic – QCI-5 for ViLTE control plane and QCI-2 for ViLTE data plane. This test case is applicable when UE is connected over an NSA network. This clause tests ViLTE user experience on an O-RAN system.

7.58. Test Setup

The SUT in this test case is an O-eNB which includes the Master eNB and can include a Secondary gNB. As most of the current NSA deployment use the 4G eNB to provide video calling services, the use of a secondary gNB is optional. The Secondary gNB is included in this test scenario, but it is only applicable if the $\mathsf { g N B }$ plays a role in establishing the control plane or data plane for a video call. The O-eNB, gNB and the components within these shall comply with the O-RAN specifications. The O-RAN setup should support the ability to perform this testing in different radio conditions as defined in Clause 4.6. A 4G core is used to support the basic functionality to authenticate and register an end user device in order to setup a PDN connection. An IMS core is used to register the end user device to support video calling services on a 4G network. The 4G and IMS cores can be completely emulated, partially emulated or real nonemulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support video calling service using ViLTE. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user devices to represent the role they plan in the video call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This could be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The Master eNB, Secondary gNB and their components (O-eNB, O-RU, O-DU and O-CU) shall have the right configuration and software load. The end user device shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G core. The end user devices shall be provisioned with the user credentials to attach to the 4G core and register with the IMS core to perform a video call using ViLTE. The 4G core network and IMS core shall be configured to support end user devices used for testing including supporting registration, authentication and PDN connection establishment for these end user devices. This also includes provisioning the IMS core to support registration of the end user devices to make video calls over ViLTE. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network like O-RAN system, 4G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the VoLTE KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNBs and gNBs), O-RAN system shall be connected to the 4G core which in turn shall have connectivity to the IMS Core.

# 7.59.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 4G core and the IMS Core have all been configured as outlined in Clause 7.6.1.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN (i.e. same O-eNB), 4G and IMS core to perform the end-to-end video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices in excellent radio condition and ensure both end user devices connect to the �G core over the Master O-eNB and optionally secondary gNB.   
2. Ensure both the MO and MT end user devices can establish a PDN connection with the �G core. Once the PDN connection has been setup, both the end user devices shall register with the IMS core to support video calling services.   
3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the call.   
4. Continue to have two-way voice and video communication on the video call for at least � minutes before terminating it.   
5. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.   
6. Repeat the above steps � through � for the MO and MT end user devices in good, fair and poor radio conditions.

# 7.60.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful PDN connection setup by the end user devices without any errors using the Master eNB and optionally the secondary gNB. Verify both the end user devices can register with the IMS core for video services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a video call between each other by dynamically setting up a QCI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the video and voice quality from both parties are clear and audible without one-way or intermittent muting or video freezing. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s video calling experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

• CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .

• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$ • MOS Score $\_ { \Sigma 3 . 5 }$ • Mute Rate $\% -- < 1 \%$ • One Way Call $\% - < 1 \%$ • RTP Packet Loss $\% - < 1 \%$

These end user video calling KPI values included in Clause 7.6 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed in different radio conditions to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Received downlink throughput (L1 and L3 PDCP layers) (average sample per second)   
• Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 722 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table \\* ARABIC \s 122 Example Test Report for Video over LTE Testing – Stationary Test   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Excellent(cell centre)</td><td rowspan=1 colspan=1>Good</td><td rowspan=1 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor(cell edge)</td></tr><tr><td rowspan=1 colspan=1>ViLTE MO/MT</td><td rowspan=1 colspan=1>ViLTE MO/MT</td><td rowspan=1 colspan=1>ViLTE MO/MT</td><td rowspan=1 colspan=1>ViLTE MO/MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Buff er status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>UE Packet delay</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td></tr></table>

The end user ViLTE experience can also be impacted by some of the features available (see Clause 7.6) on the O-eNB, O-RU, O-DU and O-CU. The details of these features, along with any other features/ functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.124. ViLTE Handover Test

This test clause is for FFS.

# 4.125. ViLTE - LTE to NR handover test

This test scenario validates the user’s video calling experience when the UE is in video call on LTE and performs a handover from LTE network to a 5G network and vice versa. This test scenario is applicable for a 5G SA deployment.

# 7.61. Test Description

Voice service is one of the basic services provided on the telecommunication network. Video service on the 4G network was provided using ViLTE. Similarly, video service on the 5G network is provided using packet switch technology called Video over New Radio. As 5G network is being deployed by a telecommunication service provider, the service provider can need to support 4G and 5G network, and thus support Video over LTE, Video over NR and the handover between the two video calling services. This scenario tests the end user’s video calling experience when the end user device performs a handover from video over LTE to Video over NR and vice versa.

# 7.62. Test Setup

The SUT in this test case is an O-eNB along with a gNB (O-RU, O-DU and O-CU). An interworking 4G-5G core (referred to as 4G-5G core going forward) which supports a combined anchor point for 4G and 5G, i.e. SMF $^ { \ast }$ PGW-C and UPF $^ +$ PGW-U is required. The eNB connects to a 4G-5G core over the 4G interfaces like S1 to provide 4G LTE service and the O-CU, O-DU and O-RU will connect to a 4G-5G core over the 5G interfaces like N2 and N3 to provide 5G SA service. The O-eNB, gNB and the components within these shall comply with the O-RAN specifications. The 4G-5G core shall support the basic functionality to authenticate and register an end user device in order to setup a PDN connection/ PDU session. An IMS core is required to register the end user device to support video calling services on a 4G and 5G network. The 4G and 5G core will interwork using the N26 interface between the MME and AMF to support seamless handover. Use of the N26 interface is recommended to ensure better customer experience when the end user device performs a handover between 4G and 5G. The 4G-5G and IMS cores can be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support video calling service using ViLTE, Video over NR and the capability to handover from ViLTE to Video over NR and vice versa. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user devices to represent their role in the video call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for. The O-eNB, gNB and their components (O-RU, O-DU and O-CU) shall have the right configuration and software load. The end user devices shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G-5G core. The end user devices shall be provisioned with the user credentials to support attach procedure to the 4G-5G core, registering to the IMS core and performing a video call over LTE and NR. This includes supporting registration, authentication and PDN connection/PDU Session establishment for these end user devices. This also includes provisioning the IMS core to support registration of the end user devices to make video calls over ViLTE and Video over NR, which includes dynamically setting up dedicated bearers/QoS Flows for video calls.

All the elements in the network like O-RAN system, 4G-5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the ViLTE and Video over NR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNBs and gNBs), O-RAN system shall be connected to the 4G-5G core which in turn shall have connectivity to the IMS Core.

# 7.63.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 4G-5G core and the IMS Core have all been configured as outlined in Clause 7.6.3.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the O-eNB and gNB to connect to the same 4G-5G and IMS core to perform the end-toend video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

The steps to perform a video over LTE to video over NR handover, followed by video over NR to video over LTE handover are shown below.

1. Power on the two end user devices and ensure both end user devices connect to the �G-�G core over the O-eNB.

2. Ensure both the MO and MT end user devices can establish a PDN connection with the �G-�G core. Once the PDN connection has been established, both the end user devices shall register with the IMS core to support video calling services.

3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the video call.

4. Once the two-way call has been setup and communication is going back and forth between the two end user devices, move the MO device to the O-RU coverage of the gNB, thus forcing a handover from �G to �G, and forcing a ViLTE to Video over NR handover. Continue two-way voice and video communication through the handover process and terminate the call once the handover process is complete. Measure the video KPIs included in Clause �.�.

5. At this point in time, the MO end user device is in �G coverage and registered to the �G-�G core. The MT end user device is in �G coverage and registered to the �G-�G core. Both end user devices should still be registered to the IMS core.

6. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the call.

7. Once the two-way call has been setup and communication is going back and forth between the two end user devices, move the MO device to the O-eNB coverage, thus forcing a handover from �G to �G, and forcing a Video over NR to ViLTE handover.

Continue the two-way voice and video communication through the handover process and terminate the call once the handover process is complete. Measure the video KPIs included in Clause �.�.

8. Repeat the test multiple times $( > 1 0$ times) and gather results.

# 7.64.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDN connection setup by the end user devices without any errors using the O-eNB when in 4G coverage. Similarly, use traces to validate successful registration and PDU session setup by the end user device without any errors using

O-RU, O-DU and O-CU when in 5G coverage. Also validate both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be validated.

Validate the end user devices can make a video call between each other by dynamically setting up a QCI-2/5QI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the video and voice quality from both parties are clear and audible without one-way or intermittent muting or video freezing. Ensure the voice and video quality is not impacted during the handover process – ViLTE to Video over NR and Video over NR to ViLTE. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s video calling experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

These end user video calling KPI values included in Clause 7.6 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed in different radio conditions to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 723 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 123 Example Test Report for Video over LTE Testing – Handover Test   

<table><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="1">Excellent(cell centre)</td><td colspan="1" rowspan="1">Good</td><td colspan="1" rowspan="1">Fair</td><td colspan="1" rowspan="1">Poor(cell edge)</td></tr><tr><td colspan="1" rowspan="1">ViLTE MO/MT</td><td colspan="1" rowspan="1">ViLTE MO/MT</td><td colspan="1" rowspan="1">ViLTE MO/MT</td><td colspan="1" rowspan="1">ViLTE MO/MT</td></tr><tr><td colspan="1" rowspan="1">Call Setup Success Rate</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Call Setup time</td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">MOS Score</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">Mute Rate</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">One Way Call</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">RTP Packet Loss</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">L1 DL Spectral efficiency [bps/Hz]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSRP [dBm]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PDSCH SINR [dB]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">MIMO rank</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PDSCH MCS</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">DL RB number</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE CQI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSRQ</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PMI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSSI</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">UE Buffer status</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE Packet delay</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">PDSCH BLER [%]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[</td></tr></table>

The end user ViLTE experience can also be impacted by some of the features available (see Clause 7.6) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.45. Video Service – EPS Fallback

# 7.7.0 Video service – EPS fallback test introduction

Video service is quickly replacing voice service and turning into one of the basic services offered by telecommunication service providers. Upgrade of telecom network occurs in phases, and this is no different for 5G. The telecom network may not be able to support video calling service on 5G during this phase for multiple reasons – the 5G network may not be deployed nationwide, or 5G network may not be tuned to support voice/video service or the devices may not be able to support video/voice service on 5G. EPS fallback is the method used to support voice/video services during this transition phase, where voice/ video services are continued to be supported on the legacy LTE network using video over LTE (ViLTE). This clause of the document only applies to the video calling service provided by the telecom service provider, which uses the telecom operator’s IMS core to establish dedicated bearer to provide superior video calling experience. The KPIs which shall be monitored to assess the video calling service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage. CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds. MOS Score ‒ Mean Opinion Score for the video call. This KPI shall be measured on both ends of the video call ‒ mobile originated and mobile terminated. Mute Rate $\%$ ‒ Percentage of video calls which were muted or video freezes in both directions (calls with RTP loss of $= 3 - 4 5$ in both directions are considered muted call). This KPI shall be measured on both ends of the video call ‒ mobile originated and mobile terminated and counted only once per call. • One Way Calls $\%$ ‒ Percentage of video calls which were muted, or video is not transmitted in any one direction only (video calls with RTP loss of $> 3 \ – 4 s$ in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the Voice call ‒ mobile originated and mobile terminated and counted only once per call.

• RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.

Along with the monitoring and validation of these services utilizing user experience KPIs, the O-RAN systems also shall be monitored. The end user service experience can also be impacted by some of the features available on the O-RAN system. Some of these features have been included below. As a part of the voice services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been enabled during this testing that impact the end user voice experience, these shall be included in the test report as well.

• EPS Fallback for IMS Voice   
• NR to EPS Mobility   
• RLC in Unacknowledged Mode   
• Robust Header Compression   
• DRX Dynamic GBR Admission Control TTI Bundling   
• VoLTE Inactivity Timer   
• Frequency Hopping Multi-Target RRC Connection Re-Establishment   
VoLTE HARQ Coordinated Multi Point (DL and UL)   
VoLTE Quality Enhancement   
• Packet Loss Detection   
Voice Codec Aware scheduler

Please see Table 724 for a summary table of test cases and applicable technology.

# Table 7SEQ Table \\* ARABIC $\mathbf { \ s u }$ 124: Video EPS Fallback Test Case summary

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Video Service-EPS Fallback</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.7.1</td><td rowspan=1 colspan=1>EPS Fallback Test</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.126. Video Service – EPS Fallback testing

This scenario tests the video calling service when an end user device (UE) is in 5G SA coverage and performs EPS fallback to 4G to make or receive a video call.

# 7.65. Test Description

This clause tests the video service on a 5G SA network when it uses EPS fallback mechanism to fallback to the LTE network to use video over LTE to support video calling service. This testing only applies to 5G SA deployment and in this scenario the UE is connected to the 5G SA Core and registered with the IMS core for video calling service. As video calling service is not supported on 5G yet, the UE is forced to fallback to 4G when it makes/receives a video call. The EPS fallback does increase the Call Setup Time due to the time needed to fallback before making/receiving the video call.

There are two mechanisms in which EPS fallback is supported on the 5G core, and the methodology used impacts the time taken to perform the fallback to LTE, and hence impacts the Call Setup Time. The two mechanisms that may be used to perform EPS fallback are included below. These two mechanisms do change the test setup, but does not change the testing procedure.

With N�� interface ‒ The AMF in the �G core communicates with the MME in the �G over the N�� interface. In this scenario the UE performs a handover from the �G network to the �G network.   
Without N�� interface ‒ The AMF in the �G core does not communicate directly with the �G core, instead uses the UDM/HSS to store and transfer relevant session information to the �G core. In this scenario the UE performs a Release with Redirect from the �G network to the �G network.

# 7.66. Test Setup

The SUT in this test case is an O-eNB along with a gNB (O-RU, O-DU and O-CU-CP/O-CU-UP). An interworking 4G-5G core (referred to as 4G-5G core going forward) which supports a combined anchor point, i.e. SMF $+$ PGW-C and UPF $^ { \prime } +$ PGW-U is required. The O-eNB connects to a 4G-5G core over the 4G interfaces like S1 to provide 4G LTE service and the gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) will connect to the 4G-5G core over the 5G interfaces like N2 and N3 to provide 5G SA service. The O-eNB, gNB and the components within these shall comply with the O-RAN specifications and support EPS fallback. The 4G-5G core will support the basic functionality to authenticate and register an end user device in order to setup a PDN connection/PDU session. The IMS core will register the end user device and will be integrated with the 4G-5G core to support video calling services over LTE (ViLTE) and EPS fallback. The 4G-5G core will interwork either using the N26 interface or without using N26 interface depending on the desired core network configuration. The existence of the N26 interface does reduce the EPS fallback time, hence reducing Call Setup Time and provides better end user experience. The 4G-5G and IMS cores may be a completely emulated, partially emulated or real non-emulated core. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support video calling service using ViLTE and EPS fallback procedure. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. For the sake of clarity, these end user devices will be addressed as UE-1 and UE-2 in this clause. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for. The O-eNB, gNB and their components (O-RU, O-DU and O-CU-CP/O-CU-UP) shall have the right configuration and software load. The end user device shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 4G-5G core. The end user devices shall be provisioned with the user credentials to attach to the 4G-5G core and register with the IMS core to perform video call using ViLTE and EPS fallback. The 4G-5G core network and IMS core shall be configured to support video calling service on the end user device used for testing, which includes dynamically setting up dedicated bearers for video calls.

All the elements in the network like O-RAN system, 4G-5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the ViLTE KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to O-RAN system(O-eNBs and gNBs), O-RAN system shall be connected to the 4G-5G core which in turn shall have connectivity to the IMS Core.

# 7.67.

# Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 4G-5G core and the IMS Core have all been configured as outlined in Clause 7.7.1.2. In this test scenario, one of the end user devices (UE-1) will be connected over the 4G O-eNB to the 4G-5G core, while the other end user device (UE-2) will be connected over 5G gNB (O-RU, O-DU and O-CU-CP/O-CU-UP) to the 4G-5G core. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure UE-� is in LTE coverage, and UE-� is in the �G coverage. Validate both end user devices register to the �G-�G core.   
2. Once the registration is complete, UE-� and UE-� shall establish a PDN connection and PDU session respectively with the �G-�G core. Once the PDN connection and PDU session have been setup, both the end user devices shall register with the IMS core to support video calling services.   
3. Use UE-� as the MO end user device to video call UE-�. Validate the UE-� performs EPS fallback to LTE to receive the video call.   
4. Answer the call on UE-� and continue to have two-way audio/video communication for at least � minutes and terminate the call. Measure the voice KPIs included in Clause �.�.   
5. At this point UE-� should have completed the video call and moved back to connect to the �G-�G Core over �G gNB (i.e. O-RU).   
6. Use UE-� as the MO end user device to call UE-�. Validate the UE-� performs EPS fallback to LTE before making the video call.   
7. Answer the call on UE-� and continue to have two-way communication for at least � minutes and terminate the call. Measure the voice KPIs included in Clause �.�.   
8. Repeat the test multiple times ${ \tt > } 1 0$ times) and gather results.

# 7.68.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate end user device UE-1 can perform a successful registration and PDN connection setup while using the O-eNB in LTE coverage. Similarly, use the traces to validate end user device UE-2 can perform a successful registration and PDU session setup while using $\mathsf { g N B }$ in 5G coverage. Verify both the end user devices can register with the IMS core for voice services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a video call between each other by dynamically setting up a QCI-2 bearer to transfer voice and video packets over RTP. Validate the device which is in the 5G coverage falls back to 4G before receiving or making a video call, in other words the EPS fallback procedure was executed successfully. The Call Setup Time will be higher than Video over LTE due to the delay associated with executing the EPS fallback procedure. Even though this test case does not directly impact the quality of the video call, for the sake of consistency, ensure the voice and video quality from both parties are clear and audible without one-way or intermittent muting and video freezing. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing and video lag issues. Use the packet captures to ensure there are no out-ofsequence packets which can impact customer’s video calling experience.

The average range of values for the KPIs are included in Table 725 for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to

remote network nodes can add latency, jitter and packet loss issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 125 Typical Video KPI values in controlled environments with good radio conditions   

<table><tr><td rowspan=1 colspan=1>KPI</td><td rowspan=1 colspan=1>With N26 Interface</td><td rowspan=1 colspan=1>Without N26 Interface</td></tr><tr><td rowspan=1 colspan=1>CSSR – Call Setup SuccessRate %</td><td rowspan=1 colspan=1>&gt;99%</td><td rowspan=1 colspan=1>&gt;99%</td></tr><tr><td rowspan=1 colspan=1>CST - Call Setup Time</td><td rowspan=1 colspan=1>3.5s</td><td rowspan=1 colspan=1>4s</td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1>3.5</td><td rowspan=1 colspan=1>3.5</td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr><tr><td rowspan=1 colspan=1>One Way Call%</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1>&lt;1%</td><td rowspan=1 colspan=1>&lt;1%</td></tr></table>

These end user video calling KPI values included in Clause 7.7 shall be included in the test report along with the minimum configuration parameters included in Clause 4.3. The following information should also be included in the test report for the testing performed to provide a comprehensive view of the test setup.

End user device side (real or emulated UE):

Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second)   
Received downlink throughput (L1 and L3 PDCP layers) (average sample per second) Downlink transmission mode   
Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 726 gives an example of the test report considering the mean and standard deviation of all test results that have been captured.

Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 126 Example Test Report for Video Calling Service Testing – EPS Fallback   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EPS Fallback MO</td><td rowspan=1 colspan=1>EPS Fallback MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>PDSCH MCS</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td></tr><tr><td rowspan=1 colspan=1>UE PMI</td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td></tr></table>

The end user ViLTE experience can also be impacted by some of the features available (see Clause 7.7) on the O-eNB, O-RU, O-DU and O-CU-CP/O-CU-UP. The details of these features, along with any other features/functionality which can impact the end user’s video calling experience should be included in the test report to provide a comprehensive view of the testing.

# 4.46. Video Service – Video over NR

# 7.8.0 Video over NR test introduction

Video calling service is slowly replacing voice as a basic calling service. The improvement in end user throughput on LTE has facilitated the move from voice call to video, and the high speeds on 5G is only going to accelerate this migration process. This clause of the document validates the user’s video calling experience in different conditions on the 5G network. This clause of the document only applies to the video calling service provided by the telecom service provider, which uses the telecom operator’s IMS core to establish dedicated QoS flows to provide superior video calling experience. The KPIs which shall be monitored to assess the video calling service are included below

CSSR ‒ Call Setup Success Rate $\%$ ‒ Total number of calls which were successful by the total number of calls made as a percentage.   
CST ‒ Call Setup Time ‒ Time taken from the initial SIP INVITE to when the SIP ��� Ringing is received in seconds.   
MOS Score ‒ Mean Opinion Score for the video call. This KPI shall be measured on both ends of the video call ‒ mobile originated and mobile terminated.   
Mute Rate $\%$ ‒ Percentage of video calls which were muted or video freezes in both directions (calls with RTP loss of $= 3 - 4 5$ in both directions are considered muted call). This KPI shall be measured on both ends of the video call ‒ mobile originated and mobile terminated and counted only once per call.   
One Way Calls $\%$ ‒ Percentage of video calls which were muted, or video is not transmitted in any one direction only (video calls with RTP loss of $>$ �-�s in one direction only are considered one-way calls). This KPI shall be monitored on both ends of the Voice call ‒ mobile originated and mobile terminated and counted only once per call.   
RTP Packet Loss $\%$ - Number of RTP packets which were dropped/lost in uplink/ downlink direction as a percentage of total packets. This KPI shall be measured on both ends of the Voice call ‒ mobile originated and mobile terminated.

End user video calling service experience can also be impacted by some of the features available on the SUT (O-RU, O-DU and O-CU-CP/O-CU-UP). Some of these features have been included below. As a part of the video calling services testing, details of these features shall be included in the test report to get a comprehensive view of the setup used for testing. If additional features or functionalities have been

enabled during this testing that impact the end user voice experience, these shall be included in the test report as well.

Basic Voice over NR • RLC in Unacknowledged Mode • Robust Header Compression • DRX Dynamic GBR Admission Control • TTI Bundling • Automated Neighbor Relations ANR • Connected mode mobility (Handover) idle mode reselection Intra-frequency Cell Reselection/Handover • Inter-frequency Redirection/Cell Reselection/Handover • NR Coverage-Triggered NR Session Continuity

Please see Table 727 for a summary of test cases and applicable technology.

Table 7SEQ Table \\* ARABIC \s 127: Video over NR Test Case summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>Video service- Video over NR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.8.1</td><td rowspan=1 colspan=1>Video over NR Test – stationary</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.8.2.</td><td rowspan=1 colspan=1>Video – Intra-Distributed Unit (O-DU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.8.3</td><td rowspan=1 colspan=1>Video – Intra-Central Unit (O-CU) Inter-Distributed Unit (O-DU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>7.8.4</td><td rowspan=1 colspan=1>Video – Inter-Central Unit (O-CU) handover</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.127. Video over NR – Stationary Testing

This test scenario validates the user’s video calling experience when the end user device (UE) makes a video call on the 5G network.

7.69. Test Description

This clause of the document tests video over NR user experience on an O-RAN system. Video over NR is similar to ViLTE where it uses IP packets to send and receive audio/video packets, with the IP packets being transferred over NR or 5G radio. Just like ViLTE, IMS is used to setup the control and data plane for the video communication. As video calling service is latency sensitive, the 5G core interacts with the IMS core to setup different QoS flows for video traffic – 5QI-5 for control plane and 5QI-2 for data plane. This test case is applicable when UE is connected over a 5G SA network.

7.70. Test Setup

The SUT as defined in Clause 4.1.0 is used to test the video calling service. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support video calling services on a 5G network. The 5G and IMS cores may be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be a real UEs or emulated, and both shall support video calling service using Video over NR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user device to represent their role in the video call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The SUT shall have the right configuration and software load. The SUT shall be setup to run this testing in different radio conditions as outlined in Clause 4.6. The end user device shall be configured with the right user credentials to be able to register and authenticate with the SUT and the 5G core. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform video call using Video over NR. The 5G core network and IMS core shall be configured to support video calling service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for video calls. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network like SUT, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the Video over NR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to SUT(O-RU, O-DU and O-CU-CP/O-CU-UP), SUT shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.71. Test Methodology/Procedure

Ensure the end user devices, O-RAN system, 5G core and the IMS core have all been configured as outlined in Clause 7.8.1.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same O-RAN system, 5G and IMS core to perform the end-to-end video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices in excellent radio condition and ensure both devices register with the �G core for video calling services over SA by connecting over the SUT (O-RU, O-DU and O-CU-CP/O-CU-UP).

2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support video calling services.

3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the call.

4. Continue to have two-way audio/video communication on the video call for at least � minutes before terminating it.

5. Repeat the test multiple times $( > 1 0$ times) and gather results.

6. Repeat the above steps � through � for good, fair and poor radio conditions.

# 7.72.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over SUT. Also validate both the end user devices can register with the IMS core for video calling services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a video call between each other by dynamically setting up a 5QI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the voice and video quality from both parties are clear and audible without one-way or intermittent muting and video freezing. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio condition without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$ MOS Score $\mathrm { \Omega } _ { - } > 3 . 5$   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

As a part of gathering data, ensure the minimum configuration parameters included in Clause 4.3 are included in the test report. The information in Table 728 should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table \\* ARABIC $\mathbf { \ s u }$ 128 Example Test Report for Video over NR – Stationary Testing   

<table><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="1">Excellent(cell centre)</td><td colspan="1" rowspan="1">Good</td><td colspan="1" rowspan="1">Fair</td><td colspan="1" rowspan="1">Poor(cell edge)</td></tr><tr><td colspan="1" rowspan="1">Video over NRMO/MT</td><td colspan="1" rowspan="1">Video over NRMO/MT</td><td colspan="1" rowspan="1">Video over NRMO/MT</td><td colspan="1" rowspan="1">Video over NRMO/MT</td></tr><tr><td colspan="1" rowspan="1">Call Setup Success Rate</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Call Setup Time</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">MOS Score</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Mute Rate %</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">One Way Call %</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">RTP Packet Loss %</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">L1 DL Spectral efficiency [bps/Hz]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSRP [dBm]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PDSCH SINR [dB]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">MIMO rank</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">PDSCH MCS</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">DL RB number</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE CQI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSRQ</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE PMI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE RSSI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE Buffer status</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">UE Packet delay</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[]</td><td colspan="1" rowspan="1">[]</td></tr><tr><td colspan="1" rowspan="1">PDSCH BLER [%]</td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[</td></tr></table>

The end user video calling service experience can also be impacted by some of the features available (see Clause 7.8) on the SUT. The details of these features, along with any other features/functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.128. Video over NR – Intra-Distributed Unit (O-DU) handover

This test scenario validates the user’s video calling experience when the end user device (UE) is on a video call over NR and performs a handover between O-RUs which connect to the same O-DU (Intra-ODU handover).

7.73. Test Description

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU-CP/O-CU-UP. This setup leads to multiple handover scenarios between the O-RAN components. This scenario tests the end user’s video calling experience during the handover between two O-RUs which are connected to the same O-DU (and O-CU-CP/O-CU-UP), hence an Intra-O-DU handover. This handover will be agnostic to the 5G core as the handover occurs on the O-RAN system. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.8.

# 7.74. Test Setup

The SUT in this test case is a pair of O-RUs which connect to the same O-DU and O-CU-CP/O-CU-UP. This O-RAN setup is used to test the video calling service during a handover (refer Clause 5.4). A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support video calling services on a 5G network. The 5G and IMS cores may be completely emulated, partially emulated or real nonemulated cores. At least two end user devices (UE) shall be used, which can be real UEs or emulated , and both shall support video calling service using 5G – Video over NR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices will be referred to as MO end user device and MT end user device to represent their role in the video call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool.

Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the dditional latency should be calculated and accounted for.

The pair of O-RUs (O-RU1 and O-RU2) shall be connected to the O-DU and O-CU-CP/O-CU-UP and all the components shall have the right configuration and software load. The end user devices shall be configured with the right user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform video call using Video over NR. The 5G core network and IMS core shall be configured to support video service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for voice calls.

All the elements in the network like SUT, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the Video over NR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to SUTSUT shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.75.

# Test Methodology/Procedure

Ensure the end user devices, SUT, 5G core and the IMS core have all been configured as outlined in Clause 7.8.2.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same SUT, 5G and IMS core to perform the end-to-end video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for video calling services over SA by connecting over the SUT. Ensure both the MO & MT end user devices are in the coverage area of the same O-RU ‒ O-RU�.   
2. Once the registration is complete, the MO and MT end user devices shall establish PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support voice services.   
3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the call.   
4. Once the call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, triggering a handover from O-RU� to O-RU�.   
5. Continue the two-way video and voice communication between MO and MT end user devices until the handover procedure is complete before terminating the video call.   
6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and gather results.

# 7.76.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over SUT. Also validate both the end user devices can register with the IMS core for video calling services. This is a prerequisite before these tests can be completed.   
Validate the end user devices can make a video call between each other by dynamically setting up a 5QI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the voice and video quality from both parties are clear and audible without one-way or intermittent muting and video freezing, for the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.   
The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT. CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score $\mathrm { \Omega } _ { - } > 3 . 5$   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Los $5 \% \mathrm { ~ - ~ } 1 \%$

As a part of gathering data, the minimum configuration parameters in Clause 4.3 shall be included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 129 Example Test Report for Video over NR – Intra-O-DU Handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video over NR MO</td><td rowspan=1 colspan=1>Video over NR MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>UE Buff er status</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

The end user video calling service experience can also be impacted by some of the features available (see Clause 7.8) on the SUT. The details of these features, along with any other features/functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.129. Video over NR – Intra-Central Unit (O-CU) Inter-Distributed Unit (O-DU) handover

This test scenario validates the user’s video calling experience when the end user device (UE) is on a video call and performs a handover between O-RUs which connect to different O-DUs which in turn are connected to the same O-CU-CP/O-CU-UP (Intra-O-CU Inter-O-DU handover)

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU-CP/O-CU-UP. This setup leads to multiple handover scenarios between the O-RAN components. This particular scenario tests the end user’s video calling experience during the handover between two O-RUs, where the O-RUs are connected to different O-DUs which in turn are connected to the same O-CU-CP/O-CU-UP, hence an Intra-O-CU Inter-O-DU handover. This handover will be agnostic to the 5G core as the handover occurs on the O-RAN system. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.8.

# 7.78. Test Setup

The SUT in this test case is a pair of O-RUs which connect to a different pair of O-DUs, which in turn connect to the same O-CU-CP/O-CU-UP (refer Clause 4.5). This O-RAN setup is used to test the video service during a handover. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support voice services on a 5G network. The 5G and IMS cores can be completely emulated, partially emulated or real non-emulated. At least two end user devices (UE) shall be used, which can be real UEs or emulated, and both shall support video calling service using Video over NR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user device to represent their role in the voice call. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The pair of O-RUs (O-RU1 and O-RU2) shall be connected to a pair of O-DUs (O-DU1 and O-DU2) and O-CU-CP/O-CU-UP. As for the O-RU to O-DU connection, O-RU1 shall connect to O-DU1, and O-RU2 shall connect to O-DU2, and both O-DUs connect to the same O-CU-CP/O-CU-UP. All the O-RAN components shall have the correct configuration and software load. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform video calls using Video over NR. The 5G core network and IMS core shall be configured to support video calling service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for video calls.

All the elements in the network like SUT, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the Video over NR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to SUT, SUT shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.79.

# Test Methodology/Procedure

Ensure the end user devices, SUT, 5G core and the IMS Core have all been configured as outlined in Clause 7.8.3.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same SUT, 5G and IMS core to perform the end-to-end video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for video calling services over SA by connecting over the SUT. Both the MO & MT end user devices shall be in the coverage area of the same O-RU ‒ O-RU�.   
2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support video calling services.   
3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the call.

4. Once the video call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, thus causing a handover from O-RU� to O-RU�, and O-DU� to O-DU�. 5. Continue the two-way video and voice communication between the end user devices until the handover procedure is complete before terminating the video call. 6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and gather results.

# 7.80.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over SUT. Also validate both the end user devices can register with the IMS core for video calling services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a video call between each other by dynamically setting up a 5QI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the voice and video quality from both parties are clear and audible without one-way or intermittent muting and video freezing, through the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which could cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s voice experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score ‒ > �.�   
• Mute Rate $\% -- < 1 \%$   
• One Way Call $\% - < 1 \%$ RTP Packet Loss $\% - < 1 \%$

As a part of gathering data, ensure the minimum configuration parameters in Clause 4.3 are included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\mathbf { \ s u }$ 130 Example Test Report for Video over NR – Intra-O-CU InterO-DU Handover

<table><tr><td></td><td>Video over NR MO</td><td>Video over NR MT</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td></tr><tr><td rowspan=1 colspan=1>MOS Score</td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td></tr><tr><td rowspan=1 colspan=1>DL RB number</td></tr><tr><td rowspan=1 colspan=1>UE CQI</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td></tr><tr><td rowspan=1 colspan=1>UE PMI</td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td></tr></table>

The end user video calling service experience can also be impacted by some of the features available (see Clause 7.8) on the SUT. The details of these features, along with any other features/functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.130. Video over NR – Intra-Central Unit (O-CU) handover

This test scenario validates the user’s video calling experience when the end user device (UE) is on a video call and performs a handover between O-RUs which connect to different O-DUs and O-CU-CP/OCU-UPs (Inter-O-CU Inter-O-DU handover)

7.81.

Test Description

The 5G O-RAN system has multiple components such as the O-RU, O-DU and the O-CU-CP/O-CU-UP. This setup leads to multiple handover scenarios between the O-RAN components. This particular scenario tests the end user’s video calling experience during the handover between two O-RUs, where the O-RUs are connected to different O-DUs which in turn are connected to different O-CU-CP/O-CU-UPs, hence an Inter-O-CU Inter-O-DU handover. This handover occurs on the O-RAN system and the 5G core is aware of the handover as it needs to send data to a new O-CU-CP/O-CU-UP as a part of the handover process. This test assesses the impact on the end user’s voice service in this handover scenario by monitoring the KPIs included in Clause 7.8.

7.82. Test Setup

The SUT in this test case is a pair of O-RAN sub-systems, a set of O-RU, O-DU and O-CU-CP/O-CU-UP which interconnects with another set of O-RU, O-DU and O-CU-CP/O-CU-UP (refer Clause 5.6). This O-RAN setup is used to test the video calling service during a handover. A 5G SA Core is required to support basic functionality to authenticate and register the end user device to establish a PDU session. An IMS core is required to register the end user device to support video services on a 5G network. The 5G and IMS cores can be completely emulated, partially emulated or real non-emulated cores. At least two end user devices (UE) shall be used, which can be a real UEs or emulated, and both shall support video calling service using Video over NR. The end user devices will serve as Mobile Originated (MO) and Mobile Terminated (MT) end user devices forming the two ends of the video call. Going forward in this clause, these end user devices are referred to as MO end user device and MT end user device to represent their role in the video call. The test setup shall include tools which can collect traces on the elements and/ or packet captures of communication between the elements. This can be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the internet, the additional latency should be calculated and accounted for.

The pair of O-RAN (O-RAN1 and O-RAN2) sub-systems shall be connected – O-RU1 shall be connected to O-DU1, which in turn shall be connected to O-CU-CP/O-CU-UP1 and similarly O-RU2 shall be connected to O-DU2, which in turn shall be connected to O-CU-CP/O-CU-UP2. The O-CU-CP/O-CUUP1 and O-CU-CP/O-CU-UP2 nodes shall be connected to each other and the 5G core. All the O-RAN components shall have the correct configuration and software load. The end user devices shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user devices shall be provisioned with the user credentials to register and setup PDU session with the 5G core and register with the IMS core to perform video call using Video over NR. The 5G core network and IMS core shall be configured to support video calling service on the end user devices used for testing, which includes the ability to dynamically set up QoS Flows for video calls. All the elements in the network like SUT, 5G core and the IMS Core should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the Video over NR KPIs. Optionally, the network can have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. Finally, all these different components shall have connectivity with each other – the end user device shall be able to connect to SUT, SUT shall be connected to the 5G core which in turn shall have connectivity to the IMS Core.

# 7.83.

# Test Methodology/Procedure

Ensure the end user devices, SUT, 5G core and the IMS Core have all been configured as outlined in Clause 7.8.4.2. In this test scenario, both the mobile originated and mobile terminated end user devices will use the same SUT, 5G and IMS core to perform the end-to-end video call. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the two end user devices and ensure both devices register with the �G core for video calling services over SA by connecting over the O-RAN� sub-system (O-RU�, O-DU� and O-CU-CP/O-CU-UP�). Both the MO & MT end user devices shall be in the coverage area of the same O-RU ‒ O-RU�.   
2. Once the registration is complete, the MO and MT end user devices shall establish a PDU session with the �G core. Once the PDU session has been setup, both the end user devices shall register with the IMS core to support video calling services.   
3. Use the MO end user device to video call the MT end user device. Validate the MT end user device can receive and answer the video call.   
4. Once the call has been setup, move the MO end user device from the coverage area of O-RU� to coverage area of O-RU�, thus causing a handover from O-RAN� to O-RAN� subsystem - O-RU� to O-RU�, O-DU� to O-DU� and O-CU-CP/O-CU-UP� to O-CU-CP/O-CUUP�.   
5. Continue the two-way video and voice communication between MO and MT end user devices until the handover procedure is complete before terminating the video call.   
6. Repeat the test (steps � through �) multiple times $( > 1 0$ times) and gather results.

# 7.84.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup by the end user devices without any errors over SUT. Also validate both the end user devices can register with the IMS core for video calling services. This is a prerequisite before these tests can be completed.

Validate the end user devices can make a video call between each other by dynamically setting up a 5QI-2 bearer to transfer voice and video packets over RTP. Ensure the Call Setup Time is reasonable, the voice and video quality from both parties are clear and audible without one-way or intermittent muting and video freezing, through the duration of the call, especially during the handover process. Use the packet captures to validate there are no RTP packet drops or high RTP packet jitter which can cause voice muting, video freezing or video lag issues. Use the packet captures to ensure there are no out-of-sequence packets which can impact customer’s video experience.

The average range of values for the KPIs are included below for guidance. These values are applicable when the testing is performed in a controlled environment in good radio conditions without the interference of external factors which can impact the KPIs. For example: use of internet to connect to remote servers/hosts can add latency, jitter and reliability issues to the connection, thus impacting the KPIs. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure in the SUT.

CSSR ‒ Call Setup Success Rate $\%  9 9 \%$ .   
• CST ‒ Call Setup Time $\phantom { 0 } - < 2 . 5 s$   
• MOS Score $\mathrm { \Omega } _ { - } > 3 . 5$   
• Mute Rate $\% -- < 1 \%$ One Way Call $\% - < 1 \%$ RTP Packet Los $5 \% \mathrm { ~ - ~ } 1 \%$

As a part of gathering data, ensure the minimum configuration parameters in Clause 4.3 are included in the test report. The following information should also be included in the test report to provide a comprehensive view of the test setup.

UE side (real or emulated UE):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/occupied slots (average sample per second)

Table 7SEQ Table \\* ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 131 Example Test Report for Video over NR – Inter-O-CU Handover   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Video over NR MO</td><td rowspan=1 colspan=1>Video over NR MT</td></tr><tr><td rowspan=1 colspan=1>Call Setup Success Rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Call Setup Time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MOS Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mute Rate %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>One Way Call %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>RTP Packet Loss %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1 DL Spectral efficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCH SINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DL RB number</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>UE CQI</td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td></tr><tr><td rowspan=1 colspan=1>UE PMI</td></tr><tr><td rowspan=1 colspan=1>UE RSSI</td></tr><tr><td rowspan=1 colspan=1>UE Buffer status</td></tr><tr><td rowspan=1 colspan=1>UE Packet delay</td></tr><tr><td rowspan=1 colspan=1>PDSCH BLER [%]</td></tr></table>

The end user video calling service experience can also be impacted by some of the features available (see Clause 7.8) on the SUT. The details of these features, along with any other features/functionality which can impact the end user’s video calling service experience should be included in the test report to provide a comprehensive view of the testing.

# 4.47. URLLC

# 7.9.0 URLLC test introduction

The 5G network has been built not just to support the data and voice use-cases of the past, but a wide variety of use-cases to support connectivity across a diverse set of verticals, such as industrial automation, health care, gaming etc. The 5G network was built with flexibility and efficiency with additional enhancements being added in every release to enable ultra-low latency or ultra-reliability to cater to a diverse set of use-cases such as: automotive applications, augment and virtual reality etc. Network slicing in 5G allows the separation of the network where services with different characteristics and requirements can be run on separate slices of the network. These enhancements in 5G, paired up with network slicing capability, allows a telecommunication service provider to support all the diverse set of use-cases using the same 5G network and different network slices.

Ultra-Reliable Low Latency Communication (URLLC) is one such use case which allows service which require low end to end latency to be deployed. As this is a new concept, new services and use-cases are being created to use this slice of the network. The generic KPIs which will be monitored to assess the URLLC use cases are included below. As the URLLC use cases vary, the KPI used and the values for these KPIs also vary by use case. Not all KPIs are used for all use cases and similarly some KPIs are used only in specific use cases.

Reliability ‒ This is the percentage of packets or messages sent which were successfully delivered to the end node.   
End to End Latency ‒ The time required to transfer a packet or message from the end user device to the application or vice versa.   
Jitter ‒ The variation of the end-to-end latency values measured in the network setup over the transmission of multiple packets or messages.   
Position Service Accuracy ‒ The distance between the location provided by the location service and the real location of the target object.   
Position Service Latency ‒ The time elapsed between the request to get location information to when the location information is available.   
User experienced throughput ‒ The network throughput as measured on the application layer.   
Mean time between failures ‒ The duration of time the service was available befor a failure condition which causes the service to be unavailable.

his clause provides the procedure to test the URLLC applications in a telecommunication network. URLLC refers to a diverse set of applications where the end-user device communicates to the application server over the 5G network. The use-case itself has stringent requirements for the end-to-end latency and reliability between the end-user device and application server. 5G has enhancements within the RAN and core to support these requirements for the URLLC use cases. The 5G RAN allows for lower downlink

data to uplink Ack, thus reducing the latency on the air interface. Similarly, the 5G Core allows for the data plane anchor (UPF) to be deployed close to the end user device in the edge location along with the application server to eliminate part of the backhaul latency. Please see the below summary table of test cases and applicable technology.

Table 7SEQ Table $\backslash \ast$ ARABIC $\mathbf { \boldsymbol { \mathsf { s } } }$ 132: Augmented Reality Test Case summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>URLLC-Augmented Reality</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.9.1</td><td rowspan=1 colspan=1>Augmented Reality</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.131. Augmented Reality

This test scenario validates the end user’s augmented reality experience when using an AR device over the 5G network.

# 7.85. Test Description

This clause uses Augmented Reality (AR) as an example application, where the end user device is an AR device which communicates with an image processing server acting as the application server. AR has a wide range of applications including gaming, augmented worker as a part of smart factory, remote maintenance, ad-hoc support from remote expert, control of heavy equipment, etc. AR is one use case where the AR device has a camera and continuously transmits images in real time to an application server, along with the position of the AR device. The application server in this use case would be an image processing server, which render the augmented image and transmits the augmented video stream back down to the AR device, that then displays the image on the AR device. The entire process of uploading the image from the AR device, to the processing on the application server, and the displaying of the augmented image on the AR device needs to occur within milliseconds, with high reliability, to ensure the end user has a realistic augmented reality experience.

The 5G URLLC network slice does not have requirements on the protocol, or the method used to communicate between the end user device and the application server. The 5G network slice acts as a pipe to allow communication between these two end points, AR device and application server, with high data rate, high reliability and low latency requirements as dictated by the application. Optionally, depending on the AR use case two additional KPIs could also be monitored when audio-visual interaction is characterized by a human being interacting with entities or humans by relying on audio-visual feedback.

Motion to photon – The latency (measured time) between the physical movement of the user’s head and the updated image on the AR device.   
Motion to audio – The latency (measured time) between the physical movement of the user’s head and the updated sound waves from the AR device’s speakers.

# 7.86.

# Test Setup

The SUT as defined in Clause 4.1.0 is used to test the URLLC use case. A 5G SA Core would be required to support basic functionality to authenticate and register the end user device to establish a PDU session. An image processing server would act as an application server for this test scenario. The 5G core and application server may be a completely emulated, partially emulated or real non-emulated core and image processing server. An end user device would be an AR device for this test scenario, which may be a customized device, such as AR based eyeglass, or an AR based head mounted device or a generic handset which support AR or any AR end user device support this use case. For testing othis use case, a real end user device or an emulated one may be used. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This may be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the Internet, the additional latency should be calculated and accounted for.

The SUT shall have the correct configuration and software load. The SUT shall also be setup to run this testing in different radio conditions as outlined in Clause 4.6. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the SUT and the 5G core. The 5G core may be distributed with the UPF deployed at the edge location along with the application server to support the stringent latency requirement of the AR use case. The end user device also shall be provisioned with the user credentials to register and set up the PDU session with the 5G core and to authenticate/communicate with the application server. The application server shall be configured and provisioned with all the necessary information, including relevant images and data to support the AR use case. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network, such as the SUT, 5G core, and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to SUT, SUT shall be connected to the 5G core which in turn shall have connectivity to the application server.

# 7.87.

# Test Methodology/Procedure

Ensure the end user devices, SUT, 5G core and the application server have all been configured as outlined in Clause 7.9.1.2. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device in excellent radio condition and ensure the device registers with the �G core over SA by connecting over the SUT.   
2. Once the registration is complete, the end user device shall establish a PDU session over the URLLC network slice, followed by connection to the application server.   
3. Use the end user device to communicate with the application server for an AR session. Depending on the end user device, this could be done using a finger and/or hand to select the correct AR application, or using a button or touch activated system to select the correct AR application.   
4. Once the application has started, complete the designated task which could be playing a game or performing a pre-defined task on a machinery, troubleshooting etc.   
5. Repeat the test multiple times $( > 1 0$ times) and gather results.   
6. Repeat the above steps � through � for the good, fair and poor radio conditions.

# 7.88.

# Test Expectation (expected results)

As a pre-validation, use the traces to validate a successful registration and PDU session setup to the URLLC network slice by the end user device without any errors over SUT. Also validate the end user device can connect to the application server for the AR session. This is a prerequisite before these tests can be validated.

Validate the end user device can set up the AR session and perform the desired task eg: remote maintenance. Ensure there is no noticeable video freezing, jitter, or lag in the AR session for the end user. Use packet captures to validate there is no jitter or packet drops between the end user device and the application server. Use the packet captures to ensure there are no out-of-sequence packets which could impact the end user’s experience. Calculate the metrics, such as latency and throughput using the packet captures.

The KPIs for an Augmented Reality session varies by the use-case type, the vertical that is being supported and even the product that is being used for testing. As there is no standard application layer protocol or method used for these use-cases, vendors have developed products which have been optimized using their own propriety mechanism(s). The specific values for these KPIs depends on the product used for testing and shall be provided by the product vendor. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

The KPIs for the URLLC session vary by use-case category, use-case type and even by the vendor products used for testing. The table below [34] gives a generic list of KPI values defined by use-case category. The specific values for these KPIs depends on the product used for testing and shall be provided by the product vendor.

Table 7 SEQ Table \\* ARABIC \s 1 33 - URLLC KPIs   

<table><tr><td rowspan=1 colspan=1>Usecasegroup</td><td rowspan=1 colspan=1>Use caseexample</td><td rowspan=1 colspan=1>e2elatency</td><td rowspan=1 colspan=1>jitter</td><td rowspan=1 colspan=1>roundtriptime</td><td rowspan=1 colspan=1>e2ereliability</td><td rowspan=1 colspan=1>networkreliability</td><td rowspan=1 colspan=1>userexperiencedthroughput</td><td rowspan=1 colspan=1>networkthroughput</td><td rowspan=1 colspan=1>availability</td><td rowspan=1 colspan=1>timesynchronousaccuracy</td><td rowspan=1 colspan=1>device/connection density</td></tr><tr><td rowspan=2 colspan=1>AR/VR</td><td rowspan=1 colspan=1>Augmentedworker</td><td rowspan=1 colspan=1>10ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.9999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>VR viewbroadcast</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>&lt;20ms</td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>40-700Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3000/km2</td></tr><tr><td rowspan=1 colspan=1>Tactileinteraction</td><td rowspan=1 colspan=1>Cloud Gaming</td><td rowspan=1 colspan=1>&lt;7ms(uplink)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1 Gbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3000/km2</td></tr><tr><td rowspan=4 colspan=1>Energy</td><td rowspan=1 colspan=1>Differentialprotection</td><td rowspan=1 colspan=1>&lt;15ms</td><td rowspan=1 colspan=1>&lt;160us</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.4Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10us</td><td rowspan=1 colspan=1>10-100/km2</td></tr><tr><td rowspan=1 colspan=1>FISR</td><td rowspan=1 colspan=1>&lt;25ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10 Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10/km2</td></tr><tr><td rowspan=1 colspan=1>Faultlocationidentification</td><td rowspan=1 colspan=1>140ms</td><td rowspan=1 colspan=1>2ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.9999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100 Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5us</td><td rowspan=1 colspan=1>10/km2</td></tr><tr><td rowspan=1 colspan=1>fault mgmt.in distr.Powergeneration</td><td rowspan=1 colspan=1>&lt;30ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1>1Mbps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>&lt;2000/km2</td></tr><tr><td rowspan=3 colspan=1>Factoryofthefuture</td><td rowspan=1 colspan=1>Advancedindustrialrobotics</td><td rowspan=1 colspan=1>&lt;2ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>&lt;30mstaskplanner；&lt;1-5msrobotctrl</td><td rowspan=1 colspan=1>99.9999% to99.999999 %</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>AGV control</td><td rowspan=1 colspan=1>5ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100kbps(downlink)3-8Mbpsuplink</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Robot tooling</td><td rowspan=1 colspan=1>1msroboticmotion ctrl;1-10msmachine ctrl</td><td rowspan=1 colspan=1>&lt;50%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.9999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>UAV</td><td rowspan=1 colspan=1>UTMconnectivity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>&lt;128 bps</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Cmnd &amp; Ctrl</td><td rowspan=1 colspan=1>&lt;100ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.999%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Payload</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>app</td><td rowspan=1 colspan=1>application dependent</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>Positionmeasure-mentdeliver</td><td rowspan=1 colspan=1>for AR insmartfactory</td><td rowspan=1 colspan=1>&lt;15ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.9%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>for inboundlogistics in</td><td rowspan=1 colspan=1>&lt;10ms</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99.9%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1>manufacturing</td></tr></table>

The capability to capture data is dependent on the end user device’s capability. As a part of gathering data, it is recommended that minimum configuration parameters (see Clause 4.3) are included in the test report. The following information is also recommended to be included in the test report to provide a comprehensive view of the test setup.

End user device (real or emulated AR device):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated occupied slots (average sample per second)

# Table 7 SEQ Table \\* ARABIC \s 1 34 Example Test Report for URLLC Testing

<table><tr><td rowspan=2 colspan=2>URLLC KPIs</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Excellent</td><td rowspan=2 colspan=1>Good</td><td rowspan=2 colspan=1>Fair</td></tr><tr><td rowspan=1 colspan=1>(cell centre)</td><td></td><td rowspan=1 colspan=1>(cell edge)</td></tr><tr><td rowspan=1 colspan=2>Reliability</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>End to End Latency</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>User ExperiencedThroughput</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>Motion-to-Photonlatency</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>Motion-to-sounddelay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>HARQRetransmission</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>DL/UL Latency -User Plane</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>DL/UL Latency -Control Plane</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>L1 DL throughput[Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>L1 DL Spectralefficiency [bps/Hz]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>L3 DL PDCPthroughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>Application DLthroughput [Mbps]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>UE RSRP [dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>UE PDSCH SINR[dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>MIMO rank</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>PDSCH MCS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>PMI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>RSSI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>PDSCH BLER [%]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.48. mMTC

# 7.10.0 mMTC test introduction

The 5G network also supports a wide set of use cases which allow machine type devices to communicate with the network to realise the Internet of Things use cases. These use cases fall under the category mMTC – massive Machine Type Communication. There are a diverse set of use cases under this category which supports a range of verticals including security, healthcare, remote control, metering, smart city, etc. The 5G network has enhanced the RAN and the core to support the mMTC requirements. Some of these enhancements include supporting large numbers of mMTC devices by improving coverage and density of devices. Enhancements also include reducing the overhead for small intermittent data transmission, thus ensuring low energy usage, and extending the battery life of the mMTC devices. Network slicing in 5G allows for a telecommunication service provider to support the diverse set of mMTC use cases by dedicating a separate slice of the network for these use cases. The 3GPP has also defined a massive Machine Type Communication (mMTC) as a slice which is used to support the use case to support very large number of small devices (million to billions) in an efficient way to ensure optimal energy utilization. This clause of the document includes scenarios to test service(s) which use the mMTC slice.

Please see the below summary table of test cases and applicable technology.

Table 7SEQ Table $\backslash ^ { * }$ ARABIC $\mathbf { \ s u }$ 135: mMTC-Sensors Test Case Selection summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>Test ID</td><td rowspan=1 colspan=1>mMTC-Sensors</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7.10.1</td><td rowspan=1 colspan=1>Sensors</td><td rowspan=1 colspan=1>Service</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.132. Sensors

This test scenario validates the working of sensors over an mMTC slice on a 5G network.

7.89. Test Description

This clause provides the procedure to test the mMTC applications in a telecommunication network. mMTC comprises a diverse set of use cases supported across various verticals. Most of the mMTC use cases include an end user equipment which communicates with an application server over the 5G network. The end user device varies based on the use case, from a sensor which measure temperature, humidity, or weight, etc.; to a gauge which measures usage of electricity, or water, etc/.; to a monitoring device which measure and report vital statistics. These end user devices collect data and update the application server periodically. The application server collects the data, stores it, analyses it, and can also perform additional tasks if needed, based on the outcome of the analysis, eg: turn off equipment when the temperature is high, etc.

This clause is using sensors to perform mMTC testing. The test case includes deploying 5G sensors in the field to collect data and upload it to an application server. The sensors could vary based on the use case needed. These sensors could be air humidity sensor, temperature sensor, and soil moisture sensor used in conjunction to identify the need to irrigate a farm. These sensors could also be used to identify gas leaks to alert the authorities, or turn off gas lines. These sensors could also be light/image sensors which can be used to identify if a parking spot is occupied. There are numerous sensors which support a varied set of use cases, but this test case has been intentionally left generic without specifying the type of sensor that will be used for testing.

The 5G mMTC network slice does not have requirements on the protocol, or the method used to communicate between the end user device and the application server. The 5G network slice acts as a pipe to allow communication between these two end points, the sensors and application server, with the low energy utilization and the ability to support massive number of such sensors to connect.

7.90. Test Setup

The SUT as defined in Clause 4.1.0 is used to test the mMTC use case. A 5G SA core shall be required to support basic functionality to authenticate and register the end user device(s) to establish a PDU session. An application server which has the capability to collect data from different end user devices(s)/sensor(s) which will be used for testing. The 5G core and application server may be a completely emulated, partially emulated or real non-emulated core. The end user device(s) in this scenario may be a single or a group of sensors which can communicate over 5G. For the testing of this use case, either real end user device(s) or emulated devices which emulate the different sensor(s) may be used. The test setup shall include tools which can collect traces on the elements and/or packet captures of communication between the elements. This may be a built-in capability of the emulated/non-emulated network elements or an external tool. Optionally, if some of the network elements are located remotely either in a cloud or on the Internet, the additional latency should be calculated and accounted for.

The SUT shall have the correct configuration and software load. The SUT shall also be setup to run this testing in different radio conditions as outlined in Clause 4.6. The end user device shall be configured with the correct user credentials to be able to register and authenticate with the O-RAN system and the 5G core. The end user device also shall be provisioned with the user credentials to register and set up the PDU session with the 5G core and authenticate/communicate with the application server. The application server shall be configured and provisioned with all the necessary information to connect to the different sensors and the values. The locations where the radio conditions are excellent, good, fair and poor shall be identified within the serving cell.

All the elements in the network, such as the SUT, 5G core and the application server should have the ability to capture traces to validate the successful execution of the test cases. The end user devices should have the capability to capture traces/packets to calculate the KPIs. Optionally, the network may have network taps deployed in various legs of the network to get packet captures to validate successful execution of the test cases. All these different components shall have connectivity with each other – the end user device shall be able to connect to SUT, SUT shall be connected to the 5G core which in turn shall have connectivity to the application server.

# 7.91.

# Test Methodology/Procedure

Ensure the end user devices, SUT, 5G core and the application server have all been configured as outlined in Clause 7.10.1.2. All traces and packet captures shall be enabled for the duration of the testing to ensure all communication between network elements can be captured and validated.

1. Power on the end user device(s) in excellent radio condition and ensure the device registers with the �G core over SA by connecting over the SUT. Depending on the type of mMTC device this could be done by pushing the power button on the end user device or could be by connecting the end user device to a battery or power source.   
2. Once the registration is complete, the end user device(s) shall establish a PDU session over the mMTC network slice, followed by connection to the application server.   
3. Based on the type of mMTC device, additional steps may be required the first time the device is connected to the network, to enable the device to register with the application server. This could include adding the end user device to the application server using a unique ID or/and unique security code etc.   
4. Validate the end user device can communicate with the application server periodically and update the sensor data.   
5. Let the test run for long enough duration of time so that the end user device(s) can upload enough data to the application server.   
6. Repeat the above steps � through � for the good, fair and poor radio conditions.

As a pre-validation, use the traces to validate a successful registration and PDU session setup to the mMTC network slice by the end user devices without any errors over SUT. Also validate the end user devices can connect to the application server. This is a prerequisite before these tests can be validated. Validate the end user devices can connect to the application server and update the sensor data periodically. Validate the application server can receive the data from the sensors, process it and take the necessary action – updating charts and report, triggering secondary actions, etc. Use packet captures to validate there are no packet drops between the end user device and the application server. Calculate the metrics, such as the latency and throughput using the packet captures.

The KPIs for the mMTC session vary by use-case category, use-case type, and even by the vendor products used for testing. As there is no standard application layer protocol or method used for these usecases, vendors have developed products which have been optimized using their own propriety mechanism(s). The specific values for these KPIs depends on the product used for testing and shall be provided by the product vendor. As there are multiple variables which can impact the testing in this scenario, a KPI outcome outside the range does not necessarily point to a failure within the SUT.

The capability to capture data is dependent on the end user device’s capability. As a part of gathering data, it is recommended that minimum configuration parameters (see Clause 4.3) are included in the test report. The following information is also recommended to be included in the test report to provide a comprehensive view of the test setup.

End user device (real or emulated sensors):

• Radio parameters such as RSRP, RSRQ, PDSCH SINR (average sample per second) PDSCH BLER, PDSCH MCS, MIMO rank (number of layers) (average sample per second) Downlink transmission mode Channel utilization, i.e. Number of allocated/occupied downlink PRBs and Number of allocated/ occupied slots (average sample per second)

Table 7 SEQ Table $\backslash ^ { * }$ ARABIC \s 1 36 Example Test Report for mMTC Testing   

<table><tr><td rowspan=2 colspan=1>MMTC KPIs</td><td rowspan=1 colspan=1>Excellent</td><td rowspan=2 colspan=1>Good</td><td rowspan=2 colspan=1>Fair</td><td rowspan=1 colspan=1>Poor</td></tr><tr><td rowspan=1 colspan=1>(cell centre)</td><td rowspan=1 colspan=1>(cell edge)</td></tr><tr><td rowspan=1 colspan=1>RACH SuccessRate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Paging SuccessRate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRP[dBm]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE RSRQ</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>UE PDSCHSINR [dB]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>CQI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Packet delay</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Buffer Status</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DRX SleepTime</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 8. Load and stress tests

# 4.49. Load and stress tests introduction

This clause describes the tests evaluating and assessing the load and stress tests of the radio access network from a network end-to-end perspective. The focus of the testing is on the tolerability of the SUT under load based on 3GPP and O-RAN specifications.

The SUT shall have an ability to handle the various traffic patterns and loads which could happen in a real field deployment. The load and stress tests are used to evaluate the tolerability of SUT against loading and

traffic in a laboratory setting. These tests may uncover problems that are difficult to observe and correct in the field. Load and stress tests in addition to Functional testing thereby help ensure the final quality of the SUT. It leads to improve the overall quality of the system, which in turn improve the user experience.

The tests also cover special calling features, such as placing an Emergency Call.   
Please see below summary table of test cases and applicable technology.

Table 8 SEQ Table \\* ARABIC \s 1 1: Load and Stress Tests summary   

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3>Applicabletechnology</td></tr><tr><td rowspan=1 colspan=2>Test case</td><td rowspan=1 colspan=1>Functionalgroup</td><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1>NSA</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>TESTID</td><td rowspan=1 colspan=1>Load and Stress Tests</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8.1</td><td rowspan=1 colspan=1>Simultaneous RRC_CONNECTED UEs</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.2</td><td rowspan=1 colspan=1>UE State Transition Rate Testing</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.3</td><td rowspan=1 colspan=1>Traffic Load Testing</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.4</td><td rowspan=1 colspan=1>Traffic Model Testing</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.5</td><td rowspan=1 colspan=1>Long hours stability Testing</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.6</td><td rowspan=1 colspan=1>Multi-cell Testing</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.7</td><td rowspan=1 colspan=1>Emergency call</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.8</td><td rowspan=1 colspan=1>ETWS (Earthquake and Tsunami Warning System)</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr><tr><td rowspan=1 colspan=1>8.9</td><td rowspan=1 colspan=1>MPS Call</td><td rowspan=1 colspan=1>Load and Stress</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>Y</td></tr></table>

# 4.50. Simultaneous RRC_CONNECTED UEs

# 4.133. Test description and applicability

The purpose of this test is to connect multiple UEs to the SUT and measure the maximum number of UEs that can be simultaneously maintained in RRC_CONNECTED state. By connecting multiple UEs at the same time, a basic SUT capacity is verified. This test is valid with either LTE or 5G NSA/SA. The test procedure is to stack the number of connected UEs to the SUT one by one and check the maximum number of simultaneous connected UEs. To perform this test, the connected UEs transmit a minimum size of U-Plane packet periodically such as ping to keep the RRC_CONNECTED state. The transmit interval of the packets shall be shorter than RRC inactivity timer value in SUT. Figure 81 illustrates how the test works.

![](images/5b8d20d34eebb622838ac9448a79c0d24901160666a97cefbec1752555a9fa32.jpg)

> **Image Summary:** {"image": "image.png"}


# Figure 8 SEQ Figure \\* ARABIC \s 1 1 Simultaneous RRC_CONNECTED UEs

4.134. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with multiple UEs placed under excellent radio conditions (see Clause 4.6).

Since this test scenario requires a large number of UE connections, it is recommended to use equipment that emulates a large number of UEs.

This test is aimed at C-Plane (i.e., RRC, PDCP and RLC) capacity benchmarking, where a maximum capacity load shall be applied in accordance with Clause 4.1.1.

Test configuration: The test configuration is not specified. The utilized test configuration (connection diagram between SUT and test equipment, parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment shall be setup to achieve excellent radio conditions (LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA/SA) as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) shall not be exceeded.

# 4.135. Test procedure

The test steps below are applicable for either LTE or 5G NSA/SA:

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.   
2. The UEs are placed under excellent radio conditions (Cell centre close to radiated SUT’s Antenna) as defined by LTE RSRP (for LTE) or �G SS-RSRP (for �G NSA/SA) in Clause �.�.   
3. The End-to-end setup shall be operational for LTE or �G NSA/SA as applicable for the test scenario, and there should not be any connectivity issues.   
4. Required performance data (incl. the signalling and control data) as specified in the “Test requirements” clause below shall be measured and captured at the UE(s) and SUT side using logging/measurement tools.   
5. "Power ON" the UEs one by one, connect them to the LTE or 5G NSA/SA cell, and confirm that they are in the RRC_CONNECTED state normally. The UE in RRC_CONNECTED state, to keep their RRC connection, periodically sends some data packets like Ping. The connection holding time shall be at least 3 minutes in Figure 81 to be sufficient for the test. Increase the number of UEs until the newly powered UE fails to connect to LTE or 5G NSA/SA cell. 5.a.Start with a number of 100 UEs and further increase the number of UEs in increments of 100, until a newly powered on UE fails to connect. Connect the UEs sequentially at a reasonable rate; the recommended rate is 10 UEs per second. 5.b. From the last increment, where all UEs connected successfully, repeat the process of increasing the number of UEs in increments of 10, until a newly powered on UE fails to connect. Connect the UEs sequentially at the same rate as before.

5.c.From the last increment, where all UEs connected successfully, repeat the process of increasing the number of UEs in increments of 1, until a newly powered on UE fails to connect. Connect the UEs sequentially at the same rate as before.

6. If all newly powered UEs successfully "Power ON" during one of the UE number increments in step �, the Uu with optional additional OpenFH and/or F� interface and test equipment (see Clause �.�.�) should be used to add more UEs until a newly powered UE fails to connect

7. Lost connections shall be re-established automatically to maximize number of RRC Connected UEs.

8. Stop and save the test logs. Check the log to make sure that the test runs successfully and that no unexpected behavior such as unexpected call release is recorded. The logs shall be captured and kept for test result reference and measurements.

# 4.136. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for performance assessment.

Radio parameters such as RSRP, RSRQ   
KPIs mentioned in Table ��   
SUT load/capacity/performance related KPIs (e.g., CPU and MEMORY utilization) if   
any

Validate the successful procedures from the collected logs. Check the maximum number of UE connections. For the UE(s) which call loss has occurred in this test more than a certain percentage (e.g., $2 \%$ ), the validity of the cause of the call loss shall be confirmed.

Table 8 SEQ Table \\* ARABIC \s 1 2 Maximum Number of simultaneous RRC_CONNECTED UEs   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Miaximum Number of simultaneousRRC_CONNECTED UEs</td></tr><tr><td rowspan=1 colspan=1>LTE</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NR(NSA)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NR (SA)</td><td rowspan=1 colspan=1></td></tr></table>

# 4.51. UE State Transition Rate Testing

# 4.137. Test description and applicability

The purpose of this test is to benchmark the number of UE state transitions that can be processed by the control plane per unit time by connecting multiple UEs with various state transitions to an SUT.

As shown in Figure 82, an incrementally increasing number of UEs are attached during each period of ‘X seconds’. UE traffic shall repeatedly perform UE state transitions (transition RRC_IDLE to/from RRC_CONNECTED) over the $\mathbf { \Delta } ^ { \prime } \mathbf { X }$ seconds’ duration of the test. After each ‘X seconds’, the UE powers shall be off. In the first interval of X seconds 100 UEs should be attached sequentially and keep on

performing UE state transitions for the rest of the interval. The recommended rate for the UEs to attach is 10 UEs per second. When the interval ends all UEs should detach. In the following intervals of X seconds this behaviour is replicated with an increasing number of UEs. The number of UEs shall increase by 100 for each following interval until a failure at connect occurs. When a failure to connect occurs the number of UEs shall increase by 10 UEs, from the last number of UEs which could connect without problem, by each following interval of X seconds until a failure to connect occurs. When a failure to connect occurs the number of UEs shall increase by 1 UE, from the last number of UEs which could connect without problem, by each following interval of X seconds until a failure to connect occurs. By connecting multiple UEs at the same time, the basic SUT control plane processing throughput is verified. This test is valid with either LTE or 5G NSA/SA.

The value of X is determined by the following formula, with I being the RRC Inactivity timer in seconds of the SUT and R being the maximum number of simultaneous RRC_CONNECTED UEs as determined by the result of test case 8.1:

Note: The formula ensures that 5 state transitions take place by including 10 times the RRC Inactivity timer of the SUT. For the 5 state transitions the ping interval also should be 2 times I. The second part of the formula (R/10) ensures that there is enough time in each interval of X seconds to connect the maximum number of UEs to the SUT using the recommended rate of 10 UEs per second.

The test procedure is to gradually increase the number of UEs connected to the SUT and check the maximum number of simultaneously connected UEs as they perform state transition. In order to transition the RRC_CONNECTED state and the RRC_IDLE state of the UE alternately and continuously, the UEs shall periodically transmit a minimum size of U-Plane packet such as a Ping. The transmit interval of the packets shall be longer than RRC inactivity timer value in SUT. By repeating state transitions by many UEs, test a limit of SUT processing capacity. In addition, by repeating the call generation and call release, it can be confirmed that there are no problems such as processing delays and memory release leaks.

![](images/78d1f09c508f1e4dc9013d107dd013222e1911a0cb1ea0d16f63cdbd3d4bb7b6.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 8 SEQ Figure \\* ARABIC \s 1 2 Benchmark of UE State Transition

# 4.138. Test setup and configuration

The test setup is a single cell scenario (i.e., isolated cell without any inter-cell interference – see Clause 4.7) with multiple UEs placed under excellent radio conditions (see Clause 4.6).

Since this test scenario requires a large number of UE connections, it is recommended to use equipment that emulates a large number of UEs.

This test is primarily C-Plane (i.e., RRC, PDCP and RLC) capacity benchmarking, where a maximum capacity load shall be applied in accordance with Clause 4.1.1.

Test configuration: The test configuration is not specified. The utilized test configuration (connection diagram between SUT and test equipment, parameters) shall be recorded in the test report.

Laboratory setup: The radio conditions experienced by the UE can be modified using a variable attenuator inserted between the antenna connectors (if available) of the O-RU and the UE, or appropriately emulated using a UE emulator. The test environment shall be setup to achieve excellent radio conditions (LTE RSRP (for LTE) or 5G SS-RSRP (for 5G NSA/SA) as defined in Clause 4.6) for the UE, but the minimum coupling loss (see Clause 4.6) shall not be exceeded.

# 4.139. Test procedure

The test steps below are applicable for either LTE or 5G NSA/SA:

1. The test setup is configured according to the test configuration. The test configuration shall be recorded in the test report. The serving cell under test is activated and unloaded. All other cells are powered off.

2. The UEs are placed under excellent radio conditions (Cell centre close to radiated SUT’s Antenna) as defined by LTE RSRP (for LTE) or �G SS-RSRP (for �G NSA/SA) in Clause �.�.

3. The End-to-end setup shall be operational for LTE or �G NSA/SA as applicable for the test scenario, and there should not be any connectivity issues.

4. Required performance data (incl. the signalling and control data) as specified in the “Test requirements” clause below shall be measured and captured at the UE(s) and SUT side using logging/measurement tools.

5. Sequentially “Power ON” the current number of UEs at a reasonable rate such as �� UEs per second, starting with ��� UEs, to attach to the LTE or �G NSA/SA cell. Observe the state transitions of each UE by checking by the state of receiving control plane messages.

6. After an interval of $^ { \circ } \mathbb { X }$ seconds’ all UEs are then “Powered off”. It shall be checked whether there are any UEs that have failed to make the RRC state transition at the SUT.

7. Run steps � and � again with an increased number of UEs. Each interval of ʻX seconds’ the number of UEs shall increase by ��� UEs until a failure to connect occurs. At this point during the next ʻX seconds’-interval the previously working number of UEs shall be used. In each following interval of ʻX seconds’ the number of UEs should increase by �� UEs until a failure to connect occurs. At this point during the next $^ { \circ } \mathbb { X }$ seconds’- interval the previously working number of UEs is used. In each following interval of ʻX seconds’ the number of UEs shall be increased by � UE until a failure to connect occurs, at which point the test cases moves on to step �.

8. Stop and save the test logs. Check the log to make sure that the test runs successfully and that no unexpected behavior such as unexpected call release is recorded. The logs shall be captured and kept for test result reference and measurements.

# 4.140. Test requirements (expected results)

In addition to the common minimum set of configuration parameters (see Clause 4.3), the following metrics and counters shall be captured and reported in the test report for performance assessment.

Radio parameters such as RSRP, RSRQ   
KPIs mentioned in Table ��   
SUT load/capacity/performance related KPIs (e.g., CPU and MEMORY utilization) if   
any

Validate the successful procedures from the collected logs. Check the rate of UE state transition that can be processed per unit time. For the UE(s) in which call loss has occurred in a X seconds test more than a certain percentage (e.g., $2 \%$ ), the validity of the cause of the call loss shall be confirmed.

Table 8 SEQ Table \\* ARABIC \s 1 3 Maximum Rate of UE State Transition   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Maximum Rate of UE StateTransition(per second)</td><td rowspan=1 colspan=1>Number of UEs</td></tr><tr><td rowspan=1 colspan=1>TE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NR(NSA)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NR (SA)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.52. Traffic Load Testing

# 4.141. Test description and applicability

The purpose of this test is to check the stability of the SUT under load, with a large number of UEs sending and receiving user data. By connecting a large number of UEs at the same time, the SUT processing capacity and stability are verified. The maximum cell throughput is discussed in Clause 6 and is out of scope of this test. This test is valid with either LTE or 5G SA.

The test procedure is to connect X UEs per second to the SUT with UDP download/upload traffic until N UEs are connected. Then disconnect X UEs per second and reconnected X new UEs per second to the SUT with UDP download/upload traffic. Continue disconnecting and connecting UEs near the maximum number of UEs to verify a stability of SUT. It is recommended that the total UDP traffic be less than the maximum cell throughput, as maximum cell throughput is out of scope for this test.

The values of X and N are determined by the result of test case 8.1, i.e., the maximum number of simultaneous RRC_CONNECTED UEs (denoted as R), and the following equations: