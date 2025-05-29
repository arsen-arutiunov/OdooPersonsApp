from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class PersonsController(http.Controller):

    @http.route('/persons', type='http', auth='public', website=True)
    def persons_list(self, **kwargs):
        persons = request.env['persons.person'].sudo().search(
            [],
            limit=5,
            order='id desc'
        )
        return request.render('persons.persons_template',
                              {'persons': persons})

    @http.route('/persons/add', type='http', auth='public',
                methods=['GET', 'POST'], website=True)
    def persons_add(self, **post):
        csrf_token = request.csrf_token()
        if request.httprequest.method == 'POST':
            vals = {
                'first_name': post.get('first_name'),
                'last_name': post.get('last_name'),
                'birthday': post.get('birthday'),
                'sex': post.get('sex'),
                'company_id': request.env.company.id,
            }
            request.env['persons.person'].sudo().create(vals)
            return request.redirect('/persons')
        return request.render('persons.person_form_template',
                              {'csrf_token': csrf_token})
