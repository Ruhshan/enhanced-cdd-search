import re
from typing import List


class AlignmentParser:
    @classmethod
    def parse(cls, alignment):
        segment_indices = cls.__find_segment_indices(alignment,"Q#[0-9]+\s-\s>.+")
        print(alignment[segment_indices[0][0]: segment_indices[0][1]])

    @classmethod
    def __find_segment_indices(cls, alignment, pattern) -> List:
        segment_start_flags = re.findall(pattern, alignment)
        previous_index = None
        segment_indices = []
        for flag in segment_start_flags:
            current_index = alignment.index(flag)
            if previous_index!=None:
                segment_indices.append((previous_index, current_index))
                previous_index = current_index
            if previous_index == None:
                previous_index = current_index
        segment_indices.append((previous_index, len(alignment)))
        return  segment_indices

if __name__=="__main__":
    data = open("/Users/ruhshan_admin/development/enhanced-cdd-search/delete_me.html","r").read()
    AlignmentParser.parse(data)