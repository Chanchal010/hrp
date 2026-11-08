<template>
	<ion-page>
		<ion-content class="ion-no-padding">
			<!-- Password Reset Dialog -->
			<div
				v-if="resetPassword.showDialog"
				class="flex h-screen w-screen flex-col bg-white"
			>
				<header class="flex items-center justify-between px-6 py-4 border-b border-gray-100">
					<div class="text-lg font-semibold text-gray-900">
						{{ __("Reset Password") }}
					</div>
					<button
						type="button"
						class="text-sm font-medium text-emerald-800 hover:text-emerald-950 underline"
						@click="resetPassword.showDialog = false"
					>
						{{ __("Back to Login") }}
					</button>
				</header>
				<div class="flex flex-1 flex-col items-center justify-center px-8 text-center max-w-md mx-auto">
					<p class="text-gray-700 leading-relaxed">
						{{ __("Your password has expired. Please reset your password to continue.") }}
					</p>
					<a
						class="mt-6 inline-flex items-center justify-center gap-2 transition-all text-white bg-[#173C2C] hover:bg-[#112F22] h-11 text-sm font-semibold px-6 rounded-full shadow-md"
						:href="resetPassword.link"
						target="_blank"
					>
						{{ __("Go to Reset Password page") }}
					</a>
				</div>
			</div>

			<!-- Main Two-Column Split Screen Login View -->
			<div v-else class="min-h-screen w-full flex items-center justify-center p-4 sm:p-6 bg-[#153426] bg-[radial-gradient(circle_at_50%_25%,#1d4533_0%,#11281e_85%,#0d1e16_100%)]">
				<div class="w-full max-w-4xl bg-white rounded-[28px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.55)] overflow-hidden flex flex-col md:flex-row">
					
					<!-- Left Pane: Sign In Form -->
					<div class="flex-1 p-8 sm:p-12 flex flex-col justify-between bg-white z-10">
						<!-- Brand Header -->
						<div class="flex items-center gap-3">
							<FrappeHRLogo class="h-9 w-auto object-contain" />
							<span class="text-xl font-bold text-gray-900 tracking-tight">ServiceDial<span class="text-[#184634]">TM</span></span>
						</div>

						<!-- Form Body -->
						<div class="my-6">
							<h1 class="text-2xl sm:text-3xl font-bold text-gray-900 tracking-tight mb-1">
								{{ __("Sign In") }}
							</h1>
							<p class="text-sm text-gray-500 mb-6">
								{{ __("Welcome back! Please enter your details to continue.") }}
							</p>

							<!-- Form Inputs -->
							<form v-if="!user_pass_login_disabled.data" class="flex flex-col space-y-4" @submit.prevent="submit">
								<div>
									<label class="block text-xs font-semibold text-gray-800 mb-1.5">{{ __("Email *") }}</label>
									<div class="flex items-center h-11 px-4 rounded-full bg-gray-100 border border-transparent focus-within:border-[#173C2C] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#173C2C]/10 transition-all">
										<svg class="w-4 h-4 text-gray-400 mr-2.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
										</svg>
										<input
											type="text"
											v-model="email"
											placeholder="name@company.com"
											class="w-full h-full bg-transparent border-none outline-none text-sm text-gray-900 placeholder-gray-400"
											autocomplete="username"
											required
										/>
									</div>
								</div>

								<div>
									<div class="flex justify-between items-center mb-1.5">
										<label class="block text-xs font-semibold text-gray-800">{{ __("Password *") }}</label>
										<router-link
											:to="{ name: 'ForgotPassword', query: email ? { email } : {} }"
											class="text-xs font-medium text-gray-500 hover:text-gray-900 transition-colors"
										>
											{{ __("Forgot password?") }}
										</router-link>
									</div>
									<div class="flex items-center h-11 px-4 rounded-full bg-gray-100 border border-transparent focus-within:border-[#173C2C] focus-within:bg-white focus-within:ring-4 focus-within:ring-[#173C2C]/10 transition-all">
										<svg class="w-4 h-4 text-gray-400 mr-2.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.8">
											<path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
										</svg>
										<input
											:type="showPassword ? 'text' : 'password'"
											v-model="password"
											placeholder="••••••••"
											class="w-full h-full bg-transparent border-none outline-none text-sm text-gray-900 placeholder-gray-400"
											autocomplete="current-password"
											required
										/>
										<button
											type="button"
											@click="showPassword = !showPassword"
											class="text-gray-400 hover:text-gray-600 focus:outline-none p-1"
										>
											<svg v-if="!showPassword" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.8">
												<path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
												<path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
											</svg>
											<svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.8">
												<path stroke-linecap="round" stroke-linejoin="round" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18"/>
											</svg>
										</button>
									</div>
								</div>

								<ErrorMessage :message="errorMessage" />

								<button
									type="submit"
									:disabled="session.login.loading"
									class="w-full h-12 rounded-full bg-[#173C2C] hover:bg-[#112F22] active:bg-[#0B2218] text-white font-semibold text-sm transition-all shadow-md shadow-[#173C2C]/25 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center gap-2 !mt-5"
								>
									<span v-if="session.login.loading" class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
									<span>{{ __("Sign In") }}</span>
								</button>
							</form>

							<!-- SSO Providers -->
							<template v-if="authProviders.data?.length">
								<div class="flex items-center gap-3 my-4">
									<div class="flex-1 h-px bg-gray-200"></div>
									<span class="text-[11px] font-semibold text-gray-400 tracking-wider">OR</span>
									<div class="flex-1 h-px bg-gray-200"></div>
								</div>
								<div class="space-y-2.5">
									<a
										v-for="provider in authProviders.data"
										:key="provider.name"
										class="w-full h-10 rounded-full border border-gray-200 hover:border-gray-300 bg-white hover:bg-gray-50 text-gray-700 text-xs font-medium flex items-center justify-center gap-2.5 transition-all"
										:href="provider.auth_url"
									>
										<img class="h-4 w-4" :src="provider.icon" :alt="provider.provider_name" />
										<span>Sign in with {{ provider.provider_name }}</span>
									</a>
								</div>
							</template>
						</div>

						<!-- Form Footer -->
						<div class="text-center text-xs text-gray-500 mt-4">
							<span>{{ __("Don't have an account?") }}</span>
							<a href="/#login#signup" class="font-semibold text-[#173C2C] underline ml-1">{{ __("Create One") }}</a>
						</div>
					</div>

					<!-- Right Pane: Testimonial & Editorial Line-Art Campus -->
					<div class="hidden md:flex flex-1 flex-col justify-between bg-[#F8F8F4] relative overflow-hidden pt-12 px-10">
						<!-- Quote Content -->
						<div class="z-10 max-w-sm">
							<div class="text-4xl text-[#E08A3C] font-serif font-bold leading-none mb-2">“</div>
							<p class="text-sm font-medium text-slate-800 leading-relaxed tracking-tight">
								A truly effortless HR &amp; payroll platform! I processed multi-tier salaries, verified biometric attendance, and generated compliant tax slips in under two minutes. The real-time employee self-service portal is a fantastic touch. I'll be using this for all our enterprise payroll cycles.
							</p>
							<div class="text-4xl text-[#E08A3C] font-serif font-bold leading-none text-right mb-4">”</div>

							<!-- Author Row -->
							<div class="flex items-center gap-3">
								<img
									:src="'/assets/hrms/images/testimonial-avatar.png'"
									alt="Carlos Benitez"
									class="w-11 h-11 rounded-full object-cover border-2 border-white shadow-sm"
								/>
								<div class="flex flex-col">
									<span class="text-sm font-bold text-gray-900">Carlos Benitez</span>
									<span class="text-xs text-gray-500">Madrid • Head of People Operations</span>
								</div>
							</div>
						</div>

						<!-- Corporate Campus Bottom Art -->
						<div class="relative w-[calc(100%+80px)] -ml-10 -mr-10 pointer-events-none mt-6">
							<img
								:src="'/assets/hrms/images/hr-campus-art.png'"
								alt="ServiceDialTM Corporate Campus"
								class="w-full h-auto object-contain object-bottom block"
							/>
						</div>
					</div>

				</div>
			</div>

			<!-- OTP Verification Dialog -->
			<Dialog v-model="otp.showDialog">
				<template #body-title>
					<h2 class="text-lg font-bold">{{ __("OTP Verification") }}</h2>
				</template>
				<template #body-content>
					<p class="mb-4 text-sm text-gray-600" v-if="otp.verification.prompt">
						{{ otp.verification.prompt }}
					</p>

					<form class="flex flex-col space-y-4" @submit.prevent="submit">
						<Input
							:label="__('OTP Code')"
							type="text"
							placeholder="000000"
							v-model="otp.code"
							autocomplete="one-time-code"
						/>
						<ErrorMessage :message="errorMessage" />
						<Button
							:loading="session.otp.loading"
							variant="solid"
							class="w-full h-11 rounded-full bg-[#173C2C] hover:bg-[#112F22] text-white font-semibold !mt-4"
						>
							{{ __("Verify") }}
						</Button>
					</form>
				</template>
			</Dialog>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue"
