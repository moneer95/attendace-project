# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns = [ 
		{ 'fieldname': 'employee_name', 'label': _('Employee'), 'fieldtype': 'Data' }, 
		{ 'fieldname': 'attendance_date', 'label': _('Attendance Date'), 'fieldtype': 'Date' }
		{ 'fieldname': 'check_in', 'label': _('Check Out'), 'fieldtype': 'Time' }
		{ 'fieldname': 'check_out', 'label': _('Check Out'), 'fieldtype': 'Time' }
		]
	data = frappe.db.get_all("Attendance", ["employee_name", "attendance_date", "check_in", "check_out"])

	return columns, data
