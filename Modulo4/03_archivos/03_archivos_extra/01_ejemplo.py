from pathlib import Path
from PyPDF2 import PdfReader  # pip install PyPDF2

RUTA_PDF = Path(__file__).with_name("ejemplo.pdf")

def leer_pdf(ruta: Path) -> str:
    """Lee un archivo PDF y retorna el texto concatenado de todas sus páginas.
    Imprime además un resumen por página.
    """
    if not ruta.exists():
        print(f"No existe el archivo: {ruta}")
        return ""
    try:
        with ruta.open('rb') as f:  # Abrir en binario
            reader = PdfReader(f)
            total_paginas = len(reader.pages)
            print(f"Total de páginas: {total_paginas}")
            texto_total = []
            for i, page in enumerate(reader.pages, start=1):
                texto = page.extract_text() or ""  # Puede devolver None
                print(f"--- Página {i} ---")
                print(texto[:200].strip().replace('\n', ' ') + ("..." if len(texto) > 200 else ""))
                texto_total.append(texto)
        return "\n".join(texto_total)
    except Exception as e:
        print(f"Error leyendo PDF: {e}")
        return ""

if __name__ == "__main__":
    # Asegúrate de tener un archivo 'ejemplo.pdf' en el mismo directorio.
    contenido = leer_pdf(RUTA_PDF)
    print("\nLongitud total del texto extraído:", len(contenido))
