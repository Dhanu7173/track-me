<template>
  <div class="flex flex-center">
    <div class="q-pa-lg q-mt-md tw-shadow-xl tw-ring-2 tw-ring-slate-50 tw-px-6 tw-py-10 tw-rounded-2xl " style="width: 420px; border-radius: 10px">
      <q-card-section class="text-center">
        <q-avatar size="46px" color="black" text-color="white" icon="person_add" />
        <div class="text-h5 q-mt-md">Create an Account</div>
        <div class="text-subtitle2 text-grey-7">Sign up with your details</div>
      </q-card-section>

      <!-- <q-separator /> -->

      <div class="tw-pt-4">
        <div>
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2">
            Username <span class="tw-text-red-500">*</span>
          </label>
          <div class="bg-grey-2  tw-rounded-lg">
            <q-input v-model="username" placeholder="Username" dense borderless="" class="tw-w-full tw-pl-2">
            </q-input>
          </div>
        </div>
      </div>

      <div class="tw-pt-6">
        <div >
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2 tw-pt-0">
            Email <span class="tw-text-red-500">*</span>
          </label>
          <div class="bg-grey-2  tw-rounded-lg">
            <q-input  v-model="email" placeholder="Email" borderless dense type="email" class="tw-w-full tw-pl-2 tw-pb-0"
            :rules="[
                  val => val !== '' || 'Email is required',
                  val => /.+@.+\..+/.test(val) || 'Please enter a valid email'
              ]"
              >
              <template v-slot:append>
              <div class="tw-mr-2 tw-mb-2">
              <button
              v-if="!emailVerified"
              @click="sendEmailOTP"
              :loading="loadingEmail"
              class="tw-bg-green-500/85 tw-text-white tw-font-medium tw-py-1.5 tw-text-xs tw-px-4 tw-rounded  tw-ml-2"
              type="button"
            >
              Verify
            </button>
            <q-badge v-if="emailVerified" class=" tw-bg-green-500/85 q-ml-sm tw-py-1 tw-rounded-full">✔ </q-badge>
              </div>
              </template>
            </q-input>
          </div>
        </div>
         <div v-if="!emailVerified">
           <div class="tw-w-full bg-grey-2  tw-rounded-lg">
             <q-input v-if="showEmailOtpInput" v-model="emailOtp" borderless dense placeholder="Enter Email OTP"  class="q-mt-sm tw-pl-2 " />

           </div>
           <div class="tw-flex tw-justify-center tw-pt-3">
             <q-btn v-if="showEmailOtpInput" label="Verify Email" color="green" class=" tw-text-white tw-font-medium tw-py-1.5 tw-text-xs tw-px-4 tw-rounded tw-ml-2" outline @click="verifyEmailOTP" :loading="loadingEmailVerify"  />
           </div>
         </div>
        <!-- <q-badge v-if="emailVerified" color="green" class="q-m-sm">✔ Verified</q-badge> -->
      </div>

      <!-- <q-separator /> -->

      <div class="tw-pt-4">
        <div>
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2">
            Phone No. <span class="tw-text-red-500">*</span>
          </label>
          <div class="bg-grey-2  tw-rounded-lg">
            <q-input :rules="[
              val => val !=='' || 'Phone number is required',
              val => /^\d{10}$/.test(val) || 'Please enter a 10-digit phone number'
            ]" v-model="phone" placeholder="Phone Number" borderless dense type="tel" class="tw-w-full tw-ml-2 tw-pb-0">
              <template v-slot:append>
                <div class="tw-mr-2 tw-mb-2">
              <button
              v-if="!phoneVerified"
              @click="sendPhoneOTP"
              :loading="loadingPhone"
              class="tw-bg-green-500/85 tw-text-white tw-font-medium tw-py-1.5 tw-text-xs tw-px-4 tw-rounded focus:outline-none focus:shadow-outline tw-ml-2"
              type="button"
            >
              Verify
            </button>
            <q-badge v-if="phoneVerified"  class=" tw-bg-green-500/85 q-ml-sm tw-py-1 tw-rounded-full">✔ </q-badge>
                </div>
              </template>
            </q-input>
          </div>
        </div>
        <div v-if="!phoneVerified">
          <div class="tw-w-full bg-grey-2  tw-rounded-lg">
            <q-input v-if="showPhoneOtpInput" v-model="phoneOtp" dense borderless  placeholder="Enter Phone OTP"  class="q-mt-sm tw-pl-2 tw-w-full tw-bg-grey-2  tw-rounded-lg" />

          </div>
          <div class="tw-flex tw-justify-center tw-pt-3">
            <q-btn v-if="showPhoneOtpInput" label="Verify Phone" color="green" class=" tw-text-white tw-font-medium tw-py-1.5 tw-text-xs tw-px-4 tw-rounded tw-ml-2" outline @click="verifyPhoneOTP" :loading="loadingPhoneVerify"  />
          </div>
        </div>
      </div>
      <!-- <q-separator /> -->

      <div class="tw-pt-4">
        <div>
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2">
            Password <span class="tw-text-red-500">*</span>
          </label>
          <div class="bg-grey-2  tw-rounded-lg">
            <q-input required v-model="password" :type="showPassword ? 'text' : 'password'" placeholder="Password" borderless dense type="password" class="tw-w-full tw-pl-2">
              <template v-slot:append>
                <q-avatar
                  v-if="!showPassword"
                  clickable
                  @click="togglePassword"
                  size="md"
                  class="tw-absolute tw-right-3 tw-top-1/2 tw-transform tw--translate-y-1/2 tw-text-gray-400 tw-cursor-pointer"
                >
                <Icon icon="ph:eye-closed-bold" />
                </q-avatar>
                <q-avatar
                  v-else
                  clickable
                  @click="togglePassword"
                  size="md"
                  class="tw-absolute tw-right-3 tw-top-1/2 tw-transform tw--translate-y-1/2 tw-text-gray-400 tw-cursor-pointer"
                >
                <Icon icon="stash:eye-opened-light" />
                </q-avatar>
              </template>

            </q-input>
          </div>
        </div>
      </div>

      <!-- <q-separator /> -->

      <div class="tw-pt-6">
        <button no-caps @click="registerUser"  :loading="loadingRegister" :disabled="!canRegister"
            class="tw-w-full tw-bg-black tw-text-white tw-rounded-lg tw-p-3 tw-font-medium"
          >
            Register
          </button>
      </div>

      <q-card-section class="text-center text-grey-7">
        already have an account?
        <router-link to="/login" class="text-black">Sign In</router-link>
      </q-card-section>
    </div>
  </div>
