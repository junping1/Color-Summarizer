import requests
import re
import os
from pathlib import Path
import colorgram
import numpy as np
import pandas as pd
from multiprocessing import Pool
import multiprocessing
import webbrowser
from datetime import datetime, timedelta

img_color = []
pool_num = multiprocessing.cpu_count()


def get_folder_img_path(folder_path):
    paths = sorted(Path(folder_path).iterdir(), key=os.path.getmtime)
    path_list = ['/'.join(x.parts) for x in paths]
    filtered_path_list = list(filter(
        lambda name: '.png' in name or '.jpeg' in name or '.jpg' in name, path_list))
    return filtered_path_list


def extract_color(file_path):
    colors = colorgram.extract(file_path, 5)
    img_data = {}
    img_data["file"] = file_path
    img_data["color"] = []
    for color in colors:
        color_data = {}
        color_data["RGB"] = tuple([color_value for color_value in color.rgb])
        color_data['HEX'] = '#%02x%02x%02x' % tuple(
            [color_value for color_value in color.rgb])
        color_data["HSL"] = tuple([color_value for color_value in color.hsl])
        color_data["percentage"] = str(round(color.proportion * 100, 2)) + "%"
        img_data["color"].append(color_data)
    return img_data


def generate_result(img_color):
    style_html = '''<style>
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .img-info {
        padding: 10px;
    }

    img {
        height: 200px;
        padding-bottom: 10px;
    }

    table {
        display: none;
    }

    th,
    td {
        text-align: center;
        /* padding-left: 10px; */
        padding-right: 20px;
        text-align: center;
        padding: 5px;
    }

    .img-result {
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .color {
        height: 20px;
        width: 20px;
        border-radius: 50%;
    }

    .color-palette {
        display: flex;
        flex-direction: row;
        width: 100%;
        height: 20px;
    }

    .container {
        max-width: 1400px;
        margin: auto;
        display: grid;
        grid-gap: 4rem;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    }
    </style>'''

    result_list = []
    for img in img_color:
        color_palette = ''.join(['<div class="color-palette_color" style="background-color: ' + str(
            x['HEX'])+'; width: ' + str(x['percentage'])+';"></div>' for x in img['color']])
        table_info = ''.join(['<tr><td><div class="color" style="background-color: ' + str(x['HEX'])+';"></div></td><td>' + str(x['RGB']) +
                              '</td><td>' + str(x['HEX'])+'</td><td>' + str(x['HSL'])+'</td><td>' + str(x['percentage'])+'</td></tr>' for x in img['color']])
        img_info = '<div class="img-info"><img src="{}"></img><div class="color-palette">{}</div></div>'.format(
            img['file'], color_palette)
        table = '<table><tr><th>COLOR</th><th>RGB</th><th>HEX</th><th>HSL</th><th>PERCENT</th></tr>{}</table>'.format(
            table_info)
        img_result = '<div class="img-result">{}{}</div>'.format(
            img_info, table)
        result_list.append(img_result)

    output_html = style_html + '<div class="container">' + \
        str(''.join(result_list)) + '</div>'

    with open(str(input_path)[:-1] + "_result.html", "w") as output:
        output.write(output_html)

    r, g, b = [[], [], []]
    for each in [x['color'] for x in img_color]:
        r += ([x['RGB'][0] for x in each])
        g += ([x['RGB'][1] for x in each])
        b += ([x['RGB'][2] for x in each])

    rdata = np.array(r)
    gdata = np.array(g)
    bdata = np.array(b)

    dot_color = []
    for b, r, g in zip(bdata, rdata, gdata):
        dot_color += ["rgb({},{},{})".format(r, g, b)]

    color_df = pd.DataFrame({"b": bdata, "r": rdata, "g": gdata})

    import plotly.express as px
    fig = px.scatter_3d(color_df, x='b', y='r', z='g',
                        title="Summary of color palettes",
                        width=1000, height=1000
                        )

    fig.update_layout(
        scene=dict(
            xaxis_showspikes=False,
            yaxis_showspikes=False,
            zaxis_showspikes=False,
            xaxis=dict(nticks=2, range=[255, 0],
                       backgroundcolor='rgba(0,0,0,0)'),
            yaxis=dict(nticks=2, range=[0, 255],
                       backgroundcolor='rgba(0,0,0,0)'),
            zaxis=dict(nticks=2, range=[0, 255],
                       backgroundcolor='rgba(0,0,0,0)'),
            xaxis_title='BLUE',
            yaxis_title='RED',
            zaxis_title='GREEN',
        ),
    )

    fig.update_traces(marker=dict(color=dot_color))

    fig.write_html("color-3d.html", include_plotlyjs="cdn")

    with open("color-3d.html", "r") as color_3d:
        color_3d_html = color_3d.read()

    print(str(input_path)[:-1] + "_result.html")

    with open(str(input_path)[:-1] + "_result.html", "w") as output:
        output.write(color_3d_html + output_html)


if __name__ == '__main__':
    input_path = input(
        "Please enter the name of the folder you want to analyse: ") + '/'

    path_list = get_folder_img_path(input_path)[:]
    print("analysing {} pics...".format(len(path_list)))

    est_secs = 0.4 * 8 / pool_num * len(path_list)
    est_end_time = datetime.now() + timedelta(seconds=est_secs)
    print("est. completed time: {}, {} mins later!".format(
        est_end_time.strftime("%H:%M:%S"), round(est_secs/60, 2)))

    with Pool(pool_num) as p:
        img_color += p.map(extract_color, path_list)
        generate_result(img_color)
        print("✅ completed")
        result_path = str('file://' + os.getcwd()) + '/' + \
            str(input_path)[:-1] + "_result.html"
        print("check result at {}".format(result_path))
        webbrowser.open(result_path, new=2)
