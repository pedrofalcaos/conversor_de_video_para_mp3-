import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)
    audio_clip.close()
    video_clip.close()

def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if input_file:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, input_file)

def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_file)

def start_conversion():
    input_file = entry_input.get()
    output_file = entry_output.get()
    if input_file and output_file:
        try:
            convert_mp4_to_mp3(input_file, output_file)
            messagebox.showinfo("Conversão Concluída 🎉", f"Conversão concluída: {output_file}")
            again = messagebox.askyesno("Nova Conversão 🔄", "Deseja fazer outra conversão?")
            if not again:
                messagebox.showinfo("Obrigado 🙏", "Obrigado por usar o conversor MP4 para MP3!")
                root.quit()
            else:
                entry_input.delete(0, tk.END)
                entry_output.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro ❌", f"Ocorreu um erro durante a conversão: {str(e)}\nVerifique se o ffmpeg está instalado e no PATH do sistema.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor MP4 para MP3 🎵")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_input = tk.Label(frame, text="Arquivo MP4:", font=("Helvetica", 12), fg="blue")
label_input.grid(row=0, column=0, pady=5)

entry_input = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry_input.grid(row=0, column=1, pady=5)

button_input = tk.Button(frame, text="Selecionar...", command=select_input_file, bg="lightblue", fg="black", font=("Helvetica", 12, "bold"))
button_input.grid(row=0, column=2, pady=5)

label_output = tk.Label(frame, text="Salvar como MP3:", font=("Helvetica", 12), fg="blue")
label_output.grid(row=1, column=0, pady=5)

entry_output = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry_output.grid(row=1, column=1, pady=5)

button_output = tk.Button(frame, text="Selecionar...", command=select_output_file, bg="lightgreen", fg="black", font=("Helvetica", 12, "bold"))
button_output.grid(row=1, column=2, pady=5)

button_convert = tk.Button(root, text="Converter 🎶", command=start_conversion, bg="orange", fg="black", font=("Helvetica", 12, "bold"))
button_convert.pack(pady=10)

root.mainloop()
