######## Annex A (normative): Measurement channels

A.1 General
===========

The throughput values defined in the measurement channels specified in
Annex A, are calculated and are valid per datastream (codeword). For
multi-stream (more than one codeword) transmissions, the throughput
referenced in the minimum requirements is the sum of throughputs of all
datastreams (codewords).

The UE category entry in the definition of the reference measurement
channel in Annex A is only informative and reveals the UE categories,
which can support the corresponding measurement channel. Whether the
measurement channel is used for testing a certain UE category or not is
specified in the individual minimum requirements.

A.2 UL reference measurement channels
=====================================

A.2.1 General
-------------

The measurement channels in the following clauses are defined to derive
the requirements in clause 6 (Transmitter Characteristics) and clause 7
(Receiver Characteristics). The measurement channels represent example
configurations of physical channels for different data rates.

The measurement channels in the following clauses are applicable to both
FDD and TDD.

The active uplink slots for TDD configurations are specified in table
A.2.1-1. TDD slot patterns defined for reference sensitivity tests will
be used for TDD UL RMCs. The active uplink slots configuration specified
in Table A.2.1-2 and the additional TDD pattern in Table A.2.1-3 are
used for shorter transient period capability EVM tests at 15 kHz SCS.

Table A.2.1-1: TDD active uplink slots

  SCS      Active Uplink slots
  -------- --------------------------------
  15 kHz   4, 9
  30 kHz   8, 9, 18, 19
  60 kHz   16, 17, 18, 19, 36, 37, 38, 39

Table A.2.1-2: TDD active uplink slots for shorter transient period
capability

+----------+---------------------+
| > SCS    | Active Uplink slots |
+==========+=====================+
| > 15 kHz | 3,4                 |
+----------+---------------------+

Table A.2.1-3: Additional TDD pattern for shorter transient period
capability

+------------------------------+------------------------------+------+
| Parameter                    | Value                        |      |
+==============================+==============================+======+
|                              | SCS 15 kHz (µ0)              |      |
+------------------------------+------------------------------+------+
| TDD Slot Configuration       | 2DS2U                        |      |
| pattern (Note 1)             |                              |      |
+------------------------------+------------------------------+------+
| Special Slot Configuration   | 10D+2G+2U                    |      |
| (Note 2)                     |                              |      |
+------------------------------+------------------------------+------+
| referenceSubcarrierSpacing   | 15 kHz                       |      |
+------------------------------+------------------------------+------+
| UL-DL configuration          | *dl                          | 5 ms |
|                              | -UL-TransmissionPeriodicity* |      |
+------------------------------+------------------------------+------+
|                              | *nrofDownlinkSlots*          | 2    |
+------------------------------+------------------------------+------+
|                              | *nrofDownlinkSymbols*        | 10   |
+------------------------------+------------------------------+------+
|                              | *nrofUplinkSlot*             | 2    |
+------------------------------+------------------------------+------+
|                              | *nrofUplinkSymbols*          | 2    |
+------------------------------+------------------------------+------+
| NOTE 1: D denotes a slot     |                              |      |
| with all DL symbols; S       |                              |      |
| denotes a slot with a mix of |                              |      |
| DL, UL and guard symbols; U  |                              |      |
| denotes a slot with all UL   |                              |      |
| symbols. The field is for    |                              |      |
| information.                 |                              |      |
|                              |                              |      |
| NOTE 2: D, G, U denote DL,   |                              |      |
| guard and UL symbols,        |                              |      |
| respectively. The field is   |                              |      |
| for information.             |                              |      |
+------------------------------+------------------------------+------+

### 

A.2.2 Reference measurement channels
------------------------------------

### A.2.2.1 DFT-s-OFDM Pi/2-BPSK

Table A.2.2.1-1: Reference Channels for DFT-s-OFDM Pi/2-BPSK

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>DFT-s-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td>1</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>24</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>132</td>
<td>132</td>
</tr>
<tr class="odd">
<td> </td>
<td>5</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>160</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>660</td>
<td>660</td>
</tr>
<tr class="even">
<td> </td>
<td>9</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>288</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1188</td>
<td>1188</td>
</tr>
<tr class="odd">
<td> </td>
<td>10</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>320</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1320</td>
<td>1320</td>
</tr>
<tr class="even">
<td> </td>
<td>12</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>384</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1584</td>
<td>1584</td>
</tr>
<tr class="odd">
<td> </td>
<td>15</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>480</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1980</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>576</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2376</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>24</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>768</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3168</td>
<td>3168</td>
</tr>
<tr class="even">
<td> </td>
<td>25</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>808</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3300</td>
<td>3300</td>
</tr>
<tr class="odd">
<td> </td>
<td>30</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>984</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3960</td>
<td>3960</td>
</tr>
<tr class="even">
<td> </td>
<td>32</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>1032</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4224</td>
<td>4224</td>
</tr>
<tr class="odd">
<td> </td>
<td>36</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>1128</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4752</td>
<td>4752</td>
</tr>
<tr class="even">
<td></td>
<td>45</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>1416</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5940</td>
<td>5940</td>
</tr>
<tr class="odd">
<td> </td>
<td>50</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>1544</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6600</td>
<td>6600</td>
</tr>
<tr class="even">
<td> </td>
<td>60</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>1864</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7920</td>
<td>7920</td>
</tr>
<tr class="odd">
<td> </td>
<td>64</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>2024</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>8448</td>
<td>8448</td>
</tr>
<tr class="even">
<td> </td>
<td>75</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>2408</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>9900</td>
<td>9900</td>
</tr>
<tr class="odd">
<td> </td>
<td>80</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>2472</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10560</td>
<td>10560</td>
</tr>
<tr class="even">
<td> </td>
<td>81</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>2536</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10692</td>
<td>10692</td>
</tr>
<tr class="odd">
<td></td>
<td>90</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>2792</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>11880</td>
<td>11880</td>
</tr>
<tr class="even">
<td> </td>
<td>100</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>3104</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>13200</td>
<td>13200</td>
</tr>
<tr class="odd">
<td> </td>
<td>108</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>3368</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>14256</td>
<td>14256</td>
</tr>
<tr class="even">
<td> </td>
<td>120</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>3752</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>15840</td>
<td>15840</td>
</tr>
<tr class="odd">
<td> </td>
<td>128</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>3976</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>16896</td>
<td>16896</td>
</tr>
<tr class="even">
<td> </td>
<td>135</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>4104</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>17820</td>
<td>17820</td>
</tr>
<tr class="odd">
<td> </td>
<td>160</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>4872</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21120</td>
<td>21120</td>
</tr>
<tr class="even">
<td> </td>
<td>162</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>5000</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21384</td>
<td>21384</td>
</tr>
<tr class="odd">
<td></td>
<td>180</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>5512</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>23760</td>
<td>23760</td>
</tr>
<tr class="even">
<td> </td>
<td>216</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>6664</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>28512</td>
<td>28512</td>
</tr>
<tr class="odd">
<td></td>
<td>243</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>7560</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>32076</td>
<td>32076</td>
</tr>
<tr class="even">
<td></td>
<td>270</td>
<td>11</td>
<td>pi/2 BPSK</td>
<td>0</td>
<td>8448</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>35640</td>
<td>35640</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 6.1.4.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.1-2: Void

Table A.2.2.1-3: Void

### A.2.2.2 DFT-s-OFDM QPSK

Table A.2.2.2-1: Reference Channels for DFT-s-OFDM QPSK

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>DFT-s-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td>1</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>48</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>264</td>
<td>132</td>
</tr>
<tr class="odd">
<td> </td>
<td>5</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>256</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1320</td>
<td>660</td>
</tr>
<tr class="even">
<td> </td>
<td>9</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>456</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2376</td>
<td>1188</td>
</tr>
<tr class="odd">
<td> </td>
<td>10</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>504</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2640</td>
<td>1320</td>
</tr>
<tr class="even">
<td> </td>
<td>12</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>608</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3168</td>
<td>1584</td>
</tr>
<tr class="odd">
<td> </td>
<td>15</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>768</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3960</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>928</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4752</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>20</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1032</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5280</td>
<td>2640</td>
</tr>
<tr class="even">
<td> </td>
<td>24</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1192</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6336</td>
<td>3168</td>
</tr>
<tr class="odd">
<td> </td>
<td>25</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1256</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6600</td>
<td>3300</td>
</tr>
<tr class="even">
<td> </td>
<td>30</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1544</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7920</td>
<td>3960</td>
</tr>
<tr class="odd">
<td> </td>
<td>32</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1608</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>8448</td>
<td>4224</td>
</tr>
<tr class="even">
<td> </td>
<td>36</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1800</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>9504</td>
<td>4752</td>
</tr>
<tr class="odd">
<td></td>
<td>45</td>
<td>11</td>
<td>QPKS</td>
<td>2</td>
<td>2208</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>11880</td>
<td>5940</td>
</tr>
<tr class="even">
<td> </td>
<td>50</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2472</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>13200</td>
<td>6600</td>
</tr>
<tr class="odd">
<td> </td>
<td>60</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3104</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>15840</td>
<td>7920</td>
</tr>
<tr class="even">
<td> </td>
<td>64</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3240</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>16896</td>
<td>8448</td>
</tr>
<tr class="odd">
<td> </td>
<td>75</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3752</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>19800</td>
<td>9900</td>
</tr>
<tr class="even">
<td> </td>
<td>80</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3976</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21120</td>
<td>10560</td>
</tr>
<tr class="odd">
<td> </td>
<td>81</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>4040</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21384</td>
<td>10692</td>
</tr>
<tr class="even">
<td></td>
<td>90</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>4488</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>23760</td>
<td>11880</td>
</tr>
<tr class="odd">
<td> </td>
<td>100</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5000</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>26400</td>
<td>13200</td>
</tr>
<tr class="even">
<td> </td>
<td>108</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5384</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>28512</td>
<td>14256</td>
</tr>
<tr class="odd">
<td> </td>
<td>120</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5896</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>31680</td>
<td>15840</td>
</tr>
<tr class="even">
<td> </td>
<td>128</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6408</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>33792</td>
<td>16896</td>
</tr>
<tr class="odd">
<td> </td>
<td>135</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6664</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>35640</td>
<td>17820</td>
</tr>
<tr class="even">
<td> </td>
<td>160</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>7944</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>42240</td>
<td>21120</td>
</tr>
<tr class="odd">
<td></td>
<td>162</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>8064</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>42768</td>
<td>21384</td>
</tr>
<tr class="even">
<td></td>
<td>180</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>8976</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>47520</td>
<td>23760</td>
</tr>
<tr class="odd">
<td></td>
<td>216</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>10752</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>57024</td>
<td>28512</td>
</tr>
<tr class="even">
<td></td>
<td>243</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>12040</td>
<td>24</td>
<td>2</td>
<td>4</td>
<td>64152</td>
<td>32076</td>
</tr>
<tr class="odd">
<td></td>
<td>270</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>13320</td>
<td>24</td>
<td>2</td>
<td>4</td>
<td>71280</td>
<td>35640</td>
</tr>
<tr class="even">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 6.1.4.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.2-2: Void

Table A.2.2.2-3: Void

### A.2.2.3 DFT-s-OFDM 16QAM

Table A.2.2.3-1: Reference Channels for DFT-s-OFDM 16QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>DFT-s-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td>1</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>176</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>528</td>
<td>132</td>
</tr>
<tr class="odd">
<td> </td>
<td>5</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>888</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2640</td>
<td>660</td>
</tr>
<tr class="even">
<td> </td>
<td>9</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1608</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4752</td>
<td>1188</td>
</tr>
<tr class="odd">
<td> </td>
<td>10</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1800</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5280</td>
<td>1320</td>
</tr>
<tr class="even">
<td> </td>
<td>12</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2088</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6336</td>
<td>1584</td>
</tr>
<tr class="odd">
<td> </td>
<td>15</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2664</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7920</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>3240</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>9504</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>24</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>4224</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>12672</td>
<td>3168</td>
</tr>
<tr class="even">
<td> </td>
<td>25</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>4352</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>13200</td>
<td>3300</td>
</tr>
<tr class="odd">
<td> </td>
<td>30</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>5248</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>15840</td>
<td>3960</td>
</tr>
<tr class="even">
<td> </td>
<td>32</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>5632</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>16896</td>
<td>4224</td>
</tr>
<tr class="odd">
<td> </td>
<td>36</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>6272</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>19008</td>
<td>4752</td>
</tr>
<tr class="even">
<td></td>
<td>45</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>7808</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>23760</td>
<td>5940</td>
</tr>
<tr class="odd">
<td> </td>
<td>50</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>8712</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>26400</td>
<td>6600</td>
</tr>
<tr class="even">
<td> </td>
<td>60</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>10504</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>31680</td>
<td>7920</td>
</tr>
<tr class="odd">
<td> </td>
<td>64</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>11272</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>33792</td>
<td>8448</td>
</tr>
<tr class="even">
<td> </td>
<td>75</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>13064</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>39600</td>
<td>9900</td>
</tr>
<tr class="odd">
<td> </td>
<td>80</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>14088</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>42240</td>
<td>10560</td>
</tr>
<tr class="even">
<td> </td>
<td>81</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>14088</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>42768</td>
<td>10692</td>
</tr>
<tr class="odd">
<td> </td>
<td>100</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>17424</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>52800</td>
<td>13200</td>
</tr>
<tr class="even">
<td> </td>
<td>108</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>18960</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>57024</td>
<td>14256</td>
</tr>
<tr class="odd">
<td> </td>
<td>120</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>21000</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>63360</td>
<td>15840</td>
</tr>
<tr class="even">
<td> </td>
<td>128</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>22536</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>67584</td>
<td>16896</td>
</tr>
<tr class="odd">
<td> </td>
<td>135</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>23568</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>71280</td>
<td>17820</td>
</tr>
<tr class="even">
<td> </td>
<td>160</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>28168</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>84480</td>
<td>21120</td>
</tr>
<tr class="odd">
<td> </td>
<td>162</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>28168</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>85536</td>
<td>21384</td>
</tr>
<tr class="even">
<td></td>
<td>216</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>37896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>114048</td>
<td>28512</td>
</tr>
<tr class="odd">
<td></td>
<td>243</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>128304</td>
<td>32076</td>
</tr>
<tr class="even">
<td></td>
<td>270</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>47112</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>142560</td>
<td>35640</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 6.1.4.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.3-2: Void

Table A.2.2.3-3: Void

### A.2.2.4 DFT-s-OFDM 64QAM

Table A.2.2.4-1: Reference Channels for DFT-s-OFDM 64QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>DFT-s-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td>1</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>408</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>792</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>2024</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3960</td>
<td>660</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>3624</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7128</td>
<td>1188</td>
</tr>
<tr class="odd">
<td> </td>
<td>10</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>3968</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>7920</td>
<td>1320</td>
</tr>
<tr class="even">
<td></td>
<td>12</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>4736</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>9504</td>
<td>1584</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>6016</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>11880</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>7168</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>14256</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>24</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>9480</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19008</td>
<td>3168</td>
</tr>
<tr class="even">
<td> </td>
<td>25</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>9992</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19800</td>
<td>3300</td>
</tr>
<tr class="odd">
<td> </td>
<td>30</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>12040</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>23760</td>
<td>3960</td>
</tr>
<tr class="even">
<td></td>
<td>32</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>12808</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>25344</td>
<td>4224</td>
</tr>
<tr class="odd">
<td> </td>
<td>36</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>14344</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>28512</td>
<td>4752</td>
</tr>
<tr class="even">
<td></td>
<td>45</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>17928</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>35640</td>
<td>5940</td>
</tr>
<tr class="odd">
<td> </td>
<td>50</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>19968</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>39600</td>
<td>6600</td>
</tr>
<tr class="even">
<td></td>
<td>60</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>24072</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>47520</td>
<td>7920</td>
</tr>
<tr class="odd">
<td> </td>
<td>64</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>25608</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>50688</td>
<td>8448</td>
</tr>
<tr class="even">
<td> </td>
<td>75</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>30216</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>59400</td>
<td>9900</td>
</tr>
<tr class="odd">
<td></td>
<td>80</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>31752</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>63360</td>
<td>10560</td>
</tr>
<tr class="even">
<td></td>
<td>81</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>32264</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>64152</td>
<td>10692</td>
</tr>
<tr class="odd">
<td></td>
<td>90</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>35856</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>71280</td>
<td>11880</td>
</tr>
<tr class="even">
<td> </td>
<td>100</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>39936</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>79200</td>
<td>13200</td>
</tr>
<tr class="odd">
<td></td>
<td>108</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>85536</td>
<td>14256</td>
</tr>
<tr class="even">
<td> </td>
<td>120</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>48168</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>95040</td>
<td>15840</td>
</tr>
<tr class="odd">
<td> </td>
<td>128</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>51216</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>101376</td>
<td>16896</td>
</tr>
<tr class="even">
<td> </td>
<td>135</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>54296</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>106920</td>
<td>17820</td>
</tr>
<tr class="odd">
<td> </td>
<td>160</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>63528</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>126720</td>
<td>21120</td>
</tr>
<tr class="even">
<td> </td>
<td>162</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>64552</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>128304</td>
<td>21384</td>
</tr>
<tr class="odd">
<td></td>
<td>180</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>71688</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>142560</td>
<td>23760</td>
</tr>
<tr class="even">
<td> </td>
<td>216</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>86040</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>171072</td>
<td>28512</td>
</tr>
<tr class="odd">
<td> </td>
<td>243</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>96264</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>192456</td>
<td>32076</td>
</tr>
<tr class="even">
<td> </td>
<td>270</td>
<td>11</td>
<td>64QAM</td>
<td>18</td>
<td>108552</td>
<td>24</td>
<td>1</td>
<td>13</td>
<td>213840</td>
<td>35640</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 6.1.4.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.4-2: Void

Table A.2.2.4-3: Void

### A.2.2.5 DFT-s-OFDM 256QAM

Table A.2.2.5-1: Reference Channels for DFT-s-OFDM 256QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>DFT-s-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td>1</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>704</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1056</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>3496</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5280</td>
<td>660</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>6272</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>9504</td>
<td>1188</td>
</tr>
<tr class="odd">
<td> </td>
<td>10</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>7040</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>10560</td>
<td>1320</td>
</tr>
<tr class="even">
<td></td>
<td>12</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>8456</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>12672</td>
<td>1584</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>10504</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>15840</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>12552</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19008</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>24</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>16896</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>25344</td>
<td>3168</td>
</tr>
<tr class="even">
<td> </td>
<td>25</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>17424</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>26400</td>
<td>3300</td>
</tr>
<tr class="odd">
<td> </td>
<td>30</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>21000</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>31680</td>
<td>3960</td>
</tr>
<tr class="even">
<td></td>
<td>32</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>22536</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>33792</td>
<td>4224</td>
</tr>
<tr class="odd">
<td> </td>
<td>36</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>25104</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>38016</td>
<td>4752</td>
</tr>
<tr class="even">
<td></td>
<td>45</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>31752</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>47520</td>
<td>5940</td>
</tr>
<tr class="odd">
<td> </td>
<td>50</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>34816</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>52800</td>
<td>6600</td>
</tr>
<tr class="even">
<td></td>
<td>60</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>42016</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>63360</td>
<td>7920</td>
</tr>
<tr class="odd">
<td> </td>
<td>64</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>45096</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>67584</td>
<td>8448</td>
</tr>
<tr class="even">
<td> </td>
<td>75</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>53288</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>79200</td>
<td>9900</td>
</tr>
<tr class="odd">
<td></td>
<td>80</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>56368</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>84480</td>
<td>10560</td>
</tr>
<tr class="even">
<td></td>
<td>81</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>57376</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>85536</td>
<td>10692</td>
</tr>
<tr class="odd">
<td></td>
<td>90</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>63528</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>95040</td>
<td>11880</td>
</tr>
<tr class="even">
<td> </td>
<td>100</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>69672</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>105600</td>
<td>13200</td>
</tr>
<tr class="odd">
<td></td>
<td>108</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>75792</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>114048</td>
<td>14256</td>
</tr>
<tr class="even">
<td> </td>
<td>120</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>83976</td>
<td>24</td>
<td>1</td>
<td>10</td>
<td>126720</td>
<td>15840</td>
</tr>
<tr class="odd">
<td> </td>
<td>128</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>90176</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>135168</td>
<td>16896</td>
</tr>
<tr class="even">
<td> </td>
<td>135</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>94248</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>142560</td>
<td>17820</td>
</tr>
<tr class="odd">
<td> </td>
<td>160</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>112648</td>
<td>24</td>
<td>1</td>
<td>14</td>
<td>168960</td>
<td>21120</td>
</tr>
<tr class="even">
<td> </td>
<td>162</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>114776</td>
<td>24</td>
<td>1</td>
<td>14</td>
<td>171072</td>
<td>21384</td>
</tr>
<tr class="odd">
<td></td>
<td>180</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>127080</td>
<td>24</td>
<td>1</td>
<td>16</td>
<td>190080</td>
<td>23760</td>
</tr>
<tr class="even">
<td> </td>
<td>216</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>151608</td>
<td>24</td>
<td>1</td>
<td>18</td>
<td>228096</td>
<td>28512</td>
</tr>
<tr class="odd">
<td> </td>
<td>243</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>172176</td>
<td>24</td>
<td>1</td>
<td>21</td>
<td>256608</td>
<td>32076</td>
</tr>
<tr class="even">
<td> </td>
<td>270</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>188576</td>
<td>24</td>
<td>1</td>
<td>23</td>
<td>285120</td>
<td>35640</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 5.1.3.1-2 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.5-2: Void

Table A.2.2.5-3: Void

### A.2.2.6 CP-OFDM QPSK

Table A.2.2.6-1: Reference Channels for CP-OFDM QPSK

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>CP-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td>1</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>48</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>264</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>256</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1320</td>
<td>660</td>
</tr>
<tr class="even">
<td> </td>
<td>6</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>304</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1584</td>
<td>792</td>
</tr>
<tr class="odd">
<td> </td>
<td>9</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>456</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2376</td>
<td>1188</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>504</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2640</td>
<td>1320</td>
</tr>
<tr class="odd">
<td> </td>
<td>11</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>552</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2904</td>
<td>1452</td>
</tr>
<tr class="even">
<td> </td>
<td>12</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>608</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3168</td>
<td>1584</td>
</tr>
<tr class="odd">
<td> </td>
<td>13</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>672</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3432</td>
<td>1716</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>768</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3960</td>
<td>1980</td>
</tr>
<tr class="odd">
<td> </td>
<td>16</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>808</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4224</td>
<td>2112</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>928</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4752</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>19</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>984</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5016</td>
<td>2508</td>
</tr>
<tr class="even">
<td> </td>
<td>24</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1192</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6336</td>
<td>3168</td>
</tr>
<tr class="odd">
<td> </td>
<td>25</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1256</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6600</td>
<td>3300</td>
</tr>
<tr class="even">
<td> </td>
<td>26</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1288</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6864</td>
<td>3432</td>
</tr>
<tr class="odd">
<td> </td>
<td>31</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1544</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>8184</td>
<td>4092</td>
</tr>
<tr class="even">
<td> </td>
<td>33</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1672</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>8712</td>
<td>4356</td>
</tr>
<tr class="odd">
<td> </td>
<td>38</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>1928</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10032</td>
<td>5016</td>
</tr>
<tr class="even">
<td> </td>
<td>39</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2024</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10296</td>
<td>5148</td>
</tr>
<tr class="odd">
<td> </td>
<td>40</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2024</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10560</td>
<td>5280</td>
</tr>
<tr class="even">
<td></td>
<td>47</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2408</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>12408</td>
<td>6204</td>
</tr>
<tr class="odd">
<td> </td>
<td>51</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2536</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>13464</td>
<td>6732</td>
</tr>
<tr class="even">
<td> </td>
<td>52</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2600</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>13728</td>
<td>6864</td>
</tr>
<tr class="odd">
<td> </td>
<td>53</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2664</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>13992</td>
<td>6996</td>
</tr>
<tr class="even">
<td> </td>
<td>54</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>2664</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>14256</td>
<td>7128</td>
</tr>
<tr class="odd">
<td> </td>
<td>61</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3104</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>16104</td>
<td>8052</td>
</tr>
<tr class="even">
<td> </td>
<td>65</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3240</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>17160</td>
<td>8580</td>
</tr>
<tr class="odd">
<td> </td>
<td>67</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3368</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>17688</td>
<td>8844</td>
</tr>
<tr class="even">
<td> </td>
<td>68</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3368</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>17952</td>
<td>8976</td>
</tr>
<tr class="odd">
<td> </td>
<td>78</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3848</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>20592</td>
<td>10296</td>
</tr>
<tr class="even">
<td></td>
<td>79</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3912</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>20856</td>
<td>10428</td>
</tr>
<tr class="odd">
<td></td>
<td>80</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>3976</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21120</td>
<td>10560</td>
</tr>
<tr class="even">
<td></td>
<td>81</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>4040</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>21384</td>
<td>10692</td>
</tr>
<tr class="odd">
<td></td>
<td>93</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>4616</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>24552</td>
<td>12276</td>
</tr>
<tr class="even">
<td></td>
<td>95</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>4744</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>25080</td>
<td>12540</td>
</tr>
<tr class="odd">
<td></td>
<td>106</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5256</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>27984</td>
<td>13992</td>
</tr>
<tr class="even">
<td></td>
<td>107</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5256</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>28248</td>
<td>14124</td>
</tr>
<tr class="odd">
<td></td>
<td>108</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5384</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>28512</td>
<td>14256</td>
</tr>
<tr class="even">
<td></td>
<td>109</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>5384</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>28776</td>
<td>14388</td>
</tr>
<tr class="odd">
<td></td>
<td>121</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6024</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>31944</td>
<td>15972</td>
</tr>
<tr class="even">
<td></td>
<td>123</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6152</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>32472</td>
<td>16236</td>
</tr>
<tr class="odd">
<td></td>
<td>133</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6664</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>35112</td>
<td>17556</td>
</tr>
<tr class="even">
<td></td>
<td>135</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6664</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>35640</td>
<td>17820</td>
</tr>
<tr class="odd">
<td></td>
<td>137</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>6792</td>
<td>24</td>
<td>2</td>
<td>2</td>
<td>36168</td>
<td>18084</td>
</tr>
<tr class="even">
<td></td>
<td>160</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>7944</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>42240</td>
<td>21120</td>
</tr>
<tr class="odd">
<td></td>
<td>162</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>8064</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>42768</td>
<td>21384</td>
</tr>
<tr class="even">
<td></td>
<td>189</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>9480</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>49896</td>
<td>24948</td>
</tr>
<tr class="odd">
<td></td>
<td>216</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>10752</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>57024</td>
<td>28512</td>
</tr>
<tr class="even">
<td></td>
<td>217</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>10752</td>
<td>24</td>
<td>2</td>
<td>3</td>
<td>57288</td>
<td>28644</td>
</tr>
<tr class="odd">
<td></td>
<td>245</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>12296</td>
<td>24</td>
<td>2</td>
<td>4</td>
<td>64680</td>
<td>32340</td>
</tr>
<tr class="even">
<td></td>
<td>270</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>13320</td>
<td>24</td>
<td>2</td>
<td>4</td>
<td>71280</td>
<td>35640</td>
</tr>
<tr class="odd">
<td></td>
<td>273</td>
<td>11</td>
<td>QPSK</td>
<td>2</td>
<td>13576</td>
<td>24</td>
<td>2</td>
<td>4</td>
<td>72072</td>
<td>36036</td>
</tr>
<tr class="even">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 5.1.3.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.6-2: Void

Table A.2.2.6-3: Void

### A.2.2.7 CP-OFDM 16QAM

Table A.2.2.7-1: Reference Channels for CP-OFDM 16QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>CP-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td> </td>
<td>1</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>176</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>528</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>888</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>2640</td>
<td>660</td>
</tr>
<tr class="even">
<td> </td>
<td>6</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1064</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3168</td>
<td>792</td>
</tr>
<tr class="odd">
<td> </td>
<td>9</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1608</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>4752</td>
<td>1188</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1800</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5280</td>
<td>1320</td>
</tr>
<tr class="odd">
<td> </td>
<td>11</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>1928</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5808</td>
<td>1452</td>
</tr>
<tr class="even">
<td> </td>
<td>12</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2088</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6336</td>
<td>1584</td>
</tr>
<tr class="odd">
<td> </td>
<td>13</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2280</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>6864</td>
<td>1716</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2664</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7920</td>
<td>1980</td>
</tr>
<tr class="odd">
<td> </td>
<td>16</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>2792</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>8448</td>
<td>2112</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>3240</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>9504</td>
<td>2376</td>
</tr>
<tr class="odd">
<td> </td>
<td>19</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>3368</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>10032</td>
<td>2508</td>
</tr>
<tr class="even">
<td> </td>
<td>24</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>4224</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>12672</td>
<td>3168</td>
</tr>
<tr class="odd">
<td> </td>
<td>25</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>4352</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>13200</td>
<td>3300</td>
</tr>
<tr class="even">
<td> </td>
<td>26</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>4480</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>13728</td>
<td>3432</td>
</tr>
<tr class="odd">
<td> </td>
<td>31</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>5376</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>16368</td>
<td>4092</td>
</tr>
<tr class="even">
<td> </td>
<td>33</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>5760</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>17424</td>
<td>4356</td>
</tr>
<tr class="odd">
<td> </td>
<td>38</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>6656</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>20064</td>
<td>5016</td>
</tr>
<tr class="even">
<td> </td>
<td>39</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>6784</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>20592</td>
<td>5148</td>
</tr>
<tr class="odd">
<td> </td>
<td>40</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>7040</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>21120</td>
<td>5280</td>
</tr>
<tr class="even">
<td></td>
<td>47</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>8192</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>24816</td>
<td>6204</td>
</tr>
<tr class="odd">
<td> </td>
<td>51</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>8968</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>26928</td>
<td>6732</td>
</tr>
<tr class="even">
<td> </td>
<td>52</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>9224</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>27456</td>
<td>6864</td>
</tr>
<tr class="odd">
<td> </td>
<td>53</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>9224</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>27984</td>
<td>6996</td>
</tr>
<tr class="even">
<td> </td>
<td>54</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>9480</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>28512</td>
<td>7128</td>
</tr>
<tr class="odd">
<td> </td>
<td>61</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>10760</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>32208</td>
<td>8052</td>
</tr>
<tr class="even">
<td> </td>
<td>65</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>11272</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>34320</td>
<td>8580</td>
</tr>
<tr class="odd">
<td> </td>
<td>67</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>11784</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>35376</td>
<td>8844</td>
</tr>
<tr class="even">
<td> </td>
<td>68</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>11784</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>35904</td>
<td>8976</td>
</tr>
<tr class="odd">
<td> </td>
<td>78</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>13576</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>41184</td>
<td>10296</td>
</tr>
<tr class="even">
<td></td>
<td>79</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>13832</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>41712</td>
<td>10428</td>
</tr>
<tr class="odd">
<td></td>
<td>80</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>14088</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>42240</td>
<td>10560</td>
</tr>
<tr class="even">
<td></td>
<td>81</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>14088</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>42768</td>
<td>10692</td>
</tr>
<tr class="odd">
<td></td>
<td>93</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>16392</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>49404</td>
<td>12276</td>
</tr>
<tr class="even">
<td></td>
<td>95</td>
<td>11</td>
<td>16QMA</td>
<td>10</td>
<td>16392</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>50160</td>
<td>12540</td>
</tr>
<tr class="odd">
<td></td>
<td>106</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>18432</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>55968</td>
<td>13992</td>
</tr>
<tr class="even">
<td></td>
<td>107</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>18960</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>56496</td>
<td>14124</td>
</tr>
<tr class="odd">
<td></td>
<td>108</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>18960</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>57024</td>
<td>14256</td>
</tr>
<tr class="even">
<td></td>
<td>109</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>18960</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>57552</td>
<td>14388</td>
</tr>
<tr class="odd">
<td></td>
<td>121</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>21000</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>63888</td>
<td>15972</td>
</tr>
<tr class="even">
<td></td>
<td>123</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>21504</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>64944</td>
<td>16236</td>
</tr>
<tr class="odd">
<td></td>
<td>133</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>23040</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>70224</td>
<td>17556</td>
</tr>
<tr class="even">
<td></td>
<td>135</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>23568</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>71280</td>
<td>17820</td>
</tr>
<tr class="odd">
<td></td>
<td>137</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>24072</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>72336</td>
<td>18084</td>
</tr>
<tr class="even">
<td></td>
<td>160</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>28168</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>84480</td>
<td>21120</td>
</tr>
<tr class="odd">
<td></td>
<td>162</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>28168</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>85536</td>
<td>21384</td>
</tr>
<tr class="even">
<td></td>
<td>189</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>32776</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>99792</td>
<td>24948</td>
</tr>
<tr class="odd">
<td></td>
<td>216</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>37896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>114048</td>
<td>28512</td>
</tr>
<tr class="even">
<td></td>
<td>217</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>37896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>114576</td>
<td>28644</td>
</tr>
<tr class="odd">
<td></td>
<td>245</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>129360</td>
<td>32340</td>
</tr>
<tr class="even">
<td></td>
<td>270</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>47112</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>142560</td>
<td>35640</td>
</tr>
<tr class="odd">
<td></td>
<td>273</td>
<td>11</td>
<td>16QAM</td>
<td>10</td>
<td>48168</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>144144</td>
<td>36036</td>
</tr>
<tr class="even">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 5.1.3.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.7-2: Void

Table A.2.2.7-3: Void

### A.2.2.8 CP-OFDM 64QAM

