from typing import List

import bs4.element
from bs4 import BeautifulSoup

from backend.exception.custom_exceptions import DhandleNotFound
from backend.schema.cd_entry import CdEntry


class Extractor:
    @classmethod
    def extract_dhandle(cls, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        dhandle_input = soup.find("input", {"name": "dhandle"})
        if dhandle_input == None:
            raise DhandleNotFound
        else:
            return dhandle_input['value']

    @classmethod
    def extract_cdd_entries(cls, html: str) -> List[CdEntry]:
        soup = BeautifulSoup(html, 'html.parser')
        disp_tables = soup.find_all("table", {"class": "disptbl backstage"})
        entries = []
        last_entry = CdEntry.new()
        for table in disp_tables:
            for tr in table.find_all("tr"):
                class_names = tr.attrs.get("class")
                class_names = class_names if class_names is not None else []
                if "entry" in class_names:
                    last_entry = cls.__construct_entries(tr)
                if "detail" in class_names:
                    last_entry.sequence = cls.__construct_sequence(tr)
                    entries.append(last_entry)
                    last_entry = CdEntry.new()
        return entries

    @staticmethod
    def __construct_entries(entry: bs4.element.Tag) -> CdEntry:
        return CdEntry(accession=entry.find_all("td")[2].find("a").text,
                       description=entry.find_all("td")[3].find("div").text,
                       interval=entry.find_all("td")[4].text, evalue=entry.find_all("td")[5].text, sequence="")

    @staticmethod
    def __construct_sequence(detail: bs4.element.Tag) -> str:
        pres = detail.find_all("pre")
        seq = ""
        for pre in pres:
            record = False
            for e in pre:
                if e.name == "a":
                    record = True
                if e.name == "font" and record:
                    txt = e.text.strip()
                    if not txt.isdigit():
                        seq += e.text
        return seq

