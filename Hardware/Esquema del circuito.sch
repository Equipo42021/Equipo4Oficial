EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Analog_ADC:INA226 U?
U 1 1 619457EB
P 1950 -2400
F 0 "U?" H 1950 -1719 50  0000 C CNN
F 1 "INA226" H 1950 -1810 50  0000 C CNN
F 2 "Package_SO:VSSOP-10_3x3mm_P0.5mm" H 2750 -2850 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ina226.pdf" H 2300 -2500 50  0001 C CNN
	1    1950 -2400
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:TL072 U2
U 1 1 619472EC
P 4450 -2500
F 0 "U2" H 4550 -2350 50  0000 C CNN
F 1 "TL072" H 4550 -2650 50  0000 C CNN
F 2 "" H 4450 -2500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 4450 -2500 50  0001 C CNN
	1    4450 -2500
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U3
U 1 1 619501D7
P 8000 -2300
F 0 "U3" H 8100 -2150 50  0000 C CNN
F 1 "TL072" H 8100 -2450 50  0000 C CNN
F 2 "" H 8000 -2300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 8000 -2300 50  0001 C CNN
	1    8000 -2300
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U4
U 1 1 6195329F
P 10800 -2200
F 0 "U4" H 10900 -2050 50  0000 C CNN
F 1 "TL072" H 10900 -2350 50  0000 C CNN
F 2 "" H 10800 -2200 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 10800 -2200 50  0001 C CNN
	1    10800 -2200
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U2
U 2 1 619602D9
P 6350 -2400
F 0 "U2" H 6450 -2250 50  0000 C CNN
F 1 "TL072" H 6450 -2550 50  0000 C CNN
F 2 "" H 6350 -2400 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 6350 -2400 50  0001 C CNN
	2    6350 -2400
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U4
U 2 1 61961A49
P 12650 -2100
F 0 "U4" H 12750 -1950 50  0000 C CNN
F 1 "TL072" H 12750 -2250 50  0000 C CNN
F 2 "" H 12650 -2100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 12650 -2100 50  0001 C CNN
	2    12650 -2100
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL072 U3
U 2 1 61964469
P 9400 -2300
F 0 "U3" H 9500 -2150 50  0000 C CNN
F 1 "TL072" H 9500 -2450 50  0000 C CNN
F 2 "" H 9400 -2300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl071.pdf" H 9400 -2300 50  0001 C CNN
	2    9400 -2300
	1    0    0    1   
$EndComp
$Comp
L Diode:1N4148 D1
U 1 1 61965E58
P 8550 -2600
F 0 "D1" V 8596 -2680 50  0000 R CNN
F 1 "1N4148" V 8505 -2680 50  0000 R CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 8550 -2775 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 8550 -2600 50  0001 C CNN
	1    8550 -2600
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4148 D2
U 1 1 6196781F
P 8550 -1950
F 0 "D2" V 8596 -2030 50  0000 R CNN
F 1 "1N4148" V 8505 -2030 50  0000 R CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 8550 -2125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 8550 -1950 50  0001 C CNN
	1    8550 -1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_POT_US RV1
U 1 1 619692D3
P 12600 -2900
F 0 "RV1" V 12750 -3100 50  0000 C CNN
F 1 "20k" V 12450 -3050 50  0000 C CNN
F 2 "" H 12600 -2900 50  0001 C CNN
F 3 "~" H 12600 -2900 50  0001 C CNN
	1    12600 -2900
	0    1    1    0   
$EndComp
$Comp
L Device:CP1 C2
U 1 1 6196AFB5
P 3400 -2100
F 0 "C2" H 3450 -2000 50  0000 L CNN
F 1 "1u" H 3450 -2200 50  0000 L CNN
F 2 "" H 3400 -2100 50  0001 C CNN
F 3 "~" H 3400 -2100 50  0001 C CNN
	1    3400 -2100
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1 C1
U 1 1 6196C42E
P 3400 -750
F 0 "C1" H 3450 -650 50  0000 L CNN
F 1 "1u" H 3450 -850 50  0000 L CNN
F 2 "" H 3400 -750 50  0001 C CNN
F 3 "~" H 3400 -750 50  0001 C CNN
	1    3400 -750
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1 C3
U 1 1 6196D652
P 5100 -2500
F 0 "C3" H 5200 -2400 50  0000 C CNN
F 1 "0.01u" H 5250 -2600 50  0000 C CNN
F 2 "" H 5100 -2500 50  0001 C CNN
F 3 "~" H 5100 -2500 50  0001 C CNN
	1    5100 -2500
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP1 C4
U 1 1 6196DF8E
P 10750 -3300
F 0 "C4" H 10800 -3200 50  0000 C CNN
F 1 "1u" H 10800 -3400 50  0000 C CNN
F 2 "" H 10750 -3300 50  0001 C CNN
F 3 "~" H 10750 -3300 50  0001 C CNN
	1    10750 -3300
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R1
U 1 1 6196F498
P 2650 -2700
F 0 "R1" V 2700 -2850 50  0000 C CNN
F 1 "1M" V 2600 -2850 50  0000 C CNN
F 2 "" V 2690 -2710 50  0001 C CNN
F 3 "~" H 2650 -2700 50  0001 C CNN
	1    2650 -2700
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R2
U 1 1 6197170F
P 3000 -2100
F 0 "R2" V 2950 -2300 50  0000 L CNN
F 1 "1M" V 3050 -2300 50  0000 L CNN
F 2 "" V 3040 -2110 50  0001 C CNN
F 3 "~" H 3000 -2100 50  0001 C CNN
	1    3000 -2100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R7
