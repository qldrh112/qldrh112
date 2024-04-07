from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

csv_path = 'austin_weather.csv'
df = pd.DataFrame(pd.read_csv(csv_path))

# Create your views here.
def problem1(request):
    context = {
        'table': df.to_html(),
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    plt.plot(pd.to_datetime(df['Date']), df['TempHighF'], label='High Temperature')
    plt.plot(pd.to_datetime(df['Date']), df['TempAvgF'], label='Average Temperature') 
    plt.plot(pd.to_datetime(df['Date']), df['TempLowF'], label='Low Temperature')
    plt.title('Temperatuer Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.clf()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'img': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df['Date'] = pd.to_datetime(df['Date'])
    df3 = df.groupby(df['Date'].dt.strftime('%y-%m'))[['TempHighF', 'TempAvgF', 'TempLowF']].mean()

    plt.plot(pd.to_datetime(df3.index, format='%y-%m'), df3['TempHighF'], label='High Temperature')
    plt.plot(pd.to_datetime(df3.index, format='%y-%m'), df3['TempAvgF'], label='Average Temperature') 
    plt.plot(pd.to_datetime(df3.index, format='%y-%m'), df3['TempLowF'], label='Low Temperature')
    plt.title('Temperatuer Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.clf()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'img': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    x, y = [], []
    events = df['Events'].unique()
    events_cnt = df['Events'].value_counts()
    print('----------------')
    for event in events:
        if ',' in event:
            for elem in event.split(' , '):
                if elem in x:
                    idx = x.index(elem)
                    y[idx] += events_cnt[event]
                else:
                    x.append(elem)
                    y.append(events_cnt[event]) 
        else:
            if event in x:
                idx = x.index(event)
                y[idx] += events_cnt[event]
            elif event == ' ':
                x.append('No Events')
                y.append(events_cnt[event])
            else:
                x.append(event)
                y.append(events_cnt[event]) 

    y = list(map(lambda x:x+1, y))
    x1, y1 = [], []
    tmp = sorted(list(zip(y, x)))
    while tmp:
        yy, xx = tmp.pop()
        x1.append(xx)
        y1.append(yy)

    plt.bar(x1, y1)
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.clf()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'img': f'data:image/png;base64, {img_base64}',
    }
    return render(request, 'weathers/problem4.html', context)