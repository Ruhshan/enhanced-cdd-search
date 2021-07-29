<template>
    <div>
        <v-spacer style="height: 20px"></v-spacer>
        <v-card v-if="count > 0">
            <v-card-text>
                <v-data-table :headers="headers" :items="results">
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title
                                >Retrieved {{ count }} CDs</v-toolbar-title
                            >
                            <v-spacer></v-spacer>
                            <v-btn depressed color="info" @click="downloadFasta"
                                >Download</v-btn
                            >
                        </v-toolbar>
                    </template>
                </v-data-table>
            </v-card-text>
        </v-card>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { BatchCdEntry } from '@/types/cdEntry'
import SearchService from '@/service/searchService'
import fileDownload from 'js-file-download'

@Component({})
export default class ResultTable extends Vue {
    private results: Array<BatchCdEntry> = []
    private count = 0
    private headers: Array<Record<string, unknown>> = [
        { text: 'Query', value: 'query' },
        { text: 'Accession', value: 'accession' },
        { text: 'Description', value: 'description' },
        { text: 'Interval', value: 'interval' },
        { text: 'EValue', value: 'evalue' },
    ]
    private async mounted(): Promise<void> {
        this.results = await SearchService.dummy()
        this.count = this.results.length
    }

    private async downloadFasta(): Promise<void> {
        var fasta = ''

        this.results.forEach(entry => {
            const secquenceHeader = `>${entry.query}_${entry.accession}_${entry.interval}`
            fasta += `${secquenceHeader}\n${entry.sequence}}\n\n`
        })
        fileDownload(fasta, 'search_id.txt')
    }
}
</script>

<style scoped></style>
