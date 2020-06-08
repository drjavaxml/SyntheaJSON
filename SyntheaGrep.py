import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sys
import time
import os
import re
import time
import json
import FHIR_util as fu
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


#TODO  Add the final numbers calculator

DataDir = "C:\\Users\\phend\\PycharmProjects\\SyntheaJSON\\fhir\\"
# ParseExp= "$..resource[?(@.resourceType == 'Encounter')]..coding..display"
SearchString = "Rheumatoid"
#cohort_info = []
cohort_dict = {"0":["0"]}

def data_run():
    txt_edit.delete('1.0', tk.END)
    global r
    files = os.listdir(DataDir)
    filecount = 0
    SearchString = search_edit.get()
    for file in files:
        #print('---------------------------------------------------------------------------')
        if ("json" in file):
            filecount += 1
            filecount_str = str(filecount)
            # print("Is it File?" + str(os.path.isfile(DataDir + file)))
            goodfile = (DataDir + file)
            opfile = open(goodfile, mode='r')
            try:
                flstring = opfile.read()
            except:-
                print("fail to read " + goodfile)
            outstr = ""
            if (flstring.lower().find(SearchString.lower()) != -1):
                list = cohort_dict.get(filecount_str)
                if(list is None):
                    list = [SearchString.lower()]
                    cohort_dict.update({filecount_str:list})
                else:
                    list = cohort_dict.get(filecount_str)
                    list.append(SearchString.lower())
                    cohort_dict.update({filecount_str: list})
            else:
                placeholder = "this is just a place holder for now"

    for x, y in cohort_dict.items():
        print(x, y)
        outstr = x + str(y) + "\n"
        txt_edit.insert(tk.END, outstr)



def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def pick_dir():
    DataDir = tk.filedialog.askdirectory()
    print(DataDir)

def count_cohort():
    txt_edit.delete('1.0', tk.END)
    cohorts_dict = {}
    dx_string = search_edit.get()
    cohorts_dict.update({dx_string: 0})
    cohort1_mask = re.split('-+', dx_string)

    print(dx_string)
    for key, dxs in cohort_dict.items():
        dx_list = dxs
        res_mask = (set(cohort1_mask) - set(dx_list))
        if len(res_mask) == 0:
            count = cohorts_dict.get(dx_string)
            count += 1
            cohorts_dict.update({dx_string: count})
    print(cohorts_dict)
    co_show = json.dumps(cohorts_dict)
    txt_edit.insert(tk.END, co_show)


window = tk.Tk()
window.title("Synthea Data Sub String Searcher")
window.rowconfigure(0, minsize=1, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=5)
window.columnconfigure(1, weight=2)



search_edit = tk.Entry(window)
search_edit.place(height=50)
txt_edit = tk.Text(window)
json_label = tk.Label(text="Enter A Search String")




fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_run = tk.Button(fr_buttons, text="DataRun", command=data_run)
btn_pic = tk.Button(fr_buttons, text="Pick Data Dir", command=pick_dir)
btn_calc = tk.Button(fr_buttons, text="Count A Cohort", command=count_cohort)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_run.grid(row=2, column=0, sticky="ew", padx=5)
btn_pic.grid(row=3, column=0, sticky="ew", padx=5)
btn_calc.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=2, column=0, sticky="ns")
json_label.grid(row=0, column=1)
search_edit.grid(row=1, column=1, columnspan=4, sticky="ew", padx=5, pady=5)
txt_edit.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
search_edit.insert('0', "snomed")

window.mainloop()


