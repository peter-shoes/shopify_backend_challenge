import { createStore } from 'vuex'

export default createStore({
  state: {
    logged_in_user: null,
    photos:{}
  },
  mutations: {
    log_in(state, user) {
      if(!state.photos[user]) {
        state.photos[user] = []
      }
      state.logged_in_user = user
    },
    add_photo(state, info) {
      state.photos[info['username']] = info['photos']
      console.log(state.photos)
    }
  },
  actions: {
  },
  modules: {
  }
})
