<template>
  <q-layout view="lHh Lpr lFf">
    <q-header>
      <q-toolbar>

        <q-toolbar-title>
          Shopify Backend Application
        </q-toolbar-title>
        <div style="padding-right:1em;"><q-btn @click="logout" label="Logout" color="secondary"></q-btn></div>
        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'LayoutDefault',

  components: {
  },

  methods: {
    logout() {
      this.$store.commit('log_in', null)
      this.$router.push('/')
    }
  },

  setup () {
  }
}
</script>
