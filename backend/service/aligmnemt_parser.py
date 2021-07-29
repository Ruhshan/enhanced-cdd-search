import asyncio
import re
from typing import List

from backend.schema.cd_entry import BatchCdEntry


class AlignmentParser:
    @classmethod
    async def parse(cls, alignment) -> List[BatchCdEntry]:
        query_result_indices = await cls.__find_segment_indices(alignment, "Q#[0-9]+\s-\s>.+")
        hits = []
        for (start, end) in query_result_indices:
            hits += await cls.__parse_query_result(alignment[start: end])
        return hits

    @classmethod
    async def __parse_query_result(cls, result) -> List[BatchCdEntry]:
        query = re.search("Q#\d+\s-\s>.+", result).group(0).split(" - >")[1]
        hit_indices = await cls.__find_segment_indices(result, ">cdd:\d+.*")
        hits = []
        for (start, end) in hit_indices:
            try:
                if start < end:
                    hits.append(await cls.__parse_hit(result[start:end], query))
            except Exception as e:
                print("unable to parse hit {}".format(result[start:end]))


        return hits

    @classmethod
    async def __parse_hit(cls, hit, query) -> BatchCdEntry:
        desc = re.findall(">cdd:\d+.*Length=\d+", hit, flags=re.DOTALL)[0]
        desc = ' '.join(re.split('\s', desc)[3:])
        accession = re.search(">cdd:\d+.*", hit).group(0).split(",")[2].strip()
        e_value = re.search("Expect\s=\s.*,", hit).group(0).split(" = ")[-1].replace(",", "")
        queries = re.findall("Query\s+\d+\s.*\s+\d+", hit)

        match_start = re.split("\s+", queries[0])[1]
        match_end = re.split("\s+", queries[len(queries) - 1])[-1]
        hit_sequences = re.findall("Sbjct\s+\d+\s+.*\s+\d+", hit)
        cd_sequence = ""

        for sequence in hit_sequences:
            cd_sequence += re.split("\s+", sequence)[2]
        cd_sequence = cd_sequence.replace("-", "")
        entry = BatchCdEntry(accession=accession, description=desc[1:], interval="{}-{}".format(match_start, match_end),
                             evalue=e_value, sequence=cd_sequence, query=query)

        return entry

    @classmethod
    async def __find_segment_indices(cls, alignment, pattern) -> List:
        segment_start_flags = re.findall(pattern, alignment)

        previous_index = None
        segment_indices = []
        for flag in segment_start_flags:
            current_index = alignment.index(flag)
            if previous_index != None:
                segment_indices.append((previous_index, current_index))
                previous_index = current_index
            if previous_index == None:
                previous_index = current_index
        segment_indices.append((previous_index, len(alignment)))
        return segment_indices
