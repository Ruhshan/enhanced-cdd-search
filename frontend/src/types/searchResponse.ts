import {CdEntry} from '@/types/cdEntry';

export interface SearchResponse{
    count: number,
    data: Array<CdEntry>
}