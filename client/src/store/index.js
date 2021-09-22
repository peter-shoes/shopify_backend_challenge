import { createStore } from 'vuex'

export default createStore({
  state: {
    logged_in_user: null,
    photos:[]
  },
  mutations: {
    log_in(state, user) {
      state.logged_in_user = user
    },
    add_photo(state, photo) {
      state.photos.push(photo)
    }
  },
  actions: {
  },
  modules: {
  }
})
