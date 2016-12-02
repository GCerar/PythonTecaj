"""
Preprosta demo aplikacija za Python tečaj. Narejena je s Tk/TKinter
"""

import tkinter as tk
import requests

url = 'http://trola.si/'
headers = {'Accept': 'application/json'}


class Application(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label_postaja = tk.Label(self, text='Postaja:')
        self.label_postaja.grid(row=0, column=0)
        
        self.postaja = tk.Entry(self)
        self.postaja.grid(row=0, column=1)
        
        self.find = tk.Button(self, text='Poišči', command=self.fetch_data)
        self.find.grid(row=0, column=2)
        
        self.quit = tk.Button(self, text="Izhod", command=root.destroy)
        self.quit.grid(row=0, column=3)
        
        self.seznam = tk.Listbox(self, width=40)
        self.seznam.grid(row=1, columnspan=4)
        
        
    def fetch_data(self, event=None):
        ime_postaje = self.postaja.get()
        res = requests.get(url + ime_postaje, headers=headers)
        data = res.json()
        busi = []
        for postaja in data['stations']:
            for bus in postaja['buses']:
                busi.append('{} ({}): {}'.format(bus['direction'], bus['number'], bus['arrivals']))
                
        #self.seznam.delete(0, -1)
        for i, bus in enumerate(busi):
            self.seznam.insert(i, bus)
        

        

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Get-a-bus')
    root.geometry('250x150')
    Application(root)
    root.mainloop()