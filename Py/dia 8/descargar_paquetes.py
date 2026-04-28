from rich.console import Console

console = Console()

console.print("Este es un mensaje normal")
console.print("¡Éxito!", style="bold green")
console.print("Cuidado, algo anda mal...", style="yellow underline")
console.print("ERROR CRÍTICO", style="white on red")