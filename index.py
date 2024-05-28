"""
38.213 chap 9.2.3  UE procedure for reporting HARQ-ACK 
ex:

// rantcp RRC Setup	=> N_CCE=45 
330	F1AP/NR RRC	SACK (Ack=4, Arwnd=352516352) , DLRRCMessageTransfer, RRC Setup																																	
controlResourceSetToAddModList: 1 item
    Item 0
        ControlResourceSet
            controlResourceSetId: 1
            frequencyDomainResources: fffffffffff8 [bit length 45, 3 LSB pad bits, 1111 1111  1111 1111  1111 1111  1111 1111  1111 1111  1111 1... decimal value 35184372088831]

// rantcp RRC Setup	=> R_PUCCH=14
330	F1AP/NR RRC	SACK (Ack=4, Arwnd=352516352) , DLRRCMessageTransfer, RRC Setup																																	
PUCCH-ResourceSet
    pucch-ResourceSetId: 0
    resourceList: 14 items

// bbuiolog (961,7,1) delta_PRI=7, n_cce=36
No.	Protocol	Info	SFN	SF	Slot index	PUCCH Resource Indicator	CCE Index	HARQ Process
9078	NR_INFO	[DL_CONFIG.req]	961	7	1	7	36	2																			

// calculate python Result:
python .\pucch_calculate.py
r_pucch =  13
            
// rantcp RRC Setup	=> startingPRB: 18
330	F1AP/NR RRC	SACK (Ack=4, Arwnd=352516352) , DLRRCMessageTransfer, RRC Setup																																	                
Item 13
    PUCCH-Resource
        pucch-ResourceId: 13
        startingPRB: 18
        format: format0 (0)
            format0
                initialCyclicShift: 1
                nrofSymbols: 1
                startingSymbolIndex: 12
                
// UE viavi log: 0x40000 = startingPRB: 18
SFN	Subframe	Slot Index	Channel	HARQ	RETRY	DCI	UCI	RB_ALLOC_E
961	9	1	PUCCH	-	-		FMT[FORMAT 0] PG[PUCCH group 1] CSI[1] NRS[1] ACK[1] TXP[-55.15] CRC[0] 	0x0000000000000000000000000000000000000000000000000000000000000000040000
"""

import math

def main():
    N_CCE = int(input("請輸入 N_CCE: "))
    R_PUCCH = int(input("請輸入 R_PUCCH: "))
    delta_PRI = int(input("請輸入 delta_PRI: "))
    n_cce = int(input("請輸入 n_cce: "))

    if delta_PRI < (R_PUCCH % 8):
        r_pucch = math.floor((n_cce * math.ceil(R_PUCCH / 8)) / N_CCE) + delta_PRI * math.ceil(R_PUCCH / 8)
    else:
        r_pucch = math.floor((n_cce * math.floor(R_PUCCH / 8)) / N_CCE) + delta_PRI * math.floor(R_PUCCH / 8) + (R_PUCCH % 8)

    print("r_pucch =", r_pucch)

if __name__ == "__main__":
    # 呼叫主要函式
    main()
