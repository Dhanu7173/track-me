<template>
  <q-page class="flex flex-center">
    <q-card class="login-card">
      <q-card-section>
        <div class="text-h6">Vendor Login</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <q-input
            filled
            type="email"
            v-model="form.email"
            label="Email *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter email']"
          />

          <q-input
            filled
            type="password"
            v-model="form.password"
            label="Password *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter password']"
          />

          <div>
            <q-btn label="Login" type="submit" color="primary"/>
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LoginPage',
  setup () {
    const $q = useQuasar()
    const router = useRouter()

    const form = ref({
      email: '',
      password: ''
    })

    const onSubmit = () => {
      // Here you would typically make an API call to authenticate the user
      // For now, we'll just show a success message and redirect to the onboarding page
      $q.notify({
        color: 'positive',
        message: 'Login successful!',
        icon: 'check'
      })
      router.push('/onboarding')
    }

    return {
      form,
      onSubmit
    }
  }
})
</script>

<style scoped>
.login-card {
  width: 100%;
  max-width: 400px;
}
</style>

