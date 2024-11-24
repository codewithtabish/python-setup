from flask import Blueprint
from controllers import home, about, products, mobile_list, service, mood_checker, live_score,kotlin_func,all_courses





routes = Blueprint('routes', __name__)

routes.add_url_rule("/", view_func=home)
routes.add_url_rule("/about", view_func=about)
routes.add_url_rule("/products", view_func=products)
routes.add_url_rule("/mobiles", view_func=mobile_list)
routes.add_url_rule("/service", view_func=service)
routes.add_url_rule("/mood_checker", view_func=mood_checker)
routes.add_url_rule("/live_score", view_func=live_score)
routes.add_url_rule("/kotlin", view_func=kotlin_func)
routes.add_url_rule("/courses", view_func=all_courses)

