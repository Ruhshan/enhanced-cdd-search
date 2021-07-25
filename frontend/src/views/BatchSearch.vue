<template>
    <v-container>
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
    </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { DatabaseInterface } from '@/types/database'
import { BatchSearchRequest } from '@/types/searchRequest'
import SearchService from '@/service/searchService'
@Component({})
export default class BatchSearch extends Vue {
    private loading = false
    private databases: Array<DatabaseInterface> = [
        { id: 0, name: 'CDD -- 58235 PSSMs', value: 'cdd' },
        { id: 1, name: 'NCBI_Curated -- 17937 PSSMs', value: 'cdd_ncbi' },
    ]
    private query: BatchSearchRequest = new BatchSearchRequest()
    private async submit(): Promise<void> {
        this.loading = true

        try {
            const res = await SearchService.batchSearch(this.query)
          console.log(JSON.stringify(res))
        } catch (e) {
            console.log(JSON.stringify(e))
        }

        this.loading = false
    }
}
</script>

<style scoped></style>
