from .external_services.mlb_api import get
from rich.console import Console
from rich.table import Table

async def today_list():

    data = await get("https://statsapi.mlb.com/api/v1/schedule?sportId=1")

    today_table = Table(title="Today's Games", show_lines=True)

    today_table.add_column("Matchup")
    today_table.add_column("Game ID")

    game_list = []
    for game in data["dates"][0]["games"]:
        
        away = game["teams"]["away"]["team"]["name"]
        home = game["teams"]["home"]["team"]["name"]
        id = game["gamePk"]

        game_list.append([f"{away} @ {home}", str(id)])

    [today_table.add_row(*game) for game in game_list]
    console = Console()
    console.print(today_table)