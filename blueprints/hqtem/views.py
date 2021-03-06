from flask import request, render_template
from hqlf.blueprints.hqtem import hqteam


@hqteam.route("/info", methods=['GET'])
def info():
    page = request.args.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    return render_template('hqteam/HQteam_%d.html'%(page))