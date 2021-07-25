import { BatchSearchRequest, SearchRequest } from '@/types/searchRequest'
import { BatchSearchResponse, SearchResponse } from '@/types/searchResponse'
import ApiService from '@/service/apiService'

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
}
