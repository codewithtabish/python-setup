from flask import Blueprint
from controllers import home,signup,get_all_users,tags_extractor,generate_qr_method,convert_currency,ip_info,domain_info,ocr_from_url,extract_seo





routes = Blueprint('routes', __name__)

routes.add_url_rule("/", view_func=home)
routes.add_url_rule("/signup", view_func=signup,methods=[ 'POST'])
routes.add_url_rule("/users", view_func=get_all_users)
routes.add_url_rule("/tags_extractor", view_func=tags_extractor,methods=[ 'POST'])
routes.add_url_rule("/generate_qr", view_func=generate_qr_method,methods=[ 'POST'])
routes.add_url_rule("/conversion_rate", view_func=convert_currency,methods=[ 'POST'])
routes.add_url_rule("/ip_info", view_func=ip_info)
routes.add_url_rule("/domain_info", view_func=domain_info)
routes.add_url_rule("/image_text_extractor", view_func=ocr_from_url,methods=[ 'POST'])
routes.add_url_rule("/website_seo_tags", view_func=extract_seo,methods=[ 'POST'])


