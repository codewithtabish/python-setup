from flask import Blueprint
from controllers import home, about, products, mobile_list, service, mood_checker, live_score,kotlin_func,all_courses,signup,get_all_users,tags_extractor,generate_qr_method,convert_currency,ip_info,domain_info





routes = Blueprint('routes', __name__)

routes.add_url_rule("/", view_func=home)
routes.add_url_rule("/about", view_func=about)
routes.add_url_rule("/products", view_func=products)
routes.add_url_rule("/mobiles", view_func=mobile_list)
routes.add_url_rule("/services", view_func=service)
routes.add_url_rule("/mood_checker", view_func=mood_checker)
routes.add_url_rule("/live_score", view_func=live_score)
routes.add_url_rule("/kotlin", view_func=kotlin_func)
routes.add_url_rule("/courses", view_func=all_courses)
routes.add_url_rule("/signup", view_func=signup,methods=[ 'POST'])
routes.add_url_rule("/users", view_func=get_all_users)
routes.add_url_rule("/tags_extractor", view_func=tags_extractor,methods=[ 'POST'])
routes.add_url_rule("/generate_qr", view_func=generate_qr_method,methods=[ 'POST'])
routes.add_url_rule("/conversion_rate", view_func=convert_currency,methods=[ 'POST'])
routes.add_url_rule("/ip_info", view_func=ip_info)
routes.add_url_rule("/domain_info", view_func=domain_info)


