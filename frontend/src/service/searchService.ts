import { BatchSearchRequest, SearchRequest } from '@/types/searchRequest'
import { BatchSearchResponse, SearchResponse } from '@/types/searchResponse'
import ApiService from '@/service/apiService'
import { BatchCdEntry } from '@/types/cdEntry'

export default class SearchService {
    static async search(payload: SearchRequest): Promise<SearchResponse> {
        return ApiService.post('search/new', payload).then(
            response => response.data
        )
    }

    static async batchSearch(
        payload: BatchSearchRequest
    ): Promise<BatchSearchResponse> {
        return ApiService.post('search/batch', payload).then(
            response => response.data
        )
    }

    static async batchSearchResult(
        searchId: string
    ): Promise<Array<BatchCdEntry>> {
        return ApiService.get(`search/batch/${searchId}`).then(
            response => response.data
        )
    }

    static async dummy(): Promise<Array<BatchCdEntry>> {
        return Promise.resolve([
            {
                accession: 'pfam00230',
                description: '',
                interval: '31-259',
                evalue: '2e-88',
                sequence:
                    'ELRSVSFLRAVIAEFLATLLFVFFGVGSALGVKKLVSSLAVSGLLAVALAFGLALATLVYCAGHISGAHLNPAVTLALLVGRRFSLLRAIFYIVAQLLGAIAGAALLYGVTVGLQRAGLFANTLAPGVNAGQAFVVEIILTFQLVYCVFATTDDRRNGSLGTVAPLAIGFAVFLNHLAGGPYTGASMNPARSFGPAVVLWKWDDHWVYWVGPFIGAALGALVY',
                query: 'myseq',
            },
            {
                accession: 'cd00333',
                description: '',
                interval: '39-262',
                evalue: '2e-76',
                sequence:
                    'RKYLAEFLGTFLLVFFGCGSVLAVKLAGGASGGLLGIALAWGFAIFVLVYAVGHISGGHINPAVTLALAVGGRFPLIRVIPYIIAQLLGAILGAALLYGLYYGLYLEFLGANNIVAGIFGTYPSPGVSNGNAFFVEFIGTFILVLVVFATTDDPNGPPPGGLAPLAIGLLVAAIGLAGGPITGASMNPARSLGPALFTGLARHWHYFWVYWVGPLIGAIAGALVYDYV',
                query: 'myseq',
            },
            {
                accession: 'TIGR00861',
                description: '',
                interval: '43-259',
                evalue: '3e-66',
                sequence:
                    'AEFLGTFLLVFFGVGSALGVNVAGAYGAVGGGQFLGVALAFGLAVATLVYCVGGISGAHLNPAVTIALLLGRRFPLKRVPVYIVAQLIGAILGAALLYGLTSGLFPGNLAVNGSASAGVSSGQAFFVEFIGTAILVLVIFATTDDRNRVPRGGFAPLAIGLLVFLIHLSMGPYTGTGMNPARSLGPALFAGLAGWGNHWVYWVGPIIGAILGALVY',
                query: 'myseq',
            },
            {
                accession: 'COG0580',
                description: '',
                interval: '42-263',
                evalue: '2e-44',
                sequence:
                    'LAEFLGTFLLIFFGNGSVAAVALKGSKALGGGWLGIALAWGLGVLVAIYAFGGISGAHLNPAVTIALAVRGRFPWRKVLPYIVAQVLGAFAGAALLYLLYYGKILETEGDPLASLGAFSTSPGGYSLGQAFLIEFVGTFVLVLGILALTDDGNANAGFAPLAIGLLVTAIGLSLGPTTGTAINPARDLGPRLAHSLAGWAANKGDSSYFWIPVIGPIVGAILGALLYKLLL',
                query: 'myseq',
            },
            {
                accession: 'PLN00027',
                description: '',
                interval: '39-256',
                evalue: '6e-37',
                sequence:
                    'KAALAEFISTLIFVFAGEGSGMAFNKLTDNGSTTPAGLVAAALAHAFALFVAVSVGANISGGHVNPAVTFGAFIGGNITLLRGILYWIAQLLGSVVACLLLKFSTGGLETSAFSLSSGVGVWNAFVFEIVMTFGLVYTVYATAVDPKKGDLGIIAPIAIGFIVGANILAGGAFDGASMNPAVSFGPAVVSWTWTNHWVYWAGPLIGGGIAG',
                query: 'myseq',
            },
            {
                accession: 'cd00018',
                description: '',
                interval: '116-147',
                evalue: '4e-14',
                sequence: 'YRGVRQRPWGKWVAEIRDPSGGRRIWLGTFDT',
                query: 'OsERF1',
            },
            {
                accession: 'smart00380',
                description: '',
                interval: '116-147',
                evalue: '9e-14',
                sequence: 'YRGVRQRPWGKWVAEIRDPSKGKRVWLGTFDT',
                query: 'OsERF1',
            },
            {
                accession: 'pfam00847',
                description: '',
                interval: '115-147',
                evalue: '0.002',
                sequence: 'KIRGVRYDKKWGRWVAEWSENGKRRKKRFSLGKYGT',
                query: 'OsERF1',
            },
        ])
    }
}
