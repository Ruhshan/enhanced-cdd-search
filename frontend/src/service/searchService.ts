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
}
