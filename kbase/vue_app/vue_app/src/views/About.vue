<template>
  <div class="about">
    <h1 class="subheading">This is an about page</h1>
    <v-container class="my-5">content</v-container>

    <vue-plotly :data="data" :layout="layout" :options="options" @click="handler" @select="handler"/>
  </div>
</template>

<script>
import VuePlotly from "@statnett/vue-plotly";

export default {
  components: {
    VuePlotly
  },
  data: function() {
    return {
      data: [{ x: [1, 3], y: [2, 4] }],
      layout: {},
      options: {}
    };
  },

  methods: {
    handler(event) {
      console.log("handled");
      console.log(event);
    }
  }
};
</script>