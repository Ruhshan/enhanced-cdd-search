<template>
  <v-app>
    <v-app-bar color="blue" app dark>
      <v-toolbar-title>Enhanced CDD Search</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-row>
          <v-col sm="8">
            <v-card style="height: 100%">
              <v-card-title>Search for Conserved Domains</v-card-title>
              <v-card-text>
                <v-textarea
                  rows="10"
                  outlined
                  label="Enter protein or nucleotide query as accession, gi, or sequence in FASTA format"
                ></v-textarea>
                <v-btn depressed color="info" @click="submit">Submit</v-btn>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col sm="4">
            <v-card>
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
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { DatabaseInterface } from '@/types/database';
import { Query } from '@/types/query';

@Component({ components: {} })
export default class App extends Vue {
  private databases: Array<DatabaseInterface> = [
    { id: 0, name: 'CDD v3.19 - 58235 PSSMs', value: 'cdd' },
    { id: 1, name: 'NCBI_Curated  - 17937 PSSMs', value: 'cdd_ncbi' },
  ];

  private query: Query = new Query();
  private submit(): void {
      console.log(JSON.stringify(this.query));
  }
}
</script>
