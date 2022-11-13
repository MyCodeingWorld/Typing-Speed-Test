from tkinter import *
from tkinter import messagebox as tkmsg
from essential_generators import DocumentGenerator as docx
import threading


def Get_ParaGraph():
    string, text = docx().paragraph(min_sentences=10, max_sentences=20), ""
    for i in range(0, len(string)):
        text += string[i]
        if i % 100 == 0 and i != 0:
            text += "\n"
    return text


print(Get_ParaGraph())