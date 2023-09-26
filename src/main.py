import torch
import os
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

import tkinter as tk
import time


def generateImage(pipeline, e1, e2):

    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = "../output/" + timestr + ".png"
    print(fileName)

    model_id = "stabilityai/stable-diffusion-2-1"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    commandline_args = os.environ.get('COMMANDLINE_ARGS', "--skip-torch-cuda-test --no-half")

    
    if pipeline == 1:
        pipe = pipe.to("cpu")
        print("Piping to CPU")
    else:
        pipe = pipe.to("gpu")
        print("Piping to GPU")

    prompt = "a photo of an astronaut riding a horse on mars"
    if e1 != "":
        prompt = e1
        print("Prompt:", e1)
    else:
        print("No prompt given. Using prompt \"" + prompt + "\"")
    
    image = pipe(prompt).images[0]
    image.save(fileName)

    print("Complete!")


master = tk.Tk()
master.title("stable-diffusion-2-1")

e1 = tk.Entry(master)
e2 = tk.Entry(master)
tk.Label(master, text='Prompt').pack(padx=10, pady=10)
e1.pack()
tk.Label(master, text='Iterations').pack(padx=10, pady=10)
e2.pack()

e1.get()

pipline = tk.IntVar()
tk.Checkbutton(master, text='Pipe to CPU', variable=pipline).pack(padx=10, pady=10)

button = tk.Button(master,
                   text='Generate',
                   command=lambda: generateImage(pipline.get(), e1.get(), e2.get())).pack(padx=10, pady=10)

tk.mainloop()
