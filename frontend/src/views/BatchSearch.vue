<template>
    <v-container>
        <v-dialog v-model="dialog" width="500">
            <v-card>
                <v-toolbar color="primary" dark
                    ><v-toolbar-title>
                        Searching in progress...
                    </v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn icon @click="dialog = false">
                        <v-icon>mdi-close</v-icon>
                    </v-btn>
                </v-toolbar>

                <v-card-text>
                    <p style="margin-top: 5px">
                        Batch search might take longer time to complete, you may
                        <strong>SAVE</strong> the search ID showing bellow and
                        come back after a while when its complete
                    </p>

                    <v-text-field
                        v-model="searchID"
                        readonly
                        solo
                    ></v-text-field>
                </v-card-text>

                <v-divider></v-divider>
            </v-card>
        </v-dialog>
        <v-row>
            <v-col sm="8">
                <v-card style="height: 100%" :loading="loading">
                    <v-card-title>Enter query protein sequences</v-card-title>
                    <v-card-text>
                        <v-textarea
                            v-model="query.queries"
                            rows="10"
                            outlined
                            label="Batch CD-Search accepts only protein sequences.(Max 4000)"
                        ></v-textarea>
                        <v-btn
                            depressed
                            color="info"
                            :loading="loading"
                            @click="submit"
                            >Submit</v-btn
                        >
                        <v-row style="margin-top: 5px">
                            <v-col sm="12">
                                <v-text-field
                                    v-model="searchID"
                                    label="Previous Search ID"
                                    outlined
                                >
                                    <template v-slot:append-outer>
                                        <v-btn
                                            depressed
                                            color="info"
                                            :loading="loading"
                                            @click="fetchSearchResult"
                                            >Fetch</v-btn
                                        >
                                    </template>
                                </v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col sm="4">
                <v-card :loading="loading">
                    <v-card-title>Options</v-card-title>
                    <v-col sm="12">
                        <v-select
                            v-model="query.selectedDatabase"
                            :items="databases"
                            item-text="name"
                            item-value="value"
                            label="Select Database"
                            required
                        ></v-select>
                        <v-text-field
                            v-model="query.eValueThreshold"
                            label="E-Value Threshold"
                            required
                        ></v-text-field>
                        <v-text-field
                            v-model="query.maxHit"
                            label="Maximum Number of hits"
                            required
                        ></v-text-field>
                        <v-checkbox
                            v-model="query.compositionCorrectedScoring"
                            label="Composition Corrected Scoring"
                        ></v-checkbox>
                        <v-checkbox
                            v-model="query.applyLowComplexityFilter"
                            label="Apply Low Complexity Filter"
                        ></v-checkbox>
                        <v-checkbox
                            v-model="query.includeRetiredSequences"
                            label="Include Retired sequences"
                        ></v-checkbox>
                    </v-col>
                </v-card>
            </v-col>
        </v-row>

        <result-table :results="searchResult"></result-table>
    </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { DatabaseInterface } from '@/types/database'
import { BatchSearchRequest } from '@/types/searchRequest'
import SearchService from '@/service/searchService'
import ResultTable from '@/components/ResultTable.vue'
import { BatchCdEntry } from '@/types/cdEntry'

@Component({
    components: { ResultTable },
})
export default class BatchSearch extends Vue {
    private dialog = false
    private loading = false
    private searchID = ''
    private searchResult: Array<BatchCdEntry> = []
    private databases: Array<DatabaseInterface> = [
        { id: 0, name: 'CDD -- 58235 PSSMs', value: 'cdd' },
        { id: 1, name: 'NCBI_Curated -- 17937 PSSMs', value: 'cdd_ncbi' },
        { id: 2, name: 'Pfam -- 18271 PSSMs', value: 'oasis_pfam' },
        { id: 3, name: 'SMART -- 1011 PSSMs', value: 'oasis_smart' },
        { id: 4, name: 'KOG -- 4825 PSSMs', value: 'oasis_kog' },
        { id: 5, name: 'COG -- 4871 PSSMs', value: 'oasis_cog' },
        { id: 6, name: 'PRK -- 11657 PSSMs', value: 'oasis_prk' },
        { id: 7, name: 'TIGR -- 4488 PSSMs', value: 'oasis_tigr' },
    ]
    private query: BatchSearchRequest = new BatchSearchRequest()
    private async submit(): Promise<void> {
        this.loading = true
        this.searchResult = []
        this.searchID = ''

        try {
            const res = await SearchService.batchSearch(this.query)
            this.searchID = res.search_id
            await this.fetchSearchResult()
        } catch (e) {
            console.log(JSON.stringify(e))
        }

        this.loading = false
    }

    private async fetchSearchResult(): Promise<void> {
        if (this.searchID) {
            this.loading = true
            this.dialog = true

            for (let i = 0; i < 5; i++) {
                console.log(i)
                try {
                    const res = await SearchService.batchSearchResult(
                        this.searchID
                    )
                    this.searchResult = res
                    break
                } catch (e) {
                    console.log('From error')
                    console.log(JSON.stringify(e))
                }
                await this.wait(1000)
            }

            this.loading = false
            this.dialog = false
        }
    }

    private async wait(ms: number): Promise<() => void> {
        return new Promise(resolve => {
            setTimeout(resolve, ms)
        })
    }
}
</script>

<style scoped></style>
