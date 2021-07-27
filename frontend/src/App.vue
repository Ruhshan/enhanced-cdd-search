<template>
    <v-app>
        <v-app-bar color="blue" app dark>
            <v-toolbar-title>Enhanced CDD Search</v-toolbar-title>
          <router-link class="nav-button" to="/">
                <v-btn color="white" text>Solo</v-btn>
          </router-link>
          <router-link class="nav-button" to="/batch-search">
                <v-btn color="white" text>Batch</v-btn>
            </router-link>
        </v-app-bar>

        <v-main>
            <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({ components: {} })
export default class App extends Vue {}
</script>

<style lang="css">
.nav-button {
    margin-left: 16px;
    text-decoration: none;
}
.options {
    color: white;
}
</style>
