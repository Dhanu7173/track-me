<template>
  <q-page class="flex flex-center">
    <q-card class="registration-card">
      <q-card-section>
        <div class="text-h6">Vendor Registration</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <q-input
            filled
            v-model="form.companyName"
            label="Company Name *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter company name']"
          />

          <q-select
            filled
            v-model="form.businessType"
            :options="businessTypes"
            label="Business Type *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please select business type']"
          />

          <q-select
            filled
            v-model="form.industry"
            :options="industries"
            label="Industry *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please select industry']"
          />

          <q-input
            filled
            v-model="form.fullName"
            label="Full Name *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter full name']"
          />

          <q-input
            filled
            v-model="form.designation"
            label="Designation *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter designation']"
          />

          <q-input
            filled
            type="email"
            v-model="form.email"
            label="Email *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter email',
                      val => val && /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(val) || 'Please enter a valid email']"
          />

          <q-input
            filled
            type="tel"
            v-model="form.phoneNumber"
            label="Phone Number *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please enter phone number',
                      val => val && /^\d{10}$/.test(val) || 'Please enter a valid 10-digit phone number']"
          />

          <q-input
            filled
            type="password"
            v-model="form.password"
            label="Password *"
            lazy-rules
            :rules="[ val => val && val.length >= 8 || 'Password must be at least 8 characters']"
          />

          <q-input
            filled
            type="password"
            v-model="form.confirmPassword"
            label="Confirm Password *"
            lazy-rules
            :rules="[ val => val === form.password || 'Passwords do not match']"
          />

          <q-toggle v-model="form.enable2FA" label="Enable Two-Factor Authentication (2FA)" />

          <div>
            <q-btn label="Register" type="submit" color="primary"/>
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
  name: 'RegistrationPage',
  setup () {
    const $q = useQuasar()
    const router = useRouter()

    const form = ref({
      companyName: '',
      businessType: '',
      industry: '',
      fullName: '',
      designation: '',
      email: '',
      phoneNumber: '',
      password: '',
      confirmPassword: '',
      enable2FA: false
    })

    const businessTypes = [
      'Manufacturer', 'Distributor', 'Supplier', 'Service Provider'
    ]

    const industries = [
      'IT', 'FMCG', 'Healthcare', 'Retail', 'Other'
    ]

    const onSubmit = () => {
      // Here you would typically make an API call to register the user
      // For now, we'll just show a success message
      $q.notify({
        color: 'positive',
        message: 'Registration successful! Please check your email for verification.',
        icon: 'check'
      })
      // You would then redirect to a verification page or login page
      router.push('/onboarding')
    }

    return {
      router,
      form,
      businessTypes,
      industries,
      onSubmit
    }
  }
})
</script>

<style scoped>
.registration-card {
  width: 100%;
  max-width: 400px;
}
</style>

