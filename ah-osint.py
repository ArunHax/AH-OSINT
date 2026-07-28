import os
import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from config import VERSION, AUTHOR
from modules import domain, ip, website
import modules.dns_osint as dns
from utils.output import save_json

console = Console()


def execute_scan(module_name, module_function, target):
    result = module_function(target)

    console.print_json(json.dumps(result, indent=4))

    filename = save_json(module_name, target, result)

    console.print(f"\n[bold green]✓ Report saved to:[/bold green] {filename}")


def clear():
    os.system("clear")


def banner():
    console.print()

    console.print(
        Panel.fit(
            f"[bold bright_green]AH-OSINT Framework {VERSION}[/bold bright_green]\n"
            f"[white]Created by {AUTHOR}[/white]",
            border_style="bright_green",
            padding=(1, 8),
        )
    )


def menu():
    table = Table(
        title="[bold white]Available Modules[/bold white]",
        border_style="white",
        header_style="bold white",
    )

    table.add_column("ID", justify="center", width=6)
    table.add_column("Module")

    table.add_row("01", "🌐 Domain Intelligence")
    table.add_row("02", "🌍 IP Intelligence")
    table.add_row("03", "📡 DNS Intelligence")
    table.add_row("04", "🖥 Website Intelligence")
    table.add_row("05", "🚪 Exit")

    console.print(table)

    console.print(
        "[white]Status:[/white] [bright_green]Ready[/bright_green]    "
        "[white]Version:[/white] [bright_green]"
        f"{VERSION}[/bright_green]"
    )


while True:
    clear()
    banner()
    menu()

    choice = console.input("\n[bold yellow]Select > [/bold yellow]")

    if choice == "1":
        target = console.input("[bold yellow]Domain > [/bold yellow]")
        execute_scan("domain", domain.run, target)

    elif choice == "2":
        target = console.input("[bold yellow]IP > [/bold yellow]")
        execute_scan("ip", ip.run, target)

    elif choice == "3":
        target = console.input("[bold yellow]Domain > [/bold yellow]")
        execute_scan("dns", dns.run, target)

    elif choice == "4":
        target = console.input("[bold yellow]Website > [/bold yellow]")
        execute_scan("website", website.run, target)

    elif choice == "5":
        console.print("\n[bold green]Thank you for using AH-OSINT![/bold green]\n")
        break

    else:
        console.print("\n[bold red]Invalid option![/bold red]")

    console.input("\n[dim]Press Enter to continue...[/dim]")