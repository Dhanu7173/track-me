import { defineStore } from "pinia";

export const authStore = defineStore("auth", {
  state: () => ({
    session: {
      id: "",
      email: "",
      phone: "",
      isLoggedIn: false,
      stage: "",
      token: "",
      kyc_status: "",
    },
  }),
  getters: {
    isLoggedIn(state) {
      return state.session.id !== null;
    },
    getSessionData(state) {
      return state.session;
    },
  },
  actions: {
    setLoginSession(data,token) {
        console.log(data, "data");
        
      this.session.isLoggedIn = true;
      this.session.id = data.id;
      this.session.email = data.email;
      this.session.phone = data.phone;
      this.session.stage = data.stage;
      this.session.token = token;
      this.session.kyc_status = data.kyc_status
    },
    saveAfterKYC(){
      this.session.kyc_status = "Completed";
    },
    destroyLoginSession() {
      this.session.isLoggedIn = false;
      this.session.id = "";
      this.session.email = "";
      this.session.phone = "";
      this.session.stage = "";
      this.session.token = "";
      this.session.kyc_status = "";
    },
  },
  persist: true,
});
