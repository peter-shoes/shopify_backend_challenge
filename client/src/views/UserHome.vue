<template>
  <div>
    <h3>Welcome Home {{$route.params.username}}!</h3>
  </div>
</template>

<script>

export default {
  name: 'Home',
  props: ['username'],
  components: {
  }
}
</script>