U 1 1 61976354
P 7150 -2400
F 0 "R7" V 7200 -2250 50  0000 C CNN
F 1 "10k" V 7050 -2250 50  0000 C CNN
F 2 "" V 7190 -2410 50  0001 C CNN
F 3 "~" H 7150 -2400 50  0001 C CNN
	1    7150 -2400
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R8
U 1 1 6197635A
P 8100 -2900
F 0 "R8" V 8150 -2750 50  0000 C CNN
F 1 "10k" V 8050 -2750 50  0000 C CNN
F 2 "" V 8140 -2910 50  0001 C CNN
F 3 "~" H 8100 -2900 50  0001 C CNN
	1    8100 -2900
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R11
U 1 1 61976360
P 9550 -2900
F 0 "R11" V 9600 -2750 50  0000 C CNN
F 1 "10k" V 9500 -2750 50  0000 C CNN
F 2 "" V 9590 -2910 50  0001 C CNN
F 3 "~" H 9550 -2900 50  0001 C CNN
	1    9550 -2900
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R4
U 1 1 61978F52
P 4450 -3000
F 0 "R4" V 4500 -3150 50  0000 C CNN
F 1 "150k" V 4400 -3150 50  0000 C CNN
F 2 "" V 4490 -3010 50  0001 C CNN
F 3 "~" H 4450 -3000 50  0001 C CNN
	1    4450 -3000
	0    1    -1   0   
$EndComp
$Comp
L Device:R_US R3
U 1 1 61978F5E
P 3650 -2600
F 0 "R3" V 3700 -2450 50  0000 C CNN
F 1 "10k" V 3600 -2450 50  0000 C CNN
F 2 "" V 3690 -2610 50  0001 C CNN
F 3 "~" H 3650 -2600 50  0001 C CNN
	1    3650 -2600
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R5
U 1 1 61978F64
P 5600 -2500
F 0 "R5" V 5650 -2350 50  0000 C CNN
F 1 "150k" V 5550 -2350 50  0000 C CNN
F 2 "" V 5640 -2510 50  0001 C CNN
F 3 "~" H 5600 -2500 50  0001 C CNN
	1    5600 -2500
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R6
U 1 1 6197A886
P 6250 -3000
F 0 "R6" V 6300 -2850 50  0000 C CNN
F 1 "150k" V 6200 -2850 50  0000 C CNN
F 2 "" V 6290 -3010 50  0001 C CNN
F 3 "~" H 6250 -3000 50  0001 C CNN
	1    6250 -3000
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R9
U 1 1 6197A88C
P 8050 -1500
F 0 "R9" V 8100 -1350 50  0000 C CNN
F 1 "10k" V 8000 -1350 50  0000 C CNN
F 2 "" V 8090 -1510 50  0001 C CNN
F 3 "~" H 8050 -1500 50  0001 C CNN
	1    8050 -1500
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R10
U 1 1 6197A892
P 8800 -2900
F 0 "R10" V 8850 -2750 50  0000 C CNN
F 1 "10k" V 8750 -2750 50  0000 C CNN
F 2 "" V 8840 -2910 50  0001 C CNN
F 3 "~" H 8800 -2900 50  0001 C CNN
	1    8800 -2900
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R12
U 1 1 6197A898
P 10150 -2300
F 0 "R12" V 10200 -2150 50  0000 C CNN
F 1 "80.6k" V 10100 -2150 50  0000 C CNN
F 2 "" V 10190 -2310 50  0001 C CNN
F 3 "~" H 10150 -2300 50  0001 C CNN
	1    10150 -2300
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R13
U 1 1 6197C248
P 10750 -2850
F 0 "R13" V 10800 -2700 50  0000 C CNN
F 1 "80.6k" V 10700 -2700 50  0000 C CNN
F 2 "" V 10790 -2860 50  0001 C CNN
F 3 "~" H 10750 -2850 50  0001 C CNN
	1    10750 -2850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	12750 -2900 12950 -2900
