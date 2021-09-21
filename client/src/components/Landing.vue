<template>
  <div class="row justify-center" style="min-height: 100vh;">
    <div class="full-height full-width q-pa-md">
      
      <q-banner v-if="login_error" inline-actions class="text-white bg-red">
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
          <q-btn @click="submit()" label="Submit" type="submit" color="primary"></q-btn>
        </div>
      </q-form>
      <div>
        <q-btn label="Create Account" type="submit" color="secondary" style="margin-top:1em;"><router-link to="create_account"/></q-btn>
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
      update: function() {
        this.login_error = true;
        this.$forceUpdate();
      },
      submit: async function(username) {
        var hack=false
        await jQuery.ajax({
          type: "POST",
          url: 'http://localhost:5000/login',
          data: JSON.stringify({username: username}),
          contentType: "application/json; charset=utf-8",
          dataType:"json",
          encode: false,
          success: function(rx) {
            if (rx['status'] == 'failure') {
              hack=true
            }
            if (rx['status'] == 'success') {
              // fix later
              console.log(rx)
            }
          }
        });
        // ashamed of this workaround, but I am very tired
        if (hack) {this.update()}
      }
    }
}
</script>

<style>

</style>