Table A.2.2.8-1: Reference Channels for CP-OFDM 64QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>CP-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td>1</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>408</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>792</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>2024</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>3960</td>
<td>660</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>3624</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>7128</td>
<td>1188</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>3968</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>7920</td>
<td>1320</td>
</tr>
<tr class="even">
<td> </td>
<td>11</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>4352</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>8712</td>
<td>1452</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>4736</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>9504</td>
<td>1584</td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>5120</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>10296</td>
<td>1716</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>6016</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>11880</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>7168</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>14256</td>
<td>2376</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>7552</td>
<td>24</td>
<td>1</td>
<td></td>
<td>15048</td>
<td>2508</td>
</tr>
<tr class="even">
<td> </td>
<td>24</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>9480</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19008</td>
<td>3168</td>
</tr>
<tr class="odd">
<td> </td>
<td>25</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>9992</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19800</td>
<td>3300</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>10504</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>20592</td>
<td>3432</td>
</tr>
<tr class="odd">
<td> </td>
<td>31</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>12296</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>24552</td>
<td>4092</td>
</tr>
<tr class="even">
<td></td>
<td>33</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>13064</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>26136</td>
<td>4356</td>
</tr>
<tr class="odd">
<td> </td>
<td>38</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>15112</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>30096</td>
<td>5016</td>
</tr>
<tr class="even">
<td></td>
<td>39</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>15624</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>30888</td>
<td>5148</td>
</tr>
<tr class="odd">
<td></td>
<td>47</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>18960</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>37224</td>
<td>6204</td>
</tr>
<tr class="even">
<td> </td>
<td>51</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>20496</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>40392</td>
<td>6732</td>
</tr>
<tr class="odd">
<td> </td>
<td>52</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>21000</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>41184</td>
<td>6864</td>
</tr>
<tr class="even">
<td></td>
<td>53</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>21000</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>41976</td>
<td>6996</td>
</tr>
<tr class="odd">
<td></td>
<td>61</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>24567</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>48312</td>
<td>8052</td>
</tr>
<tr class="even">
<td> </td>
<td>65</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>26120</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>51480</td>
<td>8580</td>
</tr>
<tr class="odd">
<td></td>
<td>67</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>26632</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>53064</td>
<td>8844</td>
</tr>
<tr class="even">
<td> </td>
<td>78</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>31240</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>61776</td>
<td>10296</td>
</tr>
<tr class="odd">
<td> </td>
<td>79</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>31752</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>62568</td>
<td>10428</td>
</tr>
<tr class="even">
<td></td>
<td>80</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>31752</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>63360</td>
<td>10560</td>
</tr>
<tr class="odd">
<td></td>
<td>81</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>32264</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>64152</td>
<td>10692</td>
</tr>
<tr class="even">
<td></td>
<td>93</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>36896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>73656</td>
<td>12276</td>
</tr>
<tr class="odd">
<td></td>
<td>95</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>37896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>75240</td>
<td>12540</td>
</tr>
<tr class="even">
<td></td>
<td>93</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>36896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>73656</td>
<td>12276</td>
</tr>
<tr class="odd">
<td> </td>
<td>106</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>42016</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>83952</td>
<td>13992</td>
</tr>
<tr class="even">
<td> </td>
<td>107</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>84744</td>
<td>14124</td>
</tr>
<tr class="odd">
<td></td>
<td>108</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>85536</td>
<td>14256</td>
</tr>
<tr class="even">
<td></td>
<td>109</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>44040</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>86328</td>
<td>14388</td>
</tr>
<tr class="odd">
<td> </td>
<td>121</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>48168</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>95832</td>
<td>15972</td>
</tr>
<tr class="even">
<td></td>
<td>123</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>49176</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>97416</td>
<td>16236</td>
</tr>
<tr class="odd">
<td> </td>
<td>133</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>53288</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>105336</td>
<td>17556</td>
</tr>
<tr class="even">
<td> </td>
<td>135</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>54296</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>106920</td>
<td>17820</td>
</tr>
<tr class="odd">
<td></td>
<td>137</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>54296</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>108504</td>
<td>18084</td>
</tr>
<tr class="even">
<td> </td>
<td>160</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>63528</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>126720</td>
<td>21120</td>
</tr>
<tr class="odd">
<td> </td>
<td>162</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>64552</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>128304</td>
<td>21384</td>
</tr>
<tr class="even">
<td></td>
<td>189</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>75792</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>149688</td>
<td>24948</td>
</tr>
<tr class="odd">
<td> </td>
<td>216</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>86040</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>171072</td>
<td>28512</td>
</tr>
<tr class="even">
<td> </td>
<td>217</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>86040</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>171864</td>
<td>28644</td>
</tr>
<tr class="odd">
<td> </td>
<td>245</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>98376</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>194040</td>
<td>32340</td>
</tr>
<tr class="even">
<td> </td>
<td>270</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>108552</td>
<td>24</td>
<td>1</td>
<td>13</td>
<td>213840</td>
<td>35640</td>
</tr>
<tr class="odd">
<td> </td>
<td>273</td>
<td>11</td>
<td>64QAM</td>
<td>19</td>
<td>108552</td>
<td>24</td>
<td>1</td>
<td>13</td>
<td>216216</td>
<td>36036</td>
</tr>
<tr class="even">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 5.1.3.1-1 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.8-2: Void

Table A.2.2.8-3: Void

### A.2.2.9 CP-OFDM 256QAM

Table A.2.2.9-1: Reference Channels for CP-OFDM 256QAM

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Allocated resource blocks (L<sub>CRB)</sub></th>
<th>CP-OFDM Symbols per slot (Note 1)</th>
<th>Modulation</th>
<th>MCS Index (Note 2)</th>
<th>Payload size</th>
<th>Transport block CRC</th>
<th>LDPC Base Graph</th>
<th>Number of code blocks per slot (Note 3)</th>
<th>Total number of bits per slot</th>
<th>Total modulated symbols per slot</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unit</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Bits</td>
<td>Bits</td>
<td> </td>
<td> </td>
<td>Bits</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td>1</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>704</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>1056</td>
<td>132</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>3496</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5280</td>
<td>660</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>6272</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>9504</td>
<td>1188</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>7040</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>10560</td>
<td>1320</td>
</tr>
<tr class="even">
<td> </td>
<td>11</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>7680</td>
<td>24</td>
<td>1</td>
<td>1</td>
<td>11616</td>
<td>1452</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>8456</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>12672</td>
<td>1584</td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>9224</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>13728</td>
<td>1716</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>10504</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>15840</td>
<td>1980</td>
</tr>
<tr class="even">
<td> </td>
<td>18</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>12552</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>19008</td>
<td>2376</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>13320</td>
<td>24</td>
<td>1</td>
<td>2</td>
<td>20064</td>
<td>2508</td>
</tr>
<tr class="even">
<td> </td>
<td>24</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>16896</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>25344</td>
<td>3168</td>
</tr>
<tr class="odd">
<td> </td>
<td>25</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>17424</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>26400</td>
<td>3300</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>18432</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>27456</td>
<td>3432</td>
</tr>
<tr class="odd">
<td> </td>
<td>31</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>22032</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>32736</td>
<td>4092</td>
</tr>
<tr class="even">
<td></td>
<td>33</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>23040</td>
<td>24</td>
<td>1</td>
<td>3</td>
<td>34848</td>
<td>4356</td>
</tr>
<tr class="odd">
<td> </td>
<td>38</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>26632</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>40128</td>
<td>5016</td>
</tr>
<tr class="even">
<td></td>
<td>39</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>27656</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>41184</td>
<td>5148</td>
</tr>
<tr class="odd">
<td></td>
<td>47</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>32776</td>
<td>24</td>
<td>1</td>
<td>4</td>
<td>49632</td>
<td>6204</td>
</tr>
<tr class="even">
<td> </td>
<td>51</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>35856</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>53856</td>
<td>6732</td>
</tr>
<tr class="odd">
<td> </td>
<td>52</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>36896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>54912</td>
<td>6864</td>
</tr>
<tr class="even">
<td></td>
<td>53</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>36896</td>
<td>24</td>
<td>1</td>
<td>5</td>
<td>55968</td>
<td>6996</td>
</tr>
<tr class="odd">
<td></td>
<td>61</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>43032</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>64416</td>
<td>8052</td>
</tr>
<tr class="even">
<td> </td>
<td>65</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>46104</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>68640</td>
<td>8580</td>
</tr>
<tr class="odd">
<td></td>
<td>67</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>47112</td>
<td>24</td>
<td>1</td>
<td>6</td>
<td>70752</td>
<td>8844</td>
</tr>
<tr class="even">
<td> </td>
<td>78</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>55304</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>82368</td>
<td>10296</td>
</tr>
<tr class="odd">
<td> </td>
<td>79</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>55304</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>83424</td>
<td>10428</td>
</tr>
<tr class="even">
<td></td>
<td>80</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>56368</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>84480</td>
<td>10560</td>
</tr>
<tr class="odd">
<td></td>
<td>81</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>57376</td>
<td>24</td>
<td>1</td>
<td>7</td>
<td>85536</td>
<td>10692</td>
</tr>
<tr class="even">
<td></td>
<td>93</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>65576</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>98208</td>
<td>12276</td>
</tr>
<tr class="odd">
<td></td>
<td>95</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>67584</td>
<td>24</td>
<td>1</td>
<td>8</td>
<td>100320</td>
<td>12540</td>
</tr>
<tr class="even">
<td> </td>
<td>106</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>73776</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>111936</td>
<td>13992</td>
</tr>
<tr class="odd">
<td> </td>
<td>107</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>75792</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>112992</td>
<td>14124</td>
</tr>
<tr class="even">
<td></td>
<td>108</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>75792</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>114048</td>
<td>14256</td>
</tr>
<tr class="odd">
<td></td>
<td>109</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>75792</td>
<td>24</td>
<td>1</td>
<td>9</td>
<td>115104</td>
<td>14388</td>
</tr>
<tr class="even">
<td> </td>
<td>121</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>86040</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>127776</td>
<td>15972</td>
</tr>
<tr class="odd">
<td></td>
<td>123</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>86040</td>
<td>24</td>
<td>1</td>
<td>11</td>
<td>129888</td>
<td>16236</td>
</tr>
<tr class="even">
<td> </td>
<td>133</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>94248</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>140448</td>
<td>17556</td>
</tr>
<tr class="odd">
<td> </td>
<td>135</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>94248</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>142560</td>
<td>17820</td>
</tr>
<tr class="even">
<td></td>
<td>137</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>96264</td>
<td>24</td>
<td>1</td>
<td>12</td>
<td>144672</td>
<td>18084</td>
</tr>
<tr class="odd">
<td> </td>
<td>160</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>112648</td>
<td>24</td>
<td>1</td>
<td>14</td>
<td>168960</td>
<td>21120</td>
</tr>
<tr class="even">
<td> </td>
<td>162</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>114776</td>
<td>24</td>
<td>1</td>
<td>14</td>
<td>171072</td>
<td>21384</td>
</tr>
<tr class="odd">
<td></td>
<td>189</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>131176</td>
<td>24</td>
<td>1</td>
<td>16</td>
<td>199584</td>
<td>24948</td>
</tr>
<tr class="even">
<td> </td>
<td>216</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>151608</td>
<td>24</td>
<td>1</td>
<td>18</td>
<td>228096</td>
<td>28512</td>
</tr>
<tr class="odd">
<td> </td>
<td>217</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>151608</td>
<td>24</td>
<td>1</td>
<td>18</td>
<td>229152</td>
<td>28644</td>
</tr>
<tr class="even">
<td> </td>
<td>245</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>172176</td>
<td>24</td>
<td>1</td>
<td>21</td>
<td>258720</td>
<td>32340</td>
</tr>
<tr class="odd">
<td> </td>
<td>270</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>188576</td>
<td>24</td>
<td>1</td>
<td>23</td>
<td>285120</td>
<td>35640</td>
</tr>
<tr class="even">
<td> </td>
<td>273</td>
<td>11</td>
<td>256QAM</td>
<td>20</td>
<td>192624</td>
<td>24</td>
<td>1</td>
<td>23</td>
<td>288288</td>
<td>36036</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: PUSCH mapping Type-A and single-symbol DM-RS configuration Type-1 with 2 additional DM-RS symbols, such that the DM-RS positions are set to symbols 2, 7, 11. DMRS is [TDM'ed] with PUSCH data. DM-RS symbols are not counted.</p>
<p>NOTE 2: MCS Index is based on MCS table 5.1.3.1-2 defined in TS 38.214 [10].</p>
<p>NOTE 3: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit)</p>
<p>NOTE 4: The RMCs apply to all channel bandwidth where L<sub>CRB</sub> ≤ N<sub>RB.</sub></p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.2.2.9-2: Void

Table A.2.2.9-3: Void

A.2.3 Reference measurement channels for TDD
--------------------------------------------

The TDD UL RMCs are defined in clause A.2.2 with the active UL slots
specified in table A.2.1-1 and TDD slot patterns as defined for
reference sensitivity tests.

### A.2.3.1 DFT-s-OFDM Pi/2-BPSK

Table A.2.3.1-1: Void

Table A.2.3.1-2: Void

Table A.2.3.1-3: Void

### A.2.3.2 DFT-s-OFDM QPSK

Table A.2.3.2-1: Void

Table A.2.3.2-2: Void

Table A.2.3.2-3: Void

### A.2.3.3 DFT-s-OFDM 16QAM

Table A.2.3.3-1: Void

Table A.2.3.3-2: Void

Table A.2.3.3-3: Void

### A.2.3.4 DFT-s-OFDM 64QAM

Table A.2.3.4-1: Void

Table A.2.3.4-2: Void

Table A.2.3.4-3: Void

### A.2.3.5 DFT-s-OFDM 256QAM

Table A.2.3.5-1: Void

Table A.2.3.5-2: Void

Table A.2.3.5-3: Void

### A.2.3.6 CP-OFDM QPSK

Table A.2.3.6-1: Void

Table A.2.3.6-2: Void

Table A.2.3.6-3: Void

### A.2.3.7 CP-OFDM 16QAM

Table A.2.3.7-1: Void

Table A.2.3.7-2: Void

Table A.2.3.7-3: Void

### A.2.3.8 CP-OFDM 64QAM

Table A.2.3.8-1: Void

Table A.2.3.8-2: Void

Table A.2.3.8-3: Void

### A.2.3.9 CP-OFDM 256QAM

Table A.2.3.9-1: Void

Table A.2.3.9-2: Void

Table A.2.3.9-3: Void

A.3 DL reference measurement channels
=====================================

A.3.1 General
-------------

Unless otherwise stated, Tables A.3.2.2-1, A.3.2.2-2, A.3.2.2-3,
A.3.3.2-1, A.3.3.2-2 and A.3.3.2-3 are applicable for measurements of
the Receiver Characteristics (clause 7) with the exception of clauses
7.4 (Maximum input level).

Unless otherwise stated, Tables A.3.2.3-1, A.3.2.3-2, A.3.2.3-3,
A.3.3.3-1, A.3.3.3-2 and A.3.3.3-3 are applicable for clauses 7.4
(Maximum input level) and for UE not supporting PDSCH 256QAM,

Unless otherwise stated, Tables A.3.2.4-1, A.3.2.4-2, A.3.2.4-3,
A.3.3.4-1, A.3.3.4-2 and A.3.3.4-3 are applicable for clauses 7.4
(Maximum input level) and for UE supporting PDSCH 256QAM,

Unless otherwise stated, Tables A.3.2.2-1, A.3.2.2-2, A.3.2.2-3,
A.3.3.2-1, A.3.3.2-2 and A.3.3.2-3 also apply for the modulated
interferer used in Clauses 7.5, 7.6 and 7.8 with test specific
bandwidths.

In case of carrier aggregation scenarios, the k1 values and number of
HARQ processes of the Reference Measurement Channels specified in Annex
A.3 shall be adapted as specified in table A.3.1-2 and A.3.1-3.

Table A.3.1-1: Common reference channel parameters

+----------------+----------------+----------------+----------------+
| Parameter      | Unit           | Value          |                |
+================+================+================+================+
| CORESET        |                | Full BW        |                |
| frequency      |                |                |                |
| domain         |                |                |                |
| allocation     |                |                |                |
+----------------+----------------+----------------+----------------+
| CORESET time   |                | 2 OFDM symbols |                |
| domain         |                | at the begin   |                |
| allocation     |                | of each slot   |                |
+----------------+----------------+----------------+----------------+
| PDSCH mapping  |                | Type A         |                |
| type           |                |                |                |
+----------------+----------------+----------------+----------------+
| PDSCH start    |                | 2              |                |
| symbol index   |                |                |                |
| (S)            |                |                |                |
+----------------+----------------+----------------+----------------+
| Number of      |                | 12             |                |
| consecutive    |                |                |                |
| PDSCH symbols  |                |                |                |
| (L)            |                |                |                |
+----------------+----------------+----------------+----------------+
| PDSCH PRB      | PRBs           | 2              |                |
| bundling       |                |                |                |
+----------------+----------------+----------------+----------------+
| Dynamic PRB    |                | false          |                |
| bundling       |                |                |                |
+----------------+----------------+----------------+----------------+
|                |                |                |                |
+----------------+----------------+----------------+----------------+
| Overhead value |                | 0              |                |
| for TBS        |                |                |                |
| determination  |                |                |                |
+----------------+----------------+----------------+----------------+
| First DMRS     |                | 2              |                |
| position for   |                |                |                |
| Type A PDSCH   |                |                |                |
| mapping        |                |                |                |
+----------------+----------------+----------------+----------------+
| DMRS type      |                | Type 1         |                |
+----------------+----------------+----------------+----------------+
| Number of      |                | 2              |                |
| additional     |                |                |                |
| DMRS           |                |                |                |
+----------------+----------------+----------------+----------------+
| FDM between    |                | Disable        |                |
| DMRS and PDSCH |                |                |                |
+----------------+----------------+----------------+----------------+
| CSI‑RS for     | First          |                | 0 for CSI-RS   |
| tracking       | subcarrier     |                | resource       |
|                | index in the   |                | 1,2,3,4        |
|                | PRB used for   |                |                |
|                | CSI-RS (k0)    |                |                |
+----------------+----------------+----------------+----------------+
|                | OFDM symbols   |                | l~0~ = 6 for   |
|                | in the PRB     |                | CSI-RS         |
|                | used for       |                | resource 1 and |
|                | CSI‑RS         |                | 3              |
|                |                |                |                |
|                |                |                | l~0~ = 10 for  |
|                |                |                | CSI-RS         |
|                |                |                | resource 2 and |
|                |                |                | 4              |
+----------------+----------------+----------------+----------------+
|                | Number of      |                | 1 for CSI-RS   |
|                | CSI-RS ports   |                | resource       |
|                |                |                | 1,2,3,4        |
+----------------+----------------+----------------+----------------+
|                | CDM Type       |                | \'No CDM\' for |
|                |                |                | CSI-RS         |
|                |                |                | resource       |
|                |                |                | 1,2,3,4        |
+----------------+----------------+----------------+----------------+
|                | Density (ρ)    |                | 3 for CSI-RS   |
|                |                |                | resource       |
|                |                |                | 1,2,3,4        |
+----------------+----------------+----------------+----------------+
|                | CSI‑RS         | Slots          | 15 kHz SCS: 20 |
|                | periodicity    |                | for CSI-RS     |
|                |                |                | resource       |
|                |                |                | 1,2,3,4        |
|                |                |                |                |
|                |                |                | 30 kHz SCS: 40 |
|                |                |                | for CSI-RS     |
|                |                |                | resource       |
|                |                |                | 1,2,3,4        |
|                |                |                |                |
|                |                |                | 60 kHz SCS: 80 |
|                |                |                | for CSI-RS     |
|                |                |                | resource       |
|                |                |                | 1,2,3,4        |
+----------------+----------------+----------------+----------------+
|                | CSI‑RS offset  | Slots          | 15 kHz SCS:    |
|                |                |                |                |
|                |                |                | 0 for CSI-RS   |
|                |                |                | resource 1 and |
|                |                |                | 2              |
|                |                |                |                |
|                |                |                | 1 for CSI-RS   |
|                |                |                | resource 3 and |
|                |                |                | 4              |
|                |                |                |                |
|                |                |                | 30 kHz SCS:    |
|                |                |                |                |
|                |                |                | 1 for CSI-RS   |
|                |                |                | resource 1 and |
|                |                |                | 2              |
|                |                |                |                |
|                |                |                | 2 for CSI-RS   |
|                |                |                | resource 3 and |
|                |                |                | 4              |
|                |                |                |                |
|                |                |                | 60 kHz SCS:    |
|                |                |                |                |
|                |                |                | 2 for CSI-RS   |
|                |                |                | resource 1 and |
|                |                |                | 2              |
|                |                |                |                |
|                |                |                | 3 for CSI-RS   |
|                |                |                | resource 3 and |
|                |                |                | 4              |
+----------------+----------------+----------------+----------------+
|                | Frequency      |                | Start PRB 0    |
|                | Occupation     |                |                |
|                |                |                | Number of PRB  |
|                |                |                | = BWP size     |
+----------------+----------------+----------------+----------------+
|                | QCL info       |                | TCI state \#0  |
+----------------+----------------+----------------+----------------+
| PTRS           |                | PTRS is not    |                |
| configuration  |                | configured     |                |
+----------------+----------------+----------------+----------------+

Table A.3.1-2: Carrier aggregation test parameters for K1 values

  The number of slots between PDSCH and corresponding HARQ-ACK information                                                                           CCs with the same duplex mode and SCS with Pcell   CCs with different duplex mode and/or SCS with Pcell   
  -------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------- ------------------------------------------------------ --------------------------------
  FDD 15 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    N/A
  FDD 15 kHz CA                                                                                                                                                                                                                                                
  FDD 15 kHz +                                                                                                                                       15kHz PCell                                        {2}                                                    {3}
  FDD 30 kHz CA                                                                                                                                      30kHz PCell                                        {2}                                                    {2}
  FDD 15 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    {2}
  TDD 15 kHz CA                                                                                                                                      TDD PCell                                          {4,3,2}                                                {4,3,2,6,5}
  FDD 15 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    {3}
  TDD 30 kHz CA                                                                                                                                      TDD PCell                                          {8,7,6,5,4,3,2}                                        {8,6,4,2,10}
  TDD 15 kHz +                                                                                                                                       TDD PCell                                          {4,3,2}                                                N/A
  TDD 15 kHz CA                                                                                                                                                                                                                                                
  TDD 15 kHz +                                                                                                                                       15kHz PCell                                        {4,3,2}                                                {4,4,3,3,2,7,6}
  TDD 30 kHz CA                                                                                                                                      30kHz PCell                                        {8,7,6,5,4,3,2}                                        {7,5,4}
  FDD 30 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    N/A
  FDD 30 kHz CA                                                                                                                                                                                                                                                
  FDD 30 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    {2}
  TDD 15 kHz CA                                                                                                                                      TDD PCell                                          {4,3,2}                                                {4,4,3,3,7,7,6,6,5,5}
  FDD 30 kHz +                                                                                                                                       FDD PCell                                          {2}                                                    {2}
  TDD 30 kHz CA                                                                                                                                      TDD PCell                                          {8,7,6,5,4,3,2}                                        {8,7,6,5,4,3,2,2,10,-}(NOTE 1)
  TDD 30 kHz +                                                                                                                                       TDD PCell                                          {8,7,6,5,4,3,2}                                        N/A
  TDD 30 kHz CA                                                                                                                                                                                                                                                
  NOTE 1: No PDSCH shall be scheduled in slots 9 and 19 to avoid HARQ conflicts and maximize Throughput. Hence no K1 value is applicable for them.                                                                                                             

Table A.3.1-3: Carrier Aggregation test parameters for number of HARQ
processes

  HARQ process number   CCs with the same duplex mode and SCS with Pcell   CCs with different duplex mode and/or SCS with Pcell   
  --------------------- -------------------------------------------------- ------------------------------------------------------ -----
  FDD 15 kHz +          FDD PCell                                          4                                                      N/A
  FDD 15 kHz CA                                                                                                                   
  FDD 15 kHz +          15kHz PCell                                        8                                                      8
  FDD 30 kHz CA         30kHz PCell                                        8                                                      8
  FDD 15 kHz +          FDD PCell                                          4                                                      8
  TDD 15 kHz CA         TDD PCell                                          8                                                      8
  FDD 15 kHz +          FDD PCell                                          4                                                      8
  TDD 30 kHz CA         TDD PCell                                          10                                                     8
  TDD 15 kHz +          TDD PCell                                          8                                                      N/A
  TDD 15 kHz CA                                                                                                                   
  TDD 15 kHz +          15kHz PCell                                        8                                                      12
  TDD 30 kHz CA         30kHz PCell                                        8                                                      8
  FDD 30 kHz +          FDD PCell                                          8                                                      N/A
  FDD 30 kHz CA                                                                                                                   
  FDD 30 kHz +          FDD PCell                                          8                                                      8
  TDD 15 kHz CA         TDD PCell                                          8                                                      16
  FDD 30 kHz +          FDD PCell                                          8                                                      8
  TDD 30 kHz CA         TDD PCell                                          8                                                      16
  TDD 30 kHz +          TDD PCell                                          8                                                      N/A
  TDD 30 kHz CA                                                                                                                   

A.3.2 DL reference measurement channels for FDD
-----------------------------------------------

### A.3.2.1 General

Table A.3.2.1-1 Additional reference channels parameters for FDD

  Parameter                  Unit   Value
  -------------------------- ------ -----------------
  Number of HARQ Processes          4
  K1 value                          2 for all slots

### A.3.2.2 FRC for receiver requirements for QPSK

Table A.3.2.2-1 Fixed reference channel for receiver requirements (SCS
15 kHz, FDD, QPSK 1/3)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="even">
<td>MCS Table for TBS determination</td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>1672</td>
<td>3368</td>
<td>5120</td>
<td>6912</td>
<td>8712</td>
<td>10504</td>
<td>14088</td>
<td>17424</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>16</td>
<td>16</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>5400</td>
<td>11232</td>
<td>17064</td>
<td>22896</td>
<td>28728</td>
<td>34560</td>
<td>46656</td>
<td>58320</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>1.338</td>
<td>2.694</td>
<td>4.096</td>
<td>5.530</td>
<td>6.970</td>
<td>8.403</td>
<td>11.270</td>
<td>13.9392</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>80</td>
<td>90</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>217</td>
<td>245</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>736</td>
<td>1608</td>
<td>2472</td>
<td>3368</td>
<td>4224</td>
<td>4992</td>
<td>6912</td>
<td>8712</td>
<td>10504</td>
<td>14088</td>
<td>15880</td>
<td>17928</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 3,…,19</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>2376</td>
<td>5184</td>
<td>8208</td>
<td>11016</td>
<td>14040</td>
<td>16848</td>
<td>22896</td>
<td>28728</td>
<td>34992</td>
<td>46872</td>
<td>52920</td>
<td>58968</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>1.251</td>
<td>2.734</td>
<td>4.202</td>
<td>5.726</td>
<td>7.181</td>
<td>8.486</td>
<td>11.750</td>
<td>14.810</td>
<td>17.857</td>
<td>23.950</td>
<td>26.996</td>
<td>30.478</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.2.2-2 Fixed reference channel for receiver requirements (SCS
30 kHz, FDD, QPSK 1/3)

### A.3.2.3 FRC for maximum input level for 64QAM

