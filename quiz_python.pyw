# ============================================================
#  QUIZ DI PROGRAMMAZIONE PYTHON - Interfaccia Grafica
#  Capolavoro - Corso di Python (marzo-aprile)
#  Concetti: variabili, tipi, input/output, cicli, funzioni, liste
# ============================================================

import tkinter as tk
from tkinter import font as tkfont

# --- DATI DEL QUIZ ---
domande = [
    {
        "testo": "Qual è il modo corretto per stampare qualcosa in Python?",
        "codice": None,
        "opzioni": ["echo('Ciao mondo')", "print('Ciao mondo')", "console.log('Ciao mondo')", "printf('Ciao mondo')"],
        "corretta": 1,
        "spiegazione": "In Python si usa print() per mostrare output a schermo. È una delle funzioni più usate e fondamentali del linguaggio."
    },
    {
        "testo": "Cosa stampa questo codice?",
        "codice": "x = 5\ny = 3\nprint(x + y)",
        "opzioni": ["x + y", "53", "8", "Errore"],
        "corretta": 2,
        "spiegazione": "Le variabili x e y contengono numeri interi. L'operatore + tra numeri esegue la somma matematica: 5 + 3 = 8."
    },
    {
        "testo": "Come si crea una variabile che contiene il testo 'Python'?",
        "codice": None,
        "opzioni": ["var nome = 'Python'", "nome = 'Python'", "string nome = 'Python'", "let nome = 'Python'"],
        "corretta": 1,
        "spiegazione": "In Python non si usa nessuna parola chiave per dichiarare variabili: si scrive semplicemente nome = valore."
    },
    {
        "testo": "Quante volte viene stampato 'Ciao' da questo ciclo?",
        "codice": "for i in range(4):\n    print('Ciao')",
        "opzioni": ["3 volte", "4 volte", "5 volte", "0 volte"],
        "corretta": 1,
        "spiegazione": "range(4) genera i numeri 0, 1, 2, 3 — quindi 4 valori. Il ciclo for esegue il corpo una volta per ogni valore."
    },
    {
        "testo": "Cosa fa questa funzione?",
        "codice": "def saluta(nome):\n    return 'Ciao, ' + nome",
        "opzioni": ["Stampa un saluto", "Restituisce una stringa di saluto", "Chiede il nome all'utente", "Crea una variabile nome"],
        "corretta": 1,
        "spiegazione": "def definisce una funzione. return restituisce un valore al chiamante — qui una stringa formata da 'Ciao, ' + il parametro nome."
    },
    {
        "testo": "Qual è il tipo di dato di questa variabile?",
        "codice": "eta = 16",
        "opzioni": ["str (stringa)", "float (decimale)", "int (intero)", "bool (booleano)"],
        "corretta": 2,
        "spiegazione": "Il numero 16 senza virgolette è un intero (int). Se fosse 16.0 sarebbe float, se fosse '16' tra virgolette sarebbe str."
    },
    {
        "testo": "Con eta = 20, cosa stampa questo codice?",
        "codice": "if eta >= 18:\n    print('Maggiorenne')\nelse:\n    print('Minorenne')",
        "opzioni": ["Minorenne", "Maggiorenne", "Errore", "Nulla"],
        "corretta": 1,
        "spiegazione": "Con eta = 20, la condizione 20 >= 18 è vera (True), quindi viene eseguito il blocco if che stampa 'Maggiorenne'."
    },
    {
        "testo": "Come si aggiunge un elemento alla fine di una lista in Python?",
        "codice": "frutti = ['mela', 'banana']\n# Come aggiungere 'arancia'?",
        "opzioni": ["frutti.add('arancia')", "frutti.push('arancia')", "frutti.append('arancia')", "frutti.insert('arancia')"],
        "corretta": 2,
        "spiegazione": "Il metodo .append() aggiunge un elemento alla fine di una lista. È il modo più semplice e diretto."
    },
]

