<template>
  <v-app>
    <v-app-bar color="blue" app dark>
      <v-toolbar-title>Enhanced CDD Search</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-row>
          <v-col sm="8">
            <v-card>
              <v-card-title>Search for Conserved Domains</v-card-title>
              <v-card-text>
                <v-textarea
                  outlined
                  label="Enter protein or nucleotide query as accession, gi, or sequence in FASTA format"
                ></v-textarea>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col sm="4">
            <v-card>
              <v-card-title>Options</v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "App",

  data: () => ({
    //
  }),
});
</script>
