<template>
  <div class="tw-min-h-screen tw-flex tw-items-center tw-justify-center tw-bg-white tw-p-6">
    <div class="tw-w-full tw-max-w-sm tw-shadow-xl tw-ring-2 tw-ring-slate-50 tw-px-6 tw-py-10 tw-rounded-2xl">
      <div class="tw-mb-8 tw-text-left">
        <!-- <div class="tw-w-12 tw-h-12 tw-bg-black tw-rounded-full tw-mb-6"></div> -->
        <h1 class="tw-text-2xl tw-font-semibold tw-mb-2">Sign In</h1>
        <p class="tw-text-gray-500 tw-text-sm">
          Be sure to enter your legal name as it appears on your government-issued ID.
        </p>
      </div>

      <form class="tw-space-y-6">
        <!-- Email -->
        <div>
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2">
            Email <span class="tw-text-red-500">*</span>
          </label>
          <q-input
            v-model="email"
            dense
            type="email"
            placeholder="mail@domain.com"
            borderless
            input-class="q-pl-sm"
            class="tw-w-full bg-grey-2 tw-rounded-lg tw-mt-3"
          />
        </div>

        <!-- Password -->
        <div>
          <label class="tw-block tw-text-sm tw-font-medium tw-mb-2">
            Password <span class="tw-text-red-500">*</span>
          </label>
          <div class="tw-relative">
            <q-input
              v-model="password"
              dense
              :type="showPassword ? 'text' : 'password'"
              placeholder="Enter password"
              borderless
              input-class="q-pl-sm"
              class="tw-w-full bg-grey-2 tw-rounded-lg tw-mt-3"
            />
            <q-avatar v-if="!showPassword" clickable @click="togglePassword" size="md" class="tw-absolute tw-right-3 tw-top-1/2 tw-transform tw--translate-y-1/2 tw-text-gray-400 tw-cursor-pointer" ><Icon icon="ph:eye-closed-bold" /></q-avatar>
            <q-avatar v-else clickable @click="togglePassword" size="lg" class="tw-absolute tw-right-3 tw-top-1/2 tw-transform tw--translate-y-1/2 tw-text-gray-400 tw-cursor-pointer" ><Icon icon="stash:eye-opened-light" /></q-avatar>
            <!-- <q-btn
              flat
              unelevated
              no-caps
              class="tw-absolute tw-right-0 tw-top-1/2 tw-transform tw--translate-y-1/2 tw-text-gray-400 tw-no-hover"
              @click="togglePassword"
            >
              <Icon icon="ph:eye-closed-bold" />
            </q-btn> -->
          </div>
        </div>

        <!-- Submit Button -->
        <q-btn no-caps @click="loginUser" :loading="loading"
          class="tw-w-full tw-bg-black tw-text-white tw-rounded-lg tw-p-3 tw-font-medium"
        >
          Sign In
        </q-btn>

        <!-- Divider -->
        <!-- <div class="tw-text-center tw-text-sm tw-text-gray-500">Or</div> -->

        <!-- Apple Login -->
        <!-- <button
          type="button"
          class="tw-w-full tw-border tw-border-gray-200 tw-rounded-lg tw-p-3 tw-flex tw-items-center tw-justify-center tw-space-x-2"
          @click="socialLogin('apple')"
        >
          <AppleIcon />
          <span>Continue with Apple</span>
        </button> -->

        <!-- Google Login -->
        <!-- <button
          type="button"
          class="tw-w-full tw-border tw-border-gray-200 tw-rounded-lg tw-p-3 tw-flex tw-items-center tw-justify-center tw-space-x-2"
          @click="socialLogin('google')"
        >
          <MailIcon class="tw-text-blue-500" />
          <span>Continue with Google</span>
        </button> -->

        <!-- Sign In Link -->
        <p class="tw-text-right tw-text-sm tw-text-gray-500">
          Don't have an account?
          <router-link to="/register" class="tw-text-gray-500 tw-underline">Sign up here</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import { useQuasar } from "quasar";
import { authStore } from "src/stores/auth";
import { Icon } from '@iconify/vue';
export default {
  setup() {
    const $q = useQuasar(); // Use Quasar Notify
    return { $q };
  },
  components: {
    Icon
  },
  data() {
    return {
      authstore: authStore(),
      email: "",
      password: "",
      loading: false,
      showPassword: false
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    showNotification(type, message) {
      this.$q.notify({
        type: type,
        message: message,
        position: "top",
        timeout: 2500
      });
    },

    loginUser() {
      this.loading = true;

      this.$api.post("/users/login", {
        email: this.email,
        password: this.password
      })
      .then((res) => {
        console.log(res.data);

        this.authstore.setLoginSession(res.data.data.user, res.data.data.token);

        this.showNotification("positive", "Login successful!");
        this.$router.push("/"); // Redirect after login
      })
      .catch((err) => {
        this.showNotification("negative", err.response?.data?.error || "Login failed");
      })
      .finally(() => {
        this.loading = false;
      });
    }
  }
};
</script>
