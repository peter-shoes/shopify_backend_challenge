<template>
  <div>
    <h4>Welcome Home {{$route.params.username}}!</h4>
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
  </div>
</template>

<script>
// import { useQuasar } from 'quasar'
// const $q = useQuasar()

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
    }
  }
}
</script>
