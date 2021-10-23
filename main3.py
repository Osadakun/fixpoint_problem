import datetime

def duration(start_time,end_time):      # 経過時間を返す関数
    start_year, end_year = int(start_time[0:4]), int(end_time[0:4])
    start_month, end_month = int(start_time[4:6]), int(end_time[4:6])
    start_day, end_day = int(start_time[6:8]), int(end_time[6:8])
    start_hour, end_hour = int(start_time[8:10]), int(end_time[8:10])
    start_min, end_min = int(start_time[10:12]), int(end_time[10:12])
    start_sec, end_sec = int(start_time[12:14]), int(end_time[12:14])
    dt1 = datetime.datetime(start_year,start_month,start_day,start_hour,start_min,start_sec)
    dt2 = datetime.datetime(end_year,end_month,end_day,end_hour,end_min,end_sec)
    return dt2 - dt1

def solve_problem():
    m = 3                                          # 平均を取る個数
    t = 2                                          # 平均時間
    f = open('log3.txt', 'r', encoding='UTF-8')
    data = [line.strip() for line in f.readlines()]    # 行要素を改行文字除去してリスト化
    for i in range(len(data)):
        data[i] = data[i].split(',')                   # 各行要素ごとに分ける(これで各要素に対してインデント指定でアクセスできる)
    for i in data:
        same_address = [j for j in data if i[0] < j[0] and (i[1] == j[1]) and j[2] != '-']    # タイムアウトが起きたサーバアドレスと同じサーバアドレスを取得(タイムアウトが起きた後のみ)
        if same_address == [] or len(same_address) < m:
            continue
        sum = 0
        for cnt in range(m):
            sum += int(same_address[cnt][2])
        avg = sum / m
        if avg >= t:
            time = duration(i[0], same_address[-1][0])
            print('故障状態のサーバアドレス：%s \n故障期間：%s' %(i[1],time))
    f.close()

solve_problem()