import { inject, reactive, ref } from "vue"
import { Input, Button, ErrorMessage, Dialog, createResource } from "frappe-ui"

import FrappeHRLogo from "@/components/icons/FrappeHRLogo.vue"

const email = ref(null)
const password = ref(null)
const showPassword = ref(false)
const errorMessage = ref("")

const resetPassword = reactive({
	showDialog: false,
	link: "",
})
const otp = reactive({
	showDialog: false,
	tmp_id: "",
	code: "",
	verification: {},
})

const session = inject("$session")
const __ = inject("$translate")

async function submit(e) {
	try {
		let response
		if (otp.showDialog) {
			response = await session.otp(otp.tmp_id, otp.code)
		} else {
			response = await session.login(email.value, password.value)
		}

		if (response.message === "Password Reset") {
			resetPassword.showDialog = true
			resetPassword.link = response.redirect_to
		} else {
			resetPassword.showDialog = false
			resetPassword.link = ""
		}

		// OTP verification
		if (response.verification) {
			if (response.verification.setup) {
				otp.showDialog = true
				otp.tmp_id = response.tmp_id
				otp.verification = response.verification
			} else {
				window.open("/login?redirect-to=" + encodeURIComponent(window.location.pathname), "_blank")
			}
		}
	} catch (error) {
		errorMessage.value = error.messages ? error.messages.join("\n") : (error.message || "Login failed")
	}
}

const user_pass_login_disabled = createResource({
	url: "hrms.api.system_settings.get_user_pass_login_disabled",
	method: 'GET',
	initialData: 0,
	auto: true,
})

const authProviders = createResource({
	url: "hrms.api.oauth.oauth_providers",
	auto: true,
})
</script>
