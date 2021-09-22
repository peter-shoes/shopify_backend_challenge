<template>
  <div>
    <q-card :bordered="true" style="text-align:center;">
      <h4>{{$route.params.username}}'s Page</h4>
      <h5 v-if="$route.params.username == $store.state.logged_in_user">Welcome Home {{$route.params.username}}!</h5>
    </q-card>
    <q-uploader
    ref="uploader"
    label="Upload Picture"
    accept="image/*"
    :max-files="1"
    color="secondary"
    :form-fields="[{name:'username', value: $route.params.username}]"
    :factory="uploadImage"
    @uploaded="onUploaded"
    @failed="onFailed"
    @rejected="onRejected"
    />
    <div style="margin-top:1em;">
      <q-img v-for="photo in this.$store.state.photos" v-bind:key="photo" :src="photo"  height="200px" width="200px" ratio="1"/>
    </div>
  </div>
</template>

<script>
import jQuery from 'jquery'

const $ = jQuery

export default {
  name: 'Home',
  props: ['username'],
  data() {
    return {
      selected_file:'',
      check_if_document_upload:false
    }
  },
  methods: {
    uploadImage(file) {
      console.log(file)
      return {
        url: 'http://localhost:5000/upload',
        method: 'POST'
      }
    },
    onUploaded(info) {
      console.log(info)
      this.$refs.uploader.reset()
      this.getPhotos()
      // $q.notify({
      //   type: 'positive',
      //   message: `${info.name} successfully uploaded`
      // })
    },
    onFailed(info) {
      let err = JSON.parse(info.xhr.response)
      console.log(err)
      // let files = info.files
      // files.forEach(item => {
      //   $q.notify({
      //     type: 'negative',
      //     message: `${item.name} - ${err.error} Error ${err.message}`
      //   })
      // })
    },
    onRejected(rejectedEntries) {
      console.log(rejectedEntries)
      // $q.notify({
      //   type: 'negative',
      //   message: `${rejectedEntries.length} file(s) did not pass validation constraints`
      // })
    },
    getPhotos: async function() {
      const names = await $.get(`http://localhost:5000/get_user_photos/${this.$route.params.username}`, function(status){
        console.log(status)
      })
      var files = []
      for (var i in names['files']) {
        var file_name = names['files'][i]
        const file = `http://localhost:5000/get_item/${this.$route.params.username}/${file_name}`
        files.push(file)
      }
      this.$store.commit('add_photo', files)
    }

  },
  created () {
    this.unsubscribe = this.$store.subscribe((mutation) => {
      if (mutation.type === 'add_photo') {
          this.$forceUpdate();
      }
    })
  },
  mounted () {
    this.getPhotos()
  },
  beforeUnmount() {
    this.unsubscribe()
  }
}
</script>
