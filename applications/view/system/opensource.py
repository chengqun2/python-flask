from flask import Blueprint, render_template, request

from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import str_escape
import requests
from bs4 import BeautifulSoup
from applications.models.opensource import Opensource
import json

bp = Blueprint('opensource', __name__, url_prefix='/opensource')


@bp.get('/')
def main():
    return render_template('system/opensource/main.html')


#   用户分页查询
@bp.get('/data')
@authorize("system:opensource:main")
def data():
    # 获取请求参数
    language = str_escape(request.args.get('language', type=str))
    if None == language:
        language = 'Python'
    list = get_list(language)
    return table_api(
        data=[{
            'project_name': opensource.project_name,
            'language': opensource.language,
            'watch': opensource.watch,
            'stars': opensource.stars,
            'fork': opensource.fork,
        } for opensource in list], count=len(list))


def get_list(language):
    cookies = {
        'BEC': '8ede56c7e7ea181fcd95cf3b7e5ea9fe',
        'Hm_lvt_24f17767262929947cc3631f99bfd274': '1700635796',
        'Hm_lpvt_24f17767262929947cc3631f99bfd274': '1700635796',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'BEC=8ede56c7e7ea181fcd95cf3b7e5ea9fe; Hm_lvt_24f17767262929947cc3631f99bfd274=1700635796; Hm_lpvt_24f17767262929947cc3631f99bfd274=1700635796',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
        'sec-ch-ua': '"Chromium";v="118", "Opera";v="104", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'skin': 'rec',
        'type': 'repository',
        'q': language,
        'sort': 'stars_count',
    }

    response = requests.get('https://search.gitee.com/', params=params, cookies=cookies, headers=headers)
    text = response.text
    bs = BeautifulSoup(text, "html.parser")
    projects = bs.select("#hits-list > .item")
    projectArray = []
    for project in projects:
        project_name2 = project.select(".header > .title > a")[0].text.strip()
        language2 = project.select(".attr > span.tag")[0].text.strip()
        watch2 = project.select(".attr > a.tag")[0].text.strip()
        stars2 = project.select(".attr > a.tag")[1].text.strip()
        fork2 = project.select(".attr > a.tag")[2].text.strip()
        opensource = Opensource(project_name2, language2, watch2, stars2, fork2)
        if len(projectArray) < 10 and language2 == language:
            projectArray.append(opensource)
    return projectArray
