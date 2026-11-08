import frappe
from frappe.utils.oauth import get_oauth2_providers
from frappe.website.utils import get_home_page

no_cache = True

def get_context(context):
	redirect_to = frappe.local.request.args.get("redirect-to")

	if frappe.session.user != "Guest":
		if not redirect_to:
			if frappe.session.data.user_type == "Website User":
				redirect_to = get_home_page()
			else:
				redirect_to = "/app"
		frappe.local.flags.redirect_location = redirect_to
		raise frappe.Redirect

	context.no_header = True
	context.no_breadcrumbs = True
	context.no_footer = True
	context.title = "Sign In - ServiceDialTM HRMS"
	context.app_name = "ServiceDialTM HRMS"
	context.app_logo = "/assets/hrms/images/servicedial-logo.webp"
	context.banner_image = "/assets/hrms/images/servicedial-logo.webp"
	context.favicon = "/assets/hrms/images/servicedial-favicon.png"

	# Pull core context if available
	try:
		from frappe.www.login import get_context as core_get_context
		core_ctx = core_get_context(context)
		if core_ctx:
			context.update(core_ctx)
	except Exception:
		pass

	# Ensure our custom branding remains dominant
	context["app_name"] = "ServiceDialTM HRMS"
	context["app_logo"] = "/assets/hrms/images/servicedial-logo.webp"
	context["banner_image"] = "/assets/hrms/images/servicedial-logo.webp"
	context["favicon"] = "/assets/hrms/images/servicedial-favicon.png"

	# Check for Google social login URL
	context["google_login_url"] = None
	if context.get("provider_logins"):
		for provider in context["provider_logins"]:
			if "google" in provider.get("name", "").lower() or "google" in provider.get("provider_name", "").lower():
				context["google_login_url"] = provider.get("auth_url")
				break

	return context
