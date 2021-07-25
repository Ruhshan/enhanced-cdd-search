export interface CdEntry{
    accession: string,
    description: string,
    interval: string,
    evalue: string,
    sequence: string
}

export interface BatchCdEntry extends CdEntry{
    query: string
}