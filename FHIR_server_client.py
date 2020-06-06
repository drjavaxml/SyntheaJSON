import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sys
import time
import os
import time
import json
import requests
import urllib
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

#FHIR_Server = "http://browser.ihtsdotools.org/fhir/ValueSet/$expand?url=http://snomed.info/sct?fhir_vs=ecl/"
FHIR_Server = "https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN/2020-03-09/concepts?module=900000000000207008&ecl="






# ParseExp= "$..resource[?(@.resourceType == 'Encounter')]..coding..display"
ParseExp1 = "$..fsn..term"
ParseExp2 = "$..conceptId"

def clear_all():
    ecl_edit.delete(0, 'end')
    result_edit.delete(1.0, 'end')
def send_fhir():

    ECL = ecl_edit.get()
    #ECL = urllib.parse.quote(pre_ECL)
    URL = FHIR_Server + ECL
    OUT = ""
    #OUT += ECL
    print(URL)
    print()
    OUT += URL + "\n\n"

    req = requests.get(url = URL)
    datas = req.text
    print(datas)
    data = json.loads(datas)
    print(data)
    #OUT += json.dumps(data) + "\n"    #this dumps the whole json result
    #OUT += "\n\n\n"
    #OUT += "-------------------------------------------------------"
    #SOUT += "\n\n\n"
    print()
    path1 = parse(ParseExp1)
    path2 = parse(ParseExp2)

    results1 = [match.value for match in path1.find(data)]
    results2 = [match.value for match in path2.find(data)]

    len1 = len(results1)
    len2 = len(results2)

    if(len(results1) == len(results2)):
        for i in range(len(results2)):  # resutls1 is longer than results2
            print(results1[i] + " : " + results2[i])
            OUT += results1[i] + " : " + results2[i] + "\n"

        print(len(results1), "  " + "results")
        OUT += str(len(results1))
        OUT += "  results"
        print(OUT)
        result_edit.insert('1.0', OUT)
        # print("function done OK ======================================")


window = tk.Tk()
window.title("FHIR ECL Client")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=900, weight=1)

ecl_edit = tk.Entry(window)
result_edit = tk.Text(window, height=35, width=80)
ecl_edit.insert(0, "<< 64572001|Disease| : (<< 363698007|Finding site| = << 39352004|Joint structure|, 116676008|Associated morphology| = 409774005|Inflammatory morphology|, << 370135005|Pathological process| = << 769247005|Abnormal immune process|)")
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_run = tk.Button(fr_buttons, text="Send Request", command=send_fhir)
btn_run.grid(row=2, column=0, sticky="ew", padx=5)
btn_clear= tk.Button(fr_buttons, text="Reset", command=clear_all)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
ecl_edit.grid(row=0, column=1, sticky="nsew")
result_edit.grid(row=1, column=1, sticky="nsew")

window.mainloop()
