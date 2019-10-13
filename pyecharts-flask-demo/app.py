from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar

import pymongo

app = Flask(__name__, static_folder="templates")
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = mongo_client['test']
countries = db['countries']
types = db['types']



def country_base() -> Bar:
    results0 = countries.find()
    dis0 = []
    for result in results0:
        dis0.append(result['distance'])
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=500, 
                    animation_easing="elasticOut",  # 延时动画效果
                    animation_duration_update=1000
                ),
            )
        )
        .add_xaxis(["中国", "美国"])
        .add_yaxis("评分差距", dis0)
        .set_global_opts(title_opts=opts.TitleOpts(title="国家"))
    )
    return c

def type_base() -> Bar:
    results1 = types.find()
    dis1 = []
    for result in results1:
        dis1.append(result['distance'])
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=500, 
                    animation_easing="elasticOut",  # 延时动画效果
                    animation_duration_update=1000
                ),
            )
        )
        .add_xaxis(["类型1", "类型2", "类型3", "类型4", "类型5"])
        .add_yaxis("评分差距", dis1)
        .set_global_opts(title_opts=opts.TitleOpts(title="国家"))
    )
    return c




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/countryChart")
def get_countryBar_chart():
    c = country_base()
    return c.dump_options_with_quotes()

@app.route("/typeChart")
def get_typeBar_chart():
    c = type_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()