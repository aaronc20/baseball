import sys
import asyncio
from python_script.boxscore import print_boxscore
from python_script.today_list import today_list


async def main():


    if len(sys.argv) < 2:
        print("'python3 main.py help' for commands")
        exit()

    command = sys.argv[1].lower()

    if command == "help":

        print("boxscore or listgames")

    elif command == "boxscore":

        await print_boxscore(sys.argv[2])

    elif command == "listgames":

        await today_list()
    
    else:

        print("'python3 main.py help' for commands")
    

asyncio.run(main())