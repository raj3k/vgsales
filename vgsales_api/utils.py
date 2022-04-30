from typing import List, Generator
from .models import Game


def _csv_reader(filename: str) -> Generator:
    for row in open(filename, "r"):
        yield row


def _create_db_record(row: List[str]) -> Game:
    data = row
    game = Game.objects.create(
        name = data[1],
        platform = data[2] if not data[2] == "N/A" else "",
        year = int(data[3]) if not data[3] == "N/A" else None,
        genre = data[4] if not data[4] == "N/A" else "",
        publisher = data[5] if not data[5] == "N/A" else "",
        na_sales = float(data[6]) if not data[6] == "N/A" else None,
        eu_sales = float(data[7]) if not data[7] == "N/A" else None,
        jp_sales = float(data[8]) if not data[8] == "N/A" else None,
        other_sales = float(data[9]) if not data[9] == "N/A" else None,
        global_sales = float(data[10]) if not data[10] == "N/A" else None
    )
    print(game)

def get_data_from_csv_file(csv_filename: str):
    for row in _csv_reader(csv_filename):
        if row.split(",")[0] == "Rank":
            continue
        if '"' not in row:
            _create_db_record(row.split(","))
        # TODO: "mixi, Inc" resolve

def asd(name):
    for r in _csv_reader(name):
        print(int(r.split(",")[3]))
        