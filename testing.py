import re

data = """
This website uses cookies to ensure you get the best experience on our website. Learn more
Got it!
Worldometer
Coronavirus
Population

 
WPopulation Population by Country
Countries in the world by population (2020)
This list includes both countries and dependent territories. Data based on the latest United Nations Population Division estimates.
Click on the name of the country or dependency for current estimates (live population clock), historical data, and projected figures.
See also: World Population
Search:
#	Country (or dependency)	Population
(2020)	Yearly
Change	Net
Change	Density
(P/Km²)	Land Area
(Km²)	Migrants
(net)	Fert.
Rate	Med.
Age	Urban
Pop %	World
Share
1	China	1,439,323,776	0.39 %	5,540,090	153	9,388,211	-348,399	1.7	38	61 %	18.47 %
2	India	1,380,004,385	0.99 %	13,586,631	464	2,973,190	-532,687	2.2	28	35 %	17.70 %
3	United States	331,002,651	0.59 %	1,937,734	36	9,147,420	954,806	1.8	38	83 %	4.25 %
4	Indonesia	273,523,615	1.07 %	2,898,047	151	1,811,570	-98,955	2.3	30	56 %	3.51 %
5	Pakistan	220,892,340	2.00 %	4,327,022	287	770,880	-233,379	3.6	23	35 %	2.83 %
6	Brazil	212,559,417	0.72 %	1,509,890	25	8,358,140	21,200	1.7	33	88 %	2.73 %
7	Nigeria	206,139,589	2.58 %	5,175,990	226	910,770	-60,000	5.4	18	52 %	2.64 %
8	Bangladesh	164,689,383	1.01 %	1,643,222	1,265	130,170	-369,501	2.1	28	39 %	2.11 %
9	Russia	145,934,462	0.04 %	62,206	9	16,376,870	182,456	1.8	40	74 %	1.87 %
10	Mexico	128,932,753	1.06 %	1,357,224	66	1,943,950	-60,000	2.1	29	84 %	1.65 %
11	Japan	126,476,461	-0.30 %	-383,840	347	364,555	71,560	1.4	48	92 %	1.62 %
12	Ethiopia	114,963,588	2.57 %	2,884,858	115	1,000,000	30,000	4.3	19	21 %	1.47 %
13	Philippines	109,581,078	1.35 %	1,464,463	368	298,170	-67,152	2.6	26	47 %	1.41 %
14	Egypt	102,334,404	1.94 %	1,946,331	103	995,450	-38,033	3.3	25	43 %	1.31 %
15	Vietnam	97,338,579	0.91 %	876,473	314	310,070	-80,000	2.1	32	38 %	1.25 %
16	DR Congo	89,561,403	3.19 %	2,770,836	40	2,267,050	23,861	6.0	17	46 %	1.15 %
17	Turkey	84,339,067	1.09 %	909,452	110	769,630	283,922	2.1	32	76 %	1.08 %
18	Iran	83,992,949	1.30 %	1,079,043	52	1,628,550	-55,000	2.2	32	76 %	1.08 %
19	Germany	83,783,942	0.32 %	266,897	240	348,560	543,822	1.6	46	76 %	1.07 %
20	Thailand	69,799,978	0.25 %	174,396	137	510,890	19,444	1.5	40	51 %	0.90 %
21	United Kingdom	67,886,011	0.53 %	355,839	281	241,930	260,650	1.8	40	83 %	0.87 %
22	France	65,273,511	0.22 %	143,783	119	547,557	36,527	1.9	42	82 %	0.84 %
23	Italy	60,461,826	-0.15 %	-88,249	206	294,140	148,943	1.3	47	69 %	0.78 %
24	Tanzania	59,734,218	2.98 %	1,728,755	67	885,800	-40,076	4.9	18	37 %	0.77 %
25	South Africa	59,308,690	1.28 %	750,420	49	1,213,090	145,405	2.4	28	67 %	0.76 %
26	Myanmar	54,409,800	0.67 %	364,380	83	653,290	-163,313	2.2	29	31 %	0.70 %
27	Kenya	53,771,296	2.28 %	1,197,323	94	569,140	-10,000	3.5	20	28 %	0.69 %
28	South Korea	51,269,185	0.09 %	43,877	527	97,230	11,731	1.1	44	82 %	0.66 %
29	Colombia	50,882,891	1.08 %	543,448	46	1,109,500	204,796	1.8	31	80 %	0.65 %
30	Spain	46,754,778	0.04 %	18,002	94	498,800	40,000	1.3	45	80 %	0.60 %
31	Uganda	45,741,007	3.32 %	1,471,413	229	199,810	168,694	5.0	17	26 %	0.59 %
32	Argentina	45,195,774	0.93 %	415,097	17	2,736,690	4,800	2.3	32	93 %	0.58 %
33	Algeria	43,851,044	1.85 %	797,990	18	2,381,740	-10,000	3.1	29	73 %	0.56 %
34	Sudan	43,849,260	2.42 %	1,036,022	25	1,765,048	-50,000	4.4	20	35 %	0.56 %
35	Ukraine	43,733,762	-0.59 %	-259,876	75	579,320	10,000	1.4	41	69 %	0.56 %
36	Iraq	40,222,493	2.32 %	912,710	93	434,320	7,834	3.7	21	73 %	0.52 %
37	Afghanistan	38,928,346	2.33 %	886,592	60	652,860	-62,920	4.6	18	25 %	0.50 %
38	Poland	37,846,611	-0.11 %	-41,157	124	306,230	-29,395	1.4	42	60 %	0.49 %
39	Canada	37,742,154	0.89 %	331,107	4	9,093,510	242,032	1.5	41	81 %	0.48 %
40	Morocco	36,910,560	1.20 %	438,791	83	446,300	-51,419	2.4	30	64 %	0.47 %
41	Saudi Arabia	34,813,871	1.59 %	545,343	16	2,149,690	134,979	2.3	32	84 %	0.45 %
42	Uzbekistan	33,469,203	1.48 %	487,487	79	425,400	-8,863	2.4	28	50 %	0.43 %
43	Peru	32,971,854	1.42 %	461,401	26	1,280,000	99,069	2.3	31	79 %	0.42 %
44	Angola	32,866,272	3.27 %	1,040,977	26	1,246,700	6,413	5.6	17	67 %	0.42 %
45	Malaysia	32,365,999	1.30 %	416,222	99	328,550	50,000	2.0	30	78 %	0.42 %
46	Mozambique	31,255,435	2.93 %	889,399	40	786,380	-5,000	4.9	18	38 %	0.40 %
47	Ghana	31,072,940	2.15 %	655,084	137	227,540	-10,000	3.9	22	57 %	0.40 %
48	Yemen	29,825,964	2.28 %	664,042	56	527,970	-30,000	3.8	20	38 %	0.38 %
49	Nepal	29,136,808	1.85 %	528,098	203	143,350	41,710	1.9	25	21 %	0.37 %
50	Venezuela	28,435,940	-0.28 %	-79,889	32	882,050	-653,249	2.3	30	N.A.	0.36 %
51	Madagascar	27,691,018	2.68 %	721,711	48	581,795	-1,500	4.1	20	39 %	0.36 %
52	Cameroon	26,545,863	2.59 %	669,483	56	472,710	-4,800	4.6	19	56 %	0.34 %
53	Côte d'Ivoire	26,378,274	2.57 %	661,730	83	318,000	-8,000	4.7	19	51 %	0.34 %
54	North Korea	25,778,816	0.44 %	112,655	214	120,410	-5,403	1.9	35	63 %	0.33 %
55	Australia	25,499,884	1.18 %	296,686	3	7,682,300	158,246	1.8	38	86 %	0.33 %
56	Niger	24,206,644	3.84 %	895,929	19	1,266,700	4,000	7.0	15	17 %	0.31 %
57	Taiwan	23,816,775	0.18 %	42,899	673	35,410	30,001	1.2	42	79 %	0.31 %
58	Sri Lanka	21,413,249	0.42 %	89,516	341	62,710	-97,986	2.2	34	18 %	0.27 %
59	Burkina Faso	20,903,273	2.86 %	581,895	76	273,600	-25,000	5.2	18	31 %	0.27 %
60	Mali	20,250,833	3.02 %	592,802	17	1,220,190	-40,000	5.9	16	44 %	0.26 %
61	Romania	19,237,691	-0.66 %	-126,866	84	230,170	-73,999	1.6	43	55 %	0.25 %
62	Malawi	19,129,952	2.69 %	501,205	203	94,280	-16,053	4.3	18	18 %	0.25 %
63	Chile	19,116,201	0.87 %	164,163	26	743,532	111,708	1.7	35	85 %	0.25 %
64	Kazakhstan	18,776,707	1.21 %	225,280	7	2,699,700	-18,000	2.8	31	58 %	0.24 %
65	Zambia	18,383,955	2.93 %	522,925	25	743,390	-8,000	4.7	18	45 %	0.24 %
66	Guatemala	17,915,568	1.90 %	334,096	167	107,160	-9,215	2.9	23	52 %	0.23 %
67	Ecuador	17,643,054	1.55 %	269,392	71	248,360	36,400	2.4	28	63 %	0.23 %
68	Syria	17,500,658	2.52 %	430,523	95	183,630	-427,391	2.8	26	60 %	0.22 %
69	Netherlands	17,134,872	0.22 %	37,742	508	33,720	16,000	1.7	43	92 %	0.22 %
70	Senegal	16,743,927	2.75 %	447,563	87	192,530	-20,000	4.7	19	49 %	0.21 %
71	Cambodia	16,718,965	1.41 %	232,423	95	176,520	-30,000	2.5	26	24 %	0.21 %
72	Chad	16,425,864	3.00 %	478,988	13	1,259,200	2,000	5.8	17	23 %	0.21 %
73	Somalia	15,893,222	2.92 %	450,317	25	627,340	-40,000	6.1	17	47 %	0.20 %
74	Zimbabwe	14,862,924	1.48 %	217,456	38	386,850	-116,858	3.6	19	38 %	0.19 %
75	Guinea	13,132,795	2.83 %	361,549	53	245,720	-4,000	4.7	18	39 %	0.17 %
76	Rwanda	12,952,218	2.58 %	325,268	525	24,670	-9,000	4.1	20	18 %	0.17 %
77	Benin	12,123,200	2.73 %	322,049	108	112,760	-2,000	4.9	19	48 %	0.16 %
78	Burundi	11,890,784	3.12 %	360,204	463	25,680	2,001	5.5	17	14 %	0.15 %
79	Tunisia	11,818,619	1.06 %	123,900	76	155,360	-4,000	2.2	33	70 %	0.15 %
80	Bolivia	11,673,021	1.39 %	159,921	11	1,083,300	-9,504	2.8	26	69 %	0.15 %
81	Belgium	11,589,623	0.44 %	50,295	383	30,280	48,000	1.7	42	98 %	0.15 %
82	Haiti	11,402,528	1.24 %	139,451	414	27,560	-35,000	3.0	24	57 %	0.15 %
83	Cuba	11,326,616	-0.06 %	-6,867	106	106,440	-14,400	1.6	42	78 %	0.15 %
84	South Sudan	11,193,725	1.19 %	131,612	18	610,952	-174,200	4.7	19	25 %	0.14 %
85	Dominican Republic	10,847,910	1.01 %	108,952	225	48,320	-30,000	2.4	28	85 %	0.14 %
86	Czech Republic (Czechia)	10,708,981	0.18 %	19,772	139	77,240	22,011	1.6	43	74 %	0.14 %
87	Greece	10,423,054	-0.48 %	-50,401	81	128,900	-16,000	1.3	46	85 %	0.13 %
88	Jordan	10,203,134	1.00 %	101,440	115	88,780	10,220	2.8	24	91 %	0.13 %
89	Portugal	10,196,709	-0.29 %	-29,478	111	91,590	-6,000	1.3	46	66 %	0.13 %
90	Azerbaijan	10,139,177	0.91 %	91,459	123	82,658	1,200	2.1	32	56 %	0.13 %
91	Sweden	10,099,265	0.63 %	62,886	25	410,340	40,000	1.9	41	88 %	0.13 %
92	Honduras	9,904,607	1.63 %	158,490	89	111,890	-6,800	2.5	24	57 %	0.13 %
93	United Arab Emirates	9,890,402	1.23 %	119,873	118	83,600	40,000	1.4	33	86 %	0.13 %
94	Hungary	9,660,351	-0.25 %	-24,328	107	90,530	6,000	1.5	43	72 %	0.12 %
95	Tajikistan	9,537,645	2.32 %	216,627	68	139,960	-20,000	3.6	22	27 %	0.12 %
96	Belarus	9,449,323	-0.03 %	-3,088	47	202,910	8,730	1.7	40	79 %	0.12 %
97	Austria	9,006,398	0.57 %	51,296	109	82,409	65,000	1.5	43	57 %	0.12 %
98	Papua New Guinea	8,947,024	1.95 %	170,915	20	452,860	-800	3.6	22	13 %	0.11 %
99	Serbia	8,737,371	-0.40 %	-34,864	100	87,460	4,000	1.5	42	56 %	0.11 %
100	Israel	8,655,535	1.60 %	136,158	400	21,640	10,000	3.0	30	93 %	0.11 %
101	Switzerland	8,654,622	0.74 %	63,257	219	39,516	52,000	1.5	43	74 %	0.11 %
102	Togo	8,278,724	2.43 %	196,358	152	54,390	-2,000	4.4	19	43 %	0.11 %
103	Sierra Leone	7,976,983	2.10 %	163,768	111	72,180	-4,200	4.3	19	43 %	0.10 %
104	Hong Kong	7,496,981	0.82 %	60,827	7,140	1,050	29,308	1.3	45	N.A.	0.10 %
105	Laos	7,275,560	1.48 %	106,105	32	230,800	-14,704	2.7	24	36 %	0.09 %
106	Paraguay	7,132,538	1.25 %	87,902	18	397,300	-16,556	2.4	26	62 %	0.09 %
107	Bulgaria	6,948,445	-0.74 %	-51,674	64	108,560	-4,800	1.6	45	76 %	0.09 %
108	Libya	6,871,292	1.38 %	93,840	4	1,759,540	-1,999	2.3	29	78 %	0.09 %
109	Lebanon	6,825,445	-0.44 %	-30,268	667	10,230	-30,012	2.1	30	78 %	0.09 %
110	Nicaragua	6,624,554	1.21 %	79,052	55	120,340	-21,272	2.4	26	57 %	0.08 %
111	Kyrgyzstan	6,524,195	1.69 %	108,345	34	191,800	-4,000	3.0	26	36 %	0.08 %
112	El Salvador	6,486,205	0.51 %	32,652	313	20,720	-40,539	2.1	28	73 %	0.08 %
113	Turkmenistan	6,031,200	1.50 %	89,111	13	469,930	-5,000	2.8	27	53 %	0.08 %
114	Singapore	5,850,342	0.79 %	46,005	8,358	700	27,028	1.2	42	N.A.	0.08 %
115	Denmark	5,792,202	0.35 %	20,326	137	42,430	15,200	1.8	42	88 %	0.07 %
116	Finland	5,540,720	0.15 %	8,564	18	303,890	14,000	1.5	43	86 %	0.07 %
117	Congo	5,518,087	2.56 %	137,579	16	341,500	-4,000	4.5	19	70 %	0.07 %
118	Slovakia	5,459,642	0.05 %	2,629	114	48,088	1,485	1.5	41	54 %	0.07 %
119	Norway	5,421,241	0.79 %	42,384	15	365,268	28,000	1.7	40	83 %	0.07 %
120	Oman	5,106,626	2.65 %	131,640	16	309,500	87,400	2.9	31	87 %	0.07 %
121	State of Palestine	5,101,414	2.41 %	119,994	847	6,020	-10,563	3.7	21	80 %	0.07 %
122	Costa Rica	5,094,118	0.92 %	46,557	100	51,060	4,200	1.8	33	80 %	0.07 %
123	Liberia	5,057,681	2.44 %	120,307	53	96,320	-5,000	4.4	19	53 %	0.06 %
124	Ireland	4,937,786	1.13 %	55,291	72	68,890	23,604	1.8	38	63 %	0.06 %
125	Central African Republic	4,829,767	1.78 %	84,582	8	622,980	-40,000	4.8	18	43 %	0.06 %
126	New Zealand	4,822,233	0.82 %	39,170	18	263,310	14,881	1.9	38	87 %	0.06 %
127	Mauritania	4,649,658	2.74 %	123,962	5	1,030,700	5,000	4.6	20	57 %	0.06 %
128	Panama	4,314,767	1.61 %	68,328	58	74,340	11,200	2.5	30	68 %	0.06 %
129	Kuwait	4,270,571	1.51 %	63,488	240	17,820	39,520	2.1	37	N.A.	0.05 %
130	Croatia	4,105,267	-0.61 %	-25,037	73	55,960	-8,001	1.4	44	58 %	0.05 %
131	Moldova	4,033,963	-0.23 %	-9,300	123	32,850	-1,387	1.3	38	43 %	0.05 %
132	Georgia	3,989,167	-0.19 %	-7,598	57	69,490	-10,000	2.1	38	58 %	0.05 %
133	Eritrea	3,546,421	1.41 %	49,304	35	101,000	-39,858	4.1	19	63 %	0.05 %
134	Uruguay	3,473,730	0.35 %	11,996	20	175,020	-3,000	2.0	36	96 %	0.04 %
135	Bosnia and Herzegovina	3,280,819	-0.61 %	-20,181	64	51,000	-21,585	1.3	43	52 %	0.04 %
136	Mongolia	3,278,290	1.65 %	53,123	2	1,553,560	-852	2.9	28	67 %	0.04 %
137	Armenia	2,963,243	0.19 %	5,512	104	28,470	-4,998	1.8	35	63 %	0.04 %
138	Jamaica	2,961,167	0.44 %	12,888	273	10,830	-11,332	2.0	31	55 %	0.04 %
139	Qatar	2,881,053	1.73 %	48,986	248	11,610	40,000	1.9	32	96 %	0.04 %
140	Albania	2,877,797	-0.11 %	-3,120	105	27,400	-14,000	1.6	36	63 %	0.04 %
141	Puerto Rico	2,860,853	-2.47 %	-72,555	323	8,870	-97,986	1.2	44	N.A.	0.04 %
142	Lithuania	2,722,289	-1.35 %	-37,338	43	62,674	-32,780	1.7	45	71 %	0.03 %
143	Namibia	2,540,905	1.86 %	46,375	3	823,290	-4,806	3.4	22	55 %	0.03 %
144	Gambia	2,416,668	2.94 %	68,962	239	10,120	-3,087	5.3	18	59 %	0.03 %
145	Botswana	2,351,627	2.08 %	47,930	4	566,730	3,000	2.9	24	73 %	0.03 %
146	Gabon	2,225,734	2.45 %	53,155	9	257,670	3,260	4.0	23	87 %	0.03 %
147	Lesotho	2,142,249	0.80 %	16,981	71	30,360	-10,047	3.2	24	31 %	0.03 %
148	North Macedonia	2,083,374	0.00 %	-85	83	25,220	-1,000	1.5	39	59 %	0.03 %
149	Slovenia	2,078,938	0.01 %	284	103	20,140	2,000	1.6	45	55 %	0.03 %
150	Guinea-Bissau	1,968,001	2.45 %	47,079	70	28,120	-1,399	4.5	19	45 %	0.03 %
151	Latvia	1,886,198	-1.08 %	-20,545	30	62,200	-14,837	1.7	44	69 %	0.02 %
152	Bahrain	1,701,575	3.68 %	60,403	2,239	760	47,800	2.0	32	89 %	0.02 %
153	Equatorial Guinea	1,402,985	3.47 %	46,999	50	28,050	16,000	4.6	22	73 %	0.02 %
154	Trinidad and Tobago	1,399,488	0.32 %	4,515	273	5,130	-800	1.7	36	52 %	0.02 %
155	Estonia	1,326,535	0.07 %	887	31	42,390	3,911	1.6	42	68 %	0.02 %
156	Timor-Leste	1,318,445	1.96 %	25,326	89	14,870	-5,385	4.1	21	33 %	0.02 %
157	Mauritius	1,271,768	0.17 %	2,100	626	2,030	0	1.4	37	41 %	0.02 %
158	Cyprus	1,207,359	0.73 %	8,784	131	9,240	5,000	1.3	37	67 %	0.02 %
159	Eswatini	1,160,164	1.05 %	12,034	67	17,200	-8,353	3.0	21	30 %	0.01 %
160	Djibouti	988,000	1.48 %	14,440	43	23,180	900	2.8	27	79 %	0.01 %
161	Fiji	896,445	0.73 %	6,492	49	18,270	-6,202	2.8	28	59 %	0.01 %
162	Réunion	895,312	0.72 %	6,385	358	2,500	-1,256	2.3	36	100 %	0.01 %
163	Comoros	869,601	2.20 %	18,715	467	1,861	-2,000	4.2	20	29 %	0.01 %
164	Guyana	786,552	0.48 %	3,786	4	196,850	-6,000	2.5	27	27 %	0.01 %
165	Bhutan	771,608	1.12 %	8,516	20	38,117	320	2.0	28	46 %	0.01 %
166	Solomon Islands	686,884	2.55 %	17,061	25	27,990	-1,600	4.4	20	23 %	0.01 %
167	Macao	649,335	1.39 %	8,890	21,645	30	5,000	1.2	39	N.A.	0.01 %
168	Montenegro	628,066	0.01 %	79	47	13,450	-480	1.8	39	68 %	0.01 %
169	Luxembourg	625,978	1.66 %	10,249	242	2,590	9,741	1.5	40	88 %	0.01 %
170	Western Sahara	597,339	2.55 %	14,876	2	266,000	5,582	2.4	28	87 %	0.01 %
171	Suriname	586,632	0.90 %	5,260	4	156,000	-1,000	2.4	29	65 %	0.01 %
172	Cabo Verde	555,987	1.10 %	6,052	138	4,030	-1,342	2.3	28	68 %	0.01 %
173	Maldives	540,544	1.81 %	9,591	1,802	300	11,370	1.9	30	35 %	0.01 %
174	Malta	441,543	0.27 %	1,171	1,380	320	900	1.5	43	93 %	0.01 %
175	Brunei	437,479	0.97 %	4,194	83	5,270	0	1.8	32	80 %	0.01 %
176	Guadeloupe	400,124	0.02 %	68	237	1,690	-1,440	2.2	44	N.A.	0.01 %
177	Belize	397,628	1.86 %	7,275	17	22,810	1,200	2.3	25	46 %	0.01 %
178	Bahamas	393,244	0.97 %	3,762	39	10,010	1,000	1.8	32	86 %	0.01 %
179	Martinique	375,265	-0.08 %	-289	354	1,060	-960	1.9	47	92 %	0.00 %
180	Iceland	341,243	0.65 %	2,212	3	100,250	380	1.8	37	94 %	0.00 %
181	Vanuatu	307,145	2.42 %	7,263	25	12,190	120	3.8	21	24 %	0.00 %
182	French Guiana	298,682	2.70 %	7,850	4	82,200	1,200	3.4	25	87 %	0.00 %
183	Barbados	287,375	0.12 %	350	668	430	-79	1.6	40	31 %	0.00 %
184	New Caledonia	285,498	0.97 %	2,748	16	18,280	502	2.0	34	72 %	0.00 %
185	French Polynesia	280,908	0.58 %	1,621	77	3,660	-1,000	2.0	34	64 %	0.00 %
186	Mayotte	272,815	2.50 %	6,665	728	375	0	3.7	20	46 %	0.00 %
187	Sao Tome & Principe	219,159	1.91 %	4,103	228	960	-1,680	4.4	19	74 %	0.00 %
188	Samoa	198,414	0.67 %	1,317	70	2,830	-2,803	3.9	22	18 %	0.00 %
189	Saint Lucia	183,627	0.46 %	837	301	610	0	1.4	34	19 %	0.00 %
190	Channel Islands	173,863	0.93 %	1,604	915	190	1,351	1.5	43	30 %	0.00 %
191	Guam	168,775	0.89 %	1,481	313	540	-506	2.3	31	95 %	0.00 %
192	Curaçao	164,093	0.41 %	669	370	444	515	1.8	42	89 %	0.00 %
193	Kiribati	119,449	1.57 %	1,843	147	810	-800	3.6	23	57 %	0.00 %
194	Micronesia	115,023	1.06 %	1,208	164	700	-600	3.1	24	21 %	0.00 %
195	Grenada	112,523	0.46 %	520	331	340	-200	2.1	32	35 %	0.00 %
196	St. Vincent & Grenadines	110,940	0.32 %	351	284	390	-200	1.9	33	53 %	0.00 %
197	Aruba	106,766	0.43 %	452	593	180	201	1.9	41	44 %	0.00 %
198	Tonga	105,695	1.15 %	1,201	147	720	-800	3.6	22	24 %	0.00 %
199	U.S. Virgin Islands	104,425	-0.15 %	-153	298	350	-451	2.0	43	96 %	0.00 %
200	Seychelles	98,347	0.62 %	608	214	460	-200	2.5	34	56 %	0.00 %
201	Antigua and Barbuda	97,929	0.84 %	811	223	440	0	2.0	34	26 %	0.00 %
202	Isle of Man	85,033	0.53 %	449	149	570		N.A.	N.A.	53 %	0.00 %
203	Andorra	77,265	0.16 %	123	164	470		N.A.	N.A.	88 %	0.00 %
204	Dominica	71,986	0.25 %	178	96	750		N.A.	N.A.	74 %	0.00 %
205	Cayman Islands	65,722	1.19 %	774	274	240		N.A.	N.A.	97 %	0.00 %
206	Bermuda	62,278	-0.36 %	-228	1,246	50		N.A.	N.A.	97 %	0.00 %
207	Marshall Islands	59,190	0.68 %	399	329	180		N.A.	N.A.	70 %	0.00 %
208	Northern Mariana Islands	57,559	0.60 %	343	125	460		N.A.	N.A.	88 %	0.00 %
209	Greenland	56,770	0.17 %	98	0	410,450		N.A.	N.A.	87 %	0.00 %
210	American Samoa	55,191	-0.22 %	-121	276	200		N.A.	N.A.	88 %	0.00 %
211	Saint Kitts & Nevis	53,199	0.71 %	376	205	260		N.A.	N.A.	33 %	0.00 %
212	Faeroe Islands	48,863	0.38 %	185	35	1,396		N.A.	N.A.	43 %	0.00 %
213	Sint Maarten	42,876	1.15 %	488	1,261	34		N.A.	N.A.	96 %	0.00 %
214	Monaco	39,242	0.71 %	278	26,337	1		N.A.	N.A.	N.A.	0.00 %
215	Turks and Caicos	38,717	1.38 %	526	41	950		N.A.	N.A.	89 %	0.00 %
216	Saint Martin	38,666	1.75 %	664	730	53		N.A.	N.A.	0 %	0.00 %
217	Liechtenstein	38,128	0.29 %	109	238	160		N.A.	N.A.	15 %	0.00 %
218	San Marino	33,931	0.21 %	71	566	60		N.A.	N.A.	97 %	0.00 %
219	Gibraltar	33,691	-0.03 %	-10	3,369	10		N.A.	N.A.	N.A.	0.00 %
220	British Virgin Islands	30,231	0.67 %	201	202	150		N.A.	N.A.	52 %	0.00 %
221	Caribbean Netherlands	26,223	0.94 %	244	80	328		N.A.	N.A.	75 %	0.00 %
222	Palau	18,094	0.48 %	86	39	460		N.A.	N.A.	N.A.	0.00 %
223	Cook Islands	17,564	0.09 %	16	73	240		N.A.	N.A.	75 %	0.00 %
224	Anguilla	15,003	0.90 %	134	167	90		N.A.	N.A.	N.A.	0.00 %
225	Tuvalu	11,792	1.25 %	146	393	30		N.A.	N.A.	62 %	0.00 %
226	Wallis & Futuna	11,239	-1.69 %	-193	80	140		N.A.	N.A.	0 %	0.00 %
227	Nauru	10,824	0.63 %	68	541	20		N.A.	N.A.	N.A.	0.00 %
228	Saint Barthelemy	9,877	0.30 %	30	470	21		N.A.	N.A.	0 %	0.00 %
229	Saint Helena	6,077	0.30 %	18	16	390		N.A.	N.A.	27 %	0.00 %
230	Saint Pierre & Miquelon	5,794	-0.48 %	-28	25	230		N.A.	N.A.	100 %	0.00 %
231	Montserrat	4,992	0.06 %	3	50	100		N.A.	N.A.	10 %	0.00 %
232	Falkland Islands	3,480	3.05 %	103	0	12,170		N.A.	N.A.	66 %	0.00 %
233	Niue	1,626	0.68 %	11	6	260		N.A.	N.A.	46 %	0.00 %
234	Tokelau	1,357	1.27 %	17	136	10		N.A.	N.A.	0 %	0.00 %
235	Holy See	801	0.25 %	2	2,003	0		N.A.	N.A.	N.A.	0.00 %

Source: Worldometer (www.Worldometers.info)
Elaboration of data by United Nations, Department of Economic and Social Affairs, Population Division. World Population Prospects: The 2019 Revision. (Medium-fertility variant).
 



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
Country/Territory	UN continental
region[4]	UN statistical
subregion[4]	Population
(1 July 2018)	Population
(1 July 2019)	Change
 China[a]	Asia	Eastern Asia	1,427,647,786	1,433,783,686	+0.43%
 India	Asia	Southern Asia	1,352,642,280	1,366,417,754	+1.02%
 United States	Americas	Northern America	327,096,265	329,064,917	+0.60%
 Indonesia	Asia	South-eastern Asia	267,670,543	270,625,568	+1.10%
 Pakistan	Asia	Southern Asia	212,228,286	216,565,318	+2.04%
 Brazil	Americas	South America	209,469,323	211,049,527	+0.75%
 Nigeria	Africa	Western Africa	195,874,683	200,963,599	+2.60%
 Bangladesh	Asia	Southern Asia	161,376,708	163,046,161	+1.03%
 Russia	Europe	Eastern Europe	145,734,038	145,872,256	+0.09%
 Mexico	Americas	Central America	126,190,788	127,575,529	+1.10%
 Japan	Asia	Eastern Asia	127,202,192	126,860,301	−0.27%
 Ethiopia	Africa	Eastern Africa	109,224,414	112,078,730	+2.61%
 Philippines	Asia	South-eastern Asia	106,651,394	108,116,615	+1.37%
 Egypt	Africa	Northern Africa	98,423,598	100,388,073	+2.00%
 Vietnam	Asia	South-eastern Asia	95,545,962	96,462,106	+0.96%
 DR Congo	Africa	Middle Africa	84,068,091	86,790,567	+3.24%
 Germany	Europe	Western Europe	83,124,418	83,517,045	+0.47%
 Turkey	Asia	Western Asia	82,340,088	83,429,615	+1.32%
 Iran	Asia	Southern Asia	81,800,188	82,913,906	+1.36%
 Thailand	Asia	South-eastern Asia	68,863,514	69,037,513	+0.25%
 United Kingdom	Europe	Northern Europe	67,141,684	67,530,172	+0.58%
 France[b]	Europe	Western Europe	64,990,511	65,129,728	+0.21%
 Italy	Europe	Southern Europe	60,627,291	60,550,075	−0.13%
 South Africa	Africa	Southern Africa	57,792,518	58,558,270	+1.33%
 Tanzania[c]	Africa	Eastern Africa	56,313,438	58,005,463	+3.00%
 Myanmar	Asia	South-eastern Asia	53,708,320	54,045,420	+0.63%
 Kenya	Africa	Eastern Africa	51,392,565	52,573,973	+2.30%
 South Korea	Asia	Eastern Asia	51,171,706	51,225,308	+0.10%
 Colombia	Americas	South America	49,661,048	50,339,443	+1.37%
 Spain[d]	Europe	Southern Europe	46,692,858	46,736,776	+0.09%
 Argentina	Americas	South America	44,361,150	44,780,677	+0.95%
 Uganda	Africa	Eastern Africa	42,729,036	44,269,594	+3.61%
 Ukraine[e]	Europe	Eastern Europe	44,246,156	43,993,638	−0.57%
 Algeria	Africa	Northern Africa	42,228,408	43,053,054	+1.95%
 Sudan	Africa	Northern Africa	41,801,533	42,813,238	+2.42%
 Iraq	Asia	Western Asia	38,433,600	39,309,783	+2.28%
 Afghanistan	Asia	Southern Asia	37,171,921	38,041,754	+2.34%
 Poland	Europe	Eastern Europe	37,921,592	37,887,768	−0.09%
 Canada	Americas	Northern America	37,074,562	37,411,047	+0.91%
 Morocco	Africa	Northern Africa	36,029,093	36,471,769	+1.23%
 Saudi Arabia	Asia	Western Asia	33,702,756	34,268,528	+1.68%
 Uzbekistan	Asia	Central Asia	32,476,244	32,981,716	+1.56%
 Peru	Americas	South America	31,989,260	32,510,453	+1.63%
 Malaysia[f]	Asia	South-eastern Asia	31,528,033	31,949,777	+1.34%
 Angola	Africa	Middle Africa	30,809,787	31,825,295	+3.30%
 Mozambique	Africa	Eastern Africa	29,496,004	30,366,036	+2.95%
 Yemen	Asia	Western Asia	28,498,683	29,161,922	+2.33%
 Ghana	Africa	Western Africa	28,206,728	28,833,629	+2.22%
   Nepal	Asia	Southern Asia	28,095,714	28,608,710	+1.83%
 Venezuela	Americas	South America	28,887,118	28,515,829	−1.29%
 Madagascar	Africa	Eastern Africa	26,262,313	26,969,307	+2.69%
 North Korea	Asia	Eastern Asia	25,549,604	25,666,161	+0.46%
 Ivory Coast	Africa	Western Africa	25,069,230	25,716,544	+2.58%
 Cameroon	Africa	Middle Africa	25,216,267	25,876,380	+2.62%
 Australia[g]	Oceania	Australia and New Zealand	24,898,152	25,203,198	+1.23%
 Taiwan[h]	Asia	Eastern Asia	23,726,460	23,773,876	+0.20%
 Niger	Africa	Western Africa	22,442,822	23,310,715	+3.87%
 Sri Lanka	Asia	Southern Asia	21,228,763	21,323,733	+0.45%
 Burkina Faso	Africa	Western Africa	19,751,466	20,321,378	+2.89%
 Mali	Africa	Western Africa	19,077,749	19,658,031	+3.04%
 Romania	Europe	Eastern Europe	19,506,114	19,364,557	−0.73%
 Malawi	Africa	Eastern Africa	18,143,217	18,628,747	+2.68%
 Chile	Americas	South America	18,729,160	18,952,038	+1.19%
 Kazakhstan	Asia	Central Asia	18,319,618	18,551,427	+1.27%
 Zambia	Africa	Eastern Africa	17,351,708	17,861,030	+2.94%
 Guatemala	Americas	Central America	17,247,849	17,581,472	+1.93%
 Ecuador	Americas	South America	17,084,358	17,373,662	+1.69%
 Netherlands[i]	Europe	Western Europe	17,059,560	17,097,130	+0.22%
 Syria	Asia	Western Asia	16,945,057	17,070,135	+0.74%
 Cambodia	Asia	South-eastern Asia	16,249,792	16,486,542	+1.46%
 Senegal	Africa	Western Africa	15,854,323	16,296,364	+2.79%
 Chad	Africa	Middle Africa	15,477,729	15,946,876	+3.03%
 Somalia	Africa	Eastern Africa	15,008,226	15,442,905	+2.90%
 Zimbabwe	Africa	Eastern Africa	14,438,802	14,645,468	+1.43%
 Guinea	Africa	Western Africa	12,414,293	12,771,246	+2.88%
 Rwanda	Africa	Eastern Africa	12,301,970	12,626,950	+2.64%
 Benin	Africa	Western Africa	11,485,044	11,801,151	+2.75%
 Tunisia	Africa	Northern Africa	11,565,201	11,694,719	+1.12%
 Belgium	Europe	Western Europe	11,482,178	11,539,328	+0.50%
 Bolivia	Americas	South America	11,353,142	11,513,100	+1.41%
 Cuba	Americas	Caribbean	11,338,134	11,333,483	−0.04%
 Haiti	Americas	Caribbean	11,123,178	11,263,770	+1.26%
 South Sudan	Africa	Eastern Africa	10,975,927	11,062,113	+0.79%
 Burundi	Africa	Eastern Africa	10,524,117	10,864,245	+3.23%
 Dominican Republic	Americas	Caribbean	10,627,141	10,738,958	+1.05%
 Czech Republic	Europe	Eastern Europe	10,665,677	10,689,209	+0.22%
 Greece	Europe	Southern Europe	10,522,246	10,473,455	−0.46%
 Portugal[j]	Europe	Southern Europe	10,256,193	10,226,187	−0.29%
 Jordan	Asia	Western Asia	9,965,318	10,101,694	+1.37%
 Azerbaijan[k]	Asia	Western Asia	9,949,537	10,047,718	+0.99%
 Sweden	Europe	Northern Europe	9,971,638	10,036,379	+0.65%
 United Arab Emirates	Asia	Western Asia	9,630,959	9,770,529	+1.45%
 Honduras	Americas	Central America	9,587,522	9,746,117	+1.65%
 Hungary	Europe	Eastern Europe	9,707,499	9,684,679	−0.24%
 Belarus	Europe	Eastern Europe	9,452,617	9,452,411	0.00%
 Tajikistan	Asia	Central Asia	9,100,835	9,321,018	+2.42%
 Austria	Europe	Western Europe	8,891,388	8,955,102	+0.72%
 Papua New Guinea	Oceania	Melanesia	8,606,323	8,776,109	+1.97%
 Serbia[l]	Europe	Southern Europe	8,802,754	8,772,235	−0.35%
  Switzerland	Europe	Western Europe	8,525,611	8,591,365	+0.77%
 Israel	Asia	Western Asia	8,381,516	8,519,377	+1.64%
 Togo	Africa	Western Africa	7,889,093	8,082,366	+2.45%
 Sierra Leone	Africa	Western Africa	7,650,150	7,813,215	+2.13%
 Hong Kong (China)[m]	Asia	Eastern Asia	7,371,730	7,436,154	+0.87%
 Laos	Asia	South-eastern Asia	7,061,507	7,169,455	+1.53%
 Paraguay	Americas	South America	6,956,066	7,044,636	+1.27%
 Bulgaria	Europe	Eastern Europe	7,051,608	7,000,119	−0.73%
 Lebanon	Asia	Western Asia	6,859,408	6,855,713	−0.05%
 Libya	Africa	Northern Africa	6,678,559	6,777,452	+1.48%
 Nicaragua	Americas	Central America	6,465,501	6,545,502	+1.24%
 El Salvador	Americas	Central America	6,420,746	6,453,553	+0.51%
 Kyrgyzstan	Asia	Central Asia	6,304,030	6,415,850	+1.77%
 Turkmenistan	Asia	Central Asia	5,850,901	5,942,089	+1.56%
 Singapore	Asia	South-eastern Asia	5,757,499	5,804,337	+0.81%
 Denmark	Europe	Northern Europe	5,752,126	5,771,876	+0.34%
 Finland[n]	Europe	Northern Europe	5,522,576	5,532,156	+0.17%
 Slovakia	Europe	Eastern Europe	5,453,014	5,457,013	+0.07%
 Congo	Africa	Middle Africa	5,244,359	5,380,508	+2.60%
 Norway[o]	Europe	Northern Europe	5,337,962	5,378,857	+0.77%
 Costa Rica	Americas	Central America	4,999,441	5,047,561	+0.96%
 Palestine[p]	Asia	Western Asia	4,862,979	4,981,420	+2.44%
 Oman	Asia	Western Asia	4,829,473	4,974,986	+3.01%
 Liberia	Africa	Western Africa	4,818,973	4,937,374	+2.46%
 Ireland	Europe	Northern Europe	4,818,690	4,882,495	+1.32%
 New Zealand	Oceania	Australia and New Zealand	4,743,131	4,783,063	+0.84%
 Central African Republic	Africa	Middle Africa	4,666,368	4,745,185	+1.69%
 Mauritania	Africa	Western Africa	4,403,313	4,525,696	+2.78%
 Panama	Americas	Central America	4,176,869	4,246,439	+1.67%
 Kuwait	Asia	Western Asia	4,137,312	4,207,083	+1.69%
 Croatia	Europe	Southern Europe	4,156,405	4,130,304	−0.63%
 Moldova[q]	Europe	Eastern Europe	4,051,944	4,043,263	−0.21%
 Georgia[r]	Asia	Western Asia	4,002,942	3,996,765	−0.15%
 Eritrea	Africa	Eastern Africa	3,452,786	3,497,117	+1.28%
 Uruguay	Americas	South America	3,449,285	3,461,734	+0.36%
 Bosnia and Herzegovina	Europe	Southern Europe	3,323,925	3,301,000	−0.69%
 Mongolia	Asia	Eastern Asia	3,170,216	3,225,167	+1.73%
 Armenia	Asia	Western Asia	2,951,745	2,957,731	+0.20%
 Jamaica	Americas	Caribbean	2,934,847	2,948,279	+0.46%
 Puerto Rico (United States)	Americas	Caribbean	3,039,596	2,933,408	−3.49%
 Albania	Europe	Southern Europe	2,882,740	2,880,917	−0.06%
 Qatar	Asia	Western Asia	2,781,682	2,832,067	+1.81%
 Lithuania	Europe	Northern Europe	2,801,264	2,759,627	−1.49%
 Namibia	Africa	Southern Africa	2,448,301	2,494,530	+1.89%
 Gambia	Africa	Western Africa	2,280,094	2,347,706	+2.97%
 Botswana	Africa	Southern Africa	2,254,068	2,303,697	+2.20%
 Gabon	Africa	Middle Africa	2,119,275	2,172,579	+2.52%
 Lesotho	Africa	Southern Africa	2,108,328	2,125,268	+0.80%
 North Macedonia	Europe	Southern Europe	2,082,957	2,083,459	+0.02%
 Slovenia	Europe	Southern Europe	2,077,837	2,078,654	+0.04%
 Guinea-Bissau	Africa	Western Africa	1,874,303	1,920,922	+2.49%
 Latvia	Europe	Northern Europe	1,928,459	1,906,743	−1.13%
 Bahrain	Asia	Western Asia	1,569,446	1,641,172	+4.57%
 Trinidad and Tobago	Americas	Caribbean	1,389,843	1,394,973	+0.37%
 Equatorial Guinea	Africa	Middle Africa	1,308,975	1,355,986	+3.59%
 Estonia	Europe	Northern Europe	1,322,920	1,325,648	+0.21%
 East Timor	Asia	South-eastern Asia	1,267,974	1,293,119	+1.98%
 Mauritius[s]	Africa	Eastern Africa	1,189,265	1,198,575	+0.78%
 Cyprus[t]	Asia	Western Asia	1,170,125	1,179,551	+0.81%
 Eswatini	Africa	Southern Africa	1,136,281	1,148,130	+1.04%
 Djibouti	Africa	Eastern Africa	958,923	973,560	+1.53%
 Fiji	Oceania	Melanesia	883,483	889,953	+0.73%
 Réunion (France)	Africa	Eastern Africa	882,526	888,927	+0.73%
 Comoros	Africa	Eastern Africa	832,322	850,886	+2.23%
 Guyana	Americas	South America	779,006	782,766	+0.48%
 Bhutan	Asia	Southern Asia	754,388	763,092	+1.15%
 Solomon Islands	Oceania	Melanesia	652,857	669,823	+2.60%
 Macau (China)[u]	Asia	Eastern Asia	631,636	640,445	+1.39%
 Montenegro	Europe	Southern Europe	627,809	627,987	+0.03%
 Luxembourg	Europe	Western Europe	604,245	615,729	+1.90%
 Western Sahara	Africa	Northern Africa	567,402	582,463	+2.65%
 Suriname	Americas	South America	575,990	581,372	+0.93%
 Cape Verde	Africa	Western Africa	543,767	549,935	+1.13%
 Maldives	Asia	Southern Asia	515,696	530,953	+2.96%
 Guadeloupe (France)[v]	Americas	Caribbean	446,928	447,905	+0.22%
 Malta	Europe	Southern Europe	439,248	440,372	+0.26%
 Brunei	Asia	South-eastern Asia	428,963	433,285	+1.01%
 Belize	Americas	Central America	383,071	390,353	+1.90%
 Bahamas	Americas	Caribbean	385,637	389,482	+1.00%
 Martinique (France)	Americas	Caribbean	375,673	375,554	−0.03%
 Iceland	Europe	Northern Europe	336,713	339,031	+0.69%
 Vanuatu	Oceania	Melanesia	292,680	299,882	+2.46%
 Barbados	Americas	Caribbean	286,641	287,025	+0.13%
 New Caledonia (France)	Oceania	Melanesia	279,993	282,750	+0.98%
 French Guiana (France)	Americas	South America	275,713	282,731	+2.55%
 French Polynesia (France)	Oceania	Polynesia	277,679	279,287	+0.58%
 Mayotte (France)	Africa	Eastern Africa	259,531	266,150	+2.55%
 São Tomé and Príncipe	Africa	Middle Africa	211,028	215,056	+1.91%
 Western Samoa	Oceania	Polynesia	196,129	197,097	+0.49%
 Saint Lucia	Americas	Caribbean	181,889	182,790	+0.50%
 Channel Islands (United Kingdom)[w]	Europe	Northern Europe	170,499	172,259	+1.03%
 Guam (United States)	Oceania	Micronesia	165,768	167,294	+0.92%
 Curaçao (Netherlands)	Americas	Caribbean	162,752	163,424	+0.41%
 Kiribati	Oceania	Micronesia	115,847	117,606	+1.52%
 F.S. Micronesia	Oceania	Micronesia	112,640	113,815	+1.04%
 Grenada	Americas	Caribbean	111,454	112,003	+0.49%
 Tonga	Oceania	Polynesia	110,589	110,940	+0.32%
 Saint Vincent and the Grenadines	Americas	Caribbean	110,211	110,589	+0.34%
 Aruba (Netherlands)	Americas	Caribbean	105,845	106,314	+0.44%
 U.S. Virgin Islands (United States)	Americas	Caribbean	104,680	104,578	−0.10%
 Seychelles	Africa	Eastern Africa	97,096	97,739	+0.66%
 Antigua and Barbuda	Americas	Caribbean	96,286	97,118	+0.86%
 Isle of Man (United Kingdom)	Europe	Northern Europe	84,077	84,584	+0.60%
 Andorra	Europe	Southern Europe	77,006	77,142	+0.18%
 Dominica	Americas	Caribbean	71,625	71,808	+0.26%
 Cayman Islands (United Kingdom)	Americas	Caribbean	64,174	64,948	+1.21%
 Bermuda (United Kingdom)	Americas	Northern America	62,756	62,506	−0.40%
 Marshall Islands	Oceania	Micronesia	58,413	58,791	+0.65%
 Greenland (Denmark)	Americas	Northern America	56,564	56,672	+0.19%
 Northern Mariana Islands (United States)	Oceania	Micronesia	56,882	56,188	−1.22%
 American Samoa (United States)	Oceania	Polynesia	55,465	55,312	−0.28%
 Saint Kitts and Nevis	Americas	Caribbean	52,441	52,823	+0.73%
 Faroe Islands (Denmark)	Europe	Northern Europe	48,497	48,678	+0.37%
 Sint Maarten (Netherlands)	Americas	Caribbean	41,940	42,388	+1.07%
 Monaco	Europe	Western Europe	38,682	38,964	+0.73%
 Turks and Caicos Islands (United Kingdom)	Americas	Caribbean	37,665	38,191	+1.40%
 Liechtenstein	Europe	Western Europe	37,910	38,019	+0.29%
 San Marino	Europe	Southern Europe	33,785	33,860	+0.22%
 Gibraltar (United Kingdom)	Europe	Southern Europe	33,718	33,701	−0.05%
 British Virgin Islands (United Kingdom)	Americas	Caribbean	29,802	30,030	+0.77%
 Caribbean Netherlands (Netherlands)[x]	Americas	Caribbean	25,711	25,979	+1.04%
 Palau	Oceania	Micronesia	17,907	18,008	+0.56%
 Cook Islands (New Zealand)	Oceania	Polynesia	17,518	17,548	+0.17%
 Anguilla (United Kingdom)	Americas	Caribbean	14,731	14,869	+0.94%
 Tuvalu	Oceania	Polynesia	11,508	11,646	+1.20%
 Wallis and Futuna (France)	Oceania	Polynesia	11,661	11,432	−1.96%
 Nauru	Oceania	Micronesia	10,670	10,756	+0.81%
 Saint Helena (United Kingdom)[y]	Africa	Western Africa	6,035	6,059	+0.40%
 Saint Pierre and Miquelon (France)	Americas	Northern America	5,849	5,822	−0.46%
 Montserrat (United Kingdom)	Americas	Caribbean	4,993	4,989	−0.08%
 Falkland Islands (United Kingdom)	Americas	South America	3,234	3,377	+4.42%
 Niue (New Zealand)	Oceania	Polynesia	1,620	1,615	−0.31%
 Tokelau (New Zealand)	Oceania	Polynesia	1,319	1,340	+1.59%
  Vatican City[z]	Europe	Southern Europe	801	799	−0.25%

Rank	Urban area	Image	State	Population (urban areas; Demographia)[2]	ESPON Population (Functional Urban Area)[4]	Population (agglomerations; UN WUP)[3]	FUA population (metropolitan areas; Eurostat)[1]	Density
(per km2; Demographia)	Annual growth
rate (%;
Demographia)
1	Paris	Paris - Eiffelturm und Marsfeld2.jpg	France	11,020,000	11,175,000	10,843,285	11,002,000	3,800	0.83
2	Ruhr (multiple cities)	Essen-Südviertel Luft.jpg	Germany	6,125,000	5,376,000	N/A	11,300,000	2,800	0.01
3	Madrid	Madrid-Azca-Castellana-170913.jpg	Spain	6,026,000	5,263,000	6,729,254	7,100,000	4,600	0.27
4	Milan	Skyline Milano - 05.JPG	Italy	4,907,000	7,636,000	3,098,974	7,465,000	2,800	−0.16
5	Barcelona	Central business district of Barcelona (2).JPG	Spain	4,588,000	4,082,000	5,658,319	5,900,000	4,300	0.12
6	Berlin	Cityscape Berlin.jpg	Germany	3,972,000	4,016,000	3,863,194	n/a	2,900	0.01
7	Naples	Napoli.jpg	Italy	3,574,000	3,714,000	2,201,789	n/a	3,600	0.01
8	Athens	Attica 06-13 Athens 36 View from Lycabettus.jpg	Greece	3,325,000	3,761,000	3,051,899	n/a	5,000	0.29
9	Rome	Colosseo 2020.jpg	Italy	3,189,000	5,190,000	3,717,956	n/a	3,400	0.89
10	Rotterdam–The Hague	RotterdamMaasNederland.jpg
Cityscape of The Hague, viewed from Het Plein (The Square).jpg	Netherlands	2,770,000	1,904,000	N/A	n/a	2,700	0.39
11	Lisbon	Aerial view of Augusta Street, Lisbon (50644280948).jpg	Portugal	2,656,000	2,591,000	2,884,297	n/a	2,800	0.39
12	Budapest	Parlement van Boedapest gelegen aan de Donau.jpg	Hungary	2,395,000	2,523,000	1,713,903	3,100,000	1,900	−0.19
13	Cologne-Bonn	Bonn Kreuzbauten Post Tower.jpg	Germany	2,085,000	3,070,000	N/A	n/a	2,300	0.50
14	Brussels	Brussels skyline gp.jpg	Belgium	1,990,000	2,639,000	2,044,993	n/a	2,600	0.02[5]
15	Hamburg	Hamburg, Speicherstadt, Wasserschloss -- 2016 -- 3230-6.jpg	Germany	1,976,000	2,983,000	1,830,673	n/a	2,700	0.43[5]
16	Warsaw	Panorama siekierkowski.jpg	Poland	1,935,000	2,785,000	1,722,310	3,000,000	3,200	0.67
17	Munich	Stadtbild München.jpg	Germany	1,928,000	2,665,000	1,437,900	n/a	4,200	0.72[5]
18	Frankfurt	Skyline Frankfurt am Main.jpg	Germany	1,904,000	2,764,000	n/a	n/a	3,000	0.50
19	Bucharest	Palatul Parlamentului 1.jpg	Romania	1,870,000	2,064,000	1,867,724	n/a	6,500	0.10[5]
20	Vienna		Austria	1,809,000	2,584,000	1,752,845	n/a	3,900	1.04[5]
21	Katowice (Katowice urban area)	Katowice Rynek.jpg	Poland	1,726,000	3,029,000	N/A	n/a	3,300	0.11
22	Turin	Turin monte cappuccini.jpg	Italy	1,445,000	1,601,000	1,764,868	n/a	4,100	−0.16[5]
23	Stockholm	Gamla Stan swe.jpg	Sweden	1,436,000	2,171,000	1,485,680	n/a	4,300	0.58[5]
24	Lyon	Lyon - La Part-Dieu de nuit - 07-12-2009.jpg	France	1,413,000	1,669,000	1,608,712	n/a	1,300	0.50[5]
25	Valencia	Valencia west night.jpg	Spain	1,393,000	1,398,000		n/a	5,700	0.29[5]
26	Marseille	Coucher de soleil sur Notre-Dame de la Garde.JPG	France	1,330,000	1,530,000	1,605,046	n/a	3,100	0.46[5]
27	Porto	Cais da Ribeira, Oporto, Portugal, 2012-05-09, DD 17.JPG	Portugal	1,323,000	1,245,000	1,299,437	n/a	1,900	
28	Copenhagen	Nyhavn MichaD.jpg	Denmark	1,321,000	2,350,000	1,268,052	1,900,000	2,700	0.04[5]
29	Dublin	View of Dublin, looking east from Sean O’Casey Bridge 20150807 1.jpg	Ireland	1,306,000	1,477,000	1,169,371	n/a	2,500	1.14[5]
30	Stuttgart	Stuttgart AltesSchloss03.JPG	Germany	1,301,000	2,289,000		n/a	2,900	
31	Helsinki	Helsinki July 2013-27a.jpg	Finland	1,282,000	1,285,000	1,179,916	1,495,271	2,400	0.81[5]
32	Lille	Lille vue gd place.JPG	France, Belgium	1,270,000	1,379,000	1,027,178	n/a	2,200	0.50[5]
33	Prague	Prague-IMG 1307-Pano-web-X3.jpg	Czechia	1,158,000	1,669,000	2,156,809	2,620,000	4,600	−0.07[5]
34	Amsterdam	ZuidasAmsterdamtheNetherlands.jpg	Netherlands	1,140,000	2,497,000	1,090,772	n/a	3,200	0.41[5]
35	Seville	19060879124 a5eac59dea o feria abril sevilla 2013.jpg	Spain	1,039,000	1,180,000		n/a	5,600	
36	Antwerp	MAS Antwerpen 2016-05 --1.jpg	Belgium	1,013,000	1,406,000		n/a	1,500	0.05[5]
37	Nice	Nice Port 1.jpg	France	955,000	1,082,000		n/a	1,300	0.52[5]
38	Toulouse	Toulouse by night with Basilique Saint-Sernin.jpg	France	944,000	832,000		n/a	1,100	0.72[5]
39	Sofia	AlexanderNevskyCathedral-Sofia-6.jpg	Bulgaria	934,000	1,174,000	1,226,155	1,543,377	5,700	0.78[5]
40	Bergamo	Italia Bergamo 03.JPG	Italy	880,000	662,000		n/a	3,300	
41	Gdańsk (Tricity)	Calle Dlugie Pobrzeze, Gdansk, Polonia, 2013-05-20, DD 06.jpg	Poland	855,000	993,000		n/a	5,000	
42	Thessaloniki	Salonica-view-aerial2.jpg	Greece	845,000	1,052,000		n/a	4,300	0.39[5]
43	Florence	Florence Cathedral.jpg	Italy	835,000	645,000		n/a	3,700	
44	Bordeaux	Bordeaux place de la bourse with tram.JPG	France	823,000	918,000		1,244,264	700	0.60[5]
45	Bilbao	Ayuntamiento-bilbao1.jpg	Spain	765,000	947,000		n/a	5,800	
46	Kraków	Rynek Glowny w Krakowie.jpg	Poland	765,000	1,236,000	1,725,894	n/a	3,500	
47	Dresden	Dresden Überblick 12.jpg	Germany	765,000	882,000		n/a	2,200	
48	Zaragoza	0849 pilar ebro 2004.png	Spain	735,000	639,000		n/a	5,700	
49	Palermo	Palermo panorama.JPG	Italy	725,000	861,000		n/a	6,000	0.12[5]
50	Catania	Catania anfiteatro romano2423.jpg	Italy	725,000	707,000		n/a	2,900	
51	Málaga	Palacio de Ferias y Congresos de Málaga.jpg	Spain	720,000	944,000		n/a	3,600	
52	Utrecht	Stadhuis Utrecht.JPG	Netherlands	715,000	692,000		n/a	3,900	
53	Hanover	Hannover Altstadt 128-h.jpg	Germany	710,000	997,000		n/a	2,500	
54	Zagreb	Zageb Croatian National Theater.jpg	Croatia	700,000	1,107,115		n/a	4,400	
55	Łódź	Manufaktura panorama Łódź.jpg	Poland	670,000	1,165,000		n/a	5,000	
56	Las Palmas	Auditorio alfredo kraus las palmas de gran canaria.jpg	Spain	670,000	640,000		n/a	6,800	
57	Nuremberg	Nuremberg panorama morning 3.jpg	Germany	665,000	1,443,000		n/a	3,000	
58	Bremen	Bremen Altstadt (5438245111).jpg	Germany	645,000	1,077,000		n/a	2,400	
59	Wrocław	Wroclaw 1.jpg	Poland	625,000	861,000		n/a	4,800	
60
Leipzig	Leipzig Burgplatz Panorama.jpg	Germany	625,000	842,000		1,037,782	2,000	
61	Mannheim	Mannheim Friedrichsplatz 2005 Richtung Augustaanlage.jpg	Germany	625,000	683,000		1,184,343	3,500	
62	Padua	Padua5.jpg	Italy	620,000	549,000		n/a	3,200	
63	Gothenburg	Älvsborgsbron.jpg	Sweden	615,000	759,000		n/a	2,700	
64	Genoa	Genova-Panorama dalla collina di Camandoli.jpg	Italy	610,000	694,000	1,500,000	n/a	7,900	
65	Riga	Riga - House of Blackheads.jpg	Latvia	605,000	1,195,000		n/a	2,900	
66	Toulon	Toulon Faron3 P1440701-P1440708.jpg	France	580,000	518,000		n/a	700	
67	Liège	Eglise-liege-stbarthelemy-juin2006.jpg	Belgium	565,000	750,000		n/a	1,900	
68	Saarbrücken	SB-Rathaus.jpg	Germany	565,000	1,102,000		n/a	2,200	
69	Nantes	Quai de la Fosse (de la butte Saint-Anne)- Nantes.jpg	France	562,000	708,000		n/a	1,100	
70	Palma, Majorca	Bellver Castle 2008 Palma Mallorca 130.JPG	Spain	560,000	433,000				
71	Aachen	Aachen Rathaus pano.jpg	Germany	545,000	672,000		n/a	1,500	
72	Santa Cruz de Tenerife	Tres de Mayo 03.jpg	Spain	540,000	399,000				
73	Bologna	Bologna Panorama.jpg	Italy	530,000	690,000				
74	Grenoble	Seilbahn-Grenoble.JPG	France	530,000	555,000		n/a	985	
75	Poznań	6 Poznan 015.jpg	Poland	525,000	919,000		n/a	2,700	
76	Murcia	Murcia.JPG	Spain	525,000	504,000				
77	Vilnius	Vilnius view.jpg	Lithuania	515,000	680,000	649,000	n/a	2,500	
78	Douai-Lens	Douai - office de tourisme (3).jpgJean Jaurès square, Lens.jpg	France	510,000	550,000		n/a	1,100	
79	Karlsruhe	Schloss Karlsruhe und Fächerstadt 2.jpg	Germany	500,000	842,000				
Other notable urban areas
Urban area	Image	State	ESPON Population (Functional Urban Area)[4]	FUA population (metropolitan areas; Eurostat)[1]
Oviedo–Gijón–Avilés	Santa María del Naranco. Oviedo.jpg	Spain	844,000	
Alicante-Elche-Elda	Alicante, Spain.jpg	Spain	793,000	
Granada	Granada-Day1-10 (47996234956).jpg	Spain	440,000	
Vigo metropolitan area	Vigo panoramico.jpg	Spain	413,000	
Cartagena	Teatro romano cartagena 1.jpg	Spain	409,000	
Cádiz	Cadiz aerea.jpg	Spain	400,000	
San Sebastián metropolitan area	San Sebastian aerial 7906a.jpg	Spain	403,000*	(403,000)
A Coruña	Torre de Hércules, La Coruña, España, 2015-09-25, DD 35-37 HDR.jpg	Spain	376,000	(408,00)
Valladolid	Ayuntamiento de la ciudad en la Plaza Mayor de Valladolid.jpg	Spain	369,000	(395,984)
Tarragona–Reus	Tarragona9.jpg	Spain	325,000	(423,360)
Malmö	Central Malmö.JPG	Sweden	658,050	
Tampere	Tampere from Näsinneula.jpg	Finland	440,372	
Aarhus	Havne udsigt fra dokken.jpg	Denmark	845,971	
Charleroi	Charleroi vu depuis Couillet cropped.jpg	Belgium	489,264	
Odense	Odense - Sankt Knuds kirke 2005-07-16.jpeg	Denmark	485,672	
Ostrava	Masarykova namesti Ostrava 2009.JPG	Czech Republic	709,768	
Braunschweig	Braunschweig Luftaufnahme Innenstadt (2011).JPG	Germany		997,089
Brno	Justiční palác v Brně.jpg	Czech Republic		735,652
Bari	Bari BW 2016-10-19 12-32-30.jpg	Italy		744,564
Eindhoven	Hoogbouw Eindhoven overzicht.jpg	Netherlands		761,702
Rouen	Cathédrale de Rouen vue de l'Opéra.JPG	France		694,558
Montpellier	Montpellier Place de la Comédie.jpg	France		709,347
Heidelberg	Heidelberg corr.jpg	Germany		707,346
Lublin	Royal Castle in Lublin.JPG	Poland		668,346
Rennes	Rennes de hermitage 2.JPG	France		684,304
Augsburg	Augsburg - Markt.jpg	Germany		675,285
Kiel	KielerStadtzentrumLuftaufnahme.jpg	Germany		649,807[6]
Ghent	Gent.graslei.jpg	Belgium		399,741
Catania	Catania-Etna-Sicilia-Italy-Castielli CC0 HQ1.JPG	Italy		656,989
World			7,631,091,040	7,713,468,100	+1.08%
 

about | faq | languages | contact
  
© Copyright Worldometers.info - All rights reserved - Disclaimer & Privacy Policy
"""

data = data.replace(",", "")
data = data.replace(".", "")

numbers = re.findall(r'\d+', data, re.M | re.I)
print(numbers)

count = {}

for number in numbers:
    if count.get(number[0]) is None:
        count[number[0]] = 0
    else:
        count[number[0]] += 1
    print(number[0], number)

print(count)
