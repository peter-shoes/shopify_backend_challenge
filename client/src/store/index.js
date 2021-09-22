import { createStore } from 'vuex'

export default createStore({
  state: {
    logged_in_user: null
  },
  mutations: {
    log_in(state, user) {
      state.logged_in_user = user
    }
  },
  actions: {
  },
  modules: {
  }
})
