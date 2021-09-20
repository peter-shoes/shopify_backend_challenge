<template>
  <div style="min-height: 100vh;">
    <div class="q-pa-md" style="max-width: 400px">
      <q-form
      class="q-gutter-md">
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
          <q-btn v-on:click="login_submit(username)" label="Submit" type="submit" color="primary"></q-btn>
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm"></q-btn>
        </div>
      </q-form>
      <div>
        <q-btn label="Create Account" type="submit" color="primary"></q-btn>
      </div>
    </div>
  </div>
</template>

<script>
import jQuery from 'jquery'

export default {
    name: 'Landing',
    data () {
      return{
        username: this.username,
        password: this.password
      }
    },
    methods: {
      login_submit: function(username) {
        jQuery.ajax({
          type: 'POST',
          url: 'http://localhost:5000/login_submit',
          json: `{'username':'${username}'}`,
          dataType:'json',
          success: function(stuff) {
            console.log(stuff)
          },
          crossDomain: true
        });
      }
    }
}
</script>

<style>

</style>