from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import random

# https://stackoverflow.com/questions/69845519/fastapi-interactive-plot-update-in-template-with-highcharts

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def dash(request: Request):
    total_users = 1234
    total_videos = 2345
    total_events = 432
    date_mapper_all = {"2021-06-13": [34, 111], "2021-06-14": [51, 321]} # video date, current day, total
    plot_1_data = [0] * 12 # month-wise data
    plot_2_cur = []
    plot_2_all = []
    plot_2_x = []
    cnt = 1
    for date, count in date_mapper_all.items():
        y, m, d = date.split('-')
        plot_1_data[int(m)-1] += count[0] # per day analysis
        plot_2_x.append(cnt)
        plot_2_cur.append(count[0])
        plot_2_all.append(count[1])
        cnt += 1

    plot_3_data = [total_videos, total_users, total_events]



    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "my random graph",
                                                        "users": total_users, "videos": total_videos, "events": total_events, "db_result": date_mapper_all,
                                                        "plot_1_data": plot_1_data, "plot_2_x": plot_2_x, "plot_2_cur": plot_2_cur, "plot_2_all": plot_2_all,
                                                        "plot_3_data": plot_3_data})


if __name__ == '__main__':
    uvicorn.run("main:app", port=80, host='0.0.0.0', reload = True)
