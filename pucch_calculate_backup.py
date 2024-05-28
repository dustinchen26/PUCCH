"""
spec 38.213 chap 9.2.3  UE procedure for reporting HARQ-ACK 

"""
import math

R_PUCCH=14
delta_PRI=7
N_CCE=45
n_cce=24

def main():
    if( delta_PRI < (R_PUCCH % 8) ) :
        r_pucch=math.floor((n_cce*math.ceil(R_PUCCH/8))/N_CCE)+delta_PRI*math.ceil(R_PUCCH/8)
    else :
        r_pucch=math.floor((n_cce*math.floor(R_PUCCH/8))/N_CCE)+delta_PRI*math.floor(R_PUCCH/8)+(R_PUCCH % 8)
    
    print("r_pucch = ", r_pucch)

if __name__ == "__main__":
   # calling main function
   main()