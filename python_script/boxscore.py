from .external_services.mlb_api import get
from rich.console import Console
from rich.table import Table

URL_PATH = lambda x: f"https://statsapi.mlb.com/api/v1.1/game/{x}/feed/live"

async def print_boxscore(gamepk):

    game_data = await get(URL_PATH(gamepk))

    boxscore_table = Table(title="Boxscore", show_lines=True)

    # create headers
    boxscore_table.add_column("Team")

    column_names = ["Team"]

    away_team = [game_data["gameData"]["teams"]["away"]["abbreviation"]]
    home_team = [game_data["gameData"]["teams"]["home"]["abbreviation"]]

    for inning in game_data["liveData"]["linescore"]["innings"]:

        ordinal_num = inning["ordinalNum"]
        boxscore_table.add_column(ordinal_num)

        ordinal_num = inning["ordinalNum"]
        away_team.append(str(inning["away"]["runs"]))
        home_team.append(str(inning["home"]["runs"]))


    for col_name in ["R", "H", "E"]:
        boxscore_table.add_column(col_name)

    total_stats = game_data["liveData"]["linescore"]["teams"]
    for elt in ["runs", "hits", "errors"]:
        away_team.append(str(total_stats["away"][elt]))
        home_team.append(str(total_stats["home"][elt]))

    boxscore_table.add_row(*away_team)
    boxscore_table.add_row(*home_team)
    console = Console()
    console.print(boxscore_table)