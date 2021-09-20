<template>
  <q-layout view="lHh Lpr lFf">
    <q-header>
      <q-toolbar>

        <q-toolbar-title>
          Shopify Backend Application
        </q-toolbar-title>

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

  setup () {
  }
}
</script>