Wire Wire Line
	13150 -2900 13150 -2100
Wire Wire Line
	12600 -2750 12600 -2650
Wire Wire Line
	12600 -2650 12950 -2650
Wire Wire Line
	12950 -2650 12950 -2900
Connection ~ 12950 -2900
Wire Wire Line
	12950 -2900 13150 -2900
Wire Wire Line
	12450 -2900 12050 -2900
Wire Wire Line
	12050 -2900 12050 -2200
Wire Wire Line
	11700 -2200 12050 -2200
$Comp
L Device:R_US R14
U 1 1 6197C24E
P 11550 -2200
F 0 "R14" V 11600 -2050 50  0000 C CNN
F 1 "1k" V 11500 -2050 50  0000 C CNN
F 2 "" V 11590 -2210 50  0001 C CNN
F 3 "~" H 11550 -2200 50  0001 C CNN
	1    11550 -2200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	10900 -2850 11250 -2850
Wire Wire Line
	11250 -2200 11400 -2200
Wire Wire Line
	10900 -3300 11250 -3300
Wire Wire Line
	11250 -3300 11250 -2850
Connection ~ 11250 -2850
Wire Wire Line
	10300 -2300 10400 -2300
Wire Wire Line
	10400 -2300 10400 -2850
Wire Wire Line
	10400 -2850 10600 -2850
Wire Wire Line
	10400 -2850 10400 -3300
Wire Wire Line
	10400 -3300 10600 -3300
Connection ~ 10400 -2850
Wire Wire Line
	12950 -2100 13150 -2100
Wire Wire Line
	12350 -2200 12050 -2200
Connection ~ 12050 -2200
Wire Wire Line
	11250 -2850 11250 -2200
Wire Wire Line
	11100 -2200 11250 -2200
Connection ~ 11250 -2200
Wire Wire Line
	10500 -2300 10400 -2300
Connection ~ 10400 -2300
Wire Wire Line
	9700 -2300 9850 -2300
Wire Wire Line
	9700 -2900 9850 -2900
Wire Wire Line
	9850 -2900 9850 -2300
Connection ~ 9850 -2300
Wire Wire Line
	9850 -2300 10000 -2300
Wire Wire Line
	9100 -2400 9050 -2400
Wire Wire Line
	9050 -2400 9050 -2900
Wire Wire Line
	9050 -2900 8950 -2900
Connection ~ 9050 -2900
Wire Wire Line
	8650 -2900 8550 -2900
Wire Wire Line
	8550 -2900 8550 -2750
Wire Wire Line
	8550 -2900 8250 -2900
Connection ~ 8550 -2900
Wire Wire Line
	7500 -2400 7500 -2900
Wire Wire Line
	7500 -2900 7950 -2900
Wire Wire Line
	8200 -1500 8550 -1500
Wire Wire Line
	8550 -1500 8550 -1800
Wire Wire Line
	7500 -2400 7500 -1500
Wire Wire Line
	7500 -1500 7900 -1500
Connection ~ 7500 -2400
Wire Wire Line
	7300 -2400 7500 -2400
Wire Wire Line
	9050 -2200 9100 -2200
Wire Wire Line
	9050 -2200 9050 -1500
Wire Wire Line
	9050 -1500 8550 -1500
Connection ~ 8550 -1500
Wire Wire Line
	8550 -2450 8550 -2300
Wire Wire Line
	8300 -2300 8550 -2300
Connection ~ 8550 -2300
Wire Wire Line
	8550 -2300 8550 -2100
Wire Wire Line
	7500 -2400 7700 -2400
Wire Wire Line
	6650 -2400 6850 -2400
Wire Wire Line
	6400 -3000 6850 -3000
Wire Wire Line
	6850 -3000 6850 -2400
Connection ~ 6850 -2400
Wire Wire Line
	6850 -2400 7000 -2400
Wire Wire Line
	6050 -2500 5850 -2500
Wire Wire Line
	5850 -2500 5850 -3000
Wire Wire Line
	5850 -3000 6100 -3000
Wire Wire Line
	5750 -2500 5850 -2500
Connection ~ 5850 -2500
Wire Wire Line
	5250 -2500 5450 -2500
Wire Wire Line
	4750 -2500 4850 -2500
Wire Wire Line
	4850 -2500 4850 -3000
Wire Wire Line
	4850 -3000 4600 -3000
Connection ~ 4850 -2500
Wire Wire Line
	4850 -2500 4950 -2500
Wire Wire Line
	4150 -2600 3950 -2600
Wire Wire Line
	4300 -3000 3950 -3000
Wire Wire Line
	3950 -3000 3950 -2600
