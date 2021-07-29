<template>
    <div>
        <v-spacer style="height: 20px"></v-spacer>
        <v-card v-if="count > 0">
            <v-card-text>
                <v-data-table :headers="headers" :items="filteredResults">
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title
                                >Retrieved {{ count }} CDs<span
                                    v-if="filteredCds"
                                    >| Filtered {{ filteredCds }} CDs</span
                                ></v-toolbar-title
                            >
                            <v-spacer></v-spacer>
                            <v-col cols="3">
                                <v-select
                                    :items="dbPrefixes"
                                    item-text="name"
                                    item-value="value"
                                    label="Filter Sources"
                                    v-model="selectedDbPrefix"
                                >
                                    <template v-slot:append-outer>
                                        <v-btn
                                            depressed
                                            color="info"
                                            @click="downloadFasta"
                                            >Download</v-btn
                                        >
                                    </template>
                                </v-select>
                            </v-col>
                        </v-toolbar>
                    </template>
                </v-data-table>
            </v-card-text>
        </v-card>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { BatchCdEntry } from '@/types/cdEntry'

import fileDownload from 'js-file-download'

@Component({})
export default class ResultTable extends Vue {
    @Prop() results!: Array<BatchCdEntry>
    private tableRows: Array<BatchCdEntry> = []
    private headers: Array<Record<string, unknown>> = [
        { text: 'Query', value: 'query' },
        { text: 'Accession', value: 'accession' },
        { text: 'Interval', value: 'interval' },
        { text: 'EValue', value: 'evalue' },
        { text: 'Description', value: 'description' },
    ]
    private dbPrefixes = [
        { name: 'None', value: '' },
        { name: 'CD', value: 'cd' },
        { name: 'SMART', value: 'smart' },
        { name: 'PFAM', value: 'pfam' },
    ]
    private selectedDbPrefix = ''
    private filteredCds = 0

    get count(): number {
        return this.results.length
    }

    get filteredResults(): Array<BatchCdEntry> {
        if (this.selectedDbPrefix) {
            var filteredResults = this.results.filter(
                r => r.accession.indexOf(this.selectedDbPrefix) == 0
            )
            this.filteredCds = filteredResults.length
            return filteredResults
        } else {
            this.filteredCds = 0
            return this.results
        }
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
