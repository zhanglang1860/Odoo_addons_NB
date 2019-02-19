from odoo.tests.common import TransactionCase

# class TestProject(TransactionCase):
#     def setUp(self, *args, **kwargs):
#         result = super().setUp(*args, **kwargs)
#         self.Project = self.env['autoreport.project']
#         self.project_ode = self.Project.create({
#             'name': 'Odoo Development Essentials',
#             'order_number': '879-1-78439-279-6'})
#         return result
#     def test_create(self):
#         "Test Projects are active by default"
#         self.assertEqual(self.project_ode.active, True)