<template>
  <div style="min-height: 100vh;">
    <div class="q-pa-md" style="max-width: 400px">
      <q-form
      class="q-gutter-md">
      <h5>Create a new account</h5>
        <q-input
          filled
          v-model="username"
          label="Username"
          lazy-rules
        ></q-input>
        <q-input
          filled
          v-model="password"
          label="Password"
          lazy-rules
        ></q-input>
        <div>
          <q-btn v-on:click="submit(username, password)" label="Submit" color="primary"></q-btn>
        </div>
      </q-form>
    </div>
  </div>
</template>

<script>
import jQuery from 'jquery'
export default {
    name: 'CreateAccount',
    methods: {
      submit: function(username, password) {
        jQuery.ajax({
          type: "POST",
          url: 'http://localhost:5000/create_user',
          data: JSON.stringify({username: username, password: password}),
          contentType: "application/json; charset=utf-8",
          dataType:"json",
          encode: false
        });
      }
    },
    data () {
        return {
            username: this.username,
            password: this.password
        }
    }
}
</script>

<style>

</style>