<template>
    <v-container>
        <v-row>
            <v-col sm="8">
                <v-card style="height: 100%" :loading="loading">
                    <v-card-title>Enter query protein sequences</v-card-title>
                    <v-card-text>
                        <v-textarea
                            rows="10"
                            outlined
                            label="Batch CD-Search accepts only protein sequences.(Max 4000)"
                        ></v-textarea>
                        <v-btn depressed color="info" :loading="loading"
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
                            :items="databases"
                            item-text="name"
                            item-value="value"
                            label="Select Database"
                            required
                        ></v-select>
                        <v-text-field
                            label="E-Value Threshold"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Maximum Number of hits"
                            required
                        ></v-text-field>
                        <v-checkbox
                            label="Composition Corrected Scoring"
                        ></v-checkbox>
                        <v-checkbox
                            label="Apply Low Complexity Filter"
                        ></v-checkbox>
                        <v-checkbox
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
@Component({})
export default class BatchSearch extends Vue {
    private loading = false
    private databases: Array<DatabaseInterface> = [
        { id: 0, name: 'CDD -- 58235 PSSMs', value: 'cdd' },
        { id: 1, name: 'NCBI_Curated -- 17937 PSSMs', value: 'cdd_ncbi' },
    ]
}
</script>

<style scoped></style>
