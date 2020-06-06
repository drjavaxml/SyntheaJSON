import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sys
import time
import os
import time
import json
import FHIR_util as fu
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

DataDir = "C:\\Users\\phend\\PycharmProjects\\SyntheaJSON\\"
Code1 = '69896004'
Name1 = "RA"
# ParseExp= "$..resource[?(@.resourceType == 'Encounter')]..coding..display"
ParseExp = "$"

def myfunc():
    global r
    files = os.listdir(DataDir)
    filecount = 0
    ParseExp = jsonpath_edit.get()
    for file in files:
        filecount += 1
        #print('---------------------------------------------------------------------------')
        if ("json" in file):
            # print("Is it File?" + str(os.path.isfile(DataDir + file)))
            goodfile = (DataDir + file)
            opfile = open(goodfile, mode='r')
            flstring = opfile.read()

            time.sleep(0.25)  # crashes without this

            try:
                jsonObj = json.loads(flstring)
            except:
                print(flstring)

            parseExpression = ParseExp
            print(ParseExp)

            path = parse(parseExpression)

            results = [match.value for match in path.find(jsonObj)]
            outstr = ""
            for r in results:
                print(r)
                rstr= json.dumps(r)
                outstr += (rstr + "\n")
            outstr += ("\n\nnew file ========================================================\n\n")
            txt_edit.insert(tk.END, outstr)

    print("myfunc finished =========================================================")

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




window = tk.Tk()
window.title("Synthea Data Jsonpath Explorer")
window.rowconfigure(0, minsize=1, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=5)
window.columnconfigure(1, weight=2)



jsonpath_edit = tk.Entry(window)
jsonpath_edit.place(height=50)
txt_edit = tk.Text(window)
json_label = tk.Label(text="Enter a jsonpath string")




fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_run = tk.Button(fr_buttons, text="DataRun", command=myfunc)
btn_pic = tk.Button(fr_buttons, text="Pick Data Dir", command=pick_dir)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_run.grid(row=2, column=0, sticky="ew", padx=5)
btn_pic.grid(row=3, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=2, column=0, sticky="ns")
json_label.grid(row=0, column=1)
jsonpath_edit.grid(row=1, column=1, columnspan=4, sticky="ew", padx=5,pady=5)
txt_edit.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
jsonpath_edit.insert('0', "$")

window.mainloop()


