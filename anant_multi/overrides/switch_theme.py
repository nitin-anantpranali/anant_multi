import frappe

@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "Anant_red_theme", "anant_blue_theme", "anant_orange_theme", "anant_green_theme"]:
		frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)