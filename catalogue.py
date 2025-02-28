from dataclasses import dataclass
from typing import Self
import json


@dataclass
class Film:
    title: str
    year: int
    director: str
    img: str


with open("ghibli.json", "r") as file:
    data = json.load(file)["films"]


class Catalogue:
    def __init__(self):
        self.films = [
            Film(
                d["title"],
                d["release_date"],
                d["director"],
                d["image"],
            )
            for d in data
        ]

        self.directors = sorted({f.director for f in self.films})

    def filter(self, directors: list[str]) -> Self:
        if directors:
            self.films = [f for f in self.films if f.director in directors]
        return self

    def search(self, query: str) -> Self:
        if query:
            self.films = [
                f
                for f in self.films
                if query.lower() in f.title.lower()
                or query.lower() in f.director.lower()
            ]
        return self

    def sort(self, key: str) -> Self:
        if key:
            print(key)
            attr, order = key.split("-")
            self.films = sorted(
                self.films,
                key=lambda f: getattr(f, attr),
                reverse=order == "desc",
            )
        return self