# --- COLORI ---
SFONDO      = "#0f0f0f"
CARD        = "#1a1a1a"
BORDO       = "#2a2a2a"
TESTO       = "#f0f0f0"
TESTO_SEC   = "#888888"
VERDE       = "#22c55e"
VERDE_BG    = "#0d2818"
ROSSO       = "#ef4444"
ROSSO_BG    = "#2a0d0d"
GIALLO      = "#eab308"
ACCENT      = "#3b82f6"
BOTTONE     = "#1e1e1e"
BOTTONE_HOV = "#2a2a2a"

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz di Programmazione Python")
        self.root.geometry("680x640")
        self.root.configure(bg=SFONDO)
        self.root.resizable(False, False)

        self.current = 0
        self.punteggio = 0
        self.risposto = False
        self.bottoni_opzioni = []

        self._build_ui()
        self.carica_domanda()

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg=SFONDO)
        header.pack(fill="x", padx=30, pady=(28, 0))

        self.lbl_badge = tk.Label(header, text="PYTHON BASICS · CAPOLAVORO",
            bg=CARD, fg=TESTO_SEC, font=("Courier New", 10), padx=10, pady=4,
            relief="flat", bd=0)
        self.lbl_badge.pack(anchor="w")

        self.lbl_titolo = tk.Label(header, text="Quiz di Programmazione Python",
            bg=SFONDO, fg=TESTO, font=("Segoe UI", 18, "bold"))
        self.lbl_titolo.pack(anchor="w", pady=(8, 0))

        self.lbl_sub = tk.Label(header, text="8 domande sui fondamenti di Python",
            bg=SFONDO, fg=TESTO_SEC, font=("Segoe UI", 11))
        self.lbl_sub.pack(anchor="w", pady=(2, 16))

        # Barra progresso
        prog_frame = tk.Frame(self.root, bg=SFONDO)
        prog_frame.pack(fill="x", padx=30, pady=(0, 6))

        self.lbl_num = tk.Label(prog_frame, text="", bg=SFONDO, fg=TESTO_SEC,
            font=("Segoe UI", 10))
        self.lbl_num.pack(anchor="e")

        self.canvas_prog = tk.Canvas(self.root, height=5, bg=BORDO,
            highlightthickness=0, bd=0)
        self.canvas_prog.pack(fill="x", padx=30, pady=(0, 20))
        self.barra = self.canvas_prog.create_rectangle(0, 0, 0, 5, fill=ACCENT, outline="")

        # Card domanda
        self.card = tk.Frame(self.root, bg=CARD, bd=0, highlightthickness=1,
            highlightbackground=BORDO)
        self.card.pack(fill="x", padx=30, pady=(0, 12))

        inner = tk.Frame(self.card, bg=CARD)
        inner.pack(fill="x", padx=20, pady=18)

        self.lbl_domanda = tk.Label(inner, text="", bg=CARD, fg=TESTO,
            font=("Segoe UI", 13), wraplength=580, justify="left", anchor="w")
        self.lbl_domanda.pack(fill="x", pady=(0, 10))

        self.lbl_codice = tk.Label(inner, text="", bg="#111111", fg="#7dd3fc",
            font=("Courier New", 11), wraplength=560, justify="left", anchor="w",
            padx=14, pady=10, relief="flat")

        # Opzioni
        self.frame_opzioni = tk.Frame(self.root, bg=SFONDO)
        self.frame_opzioni.pack(fill="x", padx=30, pady=(0, 10))

        for i in range(4):
            btn = tk.Button(self.frame_opzioni, text="", bg=BOTTONE, fg=TESTO,
                font=("Segoe UI", 12), anchor="w", padx=16, pady=10,
                relief="flat", bd=0, cursor="hand2", wraplength=580,
                activebackground=BOTTONE_HOV, activeforeground=TESTO,
                highlightthickness=1, highlightbackground=BORDO,
                command=lambda idx=i: self.seleziona(idx))
            btn.pack(fill="x", pady=4)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BOTTONE_HOV) if not self.risposto else None)
            btn.bind("<Leave>", lambda e, b=btn, i=i: self._reset_hover(b, i))
            self.bottoni_opzioni.append(btn)

        # Feedback
        self.lbl_feedback = tk.Label(self.root, text="", bg=SFONDO, fg=TESTO_SEC,
            font=("Segoe UI", 11), wraplength=620, justify="left",
            padx=30, pady=8)
        self.lbl_feedback.pack(fill="x", padx=0)

        # Bottone avanti
        self.btn_avanti = tk.Button(self.root, text="Prossima domanda →",
            bg=CARD, fg=TESTO, font=("Segoe UI", 12), padx=20, pady=10,
            relief="flat", bd=0, cursor="hand2",
            activebackground=BORDO, activeforeground=TESTO,
            highlightthickness=1, highlightbackground=BORDO,
            command=self.prossima)
        self.btn_avanti.pack(pady=(4, 0), padx=30, anchor="e")
        self.btn_avanti.pack_forget()

    def _reset_hover(self, btn, idx):
        if self.risposto:
            return
        btn.config(bg=BOTTONE)

    def carica_domanda(self):
        self.risposto = False
        q = domande[self.current]

        # Progresso
        totale = len(domande)
        self.lbl_num.config(text=f"Domanda {self.current + 1} di {totale}")
        larghezza = self.canvas_prog.winfo_width() or 620
        fill_w = int((self.current / totale) * larghezza)
        self.canvas_prog.coords(self.barra, 0, 0, fill_w, 5)

        self.lbl_domanda.config(text=q["testo"])

        # Codice
        if q["codice"]:
            self.lbl_codice.config(text=q["codice"])
            self.lbl_codice.pack(fill="x", pady=(0, 10))
        else:
            self.lbl_codice.pack_forget()

        # Opzioni
        for i, btn in enumerate(self.bottoni_opzioni):
            btn.config(text=f"  {i+1}.  {q['opzioni'][i]}",
                bg=BOTTONE, fg=TESTO, state="normal",
                highlightbackground=BORDO)

        self.lbl_feedback.config(text="")
        self.btn_avanti.pack_forget()

    def seleziona(self, idx):
        if self.risposto:
            return
        self.risposto = True
        q = domande[self.current]

        for btn in self.bottoni_opzioni:
            btn.config(state="disabled")

        if idx == q["corretta"]:
            self.punteggio += 1
            self.bottoni_opzioni[idx].config(bg=VERDE_BG, fg=VERDE,
                highlightbackground=VERDE)
            self.lbl_feedback.config(
                text=f"✓  Corretto!  —  {q['spiegazione']}", fg=VERDE)
        else:
            self.bottoni_opzioni[idx].config(bg=ROSSO_BG, fg=ROSSO,
                highlightbackground=ROSSO)
            self.bottoni_opzioni[q["corretta"]].config(bg=VERDE_BG, fg=VERDE,
                highlightbackground=VERDE)
            self.lbl_feedback.config(
                text=f"✗  Sbagliato.  —  {q['spiegazione']}", fg=ROSSO)

        testo_btn = "Vedi risultati →" if self.current == len(domande) - 1 else "Prossima domanda →"
        self.btn_avanti.config(text=testo_btn)
        self.btn_avanti.pack(pady=(4, 0), padx=30, anchor="e")

    def prossima(self):
        self.current += 1
        if self.current >= len(domande):
            self.mostra_risultato()
        else:
            self.carica_domanda()

    def mostra_risultato(self):
        totale = len(domande)
        percentuale = round((self.punteggio / totale) * 100)

        if percentuale >= 80:
            commento = "Ottimo! Hai una buona padronanza di Python!"
            colore = VERDE
        elif percentuale >= 50:
            commento = "Buon risultato! Continua a esercitarti."
            colore = GIALLO
        else:
            commento = "Riprova! La pratica rende perfetti."
            colore = ROSSO

        # Pulisci
        for w in self.root.winfo_children():
            w.destroy()

        frame = tk.Frame(self.root, bg=SFONDO)
        frame.pack(expand=True, fill="both", padx=40, pady=40)

        tk.Label(frame, text="Risultato Finale", bg=SFONDO, fg=TESTO_SEC,
            font=("Segoe UI", 13)).pack(pady=(0, 8))

        tk.Label(frame, text=f"{self.punteggio}/{totale}", bg=SFONDO, fg=TESTO,
            font=("Segoe UI", 64, "bold")).pack()

        tk.Label(frame, text=commento, bg=SFONDO, fg=colore,
            font=("Segoe UI", 14)).pack(pady=(4, 24))

        # Statistiche
        stat_frame = tk.Frame(frame, bg=SFONDO)
        stat_frame.pack(fill="x", pady=(0, 24))

        for etichetta, valore, colore_val in [
            ("Corrette", str(self.punteggio), VERDE),
            ("Errate", str(totale - self.punteggio), ROSSO),
            ("Punteggio", f"{percentuale}%", TESTO),
        ]:
            box = tk.Frame(stat_frame, bg=CARD, highlightthickness=1,
                highlightbackground=BORDO)
            box.pack(side="left", expand=True, fill="x", padx=6, pady=4)
            tk.Label(box, text=valore, bg=CARD, fg=colore_val,
                font=("Segoe UI", 26, "bold")).pack(pady=(14, 2))
            tk.Label(box, text=etichetta, bg=CARD, fg=TESTO_SEC,
                font=("Segoe UI", 11)).pack(pady=(0, 14))

        tk.Button(frame, text="Ricomincia il quiz",
            bg=CARD, fg=TESTO, font=("Segoe UI", 12), padx=24, pady=10,
            relief="flat", bd=0, cursor="hand2",
            activebackground=BORDO, activeforeground=TESTO,
            highlightthickness=1, highlightbackground=BORDO,
            command=self.ricomincia).pack()

    def ricomincia(self):
        self.current = 0
        self.punteggio = 0
        self.risposto = False
        self.bottoni_opzioni = []
        for w in self.root.winfo_children():
            w.destroy()
        self._build_ui()
        self.carica_domanda()


# --- AVVIO ---
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
