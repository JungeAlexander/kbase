<template>
  <v-content>
    <v-app-bar color="grey darken-3" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title class="text-uppercase">
        <span class="font-weight-light">k</span>
        <span>base</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-menu left bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item v-for="n in 5" :key="n" @click="() => {}">
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-btn color="grey darken-2">
        <span>Sign Out</span>
        <v-icon right>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" class="grey darken-3">
      <v-col align-center>
        <v-flex class="mt-5">
          <v-avatar size="100">
            <img class="text-lg-center" src="/avatar-2.png" />
          </v-avatar>
          <p class="white--text subheading mt-1">Ryu</p>
        </v-flex>
      </v-col>
      <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-icon>
            <v-icon class="white--text">{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-content>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
        { icon: "mdi-folder", text: "Archive", route: "/archive" },
        {
          icon: "mdi-account",
          text: "Recommendations",
          route: "/recommendations"
        },
        { icon: "mdi-information", text: "About", route: "/about" }
      ]
    };
  }
};
</script>

<style>
</style>