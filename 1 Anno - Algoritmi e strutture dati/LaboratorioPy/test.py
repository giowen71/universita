# Calcolo dell'integrale usando la tecnica dei rettangoli con n=10

# Funzione da integrare
def f(x):
    return x**2 - x

# Parametri
a = 1  # Inizio intervallo
b = 2  # Fine intervallo
n = 10  # Numero di rettangoli
delta_x = (b - a) / n  # Ampiezza di ciascun rettangolo

# Posizioni degli estremi (estremo sinistro)
x_values = [a + i * delta_x for i in range(n)]

# Valutazione della funzione nei punti x_i
f_values = [f(x) for x in x_values]

# Calcolo dell'area
area = delta_x * sum(f_values)

# Creazione del PDF con il nuovo calcolo
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Titolo
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Calcolo dell'integrale con la tecnica dei rettangoli (n=10)", ln=True, align="C")

# Contenuto
contenuto = f"""
Calcoliamo l'integrale \\int_{{1}}^{{2}}{{x^2 - x \\, dx}} usando la tecnica dei rettangoli.

1. Funzione: f(x) = x^2 - x
2. Intervallo di integrazione: [1, 2]
3. Numero di rettangoli (n): 10
4. Ampiezza di ciascun rettangolo: Δx = (2 - 1) / 10 = 0.1

Posizione degli estremi (estremo sinistro):
x_i = [ {', '.join(f'{x:.2f}' for x in x_values)} ]

Valutazione della funzione nei punti x_i:
f(x_i) = [ {', '.join(f'{fx:.4f}' for fx in f_values)} ]

Calcolo dell'area totale:
Area = Δx · sum(f(x_i))
Area = {delta_x:.2f} · {sum(f_values):.4f} = {area:.5f}

Risultato:
L'approssimazione dell'integrale con n = 10 è: {area:.5f}
"""

# Inserimento del contenuto nel PDF
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt=contenuto)

# Salvataggio del PDF
output_path = "/mnt/data/Integrale_Rettangoli_n10.pdf"
pdf.output(output_path)

output_path