</template>

<script>
import { api } from "boot/axios";
import { useQuasar } from "quasar"; // ✅ Import Quasar Notify
import { Icon } from '@iconify/vue';

export default {
  setup() {
    const $q = useQuasar(); // ✅ Use Quasar Notify
    return { $q };
  },
  components: {
    Icon
  },
  data() {
    return {
      username: "",
      email: "",
      emailOtp: "",
      phone: "",
      phoneOtp: "",
      password: "",
      showPassword: false,
      loadingEmail: false,
      loadingEmailVerify: false,
      loadingPhone: false,
      loadingPhoneVerify: false,
      loadingRegister: false,
      emailVerified: false,
      phoneVerified: false,
      showEmailOtpInput: false, // ✅ Control email OTP input visibility
      showPhoneOtpInput: false, // ✅ Control phone OTP input visibility
    };
  },
  computed: {
    canRegister() {
      return this.emailVerified && this.phoneVerified && this.username && this.password;
    }
  },
  methods: {

    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    showNotification(type, message) {
      this.$q.notify({
        type: type, // success, warning, negative, info
        message: message,
        position: "top",
        timeout: 2500, // Disappear after 2.5 sec
      });
    },
    async sendEmailOTP() {
      this.loadingEmail = true;
      try {
        await api.post("/users/send-email-otp", { email: this.email });
        this.showEmailOtpInput = true; // ✅ Show OTP input only after sending OTP
        this.showNotification("positive", "Email OTP sent successfully!");
      } catch (err) {
        this.showNotification("negative", err.response?.data?.error || "Failed to send Email OTP");
      }
      this.loadingEmail = false;
    },
    verifyEmailOTP() {
    this.loadingEmailVerify = true;

    this.$api.post("/users/verify-email-otp", { email: this.email, otp: this.emailOtp })
      .then(response => {
        if(response.data.ok){
          this.emailVerified = true;
          console.log("yessssssssssssssssssss")
          this.showNotification("positive", response.data.message);
        }
      else{
        this.showNotification("negative", res.data.error);
      }
      })
      .catch((err) => {
        this.showNotification("negative", err.response?.data?.error || "Invalid Email OTP");
      })
      .finally(() => {
        this.loadingEmailVerify = false;
      });
  },

    async sendPhoneOTP() {
      this.loadingPhone = true;
      try {
        await api.post("/users/send-phone-otp", { phone: this.phone });
        this.showPhoneOtpInput = true; // ✅ Show OTP input only after sending OTP
        this.showNotification("positive", "Phone OTP sent successfully!");
      } catch (err) {
        this.showNotification("negative", err.response?.data?.error || "Failed to send Phone OTP");
      }
      this.loadingPhone = false;
    },
    verifyPhoneOTP() {
    this.loadingPhoneVerify = true;
    this.$api.post("/users/verify-phone-otp", { phone: this.phone, otp: this.phoneOtp })
      .then(response => {
        if (response.data.ok) {
          this.phoneVerified = true;
          console.log("Phone verification successful");
          this.showNotification("positive", response.data.message);
        } else {
          this.showNotification("negative", response.data.error);
        }
      })
      .catch(err => {
        this.showNotification("negative", err.response?.data?.error || "Invalid Phone OTP");
      })
      .finally(() => {
        this.loadingPhoneVerify = false;
      });
  },
    async registerUser() {
      if (!this.canRegister) return;
      this.loadingRegister = true;
      try {
        const res = await api.post("/users/register", {
          username: this.username,
          email: this.email,
          phone: this.phone,
          password: this.password,
          emailVerified: this.emailVerified,
          phoneVerified: this.phoneVerified,
        });
        this.showNotification("positive", res.data.message);
        this.$router.push("/login");
      } catch (err) {
        this.showNotification("negative", err.response?.data?.error || "Failed to register");
      }
      this.loadingRegister = false;
    }
  }
};
</script>
