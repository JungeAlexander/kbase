<template>
  <v-app>
    <Navbar />

    <v-content class="mx-4 mb-4">
      <v-container class="fill-height" fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar";

export default {
  name: "App",
  components: { Navbar },

  data: () => ({
    //
  })
};
</script>