Connection ~ 3950 -2600
Wire Wire Line
	3950 -2600 3800 -2600
Wire Wire Line
	2350 -2600 3200 -2600
Wire Wire Line
	2350 -2700 2500 -2700
Wire Wire Line
	2800 -2700 3200 -2700
Wire Wire Line
	3200 -2700 3200 -2600
Connection ~ 3200 -2600
Wire Wire Line
	3200 -2600 3500 -2600
Wire Wire Line
	2350 -2400 3000 -2400
Wire Wire Line
	3000 -2400 3000 -2250
Wire Wire Line
	3000 -1150 3400 -1150
Wire Wire Line
	4150 -2400 3950 -2400
Wire Wire Line
	3950 -1150 3400 -1150
Connection ~ 3400 -1150
Wire Wire Line
	3400 -1950 3400 -1150
Wire Wire Line
	3000 -1950 3000 -1150
Wire Wire Line
	3950 -2400 3950 -1150
Wire Wire Line
	3950 -1150 5850 -1150
Wire Wire Line
	5850 -1150 5850 -2300
Wire Wire Line
	5850 -2300 6050 -2300
Connection ~ 3950 -1150
Wire Wire Line
	10400 -1150 10400 -2100
Wire Wire Line
	10400 -2100 10500 -2100
Wire Wire Line
	5850 -1150 7600 -1150
Connection ~ 5850 -1150
Wire Wire Line
	7700 -2200 7600 -2200
Wire Wire Line
	7600 -2200 7600 -1150
Connection ~ 7600 -1150
Wire Wire Line
	3400 -900 3400 -1150
Wire Wire Line
	2350 -2100 2650 -2100
Wire Wire Line
	2650 -2100 2650 -450
Wire Wire Line
	2650 -450 3400 -450
Wire Wire Line
	3400 -450 3400 -600
Wire Wire Line
	3400 -450 4450 -450
Wire Wire Line
	4450 -450 4450 -2400
Connection ~ 3400 -450
Wire Wire Line
	4450 -450 8000 -450
Wire Wire Line
	8000 -450 8000 -2200
Connection ~ 4450 -450
Wire Wire Line
	8000 -450 10800 -450
Wire Wire Line
	10800 -450 10800 -2100
Connection ~ 8000 -450
Wire Wire Line
	3400 -3700 4450 -3700
Wire Wire Line
	4450 -3700 4450 -2600
Wire Wire Line
	3400 -3700 3400 -2250
Wire Wire Line
	4450 -3700 8000 -3700
Wire Wire Line
	8000 -3700 8000 -2400
Connection ~ 4450 -3700
Wire Wire Line
	8000 -3700 10800 -3700
Wire Wire Line
	10800 -3700 10800 -2300
Connection ~ 8000 -3700
Wire Wire Line
	2350 -2300 2500 -2300
Wire Wire Line
	2500 -3700 3400 -3700
Connection ~ 3400 -3700
Wire Wire Line
	2500 -3700 2500 -2700
Wire Wire Line
	9050 -2900 9400 -2900
Wire Wire Line
	12350 -2000 12050 -2000
Wire Wire Line
	12050 -2000 12050 -1150
Wire Wire Line
	7600 -1150 10400 -1150
Connection ~ 10400 -1150
Wire Wire Line
	10400 -1150 12050 -1150
Text GLabel 1250 -3700 0    50   Input ~ 0
+Vs
Text GLabel 1250 -3500 0    50   Input ~ 0
GND
Text GLabel 1200 -3250 0    50   Input ~ 0
-Vs
Text GLabel 900  -2700 0    50   Input ~ 0
MidMuscle
Text GLabel 900  -2300 0    50   Input ~ 0
EndMuscle
Text GLabel 900  -2100 0    50   Input ~ 0
Reference
Wire Wire Line
	1550 -2700 900  -2700
Wire Wire Line
	1250 -3700 2500 -3700
Connection ~ 2500 -3700
Wire Wire Line
	1250 -3500 1400 -3500
Wire Wire Line
	1400 -3500 1400 -2100
Wire Wire Line
	1400 -1150 3000 -1150
Connection ~ 3000 -1150
Wire Wire Line
	900  -2300 1550 -2300
Wire Wire Line
	900  -2100 1400 -2100
Connection ~ 1400 -2100
Wire Wire Line
	1400 -2100 1400 -1150
Wire Wire Line
	1200 -3250 1200 -450
Wire Wire Line
	1200 -450 2650 -450
Connection ~ 2650 -450
Connection ~ 2500 -2700
Wire Wire Line
	2500 -2700 2500 -2300
Text GLabel 13350 -2100 2    50   Input ~ 0
Vout
Wire Wire Line
	13350 -2100 13150 -2100
Connection ~ 13150 -2100
$EndSCHEMATC
