import { SearchRequest } from '@/types/searchRequest'
import { SearchResponse } from '@/types/searchResponse'
import ApiService from '@/service/apiService'

export default class SearchService {
    static async search(payload: SearchRequest): Promise<SearchResponse> {
        return ApiService.post('search/new', payload).then(
            response => response.data
        )
    }
}