Table A.3.2.3-1 Fixed reference channel for maximum input level receiver
requirements (SCS 15 kHz, FDD, 64QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>MCS Table for TBS determination</td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>12296</td>
<td>25608</td>
<td>38936</td>
<td>52224</td>
<td>64552</td>
<td>77896</td>
<td>106576</td>
<td>131176</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slot 0,1</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>CBs</td>
<td>2</td>
<td>4</td>
<td>5</td>
<td>7</td>
<td>8</td>
<td>10</td>
<td>13</td>
<td>16</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slot 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>16200</td>
<td>33696</td>
<td>51192</td>
<td>68688</td>
<td>86184</td>
<td>103680</td>
<td>139968</td>
<td>174960</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>9.837</td>
<td>20.486</td>
<td>31.149</td>
<td>41.779</td>
<td>51.642</td>
<td>62.317</td>
<td>85.261</td>
<td>104.941</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.2.3-2 Fixed reference channel for maximum input level receiver
requirements (SCS 30 kHz, FDD, 64QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>217</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>5376</td>
<td>11784</td>
<td>18432</td>
<td>25104</td>
<td>31752</td>
<td>37896</td>
<td>52224</td>
<td>64552</td>
<td>79896</td>
<td>106576</td>
<td>135296</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slot2 0,1,2</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 3,…,19</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>7</td>
<td>8</td>
<td>10</td>
<td>13</td>
<td>17</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>7128</td>
<td>15552</td>
<td>24624</td>
<td>33048</td>
<td>42120</td>
<td>50544</td>
<td>68688</td>
<td>86184</td>
<td>104976</td>
<td>140616</td>
<td>176904</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>9.139</td>
<td>20.033</td>
<td>31.334</td>
<td>42.677</td>
<td>53.978</td>
<td>64.423</td>
<td>88.781</td>
<td>109.738</td>
<td>135.823</td>
<td>181.179</td>
<td>230.003</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

###  

Table A.3.2.3-3 Fixed Reference Channel for Maximum input level receiver
requirements (SCS 60 kHz, FDD, 64QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>18</td>
<td>24</td>
<td>31</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>79</td>
<td>107</td>
<td>135</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 4,…,39</td>
<td>Bits</td>
<td>5376</td>
<td>8712</td>
<td>11784</td>
<td>15112</td>
<td>18432</td>
<td>25104</td>
<td>31752</td>
<td>38936</td>
<td>52224</td>
<td>65576</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2,3</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 4,…,39</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>7</td>
<td>8</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 4,…,39</td>
<td>Bits</td>
<td>7128</td>
<td>11664</td>
<td>15552</td>
<td>20088</td>
<td>24624</td>
<td>33048</td>
<td>42120</td>
<td>51192</td>
<td>69336</td>
<td>87480</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>19.354</td>
<td>31.363</td>
<td>42.422</td>
<td>54.403</td>
<td>66.355</td>
<td>90.374</td>
<td>114.307</td>
<td>140.170</td>
<td>188.006</td>
<td>236.074</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### A.3.2.4 FRC for maximum input level for 256 QAM

Table A.3.2.4-1 Fixed reference channel for maximum input level receiver
requirements (SCS 15 kHz, FDD, 256QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="even">
<td>MCS Table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>16896</td>
<td>34816</td>
<td>53288</td>
<td>71688</td>
<td>90176</td>
<td>108552</td>
<td>143400</td>
<td>180376</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slot 0,1</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>CBs</td>
<td>3</td>
<td>5</td>
<td>7</td>
<td>9</td>
<td>11</td>
<td>13</td>
<td>18</td>
<td>22</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,3,4,5,6,7,8,9</td>
<td>Bits</td>
<td>21600</td>
<td>44928</td>
<td>68256</td>
<td>91584</td>
<td>114912</td>
<td>138240</td>
<td>186624</td>
<td>233280</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>13.517</td>
<td>27.853</td>
<td>42.630</td>
<td>57.350</td>
<td>72.141</td>
<td>86.842</td>
<td>114.720</td>
<td>144.301</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.2.4-2 Fixed reference channel for maximum input level receiver
requirements (SCS 30 kHz, FDD, 256QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>217</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
<td>17</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>7424</td>
<td>16136</td>
<td>25608</td>
<td>33816</td>
<td>44040</td>
<td>52224</td>
<td>71688</td>
<td>90176</td>
<td>108552</td>
<td>147576</td>
<td>184424</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 3,…,19</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>9</td>
<td>11</td>
<td>13</td>
<td>18</td>
<td>22</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 3,…,19</td>
<td>Bits</td>
<td>9504</td>
<td>20736</td>
<td>32832</td>
<td>44064</td>
<td>56160</td>
<td>67392</td>
<td>91584</td>
<td>114912</td>
<td>139968</td>
<td>187488</td>
<td>235872</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>12.621</td>
<td>27.431</td>
<td>43.534</td>
<td>57.487</td>
<td>74.868</td>
<td>88.781</td>
<td>121.870</td>
<td>153.299</td>
<td>184.538</td>
<td>250.879</td>
<td>313.521</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.2.4-3 Fixed reference channel for maximum input level receiver
requirements (SCS 60 kHz, FDD, 256QAM)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>18</td>
<td>24</td>
<td>31</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>79</td>
<td>107</td>
<td>135</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
<td>36</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 4,…,39</td>
<td>Bits</td>
<td>7424</td>
<td>12040</td>
<td>16136</td>
<td>21000</td>
<td>25608</td>
<td>33816</td>
<td>44040</td>
<td>53288</td>
<td>71688</td>
<td>90176</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2,3</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 4,…,39</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>9</td>
<td>11</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slot 0,1,2,3</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 4,…,39</td>
<td>Bits</td>
<td>9504</td>
<td>15552</td>
<td>20736</td>
<td>26784</td>
<td>32832</td>
<td>44064</td>
<td>56160</td>
<td>68256</td>
<td>92448</td>
<td>116640</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>26.726</td>
<td>43.344</td>
<td>58.090</td>
<td>75.600</td>
<td>92.189</td>
<td>121.738</td>
<td>158.544</td>
<td>191.837</td>
<td>258.077</td>
<td>324.634</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.2.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

A.3.3 DL reference measurement channels for TDD
-----------------------------------------------

### A.3.3.1 General

Table A.3.3.1-1 Additional reference channels parameters for TDD

+--------------+--------------+--------------+--------------+------+
| Parameter    | Value        |              |              |      |
+==============+==============+==============+==============+======+
|              | SCS 15 kHz   | SCS 30 kHz   | SCS 60 kHz   |      |
|              | (µ=0)        | (µ=1)        | (µ=2)        |      |
+--------------+--------------+--------------+--------------+------+
| TDD Slot     | DDDSU        | 7DS2U        | 1            |      |
| C            |              |              | 4DS~1~S~2~4U |      |
| onfiguration |              |              |              |      |
| pattern      |              |              |              |      |
| (Note 1)     |              |              |              |      |
+--------------+--------------+--------------+--------------+------+
| Special Slot | 10D+2G+2U    | 6D+4G+4U     | S~1~=12D+2G, |      |
| C            |              |              | S~2~=6G+8U   |      |
| onfiguration |              |              |              |      |
| (Note 2)     |              |              |              |      |
+--------------+--------------+--------------+--------------+------+
| re           | 15 kHz       | 30 kHz       | 60 kHz       |      |
| ferenceSubca |              |              |              |      |
| rrierSpacing |              |              |              |      |
+--------------+--------------+--------------+--------------+------+
| UL-DL        | *dl-UL-      | 5 ms         | 5 ms         | 5 ms |
| c            | Transmission |              |              |      |
| onfiguration | Periodicity* |              |              |      |
+--------------+--------------+--------------+--------------+------+
|              | *nrofDo      | 3            | 7            | 14   |
|              | wnlinkSlots* |              |              |      |
+--------------+--------------+--------------+--------------+------+
|              | *nrofDown    | 10           | 6            | 12   |
|              | linkSymbols* |              |              |      |
+--------------+--------------+--------------+--------------+------+
|              | *nro         | 1            | 2            | 4    |
|              | fUplinkSlot* |              |              |      |
+--------------+--------------+--------------+--------------+------+
|              | *nrofUp      | 2            | 4            | 8    |
|              | linkSymbols* |              |              |      |
+--------------+--------------+--------------+--------------+------+
| Number of    | 8            | 8            | 16           |      |
| HARQ         |              |              |              |      |
| Processes    |              |              |              |      |
+--------------+--------------+--------------+--------------+------+
| The number   | K1 = 4 if    | K1 = 8 if    | K1 = 13 if   |      |
| of slots     | mod(i,5) =   | mod(i,10) =  | mod(i,20) =  |      |
| between      | 0\           | 0\           | 2            |      |
| PDSCH and    | K1 = 3 if    | K1 = 7 if    |              |      |
| c            | mod(i,5) =   | mod(i,10) =  | K1 = 12 if   |      |
| orresponding | 1\           | 1\           | mod(i,20) =  |      |
| HARQ-ACK     | K1 = 2 if    | K1 = 6 if    | 3            |      |
| information  | mod(i,5) =   | mod(i,10) =  |              |      |
| (Note 3)     | 2\           | 2\           | K1 = 11 if   |      |
|              | where i is   | K1 = 5 if    | mod(i,20) =  |      |
|              | slot index   | mod(i,10) =  | 4            |      |
|              | per frame; i | 3\           |              |      |
|              | = {0,...,9}  | K1 = 4 if    | K1 = 10 if   |      |
|              |              | mod(i,10) =  | mod(i,20) =  |      |
|              |              | 4\           | 5            |      |
|              |              | K1 = 3 if    |              |      |
|              |              | mod(i,10) =  | K1 = 9 if    |      |
|              |              | 5\           | mod(i,20) =  |      |
|              |              | K1 = 2 if    | 6            |      |
|              |              | mod(i,10) =  |              |      |
|              |              | 6\           | K1 = 8 if    |      |
|              |              | where i is   | mod(i,20) =  |      |
|              |              | slot index   | 7            |      |
|              |              | per frame; i |              |      |
|              |              | = {0,...,19} | K1 = 7 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 8            |      |
|              |              |              |              |      |
|              |              |              | K1 = 6 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 9\           |      |
|              |              |              | K1 = 6 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 10           |      |
|              |              |              |              |      |
|              |              |              | K1 = 6 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 11           |      |
|              |              |              |              |      |
|              |              |              | K1 = 6 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 12\          |      |
|              |              |              | K1 = 6 if    |      |
|              |              |              | mod(i,20) =  |      |
|              |              |              | 13\          |      |
|              |              |              | where i is   |      |
|              |              |              | slot index   |      |
|              |              |              | per frame; i |      |
|              |              |              | = {0,...,39} |      |
+--------------+--------------+--------------+--------------+------+
| NOTE 1: D    |              |              |              |      |
| denotes a    |              |              |              |      |
| slot with    |              |              |              |      |
| all DL       |              |              |              |      |
| symbols; S   |              |              |              |      |
| denotes a    |              |              |              |      |
| slot with a  |              |              |              |      |
| mix of DL,   |              |              |              |      |
| UL and guard |              |              |              |      |
| symbols; U   |              |              |              |      |
| denotes a    |              |              |              |      |
| slot with    |              |              |              |      |
| all UL       |              |              |              |      |
| symbols. The |              |              |              |      |
| field is for |              |              |              |      |
| information. |              |              |              |      |
|              |              |              |              |      |
| NOTE 2: D,   |              |              |              |      |
| G, U denote  |              |              |              |      |
| DL, guard    |              |              |              |      |
| and UL       |              |              |              |      |
| symbols,     |              |              |              |      |
| r            |              |              |              |      |
| espectively. |              |              |              |      |
| The field is |              |              |              |      |
| for          |              |              |              |      |
| information. |              |              |              |      |
|              |              |              |              |      |
| NOTE 3: i is |              |              |              |      |
| the slot     |              |              |              |      |
| index per    |              |              |              |      |
| frame.       |              |              |              |      |
|              |              |              |              |      |
| NOTE 4: A    |              |              |              |      |
| -2ms or +3ms |              |              |              |      |
| time offset  |              |              |              |      |
| to the NR    |              |              |              |      |
| c            |              |              |              |      |
| onfiguration |              |              |              |      |
| pattern      |              |              |              |      |
| relative to  |              |              |              |      |
| the E-UTRA   |              |              |              |      |
| UL-DL        |              |              |              |      |
| c            |              |              |              |      |
| onfiguration |              |              |              |      |
| must be      |              |              |              |      |
| apply in the |              |              |              |      |
| TDD          |              |              |              |      |
| intra-band   |              |              |              |      |
| EN-DC.       |              |              |              |      |
+--------------+--------------+--------------+--------------+------+

### A.3.3.2 FRC for receiver requirements for QPSK

Table A.3.3.2-1 Fixed reference channel for receiver requirements (SCS
15 kHz, TDD, QPSK 1/3)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration <img src="media/image2.wmf" style="width:0.19792in;height:0.19792in" /></td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="even">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>1672</td>
<td>3368</td>
<td>5120</td>
<td>6912</td>
<td>8712</td>
<td>10504</td>
<td>14088</td>
<td>17424</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>16</td>
<td>16</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,3,4,8,9</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,5,6,7</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>5400</td>
<td>11232</td>
<td>17064</td>
<td>22896</td>
<td>28728</td>
<td>34560</td>
<td>46656</td>
<td>58320</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>0.669</td>
<td>1.347</td>
<td>2.048</td>
<td>2.765</td>
<td>3.485</td>
<td>4.202</td>
<td>5.635</td>
<td>6.970</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.3.2-2 Fixed reference channel for receiver requirements (SCS
30 kHz, TDD, QPSK 1/3)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th></th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>70</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration <img src="media/image2.wmf" style="width:0.19792in;height:0.19792in" /></td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>162</td>
<td>217</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>13</td>
<td>11</td>
<td>11</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>736</td>
<td>1608</td>
<td>2472</td>
<td>3368</td>
<td>4224</td>
<td>4992</td>
<td>6912</td>
<td>8712</td>
<td>10504</td>
<td>12296</td>
<td>14088</td>
<td>17928</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>2376</td>
<td>5184</td>
<td>8208</td>
<td>11016</td>
<td>14040</td>
<td>16848</td>
<td>22896</td>
<td>28728</td>
<td>34992</td>
<td>40824</td>
<td>46872</td>
<td>58968</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>0.810</td>
<td>2.1.769</td>
<td>2.719</td>
<td>3.705</td>
<td>4.646</td>
<td>5.491</td>
<td>7.603</td>
<td>9.583</td>
<td>11.554</td>
<td>13.526</td>
<td>15.497</td>
<td>19.721</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

###  

Table A.3.3.2-3 Fixed reference channel for receiver requirements (SCS
60 kHz, TDD, QPSK 1/3)

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Unit</th>
<th></th>
<th>Value</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>70</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration <img src="media/image2.wmf" style="width:0.19792in;height:0.19792in" /></td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>18</td>
<td>24</td>
<td>31</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>79</td>
<td>93</td>
<td>107</td>
<td>135</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>26</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
<td>QPSK</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
<td>1/3</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>Bits</td>
<td>736</td>
<td>1192</td>
<td>1608</td>
<td>2024</td>
<td>2472</td>
<td>3368</td>
<td>4224</td>
<td>5120</td>
<td>6016</td>
<td>6912</td>
<td>8712</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>16</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…,13} for i from {4,…,39}</td>
<td>Bits</td>
<td>2376</td>
<td>3888</td>
<td>5184</td>
<td>6696</td>
<td>8208</td>
<td>11016</td>
<td>14040</td>
<td>17064</td>
<td>20088</td>
<td>23112</td>
<td>29160</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>1.766</td>
<td>3.2.861</td>
<td>3.859</td>
<td>4.858</td>
<td>5.933</td>
<td>8.083</td>
<td>10.138</td>
<td>12.288</td>
<td>14.438</td>
<td>16.589</td>
<td>20.909</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### A.3.3.3 FRC for maximum input level for 64QAM

Table A.3.3.3-1 Fixed reference channel for maximum input level receiver
requirements (SCS 15 kHz, TDD, 64QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Channel bandwidth</strong></td>
<td><strong>MHz</strong></td>
<td><strong>5</strong></td>
<td><strong>10</strong></td>
<td><strong>15</strong></td>
<td><strong>20</strong></td>
<td><strong>25</strong></td>
<td><strong>30</strong></td>
<td><strong>40</strong></td>
<td><strong>50</strong></td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>12296</td>
<td>25608</td>
<td>38936</td>
<td>52224</td>
<td>64552</td>
<td>77896</td>
<td>106576</td>
<td>131176</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,3,4,8,9</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,5,6,7</td>
<td>CBs</td>
<td>2</td>
<td>4</td>
<td>5</td>
<td>7</td>
<td>8</td>
<td>10</td>
<td>13</td>
<td>16</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>16200</td>
<td>33696</td>
<td>51192</td>
<td>68688</td>
<td>86184</td>
<td>103680</td>
<td>139968</td>
<td>174960</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>4.918</td>
<td>10.243</td>
<td>15.574</td>
<td>20.890</td>
<td>20.890</td>
<td>31.158</td>
<td>42.630</td>
<td>52.470</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.3.3-2 Fixed reference channel for maximum input level receiver
requirements (SCS 30 kHz, TDD, 64QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Channel bandwidth</strong></td>
<td><strong>MHz</strong></td>
<td><strong>5</strong></td>
<td><strong>10</strong></td>
<td><strong>15</strong></td>
<td><strong>20</strong></td>
<td><strong>25</strong></td>
<td><strong>30</strong></td>
<td><strong>40</strong></td>
<td><strong>50</strong></td>
<td><strong>60</strong></td>
<td><strong>70</strong></td>
<td><strong>80</strong></td>
<td><strong>100</strong></td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>189</td>
<td>217</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>13</td>
<td>11</td>
<td>11</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>5376</td>
<td>11784</td>
<td>18432</td>
<td>25104</td>
<td>31752</td>
<td>37896</td>
<td>52224</td>
<td>64552</td>
<td>79896</td>
<td>92200</td>
<td>106576</td>
<td>135296</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>7</td>
<td>8</td>
<td>10</td>
<td>11</td>
<td>13</td>
<td>17</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>7128</td>
<td>15552</td>
<td>24624</td>
<td>33048</td>
<td>42120</td>
<td>50544</td>
<td>68688</td>
<td>86184</td>
<td>104976</td>
<td>122472</td>
<td>140616</td>
<td>176904</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>5.914</td>
<td>12.962</td>
<td>20.275</td>
<td>27.614</td>
<td>34.927</td>
<td>41.686</td>
<td>57.446</td>
<td>71.007</td>
<td>87.886</td>
<td>101.42</td>
<td>117.234</td>
<td>148.826</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

###  

Table A.3.3.3-3. Fixed reference channel for maximum input level
receiver requirements (SCS 60 kHz, TDD, 64QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Channel bandwidth</strong></td>
<td><strong>MHz</strong></td>
<td><strong>10</strong></td>
<td><strong>15</strong></td>
<td><strong>20</strong></td>
<td><strong>25</strong></td>
<td><strong>30</strong></td>
<td><strong>40</strong></td>
<td><strong>50</strong></td>
<td><strong>60</strong></td>
<td><strong>70</strong></td>
<td><strong>80</strong></td>
<td><strong>100</strong></td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>18</td>
<td>24</td>
<td>31</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>79</td>
<td>93</td>
<td>107</td>
<td>135</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>26</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>64QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
<td>64 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
<td>3/4</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>Bits</td>
<td>5376</td>
<td>8712</td>
<td>11784</td>
<td>15112</td>
<td>18432</td>
<td>25104</td>
<td>31752</td>
<td>38936</td>
<td>45096</td>
<td>52224</td>
<td>65576</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>Bits</td>
<td>7128</td>
<td>11664</td>
<td>15552</td>
<td>20088</td>
<td>24624</td>
<td>33048</td>
<td>42120</td>
<td>51192</td>
<td>60264</td>
<td>69336</td>
<td>87480</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>12.902</td>
<td>20.909</td>
<td>28.282</td>
<td>36.269</td>
<td>44.237</td>
<td>60.250</td>
<td>76.205</td>
<td>93.446</td>
<td>108.23</td>
<td>125.338</td>
<td>157.382</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### A.3.3.4 FRC for maximum input level for 256 QAM

Table A.3.3.4-1 Fixed reference channel for maximum input level receiver
requirements (SCS 15 kHz, TDD, 256QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Channel bandwidth</strong></td>
<td><strong>MHz</strong></td>
<td><strong>5</strong></td>
<td><strong>10</strong></td>
<td><strong>15</strong></td>
<td><strong>20</strong></td>
<td><strong>25</strong></td>
<td><strong>30</strong></td>
<td><strong>40</strong></td>
<td><strong>50</strong></td>
</tr>
<tr class="even">
<td>Subcarrier spacing</td>
<td>kHz</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
<td>15</td>
</tr>
<tr class="odd">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td>Allocated resource blocks</td>
<td></td>
<td>25</td>
<td>52</td>
<td>79</td>
<td>106</td>
<td>133</td>
<td>160</td>
<td>216</td>
<td>270</td>
</tr>
<tr class="odd">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="even">
<td>Allocated slots per Frame</td>
<td></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="even">
<td>MCS table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="even">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="odd">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>16896</td>
<td>34816</td>
<td>53288</td>
<td>71688</td>
<td>90176</td>
<td>108552</td>
<td>143400</td>
<td>180376</td>
</tr>
<tr class="odd">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,3,4,8,9</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slots 2,5,6,7</td>
<td>CBs</td>
<td>3</td>
<td>5</td>
<td>7</td>
<td>9</td>
<td>12</td>
<td>14</td>
<td>18</td>
<td>23</td>
</tr>
<tr class="even">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,3,4,8,9</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slots 2,5,6,7</td>
<td>Bits</td>
<td>21600</td>
<td>44928</td>
<td>68256</td>
<td>91584</td>
<td>114912</td>
<td>138240</td>
<td>186624</td>
<td>233280</td>
</tr>
<tr class="odd">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>6.758</td>
<td>13.926</td>
<td>21.315</td>
<td>28.675</td>
<td>36.070</td>
<td>43.421</td>
<td>57.360</td>
<td>72.150</td>
</tr>
<tr class="even">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot 0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table A.3.3.4-2 Fixed Reference channel for maximum input level receiver
requirements (SCS 30 kHz, TDD, 256QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>5</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>70</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>24</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>78</td>
<td>106</td>
<td>133</td>
<td>162</td>
<td>189</td>
<td>217</td>
<td>273</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>11</td>
<td>13</td>
<td>11</td>
<td>11</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>7424</td>
<td>16136</td>
<td>25608</td>
<td>33816</td>
<td>44040</td>
<td>52224</td>
<td>71688</td>
<td>90176</td>
<td>108552</td>
<td>127080</td>
<td>147576</td>
<td>184424</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>CBs</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2 and Slot i, if mod(i, 10) = {7,8,9} for i from {0,…,19}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 10) = {0,1,2,3,4,5,6} for i from {3,…,19}</td>
<td>Bits</td>
<td>9504</td>
<td>20736</td>
<td>32832</td>
<td>44064</td>
<td>56160</td>
<td>67392</td>
<td>91584</td>
<td>114912</td>
<td>139968</td>
<td>163296</td>
<td>187488</td>
<td>235872</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>8.166</td>
<td>17.750</td>
<td>28.169</td>
<td>37.198</td>
<td>48.444</td>
<td>57.446</td>
<td>78.857</td>
<td>99.194</td>
<td>119.407</td>
<td>139.788</td>
<td>162.334</td>
<td>202.866</td>
</tr>
<tr class="odd">
<td></td>
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

###  

Table A.3.3.4-3 Fixed reference channel for maximum input level receiver
requirements (SCS 60 kHz, TDD, 256QAM)

<table>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Unit</strong></th>
<th></th>
<th><strong>Value</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Channel bandwidth</td>
<td>MHz</td>
<td>10</td>
<td>15</td>
<td>20</td>
<td>25</td>
<td>30</td>
<td>40</td>
<td>50</td>
<td>60</td>
<td>70</td>
<td>80</td>
<td>100</td>
</tr>
<tr class="even">
<td>Subcarrier spacing configuration</td>
<td></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Allocated resource blocks</td>
<td></td>
<td>11</td>
<td>18</td>
<td>24</td>
<td>31</td>
<td>38</td>
<td>51</td>
<td>65</td>
<td>79</td>
<td>93</td>
<td>107</td>
<td>135</td>
</tr>
<tr class="even">
<td>Subcarriers per resource block</td>
<td></td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Allocated slots per Frame</td>
<td></td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>26</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="even">
<td>MCS Index</td>
<td></td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
<td>23</td>
</tr>
<tr class="odd">
<td>MCS Table for TBS determination</td>
<td></td>
<td>256QAM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Modulation</td>
<td></td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
<td>256 QAM</td>
</tr>
<tr class="odd">
<td>Target Coding Rate</td>
<td></td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
<td>4/5</td>
</tr>
<tr class="even">
<td>Maximum number of HARQ transmissions</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Information Bit Payload per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>Bits</td>
<td>7424</td>
<td>12040</td>
<td>16136</td>
<td>21000</td>
<td>25608</td>
<td>33816</td>
<td>44040</td>
<td>53288</td>
<td>62504</td>
<td>71688</td>
<td>90176</td>
</tr>
<tr class="even">
<td>Transport block CRC</td>
<td>Bits</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
<td>24</td>
</tr>
<tr class="odd">
<td>LDPC base graph</td>
<td></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Number of Code Blocks per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>CBs</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>CBs</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Binary Channel Bits per Slot</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>For Slots 0,1,2,3 and Slot i, if mod(i, 20) = {14,15,16,17,18,19} for i from {0,…,39}</td>
<td>Bits</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>For Slot i, if mod(i, 20) = {0,…, 13} for i from {4,…,39}</td>
<td>Bits</td>
<td>9504</td>
<td>15552</td>
<td>20736</td>
<td>26784</td>
<td>32832</td>
<td>44064</td>
<td>56160</td>
<td>68256</td>
<td>80352</td>
<td>92448</td>
<td>116640</td>
</tr>
<tr class="even">
<td>Max. Throughput averaged over 1 frame</td>
<td>Mbps</td>
<td>17.818</td>
<td>28.896</td>
<td>38.726</td>
<td>50.400</td>
<td>61.459</td>
<td>81.158</td>
<td>105.696</td>
<td>127.891</td>
<td>150.010</td>
<td>172.051</td>
<td>216.422</td>
</tr>
<tr class="odd">
<td><p>NOTE 1: Additional parameters are specified in Table A.3.1-1 and Table A.3.3.1-1.</p>
<p>NOTE 2: If more than one Code Block is present, an additional CRC sequence of L = 24 Bits is attached to each Code Block (otherwise L = 0 Bit).</p>
<p>NOTE 3: SS/PBCH block is transmitted in slot #0 of each frame</p>
<p>NOTE 4: Slot i is slot index per frame</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

A.4 CSI reference measurement channels
======================================

A.5 OFDMA Channel Noise Generator (OCNG)
========================================

A.5.1 OCNG Patterns for FDD
---------------------------

### A.5.1.1 OCNG FDD pattern 1: Generic OCNG FDD Pattern for all unused REs

Table A.5.1.1-1: OP.1 FDD: Generic OCNG FDD Pattern for all unused REs

+----------------------+----------------------+----------------------+
| OCNG Appliance       | Control Region\      | Data Region          |
|                      | (Core Set)           |                      |
| OCNG Parameters      |                      |                      |
+======================+======================+======================+
| Resources allocated  | All unused REs (Note | All unused REs (Note |
|                      | 1)                   | 2)                   |
+----------------------+----------------------+----------------------+
| Structure            | PDCCH                | PDSCH                |
+----------------------+----------------------+----------------------+
| Content              | Uncorrelated pseudo  | Uncorrelated pseudo  |
|                      | random QPSK          | random QPSK          |
|                      | modulated data       | modulated data       |
+----------------------+----------------------+----------------------+
| Transmission scheme  | Single Tx port       | Spatial multiplexing |
| for multiple         | transmission         | using any precoding  |
|                      |                      | matrix with          |
| antennas ports       |                      | dimensions same as   |
| transmission         |                      | the precoding matrix |
|                      |                      | for PDSCH            |
+----------------------+----------------------+----------------------+
| Subcarrier Spacing   | Same as for RMC      | Same as for RMC      |
|                      | PDCCH in the active  | PDSCH in the active  |
|                      | BWP                  | BWP                  |
+----------------------+----------------------+----------------------+
| Power Level          | Same as for RMC      | Same as for RMC      |
|                      | PDCCH                | PDSCH                |
+----------------------+----------------------+----------------------+
| NOTE 1: All unused   |                      |                      |
| REs in the active    |                      |                      |
| CORESETS appointed   |                      |                      |
| by the search spaces |                      |                      |
| in use.              |                      |                      |
|                      |                      |                      |
| NOTE 2: Unused       |                      |                      |
| available REs refer  |                      |                      |
| to REs in PRBs not   |                      |                      |
| allocated for any    |                      |                      |
| physical channels,   |                      |                      |
| CORESETs,            |                      |                      |
| synchronization      |                      |                      |
| signals or reference |                      |                      |
| signals in channel   |                      |                      |
| bandwidth.           |                      |                      |
+----------------------+----------------------+----------------------+

A.5.2 OCNG Patterns for TDD
---------------------------

### A.5.2.1 OCNG TDD pattern 1: Generic OCNG TDD Pattern for all unused REs

Table A.5.2.1-1: OP.1 TDD: Generic OCNG TDD Pattern for all unused REs

+----------------------+----------------------+----------------------+
| OCNG Appliance       | Control Region\      | Data Region          |
|                      | (Core Set)           |                      |
| OCNG Parameters      |                      |                      |
+======================+======================+======================+
| Resources allocated  | All unused REs (Note | All unused REs (Note |
|                      | 1)                   | 2)                   |
+----------------------+----------------------+----------------------+
| Structure            | PDCCH                | PDSCH                |
+----------------------+----------------------+----------------------+
| Content              | Uncorrelated pseudo  | Uncorrelated pseudo  |
|                      | random QPSK          | random QPSK          |
|                      | modulated data       | modulated data       |
+----------------------+----------------------+----------------------+
| Transmission scheme  | Single Tx port       | Spatial multiplexing |
| for multiple         | transmission         | using any precoding  |
|                      |                      | matrix with          |
| antennas ports       |                      | dimensions same as   |
| transmission         |                      | the precoding matrix |
|                      |                      | for PDSCH            |
+----------------------+----------------------+----------------------+
| Subcarrier Spacing   | Same as for RMC      | Same as for RMC      |
|                      | PDCCH in the active  | PDSCH in the active  |
|                      | BWP                  | BWP                  |
+----------------------+----------------------+----------------------+
| Power Level          | Same as for RMC      | Same as for RMC      |
|                      | PDCCH                | PDSCH                |
+----------------------+----------------------+----------------------+
| NOTE 1: All unused   |                      |                      |
| REs in the active    |                      |                      |
| CORESETS appointed   |                      |                      |
| by the search spaces |                      |                      |
| in use.              |                      |                      |
|                      |                      |                      |
| NOTE 2: Unused       |                      |                      |
| available REs refer  |                      |                      |
| to REs in PRBs not   |                      |                      |
| allocated for any    |                      |                      |
| physical channels,   |                      |                      |
| CORESETs,            |                      |                      |
| synchronization      |                      |                      |
| signals or reference |                      |                      |
| signals in channel   |                      |                      |
| bandwidth.           |                      |                      |
+----------------------+----------------------+----------------------+

A.6 Void
========

A.7 V2X reference measurement channels
======================================

A.7.1 General
-------------

The algorithm for determining the payload size A is as follows; given a
desired coding rate R and radio block allocation NRB

1\. Calculate the RE number of 2nd stage SCI Q\_SCI2\^\' that can be
transmitted in a given sub-frame, where in order to make sure that the
code-rate of 2-A is approximate to SCI 1-A, a beta offset is selected
based on MCS, and vacant resource elements γ value is determined based
on NRB and DMRS frequency density.

2\. Transport Block Size is determined according to clause 8.1.3.2 of TS
38.214 \[13\] based on Table A.7.1-1.

3\. Calculate Binary Channel Bits per Slot for PSSCH as below

Binary Channel Bits per Slot = (NRB\* Subcarriers per resource
block\*CP-OFDM symbols per slot -- DMRS resource REs -- PSCCH resource
Res - Q\_SCI2\^\') \* Qm

Where Qm is the modulation order corresponding to MCS.

In Table A.7.1-1 Common reference channel parameters are listed the
Sidelink reference measurement channels specified in annexes A.7.2 to
A.7.6.

Table A.7.1-1: Common reference channel parameters

+----------------------+----------------------+----------------------+
| Parameter            | Value                | remark               |
+======================+======================+======================+
| Number of HARQ       | 1                    |                      |
| Processes            |                      |                      |
+----------------------+----------------------+----------------------+
| Channel state        | AWGN                 |                      |
+----------------------+----------------------+----------------------+
| Subcarriers per      | 12                   |                      |
| resource block       |                      |                      |
+----------------------+----------------------+----------------------+
| sl-PSSCH-            | 2                    | symbol4 and symbol   |
| DMRS-TimePatternList |                      | 10 in each slot      |
|                      |                      |                      |
|                      |                      | FDMed with PSSCH     |
|                      |                      | within DMRS symbol   |
|                      |                      |                      |
|                      |                      | Frequency density is |
|                      |                      | ½                    |
+----------------------+----------------------+----------------------+
| CP-OFDM symbols per  | 12 for all slots     | Excluding the first  |
| slot (Note1)         |                      | OFDM symbol in one   |
|                      |                      | SL slot used for AGC |
+----------------------+----------------------+----------------------+
| PSCCH resource       | 10 PRBs, 3 symbols   |                      |
|                      | in time domain       |                      |
+----------------------+----------------------+----------------------+
| Slot number in 10ms  | $$10*2^{\mu}$$       | $\mu = 0,1,2$ for    |
|                      |                      | 15kHz, 30kHz, 60kHz  |
+----------------------+----------------------+----------------------+
| PT-RS                | *disable*            |                      |
+----------------------+----------------------+----------------------+
| CSI-RS               | *disable*            |                      |
+----------------------+----------------------+----------------------+
| x-overhead           | *0*                  |                      |
+----------------------+----------------------+----------------------+
| PSFCH period         | *0*                  |                      |
+----------------------+----------------------+----------------------+
| 2^nd^ stage SCI      | *59*                 | *35bits SCI-2A +     |
| payload size         |                      | 24bits CRC*          |
+----------------------+----------------------+----------------------+
| Redundancy Version   | RV0                  | For channel coding   |
+----------------------+----------------------+----------------------+
| Alpha value for      | *1*                  |                      |
| SCI-2                |                      |                      |
+----------------------+----------------------+----------------------+

A.7.2 FRC for V2X receiver requirements for QPSK
------------------------------------------------

For V2X transmission over PC5, Table A.7.2-1, Table A.7.2-2 and Table
A.7.2-3 are applicable for measurements on the Receiver Characteristics
with the exception of Maximum input level.

Table A.7.2-1: Fixed reference channel for V2X receiver requirements
(SCS 15 kHz, QPSK)

+---------------------+-------+--------+--------+--------+--------+
| Parameter           | Unit  | Value  |        |        |        |
+=====================+=======+========+========+========+========+
| Channel bandwidth   | MHz   | 10     | 20     | 30     | 40     |
+---------------------+-------+--------+--------+--------+--------+
| Subcarrier spacing  | kHz   | 15     | 15     | 15     | 15     |
+---------------------+-------+--------+--------+--------+--------+
| Subchannel size     |       | 10     | 15     | 10     | 12     |
+---------------------+-------+--------+--------+--------+--------+
| Allocated resource  |       | 50     | 105    | 160    | 216    |
| blocks              |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| MCS Index           |       | 4      | 4      | 4      | 4      |
+---------------------+-------+--------+--------+--------+--------+
| MCS Table for TBS   | 64QAM |        |        |        |        |
| determination       |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Modulation          |       | QPSK   | QPSK   | QPSK   | QPSK   |
+---------------------+-------+--------+--------+--------+--------+
| Transport Block     |       | 3624   | 7936   | 12296  | 16896  |
| Size                |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Transport block CRC | Bits  | 16     | 24     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| LDPC base graph     |       | 2      | 1      | 1      | 1      |
+---------------------+-------+--------+--------+--------+--------+
| Number of Code      |       | 1      | 1      | 2      | 3      |
| Blocks per Slot     |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Beta offset for 2nd |       | 2.25   | 2.25   | 2.25   | 2.25   |
| stage SCI           |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| $\gamma$ value when |       | 1      | 1      | 1      | 1      |
| 2nd stage SCI rate  |       |        |        |        |        |
| match               |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Binary Channel Bits |       | 12036  | 26556  | 41076  | 55860  |
| per Slot            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Max. Throughput     | Mbps  | 0.3624 | 0.7936 | 1.2296 | 1.6896 |
| averaged over 100ms |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| NOTE 1: If more     |       |        |        |        |        |
| than one Code Block |       |        |        |        |        |
| is present, an      |       |        |        |        |        |
| additional CRC      |       |        |        |        |        |
| sequence of L = 24  |       |        |        |        |        |
| Bits is attached to |       |        |        |        |        |
| each Code Block     |       |        |        |        |        |
| (otherwise L = 0    |       |        |        |        |        |
| Bit).               |       |        |        |        |        |
|                     |       |        |        |        |        |
| NOTE 2: $\gamma$ is |       |        |        |        |        |
| the number of       |       |        |        |        |        |
| vacant resource     |       |        |        |        |        |
| elements in the     |       |        |        |        |        |
| resource block to   |       |        |        |        |        |
| which the last      |       |        |        |        |        |
| coded symbol of the |       |        |        |        |        |
| 2^nd^-stage SCI     |       |        |        |        |        |
| belongs.            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+

Table A.7.2-2: Fixed reference channel for V2X receiver requirements
(SCS 30 kHz, QPSK)

+---------------------+-------+--------+--------+--------+--------+
| Parameter           | Unit  | Value  |        |        |        |
+=====================+=======+========+========+========+========+
| Channel bandwidth   | MHz   | 10     | 20     | 30     | 40     |
+---------------------+-------+--------+--------+--------+--------+
| Subcarrier spacing  | kHz   | 30     | 30     | 30     | 30     |
+---------------------+-------+--------+--------+--------+--------+
| Subchannel size     |       | 12     | 10     | 15     | 15     |
+---------------------+-------+--------+--------+--------+--------+
| Allocated resource  |       | 24     | 50     | 75     | 105    |
| blocks              |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| MCS Index           |       | 4      | 4      | 4      | 4      |
+---------------------+-------+--------+--------+--------+--------+
| MCS Table for TBS   | 64QAM |        |        |        |        |
| determination       |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Modulation          |       | QPSK   | QPSK   | QPSK   | QPSK   |
+---------------------+-------+--------+--------+--------+--------+
| Transport Block     |       | 1608   | 3624   | 5632   | 7936   |
| Size                |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Transport block CRC | Bits  | 16     | 16     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| LDPC base graph     |       | 2      | 2      | 1      | 1      |
+---------------------+-------+--------+--------+--------+--------+
| Number of Code      |       | 1      | 1      | 1      | 1      |
| Blocks per Slot     |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Beta offset for 2nd |       | 2.25   | 2.25   | 2.25   | 2.25   |
| stage SCI           |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| $\gamma$ value when |       | 7      | 1      | 1      | 1      |
| 2nd stage SCI rate  |       |        |        |        |        |
| match               |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Binary Channel Bits |       | 5160   | 12036  | 18636  | 26556  |
| per Slot            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Max. Throughput     | Mbps  | 0.3216 | 0.7248 | 1.1264 | 1.5872 |
| averaged over 100ms |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| NOTE 1: If more     |       |        |        |        |        |
| than one Code Block |       |        |        |        |        |
| is present, an      |       |        |        |        |        |
| additional CRC      |       |        |        |        |        |
| sequence of L = 24  |       |        |        |        |        |
| Bits is attached to |       |        |        |        |        |
| each Code Block     |       |        |        |        |        |
| (otherwise L = 0    |       |        |        |        |        |
| Bit).               |       |        |        |        |        |
|                     |       |        |        |        |        |
| NOTE 2: $\gamma$ is |       |        |        |        |        |
| the number of       |       |        |        |        |        |
| vacant resource     |       |        |        |        |        |
| elements in the     |       |        |        |        |        |
| resource block to   |       |        |        |        |        |
| which the last      |       |        |        |        |        |
| coded symbol of the |       |        |        |        |        |
| 2^nd^-stage SCI     |       |        |        |        |        |
| belongs.            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+

Table A.7.2-3: Fixed reference channel for V2X receiver requirements
(SCS 60 kHz, QPSK)

+---------------------+-------+--------+--------+--------+--------+
| Parameter           | Unit  | Value  |        |        |        |
+=====================+=======+========+========+========+========+
| Channel bandwidth   | MHz   | 10     | 20     | 30     | 40     |
+---------------------+-------+--------+--------+--------+--------+
| Subcarrier spacing  | kHz   | 60     | 60     | 60     | 60     |
+---------------------+-------+--------+--------+--------+--------+
| Subchannel size     |       | 10     | 12     | 12     | 10     |
+---------------------+-------+--------+--------+--------+--------+
| Allocated resource  |       | 10     | 24     | 36     | 50     |
| blocks              |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| MCS Index           |       | 4      | 4      | 4      | 4      |
+---------------------+-------+--------+--------+--------+--------+
| MCS Table for TBS   | 64QAM |        |        |        |        |
| determination       |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Modulation          |       | QPSK   | QPSK   | QPSK   | QPSK   |
+---------------------+-------+--------+--------+--------+--------+
| Transport Block     |       | 456    | 1608   | 2536   | 3624   |
| Size                |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Transport block CRC | Bits  | 16     | 16     | 16     | 16     |
+---------------------+-------+--------+--------+--------+--------+
| LDPC base graph     |       | 2      | 2      | 2      | 2      |
+---------------------+-------+--------+--------+--------+--------+
| Number of Code      |       | 1      | 1      | 1      | 1      |
| Blocks per Slot     |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Beta offset for 2nd |       | 2.25   | 2.25   | 2.25   | 2.25   |
| stage SCI           |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| $\gamma$ value when |       | 7      | 7      | 7      | 1      |
| 2nd stage SCI rate  |       |        |        |        |        |
| match               |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Binary Channel Bits |       | 1464   | 5160   | 8328   | 12036  |
| per Slot            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Max. Throughput     | Mbps  | 0.1824 | 0.6432 | 1.0144 | 1.4496 |
| averaged over 100ms |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| NOTE 1: If more     |       |        |        |        |        |
| than one Code Block |       |        |        |        |        |
| is present, an      |       |        |        |        |        |
| additional CRC      |       |        |        |        |        |
| sequence of L = 24  |       |        |        |        |        |
| Bits is attached to |       |        |        |        |        |
| each Code Block     |       |        |        |        |        |
| (otherwise L = 0    |       |        |        |        |        |
| Bit).               |       |        |        |        |        |
|                     |       |        |        |        |        |
| NOTE 2: $\gamma$ is |       |        |        |        |        |
| the number of       |       |        |        |        |        |
| vacant resource     |       |        |        |        |        |
| elements in the     |       |        |        |        |        |
| resource block to   |       |        |        |        |        |
| which the last      |       |        |        |        |        |
| coded symbol of the |       |        |        |        |        |
| 2^nd^-stage SCI     |       |        |        |        |        |
| belongs.            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+

A.7.3 FRC for maximum input level for 64QAM
-------------------------------------------

For V2X transmission over PC5, Table A.7.3-1, Table A.7.3-2 and
TableA.7.3-3 are applicable for Maximum input level when the maximum
modulation order is 64QAM.

Table A.7.3-1: Fixed reference channel for V2X receiver requirements
(SCS 15 kHz, 64QAM)

+---------------------+-------+--------+--------+--------+--------+
| Parameter           | Unit  | Value  |        |        |        |
+=====================+=======+========+========+========+========+
| Channel bandwidth   | MHz   | 10     | 20     | 30     | 40     |
+---------------------+-------+--------+--------+--------+--------+
| Subcarrier spacing  | kHz   | 15     | 15     | 15     | 15     |
+---------------------+-------+--------+--------+--------+--------+
| Subchannel size     |       | 10     | 15     | 10     | 12     |
+---------------------+-------+--------+--------+--------+--------+
| Allocated resource  |       | 50     | 105    | 160    | 216    |
| blocks              |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| MCS Index           |       | 24     | 24     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| MCS Table for TBS   | 64QAM |        |        |        |        |
| determination       |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Modulation          |       | 64QAM  | 64QAM  | 64QAM  | 64QAM  |
+---------------------+-------+--------+--------+--------+--------+
| Transport Block     |       | 27144  | 60456  | 92200  | 127080 |
| Size                |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Transport block CRC | Bits  | 24     | 24     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| LDPC base graph     |       | 1      | 1      | 1      | 1      |
+---------------------+-------+--------+--------+--------+--------+
| Number of Code      |       | 4      | 8      | 11     | 16     |
| Blocks per Slot     |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Beta offset for 2nd |       | 6.25   | 6.25   | 6.25   | 6.25   |
| stage SCI           |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| $\gamma$ value when |       | 1      | 1      | 1      | 1      |
| 2nd stage SCI rate  |       |        |        |        |        |
| match               |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Binary Channel Bits |       | 35964  | 79524  | 123084 | 167436 |
| per Slot            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Max. Throughput     | Mbps  | 2.7144 | 6.0456 | 9.22   | 12.708 |
| averaged over 100ms |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| NOTE 1: If more     |       |        |        |        |        |
| than one Code Block |       |        |        |        |        |
| is present, an      |       |        |        |        |        |
| additional CRC      |       |        |        |        |        |
| sequence of L = 24  |       |        |        |        |        |
| Bits is attached to |       |        |        |        |        |
| each Code Block     |       |        |        |        |        |
| (otherwise L = 0    |       |        |        |        |        |
| Bit).               |       |        |        |        |        |
|                     |       |        |        |        |        |
| NOTE 2: $\gamma$ is |       |        |        |        |        |
| the number of       |       |        |        |        |        |
| vacant resource     |       |        |        |        |        |
| elements in the     |       |        |        |        |        |
| resource block to   |       |        |        |        |        |
| which the last      |       |        |        |        |        |
| coded symbol of the |       |        |        |        |        |
| 2^nd^-stage SCI     |       |        |        |        |        |
| belongs.            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+

Table A.7.3-2: Fixed reference channel for V2X receiver requirements
(SCS 30 kHz, 64QAM)

+---------------------+-------+--------+--------+--------+--------+
| Parameter           | Unit  | Value  |        |        |        |
+=====================+=======+========+========+========+========+
| Channel bandwidth   | MHz   | 10     | 20     | 30     | 40     |
+---------------------+-------+--------+--------+--------+--------+
| Subcarrier spacing  | kHz   | 30     | 30     | 30     | 30     |
+---------------------+-------+--------+--------+--------+--------+
| Subchannel size     |       | 12     | 10     | 15     | 15     |
+---------------------+-------+--------+--------+--------+--------+
| Allocated resource  |       | 24     | 50     | 75     | 105    |
| blocks              |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| MCS Index           |       | 24     | 24     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| MCS Table for TBS   | 64QAM |        |        |        |        |
| determination       |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Modulation          |       | 64QAM  | 64QAM  | 64QAM  | 64QAM  |
+---------------------+-------+--------+--------+--------+--------+
| Transport Block     |       | 11528  | 27144  | 42016  | 60456  |
| Size                |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Transport block CRC | Bits  | 24     | 24     | 24     | 24     |
+---------------------+-------+--------+--------+--------+--------+
| LDPC base graph     |       | 1      | 1      | 1      | 1      |
+---------------------+-------+--------+--------+--------+--------+
| Number of Code      |       | 2      | 4      | 5      | 8      |
| Blocks per Slot     |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Beta offset for 2nd |       | 6.25   | 6.25   | 6.25   | 6.25   |
| stage SCI           |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| $\gamma$ value when |       | 7      | 1      | 1      | 1      |
| 2nd stage SCI rate  |       |        |        |        |        |
| match               |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Binary Channel Bits |       | 15336  | 35964  | 55764  | 79524  |
| per Slot            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| Max. Throughput     | Mbps  | 2.3056 | 5.4288 | 8.4032 | 12.091 |
| averaged over 100ms |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+
| NOTE 1: If more     |       |        |        |        |        |
| than one Code Block |       |        |        |        |        |
| is present, an      |       |        |        |        |        |
| additional CRC      |       |        |        |        |        |
| sequence of L = 24  |       |        |        |        |        |
| Bits is attached to |       |        |        |        |        |
| each Code Block     |       |        |        |        |        |
| (otherwise L = 0    |       |        |        |        |        |
| Bit).               |       |        |        |        |        |
|                     |       |        |        |        |        |
| NOTE                |       |        |        |        |        |
| 2                   |       |        |        |        |        |
| :$\text{\ \ \ \ γ}$ |       |        |        |        |        |
| is the number of    |       |        |        |        |        |
| vacant resource     |       |        |        |        |        |
| elements in the     |       |        |        |        |        |
| resource block to   |       |        |        |        |        |
| which the last      |       |        |        |        |        |
| coded symbol of the |       |        |        |        |        |
| 2^nd^-stage SCI     |       |        |        |        |        |
| belongs.            |       |        |        |        |        |
+---------------------+-------+--------+--------+--------+--------+

TableA.7.3-3: Fixed reference channel for V2X receiver requirements (SCS
60 kHz, 64QAM)

+-----------------------+-------+-------+--------+-------+--------+
| Parameter             | Unit  | Value |        |       |        |
+=======================+=======+=======+========+=======+========+
| Channel bandwidth     | MHz   | 10    | 20     | 30    | 40     |
+-----------------------+-------+-------+--------+-------+--------+
| Subcarrier spacing    | kHz   | 60    | 60     | 60    | 60     |
+-----------------------+-------+-------+--------+-------+--------+
| Subchannel size       |       | 10    | 12     | 12    | 10     |
+-----------------------+-------+-------+--------+-------+--------+
| Allocated resource    |       | 10    | 24     | 36    | 50     |
| blocks                |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| MCS Index             |       | 24    | 24     | 24    | 24     |
+-----------------------+-------+-------+--------+-------+--------+
| MCS Table for TBS     | 64QAM |       |        |       |        |
| determination         |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| Modulation            |       | 64QAM | 64QAM  | 64QAM | 64QAM  |
+-----------------------+-------+-------+--------+-------+--------+
| Transport Block Size  |       | 3240  | 11528  | 18960 | 27144  |
+-----------------------+-------+-------+--------+-------+--------+
| Transport block CRC   | Bits  | 16    | 24     | 24    | 24     |
+-----------------------+-------+-------+--------+-------+--------+
| LDPC base graph       |       | 2     | 1      | 1     | 1      |
+-----------------------+-------+-------+--------+-------+--------+
| Number of Code Blocks |       | 1     | 2      | 3     | 4      |
| per Slot              |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| Beta offset for 2nd   |       | 6.25  | 6.25   | 6.25  | 6.25   |
| stage SCI             |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| $\gamma$ value when   |       | 7     | 7      | 7     | 1      |
| 2nd stage SCI rate    |       |       |        |       |        |
| match                 |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| Binary Channel Bits   |       | 4248  | 15336  | 24840 | 35964  |
| per Slot              |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| Max. Throughput       | Mbps  | 1.296 | 4.6112 | 7.584 | 10.858 |
| averaged over 100ms   |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+
| NOTE 1: If more than  |       |       |        |       |        |
| one Code Block is     |       |       |        |       |        |
| present, an           |       |       |        |       |        |
| additional CRC        |       |       |        |       |        |
| sequence of L = 24    |       |       |        |       |        |
| Bits is attached to   |       |       |        |       |        |
| each Code Block       |       |       |        |       |        |
| (otherwise L = 0      |       |       |        |       |        |
| Bit).                 |       |       |        |       |        |
|                       |       |       |        |       |        |
| NOTE 2: $\gamma$ is   |       |       |        |       |        |
| the number of vacant  |       |       |        |       |        |
| resource elements in  |       |       |        |       |        |
| the resource block to |       |       |        |       |        |
| which the last coded  |       |       |        |       |        |
| symbol of the         |       |       |        |       |        |
| 2^nd^-stage SCI       |       |       |        |       |        |
| belongs.              |       |       |        |       |        |
+-----------------------+-------+-------+--------+-------+--------+

A.7.4 FRC for maximum input level for 256QAM
--------------------------------------------

For V2X transmission over PC5, Table A.7.4-1, Table A.7.4-2 and Table
A.7.4-3 are applicable for Maximum input level when the 256QAM is
supported.

Table A.7.4-1: Fixed reference channel for V2X receiver requirements
(SCS 15 kHz, 256QAM)

+--------------------+--------+--------+--------+--------+--------+
| Parameter          | Unit   | Value  |        |        |        |
+====================+========+========+========+========+========+
| Channel bandwidth  | MHz    | 10     | 20     | 30     | 40     |
+--------------------+--------+--------+--------+--------+--------+
| Subcarrier spacing | kHz    | 15     | 15     | 15     | 15     |
+--------------------+--------+--------+--------+--------+--------+
| Subchannel size    |        | 10     | 15     | 10     | 12     |
+--------------------+--------+--------+--------+--------+--------+
| Allocated resource |        | 50     | 105    | 160    | 216    |
| blocks             |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| MCS Index          |        | 23     | 23     | 23     | 23     |
+--------------------+--------+--------+--------+--------+--------+
| MCS Table for TBS  | 256QAM |        |        |        |        |
| determination      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Modulation         |        | 256QAM | 256QAM | 256QAM | 256QAM |
+--------------------+--------+--------+--------+--------+--------+
| Transport Block    |        | 36896  | 81976  | 127080 | 172176 |
| Size               |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Transport block    | Bits   | 24     | 24     | 24     | 24     |
| CRC                |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| LDPC base graph    |        | 1      | 1      | 1      | 1      |
+--------------------+--------+--------+--------+--------+--------+
| Number of Code     |        | 5      | 10     | 16     | 21     |
| Blocks per Slot    |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Beta offset for    |        | 6.25   | 6.25   | 6.25   | 6.25   |
| 2nd stage SCI      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| $\gamma$ value     |        | 3      | 3      | 3      | 3      |
| when 2nd stage SCI |        |        |        |        |        |
| rate match         |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Binary Channel     |        | 48000  | 106080 | 164160 | 223296 |
| Bits per Slot      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Max. Throughput    | Mbps   | 3.6896 | 8.1976 | 12.708 | 17.218 |
| averaged over      |        |        |        |        |        |
| 100ms              |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| NOTE 1: If more    |        |        |        |        |        |
| than one Code      |        |        |        |        |        |
| Block is present,  |        |        |        |        |        |
| an additional CRC  |        |        |        |        |        |
| sequence of L = 24 |        |        |        |        |        |
| Bits is attached   |        |        |        |        |        |
| to each Code Block |        |        |        |        |        |
| (otherwise L = 0   |        |        |        |        |        |
| Bit).              |        |        |        |        |        |
|                    |        |        |        |        |        |
| NOTE 2: $\gamma$   |        |        |        |        |        |
| is the number of   |        |        |        |        |        |
| vacant resource    |        |        |        |        |        |
| elements in the    |        |        |        |        |        |
| resource block to  |        |        |        |        |        |
| which the last     |        |        |        |        |        |
| coded symbol of    |        |        |        |        |        |
| the 2^nd^-stage    |        |        |        |        |        |
| SCI belongs.       |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+

Table A.7.4-2: Fixed reference channel for V2X receiver requirements
(SCS 30 kHz, 256QAM)

+--------------------+--------+--------+--------+--------+--------+
| Parameter          | Unit   | Value  |        |        |        |
+====================+========+========+========+========+========+
| Channel bandwidth  | MHz    | 10     | 20     | 30     | 40     |
+--------------------+--------+--------+--------+--------+--------+
| Subcarrier spacing | kHz    | 30     | 30     | 30     | 30     |
+--------------------+--------+--------+--------+--------+--------+
| Subchannel size    |        | 12     | 10     | 15     | 15     |
+--------------------+--------+--------+--------+--------+--------+
| Allocated resource |        | 24     | 50     | 75     | 105    |
| blocks             |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| MCS Index          |        | 23     | 23     | 23     | 23     |
+--------------------+--------+--------+--------+--------+--------+
| MCS Table for TBS  | 256QAM |        |        |        |        |
| determination      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Modulation         |        | 256QAM | 256QAM | 256QAM | 256QAM |
+--------------------+--------+--------+--------+--------+--------+
| Transport Block    |        | 15880  | 36896  | 58384  | 81976  |
| Size               |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Transport block    | Bits   | 24     | 24     | 24     | 24     |
| CRC                |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| LDPC base graph    |        | 1      | 1      | 1      | 1      |
+--------------------+--------+--------+--------+--------+--------+
| Number of Code     |        | 2      | 5      | 7      | 10     |
| Blocks per Slot    |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Beta offset for    |        | 6.25   | 6.25   | 6.25   | 6.25   |
| 2nd stage SCI      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| $\gamma$ value     |        | 3      | 3      | 3      | 3      |
| when 2nd stage SCI |        |        |        |        |        |
| rate match         |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Binary Channel     |        | 20544  | 48000  | 74400  | 106080 |
| Bits per Slot      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Max. Throughput    | Mbps   | 3.176  | 7.3792 | 11.677 | 16.395 |
| averaged over      |        |        |        |        |        |
| 100ms              |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| NOTE 1: If more    |        |        |        |        |        |
| than one Code      |        |        |        |        |        |
| Block is present,  |        |        |        |        |        |
| an additional CRC  |        |        |        |        |        |
| sequence of L = 24 |        |        |        |        |        |
| Bits is attached   |        |        |        |        |        |
| to each Code Block |        |        |        |        |        |
| (otherwise L = 0   |        |        |        |        |        |
| Bit).              |        |        |        |        |        |
|                    |        |        |        |        |        |
| NOTE 2: $\gamma$   |        |        |        |        |        |
| is the number of   |        |        |        |        |        |
| vacant resource    |        |        |        |        |        |
| elements in the    |        |        |        |        |        |
| resource block to  |        |        |        |        |        |
| which the last     |        |        |        |        |        |
| coded symbol of    |        |        |        |        |        |
| the 2^nd^-stage    |        |        |        |        |        |
| SCI belongs.       |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+

Table A.7.4-3: Fixed reference channel for V2X receiver requirements
(SCS 60kHz, 256QAM)

+--------------------+--------+--------+--------+--------+--------+
| Parameter          | Unit   | Value  |        |        |        |
+====================+========+========+========+========+========+
| Channel bandwidth  | MHz    | 10     | 20     | 30     | 40     |
+--------------------+--------+--------+--------+--------+--------+
| Subcarrier spacing | kHz    | 60     | 60     | 60     | 60     |
+--------------------+--------+--------+--------+--------+--------+
| Subchannel size    |        | 10     | 12     | 12     | 10     |
+--------------------+--------+--------+--------+--------+--------+
| Allocated resource |        | 10     | 24     | 36     | 50     |
| blocks             |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| MCS Index          |        | 23     | 23     | 23     | 23     |
+--------------------+--------+--------+--------+--------+--------+
| MCS Table for TBS  | 256QAM |        |        |        |        |
| determination      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Modulation         |        | 256QAM | 256QAM | 256QAM | 256QAM |
+--------------------+--------+--------+--------+--------+--------+
| Transport Block    |        | 4480   | 15880  | 25608  | 36896  |
| Size               |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Transport block    | Bits   | 24     | 24     | 24     | 24     |
| CRC                |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| LDPC base graph    |        | 1      | 1      | 1      | 1      |
+--------------------+--------+--------+--------+--------+--------+
| Number of Code     |        | 1      | 2      | 4      | 5      |
| Blocks per Slot    |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Beta offset for    |        | 6.25   | 6.25   | 6.25   | 6.25   |
| 2nd stage SCI      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| $\gamma$ value     |        | 3      | 3      | 3      | 3      |
| when 2nd stage SCI |        |        |        |        |        |
| rate match         |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Binary Channel     |        | 5760   | 20544  | 33216  | 48000  |
| Bits per Slot      |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| Max. Throughput    | Mbps   | 1.792  | 6.352  | 10.243 | 14.758 |
| averaged over      |        |        |        |        |        |
| 100ms              |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+
| NOTE 1: If more    |        |        |        |        |        |
| than one Code      |        |        |        |        |        |
| Block is present,  |        |        |        |        |        |
| an additional CRC  |        |        |        |        |        |
| sequence of L = 24 |        |        |        |        |        |
| Bits is attached   |        |        |        |        |        |
| to each Code Block |        |        |        |        |        |
| (otherwise L = 0   |        |        |        |        |        |
| Bit).              |        |        |        |        |        |
|                    |        |        |        |        |        |
| NOTE 2: $\gamma$   |        |        |        |        |        |
| is the number of   |        |        |        |        |        |
| vacant resource    |        |        |        |        |        |
| elements in the    |        |        |        |        |        |
| resource block to  |        |        |        |        |        |
| which the last     |        |        |        |        |        |
| coded symbol of    |        |        |        |        |        |
| the 2^nd^-stage    |        |        |        |        |        |
| SCI belongs.       |        |        |        |        |        |
+--------------------+--------+--------+--------+--------+--------+

######## Annex B (informative): Void

######## Annex C (informative): Downlink physical channels

C.1 General
===========

The following clauses, describes the downlink Physical Channels that are
transmitted during a connection i.e., when measurements are done.

C.2 Setup
=========

Table C.2-1 describes the downlink Physical Channels that are required
for connection set up.

Table C.2-1: Downlink Physical Channels required\
for connection set-up

  Physical Channel
  ------------------
  PBCH
  SSS
  PSS
  PDCCH
  PDSCH
  PBCH DMRS
  PDCCH DMRS
  PDSCH DMRS
  CSI-RS

C.3 Connection
==============

C.3.1 Measurement of Receiver Characteristics
---------------------------------------------

Unless otherwise stated, Table C.3.1-1 is applicable for measurements on
the Receiver Characteristics (clause 7).

Table C.3.1-1: Downlink Physical Channels transmitted during a
connection (FDD and TDD)

+---------------------------------------------+------+---------------+
| Parameter                                   | Unit | Value         |
+=============================================+======+===============+
| SSS transmit power                          | W    | Test specific |
+---------------------------------------------+------+---------------+
| EPRE ratio of PSS to SSS                    | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PBCH to SSS                   | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PBCH to PBCH DMRS             | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PDCCH to SSS                  | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PDCCH to PDCCH DMRS           | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PDSCH to SSS                  | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PDSCH to PDSCH DMRS (Note 1)  | dB   | -3            |
+---------------------------------------------+------+---------------+
| EPRE ratio of CSI-RS to SSS                 | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of PTRS to PDSCH                 | dB   | Test specific |
+---------------------------------------------+------+---------------+
| EPRE ratio of OCNG DMRS to SSS              | dB   | 0             |
+---------------------------------------------+------+---------------+
| EPRE ratio of OCNG to OCNG DMRS (Note 1)    | dB   | 0             |
+---------------------------------------------+------+---------------+
| NOTE 1: No boosting is applied to any of    |      |               |
| the channels except PDSCH DMRS. For PDSCH   |      |               |
| DMRS, 3 dB power boosting is applied        |      |               |
| assuming DMRS Type 1 configuration when     |      |               |
| DMRS and PDSCH are TDM\'ed and only half of |      |               |
| the DMRS REs are occupied.                  |      |               |
|                                             |      |               |
| NOTE 2: Number of DMRS CDM groups without   |      |               |
| data for PDSCH DMRS configuration for OCNG  |      |               |
| is set to 1.                                |      |               |
+---------------------------------------------+------+---------------+

######## Annex D (normative): Characteristics of the interfering signal

D.1 General
===========

Some RF performance requirements for the NR UE receiver are defined with
interfering signals present in addition to the wanted signal.

For NR bands with F~DL\_high~ \< 2700 MHz and F~UL\_high~ \< 2700 MHz, a
modulated 5 MHz full bandwidth NR down link signal, and in some cases an
additional CW signal, are used as interfering signal. For intra-band
contiguous CA bandwidth class B and C, a modulated 5 MHz NR downlink
signal is used. And for some cases an additional CW signal is used.

For NR bands with F~DL\_low~ ≥ 3300 MHz and F~UL\_low~ ≥ 3300 MHz, a
modulated NR downlink signal which equals to channel bandwidth of the
wanted signal for single carrier and inter-band CA cases is used as
interfering signal. For intra-band contiguous CA bandwidth Class C, a
modulated NR downlink signal which equals to the aggregated channel
bandwidth of the wanted signal is used. For intra-band contiguous CA
bandwidth class D and E cases, a modulated 50 MHz NR downlink signal is
used. And for some cases an additional CW signal is used.

D.2 Interference signals
========================

Table D.2-1 and Table D.2-4 describes the modulated interferer for
different channel bandwidth options for NR band lower than 2700MHz.

Table D.2-1: Description of modulated NR interferer for NR bands with
F~DL\_high~ \< 2700 MHz and F~UL\_high~ \< 2700 MHz

                                                                                                                                             **Channel bandwidth**                                       
  ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------- -------- -------- -------- -------- ---------
                                                                                                                                             5 MHz                   10MHz    15 MHz   20 MHz   25 MHz   30 MHz
  RB                                                                                                                                         NOTE 1                                                      
  BW~Interferer~                                                                                                                             5 MHz                                                       
                                                                                                                                             Channel bandwidth                                           
                                                                                                                                             40 MHz                  50 MHz   60 MHz   80 MHz   90 MHz   100 MHz
  RB                                                                                                                                         NOTE 1                                                      
  BW~Interferer~                                                                                                                             5 MHz                                                       
  NOTE 1: The RB configured for interfering signal is the same as maximum RB number defined in Table 5.3.2-1 for each sub-carrier spacing.                                                               

Table D.2-2 and Table D.2-3 describe the modulated interferer for
different channel bandwidth options for NR band higher than 3300MHz.

Table D.2-2: Description of modulated NR interferer for NR bands with
F~DL\_low~ ≥ 3300 MHz and F~UL\_low~ ≥ 3300 MHz

                                                                                                                                             **Channel bandwidth**                                                                  
  ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------- -------- -------- -------- -------- -------- -------- -------- ---------
                                                                                                                                             10 MHz                  15 MHz   20 MHz   40 MHz   50 MHz   60 MHz   80 MHz   90 MHz   100 MHz
  RB                                                                                                                                         NOTE 1                                                                                 
  BW~Interferer~                                                                                                                             10 MHz                  15 MHz   20 MHz   40 MHz   50 MHz   60 MHz   80 MHz   90 MHz   100 MHz
  NOTE 1: The RB configured for interfering signal is the same as maximum RB number defined in Table 5.3.2-1 for each sub-carrier spacing.                                                                                          

Table D.2-3: Description of modulated NR interferer for NR bands with
F~DL\_low~≥ 3300 MHz and F~UL\_low~≥ 3300 MHz for Intra-band contiguous
CA

                                                                                                                                                                                                                                     Aggregated Channel bandwidth of Bandwdith Class C   Bandwidth Class D/E                                                                   
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------- --------------------- --------- --------- --------- --------- --------- ------------- -------
                                                                                                                                                                                                                                     110 MHz                                             120 MHz               130 MHz   140 MHz   150 MHz   160 MHz   180 MHz   200 MHz       
  RB(SCS=30 kHz)                                                                                                                                                                                                                     NOTE 1                                              133                                                                                   
  RB(SCS=60 kHz)                                                                                                                                                                                                                     NOTE 1                                              65                                                                                    
  BW~Interferer~                                                                                                                                                                                                                     110 MHz                                             120 MHz               130 MHz   140 MHz   150 MHz   160 MHz   180 MHz   **200 MHz**   50MHz
  NOTE 1: The interfering signal shall be configured in the same way as the aggregated bandwidth of the wanted signal. The RB configurations for each component carrier are defined in Table 5.3.2-1 for each sub-carrier spacing.                                                                                                                                             

Table D.2-4: Description of modulated NR interferer for NR bands with
F~DL\_low~ \< 2700 MHz and F~UL\_low~ \< 2700 MHz for Intra-band
contiguous CA

                                                                                                                                             Bandwidth Class B   Bandwidth Class C
  ------------------------------------------------------------------------------------------------------------------------------------------ ------------------- -------------------
  RB                                                                                                                                         NOTE 1              NOTE 1
  BW~Interferer~                                                                                                                             5 MHz               5 MHz
  NOTE 1: The RB configured for interfering signal is the same as maximum RB number defined in Table 5.3.2-1 for each sub-carrier spacing.                       

######## Annex E (normative): Environmental conditions

E.1 General
===========

This normative annex specifies the environmental requirements of the UE.
Within these limits the requirements of the present documents shall be
fulfilled.

E.2 Environmental
=================

The requirements in this clause apply to all types of UE(s).

E.2.1 Temperature
-----------------

The UE shall fulfil all the requirements in the full temperature range
of:

Table E.2.1-1: Temperature conditions

  ---------------- -----------------------------------------------------------------
  +15°C to +35°C   For normal conditions (with relative humidity up to 75 %)
  -10°C to +55°C   For extreme conditions (see IEC publications 68‑2‑1 and 68‑2‑2)
  ---------------- -----------------------------------------------------------------

Outside this temperature range the UE, if powered on, shall not make
ineffective use of the radio frequency spectrum. In no case shall the UE
exceed the transmitted levels as defined in clause 6.2 for extreme
operation.

E.2.2 Voltage
-------------

The UE shall fulfil all the requirements in the full voltage range, i.e.
the voltage range between the extreme voltages.

The manufacturer shall declare the lower and higher extreme voltages and
the approximate shutdown voltage. For the equipment that can be operated
from one or more of the power sources listed below, the lower extreme
voltage shall not be higher, and the higher extreme voltage shall not be
lower than that specified below.

Table E.2.2-1: Voltage conditions

+----------------+----------------+----------------+----------------+
| Power source   | Lower extreme  | Higher extreme | Normal         |
|                |                |                | conditions     |
|                | voltage        | voltage        |                |
|                |                |                | voltage        |
+----------------+----------------+----------------+----------------+
| AC mains       | 0,9 \* nominal | 1,1 \* nominal | nominal        |
+----------------+----------------+----------------+----------------+
| Regulated lead | 0,9 \* nominal | 1,3 \* nominal | 1,1 \* nominal |
| acid battery   |                |                |                |
+----------------+----------------+----------------+----------------+
| Non regulated  | 0,85 \*        | Nominal        | Nominal        |
| batteries:     | nominal        |                |                |
|                |                | 1,1 \* Nominal | 1,1 \* Nominal |
| Leclanché      | 0,95 \*        |                |                |
|                | nominal        |                | Nominal        |
| Lithium        |                |                |                |
|                | 0,90 \*        |                |                |
| Mercury/nickel | nominal        |                |                |
| & cadmium      |                |                |                |
+----------------+----------------+----------------+----------------+

Outside this voltage range the UE if powered on, shall not make
ineffective use of the radio frequency spectrum. In no case shall the UE
exceed the transmitted levels as defined in clause 6.2 for extreme
operation. In particular, the UE shall inhibit all RF transmissions when
the power supply voltage is below the manufacturer declared shutdown
voltage.

E.2.3 Vibration
---------------

The UE shall fulfil all the requirements when vibrated at the following
frequency/amplitudes.

Table E.2.3-1: Vibration conditions

  ----------------- ------------------------------------------------------
  Frequency         ASD (Acceleration Spectral Density) random vibration
  5 Hz to 20 Hz     0.96 m2/s3
  20 Hz to 500 Hz   0.96 m2/s3 at 20 Hz, thereafter --3 dB/Octave
  ----------------- ------------------------------------------------------

Outside the specified frequency range the UE, if powered on, shall not
make ineffective use of the radio frequency spectrum. In no case shall
the UE exceed the transmitted levels as defined in TS 38.101-1 for
extreme operation.

######## Annex F (normative): Transmit modulation

F.0 General
===========

While measuring the transmit modulation quality of carriers, an
existence of the carrier leakage needs to be taken into account
indicated by the parameter *txDirectCurrentLocation* in
*UplinkTxDirectCurrent* IE.

F.1 Measurement Point
=====================

Figure F.1-1 shows the measurement point for the unwanted emission
falling into non-allocated RB(s) and the EVM for the allocated RB(s).

![](media/image3.png){width="6.267361111111111in"
height="1.7666666666666666in"}

Figure F.1-1: EVM measurement points

F.2 Basic Error Vector Magnitude measurement
============================================

The EVM is the difference between the ideal waveform and the measured
waveform for the allocated RB(s)

,

where

is a set of modulation symbols with the considered modulation scheme
being active within the measurement period,

are the samples of the signal evaluated for the EVM,

is the ideal signal reconstructed by the measurement equipment, and

is the average power of the ideal signal. For normalized modulation
symbols is equal to 1.

The basic EVM measurement interval is defined over one slot in the time
domain for PUCCH and PUSCH and over one preamble sequence for the PRACH.

F.3 Basic in-band emissions measurement
=======================================

The in-band emissions are a measure of the interference falling into the
non-allocated resources blocks. The in-band emission requirement is
evaluated for PUCCH and PUSCH transmissions. The in-band emission
requirement is not evaluated for PRACH transmissions.

The in-band emissions are measured as follows

,

where

is a set of OFDM symbols with the considered modulation scheme being
active within the measurement period,

is the starting frequency offset between the allocated RB and the
measured non-allocated RB (e.g. or for the first adjacent RB),

(resp. ) is the lower (resp. upper) edge of the UL UE channel bandwidth,

and are the lower and upper edge of the allocated BW, and

is the frequency domain signal evaluated for in-band emissions as
defined in the clause (ii)

The relative in-band emissions are, given by

where

is the number of allocated RBs

The basic in-band emissions measurement interval is defined over one
slot in the time domain. When the PUSCH or PUCCH transmission slot is
shortened due to multiplexing with SRS, the in-band emissions
measurement interval is reduced by one OFDM symbol, accordingly.

In the evaluation of in-band emissions, the timing is set according to ,
where sample time offsets and are defined in clause F.4.

F.4 Modified signal under test
==============================

Implicit in the definition of EVM is an assumption that the receiver is
able to compensate a number of transmitter impairments.

The DFT-s-OFDM modulated signals or PRACH signal under test is modified
and, in the case of DFT-s-OFDM modulated signals, decoded according to:

where

is the time domain samples of the signal under test.

The CP-OFDM modulated signals or PUSCH demodulation reference signal or
PUCCH data signal under test is equalised and, in the case of CP-OFDM
modulated signals decoded according to:

where

is the time domain samples of the signal under test.

To minimize the error, the signal under test should be modified with
respect to a set of parameters following the procedure explained below.

Notation:

is the sample timing difference between the FFT processing window in
relation to nominal timing of the ideal signal.

is the RF frequency offset.

is the phase response of the TX chain.

is the amplitude response of the TX chain.

In the following represents the middle sample of the EVM window of
length (defined in the next clauses) or the last sample of the first
window half if is even.

The EVM analyser shall

\- detect the start of each slot and estimate and ,

\- determine so that the EVM window of length is centred

\- on the time interval determined by the measured cyclic prefix minus
16κ samples of the considered OFDM symbol for symbol l for subcarrier
spacing configuration µ in a subframe, with l = 0 or l = 7\*2\^µ for
normal CP, i.e. the first 16κ samples of the CP should not be taken into
account for this step. In the determination of the number of excluded
samples, a sampling rate of 1/T~c~ is assumed. If a different sampling
rate is used, the number of excluded samples is scaled linearly.

\- on the measured cyclic prefix of the considered OFDM symbol symbol
for all other symbols for normal CP and for symbol 0 to 11 for extended
CP.

\- on the measured preamble cyclic prefix for the PRACH

To determine the other parameters a sample timing offset equal to is
corrected from the signal under test. The EVM analyser shall then

\- correct the RF frequency offset for each time slot, and

\- apply an FFT of appropriate size. The chosen FFT size shall ensure
that in the case of an ideal signal under test, there is no measured
inter-subcarrier interference.

The carrier leakage shall be removed from the evaluated signal before
calculating the EVM and the in-band emissions; however, the removed
relative carrier leakage power also has to satisfy the applicable
requirement.

At this stage the allocated RBs shall be separated from the
non-allocated RBs. In the case of PUCCH and PUSCH EVM, the signal on the
non-allocated RB(s), , is used to evaluate the in-band emissions.

Moreover, the following procedure applies only to the signal on the
allocated RB(s).

\- In the case of PUCCH and PUSCH, the UL EVM analyzer shall estimate
the TX chain equalizer coefficients and used by the ZF equalizer for all
subcarriers by time averaging at each signal subcarrier of the amplitude
and phase of the reference and data symbols. The time-averaging length
is 1 slot. This process creates an average amplitude and phase for each
signal subcarrier used by the ZF equalizer. The knowledge of data
modulation symbols may be required in this step because the
determination of symbols by demodulation is not reliable before signal
equalization.

\- In the case of PRACH, the UL EVM analyzer shall estimate the TX chain
coefficients and used for phase and amplitude correction and are seleted
so as to minimize the resulting EVM. The TX chain coefficients are not
dependent on frequency, i.e. and . The TX chain coefficient are chosen
independently for each preamble transmission and for each .

At this stage estimates of , , and are available. is one of the
extremities of the window , i.e. can be or , where if is odd and if is
even. The EVM analyser shall then

\- calculate EVM~l~ with set to ,

\- calculate EVM~h~ with set to .

For the EVM calculation on the symbols with a transient period when the
UE signals a transient period capability (tp) of 2, 4 or 7usec,
$\Delta\widetilde{t}$ is is given below.

\- calculate EVM~l\_tp~ with $\Delta\widetilde{t}$ set
to$\left\lfloor \frac{tp + \text{tp}_{\text{start}}}{T_{c}} \right\rfloor + 1$,
where is 1/T~c~ the sampling rate

\- calculate EVM~h\_tp~ with $\Delta\widetilde{t}$ set
to$\left\lfloor \frac{CP + \text{tp}_{\text{start}}}{T_{c}} \right\rfloor - 1$,
where 1/T~c~ is the sampling rate and the CP is the cyclic prefix of the
symbol on which EVM is calculated (e.g. long CP for the first symbol of
the slot) in seconds

A pictorial representation of the EVM measurement windows is given in
Figure F.4-1.

Figure F.4-1: EVM measurement window

F.5 Window length
=================

F.5.1 Timing offset
-------------------

As a result of using a cyclic prefix, there is a range of, which, at
least in the case of perfect Tx signal quality, would give close to
minimum error vector magnitude. As a first order approximation, that
range should be equal to the length of the cyclic prefix. Any time
domain windowing or FIR pulse shaping applied by the transmitter reduces
the range within which the error vector is close to its minimum.

F.5.2 Window length
-------------------

The window length *W* affects the measured EVM and is expressed as a
function of the configured cyclic prefix length. In the case where
equalization is present, as with frequency domain EVM computation, the
effect of FIR is reduced. This is because the equalization can correct
most of the linear distortion introduced by the FIR. However, the time
domain windowing effect can\'t be removed.

F.5.3 Window length for normal CP
---------------------------------

Table F.5.3-1, F.5.3-2, F.5.3-3 below specify the EVM window length
(*W*) for normal CP.

Table F.5.3-1: EVM window length for normal CP for NR, FR1, 15 kHz SCS

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Channel\                                                                                                                                                          FFT size   Cyclic prefix length for symbols 1‑6 and 8-13 in FFT samples   EVM window length *W*   Ratio of *W* to total CP length for symbols 1‑6 and 8-13^1^ (%)
  Bandwidth (MHz)                                                                                                                                                                                                                                                     
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- -------------------------------------------------------------- ----------------------- -----------------------------------------------------------------
  5                                                                                                                                                                 512        36                                                             18                      50

  10                                                                                                                                                                1024       72                                                             36                      50

  15                                                                                                                                                                1536       108                                                            54                      50

  20                                                                                                                                                                2048       144                                                            72                      50

  25                                                                                                                                                                2048       144                                                            72                      50

  30                                                                                                                                                                3072       216                                                            108                     50

  40                                                                                                                                                                4096       288                                                            144                     50

  50                                                                                                                                                                4096       288                                                            144                     50

  NOTE 1: These percentages are informative and apply to a slot\'s symbols 1 to 6 and 8 to 13. Symbols 0 and 7 have a longer CP and therefore a lower percentage.                                                                                                     
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Table F.5.3-2: EVM window length for normal CP for NR, FR1, 30 kHz SCS

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Channel\                                                                                                                                            FFT size   Cyclic prefix length for symbols 1‑13 in FFT samples   EVM window length *W*   Ratio of *W* to total CP length for symbols 1‑13^1^ (%)
  Bandwidth (MHz)                                                                                                                                                                                                                               
  --------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ------------------------------------------------------ ----------------------- ---------------------------------------------------------
  5                                                                                                                                                   256        18                                                     9                       50

  10                                                                                                                                                  512        36                                                     18                      50

  15                                                                                                                                                  768        54                                                     27                      50

  20                                                                                                                                                  1024       72                                                     36                      50

  25                                                                                                                                                  1024       72                                                     36                      50

  30                                                                                                                                                  1536       108                                                    54                      50

  40                                                                                                                                                  2048       144                                                    72                      50

  50                                                                                                                                                  2048       144                                                    72                      50

  60                                                                                                                                                  3072       216                                                    108                     50

  70                                                                                                                                                  3072       216                                                    108                     50

  80                                                                                                                                                  4096       288                                                    144                     50

  90                                                                                                                                                  4096       288                                                    144                     50

  100                                                                                                                                                 4096       288                                                    144                     50

  NOTE 1: These percentages are informative and apply to a slot\'s symbols 1 through 13. Symbol 0 has a longer CP and therefore a lower percentage.                                                                                             
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Table F.5.3-3: EVM window length for normal CP for NR (60 kHz SCS)

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Channel\                                                                                                                                                                                                                 FFT size   Cyclic prefix length for symbols in FFT samples   EVM window length *W*   Ratio of *W* to total CP length ^1^ (%)
  Bandwidth (MHz)                                                                                                                                                                                                                                                                                               
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- ------------------------------------------------- ----------------------- -----------------------------------------
  10                                                                                                                                                                                                                       256        18                                                9                       50

  15                                                                                                                                                                                                                       384        27                                                14                      50

  20                                                                                                                                                                                                                       512        36                                                18                      50

  25                                                                                                                                                                                                                       512        36                                                18                      50

  30                                                                                                                                                                                                                       768        54                                                27                      50

  40                                                                                                                                                                                                                       1024       72                                                36                      50

  50                                                                                                                                                                                                                       1024       72                                                36                      50

  60                                                                                                                                                                                                                       1536       108                                               54                      50

  70                                                                                                                                                                                                                       1536       108                                               54                      50

  80                                                                                                                                                                                                                       2048       144                                               72                      50

  90                                                                                                                                                                                                                       2048       144                                               72                      50

  100                                                                                                                                                                                                                      2048       144                                               72                      50

  NOTE 1: These percentages are informative and apply to all OFDM symbols within subframe except for symbol 0 of slot 0 and slot 2. Symbol 0 of slot 0 and slot 2 may have a longer CP and therefore a lower percentage.                                                                                        
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

F.5.4 Window length for Extended CP
-----------------------------------

Table F.5.4-1 below specifies the EVM window length (*W*) for extended
CP. The number of CP samples excluded from the EVM window is the same as
for normal CP length.

Table F.5.4-1: EVM window length for extended CP for NR, FR1, 60 kHz SCS

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Channel\                                     FFT size   Cyclic prefix length in FFT samples   EVM window length *W*   Ratio of *W* to total CP length^1^ (%)
  Bandwidth (MHz)                                                                                                       
  -------------------------------------------- ---------- ------------------------------------- ----------------------- ----------------------------------------
  10                                           256        64                                    54                      84.4

  15                                           384        96                                    80                      83.3

  20                                           512        128                                   106                     82.8

  25                                           512        128                                   110                     85.9

  30                                           768        192                                   164                     85.4

  40                                           1024       256                                   220                     85.9

  50                                           1024       256                                   220                     85.9

  60                                           1536       384                                   330                     85.9

  70                                           1536       384                                   330                     85.9

  80                                           2048       512                                   440                     85.9

  90                                           2048       512                                   440                     85.9

  100                                          2048       512                                   440                     85.9

  NOTE 1: These percentages are informative.                                                                            
  --------------------------------------------------------------------------------------------------------------------------------------------------------------

F.5.5 Window length for PRACH
-----------------------------

The table below specifies the EVM window length for PRACH preamble
formats for *L~RA~*= 839 and .

Table F.5.5-1 EVM window length for PRACH formats for *L~RA~*= 839

+-------------+-------------+-------------+-------------+-------------+
| Preamble    | Cyclic      | Nominal FFT | EVM window  | Ratio of    |
| format      | prefix      | size^1^     | length *W*  | *W* to      |
|             | length      |             | in FFT      | CP^2^       |
|             | *N~CP~*     |             | samples     |             |
+=============+=============+=============+=============+=============+
| 0           | 3168        | 24576       | 2307        | 72.8%       |
+-------------+-------------+-------------+-------------+-------------+
| 1           | 21024       | 24576       | 20163       | 95.9%       |
+-------------+-------------+-------------+-------------+-------------+
| 2           | 4688        | 24576       | 3827        | 81.6%       |
+-------------+-------------+-------------+-------------+-------------+
| 3           | 3168        | 6144        | 2952        | 93.2%       |
+-------------+-------------+-------------+-------------+-------------+
| NOTE 1: The |             |             |             |             |
| use of      |             |             |             |             |
| other FFT   |             |             |             |             |
| sizes is    |             |             |             |             |
| possible as |             |             |             |             |
| long as     |             |             |             |             |
| appropriate |             |             |             |             |
| scaling of  |             |             |             |             |
| the window  |             |             |             |             |
| length is   |             |             |             |             |
| applied     |             |             |             |             |
|             |             |             |             |             |
| NOTE 2:     |             |             |             |             |
| These       |             |             |             |             |
| percentages |             |             |             |             |
| are         |             |             |             |             |
| informative |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

The table below specifies the EVM window length for PRACH preamble
formats for *L~RA~*= 139 and where.

Table F.5.5-2 EVM window length for PRACH formats for *L~RA~*= 139

+-------------+-------------+-------------+-------------+-------------+
| Preamble    | Cyclic      | Nominal FFT | EVM window  | Ratio of    |
| format      | prefix      | size^1^     | length *W*  | *W* to      |
|             | length      |             | in FFT      | CP^2^       |
|             | *N~CP~*     |             | samples     |             |
+=============+=============+=============+=============+=============+
| A1          | 2882*^-^*   | 20482*^-^*  | 1442*^-^*   | 50.0%       |
+-------------+-------------+-------------+-------------+-------------+
| A2          | 5762*^-^*   | 20482*^-^*  | 4322*^-^*   | 75.0%       |
+-------------+-------------+-------------+-------------+-------------+
| A3          | 8642*^-^*   | 20482*^-^*  | 7202*^-^*   | 83.3%       |
+-------------+-------------+-------------+-------------+-------------+
| B1          | 2162*^-^*   | 20482*^-^*  | 722*^-^*    | 33.3%       |
+-------------+-------------+-------------+-------------+-------------+
| B2          | 3602*^-^*   | 20482*^-^*  | 2162*^-^*   | 60.0%       |
+-------------+-------------+-------------+-------------+-------------+
| B3          | 5042*^-^*   | 20482*^-^*  | 3602*^-^*   | 71.4%       |
+-------------+-------------+-------------+-------------+-------------+
| B4          | 9362*^-^*   | 20482*^-^*  | 7922*^-^*   | 84.6%       |
+-------------+-------------+-------------+-------------+-------------+
| C0          | 12402*^-^*  | 20482*^-^*  | 10962*^-^*  | 88.4%       |
+-------------+-------------+-------------+-------------+-------------+
| C2          | 20482*^-^*  | 20482*^-^*  | 19042*^-^*  | 93.0%       |
+-------------+-------------+-------------+-------------+-------------+
| NOTE 1: The |             |             |             |             |
| use of      |             |             |             |             |
| other FFT   |             |             |             |             |
| sizes is    |             |             |             |             |
| possible as |             |             |             |             |
| long as     |             |             |             |             |
| appropriate |             |             |             |             |
| scaling of  |             |             |             |             |
| the window  |             |             |             |             |
| length is   |             |             |             |             |
| applied     |             |             |             |             |
|             |             |             |             |             |
| NOTE 2:     |             |             |             |             |
| These       |             |             |             |             |
| percentages |             |             |             |             |
| are         |             |             |             |             |
| informative |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

F.6 Averaged EVM
================

The general EVM is averaged over basic EVM measurements for n slots in
the time domain.

,

where n is

$$n = \left\{ \begin{matrix}
10,\ for\ 15\ kHz\ SCS \\
20,\ for\ 30\ kHz\ SCS \\
40,\ for\ 60\ kHz\ SCS \\
\end{matrix} \right.\ $$

for PUCCH, PUSCH.

The EVM requirements shall be tested against the maximum of the RMS
average at the window W extremities of the EVM measurements:

Thus is calculated using in the expressions above and is calculated
using .

Thus we get:

*The calculation of the EVM for the demodulation reference signal,* ,
follows the same procedure as calculating the general EVM, with the
exception that the modulation symbol set defined in clause F.2 is
restricted to symbols containing uplink demodulation reference signals.

The basic measurements are first averaged over n slots in the time
domain to obtain an intermediate average .

$${\overline{\text{EVM}}}_{\text{DMRS}} = \sqrt{\frac{1}{n}\sum_{i = 1}^{n}\text{EVM}_{DMRS,i}^{2}}$$

In the determination of each ![](media/image60.wmf){width="0.75in"
height="0.2604166666666667in"}, the timing is set to if , and it is set
to otherwise, where and are the general average EVM values calculated in
the same n slots over which the intermediate average is calculated. Note
that in some cases, the general average EVM may be calculated only for
the purpose of timing selection for the *demodulation reference signal
EVM*.

Then the results are further averaged to get the *EVM for the
demodulation reference signal,* ,

The PRACH EVM, , is averaged over 2 preamble sequence measurements for
long preamble formats as defined in table 6.3.3.1-1 in \[6\] and
averaged over 10 preamble sequence measurements for short preamble
formats as defined in table 6.3.3.1-2 in \[6\].

The EVM requirements shall be tested against the maximum of the RMS
average at the window *W* extremities of the EVM measurements:

Thus is calculated using and is calculated using .

Thus we get:

F.7 Spectrum Flatness
=====================

The data shall be taken from FFT coded data symbols and the demodulation
reference symbols of the allocated resource block.

F.8
===

F.9
===

F.10 EVM for UL MIMO
====================

F10.1 General
-------------

EVM for UL MIMO is measured per layer. A zero-forcing (ZF) MIMO receiver
architecture is used so that dual layer transmissions by the UE can be
demodulated by the test equipment receiver.

![X:\\PROJECT\\CMW\\DEVELOP\\USER\\1CM5\\KRAKOWSK\\NR\\NR\_EVM\_2L\_UL\_MIMO.png](media/image67.png){width="6.5375in"
height="3.248611111111111in"}

Figure F.10.1-1: EVM calculation block diagram for 2-Layer UL MIMO

The TE receives signals from 2 different ports which are connected to
two antenna connectors in the test system.

For UL MIMO measurements a MIMO equalization step as described in
section F.10.2 is performed to separate the layers.

Each layer is then processed as described in section F.10.3 to receive
the measurement results for each individual layer.

F10.2 MIMO Equalization
-----------------------

The MIMO equalization is based only on reference signals (DMRS) without
using any data symbols. For the equalization process all available DMRS
symbols shall be used.

The effective 2x2 channel matrix is estimated using reference signals of
different subcarriers, e.g. in case of DMRS antenna ports 0 and 2. In
case that same subcarriers are used, e.g. DMRS antenna ports 0 and 1, a
channel decomposition is necessary taking advantage of the orthogonal
codes *w~f~* and *w~t~* and assuming identical channel coefficients for
adjacent subcarriers of same CDM group.

Effective channel including the precoding matrix *P* is:

$$\widetilde{H} = \text{HP} = \ \begin{bmatrix}
{\widetilde{h}}_{0,0} & {\widetilde{h}}_{0,1} \\
{\widetilde{h}}_{1,0} & {\widetilde{h}}_{1,1} \\
\end{bmatrix}$$

with

$${\widetilde{h}}_{n,\nu} = \frac{y_{n}r_{\nu}^{*}}{{|r_{\nu}|}^{2}}$$

where *y* denotes the received symbol on port index *n* and *r* the
reference signal for layer index *ν*.

Since reference signals of a specific layer are transmitted only on
subcarriers of one CDM group channel, interpolation is needed in order
to obtain channel coefficients for all subcarriers. Channel
interpolation is done using the channel coefficients of active CDM group
in all other CDM groups.

The channel coefficients used to calculate the equalizer coefficients
are obtained after channel smoothing in frequency domain by computing
the moving average of interpolated channel coefficients. The moving
average window size is 7. For subcarriers at or near the edge of
allocation the window size is reduced accordingly.

The ZF equalizer coefficients are calculated as the inverse of the
effective channel matrix, in general:

$$G_{\text{ZF}} = {\widetilde{H}}^{- 1}$$

F10.3 Layer processing
----------------------

After performing the MIMO equalization as described in section F.10.2
each layer is processed using the existing procedure as defined in Annex
E of TS 38.521-1 \[4\].

Since the channel estimation is calculated only on the DMRS symbols, an
averaging including all 14 symbols of one slot, i.e. data and reference
signals, is needed in order to minimize EVM. The averaging is achieved
by the least square (LS) equalization method described for single layer
in Annex E.3. of TS 38.521-1 \[4\].

*MS(f,t)* and *NS(f,t)* are processed with a LS estimator, to derive one
equalizer coefficient per time slot and per allocated subcarrier.
*EC(f)* is defined for each layer as:

$$\text{EC}_{\nu}(f) = \frac{\sum_{t = 0}^{13}{\text{NS}_{\nu}(f,t)^{*}\text{NS}_{\nu}(f,t)}}{\sum_{t = 0}^{13}{MS_{\nu}(f,t)^{*}\text{NS}_{\nu}(f,t)}}$$

With \* denoting complex conjugation. *EC(f)* are used to equalize layer
data symbols.

EVM equalizer spectral flatness is derived from equalizer coefficients
for each layer as follows:

$$c_{\nu} = \left| \text{EC}_{\nu}(f) \right|\ \sqrt{\left| g_{\nu,0} \right|^{2} + \left| g_{\nu,1} \right|^{2}}$$

######## Annex G (normative):

Difference of relative phase and power errors

G.0 General
===========

This annex gives further information needed for understanding and
implementing 6.4D.4. The following terms should be understood as
follows:

Relative phase error: refers to the phase difference between signals at
different antenna connectors, which should be ideally 0. It should be
understood as for a slot i.e. (slot) relative phase. It is calculated
based on DMRS symbols of that slot or on SRS symbols.

Difference of relative phase error: refers to the difference between the
relative phase error determined per slot and the relative phase error
determined based on the SRS transmitted.

G.1 Measurement Point
=====================

Figure G.1-1 shows the measurement point for the difference of relative
phase and power errors.

Figure G.1-1 - Measurement point for difference of relative phase/power
error for UL coherent MIMO

G.2 Relative Phase Error Measurement
====================================

Here are listed the different aspects that may lead to different
interpretations.

G.2.1 Symbols and subcarriers used
----------------------------------

Phase error is determined based on DMRS REs (DMRS mapping type A with 3
DMRS symbols per slot, the REs corresponding to the odd subcarriers and
DMRS symbols are non-allocated for data or DMRS.) and SRS REs (with 4
SRS symbols in the SRS slot, same SRS resource mapping is used for
non-codebook-based and codebook-based precoding).

For the DMRS and SRS to occupy identical SCs and maximimize their
frequency density, DMRS configuration type 1 and SRS comb2 configuration
are used.

UL RMC described in Annex A.2 is used.

G.2.2 CFO (carrier frequency offset) correction
-----------------------------------------------

The TE performs a CFO correction on a slot-by-slot basis using a common
frequency correction at the two uplink antenna connectors.

G.2.3 Steps of the measurement method
-------------------------------------

Below are detailed the steps necessary to obtain the maximum difference
of relative phase error during the 20ms time window.

1 Determination for each subcarrier and at each antenna, the SRS
relative phase error based on the last SRS transmitted on Ant1 and Ant2,
that relative phase error serves as a reference for the calculation of
the difference of relative phase error for each slot inside the 20 ms
time window.

The output is the "SRS relative phase error" vector for the last SRS
transmitted:
$\left\lbrack 1 \times number\_ of\_ subcarriers \right\rbrack$.

2 Calculation for the last SRS transmitted, for each RB of the SRS
relative phase errors based on the arithmetic mean of the subcarrier SRS
relative phase errors determined in previous step.

The output is the "SRS relative phase error" vector for the last SRS
transmitted: $\left\lbrack 1 \times number\_ of\_ RBs \right\rbrack$.

3 CFO correction on slot-by-slot basis using a common frequency
correction for both antenna outputs. 4 Determination for each subcarrier
and at each antenna, the phase over the slot being analyzed. The phase
is extracted from the channel estimate derived from the 3 DMRS symbols
of the slot using the LSE technique.

The output is one vector of dimension
$\left\lbrack 1 \times number\_ of\_ subcarriers \right\rbrack$ for each
antenna.

5 Calculation for a slot for each subcarrier of the relative phase error
(difference between the vectors determined in the previous step).

The output is subcarrier relative phase errors of a slot:
$\left\lbrack 1 \times number\_ of\_ subcarriers \right\rbrack$.

6 Calculation for a slot, for each RB of the relative phase errors based
on the arithmetic mean of the subcarrier relative phase errors
determined in previous step.

The output is a "slot relative phase error" vector for a
slot:$\ \left\lbrack 1 \times number\_ of\_ RBs \right\rbrack$.

7 Calculation for a slot of the difference of relative phase errors
based on the "SRS relative phase error" (reference) determined in step 2
and the "slot relative phase error" determined in previous step.

The output is a "difference of relative phase error" vector for a
slot:$\ \left\lbrack 1 \times number\_ of\_ RBs \right\rbrack$.

8 Calculation for a slot of the arithmetic mean value of the "difference
of relative phase error" vector determined in previous step, this value
corresponds to an RB.

The output is a "difference of relative phase error" value for a slot:
$\left\lbrack 1 \times 1 \right\rbrack.$

9 Perform for each slot of the 20ms time window, steps 3 to 8.

The output is a "difference of relative phase error" vector:
$\left\lbrack 1 \times number\_ of\_ slots \right\rbrack$.

10 Calculation of the maximum value of the "difference of relative phase
error".

The output is the "difference of relative phase error" that should be
verified as complying with the 40° maximum allowable difference of
relative phase error requirement:
$\left\lbrack 1 \times 1 \right\rbrack$.

######## Annex H (informative): Void

######## Annex I (informative): Void

######## Annex J (informative): Void

######## Annex K (informative): Void

######## Annex L (normative): ModifiedMPR-Behavior

L.1 Indication of modified MPR behavior
=======================================

This annex contains the definitions of the bits in the field
*modifiedMPR-Behavior* indicated per supported NR band in the IE
*RF-Parameters* \[7\] by a UE supporting an MPR or A-MPR modified in a
given version of this specification. A modified MPR or A-MPR behaviour
can apply to a supported NR band in stand-alone operation (including CA
and NN-DC operation) or in non-standalone operation with the said NR
band as part of an EN-DC or NE-DC band combination.

NOTE 1: In the present release, the *modifiedMPR-Behavior* is indicated
\[7\] by an 8-bit bitmap per supported NR band.

Table L.1-1: Definitions of the bits in the field *modifiedMPR-Behavior*

+---------+------------------+------------------+------------------+
| NR Band | Index of field   | Definition       | Notes            |
|         |                  |                  |                  |
|         | (bit number)     | (description of  |                  |
|         |                  | the supported    |                  |
|         |                  | functionality if |                  |
|         |                  | indicator set to |                  |
|         |                  | one)             |                  |
+=========+==================+==================+==================+
| n41     | 0 (leftmost bit) | \- EN-DC         | \- This bit      |
|         |                  | contiguous       | shall be set to  |
|         |                  | intraband MPR as | 1 by a UE        |
|         |                  | defined in       | supporting       |
|         |                  | clause 6.2B.2.1  | DC\_(n)41AA UE   |
|         |                  | of 38.101-3      | EN-DC            |
|         |                  | v15.5.0          |                  |
+---------+------------------+------------------+------------------+
|         | 1                | \- EN-DC         | \- This bit      |
|         |                  | non-contiguous   | shall be set to  |
|         |                  | intraband MPR as | 1 by a UE        |
|         |                  | defined in       | supporting       |
|         |                  | clause 6.2B.2.2  | DC\_41A\_n41A    |
|         |                  | of 38.101-3      | EN-DC            |
|         |                  | v15.5.0          |                  |
+---------+------------------+------------------+------------------+
|         | 2                | \- EN-DC         | -This bit may be |
|         |                  | contiguous and   | set to 1 by a UE |
|         |                  | non-contiguous   | supporting       |
|         |                  | intraband MPR    | DC\_(n)41AA or   |
|         |                  | and A-MPR as     | DC\_41A\_n41A    |
|         |                  | defined in       | EN-DC            |
|         |                  | 38.101-3         |                  |
|         |                  | v16.4.0. If this |                  |
|         |                  | bit is not set   |                  |
|         |                  | the UE uses      |                  |
|         |                  | Rel-15 MPR or    |                  |
|         |                  | A-MPR for EN-DC  |                  |
|         |                  | contiguous and   |                  |
|         |                  | non-contiguous   |                  |
|         |                  | intraband MPR    |                  |
|         |                  | and A-MPR        |                  |
+---------+------------------+------------------+------------------+
| n71     | 0 (leftmost bit) | \- EN-DC         | \- This bit      |
|         |                  | contiguous       | shall be set to  |
|         |                  | intraband MPR as | 1 by a UE        |
|         |                  | defined in       | supporting       |
|         |                  | clause 6.2B.2.1  | DC\_(n)71AA UE   |
|         |                  | of 38.101-3      | EN-DC            |
|         |                  | v15.5.0          |                  |
+---------+------------------+------------------+------------------+

######## Annex M (informative): Change history

+--------+--------+--------+------+-----+-----+--------+--------+
| Change |        |        |      |     |     |        |        |
| h      |        |        |      |     |     |        |        |
| istory |        |        |      |     |     |        |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| Date   | M      | TDoc   | CR   | Rev | Cat | Sub    | New    |
|        | eeting |        |      |     |     | ject/C | v      |
|        |        |        |      |     |     | omment | ersion |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | R4-1   |      |     |     | I      | 0.0.1  |
| 017-08 | N4\#84 | 708909 |      |     |     | nitial |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | eleton |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN4\  | R4-1   |      |     |     | Added  | 0.1.0  |
| 017-10 | #84Bis | 709958 |      |     |     | ap     |        |
|        |        |        |      |     |     | proved |        |
|        |        |        |      |     |     | TPs in |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | AN4-NR |        |
|        |        |        |      |     |     | -AH\#3 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 09948, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 09454, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.10  |        |
|        |        |        |      |     |     | 1-1:UE |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | range  |        |
|        |        |        |      |     |     | 1, ZTE |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN4\  | R4-1   |      |     |     | Em     | 0.2.0  |
| 017-10 | #84Bis | 711978 |      |     |     | bedded |        |
|        |        |        |      |     |     | ap     |        |
|        |        |        |      |     |     | proved |        |
|        |        |        |      |     |     | TPs in |        |
|        |        |        |      |     |     | RAN4\  |        |
|        |        |        |      |     |     | #84Bis |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 11556, |        |
|        |        |        |      |     |     | \"TP   |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101: |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | Trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | cla    |        |
|        |        |        |      |     |     | use\", |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 10962, |        |
|        |        |        |      |     |     | \"TP   |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | Output |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | emiss  |        |
|        |        |        |      |     |     | ions\" |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 11608, |        |
|        |        |        |      |     |     | \"TP   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | ducted |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | ermodu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1(s  |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 6.5)\" |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | Number |        |
|        |        |        |      |     |     | of TPs |        |
|        |        |        |      |     |     | by     |        |
|        |        |        |      |     |     | e      |        |
|        |        |        |      |     |     | ditors |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | R4-1   |      |     |     | Ap     | 0.3.0  |
| 017-12 | N4\#85 | 713805 |      |     |     | proved |        |
|        |        |        |      |     |     | TPs in |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#85 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 13204, |        |
|        |        |        |      |     |     | TP on  |        |
|        |        |        |      |     |     | g      |        |
|        |        |        |      |     |     | eneral |        |
|        |        |        |      |     |     | parts  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14047, |        |
|        |        |        |      |     |     | WF on  |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | su     |        |
|        |        |        |      |     |     | b6GHz, |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14052, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | char   |        |
|        |        |        |      |     |     | acteri |        |
|        |        |        |      |     |     | stics, |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     | USA    |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14162, |        |
|        |        |        |      |     |     | TP to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | ACS,   |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14163, |        |
|        |        |        |      |     |     | TP to  |        |
|        |        |        |      |     |     | 36.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | I      |        |
|        |        |        |      |     |     | n-band |        |
|        |        |        |      |     |     | blo    |        |
|        |        |        |      |     |     | cking, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14446, |        |
|        |        |        |      |     |     | TP to  |        |
|        |        |        |      |     |     | 36.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | exce   |        |
|        |        |        |      |     |     | ptions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | res    |        |
|        |        |        |      |     |     | ponse, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14369, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | NBB    |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14529, |        |
|        |        |        |      |     |     | TP on  |        |
|        |        |        |      |     |     | intro  |        |
|        |        |        |      |     |     | ducing |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NR-LTE |        |
|        |        |        |      |     |     | DC     |        |
|        |        |        |      |     |     | inc    |        |
|        |        |        |      |     |     | luding |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14097, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | UE RF  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | stan   |        |
|        |        |        |      |     |     | dalone |        |
|        |        |        |      |     |     | SUL,   |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14536, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | Ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | Defin  |        |
|        |        |        |      |     |     | ition, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     | (Note, |        |
|        |        |        |      |     |     | this   |        |
|        |        |        |      |     |     | TP was |        |
|        |        |        |      |     |     | f      |        |
|        |        |        |      |     |     | urther |        |
|        |        |        |      |     |     | dis    |        |
|        |        |        |      |     |     | cussed |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | edited |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | refl   |        |
|        |        |        |      |     |     | ector) |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14114, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | Arrang |        |
|        |        |        |      |     |     | ement, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     | (Note, |        |
|        |        |        |      |     |     | this   |        |
|        |        |        |      |     |     | TP was |        |
|        |        |        |      |     |     | f      |        |
|        |        |        |      |     |     | urther |        |
|        |        |        |      |     |     | dis    |        |
|        |        |        |      |     |     | cussed |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | edited |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | refl   |        |
|        |        |        |      |     |     | ector) |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14029, |        |
|        |        |        |      |     |     | Sub6   |        |
|        |        |        |      |     |     | Ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | Sensit |        |
|        |        |        |      |     |     | ivity, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14329, |        |
|        |        |        |      |     |     | TP to  |        |
|        |        |        |      |     |     | TR     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-01 |        |
|        |        |        |      |     |     | v      |        |
|        |        |        |      |     |     | 0.2.0: |        |
|        |        |        |      |     |     | ON/OFF |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | design |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | t      |        |
|        |        |        |      |     |     | ransmi |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | list   |        |
|        |        |        |      |     |     | acc    |        |
|        |        |        |      |     |     | ording |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14542, |        |
|        |        |        |      |     |     | List   |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | to be  |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | oduced |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | RAN4   |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | core   |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | by     |        |
|        |        |        |      |     |     | De     |        |
|        |        |        |      |     |     | cember |        |
|        |        |        |      |     |     | 2017,  |        |
|        |        |        |      |     |     | RAN4   |        |
|        |        |        |      |     |     | Ch     |        |
|        |        |        |      |     |     | airmen |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | Input  |        |
|        |        |        |      |     |     | from:  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-17  |        |
|        |        |        |      |     |     | 14479, |        |
|        |        |        |      |     |     | TP for |        |
|        |        |        |      |     |     | TR     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 817-01 |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | width, |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | R4-1   |      |     |     | F      | 0.4.0  |
| 017-12 | N4\#85 | 714569 |      |     |     | urther |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | alig   |        |
|        |        |        |      |     |     | nments |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | 38.104 |        |
|        |        |        |      |     |     | after  |        |
|        |        |        |      |     |     | email  |        |
|        |        |        |      |     |     | review |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    |      |     |     | v1.0.0 | 1.0.0  |
| 017-12 | AN\#78 | 172475 |      |     |     | sub    |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | lenary |        |
|        |        |        |      |     |     | app    |        |
|        |        |        |      |     |     | roval. |        |
|        |        |        |      |     |     | Co     |        |
|        |        |        |      |     |     | ntents |        |
|        |        |        |      |     |     | same   |        |
|        |        |        |      |     |     | as     |        |
|        |        |        |      |     |     | 0.4.0  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      |        |      |     |     | Ap     | 15.0.0 |
| 017-12 | AN\#78 |        |      |     |     | proved |        |
|        |        |        |      |     |     | by     |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | lenary |        |
|        |        |        |      |     |     | --     |        |
|        |        |        |      |     |     | Rel-15 |        |
|        |        |        |      |     |     | spec   |        |
|        |        |        |      |     |     | under  |        |
|        |        |        |      |     |     | change |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | ontrol |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0003 |     | F   | Im     | 15.1.0 |
| 018-03 | AN\#79 | 180264 |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | CRs to |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00400, |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | B:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01102, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 30 MHz |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | su     |        |
|        |        |        |      |     |     | pport, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00032, |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 6.2.3  |        |
|        |        |        |      |     |     | - UE   |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | - NS   |        |
|        |        |        |      |     |     | v      |        |
|        |        |        |      |     |     | alues, |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     | USA    |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | B:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01121, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | pCR    |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | v      |        |
|        |        |        |      |     |     | ersion |        |
|        |        |        |      |     |     | 1      |        |
|        |        |        |      |     |     | 5.0.0: |        |
|        |        |        |      |     |     | Rem    |        |
|        |        |        |      |     |     | aining |        |
|        |        |        |      |     |     | ON/OFF |        |
|        |        |        |      |     |     | masks  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 NR |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | tr     |        |
|        |        |        |      |     |     | ansmis |        |
|        |        |        |      |     |     | sions, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00417, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | SEM    |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | table, |        |
|        |        |        |      |     |     | vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00033, |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 6      |        |
|        |        |        |      |     |     | .5.3.2 |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | o-exis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     | USA    |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01114, |        |
|        |        |        |      |     |     | Pr     |        |
|        |        |        |      |     |     | oposal |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | pro    |        |
|        |        |        |      |     |     | tected |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | num    |        |
|        |        |        |      |     |     | bering |        |
|        |        |        |      |     |     | in UE  |        |
|        |        |        |      |     |     | specs, |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00407, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Man    |        |
|        |        |        |      |     |     | datory |        |
|        |        |        |      |     |     | 4Rx    |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ntenna |        |
|        |        |        |      |     |     | perfo  |        |
|        |        |        |      |     |     | rmance |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | UE,    |        |
|        |        |        |      |     |     | Vo     |        |
|        |        |        |      |     |     | dafone |        |
|        |        |        |      |     |     | Group  |        |
|        |        |        |      |     |     | Plc    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 800451 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of 4Rx |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01136, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01137, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR:    |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | RE     |        |
|        |        |        |      |     |     | FSENS, |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00395, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to ACS |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | i      |        |
|        |        |        |      |     |     | n-band |        |
|        |        |        |      |     |     | blo    |        |
|        |        |        |      |     |     | cking, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00396, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | blo    |        |
|        |        |        |      |     |     | cking, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00397, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | res    |        |
|        |        |        |      |     |     | ponse, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00305, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | NR FR1 |        |
|        |        |        |      |     |     | wide   |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | ermodu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00320, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | (s     |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 7.9),  |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00473, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | UE RF  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00965, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Asym   |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | CH BW  |        |
|        |        |        |      |     |     | oper   |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00882, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | n77    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n78    |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Orange |        |
|        |        |        |      |     |     | UK     |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01012, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Cl     |        |
|        |        |        |      |     |     | arific |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | to UE  |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | utili  |        |
|        |        |        |      |     |     | zation |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.3,   |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 00030, |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.4.4  |        |
|        |        |        |      |     |     | -      |        |
|        |        |        |      |     |     | TX--RX |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | separ  |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     | USA    |        |
|        |        |        |      |     |     | Inc    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01228, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pacing |        |
|        |        |        |      |     |     | for CA |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | FR1(s  |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.4    |        |
|        |        |        |      |     |     | .1.2), |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01231, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | spaci  |        |
|        |        |        |      |     |     | ng:38. |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | amsung |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01235, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | calcu  |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.4.2, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F:     |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01318, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | syn    |        |
|        |        |        |      |     |     | chroni |        |
|        |        |        |      |     |     | zation |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | aster, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | RAN    |        |
|        |        |        |      |     |     | 4\#86: |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03053, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | new    |        |
|        |        |        |      |     |     | spec   |        |
|        |        |        |      |     |     | str    |        |
|        |        |        |      |     |     | ucture |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01479, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | efault |        |
|        |        |        |      |     |     | Tx-RX  |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | sepa   |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | FR1(s  |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5      |        |
|        |        |        |      |     |     | .4.4), |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 01581, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | update |        |
|        |        |        |      |     |     | of 4Rx |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     | Techno |        |
|        |        |        |      |     |     | logies |        |
|        |        |        |      |     |     | France |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 02211, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Uplink |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 NR |        |
|        |        |        |      |     |     | RE     |        |
|        |        |        |      |     |     | FSENS, |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 02342, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | NR FR1 |        |
|        |        |        |      |     |     | ACS    |        |
|        |        |        |      |     |     | case 2 |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | etting |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | (Note  |        |
|        |        |        |      |     |     | 1),    |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 02509, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | v1     |        |
|        |        |        |      |     |     | 5.0.0: |        |
|        |        |        |      |     |     | Rem    |        |
|        |        |        |      |     |     | aining |        |
|        |        |        |      |     |     | ON/OFF |        |
|        |        |        |      |     |     | masks  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 NR |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | tr     |        |
|        |        |        |      |     |     | ansmis |        |
|        |        |        |      |     |     | sions, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 02566, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | mixed  |        |
|        |        |        |      |     |     | nume   |        |
|        |        |        |      |     |     | rology |        |
|        |        |        |      |     |     | gua    |        |
|        |        |        |      |     |     | rdband |        |
|        |        |        |      |     |     | size,  |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 02978, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.     |        |
|        |        |        |      |     |     | 4.2.3, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03064, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | e      |        |
|        |        |        |      |     |     | rrors, |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03065, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | n41r   |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03242, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | n66,   |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03285, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to CH  |        |
|        |        |        |      |     |     | BWs    |        |
|        |        |        |      |     |     | w      |        |
|        |        |        |      |     |     | ithout |        |
|        |        |        |      |     |     | sym    |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | Ne     |        |
|        |        |        |      |     |     | twork, |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03436, |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of UL  |        |
|        |        |        |      |     |     | subc   |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | ali    |        |
|        |        |        |      |     |     | gnment |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | AT&T   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03456, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | Emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | Coexis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03461, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03452, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | 37.865 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03567, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Sync   |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | offset |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | re-f   |        |
|        |        |        |      |     |     | arming |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | (5     |        |
|        |        |        |      |     |     | .4.3), |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03365, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | PC2    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | PC3    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | UTRA   |        |
|        |        |        |      |     |     | prote  |        |
|        |        |        |      |     |     | ction, |        |
|        |        |        |      |     |     | Nokia  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0011 |     | F   | CR to  | 15.2.0 |
| 018-06 | AN\#80 | 181262 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4   |        |
|        |        |        |      |     |     | \      |        |
|        |        |        |      |     |     | #86bis |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | RAN4   |        |
|        |        |        |      |     |     | \#87   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 03900, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL,   |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804021 |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | cl     |        |
|        |        |        |      |     |     | arific |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | FR1 CA |        |
|        |        |        |      |     |     | BW     |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | lasses |        |
|        |        |        |      |     |     | Nokia, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | anghai |        |
|        |        |        |      |     |     | Bell   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804140 |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | Narrow |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | Bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804219 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | SEM    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | SPRINT |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804266 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | cr     |        |
|        |        |        |      |     |     | iteria |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804267 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n3     |        |
|        |        |        |      |     |     | ,n5,n8 |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | levels |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804268 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corrr  |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to n41 |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | sensi  |        |
|        |        |        |      |     |     | tivity |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804370 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | add    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | DL CA  |        |
|        |        |        |      |     |     | in FR1 |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804581 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | On EVM |        |
|        |        |        |      |     |     | W      |        |
|        |        |        |      |     |     | ording |        |
|        |        |        |      |     |     | Qua    |        |
|        |        |        |      |     |     | lcomm, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804948 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 5.3.3  |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Nokia, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | anghai |        |
|        |        |        |      |     |     | Bell   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804877 |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 37.865 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805444 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Asym   |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | CH BW  |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805447 |        |
|        |        |        |      |     |     | drfat  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | inc    |        |
|        |        |        |      |     |     | luding |        |
|        |        |        |      |     |     | SRS    |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ntenna |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805462 |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to UE  |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805659 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805664 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | F      |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805665 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | inner  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | outer  |        |
|        |        |        |      |     |     | defin  |        |
|        |        |        |      |     |     | itions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805684 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | Raster |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Re     |        |
|        |        |        |      |     |     | source |        |
|        |        |        |      |     |     | E      |        |
|        |        |        |      |     |     | lement |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | apping |        |
|        |        |        |      |     |     | (S     |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.     |        |
|        |        |        |      |     |     | 4.2.2) |        |
|        |        |        |      |     |     | and RB |        |
|        |        |        |      |     |     | ali    |        |
|        |        |        |      |     |     | gnment |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | dif    |        |
|        |        |        |      |     |     | ferent |        |
|        |        |        |      |     |     | numero |        |
|        |        |        |      |     |     | logies |        |
|        |        |        |      |     |     | (S     |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.3.4) |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805698 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | x(Ch7) |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n77,   |        |
|        |        |        |      |     |     | n78    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n79 RF |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805699 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Tx/Rx  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA ZTE |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805751 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | -to-UE |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | rotect |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | 29     |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | 71 LG  |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | France |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805783 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | T      |        |
|        |        |        |      |     |     | x(Ch6) |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n77,   |        |
|        |        |        |      |     |     | n78    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n79 RF |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805902 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | SUL\_n |        |
|        |        |        |      |     |     | 78-n80 |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805904 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of new |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805921 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | NR UE  |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | SNR    |        |
|        |        |        |      |     |     | FRC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 805981 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS3    |        |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | 1:Sync |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | amsung |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 804548 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | CA BW  |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806170 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | error  |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806481 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | E      |        |
|        |        |        |      |     |     | nviron |        |
|        |        |        |      |     |     | mental |        |
|        |        |        |      |     |     | cond   |        |
|        |        |        |      |     |     | itions |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806657 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | BW for |        |
|        |        |        |      |     |     | min    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | off    |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806669 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38.1 |        |
|        |        |        |      |     |     | 01-1\_ |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | 2UL CA |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806673 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38.1 |        |
|        |        |        |      |     |     | 01-1\_ |        |
|        |        |        |      |     |     | Remove |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | Tx and |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806677 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | inc    |        |
|        |        |        |      |     |     | luding |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA LG  |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | France |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806719 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of 7.5 |        |
|        |        |        |      |     |     | kHz    |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | Eri    |        |
|        |        |        |      |     |     | csson, |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806844 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | (Ch6): |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for n1 |        |
|        |        |        |      |     |     | and n8 |        |
|        |        |        |      |     |     | So     |        |
|        |        |        |      |     |     | ftBank |        |
|        |        |        |      |     |     | Corp.  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 806945 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | -ARFCN |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | 5.4.2) |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807039 |        |
|        |        |        |      |     |     | Intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | termi  |        |
|        |        |        |      |     |     | nology |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807178 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to n70 |        |
|        |        |        |      |     |     | TX/RX  |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | sepa   |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807181 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807234 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Some   |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807269 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Wide   |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | ermodu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | \<2    |        |
|        |        |        |      |     |     | 700MHz |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807392 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | remove |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | for SU |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807647 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Asym   |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | CH BW  |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807680 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | chieve |        |
|        |        |        |      |     |     | ali    |        |
|        |        |        |      |     |     | gnment |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | data   |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | SSB    |        |
|        |        |        |      |     |     | subc   |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | grids  |        |
|        |        |        |      |     |     | Nokia, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | anghai |        |
|        |        |        |      |     |     | Bell,  |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807705 |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n51    |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | His    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807814 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | SEM    |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807851 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | prot   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for n5 |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807920 |        |
|        |        |        |      |     |     | G      |        |
|        |        |        |      |     |     | eneral |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | do     |        |
|        |        |        |      |     |     | wnlink |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 807923 |        |
|        |        |        |      |     |     | Reso   |        |
|        |        |        |      |     |     | lution |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | ACLR   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808084 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of n12 |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808087 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of n2, |        |
|        |        |        |      |     |     | n25,   |        |
|        |        |        |      |     |     | n66    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n70    |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpor |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Dishn  |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808090 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Inc    |        |
|        |        |        |      |     |     | lusion |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | RxTx   |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | Eri    |        |
|        |        |        |      |     |     | csson, |        |
|        |        |        |      |     |     | Vod    |        |
|        |        |        |      |     |     | afone, |        |
|        |        |        |      |     |     | Orange |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808107 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1\ |        |
|        |        |        |      |     |     | _corre |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808111 |        |
|        |        |        |      |     |     | TP to  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | - UE   |        |
|        |        |        |      |     |     | ON/OFF |        |
|        |        |        |      |     |     | masks  |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808116 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | 34,n39 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n40 RF |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corp   |        |
|        |        |        |      |     |     | oratio |        |
|        |        |        |      |     |     | n,CMCC |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808136 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | FR1 UE |        |
|        |        |        |      |     |     | Power  |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | ontrol |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808141 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to MPR |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | PC2    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808142 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpor |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Nokia, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | anghai |        |
|        |        |        |      |     |     | Bell,  |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808143 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n20    |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808155 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | reqir  |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | amsung |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808178 |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | about  |        |
|        |        |        |      |     |     | n50 &  |        |
|        |        |        |      |     |     | n51 in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | Hisi   |        |
|        |        |        |      |     |     | licon, |        |
|        |        |        |      |     |     | Et     |        |
|        |        |        |      |     |     | isalat |        |
|        |        |        |      |     |     | (e     |        |
|        |        |        |      |     |     | ditors |        |
|        |        |        |      |     |     | note:  |        |
|        |        |        |      |     |     | n50    |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | imple  |        |
|        |        |        |      |     |     | mented |        |
|        |        |        |      |     |     | per    |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | irmans |        |
|        |        |        |      |     |     | aggre  |        |
|        |        |        |      |     |     | ement) |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808182 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n28    |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808187 |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Co     |        |
|        |        |        |      |     |     | herent |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | MIMO   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | ustria |        |
|        |        |        |      |     |     | RFFE   |        |
|        |        |        |      |     |     | GmbH   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808207 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | On EVM |        |
|        |        |        |      |     |     | Ave    |        |
|        |        |        |      |     |     | raging |        |
|        |        |        |      |     |     | L      |        |
|        |        |        |      |     |     | ength, |        |
|        |        |        |      |     |     | W      |        |
|        |        |        |      |     |     | ording |        |
|        |        |        |      |     |     | ,      |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808209 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for Tx |        |
|        |        |        |      |     |     | (Ch6)  |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | HPUE   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808466 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | UL RMC |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | OCNG   |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | attern |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FDD    |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | tests  |        |
|        |        |        |      |     |     | RD     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ession |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808493 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | sync   |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | (5.4)  |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 808507 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of new |        |
|        |        |        |      |     |     | 90MHz  |        |
|        |        |        |      |     |     | UE CBW |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | 41/n78 |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | Inc.,  |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Uplus, |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | amsung |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 08176, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | :      |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n8,    |        |
|        |        |        |      |     |     | So     |        |
|        |        |        |      |     |     | ftBank |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 08201, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | :      |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n1,    |        |
|        |        |        |      |     |     | So     |        |
|        |        |        |      |     |     | ftBank |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 07101, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 37.865 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0025 |     | F   | Big CR | 15.3.0 |
| 018-09 | AN\#81 | 181896 |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4   |        |
|        |        |        |      |     |     | \#NR-A |        |
|        |        |        |      |     |     | H-1807 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09335, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | UL RMC |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 RF |        |
|        |        |        |      |     |     | tests  |        |
|        |        |        |      |     |     | ,      |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09337, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | NR UE  |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | SNR    |        |
|        |        |        |      |     |     | FRC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09339, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 RF |        |
|        |        |        |      |     |     | Tests, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09396, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | NR UE  |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | input  |        |
|        |        |        |      |     |     | level  |        |
|        |        |        |      |     |     | FRC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09567, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | OCNG   |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | attern |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | tests, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | I      |        |
|        |        |        |      |     |     | ncorpo |        |
|        |        |        |      |     |     | rated, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#88 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09714, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | i      |        |
|        |        |        |      |     |     | n-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | nritsu |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09784, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on CA  |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | lasses |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09785, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | power, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09793, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | mask,  |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 09919, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | CATT   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10091, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | - UE   |        |
|        |        |        |      |     |     | ON-OFF |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | clean  |        |
|        |        |        |      |     |     | up,    |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10210, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | inner  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | outer  |        |
|        |        |        |      |     |     | RB     |        |
|        |        |        |      |     |     | alloc  |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | f      |        |
|        |        |        |      |     |     | ormula |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ction, |        |
|        |        |        |      |     |     | Med    |        |
|        |        |        |      |     |     | iaTek, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10229, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | correc |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Med    |        |
|        |        |        |      |     |     | iaTek, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10230, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | 90MHz  |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | CBW,   |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Electr |        |
|        |        |        |      |     |     | onics, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10232, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 7      |        |
|        |        |        |      |     |     | .3.2-1 |        |
|        |        |        |      |     |     | n77    |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | sensi  |        |
|        |        |        |      |     |     | tivity |        |
|        |        |        |      |     |     | correc |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Med    |        |
|        |        |        |      |     |     | iaTek, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10369, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ymbols |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | bbrevi |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 3, ZTE |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10376, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR:    |        |
|        |        |        |      |     |     | G      |        |
|        |        |        |      |     |     | eneral |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to n71 |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Dish   |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10428, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for UL |        |
|        |        |        |      |     |     | MIMO,  |        |
|        |        |        |      |     |     | OPPO   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10552, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | t      |        |
|        |        |        |      |     |     | ables, |        |
|        |        |        |      |     |     | OPPO   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10729, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n74    |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10862, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | U      |        |
|        |        |        |      |     |     | pdates |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Tr     |        |
|        |        |        |      |     |     | ansmit |        |
|        |        |        |      |     |     | Modu   |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | Annex, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10892, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | update |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 6.     |        |
|        |        |        |      |     |     | 2D.1-2 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10961, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | ACS    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ement, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10965, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-Band |        |
|        |        |        |      |     |     | Bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ement, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10967, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | Int    |        |
|        |        |        |      |     |     | ermodu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 10974, |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | let    |        |
|        |        |        |      |     |     | tering |        |
|        |        |        |      |     |     | change |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11189, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | add    |        |
|        |        |        |      |     |     | more   |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | etails |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Co     |        |
|        |        |        |      |     |     | herent |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | MIMO   |        |
|        |        |        |      |     |     | spec   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11280, |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | t      |        |
|        |        |        |      |     |     | itles, |        |
|        |        |        |      |     |     | Vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11455, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | Ph     |        |
|        |        |        |      |     |     | ysical |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 RF |        |
|        |        |        |      |     |     | tests, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Europe |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | Spain) |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11457, |        |
|        |        |        |      |     |     | NS     |        |
|        |        |        |      |     |     | numb   |        |
|        |        |        |      |     |     | ering, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11459, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | CATT   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11463, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | NR CA  |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | n8-n75 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n2     |        |
|        |        |        |      |     |     | 8-n75, |        |
|        |        |        |      |     |     | Vo     |        |
|        |        |        |      |     |     | dafone |        |
|        |        |        |      |     |     | Italia |        |
|        |        |        |      |     |     | SpA    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11472, |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | about  |        |
|        |        |        |      |     |     | n51 in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | Hisi   |        |
|        |        |        |      |     |     | licon, |        |
|        |        |        |      |     |     | Et     |        |
|        |        |        |      |     |     | isalat |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11474, |        |
|        |        |        |      |     |     | CR CP- |        |
|        |        |        |      |     |     | OFDM   |        |
|        |        |        |      |     |     | almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | alloc  |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Nokia, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | anghai |        |
|        |        |        |      |     |     | Bell   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11477, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | Power  |        |
|        |        |        |      |     |     | Co     |        |
|        |        |        |      |     |     | ntrol, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11478, |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n20    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n28,   |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11490, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | L      |        |
|        |        |        |      |     |     | eakage |        |
|        |        |        |      |     |     | table, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11491, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | tr     |        |
|        |        |        |      |     |     | ansmit |        |
|        |        |        |      |     |     | signal |        |
|        |        |        |      |     |     | qu     |        |
|        |        |        |      |     |     | ality, |        |
|        |        |        |      |     |     | OPPO   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11493, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | Sh     |        |
|        |        |        |      |     |     | aping, |        |
|        |        |        |      |     |     | Indian |        |
|        |        |        |      |     |     | Ins    |        |
|        |        |        |      |     |     | titute |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Tech   |        |
|        |        |        |      |     |     | (M),   |        |
|        |        |        |      |     |     | Indian |        |
|        |        |        |      |     |     | Ins    |        |
|        |        |        |      |     |     | titute |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Tech   |        |
|        |        |        |      |     |     | (H),   |        |
|        |        |        |      |     |     | CEWiT, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11513, |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | pr     |        |
|        |        |        |      |     |     | oposal |        |
|        |        |        |      |     |     | on 2UL |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | odific |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | So     |        |
|        |        |        |      |     |     | ftBank |        |
|        |        |        |      |     |     | Corp.  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11514, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | OCNG,  |        |
|        |        |        |      |     |     | Ke     |        |
|        |        |        |      |     |     | ysight |        |
|        |        |        |      |     |     | Techno |        |
|        |        |        |      |     |     | logies |        |
|        |        |        |      |     |     | UK Ltd |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11516, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | NR DL  |        |
|        |        |        |      |     |     | FRCs   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 UE |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11550, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pacing |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | escrip |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11553, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | tries, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11783, |        |
|        |        |        |      |     |     | Measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | period |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | PRACH  |        |
|        |        |        |      |     |     | time   |        |
|        |        |        |      |     |     | mask,  |        |
|        |        |        |      |     |     | CATT   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11792, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | vision |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n1,    |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11798, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | Pcmax  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11799, |        |
|        |        |        |      |     |     | Pcmax  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | NR CA  |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR,    |        |
|        |        |        |      |     |     | I      |        |
|        |        |        |      |     |     | nterDi |        |
|        |        |        |      |     |     | gital, |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11812, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | On FR1 |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_04, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11816, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | update |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Long   |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Short  |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ubslot |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11894, |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | about  |        |
|        |        |        |      |     |     | n50 in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11896, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | GSCN   |        |
|        |        |        |      |     |     | range  |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | odific |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 11285, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | NS\_04 |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | -MPR\' |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | isison |        |
|        |        |        |      |     |     | correc |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Sprint |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0029 | 1   | F   | En     | 15.4.0 |
| 018-12 | AN\#82 | 182836 |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4\# |        |
|        |        |        |      |     |     | 88Bis: |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12050, |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | Si     |        |
|        |        |        |      |     |     | mplifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_08, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12054, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Nokia. |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12079, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | asym   |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | UL DL  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | BW     |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n71,   |        |
|        |        |        |      |     |     | T-     |        |
|        |        |        |      |     |     | Mobile |        |
|        |        |        |      |     |     | USA    |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12121, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | Note1  |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | RX     |        |
|        |        |        |      |     |     | tests, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12128, |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | 256QAM |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ement, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12200, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Add    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | to PC3 |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | table, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12217, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | descri |        |
|        |        |        |      |     |     | ptions |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12319, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | correc |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12320, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | exce   |        |
|        |        |        |      |     |     | ptions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12322, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL,   |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12397, |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CP     |        |
|        |        |        |      |     |     | -OFDM, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12508, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | & SS   |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 12611, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Some   |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | ombina |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13459, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | 4Rx    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n38,   |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13469, |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of TDD |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ratiin |        |
|        |        |        |      |     |     | for CA |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13521, |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | ?TC,c  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | single |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | Pcmax  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13798, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | redu   |        |
|        |        |        |      |     |     | ction, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13811, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corrr  |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to n12 |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | sensi  |        |
|        |        |        |      |     |     | tivity |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | l      |        |
|        |        |        |      |     |     | evels, |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13812, |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | limits |        |
|        |        |        |      |     |     | ,      |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13813, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | P-Max  |        |
|        |        |        |      |     |     | for 5G |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | HPUE,  |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14158, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | o-exis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14159, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | CS/IBB |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | C,     |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13843, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | F,     |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 13845, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | PI/2   |        |
|        |        |        |      |     |     | PBSK   |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equrie |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR\'s  |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#89 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15950, |        |
|        |        |        |      |     |     | dCR on |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | erging |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4\# |        |
|        |        |        |      |     |     | 88Bis, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14752, |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | n41,   |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14824, |        |
|        |        |        |      |     |     | n50    |        |
|        |        |        |      |     |     | A-MPR, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14959, |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hanges |        |
|        |        |        |      |     |     | to Max |        |
|        |        |        |      |     |     | input  |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | UL and |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | figura |        |
|        |        |        |      |     |     | tgions |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | OPPO   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14970, |        |
|        |        |        |      |     |     | NR FR1 |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | lative |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | tol    |        |
|        |        |        |      |     |     | erance |        |
|        |        |        |      |     |     | CR,    |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 14972, |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_03 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_03U |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | -formu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | NS     |        |
|        |        |        |      |     |     | \_100, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15060, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | about  |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | fa     |        |
|        |        |        |      |     |     | llback |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | CA in  |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | NTT    |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | OCOMO, |        |
|        |        |        |      |     |     | INC.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15392, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | NS\_04 |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15563, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | on 7.5 |        |
|        |        |        |      |     |     | KHz    |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | in NR  |        |
|        |        |        |      |     |     | re-    |        |
|        |        |        |      |     |     | farmed |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15863, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | ominal |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pacing |        |
|        |        |        |      |     |     | for 30 |        |
|        |        |        |      |     |     | kHz    |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | aster, |        |
|        |        |        |      |     |     | SPRINT |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15898, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | F,     |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 15917, |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | on DL  |        |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16162, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of SRS |        |
|        |        |        |      |     |     | switch |        |
|        |        |        |      |     |     | IL in  |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | OPPO   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16199, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | F      |        |
|        |        |        |      |     |     | R1-FR2 |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | -to-UE |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | France |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16200, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16240, |        |
|        |        |        |      |     |     | Tra    |        |
|        |        |        |      |     |     | nsient |        |
|        |        |        |      |     |     | period |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SRS    |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | ntenna |        |
|        |        |        |      |     |     | Swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16243, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | -1\_Cl |        |
|        |        |        |      |     |     | arific |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | on MSD |        |
|        |        |        |      |     |     | and UL |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16466, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hanges |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16468, |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | of 7.5 |        |
|        |        |        |      |     |     | kHz    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | bands, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16604, |        |
|        |        |        |      |     |     | TDD    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | test   |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16663, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | 5.3.4) |        |
|        |        |        |      |     |     | RB     |        |
|        |        |        |      |     |     | alig   |        |
|        |        |        |      |     |     | nment, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-18  |        |
|        |        |        |      |     |     | 16755, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | ACS    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | IBB    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | F      |        |
|        |        |        |      |     |     | urther |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hanges |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | AN\#82 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | \- 7.5 |        |
|        |        |        |      |     |     | kHz    |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | is     |        |
|        |        |        |      |     |     | spe    |        |
|        |        |        |      |     |     | cified |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | all    |        |
|        |        |        |      |     |     | FDD    |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | 5      |        |
|        |        |        |      |     |     | .4.2.1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0030 | 2   | F   | C      | 15.4.0 |
| 018-12 | AN\#82 | 182814 |      |     |     | ompany |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | 2Rx    |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | veh    |        |
|        |        |        |      |     |     | icular |        |
|        |        |        |      |     |     | UE at  |        |
|        |        |        |      |     |     | FR1    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0034 |     | F   | CR to  | 15.5.0 |
| 019-03 | AN\#83 | 190403 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#90 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | Ra     |        |
|        |        |        |      |     |     | n4\#90 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00032, |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00031, |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | on SRS |        |
|        |        |        |      |     |     | IL for |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00161, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | Re     |        |
|        |        |        |      |     |     | lative |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | tole   |        |
|        |        |        |      |     |     | rance, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00162, |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00274, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on NR  |        |
|        |        |        |      |     |     | g      |        |
|        |        |        |      |     |     | eneral |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | mask,  |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00275, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | sssion |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     | sig    |        |
|        |        |        |      |     |     | nalled |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_40, |        |
|        |        |        |      |     |     | NS\_41 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_42, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00424, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | refe   |        |
|        |        |        |      |     |     | rences |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | other  |        |
|        |        |        |      |     |     | typos, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00508, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on UE  |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitter |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | other  |        |
|        |        |        |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | correc |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00723, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | error  |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00727, |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | PRACH  |        |
|        |        |        |      |     |     | EVM    |        |
|        |        |        |      |     |     | window |        |
|        |        |        |      |     |     | length |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00840, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | modifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Tr     |        |
|        |        |        |      |     |     | ansmit |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | ermodu |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ement, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 00848, |        |
|        |        |        |      |     |     | \[RAN5 |        |
|        |        |        |      |     |     | LS\    |        |
|        |        |        |      |     |     | ]Draft |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emis   |        |
|        |        |        |      |     |     | sions, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01033, |        |
|        |        |        |      |     |     | Ali    |        |
|        |        |        |      |     |     | gnment |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Foob   |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | elated |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01273, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | HA     |        |
|        |        |        |      |     |     | RQ-ACK |        |
|        |        |        |      |     |     | transm |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | timing |        |
|        |        |        |      |     |     | for DL |        |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | TDD    |        |
|        |        |        |      |     |     | SCS=   |        |
|        |        |        |      |     |     | 60kHz, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01766, |        |
|        |        |        |      |     |     | dra    |        |
|        |        |        |      |     |     | ft\_CR |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to UL  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | sensit |        |
|        |        |        |      |     |     | ivity, |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01823, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | requ   |        |
|        |        |        |      |     |     | irment |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | H      |        |
|        |        |        |      |     |     | uawei, |        |
|        |        |        |      |     |     | HiS    |        |
|        |        |        |      |     |     | ilicon |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01835, |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | on MSD |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 41-n78 |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01847, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | efault |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | class, |        |
|        |        |        |      |     |     | Sprint |        |
|        |        |        |      |     |     | Corpor |        |
|        |        |        |      |     |     | ation\ |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01873, |        |
|        |        |        |      |     |     | Re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | refer  |        |
|        |        |        |      |     |     | ences, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01925, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | update |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | wide   |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | termod |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rments |        |
|        |        |        |      |     |     | for BW |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | C, D,  |        |
|        |        |        |      |     |     | E,     |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01992, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | NS\_41 |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50 ,  |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02001, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on n41 |        |
|        |        |        |      |     |     | -- B40 |        |
|        |        |        |      |     |     | coexis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02150, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | -1\_Cl |        |
|        |        |        |      |     |     | arific |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | on MSD |        |
|        |        |        |      |     |     | and UL |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02166, |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | ON/OFF |        |
|        |        |        |      |     |     | time   |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Inc    |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02174, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | On FR1 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | NS\_08 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n8,    |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02175, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_05U |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_08U |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02194, |        |
|        |        |        |      |     |     | \[41   |        |
|        |        |        |      |     |     | DL\    |        |
|        |        |        |      |     |     | ]Draft |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | less   |        |
|        |        |        |      |     |     | than   |        |
|        |        |        |      |     |     | 27     |        |
|        |        |        |      |     |     | 00MHz, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02196, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 7.9A   |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02223, |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | op     |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02225, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on CA  |        |
|        |        |        |      |     |     | BW     |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | lasses |        |
|        |        |        |      |     |     | fa     |        |
|        |        |        |      |     |     | llback |        |
|        |        |        |      |     |     | g      |        |
|        |        |        |      |     |     | roups, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02233, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | cla    |        |
|        |        |        |      |     |     | rifica |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02339, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on FR1 |        |
|        |        |        |      |     |     | exte   |        |
|        |        |        |      |     |     | nsion, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02455, |        |
|        |        |        |      |     |     | Comp   |        |
|        |        |        |      |     |     | letion |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | Pcmax  |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ecific |        |
|        |        |        |      |     |     | ation: |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | P-max  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | P\_NR, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02468, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR:    |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | Cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | Inter  |        |
|        |        |        |      |     |     | fering |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | ignal, |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | amsung |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02479, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | errors |        |
|        |        |        |      |     |     | to TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02480, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | modifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     | sig    |        |
|        |        |        |      |     |     | nalled |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_04, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02655, |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on NR  |        |
|        |        |        |      |     |     | Uplink |        |
|        |        |        |      |     |     | RBs    |        |
|        |        |        |      |     |     | loc    |        |
|        |        |        |      |     |     | ation, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 01610, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | for UL |        |
|        |        |        |      |     |     | MIMO , |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hanges |        |
|        |        |        |      |     |     | after  |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | AN\#83 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | To     |        |
|        |        |        |      |     |     | align  |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | annex  |        |
|        |        |        |      |     |     | num    |        |
|        |        |        |      |     |     | bering |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | other  |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ecific |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | (TS    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-x |        |
|        |        |        |      |     |     | se     |        |
|        |        |        |      |     |     | ries), |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | nnexes |        |
|        |        |        |      |     |     | J and  |        |
|        |        |        |      |     |     | K were |        |
|        |        |        |      |     |     | added  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Change |        |
|        |        |        |      |     |     | h      |        |
|        |        |        |      |     |     | istory |        |
|        |        |        |      |     |     | was    |        |
|        |        |        |      |     |     | nu     |        |
|        |        |        |      |     |     | mbered |        |
|        |        |        |      |     |     | as     |        |
|        |        |        |      |     |     | annex  |        |
|        |        |        |      |     |     | L.     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0047 |     | F   | CR to  | 15.6.0 |
| 019-06 | AN\#84 | 191240 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4\  |        |
|        |        |        |      |     |     | #90bis |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#91 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RAN4\  |        |
|        |        |        |      |     |     | #90Bis |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02826, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | modifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of ACS |        |
|        |        |        |      |     |     | test   |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | case 2 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA ,   |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02926, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Pcmax, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 02975, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | PRACH  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | PUCCH  |        |
|        |        |        |      |     |     | format |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | EVM in |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | nritsu |        |
|        |        |        |      |     |     | corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03032, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | error  |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | LG     |        |
|        |        |        |      |     |     | Elect  |        |
|        |        |        |      |     |     | ronics |        |
|        |        |        |      |     |     | France |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03120, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | allo   |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03124, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | 41-n40 |        |
|        |        |        |      |     |     | coexis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03151, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | -1\_re |        |
|        |        |        |      |     |     | moving |        |
|        |        |        |      |     |     | DC     |        |
|        |        |        |      |     |     | sec    |        |
|        |        |        |      |     |     | tions, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03195, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | remove |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | racket |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | \"     |        |
|        |        |        |      |     |     | powerB |        |
|        |        |        |      |     |     | oostin |        |
|        |        |        |      |     |     | g-pi2B |        |
|        |        |        |      |     |     | PSK\", |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03392, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to EVM |        |
|        |        |        |      |     |     | equ    |        |
|        |        |        |      |     |     | alizer |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | fl     |        |
|        |        |        |      |     |     | atness |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | equire |        |
|        |        |        |      |     |     | ments, |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03473, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | FREF,  |        |
|        |        |        |      |     |     | Shift, |        |
|        |        |        |      |     |     | CMCC   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 03508, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | o-exis |        |
|        |        |        |      |     |     | tence, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04335, |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | raftCR |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_100 |        |
|        |        |        |      |     |     | UTRA   |        |
|        |        |        |      |     |     | ACLR   |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | list,  |        |
|        |        |        |      |     |     | Sk     |        |
|        |        |        |      |     |     | yworks |        |
|        |        |        |      |     |     | Sol    |        |
|        |        |        |      |     |     | utions |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04460, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Pcmax, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04537, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TR     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_04, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04554, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | dy     |        |
|        |        |        |      |     |     | namics |        |
|        |        |        |      |     |     | DTX    |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | moval, |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04927, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | l      |        |
|        |        |        |      |     |     | eakage |        |
|        |        |        |      |     |     | in RBs |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1,   |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | nritsu |        |
|        |        |        |      |     |     | corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04928, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | output |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | redu   |        |
|        |        |        |      |     |     | ction, |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04929, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | Rel-15 |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04941, |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | boo    |        |
|        |        |        |      |     |     | sting, |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04957, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TR38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | --     |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | to EVM |        |
|        |        |        |      |     |     | aver   |        |
|        |        |        |      |     |     | aging, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04958, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TR38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | --     |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | fla    |        |
|        |        |        |      |     |     | tness, |        |
|        |        |        |      |     |     | Rohde  |        |
|        |        |        |      |     |     | &      |        |
|        |        |        |      |     |     | S      |        |
|        |        |        |      |     |     | chwarz |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04967, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | input  |        |
|        |        |        |      |     |     | level  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA,    |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04969, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | ed     |        |
|        |        |        |      |     |     | itoral |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ction, |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-19  |        |
|        |        |        |      |     |     | 04987, |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | CATT   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorced |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#91 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905339 |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | in FR1 |        |
|        |        |        |      |     |     | Nokia  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905503 |        |
|        |        |        |      |     |     | Change |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | 4.2(d) |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905524 |        |
|        |        |        |      |     |     | \[Rx\  |        |
|        |        |        |      |     |     | ]Draft |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Re     |        |
|        |        |        |      |     |     | moving |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | in Rx  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905526 |        |
|        |        |        |      |     |     | \[Rx\  |        |
|        |        |        |      |     |     | ]Draft |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | de     |        |
|        |        |        |      |     |     | fining |        |
|        |        |        |      |     |     | NBB    |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | quirem |        |
|        |        |        |      |     |     | ents\< |        |
|        |        |        |      |     |     | 2.7GHz |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905772 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905795 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to a   |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | of PRB |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | i      |        |
|        |        |        |      |     |     | n-band |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | in FR1 |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | nritsu |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 905797 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | ontrol |        |
|        |        |        |      |     |     | in FR1 |        |
|        |        |        |      |     |     | A      |        |
|        |        |        |      |     |     | nritsu |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 906140 |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for CA |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 906153 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA ACS |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | i      |        |
|        |        |        |      |     |     | n-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 906154 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Adding |        |
|        |        |        |      |     |     | symbol |        |
|        |        |        |      |     |     | defin  |        |
|        |        |        |      |     |     | itions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA Rx  |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | input  |        |
|        |        |        |      |     |     | level  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | ACS    |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 906871 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | op     |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907131 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | to FR1 |        |
|        |        |        |      |     |     | NS\_43 |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | ranges |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907135 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | rel.   |        |
|        |        |        |      |     |     | 15 to  |        |
|        |        |        |      |     |     | fix    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | Exce   |        |
|        |        |        |      |     |     | ptions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | Bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | Apple  |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907419 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | impro  |        |
|        |        |        |      |     |     | vement |        |
|        |        |        |      |     |     | to EVM |        |
|        |        |        |      |     |     | equ    |        |
|        |        |        |      |     |     | alizer |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | fl     |        |
|        |        |        |      |     |     | atness |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | Me     |        |
|        |        |        |      |     |     | diaTek |        |
|        |        |        |      |     |     | Inc.   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907429 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Intel  |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907434 |        |
|        |        |        |      |     |     | \[Rx\  |        |
|        |        |        |      |     |     | ]Draft |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | mod    |        |
|        |        |        |      |     |     | ifying |        |
|        |        |        |      |     |     | cha    |        |
|        |        |        |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | fering |        |
|        |        |        |      |     |     | signal |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | D      |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907435 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS38.1 |        |
|        |        |        |      |     |     | 01-1\_ |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | n41C   |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on Rx  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA ZTE |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907439 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on CA  |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907471 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | all RB |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | so     |        |
|        |        |        |      |     |     | transm |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | BW     |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | pplies |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | all    |        |
|        |        |        |      |     |     | SCS    |        |
|        |        |        |      |     |     | Qu     |        |
|        |        |        |      |     |     | alcomm |        |
|        |        |        |      |     |     | Incorp |        |
|        |        |        |      |     |     | orated |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907474 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | set    |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Huawei |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907477 |        |
|        |        |        |      |     |     | Draft  |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | aggr   |        |
|        |        |        |      |     |     | egated |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | ZTE    |        |
|        |        |        |      |     |     | Corpo  |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907481 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | efSens |        |
|        |        |        |      |     |     | exce   |        |
|        |        |        |      |     |     | ptions |        |
|        |        |        |      |     |     | due to |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | ha     |        |
|        |        |        |      |     |     | rmonic |        |
|        |        |        |      |     |     | interf |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA in  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | vivo   |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 907687 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to CA  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pacing |        |
|        |        |        |      |     |     | Er     |        |
|        |        |        |      |     |     | icsson |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0037 | 1   | B   | Introd | 16.0.0 |
| 019-06 | AN\#84 | 191248 |      |     |     | uction |        |
|        |        |        |      |     |     | of n48 |        |
|        |        |        |      |     |     | in to  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0040 |     | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191241 |      |     |     | REL-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs on |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | dual   |        |
|        |        |        |      |     |     | Connec |        |
|        |        |        |      |     |     | tivity |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0041 | 1   | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191242 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n14 -- |        |
|        |        |        |      |     |     | En     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 904008 |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | RAN    |        |
|        |        |        |      |     |     | 4\#90b |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0042 | 1   | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191246 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n30 +  |        |
|        |        |        |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | 7      |        |
|        |        |        |      |     |     | .6.2-2 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0043 | 1   | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191244 |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | n18 to |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0044 | 1   | B   | n65    | 16.0.0 |
| 019-06 | AN\#84 | 191250 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0045 |     | B   | Ad     | 16.0.0 |
| 019-06 | AN\#84 | 191251 |      |     |     | dition |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | 30MHz  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50 in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0046 | 1   | B   | Introd | 16.0.0 |
| 019-06 | AN\#84 | 191252 |      |     |     | uction |        |
|        |        |        |      |     |     | of a   |        |
|        |        |        |      |     |     | new NR |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | LTE/NR |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | haring |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | 41/n41 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0048 |     | B   | CR on  | 16.0.0 |
| 019-06 | AN\#84 | 191241 |      |     |     | intro  |        |
|        |        |        |      |     |     | ducing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA of  |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 1UL    |        |
|        |        |        |      |     |     | band   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0049 |     | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191241 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA/DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0050 |     | B   | CR to  | 16.0.0 |
| 019-06 | AN\#84 | 191241 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA/DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 3  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with 2 |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0051 |     | B   | CR     | 16.0.0 |
| 019-06 | AN\#84 | 191241 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0052 |     | F   | Corr   | 16.1.0 |
| 019-09 | AN\#85 | 192038 |      |     |     | ection |        |
|        |        |        |      |     |     | to FR1 |        |
|        |        |        |      |     |     | ASEM   |        |
|        |        |        |      |     |     | NS\_27 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0053 |     | B   | Ad     | 16.1.0 |
| 019-09 | AN\#85 | 192032 |      |     |     | dition |        |
|        |        |        |      |     |     | of NS  |        |
|        |        |        |      |     |     | infor  |        |
|        |        |        |      |     |     | mation |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | 30MHz  |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n41    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0054 | 1   | B   | Ad     | 16.1.0 |
| 019-09 | AN\#85 | 192031 |      |     |     | dition |        |
|        |        |        |      |     |     | of new |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | widths |        |
|        |        |        |      |     |     | for n7 |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0055 |     | B   | CR on  | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | intro  |        |
|        |        |        |      |     |     | ducing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA for |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 1UL    |        |
|        |        |        |      |     |     | band   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0057 | 1   | F   | Minor  | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0058 | 1   | F   | Adding | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | De     |        |
|        |        |        |      |     |     | ltaFHD |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | n1-n77 |        |
|        |        |        |      |     |     | refe   |        |
|        |        |        |      |     |     | rsense |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rments |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0060 |     | B   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192032 |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | 30MHz  |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | of n41 |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0061 | 1   | B   | Cha    | 16.1.0 |
| 019-09 | AN\#85 | 192026 |      |     |     | racter |        |
|        |        |        |      |     |     | istics |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Inter  |        |
|        |        |        |      |     |     | fering |        |
|        |        |        |      |     |     | signal |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | Intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Class  |        |
|        |        |        |      |     |     | B      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0062 | 1   | F   | Corr   | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | ection |        |
|        |        |        |      |     |     | Inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0063 | 1   | F   | Fina   | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | lizing |        |
|        |        |        |      |     |     | G      |        |
|        |        |        |      |     |     | eneric |        |
|        |        |        |      |     |     | Intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | Cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | Class  |        |
|        |        |        |      |     |     | B      |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0064 | 1   | B   | n29    | 16.1.0 |
| 019-09 | AN\#85 | 192034 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 38.101 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0065 |     | F   | \      | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | [SUL\] |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0066 |     | B   | CR on  | 16.1.0 |
| 019-09 | AN\#85 | 192029 |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of SUL |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n89    |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0068 | 2   | F   | Corr   | 16.1.0 |
| 019-09 | AN\#85 | 192046 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n66    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0070 | 1   | F   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192026 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
|        |        |        |      |     |     | Revamp |        |
|        |        |        |      |     |     | CA ACS |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | IBB    |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | iffere |        |
|        |        |        |      |     |     | ntiate |        |
|        |        |        |      |     |     | by     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | umbers |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0071 |     | F   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192038 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
|        |        |        |      |     |     | Add    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | NS27   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0072 |     | B   | CR for | 16.1.0 |
| 019-09 | AN\#85 | 192026 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rx     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0073 |     | F   | CR for | 16.1.0 |
| 019-09 | AN\#85 | 192036 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to the |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | Em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | Coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n14    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0074 |     | F   | CR for | 16.1.0 |
| 019-09 | AN\#85 | 192037 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to the |        |
|        |        |        |      |     |     | Sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | Em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | Coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n30    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0075 |     | B   | CR     | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0076 |     | B   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 2  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | up to  |        |
|        |        |        |      |     |     | 2      |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0077 |     | B   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192027 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 3  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with 2 |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0079 |     | A   | CR to  | 16.1.0 |
| 019-09 | AN\#85 | 192049 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | en     |        |
|        |        |        |      |     |     | dorsed |        |
|        |        |        |      |     |     | draft  |        |
|        |        |        |      |     |     | CRs    |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | RA     |        |
|        |        |        |      |     |     | N4\#92 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | \-     |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | irrors |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hanges |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | R4-1   |        |
|        |        |        |      |     |     | 910350 |        |
|        |        |        |      |     |     | (of    |        |
|        |        |        |      |     |     | RAN    |        |
|        |        |        |      |     |     | 4\#92) |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Rel-15 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0097 |     | F   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193022 |      |     |     | align  |        |
|        |        |        |      |     |     | NS27   |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | NS\_10 |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 40MHz  |        |
|        |        |        |      |     |     | BW at  |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | center |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | 48.    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0099 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | RX     |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-Band |        |
|        |        |        |      |     |     | Bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | B38    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | B41    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0103 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | n39    |        |
|        |        |        |      |     |     | AMPR   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0105 | 1   | B   | Introd | 16.2.0 |
| 019-12 | AN\#86 | 193013 |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | 2010-2 |        |
|        |        |        |      |     |     | 025MHz |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0110 |     | B   | Ad     | 16.2.0 |
| 019-12 | AN\#86 | 193015 |      |     |     | dition |        |
|        |        |        |      |     |     | of 25, |        |
|        |        |        |      |     |     | 30 and |        |
|        |        |        |      |     |     | 40 MHz |        |
|        |        |        |      |     |     | to NR  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n25 in |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0112 |     | A   | Sync   | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | raster |        |
|        |        |        |      |     |     | to SSB |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | source |        |
|        |        |        |      |     |     | e      |        |
|        |        |        |      |     |     | lement |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | apping |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0114 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0118 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | terval |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | obser  |        |
|        |        |        |      |     |     | vation |        |
|        |        |        |      |     |     | window |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | error  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0119 |     | D   | Format | 16.2.0 |
| 019-12 | AN\#86 | 193020 |      |     |     | misali |        |
|        |        |        |      |     |     | gnment |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | NS\_47 |        |
|        |        |        |      |     |     | prot   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | table  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0121 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | eplace |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ymbols |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | efined |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pecifi |        |
|        |        |        |      |     |     | cation |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0124 |     | B   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 2  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | up to  |        |
|        |        |        |      |     |     | 2      |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0125 |     | B   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 3  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with 2 |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0126 |     | F   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | remove |        |
|        |        |        |      |     |     | square |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n90 in |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0128 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0132 |     | B   | Intro  | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | ducing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA for |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 1UL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0133 |     | B   | Adding | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | band   |        |
|        |        |        |      |     |     | n71    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n28 to |        |
|        |        |        |      |     |     | 4 Rx   |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ntenna |        |
|        |        |        |      |     |     | ports  |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0137 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for n2 |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | index  |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 7      |        |
|        |        |        |      |     |     | .3.2-3 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0138 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0140 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Re     |        |
|        |        |        |      |     |     | moving |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 77D/E, |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 78D/E, |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | n79D/E |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0144 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Fix    |        |
|        |        |        |      |     |     | out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | issue  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n75    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0146 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | raster |        |
|        |        |        |      |     |     | e      |        |
|        |        |        |      |     |     | ntries |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0150 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | tr     |        |
|        |        |        |      |     |     | ansmit |        |
|        |        |        |      |     |     | modu   |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | q      |        |
|        |        |        |      |     |     | uality |        |
|        |        |        |      |     |     | in FR1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0151 |     | F   | Corre  | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | ctions |        |
|        |        |        |      |     |     | Intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | TX/RX  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0153 |     | F   | R      | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ciever |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | REL-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0155 |     | B   | Ext    | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | ension |        |
|        |        |        |      |     |     | of CA  |        |
|        |        |        |      |     |     | BW     |        |
|        |        |        |      |     |     | class  |        |
|        |        |        |      |     |     | B      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0157 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of UL  |        |
|        |        |        |      |     |     | RMCs   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0164 |     | B   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combi  |        |
|        |        |        |      |     |     | nation |        |
|        |        |        |      |     |     | CA\    |        |
|        |        |        |      |     |     | _n78(2 |        |
|        |        |        |      |     |     | A)\_SU |        |
|        |        |        |      |     |     | L\_n78 |        |
|        |        |        |      |     |     | A-n86A |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0165 |     | F   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193010 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | add    |        |
|        |        |        |      |     |     | BCS1   |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 78(2A) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0166 |     | B   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193017 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | - Band |        |
|        |        |        |      |     |     | n75 -  |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | CBW    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0167 |     | B   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193018 |      |     |     | TS     |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101: |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | widths |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0168 |     | B   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193016 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n38    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0169 |     | B   | CR     | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0170 |     | B   | CR     | 16.2.0 |
| 019-12 | AN\#86 | 193012 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -04-01 |        |
|        |        |        |      |     |     | -\>    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0171 |     | C   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193021 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Making |        |
|        |        |        |      |     |     | 90 MHz |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | man    |        |
|        |        |        |      |     |     | datory |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n41,   |        |
|        |        |        |      |     |     | n78    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n90    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0172 |     | B   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193020 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | 30 MHz |        |
|        |        |        |      |     |     | CHBW   |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | NS\_04 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n41    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0174 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | 38.101 |        |
|        |        |        |      |     |     | -1-g10 |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Tra    |        |
|        |        |        |      |     |     | nsient |        |
|        |        |        |      |     |     | Time   |        |
|        |        |        |      |     |     | Masks  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0176 | 1   | F   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193010 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA RF  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0179 |     | B   | Introd | 16.2.0 |
| 019-12 | AN\#86 | 193010 |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | PC2    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0180 |     | A   | CR for | 16.2.0 |
| 019-12 | AN\#86 | 193029 |      |     |     | asynch |        |
|        |        |        |      |     |     | ronous |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | 78-n79 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0182 |     | A   | CR to  | 16.2.0 |
| 019-12 | AN\#86 | 193028 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | DMRS   |        |
|        |        |        |      |     |     | Exce   |        |
|        |        |        |      |     |     | ptions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0191 |     | F   | Corre  | 16.3.0 |
| 020-03 | AN\#87 | 200408 |      |     |     | ctions |        |
|        |        |        |      |     |     | to n65 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0201 | 1   | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200377 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | BCS1   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n77C |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n78C |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0203 |     | A   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | etwork |        |
|        |        |        |      |     |     | sign   |        |
|        |        |        |      |     |     | alling |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0208 |     | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200484 |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | n39 NS |        |
|        |        |        |      |     |     | flag   |        |
|        |        |        |      |     |     | change |        |
|        |        |        |      |     |     | due to |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nflict |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0210 |     | A   | Mirror | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | CR for |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n25    |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0211 | 2   | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | tables |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0212 |     | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200387 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | 70 MHz |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_01 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0215 |     | B   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200381 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of n26 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0216 |     | F   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on MSD |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 20-n78 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 66-n78 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0218 |     | A   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on ACS |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0219 | 1   | F   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Impro  |        |
|        |        |        |      |     |     | vement |        |
|        |        |        |      |     |     | on NR  |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | combi  |        |
|        |        |        |      |     |     | nation |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0221 |     | A   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | eplace |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ymbols |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | efined |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ecific |        |
|        |        |        |      |     |     | ation. |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | NOTE:  |        |
|        |        |        |      |     |     | The CR |        |
|        |        |        |      |     |     | is     |        |
|        |        |        |      |     |     | based  |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | som    |        |
|        |        |        |      |     |     | ething |        |
|        |        |        |      |     |     | else   |        |
|        |        |        |      |     |     | than   |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | latest |        |
|        |        |        |      |     |     | v      |        |
|        |        |        |      |     |     | ersion |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pecifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | refore |        |
|        |        |        |      |     |     | it is  |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | implem |        |
|        |        |        |      |     |     | ented, |        |
|        |        |        |      |     |     | e.g.   |        |
|        |        |        |      |     |     | Tables |        |
|        |        |        |      |     |     | 6.2.   |        |
|        |        |        |      |     |     | 3.1-1, |        |
|        |        |        |      |     |     | 7      |        |
|        |        |        |      |     |     | .6.2-2 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 7      |        |
|        |        |        |      |     |     | .6.2-4 |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | CR0221 |        |
|        |        |        |      |     |     | are    |        |
|        |        |        |      |     |     | dif    |        |
|        |        |        |      |     |     | ferent |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | mpared |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | those  |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | v1     |        |
|        |        |        |      |     |     | 6.2.0. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0222 |     | B   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 2  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | up to  |        |
|        |        |        |      |     |     | 2      |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0223 |     | B   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 3  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with 2 |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0224 | 1   | B   | Introd | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | uction |        |
|        |        |        |      |     |     | of n53 |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0229 |     | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Remove |        |
|        |        |        |      |     |     | notes  |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0231 |     | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of IE  |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | F-Para |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | name   |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | maxUpl |        |
|        |        |        |      |     |     | inkDut |        |
|        |        |        |      |     |     | yCycle |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0234 | 1   | B   | Intro  | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | ducing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA for |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 1UL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0239 | 1   | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200377 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n48    |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0240 | 1   | B   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200386 |      |     |     | TS     |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101: |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | widths |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n66    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0241 | 1   | F   | Maint  | 16.3.0 |
| 020-03 | AN\#87 | 200392 |      |     |     | enance |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | UE BW  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n92    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n94    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0242 |     | F   | Maint  | 16.3.0 |
| 020-03 | AN\#87 | 200392 |      |     |     | enance |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | Rx-Tx  |        |
|        |        |        |      |     |     | sepa   |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | terms  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0244 |     | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | remove |        |
|        |        |        |      |     |     | fa     |        |
|        |        |        |      |     |     | llback |        |
|        |        |        |      |     |     | group  |        |
|        |        |        |      |     |     | 1 in   |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | 5.     |        |
|        |        |        |      |     |     | 5A.1-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0247 |     | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200389 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | CA\_n8 |        |
|        |        |        |      |     |     | A-n75A |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0249 | 1   | B   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200384 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | UE RF  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n28    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0250 | 1   | B   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200383 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n1 -   |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | CBW -  |        |
|        |        |        |      |     |     | Addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | BW     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0252 | 1   | B   | CR to  | 16.3.0 |
| 020-03 | AN\#87 | 200385 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n38 -  |        |
|        |        |        |      |     |     | wider  |        |
|        |        |        |      |     |     | CBW -  |        |
|        |        |        |      |     |     | Addi   |        |
|        |        |        |      |     |     | tional |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | BW     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0260 | 1   | F   | Edi    | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0263 |     | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200377 |      |     |     | a      |        |
|        |        |        |      |     |     | lomost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | allo   |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0265 | 1   | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA Tx  |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0266 | 1   | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200377 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | and DL |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0273 |     | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200391 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Man    |        |
|        |        |        |      |     |     | datory |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n41 by |        |
|        |        |        |      |     |     | UEs    |        |
|        |        |        |      |     |     | that   |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | n90    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0275 |     | A   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | \[ag   |        |
|        |        |        |      |     |     | reed\] |        |
|        |        |        |      |     |     | asynch |        |
|        |        |        |      |     |     | ronous |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | 78-n79 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | NOTE:  |        |
|        |        |        |      |     |     | The CR |        |
|        |        |        |      |     |     | is     |        |
|        |        |        |      |     |     | based  |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | som    |        |
|        |        |        |      |     |     | ething |        |
|        |        |        |      |     |     | else   |        |
|        |        |        |      |     |     | than   |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | latest |        |
|        |        |        |      |     |     | v      |        |
|        |        |        |      |     |     | ersion |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pecifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | refore |        |
|        |        |        |      |     |     | it is  |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | implem |        |
|        |        |        |      |     |     | ented, |        |
|        |        |        |      |     |     | e.g.   |        |
|        |        |        |      |     |     | Tables |        |
|        |        |        |      |     |     | 6      |        |
|        |        |        |      |     |     | .2A.4. |        |
|        |        |        |      |     |     | 2.3-1, |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 7.3    |        |
|        |        |        |      |     |     | A.6-1, |        |
|        |        |        |      |     |     | 7.     |        |
|        |        |        |      |     |     | 3A.6.2 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | notes  |        |
|        |        |        |      |     |     | are    |        |
|        |        |        |      |     |     | dif    |        |
|        |        |        |      |     |     | ferent |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | mpared |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | those  |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | v1     |        |
|        |        |        |      |     |     | 6.2.0. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0280 |     | F   | CR for | 16.3.0 |
| 020-03 | AN\#87 | 200380 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | delta  |        |
|        |        |        |      |     |     | Tib    |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0281 |     | A   | R      | 16.3.0 |
| 020-03 | AN\#87 | 200394 |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | unnec  |        |
|        |        |        |      |     |     | essary |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | offs   |        |
|        |        |        |      |     |     | et~max |        |
|        |        |        |      |     |     | ,IMD3~ |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | Table  |        |
|        |        |        |      |     |     | 6.2    |        |
|        |        |        |      |     |     | .3.2-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0293 | 4   | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 201338 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | time   |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | etween |        |
|        |        |        |      |     |     | two    |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | ca     |        |
|        |        |        |      |     |     | rriers |        |
|        |        |        |      |     |     | in UL  |        |
|        |        |        |      |     |     | CA and |        |
|        |        |        |      |     |     | SUL    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0294 |     | F   | Corre  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | ctions |        |
|        |        |        |      |     |     | to CA  |        |
|        |        |        |      |     |     | n48    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0300 |     | A   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | asym   |        |
|        |        |        |      |     |     | metric |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | in FR1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0302 |     | A   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | ACLR   |        |
|        |        |        |      |     |     | MBW    |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | in FR1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0305 |     | B   | Intro  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | ducing |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA for |        |
|        |        |        |      |     |     | 3DL    |        |
|        |        |        |      |     |     | Bands  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 1UL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0307 |     | F   | CR     | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | Coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0310 |     | A   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | R16:   |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on ACS |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0311 |     | F   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200966 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | ha     |        |
|        |        |        |      |     |     | rmonic |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | OOBB   |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0315 |     | F   | Update | 16.4.0 |
| 020-06 | AN\#88 | 200981 |      |     |     | 4Rx    |        |
|        |        |        |      |     |     | Requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n30    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0317 |     | B   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 200958 |      |     |     | NR V2X |        |
|        |        |        |      |     |     | UE RF  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | single |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0327 |     | A   | Maint  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | enance |        |
|        |        |        |      |     |     | CR to  |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | lative |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | tol    |        |
|        |        |        |      |     |     | erance |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0329 |     | F   | En     | 16.4.0 |
| 020-06 | AN\#88 | 200974 |      |     |     | dorsed |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | efault |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | sig    |        |
|        |        |        |      |     |     | naling |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n91    |        |
|        |        |        |      |     |     | n92    |        |
|        |        |        |      |     |     | n93    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n94    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0331 |     | A   | Update | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | of     |        |
|        |        |        |      |     |     | CSI-RS |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 DL |        |
|        |        |        |      |     |     | RMCs   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0335 |     | A   | Corr   | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | ection |        |
|        |        |        |      |     |     | to FR1 |        |
|        |        |        |      |     |     | QPSK   |        |
|        |        |        |      |     |     | UL RMC |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0336 |     | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200966 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | DC(C   |        |
|        |        |        |      |     |     | lauses |        |
|        |        |        |      |     |     | 3      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0338 |     | A   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | ominal |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | pacing |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0340 |     | A   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | eplace |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ymbols |        |
|        |        |        |      |     |     | d      |        |
|        |        |        |      |     |     | efined |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ecific |        |
|        |        |        |      |     |     | ation. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0341 |     | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 2  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | up to  |        |
|        |        |        |      |     |     | 2      |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0345 |     | A   | 30k    | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | SSB    |        |
|        |        |        |      |     |     | SCS    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0347 |     | A   | Ad     | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | dition |        |
|        |        |        |      |     |     | of 30k |        |
|        |        |        |      |     |     | SSB    |        |
|        |        |        |      |     |     | SCS    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n38    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0354 |     | A   | IBE    | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | measur |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | haping |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0357 |     | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | r      |        |
|        |        |        |      |     |     | eflect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for 3  |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | DL     |        |
|        |        |        |      |     |     | with 2 |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0360 |     | B   | CR     | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -01-01 |        |
|        |        |        |      |     |     | -      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0361 |     | B   | CR     | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | 38.716 |        |
|        |        |        |      |     |     | -04-01 |        |
|        |        |        |      |     |     | -      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0364 |     | B   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | com    |        |
|        |        |        |      |     |     | pleted |        |
|        |        |        |      |     |     | SUL    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0365 |     | F   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 201045 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | BCS2   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n7 |        |
|        |        |        |      |     |     | 8(2A). |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0367 |     | A   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | remove |        |
|        |        |        |      |     |     | the NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
|        |        |        |      |     |     | due to |        |
|        |        |        |      |     |     | cross  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | iso    |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | for CA |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | mirror |        |
|        |        |        |      |     |     | CR)    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0369 |     | A   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to add |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inter  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | SDL    |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | mirror |        |
|        |        |        |      |     |     | CR)    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0373 |     | F   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 200979 |      |     |     | int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | del    |        |
|        |        |        |      |     |     | ta-MPR |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA in  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n28    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | review |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0379 |     | A   | IBE    | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | alloc  |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0385 |     | A   | OOB    | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n70    |        |
|        |        |        |      |     |     | ad     |        |
|        |        |        |      |     |     | jacent |        |
|        |        |        |      |     |     | to n25 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0394 |     | F   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0396 |     | F   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | RFC    |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0400 |     | A   | TS38   | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | .101-1 |        |
|        |        |        |      |     |     | CR on  |        |
|        |        |        |      |     |     | 30KHz  |        |
|        |        |        |      |     |     | SSB    |        |
|        |        |        |      |     |     | SCS    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n40(R  |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0318 | 1   | F   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200959 |      |     |     | add    |        |
|        |        |        |      |     |     | simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | RXTX   |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 41-n79 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0404 |     | A   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | to add |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | sub-   |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | title  |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0343 | 1   | A   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | \[ag   |        |
|        |        |        |      |     |     | reed\] |        |
|        |        |        |      |     |     | asynch |        |
|        |        |        |      |     |     | ronous |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | n      |        |
|        |        |        |      |     |     | 78-n79 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0387 | 1   | B   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 201045 |      |     |     | FR1 UL |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0325 | 1   | F   | CR on  | 16.4.0 |
| 020-06 | AN\#88 | 200974 |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n91    |        |
|        |        |        |      |     |     | n92    |        |
|        |        |        |      |     |     | n93    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n94    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0380 | 1   | B   | Ad     | 16.4.0 |
| 020-06 | AN\#88 | 201045 |      |     |     | dition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | mutual |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | etween |        |
|        |        |        |      |     |     | US     |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | and NR |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n77    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0356 | 1   | B   | CR for | 16.4.0 |
| 020-06 | AN\#88 | 200977 |      |     |     | TS     |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101: |        |
|        |        |        |      |     |     | adding |        |
|        |        |        |      |     |     | 50 MHz |        |
|        |        |        |      |     |     | CBW    |        |
|        |        |        |      |     |     | for n1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0358 | 1   | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200980 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | - Add  |        |
|        |        |        |      |     |     | 40 MHz |        |
|        |        |        |      |     |     | CBW in |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n3     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0359 | 1   | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200982 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | - Add  |        |
|        |        |        |      |     |     | 50 MHz |        |
|        |        |        |      |     |     | CBW in |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n65    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0405 |     | F   | Corre  | 16.4.0 |
| 020-06 | AN\#88 | 200985 |      |     |     | ctions |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | J      |        |
|        |        |        |      |     |     | apan-r |        |
|        |        |        |      |     |     | elated |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0320 | 2   | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 201045 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Int    |        |
|        |        |        |      |     |     | roduce |        |
|        |        |        |      |     |     | an     |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | rating |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | list   |        |
|        |        |        |      |     |     | and NR |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | to UL  |        |
|        |        |        |      |     |     | MIMO   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0362 | 1   | B   | CR to  | 16.4.0 |
| 020-06 | AN\#88 | 200966 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NR-DC  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0407 | 1   | F   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | ection |        |
|        |        |        |      |     |     | to FR1 |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA MPR |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | egions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0409 |     | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201506 |      |     |     | n26    |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 256QAM |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0411 |     | A   | OOB    | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0416 | 1   | F   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | ASEM   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_27 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0419 |     | F   | Introd | 16.5.0 |
| 020-09 | AN\#89 | 201507 |      |     |     | uction |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | PC2    |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n40    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0422 | 1   | B   | Introd | 16.5.0 |
| 020-09 | AN\#89 | 201502 |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | LTE/NR |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | haring |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | 48/n48 |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | range  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0423 |     | F   | Coexi  | 16.5.0 |
| 020-09 | AN\#89 | 201507 |      |     |     | stence |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0424 |     | D   | CR     | 16.5.0 |
| 020-09 | AN\#89 | 201506 |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combi  |        |
|        |        |        |      |     |     | nation |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0426 |     | A   | CR to  | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | narrow |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0428 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201492 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | 6.5E.3 |        |
|        |        |        |      |     |     | .4.3-1 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | 6.5E.3 |        |
|        |        |        |      |     |     | .4.3-2 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0432 | 1   | B   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201503 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Power  |        |
|        |        |        |      |     |     | Class  |        |
|        |        |        |      |     |     | 1.5    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0433 | 1   | B   | CR to  | 16.5.0 |
| 020-09 | AN\#89 | 201488 |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Uplink |        |
|        |        |        |      |     |     | Full   |        |
|        |        |        |      |     |     | Power  |        |
|        |        |        |      |     |     | Transm |        |
|        |        |        |      |     |     | ission |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0435 |     | A   | Corre  | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | ctions |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | J      |        |
|        |        |        |      |     |     | apan-r |        |
|        |        |        |      |     |     | elated |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | tables |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | REL-15 |        |
|        |        |        |      |     |     | combo  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0437 | 1   | F   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201492 |      |     |     | ection |        |
|        |        |        |      |     |     | on 5G  |        |
|        |        |        |      |     |     | V2X UE |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0438 | 2   | B   | A-MPR  | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\    |        |
|        |        |        |      |     |     | _n48B, |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n41B |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n41C |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0439 |     | F   | CR     | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | Res    |        |
|        |        |        |      |     |     | toring |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | str    |        |
|        |        |        |      |     |     | ucture |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | raband |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0440 | 1   | F   | CR on  | 16.5.0 |
| 020-09 | AN\#89 | 201492 |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | V2X    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0442 |     | A   | 30k    | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | SSB    |        |
|        |        |        |      |     |     | SCS    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n34    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n39    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0444 |     | F   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | ection |        |
|        |        |        |      |     |     | for 5  |        |
|        |        |        |      |     |     | MHz    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n50    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Annex  |        |
|        |        |        |      |     |     | H      |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0458 |     | A   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | FRC    |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0459 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201506 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | remove |        |
|        |        |        |      |     |     | PHS    |        |
|        |        |        |      |     |     | system |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | 86     |        |
|        |        |        |      |     |     | 0\~890 |        |
|        |        |        |      |     |     | prot   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combi  |        |
|        |        |        |      |     |     | nation |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n1 and |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n8     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0460 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201506 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to add |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | region |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_18 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | ?mprc  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0462 |     | A   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to add |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | A\_n41 |        |
|        |        |        |      |     |     | A-n78A |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0465 |     | A   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | all    |        |
|        |        |        |      |     |     | owance |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SRS    |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0466 |     | B   | Int    | 16.5.0 |
| 020-09 | AN\#89 | 202117 |      |     |     | roduce |        |
|        |        |        |      |     |     | UE     |        |
|        |        |        |      |     |     | NR-U   |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | inc    |        |
|        |        |        |      |     |     | luding |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n46 (5 |        |
|        |        |        |      |     |     | GHz)   |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n96 (6 |        |
|        |        |        |      |     |     | GHz)   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0468 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0469 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0470 | 1   | F   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | lo     |        |
|        |        |        |      |     |     | cation |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0471 | 1   | B   | CR for | 16.5.0 |
| 020-09 | AN\#89 | 201495 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0480 | 1   | F   | CR to  | 16.5.0 |
| 020-09 | AN\#89 | 201507 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | -      |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to CA  |        |
|        |        |        |      |     |     | BCS    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | cross  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | iso    |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | tables |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0483 |     | A   | Corr   | 16.5.0 |
| 020-09 | AN\#89 | 201512 |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of 2Rx |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0486 | 2   | B   | CR to  | 16.5.0 |
| 020-09 | AN\#89 | 201488 |      |     |     | add    |        |
|        |        |        |      |     |     | PC3    |        |
|        |        |        |      |     |     | Pi/2   |        |
|        |        |        |      |     |     | BPSK   |        |
|        |        |        |      |     |     | DMRS   |        |
|        |        |        |      |     |     | for IE |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | BoostP |        |
|        |        |        |      |     |     | i2BPSK |        |
|        |        |        |      |     |     | = 0    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0499 | 1   | C   | 7.5    | 16.5.0 |
| 020-09 | AN\#89 | 202098 |      |     |     | kHz UL |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | LTE/NR |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | haring |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | 38/n38 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0492 | 1   | F   | CR     | 16.6.0 |
| 020-12 | AN\#90 | 202440 |      |     |     | CatF   |        |
|        |        |        |      |     |     | n7     |        |
|        |        |        |      |     |     | NS\_46 |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | coexi  |        |
|        |        |        |      |     |     | stence |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0498 | 1   | F   | Corr   | 16.6.0 |
| 020-12 | AN\#90 | 202427 |      |     |     | ection |        |
|        |        |        |      |     |     | on 5G  |        |
|        |        |        |      |     |     | V2X UE |        |
|        |        |        |      |     |     | RF     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0506 |     | F   | n53    | 16.6.0 |
| 020-12 | AN\#90 | 202438 |      |     |     | b      |        |
|        |        |        |      |     |     | racket |        |
|        |        |        |      |     |     | r      |        |
|        |        |        |      |     |     | emoval |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0507 | 2   | F   | A-MPR  | 16.6.0 |
| 020-12 | AN\#90 | 202442 |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n7B, |        |
|        |        |        |      |     |     | CA\    |        |
|        |        |        |      |     |     | _n48B, |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n41B |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_n41C |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0512 |     | A   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on DC  |        |
|        |        |        |      |     |     | lo     |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0518 |     | F   | Coexi  | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | stence |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0524 | 1   | F   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | si     |        |
|        |        |        |      |     |     | mplifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0525 |     | F   | CR on  | 16.6.0 |
| 020-12 | AN\#90 | 202427 |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | V2X    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0527 |     | A   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.1   |        |
|        |        |        |      |     |     | 01-1\[ |        |
|        |        |        |      |     |     | R16\]: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | non-   |        |
|        |        |        |      |     |     | simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | Rx/Tx  |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 77-n79 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 78-n79 |        |
|        |        |        |      |     |     | in TS  |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0533 | 1   | F   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202442 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Add    |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | no DL  |        |
|        |        |        |      |     |     | interr |        |
|        |        |        |      |     |     | uption |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0534 |     | F   | Edi    | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | torial |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 5.2C   |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0535 | 1   | F   | CR on  | 16.6.0 |
| 020-12 | AN\#90 | 202427 |      |     |     | V2X    |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | table  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0536 | 1   | F   | CR on  | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | sum of |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | mu     |        |
|        |        |        |      |     |     | ltiple |        |
|        |        |        |      |     |     | tr     |        |
|        |        |        |      |     |     | ansmit |        |
|        |        |        |      |     |     | conn   |        |
|        |        |        |      |     |     | ectors |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0540 |     | F   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202428 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | of SUL |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | order  |        |
|        |        |        |      |     |     | to be  |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ligned |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-3 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0542 |     | A   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | adjust |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | str    |        |
|        |        |        |      |     |     | ucture |        |
|        |        |        |      |     |     | of NR  |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0544 |     | F   | Ref    | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | erence |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | ch     |        |
|        |        |        |      |     |     | annels |        |
|        |        |        |      |     |     | for 70 |        |
|        |        |        |      |     |     | MHz    |        |
|        |        |        |      |     |     | CBW    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0547 |     | F   | Corr   | 16.6.0 |
| 020-12 | AN\#90 | 202428 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | sup    |        |
|        |        |        |      |     |     | ported |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | widths |        |
|        |        |        |      |     |     | per    |        |
|        |        |        |      |     |     | SU     |        |
|        |        |        |      |     |     | L\_n41 |        |
|        |        |        |      |     |     | A-n81A |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0550 | 3   | F   | Corr   | 16.6.0 |
| 020-12 | AN\#90 | 202414 |      |     |     | ection |        |
|        |        |        |      |     |     | to the |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-cell |        |
|        |        |        |      |     |     | guard  |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | wi     |        |
|        |        |        |      |     |     | deband |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0552 | 1   | F   | Corr   | 16.6.0 |
| 020-12 | AN\#90 | 202414 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | shared |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | access |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0556 |     | F   | CR     | 16.6.0 |
| 020-12 | AN\#90 | 202442 |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | NS\_27 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | 10     |        |
|        |        |        |      |     |     | prot   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | 3      |        |
|        |        |        |      |     |     | 8101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0557 | 1   | F   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202428 |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0558 | 2   | F   | R      | 16.6.0 |
| 020-12 | AN\#90 | 202414 |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | square |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | NR-U   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0562 |     | F   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | for    |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0563 |     | D   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202509 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0566 | 1   | F   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202427 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | NR V2X |        |
|        |        |        |      |     |     | FRC    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0571 |     | A   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | delta  |        |
|        |        |        |      |     |     | Tib    |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | supp   |        |
|        |        |        |      |     |     | orting |        |
|        |        |        |      |     |     | mu     |        |
|        |        |        |      |     |     | ltiple |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0574 | 1   | B   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202442 |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0581 |     | A   | CR for | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | AMPR-  |        |
|        |        |        |      |     |     | Rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0584 |     | A   | CR to  | 16.6.0 |
| 020-12 | AN\#90 | 202485 |      |     |     | DMRS   |        |
|        |        |        |      |     |     | po     |        |
|        |        |        |      |     |     | sition |        |
|        |        |        |      |     |     | in UL  |        |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0588 | 2   | F   | PC1    | 16.7.0 |
| 021-03 | AN\#91 | 210190 |      |     |     | and    |        |
|        |        |        |      |     |     | PC3    |        |
|        |        |        |      |     |     | U      |        |
|        |        |        |      |     |     | pdates |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n14    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0593 | 1   | F   | 38.101 | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | Void   |        |
|        |        |        |      |     |     | clean  |        |
|        |        |        |      |     |     | up R16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0600 |     | F   | CA     | 16.7.0 |
| 021-03 | AN\#91 | 210082 |      |     |     | \_n7B\ |        |
|        |        |        |      |     |     | _REFSE |        |
|        |        |        |      |     |     | NS\_Ca |        |
|        |        |        |      |     |     | tF\_CR |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0605 | 1   | F   | CR on  | 16.7.0 |
| 021-03 | AN\#91 | 210072 |      |     |     | edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on V2X |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0611 |     | A   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS38   |        |
|        |        |        |      |     |     | 101-1  |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | P-MPR  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0613 | 2   | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS38   |        |
|        |        |        |      |     |     | 101-1  |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | delta  |        |
|        |        |        |      |     |     | MPR    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0629 |     | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210082 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | 1      |        |
|        |        |        |      |     |     | Tx-2Tx |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | etween |        |
|        |        |        |      |     |     | two    |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | ca     |        |
|        |        |        |      |     |     | rriers |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0632 |     | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210091 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Update |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | fa     |        |
|        |        |        |      |     |     | llback |        |
|        |        |        |      |     |     | NR-DC  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | Rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0637 | 1   | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0641 | 1   | B   | CR on  | 16.7.0 |
| 021-03 | AN\#91 | 210091 |      |     |     | introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | horter |        |
|        |        |        |      |     |     | Tra    |        |
|        |        |        |      |     |     | nsient |        |
|        |        |        |      |     |     | Period |        |
|        |        |        |      |     |     | Capa   |        |
|        |        |        |      |     |     | bility |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0659 |     | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210091 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to add |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n38 UE |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0662 | 1   | F   | CR to  | 16.7.0 |
| 021-03 | AN\#91 | 210084 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | system |        |
|        |        |        |      |     |     | para   |        |
|        |        |        |      |     |     | meters |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NR-U   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0664 |     | A   | Si     | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | mplifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of n70 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0668 |     | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210074 |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Add    |        |
|        |        |        |      |     |     | CA\    |        |
|        |        |        |      |     |     | _n25A- |        |
|        |        |        |      |     |     | n41(2A |        |
|        |        |        |      |     |     | )-n71A |        |
|        |        |        |      |     |     | which  |        |
|        |        |        |      |     |     | was    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | im     |        |
|        |        |        |      |     |     | plemen |        |
|        |        |        |      |     |     | tation |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0673 |     | A   | CR to  | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0676 |     | A   | CR to  | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on the |        |
|        |        |        |      |     |     | Aggr   |        |
|        |        |        |      |     |     | egated |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | Ban    |        |
|        |        |        |      |     |     | dwidth |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0678 |     | F   | CR to  | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | requ   |        |
|        |        |        |      |     |     | iremen |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0689 | 1   | D   | M      | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | issing |        |
|        |        |        |      |     |     | parent |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NR-DC  |        |
|        |        |        |      |     |     | PCMAX  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0691 | 1   | F   | Corre  | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | PCMAX  |        |
|        |        |        |      |     |     | for UL |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0698 |     | A   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210117 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to FR1 |        |
|        |        |        |      |     |     | time   |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SRS    |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ntenna |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0700 | 1   | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210082 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL NC  |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0702 |     | F   | CR for | 16.7.0 |
| 021-03 | AN\#91 | 210091 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | leanup |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | emi    |        |
|        |        |        |      |     |     | ssions |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | table  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0710 |     | F   | CR on  | 16.7.0 |
| 021-03 | AN\#91 | 210091 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | NS\_49 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0735 |     | A   | Update | 16.8.0 |
| 021-06 | AN\#92 | 211084 |      |     |     | of FR1 |        |
|        |        |        |      |     |     | UL RMC |        |
|        |        |        |      |     |     | tables |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0737 |     | F   | CR     | 16.8.0 |
| 021-06 | AN\#92 | 211104 |      |     |     | R      |        |
|        |        |        |      |     |     | emoval |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | square |        |
|        |        |        |      |     |     | br     |        |
|        |        |        |      |     |     | ackets |        |
|        |        |        |      |     |     | from   |        |
|        |        |        |      |     |     | n48    |        |
|        |        |        |      |     |     | NS\_27 |        |
|        |        |        |      |     |     | R16    |        |
|        |        |        |      |     |     | CAT F  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0739 | 1   | F   | CR TDD | 16.8.0 |
| 021-06 | AN\#92 | 211114 |      |     |     | Int    |        |
|        |        |        |      |     |     | raband |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | issue  |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0744 | 1   | F   | CR on  | 16.8.0 |
| 021-06 | AN\#92 | 211118 |      |     |     | PC1.5  |        |
|        |        |        |      |     |     | HPUE   |        |
|        |        |        |      |     |     | SAR    |        |
|        |        |        |      |     |     | issue  |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0749 | 1   | F   | CR on  | 16.8.0 |
| 021-06 | AN\#92 | 211102 |      |     |     | sp     |        |
|        |        |        |      |     |     | urious |        |
|        |        |        |      |     |     | em     |        |
|        |        |        |      |     |     | ission |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | etween |        |
|        |        |        |      |     |     | n40    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n41    |        |
|        |        |        |      |     |     | into   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0759 | 1   | F   | Corr   | 16.8.0 |
| 021-06 | AN\#92 | 211080 |      |     |     | ection |        |
|        |        |        |      |     |     | of an  |        |
|        |        |        |      |     |     | im     |        |
|        |        |        |      |     |     | proper |        |
|        |        |        |      |     |     | usage  |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | edge   |        |
|        |        |        |      |     |     | rela   |        |
|        |        |        |      |     |     | xation |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | MOP    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0764 |     | A   | CR to  | 16.8.0 |
| 021-06 | AN\#92 | 211085 |      |     |     | TS38.1 |        |
|        |        |        |      |     |     | 01-1\[ |        |
|        |        |        |      |     |     | R16\]: |        |
|        |        |        |      |     |     | Ad     |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | of UE  |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n40    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0767 |     | F   | Corr   | 16.8.0 |
| 021-06 | AN\#92 | 211115 |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | sup    |        |
|        |        |        |      |     |     | ported |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | hannel |        |
|        |        |        |      |     |     | ban    |        |
|        |        |        |      |     |     | dwidth |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\    |        |
|        |        |        |      |     |     | _n39-n |        |
|        |        |        |      |     |     | 41-n79 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0774 | 1   | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211114 |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | NR     |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA DC  |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 2DL    |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | up to  |        |
|        |        |        |      |     |     | 2      |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | UL     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0778 | 1   | F   | C      | 16.8.0 |
| 021-06 | AN\#92 | 211077 |      |     |     | leanup |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0782 |     | F   | UL     | 16.8.0 |
| 021-06 | AN\#92 | 211105 |      |     |     | MIMO   |        |
|        |        |        |      |     |     | coh    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | for Tx |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | b      |        |
|        |        |        |      |     |     | etween |        |
|        |        |        |      |     |     | two    |        |
|        |        |        |      |     |     | ca     |        |
|        |        |        |      |     |     | rriers |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0785 |     | F   | CR to  | 16.8.0 |
| 021-06 | AN\#92 | 211077 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | due to |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | ceiver |        |
|        |        |        |      |     |     | ha     |        |
|        |        |        |      |     |     | rmonic |        |
|        |        |        |      |     |     | mixing |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | combos |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | n46    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0791 | 1   | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211077 |      |     |     | up     |        |
|        |        |        |      |     |     | dating |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | man    |        |
|        |        |        |      |     |     | datory |        |
|        |        |        |      |     |     | simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | Rx/Tx  |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | NR-CA  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0799 | 1   | F   | Corr   | 16.8.0 |
| 021-06 | AN\#92 | 211077 |      |     |     | ection |        |
|        |        |        |      |     |     | to MPR |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | erving |        |
|        |        |        |      |     |     | cells  |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0801 | 1   | F   | Corre  | 16.8.0 |
| 021-06 | AN\#92 | 211095 |      |     |     | ctions |        |
|        |        |        |      |     |     | to BCS |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n46    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0803 | 1   | F   | A      | 16.8.0 |
| 021-06 | AN\#92 | 211095 |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | shared |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ectrum |        |
|        |        |        |      |     |     | access |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0810 |     | F   | CR to  | 16.8.0 |
| 021-06 | AN\#92 | 211095 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | NR-U   |        |
|        |        |        |      |     |     | 60 MHz |        |
|        |        |        |      |     |     | and 80 |        |
|        |        |        |      |     |     | MHz    |        |
|        |        |        |      |     |     | ch     |        |
|        |        |        |      |     |     | annels |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0813 |     | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211086 |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | some   |        |
|        |        |        |      |     |     | errors |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Delta  |        |
|        |        |        |      |     |     | TIB    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | Delta  |        |
|        |        |        |      |     |     | RIB    |        |
|        |        |        |      |     |     | table  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0815 |     | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211086 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | tol    |        |
|        |        |        |      |     |     | erance |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0820 | 1   | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211101 |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | V2X    |        |
|        |        |        |      |     |     | NS     |        |
|        |        |        |      |     |     | \_52(R |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0822 |     | F   | CR to  | 16.8.0 |
| 021-06 | AN\#92 | 211107 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0824 |     | F   | CR to  | 16.8.0 |
| 021-06 | AN\#92 | 211115 |      |     |     | TS38.  |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Add    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | n1A-n3 |        |
|        |        |        |      |     |     | A-n78A |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0835 |     | F   | A      | 16.8.0 |
| 021-06 | AN\#92 | 211095 |      |     |     | pplica |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0837 | 1   | F   | Corr   | 16.8.0 |
| 021-06 | AN\#92 | 211102 |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | n48    |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | sensi  |        |
|        |        |        |      |     |     | tivity |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0846 | 1   | F   | Rel-16 | 16.8.0 |
| 021-06 | AN\#92 | 211114 |      |     |     | CR     |        |
|        |        |        |      |     |     | 38101  |        |
|        |        |        |      |     |     | -1-g70 |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0863 | 2   | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211101 |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | update |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | V2X    |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0867 | 1   | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211080 |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | 1-g70: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | EFSENS |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0869 |     | F   | CR for | 16.8.0 |
| 021-06 | AN\#92 | 211116 |      |     |     | 3      |        |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | 1-g70: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_12, |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_13, |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_14, |        |
|        |        |        |      |     |     | NS\_15 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0910 | 1   | B   | Introd | 16.9.0 |
| 021-09 | AN\#93 | 211910 |      |     |     | uction |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | 7.5kHz |        |
|        |        |        |      |     |     | shift  |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | TDD    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n34    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n39    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0920 |     | F   | Big CR | 16.9.0 |
| 021-09 | AN\#93 | 211921 |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | part1  |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0922 |     | F   | Big CR | 16.9.0 |
| 021-09 | AN\#93 | 211907 |      |     |     | for TS |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | part2  |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0926 | 2   | C   | Introd | 16.9.0 |
| 021-09 | AN\#93 | 212599 |      |     |     | uction |        |
|        |        |        |      |     |     | of NS  |        |
|        |        |        |      |     |     | value  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | di     |        |
|        |        |        |      |     |     | stingu |        |
|        |        |        |      |     |     | ishing |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | upport |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | ex     |        |
|        |        |        |      |     |     | tended |        |
|        |        |        |      |     |     | n77    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0976 |     | F   | CR to  | 1      |
| 021-12 | AN\#94 | 212847 |      |     |     | remove | 6.10.0 |
|        |        |        |      |     |     | LO     |        |
|        |        |        |      |     |     | exce   |        |
|        |        |        |      |     |     | ptions |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 0982 |     | F   | Big CR | 1      |
| 021-12 | AN\#94 | 212853 |      |     |     | for TS | 6.10.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1036 |     | F   | Big CR | 1      |
| 022-03 | AN\#95 | 220337 |      |     |     | for TS | 6.11.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | Part-1 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1038 |     | F   | Big CR | 1      |
| 022-03 | AN\#95 | 220337 |      |     |     | for TS | 6.11.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | Part-2 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1052 |     | F   | CR for | 1      |
| 022-06 | AN\#96 | 221666 |      |     |     | 3      | 6.12.0 |
|        |        |        |      |     |     | 8.101- |        |
|        |        |        |      |     |     | 1-gb0: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for n7 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | (N     |        |
|        |        |        |      |     |     | S\_46) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1056 |     | F   | CR for | 1      |
| 022-06 | AN\#96 | 221668 |      |     |     | 38     | 6.12.0 |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel16  |        |
|        |        |        |      |     |     | Minor  |        |
|        |        |        |      |     |     | AMPR   |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n65 to |        |
|        |        |        |      |     |     | a      |        |
|        |        |        |      |     |     | ccount |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SCS    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1115 | 1   | F   | CR to  | 1      |
| 022-06 | AN\#96 | 221661 |      |     |     | R16    | 6.12.0 |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | tra    |        |
|        |        |        |      |     |     | nsient |        |
|        |        |        |      |     |     | period |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1120 |     | F   | Big CR | 1      |
| 022-06 | AN\#96 | 221655 |      |     |     | for TS | 6.12.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | Part-1 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1125 |     | F   | CR for | 1      |
| 022-06 | AN\#96 | 221066 |      |     |     | up     | 6.12.1 |
|        |        |        |      |     |     | dating |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | note   |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | man    |        |
|        |        |        |      |     |     | datory |        |
|        |        |        |      |     |     | simult |        |
|        |        |        |      |     |     | aneous |        |
|        |        |        |      |     |     | Rx/Tx  |        |
|        |        |        |      |     |     | capa   |        |
|        |        |        |      |     |     | bility |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1    |        |
|        |        |        |      |     |     | NR-CA  |        |
|        |        |        |      |     |     | combin |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1189 |     | F   | CR for | 1      |
| 022-09 | AN\#97 | 222035 |      |     |     | TS     | 6.13.0 |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1, |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | conf   |        |
|        |        |        |      |     |     | igured |        |
|        |        |        |      |     |     | trans  |        |
|        |        |        |      |     |     | mitted |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | V2X    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1191 |     | F   | Big CR | 1      |
| 022-09 | AN\#97 | 222023 |      |     |     | for    | 6.13.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | part1  |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1193 |     | F   | Big CR | 1      |
| 022-09 | AN\#97 | 222023 |      |     |     | for    | 6.13.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | part2  |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1195 | 2   | C   | Ext    | 1      |
| 022-09 | AN\#97 | 222682 |      |     |     | ension | 6.13.0 |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | ope    |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | n77    |        |
|        |        |        |      |     |     | fre    |        |
|        |        |        |      |     |     | quency |        |
|        |        |        |      |     |     | range  |        |
|        |        |        |      |     |     | in US  |        |
|        |        |        |      |     |     | \[n77  |        |
|        |        |        |      |     |     | US\]   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1209 |     | A   | Ad     | 1      |
| 022-12 | \#98-e | 223290 |      |     |     | dition | 6.14.0 |
|        |        |        |      |     |     | of FR1 |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | MIMO   |        |
|        |        |        |      |     |     | EVM    |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1212 |     | A   | Ad     | 1      |
| 022-12 | \#98-e | 223290 |      |     |     | dition | 6.14.0 |
|        |        |        |      |     |     | of FR2 |        |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | MIMO   |        |
|        |        |        |      |     |     | EVM    |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | Note:  |        |
|        |        |        |      |     |     | The CR |        |
|        |        |        |      |     |     | was    |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | i      |        |
|        |        |        |      |     |     | mpleme |        |
|        |        |        |      |     |     | ntable |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | refore |        |
|        |        |        |      |     |     | was    |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | imple  |        |
|        |        |        |      |     |     | mented |        |
|        |        |        |      |     |     | in the |        |
|        |        |        |      |     |     | sp     |        |
|        |        |        |      |     |     | ecific |        |
|        |        |        |      |     |     | ation. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1219 | 2   | F   | Ad     | 1      |
| 022-12 | \#98-e | 223295 |      |     |     | dition | 6.14.0 |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 77-n78 |        |
|        |        |        |      |     |     | to CA  |        |
|        |        |        |      |     |     | Band   |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1221 |     | F   | Corr   | 1      |
| 022-12 | \#98-e | 223297 |      |     |     | ection | 6.14.0 |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | n91,n  |        |
|        |        |        |      |     |     | 92,n93 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n94    |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1224 |     | F   | CR for | 1      |
| 022-12 | \#98-e | 223296 |      |     |     | TS     | 6.14.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | el-16: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ecting |        |
|        |        |        |      |     |     | cr     |        |
|        |        |        |      |     |     | itical |        |
|        |        |        |      |     |     | error  |        |
|        |        |        |      |     |     | with   |        |
|        |        |        |      |     |     | co-exi |        |
|        |        |        |      |     |     | stence |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | n8-n40 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1243 |     | F   | CR to  | 1      |
| 022-12 | \#98-e | 223296 |      |     |     | R16    | 6.14.0 |
|        |        |        |      |     |     | TS38   |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | for UE |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for UL |        |
|        |        |        |      |     |     | CA     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1252 | 2   | F   | CR to  | 1      |
| 022-12 | \#98-e | 223296 |      |     |     | 38     | 6.14.0 |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | moving |        |
|        |        |        |      |     |     | amb    |        |
|        |        |        |      |     |     | iguity |        |
|        |        |        |      |     |     | in CA  |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | defi   |        |
|        |        |        |      |     |     | nition |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1266 |     | A   | CR on  | 1      |
| 022-12 | \#98-e | 223291 |      |     |     | 'Annex | 6.14.0 |
|        |        |        |      |     |     | G      |        |
|        |        |        |      |     |     | Diff   |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | lative |        |
|        |        |        |      |     |     | phase  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | e      |        |
|        |        |        |      |     |     | rrors' |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | FR1 UL |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | herent |        |
|        |        |        |      |     |     | MIMO   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1269 |     | A   | CR on  | 1      |
| 022-12 | \#98-e | 223291 |      |     |     | TDD    | 6.14.0 |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | EN-DC  |        |
|        |        |        |      |     |     | - TS   |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RAN    | RP-    | 1277 | 2   | F   | C      | 1      |
| 022-12 | \#98-e | 223480 |      |     |     | larifi | 6.14.0 |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | CA\_NS |        |
|        |        |        |      |     |     | indi   |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | values |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | n77 in |        |
|        |        |        |      |     |     | the US |        |
|        |        |        |      |     |     | \[n77  |        |
|        |        |        |      |     |     | US\]   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1303 |     | F   | CR for | 1      |
| 023-03 | AN\#99 | 230501 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | el-16: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | wrong  |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | NS\_50 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1322 |     | A   | Ad     | 1      |
| 023-03 | AN\#99 | 230502 |      |     |     | dition | 6.15.0 |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | onfigu |        |
|        |        |        |      |     |     | ration |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | arrier |        |
|        |        |        |      |     |     | aggre  |        |
|        |        |        |      |     |     | gation |        |
|        |        |        |      |     |     | RMCs   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1353 | 1   | F   | Rel16  | 1      |
| 023-03 | AN\#99 | 230504 |      |     |     | Cat F  | 6.15.0 |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | wrong  |        |
|        |        |        |      |     |     | table  |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | that   |        |
|        |        |        |      |     |     | clause |        |
|        |        |        |      |     |     | 6.2A   |        |
|        |        |        |      |     |     | .3.1.1 |        |
|        |        |        |      |     |     | refer  |        |
|        |        |        |      |     |     | to     |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1371 |     | F   | C      | 1      |
| 023-03 | AN\#99 | 230507 |      |     |     | orrect | 6.15.0 |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | caling |        |
|        |        |        |      |     |     | number |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | MPR    |        |
|        |        |        |      |     |     | /A-MPR |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | NS\_04 |        |
|        |        |        |      |     |     | SEM    |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1379 |     | A   | CR on  | 1      |
| 023-03 | AN\#99 | 230502 |      |     |     | Ha     | 6.15.0 |
|        |        |        |      |     |     | rmonic |        |
|        |        |        |      |     |     | mixing |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n8 |        |
|        |        |        |      |     |     | A-n79A |        |
|        |        |        |      |     |     | (R16   |        |
|        |        |        |      |     |     | CAT-A) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1391 | 1   | F   | C      | 1      |
| 023-03 | AN\#99 | 230507 |      |     |     | larifi | 6.15.0 |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | Time   |        |
|        |        |        |      |     |     | mask   |        |
|        |        |        |      |     |     | for Tx |        |
|        |        |        |      |     |     | swi    |        |
|        |        |        |      |     |     | tching |        |
|        |        |        |      |     |     | for SA |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1398 | 1   | F   | CR for | 1      |
| 023-03 | AN\#99 | 230504 |      |     |     | Rel-16 | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | orrect |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n4 |        |
|        |        |        |      |     |     | 6M/N/O |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1402 |     | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230507 |      |     |     | 38.    | 6.15.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | ref    |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | \_NC\_ |        |
|        |        |        |      |     |     | NS\_04 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1409 |     | A   | CR for | 1      |
| 023-03 | AN\#99 | 230503 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | inner  |        |
|        |        |        |      |     |     | outer  |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | almost |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | RB     |        |
|        |        |        |      |     |     | allo   |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1412 |     | F   | CR for | 1      |
| 023-03 | AN\#99 | 230501 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n34    |        |
|        |        |        |      |     |     | prot   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n1 and |        |
|        |        |        |      |     |     | n65    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1415 |     | F   | CR for | 1      |
| 023-03 | AN\#99 | 230501 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | c      |        |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | Out-o  |        |
|        |        |        |      |     |     | f-band |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | exc    |        |
|        |        |        |      |     |     | eption |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n20    |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | n28    |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1434 |     | A   | CR to  | 1      |
| 023-03 | AN\#99 | 230503 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | hu     |        |
|        |        |        |      |     |     | midity |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | dition |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | normal |        |
|        |        |        |      |     |     | tempe  |        |
|        |        |        |      |     |     | rature |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1452 | 1   | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230507 |      |     |     | return | 6.15.0 |
|        |        |        |      |     |     | he Eq1 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | intr   |        |
|        |        |        |      |     |     | a-band |        |
|        |        |        |      |     |     | UL CA  |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1453 | 1   | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230504 |      |     |     | c      | 6.15.0 |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | duplex |        |
|        |        |        |      |     |     | mode   |        |
|        |        |        |      |     |     | of SDL |        |
|        |        |        |      |     |     | bands  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1455 |     | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230501 |      |     |     | add    | 6.15.0 |
|        |        |        |      |     |     | band   |        |
|        |        |        |      |     |     | n29 to |        |
|        |        |        |      |     |     | bl     |        |
|        |        |        |      |     |     | ocking |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1457 |     | A   | Output | 1      |
| 023-03 | AN\#99 | 230504 |      |     |     | power  | 6.15.0 |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_38, |        |
|        |        |        |      |     |     | N      |        |
|        |        |        |      |     |     | S\_40, |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | NS\_41 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1463 |     | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230501 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38.1   |        |
|        |        |        |      |     |     | 01-1\_ |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | 4Rx    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | SUL    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | R      | RP-    | 1466 | 1   | F   | CR to  | 1      |
| 023-03 | AN\#99 | 230504 |      |     |     | TS     | 6.15.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | M      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | gua    |        |
|        |        |        |      |     |     | rdband |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | ULCA   |        |
|        |        |        |      |     |     | power  |        |
|        |        |        |      |     |     | class  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1482 |     | A   | CR to  | 1      |
| 023-06 | N\#100 | 231355 |      |     |     | K1 and | 6.16.0 |
|        |        |        |      |     |     | Pds    |        |
|        |        |        |      |     |     | chNumO |        |
|        |        |        |      |     |     | fHarqP |        |
|        |        |        |      |     |     | rocess |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | DL-CA  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1486 |     | A   | FR1    | 1      |
| 023-06 | N\#100 | 231355 |      |     |     | OOB    | 6.16.0 |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1492 |     | F   | CR TS  | 1      |
| 023-06 | N\#100 | 231351 |      |     |     | 38.    | 6.16.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on NR  |        |
|        |        |        |      |     |     | V2X    |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | in     |        |
|        |        |        |      |     |     | Rel-16 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1532 | 1   | F   | NR     | 1      |
| 023-06 | N\#100 | 231354 |      |     |     | int    | 6.16.0 |
|        |        |        |      |     |     | erband |        |
|        |        |        |      |     |     | 2UL CA |        |
|        |        |        |      |     |     | co-ex  |        |
|        |        |        |      |     |     | simpli |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1541 |     | A   | CR for | 1      |
| 023-06 | N\#100 | 231355 |      |     |     | TS     | 6.16.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | to the |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | inimum |        |
|        |        |        |      |     |     | gua    |        |
|        |        |        |      |     |     | rdband |        |
|        |        |        |      |     |     | calcu  |        |
|        |        |        |      |     |     | lation |        |
|        |        |        |      |     |     | (      |        |
|        |        |        |      |     |     | R16\_C |        |
|        |        |        |      |     |     | AT\_A) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1544 | 2   | F   | Rel-16 | 1      |
| 023-06 | N\#100 | 231351 |      |     |     | CR to  | 6.16.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | 101-1  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | C      |        |
|        |        |        |      |     |     | larifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | of UL  |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | Swi    |        |
|        |        |        |      |     |     | tching |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1555 | 2   | F   | CR to  | 1      |
| 023-06 | N\#100 | 231356 |      |     |     | TS38.  | 6.16.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | terms  |        |
|        |        |        |      |     |     | for NR |        |
|        |        |        |      |     |     | DC     |        |
|        |        |        |      |     |     | Pcmax  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1586 |     | F   | CR for | 1      |
| 023-06 | N\#100 | 231351 |      |     |     | TS     | 6.16.0 |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Adding |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NR-U   |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | CAT-F  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1593 |     | F   | CR for | 1      |
| 023-06 | N\#100 | 231352 |      |     |     | 38.    | 6.16.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Single |        |
|        |        |        |      |     |     | SUL CA |        |
|        |        |        |      |     |     | combi  |        |
|        |        |        |      |     |     | nation |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | tation |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | odific |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1597 |     | A   | Update | 1      |
| 023-06 | N\#100 | 231356 |      |     |     | of FR1 | 6.16.0 |
|        |        |        |      |     |     | UL     |        |
|        |        |        |      |     |     | MIMO   |        |
|        |        |        |      |     |     | EVM    |        |
|        |        |        |      |     |     | measu  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | descr  |        |
|        |        |        |      |     |     | iption |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1603 |     | A   | CR to  | 1      |
| 023-06 | N\#100 | 231356 |      |     |     | 38     | 6.16.0 |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | Cat A, |        |
|        |        |        |      |     |     | FRC    |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1648 | 1   | F   | CR to  | 1      |
| 023-09 | N\#101 | 232505 |      |     |     | TS     | 6.17.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | Introd |        |
|        |        |        |      |     |     | uction |        |
|        |        |        |      |     |     | of TDD |        |
|        |        |        |      |     |     | uplink |        |
|        |        |        |      |     |     | RMC    |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | s      |        |
|        |        |        |      |     |     | horter |        |
|        |        |        |      |     |     | tran   |        |
|        |        |        |      |     |     | sients |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1657 |     | A   | CR for | 1      |
| 023-09 | N\#101 | 232487 |      |     |     | TS     | 6.17.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | CAT-A: |        |
|        |        |        |      |     |     | Intro  |        |
|        |        |        |      |     |     | ducing |        |
|        |        |        |      |     |     | modifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_43 |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | region |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1664 |     | A   | CR to  | 1      |
| 023-09 | N\#101 | 232504 |      |     |     | c      | 6.17.0 |
|        |        |        |      |     |     | larify |        |
|        |        |        |      |     |     | p      |        |
|        |        |        |      |     |     | i2BPSK |        |
|        |        |        |      |     |     | note   |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1676 |     | F   | \[T    | 1      |
| 023-09 | N\#101 | 232500 |      |     |     | EI16\] | 6.17.0 |
|        |        |        |      |     |     | CR     |        |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | V      |        |
|        |        |        |      |     |     | arious |        |
|        |        |        |      |     |     | maint  |        |
|        |        |        |      |     |     | enance |        |
|        |        |        |      |     |     | issues |        |
|        |        |        |      |     |     | R16    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1690 |     | A   | CR for | 1      |
| 023-09 | N\#101 | 232487 |      |     |     | 38     | 6.17.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | Almost |        |
|        |        |        |      |     |     | con    |        |
|        |        |        |      |     |     | tiguos |        |
|        |        |        |      |     |     | NBC    |        |
|        |        |        |      |     |     | change |        |
|        |        |        |      |     |     | re     |        |
|        |        |        |      |     |     | versal |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1708 |     | A   | CR to  | 1      |
| 023-09 | N\#101 | 232505 |      |     |     | TS     | 6.17.0 |
|        |        |        |      |     |     | 38.    |        |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | Pcmax  |        |
|        |        |        |      |     |     | tol    |        |
|        |        |        |      |     |     | erance |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 2Tx    |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1724 |     | F   | CR for | 1      |
| 023-09 | N\#101 | 232489 |      |     |     | TS     | 6.17.0 |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | \[NR   |        |
|        |        |        |      |     |     | \_CADC |        |
|        |        |        |      |     |     | \_R16\ |        |
|        |        |        |      |     |     | _3BDL\ |        |
|        |        |        |      |     |     | _2BUL- |        |
|        |        |        |      |     |     | Core\] |        |
|        |        |        |      |     |     | R      |        |
|        |        |        |      |     |     | emoval |        |
|        |        |        |      |     |     | of the |        |
|        |        |        |      |     |     | const  |        |
|        |        |        |      |     |     | ituent |        |
|        |        |        |      |     |     | bands  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | delta  |        |
|        |        |        |      |     |     | RIB    |        |
|        |        |        |      |     |     | values |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | inte   |        |
|        |        |        |      |     |     | r-band |        |
|        |        |        |      |     |     | CA     |        |
|        |        |        |      |     |     | co     |        |
|        |        |        |      |     |     | nfigur |        |
|        |        |        |      |     |     | ations |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1733 |     | A   | \[NR   | 1      |
| 023-09 | N\#101 | 232502 |      |     |     | \_newR | 6.17.0 |
|        |        |        |      |     |     | AT-Cor |        |
|        |        |        |      |     |     | e\]Edi |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | modifi |        |
|        |        |        |      |     |     | cation |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38.101 |        |
|        |        |        |      |     |     | -1\_V2 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1748 |     | A   | \      | 1      |
| 023-09 | N\#101 | 232503 |      |     |     | [NR\_n | 6.17.0 |
|        |        |        |      |     |     | ewRAT- |        |
|        |        |        |      |     |     | Perf\] |        |
|        |        |        |      |     |     | CR:    |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of FRC |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | aximum |        |
|        |        |        |      |     |     | input  |        |
|        |        |        |      |     |     | level  |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | 256QAM |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1751 |     | F   | CR to  | 1      |
| 023-09 | N\#101 | 232489 |      |     |     | 38.    | 6.17.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | add    |        |
|        |        |        |      |     |     | the    |        |
|        |        |        |      |     |     | m      |        |
|        |        |        |      |     |     | issing |        |
|        |        |        |      |     |     | Tx     |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | CA\_n  |        |
|        |        |        |      |     |     | 25-n71 |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1756 | 1   | A   | \      | 1      |
| 023-09 | N\#101 | 232501 |      |     |     | [NR\_n | 6.17.0 |
|        |        |        |      |     |     | ewRAT- |        |
|        |        |        |      |     |     | Core\] |        |
|        |        |        |      |     |     | CR for |        |
|        |        |        |      |     |     | TS     |        |
|        |        |        |      |     |     | 38     |        |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | modify |        |
|        |        |        |      |     |     | MSD    |        |
|        |        |        |      |     |     | due to |        |
|        |        |        |      |     |     | ha     |        |
|        |        |        |      |     |     | rmonic |        |
|        |        |        |      |     |     | mixing |        |
|        |        |        |      |     |     | interf |        |
|        |        |        |      |     |     | erence |        |
|        |        |        |      |     |     | (R16)  |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1761 |     | F   | CR to  | 1      |
| 023-09 | N\#101 | 232486 |      |     |     | TS38   | 6.17.0 |
|        |        |        |      |     |     | .101-1 |        |
|        |        |        |      |     |     | on     |        |
|        |        |        |      |     |     | corre  |        |
|        |        |        |      |     |     | ctions |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | requi  |        |
|        |        |        |      |     |     | rement |        |
|        |        |        |      |     |     | s\_R16 |        |
|        |        |        |      |     |     |        |        |
|        |        |        |      |     |     | NOTE:  |        |
|        |        |        |      |     |     | CR was |        |
|        |        |        |      |     |     | not    |        |
|        |        |        |      |     |     | imple  |        |
|        |        |        |      |     |     | mented |        |
|        |        |        |      |     |     | as     |        |
|        |        |        |      |     |     | A-MPR  |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | NS\_59 |        |
|        |        |        |      |     |     | for    |        |
|        |        |        |      |     |     | Rel-16 |        |
|        |        |        |      |     |     | does   |        |
|        |        |        |      |     |     | ot     |        |
|        |        |        |      |     |     | exist. |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1766 | 1   | F   | \[     | 1      |
| 023-09 | N\#101 | 232503 |      |     |     | NR\_RF | 6.17.0 |
|        |        |        |      |     |     | \_FR1- |        |
|        |        |        |      |     |     | Core\] |        |
|        |        |        |      |     |     | Edi    |        |
|        |        |        |      |     |     | torial |        |
|        |        |        |      |     |     | corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | to     |        |
|        |        |        |      |     |     | 6.2A.4 |        |
|        |        |        |      |     |     | (R     |        |
|        |        |        |      |     |     | el-16) |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1787 |     | A   | \      | 1      |
| 023-09 | N\#101 | 232501 |      |     |     | [NR\_n | 6.17.0 |
|        |        |        |      |     |     | ewRAT- |        |
|        |        |        |      |     |     | Core\] |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | raband |        |
|        |        |        |      |     |     | cont   |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA ACS |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1790 |     | F   | \[N    | 1      |
| 023-09 | N\#101 | 232498 |      |     |     | R\_RF\ | 6.17.0 |
|        |        |        |      |     |     | _FR1\] |        |
|        |        |        |      |     |     | Corr   |        |
|        |        |        |      |     |     | ection |        |
|        |        |        |      |     |     | of     |        |
|        |        |        |      |     |     | int    |        |
|        |        |        |      |     |     | raband |        |
|        |        |        |      |     |     | no     |        |
|        |        |        |      |     |     | n-cont |        |
|        |        |        |      |     |     | iguous |        |
|        |        |        |      |     |     | CA ACS |        |
|        |        |        |      |     |     | requir |        |
|        |        |        |      |     |     | ements |        |
+--------+--------+--------+------+-----+-----+--------+--------+
| 2      | RA     | RP-    | 1805 | 1   | F   | CR for | 1      |
| 023-09 | N\#101 | 232498 |      |     |     | 38.    | 6.17.0 |
|        |        |        |      |     |     | 101-1: |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | NS\_27 |        |
|        |        |        |      |     |     | and    |        |
|        |        |        |      |     |     | CA\_   |        |
|        |        |        |      |     |     | NS\_46 |        |
|        |        |        |      |     |     | fix    |        |
+--------+--------+--------+------+-----+-----+--------+--------+
