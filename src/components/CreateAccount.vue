<template>
  <div style="min-height: 100vh;">
    <div class="q-pa-md" style="max-width: 400px">
      <q-form
      class="q-gutter-md">
      <h5>Create a new account</h5>
      <q-banner v-if="this.creation_error" inline-actions class="text-white bg-red">
        Username already exists!
      </q-banner>
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
    data () {
      return {
        username: this.username,
        password: this.password,
        creation_error: false
      }
    },
    methods: {
      update: function(hack) {
        this.creation_error = hack;
        this.$forceUpdate();
      },
      submit: async function(username, password) {
        var hack=false
        var home = false
        await jQuery.ajax({
          type: "POST",
          url: 'http://localhost:5000/create_user',
          data: JSON.stringify({username: username, password: password}),
          contentType: "application/json; charset=utf-8",
          dataType:"json",
          encode: false,
          success: function(rx) {
            if (rx['status'] == 'failure'){
              hack=true
            }
            if (rx['status'] == 'success'){
              hack=false
              home= true
            }
          }
        });
        this.update(hack)
        if (home) {this.$router.push('/')}
      }
    }
}
</script>
