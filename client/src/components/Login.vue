<template>
  <div style="min-height: 100vh;">
    <div class="q-pa-md" style="max-width: 400px">
      <h5>Login to the Image Repo!</h5>
      <q-banner v-if="this.login_error" inline-actions class="text-white bg-red">
        Username or Password is incorrect!
      </q-banner>
      <q-form
      class="q-gutter-md">
        <q-input
          filled
          v-model="username"
          label="Username"
        ></q-input>
        <q-input
          filled
          v-model="password"
          label="Password"
        ></q-input>
        <div>
          <q-btn @click="submit(username, password)" label="Submit" color="primary"/>
        </div>
      </q-form>
      <div>
        <router-link to="create_account" style="text-decoration:none;color=inherit;"><q-btn label="Create Account" color="secondary" style="margin-top:1em;"/></router-link>
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
        password: this.password,
        login_error: false
      }
    },
    methods: {
      update: function(hack) {
        this.login_error = hack;
        this.$forceUpdate();
      },
      login: function(username) {
        console.log(username)
        // move username to store
        // route to user's home page
        this.$router.push(`/home/${username}`)
      },
      submit: async function(username, password) {
        var hack=false
        var login = false
        await jQuery.ajax({
          type: "POST",
          url: 'http://localhost:5000/login',
          data: JSON.stringify({username: username, password: password}),
          contentType: "application/json; charset=utf-8",
          dataType:"json",
          encode: false,
          success: function(rx) {
            if (rx['status'] == 'failure') {
              hack=true
            }
            if (rx['status'] == 'success') {
              login = true
            }
          }
        });
        // ashamed of this workaround, but I am very tired
        this.update(hack)
        if (login) {this.login(username)}
      }
    }
}
</script>

<style>

</style>