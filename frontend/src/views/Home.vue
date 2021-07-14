<template>
    <v-container>
        <v-row>
            <v-col sm="8">
                <v-card style="height: 100%" :loading="loading">
                    <v-card-title>Search for Conserved Domains</v-card-title>
                    <v-card-text>
                        <v-textarea
                            v-model="query.seqinput"
                            rows="10"
                            outlined
                            label="Enter protein or nucleotide query as accession, gi, or sequence in FASTA format"
                        ></v-textarea>
                        <v-btn
                            depressed
                            color="info"
                            @click="submit"
                            :loading="loading"
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
                            label="E-Value Threshold"
                            v-model="query.eValueThreshold"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Maximum Number of hits"
                            v-model="query.maxHit"
                            required
                        ></v-text-field>
                        <v-checkbox
                            v-model="query.compositionBasedAdjustment"
                            label="Composition based statistics adjustment"
                        ></v-checkbox>
                        <v-checkbox
                            v-model="query.rescueBorderLineHits"
                            label="Rescue Borderline Hits"
                        ></v-checkbox>
                        <v-checkbox
                            v-model="query.suppressWeakOverLappingHits"
                            label="Suppress Weak Overlapping Hits"
                        ></v-checkbox>
                    </v-col>
                </v-card>
            </v-col>
        </v-row>
        <v-spacer style="height: 20px"></v-spacer>
        <v-card v-if="count > 0">
            <v-card-text>
                <v-data-table :headers="headers" :items="cdEntries">
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title
                                >Retrieved {{ count }} CDs</v-toolbar-title
                            >
                            <v-spacer></v-spacer>
                            <v-btn depressed color="info" @click="download"
                                >Download</v-btn
                            >
                        </v-toolbar>
                    </template>
                </v-data-table>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { DatabaseInterface } from '@/types/database'
import { SearchRequest } from '@/types/searchRequest'
import SearchService from '@/service/searchService'
import { CdEntry } from '@/types/cdEntry'
import fileDownload from 'js-file-download'
@Component
export default class Home extends Vue {
    private loading = false
    private databases: Array<DatabaseInterface> = [
        { id: 0, name: 'CDD v3.19 - 58235 PSSMs', value: 'cdd' },
        { id: 1, name: 'NCBI_Curated  - 17937 PSSMs', value: 'cdd_ncbi' },
    ]
    private headers: Array<Record<string, unknown>> = [
        { text: 'Accession', value: 'accession' },
        { text: 'Description', value: 'description' },
        { text: 'Interval', value: 'interval' },
        { text: 'EValue', value: 'evalue' },
    ]
    private query: SearchRequest = new SearchRequest()
    private cdEntries: Array<CdEntry> = []
    private count = 0
    async submit(): Promise<void> {
        this.loading = true
        try {
            const { count, data } = await SearchService.search(this.query)
            this.count = count
            this.cdEntries = data
        } catch (e) {
            console.log(JSON.stringify(e))
        }

        this.loading = false
    }
    download(): void {
        fileDownload(JSON.stringify(this.cdEntries), 'download.json')
    }
}
</script>

<style scoped></style>
