import tkinter as Tk
import asyncio
from pyartnet import ArtNetNode

async def new_fade(node, universe, channel, dmx_var):
    await node.start()
    channel.set_fade(dmx_var,0)
    await channel.wait_till_fade_complete()
    print(channel.get_channel_values())
    await node.stop()

async def main():
    node = ArtNetNode('192.168.0.111', 6454)
    universe = node.add_universe(0)

    def send_to_light(dmx_vars):
        print(dmx_vars)
##        try:
##            channel = universe.add_channel(start=int(dmx_entry.get()), width=int(width_entry.get()))
##        except:
##            channel = universe.get_channel(f"{int(dmx_entry.get())}/{int(width_entry.get())}")
##        asyncio.run(new_fade(node,universe,channel,dmx_vars))
##        return channel

    def add_scales(num_scales):
        for i in range(num_scales):
            Tk.Scale(frame2, label=i+1, from_=255, to=0, length=200, command=lambda e:update_vals()).grid(row=2, column=i)
        patch_btn.config(state='disabled')

    def update_vals():
##        btns = frame3.children
##        for i, j in btns.items():
##            print(i, j.keys())
        dmx_vars=[]
        scales = frame2.children
        for k, v in scales.items():
            dmx_vars.append(scales[k].get())
        send_to_light(dmx_vars)

    def clear_all():
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(0)
        update_vals()

    def store1(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset1.append(scales[k].get())
        store1_btn.config(state='disabled')
    def recall1(presets):
        send_to_light(preset1)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset1[int(v['label'])-1])

    def store2(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset2.append(scales[k].get())
        store2_btn.config(state='disabled')
    def recall2(presets):
        send_to_light(preset2)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset2[int(v['label'])-1])

    def store3(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset3.append(scales[k].get())
        store3_btn.config(state='disabled')
    def recall3(presets):
        send_to_light(preset3)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset3[int(v['label'])-1])

    def store4(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset4.append(scales[k].get())
        store4_btn.config(state='disabled')
    def recall4(presets):
        send_to_light(preset4)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset4[int(v['label'])-1])

    def store5(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset5.append(scales[k].get())
        store5_btn.config(state='disabled')
    def recall5(presets):
        send_to_light(preset5)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset5[int(v['label'])-1])
            
    def store6(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset6.append(scales[k].get())
        store6_btn.config(state='disabled')
    def recall6(presets):
        send_to_light(preset6)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset6[int(v['label'])-1])

    def store7(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset7.append(scales[k].get())
        store7_btn.config(state='disabled')
    def recall7(presets):
        send_to_light(preset7)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset7[int(v['label'])-1])

    def store8(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset8.append(scales[k].get())
        store8_btn.config(state='disabled')
    def recall8(presets):
        send_to_light(preset8)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset8[int(v['label'])-1])

    def store9(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset9.append(scales[k].get())
        store9_btn.config(state='disabled')
    def recall9(presets):
        send_to_light(preset9)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset9[int(v['label'])-1])

    def store10(presets):
        scales = frame2.children
        for k, v in scales.items():
            preset10.append(scales[k].get())
        store10_btn.config(state='disabled')
    def recall10(presets):
        send_to_light(preset10)
        scales = frame2.children
        for k, v in scales.items():
            scales[k].set(preset10[int(v['label'])-1])


    preset1=[]
    preset2=[]
    preset3=[]
    preset4=[]
    preset5=[]
    preset6=[]
    preset7=[]
    preset8=[]
    preset9=[]
    preset10=[]
    presets = [[preset1],[preset2],[preset3],[preset4],[preset5],
               [preset6],[preset7],[preset8],[preset9],[preset10]]
    
    root = Tk.Tk()

    #Frame1#
    frame1 = Tk.Frame(root)
    frame1.grid(row=0, column=0)

    dmx_address = Tk.Label(frame1, text='DMX Address')
    dmx_address.grid(row=0,column=0)

    dmx_entry = Tk.Entry(frame1)
    dmx_entry.grid(row=0,column=1, padx=15, sticky='')

    channel_width = Tk.Label(frame1, text='Channel Width')
    channel_width.grid(row=1,column=0)

    width_entry = Tk.Entry(frame1)
    width_entry.grid(row=1,column=1, padx=15, sticky='')

    patch_btn = Tk.Button(frame1, text='Patch', command=lambda: add_scales(int(width_entry.get())))
    patch_btn.grid(row=1, column=2)

    #Frame2#
    frame2 = Tk.Frame(root)
    frame2.grid(row=2, column=0, pady=25)

    #Frame 3#
    frame3= Tk.Frame(root)
    frame3.grid(row=3, column=0)

    clear_btn = Tk.Button(frame3, text='Clear', command=clear_all)
    clear_btn.grid(row=0,column=0, columnspan=120, ipadx=335, pady=5)

    #Store Buttons#
    store1_btn = Tk.Button(frame3, text='Store 1', command=lambda: store1(presets))
    store1_btn.grid(row=1,column=0, ipadx=12)

    store2_btn = Tk.Button(frame3, text='Store 2', command=lambda: store2(presets))
    store2_btn.grid(row=1,column=1, ipadx=12)

    store3_btn = Tk.Button(frame3, text='Store 3', command=lambda: store3(presets))
    store3_btn.grid(row=1,column=2, ipadx=12)

    store4_btn = Tk.Button(frame3, text='Store 4', command=lambda: store4(presets))
    store4_btn.grid(row=1,column=3, ipadx=12)

    store5_btn = Tk.Button(frame3, text='Store 5', command=lambda: store5(presets))
    store5_btn.grid(row=1,column=5, ipadx=12)

    store6_btn = Tk.Button(frame3, text='Store 6', command=lambda: store6(presets))
    store6_btn.grid(row=1,column=6, ipadx=12)

    store7_btn = Tk.Button(frame3, text='Store 7', command=lambda: store7(presets))
    store7_btn.grid(row=1,column=7, ipadx=12)

    store8_btn = Tk.Button(frame3, text='Store 8', command=lambda: store8(presets))
    store8_btn.grid(row=1,column=8, ipadx=12)

    store9_btn = Tk.Button(frame3, text='Store 9', command=lambda: store9(presets))
    store9_btn.grid(row=1,column=9, ipadx=12)

    store10_btn = Tk.Button(frame3, text='Store 10', command=lambda: store10(presets))
    store10_btn.grid(row=1,column=10, ipadx=12)

    #Recall Buttons#
    recall1_btn = Tk.Button(frame3, text='Recall 1', command=lambda: recall1(presets))
    recall1_btn.grid(row=2,column=0, ipadx=10)

    recall2_btn = Tk.Button(frame3, text='Recall 2', command=lambda: recall2(presets))
    recall2_btn.grid(row=2,column=1, ipadx=10)

    recall3_btn = Tk.Button(frame3, text='Recall 3', command=lambda: recall3(presets))
    recall3_btn.grid(row=2,column=2, ipadx=10)

    recall4_btn = Tk.Button(frame3, text='Recall 4', command=lambda: recall4(presets))
    recall4_btn.grid(row=2,column=3, ipadx=10)

    recall5_btn = Tk.Button(frame3, text='Recall 5', command=lambda: recall5(presets))
    recall5_btn.grid(row=2,column=5, ipadx=10)

    recall6_btn = Tk.Button(frame3, text='Recall 6', command=lambda: recall6(presets))
    recall6_btn.grid(row=2,column=6, ipadx=10)

    recall7_btn = Tk.Button(frame3, text='Recall 7', command=lambda: recall7(presets))
    recall7_btn.grid(row=2,column=7, ipadx=10)

    recall8_btn = Tk.Button(frame3, text='Recall 8', command=lambda: recall8(presets))
    recall8_btn.grid(row=2,column=8, ipadx=10)

    recall9_btn = Tk.Button(frame3, text='Recall 9', command=lambda: recall9(presets))
    recall9_btn.grid(row=2,column=9, ipadx=10)

    recall10_btn = Tk.Button(frame3, text='Recall 10', command=lambda: recall10(presets))
    recall10_btn.grid(row=2,column=10, ipadx=10)

asyncio.run(main())
