import os
import sys
import json

result_list = []

D1 = "Rheumatoid Arthritis"  # Disease One
D2 = "COPD"  # Disease Two
Rx = "TNF inh Product"  # Treatment for Disease One
Cx = "Bacterial Pneumonia"  # Complication of Rx

TFFF = 0 # COPD RA TNF BACT
TFFT = 0
FTFF = 0
FTFT = 0
FTTF = 0
FTTT = 0
TTFF = 0
TTFT = 0
TTTF = 0
TTTT = 0


files = os.listdir("./output/fhir/")

file_count = 0
for file in files:
  if("json" in file):      
    #print("============New File==========")
    #print(file)
    file_count+=1
    D2B = False  # Disease two Boolean etc
    D1B = False
    RxB = False 
    CxB = False
    #print(file_count , ":File Count")
    with open(file) as j:     
        d1 = json.load(j)
        l1 = d1['entry']
        for d2 in l1:
            d3 = d2['resource']
    
            if(d3['resourceType'] == 'Condition'):  # Here d3 means the third level nested dictionary
                d3_cond = d3
                d3_code = d3_cond['code']      
                d3_text = d3_code['text']
                #print(d3_text)
                cnd = d3_text
                
                if(cnd == D1):
                    D1B = True
                           
                if(cnd == D2):
                    D2B = True
                           
                if(cnd == Cx):
                    CxB = True
                           
                if(cnd == Rx):
                    RxB = True
                               
                #print(COPD, RA, TNF, BACT)
                
                result = [D2B, D1B, RxB, CxB]  # For some reason I put D2 first?
                
                result_list.append(result)  # All the patients in this list ready for counting cohorts
                
#print(result_list)

for list in result_list:
    if (list == [True, False, False, False]):
        TFFF += 1
        
    if (list == [True, False, False, True]):
        TFFT += 1
                                        
    if (list == [False, True, False, False]):
        FTFF += 1
                    
    if (list == [False, True, False, True]):
        FTFT += 1
                    
    if (list == [False, True, True, False]):
        FTTF += 1
                    
    if (list == [False, True, True, True]):
        FTTT += 1
                    
    if (list == [True, True, False, False]):
        TTFF += 1
                    
    if (list == [True, True, True, False]):
        TTTF += 1
                    
    if (list == [True, True, True, True]):
        TTTT += 1
        
    if (list == [True, True, False, True]):
        TTFT += 1    
 

D1risk = TFFT / (TFFT + TFFF)
print ( D1 , " risk:" , D1risk)

D2risk = FTFT / (FTFT + FTFF)
print ( D2 , " risk:" , D2risk)

D1_Cxrisk = FTTT / (FTTT + FTTF)      
print (D1 , " " , Rx,  " risk:" , D1_Cxrisk)

D1_D2risk = TTFT / (TTFT+TTFF)
print( D1, " " , D2,  " risk:" , D1_D2risk)

D1_D2_Rxrisk = TTTT /(TTTT + TTTF)
print ( D1, " ", D2, " ", Rx, " risk:" , D1_D2_Rxrisk)

RiskRatio = D1_D2_Rxrisk / D1_D2risk
print ("Risk Ratio:" , RiskRatio)
                    
                    
                    
           
      

      
                