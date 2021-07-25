import {CdEntry} from '@/types/cdEntry';

export interface SearchResponse{
    count: number,
    data: Array<CdEntry>
}

export interface BatchSearchResponse{
    search_id: string
}